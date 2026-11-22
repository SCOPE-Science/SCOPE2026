"""Finite signed-chain checks for a pentagonal lexicographic graph product.

Python 3 standard library only. Exhaustive on 551 faces; all calculations deterministic.
The infinite-family proof is in RESULT.md, not inferred from this finite test.
Outer positions use complementary-cycle order; adjacent outer positions
therefore represent independent fiber pairs in the original five-cycle.
"""
from collections import defaultdict
from itertools import product

PRIME=101

def cycle_independent_faces():
    return [tuple(j for j in range(5) if (m >> j)&1)
            for m in range(32)
            if all(not ((m >> j)&1 and (m >> ((j+1)%5))&1) for j in range(5))]

local=cycle_independent_faces()
faces={()}
for i in range(5):
    j=(i+1)%5
    for a in local:
        for b in local:
            faces.add(tuple(sorted([5*i+x for x in a]+[5*j+y for y in b])))
assert len(faces)==551
by_dim={k:sorted(f for f in faces if len(f)==k+1) for k in range(4)}
assert tuple(map(lambda k:len(by_dim[k]),range(4)))==(25,150,250,125)
index={k:{f:i for i,f in enumerate(by_dim[k])} for k in range(4)}

def sign(seq):
    return (-1)**(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2)

def make_action(eps,shift,bits):
    p=tuple((eps*i+shift)%5 for i in range(5))
    inside=[tuple(((-v if bits[i] else v))%5 for v in range(5)) for i in range(5)]
    action={}
    for k in range(4):
        a=[]
        for f in by_dim[k]:
            g=[5*p[i//5]+inside[i//5][i%5] for i in f]
            a.append((index[k][tuple(sorted(g))],sign(g)))
        action[k]=a
    return p,action

def expected_traces(p,eps,bits):
    chi=[(-1 if b else 1) for b in bits]
    t1=eps
    t2=eps*sum(chi[i] for i in range(5) if p[i]==i)
    t3=sum(chi[i]*chi[(i+1)%5] for i in range(5)
           if {p[i],p[(i+1)%5]}=={i,(i+1)%5})
    return (t1,t2,t3)

def reduced_lefschetz(action):
    total=-1
    for k in range(4):
        total+=(-1)**k*sum(s for i,(j,s) in enumerate(action[k]) if i==j)
    return total

# All 10 outer dihedral elements times 32 independent inner reflection choices.
for eps in (1,-1):
    for shift in range(5):
        for bits in product((0,1),repeat=5):
            p,act=make_action(eps,shift,bits)
            t=expected_traces(p,eps,bits)
            assert reduced_lefschetz(act)==-t[0]+t[1]-t[2]
print('PASS: 320 signed reduced Lefschetz identities on 551 faces')

# Modular boundary image echelon bases; signed homology traces are computed
# independently of the expected representation description.
def image_basis(k):
    basis={}
    for f in by_dim.get(k+1,[]):
        v={index[k][f[:i]+f[i+1:]]:(1 if i%2==0 else PRIME-1)
           for i in range(len(f))}
        while v:
            pivot=max(v)
            if pivot not in basis:
                c=pow(v[pivot],-1,PRIME)
                basis[pivot]={j:(x*c)%PRIME for j,x in v.items()}
                break
            coeff=v[pivot]
            for j,x in basis[pivot].items():
                a=(v.get(j,0)-coeff*x)%PRIME
                if a:v[j]=a
                else:v.pop(j,None)
    return basis

bases={k:image_basis(k) for k in (0,1,2)}
assert tuple(len(bases[k]) for k in (0,1,2))==(24,125,120)
assert tuple(len(by_dim[k])-len(bases.get(k,{}))-len(bases.get(k-1,{}))
             -int(k==0) for k in (0,1,2,3))==(0,1,5,5)

def tr_image(k,act):
    basis=bases[k]
    trace=0
    for pivot,v in basis.items():
        w={}
        for i,coeff in v.items():
            j,sgn=act[k][i]
            w[j]=(w.get(j,0)+coeff*sgn)%PRIME
            if not w[j]:w.pop(j,None)
        diagonal=0
        while w:
            q=max(w)
            assert q in basis
            a=w[q]
            if q==pivot:diagonal=a
            for j,x in basis[q].items():
                z=(w.get(j,0)-a*x)%PRIME
                if z:w[j]=z
                else:w.pop(j,None)
        trace=(trace+diagonal)%PRIME
    return trace

def signed_mod(x):
    x%=PRIME
    return x if x<=PRIME//2 else x-PRIME

samples=((1,0,(0,0,0,0,0)), (1,1,(0,0,0,0,0)),
         (-1,0,(0,0,0,0,0)), (1,0,(1,0,0,0,0)),
         (-1,2,(1,1,0,0,0)), (1,0,(1,1,1,1,1)))
for eps,shift,bits in samples:
    p,act=make_action(eps,shift,bits)
    image_tr={k:tr_image(k,act) for k in (0,1,2)}
    predicted=expected_traces(p,eps,bits)
    actual=tuple(signed_mod(sum(s for i,(j,s) in enumerate(act[k]) if i==j)
                            -image_tr.get(k,0)-image_tr.get(k-1,0))
                 for k in (1,2,3))
    assert actual==predicted,(eps,shift,bits,actual,predicted)
    print(f'PASS homology traces: outer=({eps},{shift}), inner={bits}: {actual}')
print('PASS: six independently computed signed homology characters over F_101')
