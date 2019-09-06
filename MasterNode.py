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
    else:
        for groupOfLines in range(6):
            if groupOfLines != 5:
                listOfLines.append(main_file_lines[:int(line_divider)])
                main_file_lines[:int(line_divider)] = []
                newfile = open("node" + str(groupOfLines) + ".txt", "w+")
                for val in range(int(line_divider)):
                    newfile.write(listOfLines[groupOfLines][val])
            else:
                listOfLines.append(main_file_lines[:])
                main_file_lines[:] = []
                newfile = open("node" + str(groupOfLines) + ".txt", "w+")
                for line in range(len(listOfLines[-1])):
                    newfile.write(listOfLines[-1][line])

    ThreadCoordinator()


def ThreadCoordinator():
    '''
    No parameters
    launch a thread per file
    '''
    for i in range(6):
        thread = Thread(target=MapNode, args=[i])
        thread.start()


def MapNode(fileNumber):
    '''
    This method will be called by each thread to handle each file
    Do the Map part of algorithm
    Should this method receive a parameter?
    :return: nothing? the new files with this part of the algorithm solved?
    '''
    # print(str(fileNumber) + " this file")
    processed_file = open("node" + str(fileNumber) + ".txt")
    lines_to_process = processed_file.readlines()

    newfile = open("Map" + str(fileNumber) + ".txt", "w+")
    #set up a data structure to hold values.
    value_holder = []
    with open("node" + str(fileNumber) + ".txt", newline=None) as f:
        for line_terminated in f.readlines():
            # get rid of newline character
            line = line_terminated.rstrip('\n')
            # if the line is not empty process it
            if len(line) > 0:
                print(str(fileNumber) + " " + line)
                #create an individual list per line that separates strings by space character
                word_list = line.split(" ")
                for word in word_list:
                    #get rid of ( , . ! ? )
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    value_holder.append((word, 1))

    for value in value_holder:
        newfile.write(str(value))

    # just a checker
    # if fileNumber == 0:
    #    print(value_holder)









ReadText()

