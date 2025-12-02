# Example Python wrapper functions for the API
def SetThermalCal(iCtrl1, iProbe1, iCtrl2, iProbe2):
    # Simulate calling the C API to set thermal calibration
    print(f"SetThermalCal called with: {iCtrl1}, {iProbe1}, {iCtrl2}, {iProbe2}")

def WriteEEPROM():
    # Simulate writing EEPROM to save the settings permanently
    print("WriteEEPROM called to save settings permanently")

def main():
    # Set example calibration points (in hundredths of degree Celsius)
    iCtrl1 = 2500  # 25.00°C
    iProbe1 = 2480 # 24.80°C reading
    iCtrl2 = 8000  # 80.00°C
    iProbe2 = 7980 # 79.80°C reading

    # Call setters
    SetThermalCal(iCtrl1, iProbe1, iCtrl2, iProbe2)

    # Persist calibration
    WriteEEPROM()

if __name__ == "__main__":
    main()
