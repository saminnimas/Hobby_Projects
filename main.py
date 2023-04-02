sample_dic = {}
sample_or_manual = input("Do you want to use a) sample mode, or b) Manual mode:\nwrite either a or b\n")

if sample_or_manual.lower() == "a":
    sample = open('C:\\Users\\SkyN3\\OneDrive\\Documents\\tictactoe samples.txt', "r") # use the directory where the tictactoe samples.txt file is stored
    for i in range(9): # there are 9 separate lines in the text file; thus range 9.
        lines = sample.readline()
        position, move = lines.split()
        move = move.strip()
        sample_dic[position] = move

    j = 0
    for k, v in sample_dic.items():
        if v == '-':
            sample_dic[k] = str(j)
            j += 1
        # initially vacant positions after the game are represented as '-'; but multiple
        # adjacent '-'s might end up printing winner so the '-' occurrences are changed to nums

    print(sample_dic['topl'] + '|' + sample_dic["topm"] + "|" + sample_dic['topr'])
    print("-+-+-")
    print(sample_dic['midl'] + '|' + sample_dic["midm"] + "|" + sample_dic['midr'])
    print('-+-+-')
    print(sample_dic['botl'] + '|' + sample_dic["botm"] + "|" + sample_dic['botr'])
    print()

    if sample_dic["topl"] == sample_dic['topm'] == sample_dic["topr"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["topl"] == sample_dic['midl'] == sample_dic["botl"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["topl"] == sample_dic['midm'] == sample_dic["botr"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["topm"] == sample_dic['midm'] == sample_dic["botm"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["topr"] == sample_dic['midr'] == sample_dic["botr"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["midl"] == sample_dic['midm'] == sample_dic["midr"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["botl"] == sample_dic['botm'] == sample_dic["botr"]:
        print("WE HAVE A WINNER!!")

    elif sample_dic["topr"] == sample_dic['midm'] == sample_dic["botl"]:
        print("WE HAVE A WINNER!!")

    else:
        print("-_- DRAW -_-")

elif sample_or_manual.lower() == 'b':
    print("Option b under construction")

else:
    print('CAN YOU READ?')
# print(sample_dic)
# the numbers on the grid represents the vacancy of the grid.
