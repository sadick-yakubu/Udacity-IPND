"""
# Find substring function
def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

print(is_substring('dab', 'abracadabra'))

"""
"""
# Count substring function
def count_substring(string, target):
    index = 0
    total  = 0
    while index < len(string):
        if string[index:index+len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total
print(count_substring('love, love, love, all you need is love', 'love'))
print(count_substring("papa pony and the parcel post problem", "p"))
"""
"""
# Locate position of a substring
def locate_first(string, target):
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            return index
        index += 1
    return - 1

print(locate_first('cookbook', 'ook'))
print(locate_first('all your bass are belong to us', 'base'))
"""
import time

n = 10
while n > 0:
    print(n)
    time.sleep(2)
    n -= 1

print("Blastoff!")