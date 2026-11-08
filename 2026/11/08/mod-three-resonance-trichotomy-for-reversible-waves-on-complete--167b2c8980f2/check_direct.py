"""Independent neighbor-by-neighbor exhaustive orbit census; no matrix routines.
Run: python check_direct.py
"""
from itertools import product
from collections import Counter

def one_step(s,a,b):
    n=a+b;u=s[:n];v=s[n:];su=sum(u[:a])%3;sv=sum(u[a:])%3
    return tuple(((sv if i<a else su)-v[i])%3 for i in range(n))+u

def predicted(a,b):
    n=a+b; k=a*b%3; q=3
    if k==0:return {1:1,4:q**(2*(n-2))-1,12:q**(2*n)-q**(2*(n-2))}
    if k==2:return {1:1,4:q**(2*(n-2))-1,8:q**(2*n)-q**(2*(n-2))}
    def f(t):
        return q**((2*(n-2) if t%4==0 else 0)+(2 if t%3==0 else 1)*(1+(t%2==0)))
    return {1:f(1),2:f(2)-f(1),3:f(3)-f(1),4:f(4)-f(2),6:f(6)-f(3)-f(2)+f(1),12:f(12)-f(6)-f(4)+f(2)}

states=0
for a,b in [(2,2),(2,3),(2,4)]:
    n=a+b; bound=8 if a*b%3==2 else 12
    c=Counter()
    for s in product(range(3),repeat=2*n):
        y=s
        for t in range(1,bound+1):
            y=one_step(y,a,b)
            if y==s:
                c[t]+=1;break
        else:raise AssertionError(('nonperiodic',a,b,s))
    expect=predicted(a,b)
    assert dict(c)==expect,(a,b,c,expect)
    states+=3**(2*n)
    print(f'K_{{{a},{b}}}: {dict(sorted(c.items()))}')
print(f'PASS: {states} individually iterated states, exact primitive-period populations.')
