"""Exact independent finite-polynomial certificate for the two optimal sextics."""
p=7

def trim(a):
    while len(a)>1 and a[-1]%p==0: a.pop()
    return [v%p for v in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c)
def power(a,n):
    r=[1]
    for _ in range(n):r=mul(r,a)
    return r
def sub(a,b):
    return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mod(a,b):
    a=trim(a[:]);b=trim(b[:]);assert b!=[0]
    while len(a)>=len(b) and a!=[0]:
        coeff=a[-1]*pow(b[-1],-1,p)%p;shift=len(a)-len(b)
        for i in range(len(b)):a[i+shift]=(a[i+shift]-coeff*b[i])%p
        a=trim(a)
    return a
def gcd(a,b):
    while b!=[0]:a,b=b,mod(a,b)
    return trim([(v*pow(a[-1],-1,p))%p for v in a])
P=sub(power([0,1],8),[1])
assert gcd(P,sub(power([2,-1],8),[1]))==[6,1]
assert gcd(P,sub(power([3,-2],8),[1]))==[6,1]
# Nonzero sixth powers in F_49 are the eight eighth roots of unity; their
# intersection with F_7^* is the subgroup {+1,-1}.
assert 2 not in (1,6) and 3 not in (1,6) and 5 not in (1,6)
print('VERIFY_GCD_OK: both gcds equal T-1 in F7[T]')
