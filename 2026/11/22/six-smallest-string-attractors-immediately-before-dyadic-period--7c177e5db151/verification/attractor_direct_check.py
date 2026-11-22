#!/usr/bin/env python3
"""Independent direct factor-coverage enumeration for small dyadic orders."""

def phi(w):return ''.join('01' if c=='0' else '00' for c in w)

def pairs(w):
    n=len(w)
    masks={}
    for a in range(n):
        for b in range(a+1,n+1):
            factor=w[a:b]
            masks[factor]=masks.get(factor,0)|(((1<<(b-a))-1)<<a)
    vals=list(set(masks.values()))
    ans=[]
    for i in range(n):
        missing=[m for m in vals if not ((m>>i)&1)]
        for j in range(i+1,n):
            if all((m>>j)&1 for m in missing):ans.append((i+1,j+1))
    return ans

seed={(4,8),(4,10),(5,10),(6,11),(6,12),(8,12)}
w='0'
for k in range(1,9):
    w=phi(w)
    if k>=4:
        got=set(pairs(w[:-1]))
        want={(a*2**(k-4),b*2**(k-4)) for a,b in seed}
        assert got==want,(k,got,want)
        print('k =',k,'length =',len(w)-1,'count =',len(got),'PASS')
print('DIRECT FINITE CHECK PASS (the infinite theorem uses induction and a local certificate)')
