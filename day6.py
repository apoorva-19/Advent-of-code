# base_set = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
def count_combi(customs_form):
    total = 0
    for form in customs_form:
        # print(len(form))
        total += len(form)-1
    return total

inputs=[]
new_set = set()
b_set = set()
with open("in6.txt", "r") as f:
    for line in f:
        if line == "\n":
            inputs.append(b_set)
            new_set = set()
            b_set = set()
        else:
            split_line = list(line)
            new_set = set(split_line)
            if len(b_set):
                b_set = b_set.intersection(new_set)
            else:
                b_set = new_set

# print(len(set()))
print(count_combi(inputs))