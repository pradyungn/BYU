languages = []
with open('language.txt') as txt:#This takes the languages and puts them into a raw list, without alphabetizing the list.
    for line in txt:
        languages.append(line.strip())

key=input('What language would you like to find in the list? Make sure the first letter is capitalized')#Completes a linear search for a language of your choice.
pos = 0
while pos < len(languages) and key != languages[pos]:
    pos += 1

if pos<len(languages):
    print(key+' is included in this list, at position '+str(pos))
else:
    print(key+' was not listed in this list of languages')\


for key_pos in range(1, len(languages)):#Alphabetizes list
 
        key_value = languages[key_pos]
 
        scan_pos = key_pos - 1
 
        while scan_pos >= 0 and languages[scan_pos] > key_value:
            languages[scan_pos + 1] = languages[scan_pos]
            scan_pos = scan_pos - 1
 
        languages[scan_pos + 1] = key_value

for language in languages:
    print(language)
        
