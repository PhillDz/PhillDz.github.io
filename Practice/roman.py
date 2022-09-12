# Roman to Integer

inp_roman = input("Enter Roman Number.")

roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

# if something is in front of I subtract 1 unless its I

inplength = len(inp_roman)
counter = 0
integer = 0
numlist = []

for char in inp_roman:
    num = roman[char]
    numlist.append(num)

    if len(numlist) > 1:
        prev_num = numlist[counter - 2]
        if num > prev_num and num == 5 or num == 10 or num == 50 or num == 100 or num == 500 or num == 1000:
            integer -= prev_num
            num -= prev_num
            integer += num
        else:
            integer += num
    else:
        integer += num
        continue

    counter += 1
    if counter == inplength:
        exit

print(numlist)
print(integer)


