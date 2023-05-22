import time
import sys

start_time = time.time()
relation_name = "kosarak"

print("Args: ",sys.argv[1])
file_path = sys.argv[1]

inputFile = open(file_path, 'r')
outputFile = open('parsed_p2.arff', 'w')

num_lines = len(inputFile.readlines())
outputFile.write("@RELATION " + relation_name + "\n\n")

for i in range(41270):
    outputFile.write("@ATTRIBUTE " + "news" + str(i) + " {0,1}\n")

outputFile.write("\n@DATA\n")

inputFile = open('Kosarak.dat', 'r')
for line in inputFile:
    clicks = line.strip().split(" ")
    parsed_line_str = "{"
    click_set = set()
    sorted_list = []
    for click in clicks:
        click_int_reindexed = int(click) - 1;
        click_set.add(click_int_reindexed)

    sorted_list.extend(click_set)
    sorted_list.sort()
    for click in sorted_list:
        parsed_line_str += str(click) + " 1,"

    final_str = parsed_line_str[:len(parsed_line_str)-1] + "}\n"
    outputFile.write(final_str)
    # print("parsed line: ", final_str)

print("num lines: ", num_lines)
print("--- %s seconds ---" % (time.time() - start_time))