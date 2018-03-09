import sys

def strip_timestamp(input_file, output_file):
    line = input_file.readline()[15:]
    while line:
        output_file.write(line)
        print(line.strip())
        line = input_file.readline()[15:]


def main():
    try:
        input_name = sys.argv[1]
    except:
        input_name = ""
        while input_name.rstrip() is "":
            input_name = raw_input("Enter the log file name: ")

    try:
        output_name = sys.argv[2]
    except:        
        try:
            name, extension = input_name.split('.')
            extension = "." + extension
        except:
            name = input_name
            extension = ""
        finally:
            output_name = name + "_clean" + extension
            

    input_file = None
    output_file = None

    try:
        input_file = open(input_name,"r")
        print("Opening {}".format(input_name))
    except:
        print("Failed to open {}\n".format(input_name))
        return

    try:
        output_file = open(output_name,"wx")
        print("Opening {}".format(output_name))
    except:
        print("Failed to open {}\nPerhaps it already exists?".format(output_name))
        return
            
    strip_timestamp(input_file, output_file)
    
    print("-"*60)
    print("Saving files...")
    input_file.close()
    output_file.close()
    print("Finished!")
    
main()

