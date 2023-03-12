
"""
Python Sets
1. A set is a collection of unique data. 
2. That is, elements of a set cannot be duplicate.
3. remove duplicate automatic
"""
set1={34,12,56,21,94};
set2={"java","python","javascript"};
set3={'a','i','e','u','o'};
print("set1=",set1);

# create an empty tupple
empty1=();
print("data type : ",type(empty1)); 

# create an empty set
empty2=set();
print("data type : ",type(empty2));

# create an empty dictonary
empty3={};
print("data type : ",type(empty3));

# create an empty list
empty4=[];
print("data type : ",type(empty4));


# Duplicate Items in a Set
set4={3,5,6,3,7,5};
print("set4 =",set4);   # remove duplicate automatic

# add element to set
set4.add(23);
print("set4 =",set4);

# Remove an Element from a Set
set4.discard(7);
print("set4 =",set4);

# Returns the length in the set.
print("length of set4=",len(set4));

# Returns the largest item in the set.
print("max(set4)=",max(set4));
print("max(set2)=",max(set2));

# Returns the smallest item in the set.
print("min(set4)=",min(set4));
print("min(set2)=",min(set2));

# Returns the sum of all elements in the set.
print("sum(set4))=",sum(set4));

# Iterate Over a Set in Python
for set4 in set4:
    print(set4);

