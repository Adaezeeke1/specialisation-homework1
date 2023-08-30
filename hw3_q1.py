from collections import deque

input_file = "hw3_q1.txt"
with open(input_file, "r") as f:
    lines = f.readlines()

queue = deque()

for line in lines:
    operation, person = line.strip().split()
    if operation == "JUMP":
        queue.appendleft(person)
    elif operation == "JOIN":
        queue.append(person)

print("Final queue order:")
for person in queue:
    print(person)


# Time and Space Complexity:
# Time Complexity:
#
# Reading the Input File: The time complexity of reading the input file line by line is O(n),
# where n is the number of lines in the file.
#
# Initializing the Queue: Initializing a deque has a constant time complexity, so it is O(1).
#
# Processing the Input: For each line in the input file, we perform the following operations:
# Splitting the line into words: This operation takes constant time as it involves iterating through the characters
# of the line and creating two substrings. Thus, it's O(1).
# Checking the operation type (JUMP or JOIN) and adding to the deque: These operations are constant time as well, O(1).
#
# Since we're processing 'x' lines, the time complexity of this part is O(x), where 'x' is the number of lines in the
# input file.
#
# Printing the Final Order: Looping through the queue and printing the names takes O(p) time, where 'p' is the number
# of people in the queue.
#
# When we add up these complexities, the overall time complexity is O(n + x + p).
#
# Space Complexity:
#
# Storing Input Data: We use memory to store the lines read from the input file. This memory consumption scales with
# the number of lines, which makes it O(n), where 'n' is the number of lines in the input file.
#
# Queue: The space used by the queue depends on the number of people in the queue. In the worst case, if all the people
# are added to the queue, it could be O(p), where 'p' is the number of people.
#
# When we add up these space complexities, the overall space complexity is O(n + p), where 'n' is the input data size
# and 'p' is the number of people in the queue.
#
# Assumptions:
#
# We assume that the input file follows a consistent format of the operation and name in pairs
# (e.g., "JUMP Amal", "JOIN Belle").
# We assume that the input data size (lines in the file and number of people) is not extremely large,
# such that it would cause memory or processing constraints.
# We assume that the deque operations provided by Python's collections module are implemented with optimal time
# complexity, such as O(1) for adding/removing elements from both ends.
