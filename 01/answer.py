import os

with open(os.path.join(os.getcwd(),'01\\inputs\\input_list.txt')) as f:
    text = f.read()

lines = text.strip().split('\n')
list_1, list_2 = [], []

for line in lines:
    number_1, number_2 = map(int, line.split())
    list_1.append(number_1)
    list_2.append(number_2)

list_1.sort()
list_2.sort()

differences = [abs(list_2[i] - list_1[i]) for i in range(len(list_1))]
print("Part 1 Answer:", sum(differences))


similarity_score = 0
for number_1 in list_1:
    occurences = sum(1 for number_2 in list_2 if number_1 == number_2)
    instance_score = number_1 * occurences
    similarity_score += instance_score

print("Part 2 Answer:", similarity_score)
