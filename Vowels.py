def vowel(s): 
    if not s: 
        return s
    elif s[0] in "aeiouAEIOU": 
        return vowel(s[1:]) #Removes vowels in string
    return s[0] + vowel(s[1:]) #Removes vowels in string
#Recursive code = BigO (N)

print(vowel("My Name Is DJ Stutz"))

#BigO (N)

def VOWEL(S)
    if not s
        return s
    elif s[0] in "aeiouAEIOU"
        return VOWEL
print VOWEL "users input"
