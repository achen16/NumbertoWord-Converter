#arrays to hold number words
ones = ["", "One ","Two ","Three ","Four ", "Five ", "Six ","Seven ","Eight ","Nine "]
teens = ["Ten ","Eleven ","Twelve ", "Thirteen ", "Fourteen ", "Fifteen ","Sixteen ","Seventeen ", "Eighteen ","Nineteen "]
tens = ["", "", "Twenty ","Thirty ","Forty ", "Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]
thousands = ["","Thousand ","Million ", "Billion ", "Trillion ", "Quadrillion ", "Quintillion ", "Sextillion ", "Septillion ","Octillion ", "Nonillion ", "Decillion ", "Undecillion ", "Duodecillion ", "Tredecillion ", "Quattuordecillion ", "Quindecillion", "Sexdecillion ", "Septendecillion ", "Octodecillion ", "Novemdecillion ", "Vigintillion "]

#convert the number to a word
def convertNumber(num):
    #return zero if 0 is entered
    if num == 0:
        return "zero"

    n_string = str(num)
    remaining = n_string
    t = 0
    word = ""

    #split the number into 3 digits at a time, staring with the last 3 to calculate hundreds, thousands, millions, etc
    #last_three is the current working digit trio. Remaining is the rest of the number minus the last 3 digits
    #repeat calculations until their are no more digits left
    while (remaining != ""):
        last_three = remaining[-3:]
        if len(last_three) == 1:
            last_three = "00" + last_three
        elif len(last_three) == 2:
            last_three = "0" + last_three

        remaining = remaining[:-3]
        #print (remaining)
        #print (last_three)

        #Calculate the word value of the three digits using their index
        #i.e if num = 123, ones = 3(three), tens = 2(two), hundreds = 1(one)
        ones_value = int(last_three[2])
        tens_value = int(last_three[1])
        hundreds_value = int(last_three[0])

        #print "Tens:", tens_value
        #print "Ones:" ,ones_value
        #print "Hundreds:", hundreds_value

        #put the words together and add to existing word
        if hundreds_value > 0:
            hundred_value = ones[hundreds_value] + "Hundred "
        else:
            hundred_value = ""

        if tens_value == 1:
            tens_value = teens[ones_value]
            ones_value = ""
        elif tens_value > 1 and ones_value > 0:
            tens_value = tens[tens_value].replace(" ", "-", 1)
            ones_value = ones[ones_value]
        else:
            tens_value = tens[tens_value]
            ones_value = ones[ones_value]

        if (hundred_value + tens_value + ones_value != ""):
            word = hundred_value + tens_value + ones_value + thousands[t] + word
        t+= 1

    return word

def main():
    num = input("Choose a number: ")
    word = convertNumber(num)
    print ("Number: " + str(num))
    print ("Word: " +  word)


if __name__ == '__main__':
    main()
