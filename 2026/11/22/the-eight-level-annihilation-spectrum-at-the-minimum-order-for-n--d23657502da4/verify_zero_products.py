"""Independent finite multiplication checks for minimum-order centrally essential rings.

The representative parameter families are from Abyzov--Lyubimtsev--Tuganbaev,
'Minimal Finite Non-Commutative Centrally Essential Rings', arXiv:2611.16086,
Tables 1--3 and Propositions 4.1--4.3. For each representative the checker counts
zero products in the 32-element radical; 64 pairs outside its square account
for a zero factor involving a unit in the 64-element ring.
"""
from collections import Counter
from itertools import product

F1 = [
    ((0,0),(0,1)), ((0,0),(1,1)), ((1,0),(0,0)),
    ((1,0),(1,0)), ((0,0),(0,0)), ((1,0),(0,1)),
    ((0,1),(0,0)), ((0,1),(1,0)), ((0,1),(0,1)),
    ((0,1),(1,1))
]
F2 = [(0,0), (1,1)]
F3 = [
    ((1,0,0,0),(0,0)), ((1,0,0,0),(0,1)),
    ((0,1,0,0),(0,0)), ((0,1,0,0),(0,1)),
    ((0,1,1,0),(0,0)), ((1,1,1,0),(0,0)),
    ((1,1,0,1),(0,0))
]
F4_outside = [
    ((0,0,0,0),[(0,0),(0,1),(1,1)]),
    ((1,0,0,0),[(0,0),(0,1),(1,1)]),
    ((0,1,1,0),[(0,0),(0,1)]),
    ((1,1,1,0),[(0,0),(0,1)]),
    ((0,1,0,0),[(0,0),(0,1)]),
    ((0,0,1,0),[(0,0),(1,0),(0,1),(1,1)]),
    ((0,0,0,1),[(0,0),(1,0)]),
    ((1,0,0,1),[(0,0),(1,0)]),
    ((0,1,0,1),[(0,0),(0,1)]),
    ((1,0,1,1),[(0,0),(1,0)])
]

F2_5 = list(product(range(2), repeat=5))
F4_3 = list(product(range(4),range(4),range(2)))
F4_4 = list(product(range(4),range(2),range(2),range(2)))


def addmod(pairs,mods):
    return tuple(sum(val for val in pairs[j]) % mods[j] for j in range(len(mods)))

def bilinear(x,y,table,mods):
    n=len(mods)
    z=[0]*n
    for i,u in enumerate(x):
        for j,v in enumerate(y):
            if u and v:
                t=table.get((i,j),(0,)*n)
                for k in range(n): z[k] += u*v*t[k]
    return tuple(z[k]%mods[k] for k in range(n))

def radical_zero_count(elems,table,mods):
    z=(0,)*len(mods)
    return sum(bilinear(a,b,table,mods)==z for a in elems for b in elems)

def fam1_binary(alpha,beta):
    # a,b,c,s1,s2; every coefficient has order two.
    n=5; T={}
    def put(i,j,k): T[i,j]=tuple(k)
    put(0,0,(0,0,0,*alpha))
    put(1,1,(0,0,0,*beta))
    put(0,1,(0,0,0,1,0))
    for i,j,k in [(0,2,3),(2,0,3),(1,2,4),(2,1,4)]:
        z=[0]*n;z[k]=1;put(i,j,z)
    return radical_zero_count(F2_5,T,(2,)*5)

def fam23_binary(lam,alpha,beta):
    # a,b,c1,c2,w; all coefficients have order two.
    l1,l2,l3,l4=lam
    T={(0,0):(0,0,l1,l2,alpha),
       (0,1):(0,0,l2,l3,1), (1,0):(0,0,l2,l3,0),
       (1,1):(0,0,l3,l4,beta)}
    for i,j in [(0,2),(2,0),(1,3),(3,1)]:T[i,j]=(0,0,0,0,1)
    return radical_zero_count(F2_5,T,(2,)*5)

def fam1_char4_outside(alpha,beta):
    # J=Z4 a + Z4 b + Z2 c, 2a=s1,2b=s2,c=2*1.
    # Every product belongs to 2Z4 a + 2Z4 b.
    T={(0,0):(2*alpha[0],2*alpha[1],0),
       (1,1):(2*beta[0],2*beta[1],0),
       (0,1):(2,0,0),
       (0,2):(2,0,0),(2,0):(2,0,0),
       (1,2):(0,2,0),(2,1):(0,2,0)}
    return radical_zero_count(F4_3,T,(4,4,2))

def fam23_char4_outside(lam,alpha,beta):
    # J=Z4 a + Z2 b + Z2 c1 + Z2 c2, 2a=w; c1=2*1.
    l1,l2,l3,l4=lam
    T={(0,0):(2*alpha,0,l1,l2),
       (0,1):(2,0,l2,l3), (1,0):(0,0,l2,l3),
       (1,1):(2*beta,0,l3,l4)}
    for i,j in [(0,2),(2,0),(1,3),(3,1)]:T[i,j]=(2,0,0,0)
    return radical_zero_count(F4_4,T,(4,2,2,2))

def q_first_family(alpha,beta):
    add=lambda x,y: (x[0]^y[0],x[1]^y[1])
    return int(alpha in ((0,0),(1,0))) + int(beta in ((0,0),(0,1))) + int(add(add(alpha,beta),(1,0)) in ((0,0),(1,1)))

def rank2(x):
    a,b=x[0];c,d=x[1]
    return 2 if (a*d-b*c)&1 else (1 if (a|b|c|d) else 0)

def cubic_N(lam):
    p,q,r,s=lam
    return sum(2**(2-rank2(((x*p^y*q,x*q^y*r),(x*q^y*r,x*r^y*s)))) for x,y in product(range(2),repeat=2))

def count():
    actual=Counter(); detail=[]
    def record(label,zeroJ,expect):
        n=zeroJ+64
        assert n == expect,(label,n,expect)
        actual[n]+=1;detail.append((label,n))
    # Characteristic 2: 10+2+7=19.
    for i,(a,b) in enumerate(F1,1):record('char2-family1-%02d'%i,fam1_binary(a,b),416+32*q_first_family(a,b))
    for i,(a,b) in enumerate(F2,1):record('char2-family2-%02d'%i,fam23_binary((0,0,0,0),a,b),608)
    for i,(la,(a,b)) in enumerate(F3,1):record('char2-family3-%02d'%i,fam23_binary(la,a,b),32*cubic_N(la)+96)
    # Characteristic 4, with 2*1 inside W0: 10+16+2+7=35.
    for i,(a,b) in enumerate(F1,1):record('char4-inW-comm-%02d'%i,fam1_binary(a,b),416+32*q_first_family(a,b))
    for i,(a,b) in enumerate(product(tuple(product(range(2),repeat=2)),repeat=2),1):
        record('char4-inW-noncomm-%02d'%i,fam1_binary(a,b),416+32*q_first_family(a,b))
    for i,(a,b) in enumerate(F2,1):record('char4-inW-family2-%02d'%i,fam23_binary((0,0,0,0),a,b),608)
    for i,(la,(a,b)) in enumerate(F3,1):record('char4-inW-family3-%02d'%i,fam23_binary(la,a,b),32*cubic_N(la)+96)
    # Characteristic 4, 2*1 outside W0 and dim W0=2: 10 representatives.
    for i,(a,b) in enumerate(F1,1):record('char4-outW-dim2-%02d'%i,fam1_char4_outside(a,b),416+32*q_first_family(a,b))
    # Characteristic 4, 2*1 outside W0 and dim W0=1: 24 representatives.
    for i,(la,params) in enumerate(F4_outside,1):
        for j,(a,b) in enumerate(params,1):
            expected=608 if la == (0,0,0,0) else 32*cubic_N(la)+96
            record('char4-outW-dim1-%02d-%02d'%(i,j),fam23_char4_outside(la,a,b),expected)
    expected={320:8,352:12,384:6,416:5,448:18,480:24,512:8,608:7}
    assert dict(actual)==expected, (actual,expected)
    assert len(detail)==88
    print('MINIMAL_CENTRAL_ESSENTIAL_ZERO_PAIRS_OK',len(detail))
    print('zero_pair_count : isomorphism_class_count')
    for k in sorted(actual):print(k,actual[k])
    return detail

if __name__=='__main__':count()
