"""Independent finite-field enumeration of distinct centralizers in T_3(F_q).
Requires Python 3 standard library only; supports primes 2,3,5,7 and GF(4).
Each centralizer is represented by the row-reduced space of its commutator equations.
"""
from collections import Counter
from itertools import product


def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def neg(a,q):
    return a if q==4 else (-a)%q

def mul(a,b,q):
    if q!=4:
        return (a*b)%q
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a&4:a^=7  # t^2+t+1
    return r

def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def reduced_rowspace(rows,q):
    M=[list(row) for row in rows]
    pivot=0
    for j in range(5):
        i=next((i for i in range(pivot,3) if M[i][j]),None)
        if i is None:continue
        M[pivot],M[i]=M[i],M[pivot]
        invp=inv(M[pivot][j],q)
        M[pivot]=[mul(x,invp,q) for x in M[pivot]]
        for r in range(3):
            if r!=pivot and M[r][j]:
                a=M[r][j]
                M[r]=[add(x,neg(mul(a,y,q),q),q) for x,y in zip(M[r],M[pivot])]
        pivot+=1
        if pivot==3:break
    return tuple(tuple(row) for row in M[:pivot])

def check(q):
    centralizers=set()
    for a,b,c,u,w,v in product(range(q),repeat=6):
        ab=add(a,neg(b,q),q)
        bc=add(b,neg(c,q),q)
        ac=add(ab,bc,q)
        # Constraints in variables (beta-alpha, gamma-beta, s, r, t).
        rows=((u,0,ab,0,0),(0,w,0,bc,0),(v,v,neg(w,q),u,ac))
        centralizers.add(reduced_rowspace(rows,q))
    spectrum=Counter(len(s) for s in centralizers)
    expected={0:1,1:1,2:3*q*q+2*q,3:3*q*q+q-1+(q**3 if q>2 else 0)}
    actual=sum(spectrum.values())
    predicted=31 if q==2 else q**3+6*q*q+3*q+1
    assert dict(spectrum)==expected,(q,spectrum,expected)
    assert actual==predicted,(q,actual,predicted)
    print('q=%d: %d centralizers; commutator-rank census %s'%(q,actual,dict(sorted(spectrum.items()))))

if __name__=='__main__':
    for q in (2,3,4,5,7):check(q)
    print('VERIFY_OK')
