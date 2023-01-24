# Python Strings

# Multiline Strings
a1 = """My,          
name is,
Avik
Das.
-----------
"""
print(a1);


# Multiline Strings
a2 = '''I,                
Love,
Java
python.'''
print(a2);


# Strings are Arrays
a3="I love python & java";             
print(a3[2],a3[7]);



# for loop
for i in a3: 
    print(i);
    
    
#String Length
print(len(a3));
    

# Check String = certain phrase or character is present in a string
print("java" in a3);      #true
print("j" in a3);         #true
print("javas" in a3);     #false
print("javas" not in a3); #true

if "&" in a3:
    print("character is present");
    
    
# Slicing Strings
print(a3[9:12]);      #start index and the end index  separated by a colon 
print(a3[9:]);        #Slice To the end
print(a3[:12]);       #Slice From the Start


#Negative Indexing
print(a3[-9:-12]);
print(a3[-9:]);
print(a3[:-12]);


a4="  Python , Java  "

#Upper Case
print(a4.upper());

#Lower Case
print(a4.lower());

#Remove Whitespace
print(a4.strip());

#Replace String
print(a4.replace("P","a"));

#Split String
print(a4.split(","));

#String Concatenation
a5="Avik";
a6="das";
print(a5+a6);

#String Format 
rank=1;
s1= "I learn python whose rank is {}";
print(s1.format(rank));

ap=12;
ma=13;
ora=20;
av=60;
wal=120;

s2='''price of apple {}
price of mango {}
price of orange {}
price of avocado {}
price of walnut {} ''';

print(s2.format(ap,ma,ora,av,wal));



