def find_trees(mapping):
    cnt_tree = 0
    i = 0
    j = 0
    points = len(mapping[0])
    while j != len(mapping)-1:
        i = (i+3)%points
        j += 1
        # print(j,i)
        if mapping[j][i] == '#':
            cnt_tree +=1
    
    return cnt_tree

def find_trees2(right, down, mapping):
    cnt_tree = 0
    i = 0
    j = 0
    points = len(mapping[0])
    while j != len(mapping)-1:
        i = (i+right)%points
        j += down
        # print(j,i)
        if mapping[j][i] == '#':
            cnt_tree +=1
    
    return cnt_tree

inputs = []
with open("in3.txt", "r") as f:
    inputs = [list(line.strip()) for line in f]
# print(len(inputs))
# print(find_trees(inputs))
print(find_trees2(1,1,inputs)*find_trees2(3,1,inputs)*find_trees2(5,1,inputs)*find_trees2(7,1,inputs)*find_trees2(1,2,inputs))