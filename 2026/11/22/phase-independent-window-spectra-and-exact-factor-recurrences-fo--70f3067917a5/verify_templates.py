"""Independent complete local-factor oracle for prime-base valuation words.

A factor of length n is represented by a residue modulo p**h > n;
at most one position is exceptional. We enumerate all its q possible residues.
"""
from collections import defaultdict

def factor_set(p,q,n):
    h=1
    while p**h<=n: h+=1
    modulus=p**h
    out=set()
    for s in range(modulus):
        block=[]; unknown=[]
        for i in range(n):
            a=s+i+1
            if a%modulus==0:
                block.append(-1); unknown.append(i)
            else:
                v=0
                while a%p==0:
                    a//=p;v+=1
                block.append(v%q)
        assert len(unknown)<=1
        if unknown:
            for c in range(q):
                temp=block[:];temp[unknown[0]]=c;out.add(tuple(temp))
        else:out.add(tuple(block))
    return out

def recurrence(p,q,n,values):
    if n<=p:return 1+n*(q-1)
    if n<2*p:
        r=n-p;return 1+r+n*(q-1)
    m,r=divmod(n,p)
    return (p-r)*values[m]+r*values[m+1]

def main():
    total=0
    for p in (2,3,5,7):
        for q in (2,3,4):
            upto={2:62,3:52,5:36,7:25}[p]
            values={}
            for n in range(1,upto+1):
                actual=len(factor_set(p,q,n))
                predicted=recurrence(p,q,n,values)
                if actual != predicted:
                    raise AssertionError((p,q,n,actual,predicted))
                values[n]=predicted;total+=1
            print(f'p={p}, q={q}: all n=1..{upto} complete residue-template counts verified; P(p)={values[p]}')
    print(f'PASS: {total} exact independent all-factor counts matched the recurrence')
if __name__=='__main__': main()
