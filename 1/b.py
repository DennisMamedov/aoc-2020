with open('data') as f:
    data = f.readlines()
    for d in range(len(data)):
        data[d] = int(data[d].replace('\n', ''))

for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i*j*k)
                quit()