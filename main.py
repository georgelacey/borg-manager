from sys import stdin

borg_output = stdin.readlines()

attributes = {  "Archive name: " : "",
                "Archive fingerprint: " : "",
                "Time (start): " : "",
                "Duration: " : "",
                "Number of files: " : "", }
                
#archive_name, archive_fingerprint, time_start, duration, file_count

for i in range(0, len(borg_output)):
    
    for key in attributes:
        if borg_output[i].startswith(key):
            attributes[key] = borg_output[i] \
            .strip(key) \
            .strip("\n")

output = open("borg.txt", "w")

for key, value in attributes.iteritems():
    output.write("%s%s\n" % (key, value))

output.close()
