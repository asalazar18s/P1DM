'''
| Master Node |
Will control the division of the txt
Send to each of the MAP nodes the excerpt
MAP Node sends info of size and location of results
info is sent to REDUCE Node.
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
'''

from threading import Thread
import string
import re

Dictionary1 = {}
Dictionary2 = {}


def ReadText():
    '''
    Gets txt file and separates given the value of lines
    Starts the threading process?? or separate method to handle and initiate that process??
    '''
    # maybe refactor code so that all the "new file" generation fits in one method...
    # opens file and reads lines into list
    main_file = open("alice29.txt")
    main_file_lines = main_file.readlines()

    # gets number of nodes to be processed
    line_divider = (len(main_file_lines) / 6)

    listOfLines = []
    if line_divider.is_integer():
        for groupOfLines in range(6):
            listOfLines.append(main_file_lines[:int(line_divider)])
            main_file_lines[:int(line_divider)] = []
            newfile = open("node" + str(groupOfLines) + ".txt", "w+")
            for val in range(int(line_divider)):
                newfile.write(listOfLines[groupOfLines][val])
            newfile.close()
    else:
        for groupOfLines in range(6):
            if groupOfLines != 5:
                listOfLines.append(main_file_lines[:int(line_divider)])
                main_file_lines[:int(line_divider)] = []
                newfile = open("node" + str(groupOfLines) + ".txt", "w+")
                for val in range(int(line_divider)):
                    newfile.write(listOfLines[groupOfLines][val])
                newfile.close()
            else:
                listOfLines.append(main_file_lines[:])
                main_file_lines[:] = []
                newfile = open("node" + str(groupOfLines) + ".txt", "w+")
                for line in range(len(listOfLines[-1])):
                    newfile.write(listOfLines[-1][line])
                newfile.close()

    ThreadCoordinator()


def ThreadCoordinator():
    '''
    No parameters
    launch a thread per file for map
    hold for them to finish
    launch shuffle threads.
    '''
    for i in range(6):
        thread = Thread(target=MapNode, args=[i])
        thread.start()
        thread.join()

    print("All Map threads done")

    ShuffleNode()

    for i in range(2):
        number = i+1
        node = "Shuffle" + str(number) + ".txt"
        thread = Thread(target=ReduceNode, args=(node,))
        thread.start()
        thread.join()

    print("All reduce threads are done")



def MapNode(fileNumber):
    '''
    This method will be called by each thread to handle each file
    Do the Map part of algorithm
    Should this method receive a parameter?
    :return: nothing? the new files with this part of the algorithm solved?
    '''

    # set up a data structure to hold values.
    value_holder = []
    with open("node" + str(fileNumber) + ".txt") as f:
        for line_terminated in f.readlines():
            # get rid of newline character
            line = line_terminated.rstrip('\n')
            # if the line is not empty process it
            if len(line) > 0:
                # print(str(fileNumber) + " " + line)
                # create an individual list per line that separates strings by space character
                word_list = line.split(" ")
                for word in word_list:
                    # get rid of ( , . ! ? )
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    word = word.lower()
                    value_holder.append((word, 1))

    newfile = open("Map" + str(fileNumber) + ".txt", "w+")
    for value in value_holder:
        newfile.write(str(value) + ":")

def ShuffleNode():
    '''
    this node will add up all the values up into one file? 2 files? one per file?
    create two tuples maybe? return that to the thread coordinator to launch two threads to reduce?
    :return: two touples
    ME ESTA BOTANDO LOS ULTIMOS DICCIONARIOS VACIOS
    '''

    validator_list_A = list(string.ascii_lowercase[0:13])
    validator_list_B = list(string.ascii_lowercase[13:])

    a_to_m_dict = {}
    n_to_z_dict = {}

    for val in range(6):
        file_to_process = open("Map" + str(val) + ".txt")
        tuples_to_process = file_to_process.readlines()
        tuples_to_process = tuples_to_process[0].split(":")
        tuples_to_process.pop(-1)

        for element in tuples_to_process:
            element_to_process = element.split(",")
            element_to_process = element_to_process[0]
            element_to_process = element_to_process.translate(str.maketrans('', '', string.punctuation))
            if len(element_to_process) > 0:
                if element_to_process[0] in validator_list_A:
                    if element_to_process in a_to_m_dict:
                        a_to_m_dict[element_to_process].append(1)
                    else:
                        a_to_m_dict[element_to_process] = [1]

                elif element_to_process[0] in validator_list_B:
                    if element_to_process in n_to_z_dict:
                        n_to_z_dict[element_to_process].append(1)
                    else:
                        n_to_z_dict[element_to_process] = [1]
        file_to_process.close()


    newfile1 = open("Shuffle1.txt", "w+")
    newfile1.write(str(a_to_m_dict))
    newfile2 = open("Shuffle2.txt", "w+")
    newfile2.write(str(n_to_z_dict))
    newfile1.close()


def ReduceNode(txtNode):
    """

    :param txtNode: Shuffle node to reduce
    :return: reduced nodes
    """
    dictionary = {}
    file_to_reduce = open(txtNode)
    values_to_reduce = file_to_reduce.readlines()
    values_to_reduce = values_to_reduce[0].split("],")
    for element in values_to_reduce:
        element_to_reduce = element.split(":")
        number_to_reduce = element_to_reduce[1]
        number_to_reduce = number_to_reduce.translate(str.maketrans('', '', string.punctuation))
        number_to_reduce = number_to_reduce.strip()
        number_to_reduce = re.sub("\s+", ",", number_to_reduce.strip())
        number_to_reduce = [int(x) for x in number_to_reduce.split(',')]
        element_to_reduce = element_to_reduce[0]
        element_to_reduce = element_to_reduce.translate(str.maketrans('','', string.punctuation))
        dictionary.update({element_to_reduce:len(number_to_reduce)})

    newfile1 = open("Reduced.txt", "a+")
    if txtNode == "Shuffle1.txt":
        Dictionary1 = dictionary
        newfile1.write(str(Dictionary1))
    if txtNode == "Shuffle2.txt":
        Dictionary2 = dictionary
        newfile1.write(str(Dictionary2))


ReadText()

