file = open("sample_data.csv")
header = file.readline()
for line in file:
    parts = line.strip().split(",")
    print(parts)

    time=parts[0]
    temp=parts[1]

    print("Time",time)
    print("temp",temp)
    

file.close()
