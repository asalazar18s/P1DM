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


    #opens file and reads lines into list
    file = open("alice29.txt")
    lines = file.readlines()

    #gets number of nodes to be processed
    line_divider = int(len(lines) / 25)
    #print(line_divider)

    #appends group of 25 lines to list
    listOfLines = []
    for groupOfLines in lines:
        listOfLines.append(lines[:24])
        lines[:24] = []

        #abrir un fichero con las lineas dentro del for

    #checks for remaining lines after
    if len(lines) > 0:
        listOfLines.append(lines)

    print len(listOfLines)
    #print listOfLines[145]

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


def MapNode(list = [], *args):
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
