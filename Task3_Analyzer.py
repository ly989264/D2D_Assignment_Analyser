import matplotlib.pyplot as plt

# find the 1st, 2nd and 3rd
with open("data4.txt", "r") as f:
    for each_line in f.readlines():
        result_arr = each_line.split(" ")
        fr = []
        for each in result_arr:
            if each != '' and each != '\n':
                fr.append(int(each))
        fr.sort(reverse=True)
        print(f"{fr[1]*100/fr[0]:6.2f}% {fr[2]*100/fr[0]:6.2f}% {fr[2]*100/fr[1]:6.2f}%")
