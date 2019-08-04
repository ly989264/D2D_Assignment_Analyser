def get_lcs(string1, string2):
    string1_list=list(string1)
    string2_list=list(string2)
    lcs_list = []
    for i in range(len(string1_list)):
        flag = 0
        lcs = ''
        for j in range(i, len(string1_list)):
            for k in range(flag, len(string2_list)):
                if string1_list[j] == string2_list[k]:
                    lcs += string1_list[j]
                    flag = k + 1
        lcs_list.append((len(lcs), lcs))
    return sorted(lcs_list, reverse=True)


lcs_list = get_lcs("abcdef", "acxdefy");
print(lcs_list[0][1])