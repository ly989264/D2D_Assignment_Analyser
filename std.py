def hash_func(a, b):
    return a * 31 + b * 51

string = "ly989264@gmail.com"
bits = []
for each in string:
    temp = ord(each)
    for i in range(0,8):
        if (temp >= 2**(7-i)):
            temp -= 2**(7-i)
            bits.append(1)
        else:
            bits.append(0)
result = []
for i in range(0, len(bits), 2):
    hash_value = hash_func(bits[i], bits[i+1])
    if hash_value == 0:
        result.append(3)
    elif hash_value == 51:
        result.append(5)
    elif hash_value == 31:
        result.append(4)
    else:
        result.append(2)
cnt = 0
for each in result:
    print(each, end="")
    cnt += 1
    if cnt == 8:
        print(" ", end="")
        cnt = 0
print()

with open("data8_res.txt") as f:
    x_cnt = 0
    cnt = 0
    prev_pos = -5
    for each in f:
        each = int(each)
        if prev_pos == -5 and each != -1:
            prev_pos = each
            cnt = 1
        elif each == prev_pos:
            if cnt > 3:
                print(prev_pos, end="")
                cnt = 1
                x_cnt += 1
                if x_cnt == 8:
                    print(" ", end="")
                    x_cnt = 0
            else:
                cnt += 1
        elif each == -1:
            if cnt != 0:
                print(prev_pos, end="")
                x_cnt += 1
                if x_cnt == 8:
                    print(" ", end="")
                    x_cnt = 0
                prev_pos = -5
                cnt = 0
        else:
            if cnt > 1:
                print(prev_pos, end="")
                x_cnt += 1
                if x_cnt == 8:
                    print(" ", end="")
                    x_cnt = 0
            cnt = 1
            prev_pos = each