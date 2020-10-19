# Initialization block
sfile = None
saddress = 'rasp.json'
text = None


def load_file(address):
    global sfile
    sfile = open(address, 'r')


load_file(saddress)
text = sfile.read(2000)


# End of init block

# Cleaning block. Deletes special symbols and extra whitespaces.
# Also changes some symbols for another for comofrtable parsing.
def clean(a, b, c):
    for i in range(len(b)):
        a = a.replace(b[i], c[i])
    return a


mas_t = clean(text, [',', '\r', '\t', '   ', '\n', '{', '}', ' "', '  "', '""'],
              ['', '', '', '', ' ', '"{"', '"}"', '"', '"', '"']).split('"')
for i in range(mas_t.count('')):
    mas_t.remove('')
for i in range(mas_t.count(' ')):
    mas_t.remove(' ')


# End of block

# Main block. Parses source text and generates data array which contains all info in blocks

def tokenizer(mas):  # converts "clear" array in special data structure. Structure described in doc.
    timetable = []
    n = int(mas[6])
    timetable.append(mas[1])
    timetable.append(n)
    k = 7
    massiv = []
    for i in range(n):
        k = k + 6
        massiv.append({})
        for j in range(6):
            massiv[i].update([[names[j], mas[k - 1 + 3 * j]]])
        k = k + 16
    timetable.append(massiv)
    return timetable


names = ['subject', 'starttime', 'endingtime', 'room', 'street', 'classformat']  # name of <lesson> attributes

outdata = tokenizer(mas_t)
print(outdata)
# Output string generation
answer = '<?xml version="1.0" encoding="ASCII"?>\n<day name="' + outdata[0] + '">\n'
for i in range(outdata[1]):
    answer = answer + '  <lesson subject="' + outdata[2][i]['subject'] + '" starttime="' + outdata[2][i][
        'starttime'] + '" endingtime="' + outdata[2][i]['endingtime'] + '" room="' + outdata[2][i][
                 'room'] + '" street="' + outdata[2][i]['street'] + '" classformat="' + outdata[2][i][
                 'classformat'] + '">\n'
answer = answer + '</day>'
# End of main block

# Final stage. Output file generation
f = open('rasp.xml', 'w')
f.write(answer)
f.close()
