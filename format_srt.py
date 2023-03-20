import os
def format_srt(input):
    arr = input.split('\n')
    output = []
    for i in range(0, len(arr)):
        if (i - 2) % 4 == 0:
            line = arr[i].lower()
            line = line.replace("i ", "I ")
            line = line.replace("kind of","kinda")
            line = line.replace("going to","gonna")
            line = line.replace("could have","could've")
            line = line.replace("I will","I'll")
            line = line.replace(",","")
            line = line.replace(".","")
            line = line.replace("?","")
            line = line.replace("!", "")
            line = line.replace("i'","I'")
            output.append(line)
        else:
            output.append(arr[i])
    return "\n".join(output)

for filename in os.listdir('input'):
    f_in = open(f'input/{filename}', 'r')

    content = format_srt(f_in.read())

    f_out = open(f'output/{filename}', 'a')
    f_out.write(content)