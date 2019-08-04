def to_binary(i):
    res = ""
    for index in range(4):
        if i >= 2 ** (3-index):
            i -= 2** (3-index)
            res += "1"
        else:
            res += "0"
    return res

def calculate_difference(i, j):
    cnt = 0
    for index in range(4):
        if i[index] != j[index]:
            cnt += 1
    return cnt

raw_arr = [ to_binary(i) for i in range(16)]

# print("    ", end="  ")
# for each in raw_arr:
#     print(each, end="  ")
# print()

dict = {}

# for i in raw_arr:
#     print(i, end="  ")
#     for j in raw_arr:
#         print(" "+str(calculate_difference(i, j))+"  ", end="  ")
#     print()

res = []
for a in range(len(raw_arr)):
    for b in range(a+1, len(raw_arr)):
        for c in range(b+1, len(raw_arr)):
            for d in range(c+1, len(raw_arr)):
                arr = [calculate_difference(raw_arr[a], raw_arr[b]), calculate_difference(raw_arr[a], raw_arr[c]), calculate_difference(raw_arr[a], raw_arr[d]),
                       calculate_difference(raw_arr[b], raw_arr[c]), calculate_difference(raw_arr[b], raw_arr[d]), calculate_difference(raw_arr[c], raw_arr[d])]
                res.append([raw_arr[a], raw_arr[b], raw_arr[c], raw_arr[d], min(arr)])
res.sort(key=lambda x: x[4], reverse=True)
print(res[0])
max_value = res[0][4]
for each in res:
    if each[4] < max_value:
        break
    for raw_data in raw_arr:
        if (calculate_difference(raw_arr, each[0]) != calculate_difference(raw_arr, each[1]) and
        calculate_difference(raw_arr, each[0]) != calculate_difference(raw_arr, each[2]) and
        calculate_difference(raw_arr, each[0]) != calculate_difference(raw_arr, each[3]) and
        calculate_difference(raw_arr, each[1]) != calculate_difference(raw_arr, each[2]) and
        calculate_difference(raw_arr, each[1]) != calculate_difference(raw_arr, each[3]) and
        calculate_difference(raw_arr, each[2]) != calculate_difference(raw_arr, each[3])):
            print(each)

selected = ["0000", "0011", "0101", "0110"]
for each in raw_arr:
    print(each, end="  ")
    print(calculate_difference(each, selected[0]), end="  ")
    print(calculate_difference(each, selected[1]), end="  ")
    print(calculate_difference(each, selected[2]), end="  ")
    print(calculate_difference(each, selected[3]))