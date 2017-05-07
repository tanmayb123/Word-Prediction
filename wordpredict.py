import sys
import os

prime = sys.argv[1]
result = os.popen('python sample.py --save_dir saveemail --prime "' + prime  + '"').read()
print result.split("\n")[0].split(" ")[len(prime.split(" "))-1]

# "Watson Made " : Prime
# ["Watson", "Made", ""] : Length: 3
# Length - 1 = 2
# "..." : First Line : ["Watson", "Made", "Simple", ...][2] == "Simple"
