def find_acceptable_password(passwords):
    cnt = 0
    for pwd in passwords:
        if pwd[0]<= pwd[3].count(pwd[2]) <= pwd[1]:
            cnt += 1
    return cnt

def find_acceptable_password2(passwords):
    cnt = 0
    for pwd in passwords:
        flag1 = flag2 = 0
        if pwd[3][pwd[0]-1] == pwd[2]:
            flag1 = 1
        if pwd[3][pwd[1]-1] == pwd[2]:
            flag2 = 1
        if flag1 or flag2:
            cnt +=1
        if flag1 and flag2:
            cnt -=1
    return cnt

inputs = []
with open("in2.txt", "r") as f:
    inputs = [line.strip() for line in f]
ready_inputs = []
for inp in inputs:
    split_inp = inp.split()
    r = split_inp[0].split('-')
    new_inp = [int(r[0]), int(r[1]), split_inp[1][0], split_inp[2]]
    ready_inputs.append(new_inp)

print(find_acceptable_password(ready_inputs))
print(find_acceptable_password2(ready_inputs))
