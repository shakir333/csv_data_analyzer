import matplotlib.pyplot as plt
TEMP_LIMIT = 200
PRESSURE_LIMIT = 80
VIBRATION_LIMIT = 10
JOINT_ANGLE_LIMIT = 100
MOTOR_SPEED_LIMIT = 200

file = open("sample_data.csv")
header = file.readline()

times = []
temperatures = []
pressures = []
vibrations = []
joint_angles = []
motor_speeds = []

print("Engineering Test Data Report")
print("---------------------")
print("Warnings:")

for line in file:
    parts = line.strip().split(",")

    time = float(parts[0])
    temp = float(parts[1])
    pressure = float(parts[2])
    vibration = float(parts[3])
    joint_angle = float(parts[4])
    motor_speed = float(parts[5])


    times.append(time)
    temperatures.append(temp)
    pressures.append(pressure)
    vibrations.append(vibration)
    joint_angles.append(joint_angle)
    motor_speeds.append(motor_speed)


    if temp>TEMP_LIMIT:
        print("WARNING: High temperature at time:", time)
        
    if pressure> PRESSURE_LIMIT:
        print("WARNING: High pressure at time:", time)
        
    if vibration > VIBRATION_LIMIT:
        print("WARNING: High vibration at time:", time)

    if joint_angle> JOINT_ANGLE_LIMIT:
        print("WARNING: High joint angle at time:", time)

    if motor_speed>MOTOR_SPEED_LIMIT:
        print("WARNING: High motor speed at time:", time)

print("")



    
        
    
    

file.close()
#calculations
average_temp= sum(temperatures) / len(temperatures)
average_pressure = sum(pressures) /len(pressures)
average_vibration= sum(vibrations) /len(vibrations)
average_joint_angle= sum(joint_angles) /len(joint_angles)
average_motor_speed = sum(motor_speeds) /len(motor_speeds)

print("Summary:")

#printing
print("Average temperature:", format(average_temp,".2f"))
print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))

print("")

print("Average pressure:", format(average_pressure,".2f"))
print("Maximum pressure:", max(pressures))
print("Minimum pressure:", min(pressures))

print("")

print("Average vibration:", format(average_vibration,".2f"))
print("Maximum vibration:", max(vibrations))
print("Minimum vibration:", min(vibrations))

print("")

print("Average joint angle:", format(average_joint_angle,".2f"))
print("Maximum joint angle:", max(joint_angles))
print("Minimum joint angle:", min(joint_angles))

print("")

print("Average motor speed:", format(average_motor_speed,".2f"))
print("Maximum motor speed:", max(motor_speeds))
print("Minimum motor speed:", min(motor_speeds))

#graph codes
plt.plot(times,temperatures)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature over Time")
plt.savefig("temperature_graph.png")
plt.show()
