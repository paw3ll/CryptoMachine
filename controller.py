# Import Custom Function Library.
import FunctionLib as FL


# Main Function.
def main():
    configFile = 'config.csv'
    FL.readConfigurationFile(configFile)
    FL.welcomeMessage(FL.globalURL)

    # FL.CSV_Write(FL.writeFileName[0], FL.data, '')
    # Write "while run program = true keep running program
    # FunctionLib.runProgramAgain()


if __name__ == "__main__":
    main()

