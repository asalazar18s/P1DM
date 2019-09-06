'''
| Master Node |
Will control the division of the txt
Send to each of the MAP nodes the excerpt
MAP Node sends info of size and location of results
info is sent to REDUCE Node.
'''

from threading import Thread


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




    '''
    myThreads = []
    for i in range(6):
        thread = Thread(target = MapNode, args = (listOfLines[i]))
        thread.start()
        myThreads.append(thread)
        listOfLines.pop(i)

    #checks each thread and passes 25 new lines if thread is NOT alive, this keeps 6 threads running all the time.
    while listOfLines > 0:
        for thread in myThreads:
            if thread.isAlive():
                continue
            else:
                newThread = Thread(target = MapNode, args = (listOfLines[0]))
                newThread.start()
                myThreads.remove(thread)
                myThreads.append(newThread)
                listOfLines.pop(0)
    '''

def MapNode(list):
    print(list[0])

        # with open("aaa.txt", newline=None) as f:
        # for line_terminated in f.readlines():
        #     # get rid of newline character
        #     line = line_terminated.rstrip('\n')
        #     # if the line is not empty process it
        #     if len(line) > 0:
        #         # add the line to the list used as placeholder
        #         linePlaceHolder.append(line)
        #         if len(linePlaceHolder) == 2:
        #             # what to do here once you have the max lines you want
        #             print(linePlaceHolder)
        #             linePlaceHolder.clear()


ReadText()
