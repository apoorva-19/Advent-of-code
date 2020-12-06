def find_seat(boarding_pass):
    max_seat = 0
    for b_pass in boarding_pass:
        start_r = 0
        end_r = 127
        start_c = 0
        end_c = 7
        for j in range(7):
            if b_pass[0][j] == 'F':
                end_r = (end_r+start_r)//2
            elif b_pass[0][j] == 'B':
                start_r = (end_r+start_r)//2 + 1
        for k in range(3):
            if b_pass[1][k] == 'L':
                end_c = (end_c+start_c)//2
            elif b_pass[1][k] == 'R':
                start_c = (end_c+start_c)//2 + 1
        max_seat = max(max_seat, start_r*8+start_c)
    
    return max_seat

def find_seat2(boarding_pass):
    seats = []
    for b_pass in boarding_pass:
        start_r = 0
        end_r = 127
        start_c = 0
        end_c = 7
        for j in range(7):
            if b_pass[0][j] == 'F':
                end_r = (end_r+start_r)//2
            elif b_pass[0][j] == 'B':
                start_r = (end_r+start_r)//2 + 1
        for k in range(3):
            if b_pass[1][k] == 'L':
                end_c = (end_c+start_c)//2
            elif b_pass[1][k] == 'R':
                start_c = (end_c+start_c)//2 + 1
        seats.append(start_r*8+start_c)
    
    seats.sort()
    i = 0
    while(seats[i]+1 == seats[i+1]):
        i+=1
    return seats[i]+1


    

inputs = []
with open("in5.txt", "r") as f:
    inputs = [list([line.strip()[:7], line.strip()[7:]]) for line in f]

print(find_seat(inputs))
print(find_seat2(inputs))
# print(inputs)