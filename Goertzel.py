import math
import numpy as np
import matplotlib.pyplot as plt

def seq_generator():
    duration = 1
    sampleRate = 2000
    numSamples = duration * sampleRate
    sample = []
    frequency = 400
    generated = []

    for i in range(numSamples):
        sample.append(math.sin(2 * math.pi * i / (sampleRate/frequency)))
    for each in sample:
        val = each * 32767
        generated.append()
    tmp_sample = sample[1000:1050]
    plt.plot(tmp_sample)
    plt.show()

# seq_generator()
# with open("data.txt", "r") as f:
#     string = f.readline()
# arr = string.split(" ")
# result_arr = []
# index=[i for i in range(100, 20000, 70)]
# for each in arr:
#     if each != '':
#         print(each)
#         result_arr.append(int(each))
# print(len(result_arr))
# print(len(index))
# plt.plot(index, result_arr)
# # plt.plot(result_arr)
# plt.show()

# with open("data2.txt", "r") as f:
#     string = f.readline()
# arr = string.split(" ")
# result_arr = []
# index=[i for i in range(450-150, 450+150, 2)]
# for each in arr:
#     if each != '':
#         result_arr.append(int(each))
# print(len(result_arr))
# print(len(index))
# plt.plot(index, result_arr)
# plt.show()

# index = [i for i in range(1,19)]
# # out = open("data.csv", "w")
# cnt = 0
# with open("data.txt", "r") as f:
#     for each_line in f.readlines():
#         arr = each_line.split(" ");
#         result_arr = []
#         current_max = int(arr[0])
#         current_pos = 0
#         previous_max = int(arr[0])
#         previous_pos = 0
#         for each in arr:
#             if each != '\n':
#                 result_arr.append(int(each))
#         for i in range(0,18):
#             if result_arr[i] > current_max:
#                 previous_max = current_max
#                 previous_pos = current_pos
#                 current_max = result_arr[i]
#                 current_pos = i
#             elif result_arr[i] > previous_max:
#                 previous_max = result_arr[i]
#                 previous_pos = i
#         print(f"{int(cnt/2)+1}: {current_pos+1}<=>{current_max}    {previous_pos+1}<=>{previous_max}    diff: {current_max-previous_max}   {previous_max*100/current_max:.2f}%  {(current_max-previous_max)*100/current_max:.2f}%")
#         cnt+=1
#         # print(len(result_arr))
#         # print(len(index))
#         # plt.plot(index, result_arr)
#         # plt.show()
#
# print("**********")
#
# # find the threshold
# with open("data.txt", "r") as f:
#     result_td = []
#     for each_line in f.readlines():
#         arr = each_line.split(" ");
#         result_arr = []
#         current_max = int(arr[0])
#         current_pos = 0
#         previous_max = int(arr[0])
#         previous_pos = 0
#         for each in arr:
#             if each != '\n':
#                 result_arr.append(int(each))
#         result_td.append(result_arr)
#     for i in range(0, 18):
#         tmp_arr = []
#         for each_arr in result_td:
#             tmp_arr.append(each_arr[i])
#         tmp_arr.sort(reverse=True)
#         print(f"Line {i+1}: {tmp_arr[0]}   {tmp_arr[1]}   {tmp_arr[2]}    {tmp_arr[2]*100/tmp_arr[1]:2f}%")
#
# print("**********")
#
# with open("high_9.txt", "r") as f:
#     for each_line in f.readlines():
#         cnt = 0
#         arr = each_line.split(" ");
#         result_arr = []
#         current_max = int(arr[0])
#         current_pos = 0
#         previous_max = int(arr[0])
#         previous_pos = 0
#         for each in arr:
#             if each != '\n':
#                 result_arr.append(int(each))
#         for i in range(0,18):
#             if result_arr[i] > current_max:
#                 previous_max = current_max
#                 previous_pos = current_pos
#                 current_max = result_arr[i]
#                 current_pos = i
#             elif result_arr[i] > previous_max:
#                 previous_max = result_arr[i]
#                 previous_pos = i
#         print(f"{int(cnt/2)+1}: {current_pos+1}<=>{current_max}    {previous_pos+1}<=>{previous_max}    diff: {current_max-previous_max}   {previous_max*100/current_max:.2f}%  {(current_max-previous_max)*100/current_max:.2f}%")
#         cnt+=1
#
# print("**********")
#
# with open("debugger.txt", "r") as f:
#     for each_line in f.readlines():
#         cnt = 0
#         arr = each_line.split(" ");
#         result_arr = []
#         current_max = 0
#         current_pos = 0
#         previous_max = 0
#         previous_pos = -1
#         for each in arr:
#             if each != '\n':
#                 result_arr.append(int(each))
#         for i in range(0,18):
#             if result_arr[i] > current_max:
#                 previous_max = current_max
#                 previous_pos = current_pos
#                 current_max = result_arr[i]
#                 current_pos = i
#             elif result_arr[i] > previous_max:
#                 previous_max = result_arr[i]
#                 previous_pos = i
#         print(f"{int(cnt/2)+1}: {current_pos+1}<=>{current_max}    {previous_pos+1}<=>{previous_max}    diff: {current_max-previous_max}   {previous_max*100/current_max:.2f}%  {(current_max-previous_max)*100/current_max:.2f}%")
#         cnt+=1

with open("data.txt", "r") as f:
    result_arr = f.readline().split(" ")
    fr = []
    for each in result_arr:
        if each != '' and each != '\n':
            fr.append(int(each))
    plt.plot(fr)
    plt.show()