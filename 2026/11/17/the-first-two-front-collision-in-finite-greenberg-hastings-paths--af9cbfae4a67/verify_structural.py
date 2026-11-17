"""Independent microscopic verifier of the first-interference theorem.
Uses product states and a direct array-based synchronous update.
"""
from itertools import product
from collections import Counter
from math import factorial

def evolve(x,q):
    v=list(x)
    steps=0
    while any(v):
        w=[]
        for i,a in enumerate(v):
            neighbors=(i>0 and v[i-1]==1) or (i<len(v)-1 and v[i+1]==1)
            w.append((a+1)%q if a else int(bool(neighbors)))
        v=w
        steps+=1
        assert steps<=len(x)+q-2
    return steps

def test(n,q):
    maximal={}; shell=Counter(); first=Counter()
    for x in product(range(q),repeat=n):
        t=evolve(x,q)
        if t==n+q-2:
            k=sum(v>=2 for v in x)
            e=sum(v==1 for v in x)
            shell[(k,e)]+=1
            maximal[x]=e
        # candidate: one oriented wave, penultimate collision veto
        pred=False
        for a in [x,x[::-1]]:
            if a[0]==1 and all(a[i]==0 or a[i]>=q-i+1 for i in range(1,n-1)):
                if not (a[-1]==1 and a[-2]==0):
                    pred=True
        assert pred==(t==n+q-2), (n,q,x,t,pred)
    expected=Counter()
    # polynomial expansion 2 product_(j=0..n-4)(1+j*z)*[(1+(n-3)z)^2+u(n-3)z],
    # exponent of u records the second initially excited endpoint
    coeff=[1]
    for j in range(n-3):
        p=[0]*(len(coeff)+1)
        for k,c in enumerate(coeff):
            p[k]+=c;p[k+1]+=j*c
        coeff=p
    for k,c in enumerate(coeff):
        expected[(k,1)]+=2*c
        expected[(k+1,1)]+=4*(n-3)*c
        expected[(k+2,1)]+=2*(n-3)**2*c
        expected[(k+1,2)]+=2*(n-3)*c
    assert shell==expected,(n,q,shell,expected)
    count=len(maximal)
    assert count==2*(factorial(n-1)-factorial(n-3))
    print(f"n={n} q={q} checked={q**n} maximal={count} one_source={sum(v for (k,e),v in shell.items() if e==1)} two_source={sum(v for (k,e),v in shell.items() if e==2)} polynomial={dict(sorted(shell.items()))}")
for n in range(4,8):test(n,n-1)
print("PASS predicate and bivariate polynomial")
