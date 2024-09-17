import json
import re
import sys
import os

def fix_nested_quotes(json_string):
    def escape_quotes(match):
        return match.group(0).replace('"', '\\"')
    pattern = r'"(?:[^"\\]|\\.)*"'
    fixed_json_string = re.sub(pattern, escape_quotes, json_string)
    return fixed_json_string

def write_file(output_file,data):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(data)


def process_json_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            json_content = file.read()

        fixed_json_content = fix_nested_quotes(json_content)
        base, ext = os.path.splitext(input_file)
        tmp_file = f"{base}-tmp{ext}"
        write_file(tmp_file,fixed_json_content)

        # validate
        json.loads(fixed_json_content)

        write_file(output_file,fixed_json_content)

        print(f"Successfully processed {input_file} and saved to {output_file}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_file}")
        print(f"Error message: {str(e)}")
    except IOError as e:
        print(f"Error: Unable to read or write file")
        print(f"Error message: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]

    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        # Generate output filename by adding "-fixed" before the extension
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}-fixed{ext}"

    process_json_file(input_file, output_file)

if __name__ == "__main__":
    main()