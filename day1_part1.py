inputs = []
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(int(inp))

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