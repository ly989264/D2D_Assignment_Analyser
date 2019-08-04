import matplotlib.pyplot as plt

# with open("file5.txt", "r") as f:
#     string = f.readline()

threshold = 0

def generator(a, b, c, d, e, f):
    if not check_noise([a, b, c, d, e, f]):
        return -1
    if a>b and a>c and a>d and a>e and a>f:
        return 0
    if b>a and b>c and b>d and b>e and b>f:
        return 1
    if c>a and c>b and c>d and c>e and c>f:
        return 2
    if d>a and d>b and d>c and d>e and d>f:
        return 3
    if e>a and e>b and e>c and e>d and e>f:
        return 4
    return 5


def check_noise(arr):
    global threshold
    for each in arr:
        if each > threshold:
            return True
    return False


def process_data(arr):
    # define variables
    temp_long = 0
    for i in range(40):
        if arr[i][0] > temp_long:
            temp_long = arr[i][0]
    global threshold
    threshold = temp_long * 0.03
    print(threshold)
    res = []
    for each_arr in arr:
        if check_noise(each_arr):
            res.append(generator(each_arr[0], each_arr[1], each_arr[2], each_arr[3]))
        else:
            res.append(-1)
    # cnt_max = 3
    # cnt_min = 1
    # cnt = 0
    # prev_pos = None
    # current_index = 0
    # clear_flag = False
    # second_res = []
    # # modified here
    # pos1 = None
    # pos2 = None
    # pos1_cnt = 0
    # pos2_cnt = 0
    # last_append = None
    # # modify end
    # # 0 -> clearh
    # # 1 -> clearl
    # # 2 -> high
    # # 3 -> low
    # print(res)
    # tmp = [str(i) for i in res]
    # tmp_v2 = "".join(tmp).split("-1")
    # tmp_v3 = []
    # for each in tmp_v2:
    #     if each == '':
    #         continue
    #     tmp_v3.append(each)
    # print(tmp_v3)
    # for current_index in range(len(res)):
    #     # modified here
    #     # if not clear_flag:
    #     #     if res[current_index] == -1:
    #     #         continue
    #     #     if res[current_index] == 0:
    #     #         clear_flag = True
    #     #         cnt += 1
    #     #         prev_pos = 0
    #     #         continue
    #     #     continue
    #     if prev_pos is None and res[current_index] != -1:
    #         prev_pos = res[current_index]
    #         cnt = 1
    #     # modify end and below
    #     elif res[current_index] == prev_pos:
    #         # modified here!
    #         if cnt > cnt_max:
    #             second_res.append(prev_pos)
    #             cnt = 1
    #         else:
    #             cnt += 1
    #         # modify end
    #     elif res[current_index] == -1:
    #         # modified here
    #         if pos1 is not None:
    #             if pos1_cnt == pos2_cnt and pos1_cnt == 1:
    #                 if last_append is not None:
    #                     second_res.append(last_append)
    #                 else:
    #                     second_res.append(pos2)  # arbitrary
    #             elif pos1_cnt == pos2_cnt:
    #                 print("Oops")
    #                 second_res.append(pos1)
    #                 second_res.append(pos2)
    #             elif pos1_cnt > pos2_cnt and pos2_cnt == 2:
    #                 second_res.append(pos1)
    #                 second_res.append(pos2)
    #             elif pos2_cnt > pos1_cnt and pos1_cnt == 2:
    #                 second_res.append(pos1)
    #                 second_res.append(pos2)
    #             elif pos1_cnt > pos2_cnt:
    #                 second_res.append(pos1)
    #             else:
    #                 second_res.append(pos2)
    #             pos1 = None
    #             pos2 = None
    #             pos1_cnt = 0
    #             pos2_cnt = 0
    #             last_append = None
    #             cnt = 0
    #             continue
    #         if cnt != 0:
    #             second_res.append(prev_pos)
    #             prev_pos = None
    #             cnt = 0
    #         # modify end
    #     else:
    #         # modified here
    #         if pos1 is not None:
    #             if pos1 == res[current_index]:
    #                 pos1_cnt += 1
    #                 if pos1_cnt > cnt_max:
    #                     second_res.append(pos1)
    #                     last_append = pos1
    #                     pos1_cnt = 1
    #             elif pos2 == res[current_index]:
    #                 pos2_cnt += 1
    #                 if pos2_cnt > cnt_max:
    #                     second_res.append(pos2)
    #                     last_append = pos2
    #                     pos2_cnt = 1
    #             else:
    #                 continue
    #         else:
    #             pos1 = prev_pos
    #             pos2 = res[current_index]
    #             pos1_cnt = cnt
    #             pos2_cnt = 1
    #         cnt += 1
    #         # modify end
    # print(second_res)

    cnt_max = 3
    cnt_min = 1
    cnt = 0
    prev_pos = None
    current_index = 0
    clear_flag = False
    second_res = []
    # modified here
    pos1 = None
    pos2 = None
    pos1_cnt = 0
    pos2_cnt = 0
    last_append = None
    # modify end
    # 0 -> clearh
    # 1 -> clearl
    # 2 -> high
    # 3 -> low
    print("res:")
    print(res)
    tmp = [str(i) for i in res]
    tmp_v2 = "".join(tmp).split("-1")
    tmp_v3 = []
    for each in tmp_v2:
        if each == '':
            continue
        tmp_v3.append(each)
    print(tmp_v3)
    for current_index in range(len(res)):
        # modified here
        # if not clear_flag:
        #     if res[current_index] == -1:
        #         continue
        #     if res[current_index] == 0:
        #         clear_flag = True
        #         cnt += 1
        #         prev_pos = 0
        #         continue
        #     continue
        if prev_pos is None and res[current_index] != -1:
            prev_pos = res[current_index]
            cnt = 1
        # modify end and below
        elif res[current_index] == prev_pos:
            # modified here!
            if cnt > cnt_max:
                second_res.append(prev_pos)
                cnt = 1
            else:
                cnt += 1
            # modify end
        elif res[current_index] == -1:
            # modified here
            # if pos1 is not None:
            #     if pos1_cnt == pos2_cnt and pos1_cnt == 1:
            #         if last_append is not None:
            #             second_res.append(last_append)
            #         else:
            #             second_res.append(pos2)  # arbitrary
            #     elif pos1_cnt == pos2_cnt:
            #         print("Oops")
            #         second_res.append(pos1)
            #         second_res.append(pos2)
            #     elif pos1_cnt > pos2_cnt and pos2_cnt == 2:
            #         second_res.append(pos1)
            #         second_res.append(pos2)
            #     elif pos2_cnt > pos1_cnt and pos1_cnt == 2:
            #         second_res.append(pos1)
            #         second_res.append(pos2)
            #     elif pos1_cnt > pos2_cnt:
            #         second_res.append(pos1)
            #     else:
            #         second_res.append(pos2)
            #     pos1 = None
            #     pos2 = None
            #     pos1_cnt = 0
            #     pos2_cnt = 0
            #     last_append = None
            #     cnt = 0
            #     continue
            if cnt != 0:
                second_res.append(prev_pos)
                prev_pos = None
                cnt = 0
            # modify end
        else:
            # modified here
            # if pos1 is not None:
            #     if pos1 == res[current_index]:
            #         pos1_cnt += 1
            #         if pos1_cnt > cnt_max:
            #             second_res.append(pos1)
            #             last_append = pos1
            #             pos1_cnt = 1
            #     elif pos2 == res[current_index]:
            #         pos2_cnt += 1
            #         if pos2_cnt > cnt_max:
            #             second_res.append(pos2)
            #             last_append = pos2
            #             pos2_cnt = 1
            #     else:
            #         continue
            # else:
            if cnt > 1:
                second_res.append(prev_pos)
            cnt = 1
            prev_pos = res[current_index]
            # modify end
    print(second_res)

    cnt = 0
    for each in second_res:
        if each==3:
            print("0", end="")
            cnt += 1
        if each==2:
            print("1", end="")
            cnt += 1
        if cnt == 8:
            print(" ", end="")
            cnt = 0
    print()





result_clearh = []
result_clearl = []
result_high = []
result_low = []
result_high2 = []
result_low2 = []
arr = []
ft = open("data8_res.txt", "w")
tmp_min = 0
with open("data8.txt", "r") as f:
    for each_line in f:
        temp_arr = each_line.split(" ")
        if int(temp_arr[0]) > tmp_min:
            tmp_min = int(temp_arr[0])
    threshold = tmp_min * 0.03
with open("data8.txt", "r") as f:
    for each_line in f.readlines():
        temp_arr = each_line.split(" ")
        print(generator(int(temp_arr[0]), int(temp_arr[1]), int(temp_arr[2]), int(temp_arr[3]), int(temp_arr[4]), int(temp_arr[5])), file=ft)
        result_clearh.append(int(temp_arr[0]))
        result_clearl.append(int(temp_arr[1]))
        result_high.append(int(temp_arr[2]))
        result_low.append(int(temp_arr[3]))
        result_high2.append(int(temp_arr[4]))
        result_low2.append(int(temp_arr[5]))
        temp_arr[0] = int(temp_arr[0])
        temp_arr[1] = int(temp_arr[1])
        temp_arr[2] = int(temp_arr[2])
        temp_arr[3] = int(temp_arr[3])
        arr.append(temp_arr)
index = [i for i in range(len(result_clearh))]
plt.plot(index, result_clearh)
plt.plot(index, result_clearl)
plt.plot(index, result_high)
plt.plot(index, result_low)
plt.plot(index, result_high2)
plt.plot(index, result_low2)
plt.title("Data Transfer")
plt.show()
ft.close()
# with open("data7_res.txt", "r") as f:
#     arr = []
#     for each_line in f.readlines():
#         each_line = each_line.rstrip('\n')
#         temp_arr = each_line.split(" ")
#         if temp_arr[0] == "1":
#             arr.append(0)
#         if temp_arr[1] == "1":
#             arr.append(1)
#         if temp_arr[2] == "1":
#             arr.append(2)
#         if temp_arr[3] == "1":
#             arr.append(3)
#     # clear_flag = True
#     # clear_cnt_num = None
#     # cnt = 0
#     # prev = None
#     # last_prev = None
#     # for index in range(len(arr)):
#     #     if arr[index] == 0:
#     print(arr)
# process_data(arr)