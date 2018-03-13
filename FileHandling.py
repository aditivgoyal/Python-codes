"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = ["first string", "Second string", "Third string"]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

my_file = open("firstfile.txt", "r")
print(str(my_file.read()))
my_file.close()

my_file = open("firstfile.txt", "r")
for line in my_file:
    print(line)
# for line in my_file.readlines():
#     print(line)
my_file.close()
