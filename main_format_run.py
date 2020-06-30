import re  # import regex

counter = 0
# Read file line by line
# Every 3 lines, skip 1

with open("input.txt") as f:
    content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    print(content)

for x in content:

    # iterate through list of lines
    print(x)
    # If not a blank line, execute

    fileWriter = open("output.txt", 'a')

    if not counter == 3:
        # If the start of a paragraph
        if counter == 0:
            # Write the first line to be capital
            fileWriter.write("\n\n<h3>" + x + "</h3>\n")
            # If not the first paragraph, it is the second paragraph
            counter += 1
            continue

        elif counter == 1:
            # perform modifications to each line
            try:
                link = re.match(r"[^,]*", x)
            except AttributeError:
                link = " [Error]"

            fileWriter.write("<strong>" + '<a href="https://' + link.group() +
                             '"</a>' + x.split(",", 1)[1] + "</strong>\n")
            counter += 1
            continue
        # Else it is the third paragraph
        else:
            fileWriter.write("<p>" + x.split(".", 1)[0] + ".<i>" +
                             x.split(".", 1)[1] + "</i>" + "</p>")
        counter = 3
    else:
        counter = 0
