import re
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_for_fields(passport):
    cnt = 0
    flag = 0
    valid_passport = []
    for p1 in passport:
        fields = p1.keys()
        # print(fields)
        flag = 0
        for r in required:
            if r not in fields:
                flag = 1
                break
        if not flag:
            cnt +=1 
            valid_passport.append(p1)
    return valid_passport

def check_height(hgt):
    if hgt.endswith("cm"):
        hgt = hgt.replace("cm", "")
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76
        except:
            return False
    return False

def check_further(passport):
    cnt = 0
    # flag = 0
    for p1 in passport:
        checks = [
        1920 <= int(p1.get('byr', 0)) <= 2002,
        2010 <= int(p1.get('iyr', 0)) <= 2020,
        2020 <= int(p1.get('eyr', 0)) <= 2030,
        check_height(p1.get('hgt', "")),
        re.match(r"^#[0-9a-f]{6}$", str(p1.get("hcl" ""))),
        p1.get('ecl', "") in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r"^[0-9]{9}$", p1.get("pid", "")),
    ]
        if all(checks):
            cnt+=1
    return cnt
    

inputs = []
new_dict = {}
with open("in4.txt", "r") as f:
    for line in f:
        if line == "\n":
            # print("here")
            inputs.append(new_dict)
            new_dict = {}
        else:
            split_line = line.split()
            for sp in split_line:
                more_split = sp.split(":")
                # new_dict[more_split[0]] = more_split[1]
                # print(more_split)
                new_dict.update({more_split[0]:more_split[1]})
            # print(new_dict)

# print(inputs)
# print(check_for_fields(inputs))
valid = check_for_fields(inputs)

print(check_further(valid))