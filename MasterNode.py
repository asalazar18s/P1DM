'''
| Master Node |
Will control the division of the txt
Send to each of the MAP nodes the excerpt
MAP Node sends info of size and location of results
info is sent to REDUCE Node.
'''


def ReadText():
    '''
    Gets txt file and separates given the value of lines
    Starts the threading process?? or separate method to handle and initiate that process??
    '''

    linePlaceHolder = []

    file = open("aaa.txt")
    lines = file.readlines()

    line_counter = 2
    line_divider = int(len(lines) / 2)
    print(line_divider)
    while line_divider >0:
        print(line_divider)
        line_divider = line_divider - 1



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
