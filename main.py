import sys
import datetime

def main():
    file_to_be_parsed = open(sys.argv[1], 'r')
    file_lines = file_to_be_parsed.readlines()
    write_parsed_file(sys.argv[2], file_lines)

def write_parsed_file(parse_string, parsed_doc):
    parsed_list = []

    for ps in parsed_doc:
        if parse_string in ps:
            parsed_list.append(ps)

    dated_file = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
    new_file = open(dated_file, 'w')
    new_file.writelines(parsed_list)

if __name__ == "__main__":
    main()