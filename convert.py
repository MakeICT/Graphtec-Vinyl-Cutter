import sys

def convert(file):
    in_file = open(file, 'r')
    content = in_file.read()
    print(content)
    commands = content.split(';')
    print(commands)
    new_content = ""
    for command in commands:
        command = command.strip()
        if len(command) > 0:
            if command[0:2] == 'PD':
                print(command)
                split_command = command.split(',')
                if len(split_command) > 2:
                    print(split_command)
                    new_split_command = []
                    for i,c in enumerate(split_command):
                        if i == 0:
                            c = c[2:]
                        if not i%2:
                            new_split_command.append(command[0:2] + c + ',' + split_command[i+1])
                    
                    print(new_split_command)
                    new_content += ';'.join(new_split_command) + ';'
                else:
                    new_content += command + ';'
            else:
                new_content += command + ';'

    print(new_content)

    modified_file = open(file.split('.')[0]+"_converted."+file.split('.')[1], 'w')
    modified_file.write(new_content)

if __name__ == "__main__":
    convert(sys.argv[1])