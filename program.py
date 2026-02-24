import os

def input_file_bekeres():
    try:
        file_helye = input("Add meg az input file helyét: ")
        return file_helye
    except KeyboardInterrupt:
        return "\""

def output_file_hely_bekeres():
        file_elh = input("Adja meg a file helyet: ")
        file_elh_kit = file_elh + ".webm"
        return file_elh_kit

def ouput_file_bekeres():
        file_name = input("Add meg a file nevét: ")
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
        print("Nem jó helyet adtál meg/Nem adtál meg helyet")
    except IsADirectoryError:
        print("Directory-t adtál meg")
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
                a = input("Szeretnél megadni helyet?(I/N)")
                b = a.lower()
                if b == "i":
                    file_elh_kit = output_file_hely_bekeres()
                else:
                    file_elh_kit = ouput_file_bekeres()
                   
                if os.path.exists(file_elh_kit):
                    print("A file már megtalálható az adott helyen")
                    print("Probáljon megadni uj helyet")
                else:
                    try:
                        program(file_helye, file_elh_kit)
                    except UnboundLocalError:
                        print("Nem adtál meg helyet/nem jó helyet adtál meg")
                    except IsADirectoryError:
                        print("Directory-t adtál meg")
                    break
            except KeyboardInterrupt:
                break

main()