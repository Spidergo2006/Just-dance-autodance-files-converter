import os

def input_file_bekeres():
    try:
        file_helye = input("Give a location to the file: ")
        return file_helye
    except KeyboardInterrupt:
        return "\""

def output_file_hely_bekeres():
        file_elh = input("Give file location: ")
        file_elh_kit = file_elh + ".webm"
        return file_elh_kit

def ouput_file_bekeres():
        file_name = input("Give a name to the file: ")
        file_elh = ""
        file_elh_kit = file_elh + file_name + ".webm"
        return file_elh_kit 

def program(file_helye, file_elh_kit):
    pattern = bytes.fromhex(
        "1A45DFA3"
    )
    try:
        with open(file_helye, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print("You did't give a good place or did't give a place at all")
    except IsADirectoryError:
        print("You just only put directory in")
    pos = data.find(pattern)

    if pos != -1:
        remaining = data[pos:]


        with open(file_elh_kit, "wb") as out:
            out.write(remaining)

        print(f"Extraction complete. {len(remaining)} bytes saved to {file_elh_kit}")
    else:
        print("Pattern not found in the file")

def main():
    file_helye = input_file_bekeres()
    if file_helye != "\"":
        while True:
            try:
                a = input("Do you want to give a location?(Y/N)")
                b = a.lower()
                if b == "y":
                    file_elh_kit = output_file_hely_bekeres()
                else:
                    file_elh_kit = ouput_file_bekeres()
                   
                if os.path.exists(file_elh_kit):
                    print("The file can be found")
                    print("Plese try another location")
                else:
                    try:
                        program(file_helye, file_elh_kit)
                    except UnboundLocalError:
                        print("You did't give a good place or did't give a place at all")
                    except IsADirectoryError:
                        print("You just only put directory in")
                    break
            except KeyboardInterrupt:
                break

main()