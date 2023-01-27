def Xor(s1, s2):   #Xor function that takes two hex strings as an input
    res = ""  #initializing an empty string
    for i in range(len(s1)):  # looping over the length of the input string
        res += format(int(s1[i], 16) ^ int(s2[i], 16), '01x') # convert hex string to an integer then Xor the two hex strings then convert back to hexadecimal
    return res  # returning the results of Xoring the two hex strings

# def printingeach2hex(mylist):
#     for x in range(0, len(mylist), 2):
#         print(mylist[x:x + 2], end=" ")
#     print(" ")

if __name__ == '__main__':
    c1 = "68AF0BEF7F39982DA975B5E6D06947E61C22748C94A2155CFCCC464DEAFB6F4844DB2D7312ED192B6B7251580C61D5A296964E824A16648B16B9"
    c2 = "70A20FBD7E209324A979BFE2997A46E61B22749692EB1655FA995D46A9FA654F43C93F2114A21E3E227714580A6790B88BD74F9E09107D8B0EAC"
    c3 = "6FA20DBA622CDD28EC68F0F0C16D41A7023778C29EB8455EFC894B46EDA96C46459E2D2A1CEF1239707F571604618CEB9DD85E955013628B0DAE"
    c4 = "6FA20DBA6220893AA970A4B5CD664CE609286D8799B80010F68A0F56FAE868405BD72A2A51E118386E7214520E6994AC9D964E824A16648B16B9"
    c5 = "71A80AAA6227DD20FB68A0E1D6695BA71C3864C285AE1445F09E4A50A9EA6B5B52D82B3F51E3192922645D5100769ABE8B965C89480F6F910BB3"
    c6 = "7DA30ABD753A8E63FB70BEF1D66340BC0D24748D99EB065FEC804B03F9FB6F5F52D02A731CE31B24617F5B431C2496AA94DA1D865D17778109B3"
    c7 = "75B34EA66369932CFD31A0E7D86D5DAF0F3171C283A44542FC805603FAE6664C5BC77E3C1FA204346F7B51421D6D96EB9DD85E955013628B0DAE"
    c8 = "75E71DA771259163E774A6F0CB2E5BA3192378C283A30010EA8D4246A9F96B5A44C9312115A21823227B415A1B6D85A79D965C844A0C638C16B3"
    Allciphers = [c1, c2, c3, c4, c5, c6, c7, c8] # list of all ciphers
    xorclist = [] # initializing list to append in it the xor of all ciphers result

    for cipher in Allciphers:  #looping over the list of all ciphers
        for ciphertext in Allciphers: # loop on each cipher text inside the list of all cipher texts
            if ciphertext != cipher: # avoiding xor the ciphertext with itself example avoiding xor c1 with c1
                xorc = Xor(ciphertext, cipher) # calling function xor to xor the cipher texts
                xorclist.append(xorc) # appending the results in xorclist

    i = 0  # initializing i with 0
    spaces = [[] for p in range(0, len(Allciphers))] #initializing list of lists with the length of Allciphers length to store the spaces indexes
    for j in range(0, len(xorclist[i]), 2): #Looping over each two elements in the xorclist
        count = 0  # initializing count with zer
        for i in range(len(xorclist)): #looping over the length of xorclist
            if i % 7 == 0 and i != 0:  #separating the xor of each cipher from each others
                if count == 7:         # checking if the count equal 7 means there exists a space in this index of this cipher
                    spaces[int(i / 8)].append(j) # append the index in the list of lists of spaces
                count = 0         # returing count to zero
            if xorclist[i][j:j + 2] > "40" or xorclist[i][j:j + 2] == "00": # checking that each two hex strings in the column are begger than 40 (the beggining of letters in ascii) or equal to zero
                count = count + 1  # increasing count by 1 ther may exixts a space in this index
            if i == len(xorclist) - 1: # to reach the last cipher Xors that are stored in xorclist
                if count == 7:          # check if the count equal 7 to know the index of space in the last cipher
                    spaces[int(len(Allciphers) - 1)].append(j) # append the index of spaces in the last list in lists of lists of spaces
                count = 0   #returing count to zero
    # print(spaces)

    i = 0  # initializing i to zero
    restored_msg = ["" for k in range(len(Allciphers))] # creating an restored_msg string with the length of Allciphers
    for j in range(0, len(xorclist[i]), 2): #Looping over each two elements in the xorclist
        i = 0  # return i to zero
        spaces_flag = 0  #initializing spaces_flag with zero
        for k in range(0, len(spaces)): #looping over the length of the list of lists of spaces
            if j in spaces[k]: #checking if the index is in the spaces lists
                i = k * (len(restored_msg) - 1) #seeing the starting of each msg eample msg 1 from 0 msg 2 from 7
                spaces_flag = 1   # setting spaces_flag to 1 to indicate that there exists a space in this index
                for p in range(0, len(restored_msg)): # looping over the list of strings
                    if p == k: #checking if the string number is the same as the list number
                        restored_msg[k] += bytes.fromhex("20").decode() #adding a space in this position
                        continue

                    restored_msg[p] += bytes.fromhex(Xor(xorclist[i][j:j + 2], "20")).decode() # xor with 20 in hex then convert from hex to string
                    i += 1 # increasing i by 1
                break
        if spaces_flag == 0: #checking if spaces_flag equal zero (there is no space in this index)
            for p in range(0, len(restored_msg)): #looping over the list of string
                restored_msg[p] += "#"  #concatenating # in the unknown indexes
    for h in range(0,len(restored_msg)):
        print(restored_msg[h]) #printing the restored_msg

    # print(".............The restored msg after guessing ..............:")
    # print("The open design principle increases confidence in security"
    #         "\nLearning how to write secure software is a necessary skill"
    #         "\nSecure key exchange is needed for symmetric key encryption"
    #         "\nSecurity at the expense of usability could damage security"
    #         "\nModern cryptography requires careful and rigorous analysis"
    #         "\nAddress randomization could prevent malicious call attacks"
    #         "\nIt is not practical to rely solely on symmetric encryption"
    #         "\nI shall never reuse the same password on multiple accounts")
