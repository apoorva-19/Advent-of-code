def find_product(ledger):
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
print(find_product(inputs))