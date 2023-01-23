# Type Conversion

a=5;
b=6+5j;
c=3.456;

print(type(a));
print(type(b));
print(type(c));

a1=float(a);
a2=complex(a);

print(a1);
print(a2);

# b1=int(b);        # can't convert complex to int
# b2=float(b);      # can't convert complex to float

c1=int(c);
c2=complex(c);

print(c1);
print(c2);