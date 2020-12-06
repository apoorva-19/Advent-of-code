def find_product1(inputs):
    max = 2020
    diff = 0
    for i in range(len(inputs)):
        d = max-inputs[i]
        if d in inputs:
            diff = d
            break

    if diff:
        print(inputs[i],diff, inputs[i]*diff)
    else:
        print("no")

def find_product2(ledger):
    ledger_dict = {(2020 - i - j): (i, j)
                    for i in ledger
                    for j in ledger
                    if i != j}
    for entry in ledger:
        if entry in ledger_dict:
            j, k = ledger_dict[entry]
            return entry * j * k

with open("in1.txt", "r") as f:
    inputs = [int(line.strip()) for line in f]
print(find_product1(inputs))
print(find_product2(inputs))