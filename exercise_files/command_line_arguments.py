from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--output", "-o", required=True, help="The destination folder")
parser.add_argument("--text", "-t", required=True, help="The text to write to the file")
args = parser.parse_args()

with open(args.output, "w") as file:
    file.write(args.text + "\n")

print(f'The text: "{args.text}" has been successfully written in the "{args.output}" file.')