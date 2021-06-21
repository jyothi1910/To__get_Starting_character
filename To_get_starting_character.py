
# To get the words of specified character
file_object=open('text.py','r')
count = 0

text=file_object.read()
split_text=(text.split())
#print(split_text)

charToGet=input("enter the starting character to get from string:")
for char in split_text:
    if char[0] == charToGet:
        count += 1
        print(char)
print("{} words are found with starting character {}".format(count,charToGet))        


#if count == 0:
#    print("No words are found with matching character ",charToGet)
        
    




    
