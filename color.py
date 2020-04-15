terminalcolors = {"OKGREEN": '\033[92m',
                  "WARNING": '\033[93m',
                  "FAIL": '\033[91m',
                  "ENDC": '\033[0m'}

version = "0.1"
cmdList = {
    "fr": {"args": ["ni", "nt", "theta_i"], "types": ["float", "float", "float"], "desc": "Find fresnal coef and return refractive angle."},
    "r2fin": {"args": ["R"], "types": ["float"], "desc": "Find finesse with reflectivity."},
    "fin2r": {"args": ["Finesse"], "types": ["float"], "desc": "Find reflectivity with finesse."},    
    "prop": {"args": ["type", "value"], "types": ["string", "float"], "desc": "Conversion between light spacial and temporal properties."},
    "q/quit": {"args": ["NONE"], "desc": "Quit the toolkit."},
    "help": {"args": ["NONE"], "desc": "Show this help message."}
}

def print_to_terminal(type, text):
    print(terminalcolors[type] + text + terminalcolors["ENDC"])

def print_args_error(cmd):
    arguments_needed = ""

    for i in cmdList[cmd]["args"]:
        arguments_needed += i + ", "
    arguments_needed = arguments_needed[: -2]
    arguments_needed += "."
    print(terminalcolors["FAIL"] + cmd + " needs " + str(len(cmdList[cmd]["args"])) + " arguments: " + arguments_needed + terminalcolors["ENDC"])

def print_type_error(cmd):
    type_needed = ""

    for i in cmdList[cmd]["types"]:
        type_needed += i + ", "
    type_needed = type_needed[: -2]
    type_needed += "."
    print(terminalcolors["FAIL"] + cmd + " needs " + str(len(cmdList[cmd]["args"])) + " arguments with type: " + type_needed + terminalcolors["ENDC"])

def r2fin_help():
    print(terminalcolors["FAIL"] + "Reflectivity cannot be greater than 1.0 pr less than 0.0" + terminalcolors["ENDC"])

def fin2r_help():
    print(terminalcolors["FAIL"] + "Finesse cannot be less than 0.0" + terminalcolors["ENDC"])

def property_help(name):
    print(terminalcolors["FAIL"] + "Property with name: \"" + name + "\" is not found" + terminalcolors["ENDC"])

def printhelp(cmd):
    if len(cmd) == 1:
        print_to_terminal("OKGREEN", "ECE318 toolkit now support the following commands:")
        for cmd in cmdList:
           print(cmd.ljust(10), cmdList[cmd]["desc"][:-1].ljust(50), "Required Arguments:", cmdList[cmd]["args"])
    else:
        printhelp_cmd(cmd)

def printhelp_cmd(cmd):
    if(len(cmd) > 2):
        print(terminalcolors["FAIL"] + "Help can only have zero or one argument." + terminalcolors["ENDC"])
    try:
        print(cmd[1].ljust(10), cmdList[cmd[1]]["desc"][:-1].ljust(50), "Required Arguments:", cmdList[cmd[1]]["args"])
    except:
        print_to_terminal("FAIL", "command not found: " + cmd[1])
