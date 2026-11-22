"""Reproduce the exact one-insertion spectrum of ternary 2-irreducible words.
Uses independent word insertion and run-composition enumeration; no external data.
"""
from collections import Counter
from itertools import product

def admissible(w):
    return all(w[i] != w[i+1] for i in range(len(w)-1)) and all(
        w[i:i+2] != w[i+2:i+4] for i in range(len(w)-3))

def direct(n):
    out=Counter()
    for w in product(range(3),repeat=n):
        if not admissible(w):
            continue
        descendants=set()
        for i in range(n+1):
            for a in range(3):
                v=w[:i]+(a,)+w[i:]
                if admissible(v):
                    descendants.add(v)
        out[len(descendants)]+=1
    return out

def runs(s):
    lengths=[]
    for bit in s:
        if lengths and bit==prev: lengths[-1]+=1
        else: lengths.append(1)
        prev=bit
    return lengths

def formula(n):
    m=n-1
    out=Counter()
    for s in product((-1,1),repeat=m):
        if any(s[i]==s[i+2]!=s[i+1] for i in range(m-2)):
            continue
        lens=runs(s)
        if len(lens)==1:
            degree=m+4
        else:
            degree=4+(lens[0]-1)+(lens[-1]-1)
            degree+=sum(L-2+(L==3) for L in lens[1:-1])
        out[degree]+=3  # independent initial nucleotide choices
    return out

def from_gf(n):
    """Coefficient of z^(n-1) in 6*y^4*((zy)^2/(1-zy)+B^2/(1-I)).
    Computed by compositional DP, independently of bitstring enumeration.
    """
    m=n-1
    out=Counter({m+4:6}) # one run, two signs, three starting letters
    def interiors(total, excess):
        # choose any sequence of interior runs of lengths >=2
        if total==0:
            yield excess
            return
        for L in range(2,total+1):
            for e in interiors(total-L,excess+L-2+(L==3)):
                yield e
    for l in range(1,m):
        for r in range(1,m-l+1):
            total=m-l-r
            for extra in interiors(total,l-1+r-1):
                out[4+extra]+=6
    return out

if __name__=='__main__':
    for n in range(3,13):
        a,b,c=direct(n),formula(n),from_gf(n)
        assert a==b==c,(n,a,b,c)
        m=n-1
        support=({4}|set(range(6,m+3))|{m+4} if m%2==0
                 else set(range(5,m+3))|{m+4})
        assert set(a)==support,(n,a,support)
        assert a[m+4]==6
        assert a[min(a)]==(6 if m%2==0 else 12)
        print(n,dict(sorted(a.items())))
    print('PASS: exact enumeration, run formula, generating function, support/extremizers n=3..12')
