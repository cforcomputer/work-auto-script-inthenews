import re  # import regex


def run_formatter():
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
                fileWriter.write("\n\n<h3>" + x.capitalize() + "</h3>\n")
                # If not the first paragraph, it is the second paragraph
                counter += 1
                continue

            elif counter == 1:
                # perform modifications to each line
                try:
                    link = re.match(r"[^,]*", x)
                except AttributeError:
                    link = " [Error]"

                fileWriter.write("<p><strong>" + '<a href="https://' + link.group().lower() + '">' +
                                 link.group().lower() + '</a>' + ", " + x.split(",", 1)[1] + "</strong>\n<br />")
                counter += 1
                continue
            # Else it is the third paragraph
            else:
                first_sentence = x.split(".", 1)[0]
                italicized_sentence = x.split(".", 1)[1]
                fileWriter.write(first_sentence + ".<i>" + italicized_sentence
                                 + "</i>" + "</p>")
            counter = 3
        else:
            counter = 0
