# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
MIN_KEY_LENGTH = 3      # A00
MAX_SIGNAL = 5.0        # Max five
MIN_SIGNAL = 1.0        # Min 1

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
theRecords = [["7JA3B1", 3.41], ["A7B", 2.33], ["Y8R4K", 2.78],
              ["O9N1K0", 5.0], ["A1&2X3", 1.25],
              ["A12B3", 2.47], ["B1P6Y7", -1.23], ["F8D7L5", 5.17],
              ["AB23A5", 2.47], ["X0B9A9", 0], ["Q6B7T3", 0.5],
              ["A15B6C2", 2.56], ["A12340", 2.5], ["P3Y1M4V7", 4.35],
              ["J1H0Q1", 1.0], ["X", 2.3], ["W64T18B1", 1.51],
              ["A00", 1.99], ["A3B1C14", 4.59]
             ]


# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

def recordDivide():
    keys = []
    signals = []
    for row in theRecords:
        keys.append(row[0])
        signals.append(row[1])
    return keys, signals

def minimumLength(keys):
    for KeyLength in keys:
        if len(KeyLength) < MIN_KEY_LENGTH:
            print("Too short key:", KeyLength)
    return True

def checkSignals(signals):
    for SignalLength in signals:
        if SignalLength > MAX_SIGNAL:
            print("Signal to high:", s)
        elif SignalLength < MIN_SIGNAL:
            print("Signal too low", s)
        else:
            print("Signal OK => " + str(s))



# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

def processManager():
    KeyLength, SignalLength = recordDivide()
    minimumLength(KeyLength)
    checkSignals(SignalLength)

processManager()
