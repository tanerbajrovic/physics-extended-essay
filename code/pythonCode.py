import serial
import math

# Serial port of Arduino (on Win it's COM5)
arduinoPort = 'COM3' # Connect to Arduino port
baud = 9600 # Arduino runs at 9600
fileName = 'analogData.csv' # Name of the CSV file fro data collection
resistor = 989 # Resistor has nominal resistance 1000ohms but experimentally 989ohms
voltageArduino = 5 # Voltage of Arduino
B = 3540.94 # Coefficient value obtained from Steinhart-Hart 
nominalResistance = 1330 # at 22.6 Celsius

ser = serial.Serial(arduinoPort, baud)
print('Connected to Arduino port:' + arduinoPort)
file = open(fileName, "a")
print("Created file")

# Initial declaration of variables
line = 0
temperature = 0

def temperatureCalculation(input):
    temperature = B / math.log(thermistorResistance / (nominalResistance * math.exp( -B / 295.8))) - 273.15 # Steinhart-Hart B Formula 
    return temperature

while 0 <= temperature:
    getData = str(ser.readline().decode('utf-8')) # Using decode since Python 3 
    voltageThermistor = float(getData[0:][:-2]) # Curent line converted to float for VoltageTwo (thermistor)
    thermistorResistance = (voltageThermistor * resistor) / (voltageArduino - voltageThermistor)
    temperature = temperatureCalculation(thermistorResistance) # Pass the value of thermistorResistance into function defined above and return value of temperature
    print(voltageThermistor, temperature)

    file = open(fileName, "a")

    file.write(str(voltageThermistor) + ',' + str(temperature) + '\n') # Write thermistor voltage into CSV file
    line = line + 1

print('Data collection complete!')
file.close()