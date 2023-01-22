
a=5;                     #global variable
d="java";
def function():          #declare function
    b=6;                 #local variable
    a=7;      # when local & global variable name same
    global c       # global variable inside function
    c="Python";
    global d;
    d="python";  # change value of global variable inside function
    print(a+b);
    
function();              #call function
print(c);
print(d);
