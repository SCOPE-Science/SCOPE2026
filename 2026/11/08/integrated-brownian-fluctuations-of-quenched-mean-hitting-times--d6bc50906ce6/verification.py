"""Standalone finite and exact checks for a Bernoulli-generated comb tree.
Run: python3 verification.py
Standard-library only; finite tests supplement, not prove, limit assertions.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose
import random

checks = 0

def verify(condition, message):
    global checks
    assert condition, message
    checks += 1


def tree_from_bits(bits):
    # bits[0]=1, bits[j] decides whether v_{j+1} joins v_j.
    N = len(bits)+1
    parent = [-1, 0]
    for i in range(2, N):
        parent.append(i-1 if bits[i-1] else i-2)
    spine = []
    t = N-1
    while t >= 0:
        spine.append(t)
        t = parent[t]
    spine.reverse()
    roots = set(spine)
    L = {j:0 for j in spine}
    for j in range(N):
        if j not in roots:
            t=j
            while t not in roots:
                t=parent[t]
            L[t]+=1
    return parent,spine,L


def hit_expectation(parent,target):
    n=len(parent)
    nei=[[] for _ in range(n)]
    for v in range(1,n):
        u=parent[v]
        nei[u].append(v);nei[v].append(u)
    vertices=[i for i in range(n) if i!=target]
    M=[]; b=[]
    for u in vertices:
        M.append([F(len(nei[u]) if u==v else -int(v in nei[u])) for v in vertices])
        b.append(F(len(nei[u])))
    for i in range(len(vertices)):
        z=next(j for j in range(i,len(vertices)) if M[j][i])
        M[i],M[z]=M[z],M[i];b[i],b[z]=b[z],b[i]
        div=M[i][i];M[i]=[x/div for x in M[i]];b[i]/=div
        for j in range(len(vertices)):
            if j!=i:
                c=M[j][i]
                if c:
                    M[j]=[x-c*y for x,y in zip(M[j],M[i])]
                    b[j]-=c*b[i]
    return b[vertices.index(0)]

# Exhaust all early construction decisions and independently solve hitting equations.
for n in range(3,10):
    for tail in product((0,1), repeat=n-2):
        bits=(1,)+tail
        parent,spine,L=tree_from_bits(bits)
        ones=[j for j in range(len(bits)) if bits[j]]
        for a,b in zip(ones,ones[1:]):
            k=b-a-1
            verify(L[a]==(k+1)//2, 'tooth length from next success')
            verify(spine.index(b)-spine.index(a)==k//2+1, 'spine advance between successes')
        for m in range(1,len(spine)):
            tree_formula=m*m+2*sum((m-i)*L[spine[i]] for i in range(m))
            direct=hit_expectation(parent,spine[m])
            verify(direct==tree_formula, 'exact hitting equation')

# A/H regenerative centered reward has exact variance q/(1+q).
for den in range(2,14):
    for num in range(1,den):
        q=F(num,den);p=1-q;z=q*q
        s0=1/(1-z);s1=z/(1-z)**2;s2=z*(1+z)/(1-z)**3
        Ed2=p*((p*p*s2-2*p*q*s1+q*q*s0)+q*p*p*(s2+2*s1+s0))
        EH=1/(p*(1+q))
        EA=q/(p*(1+q))
        verify(EA/EH==q, 'mean reward per spine site')
        verify(Ed2==q/(1+q), 'centered block reward variance')
        verify(Ed2/EH==p*q, 'variance per spine site')

# Seeded Monte Carlo is a diagnostic, not an infinite-limit proof.
rng=random.Random(20261106)
q=F(3,5);p=1-q;m=400
ys=[]
for _ in range(900):
    L=[0]*m;h=0
    while h<m:
        k=0
        while rng.random()<float(q):k+=1
        L[h]=(k+1)//2
        h+=(k//2+1)
    ht=m*m+2*sum((m-j)*L[j] for j in range(m))
    ys.append((ht-(1+float(q))*m*m)/m**1.5)
av=sum(ys)/len(ys)
vv=sum((y-av)**2 for y in ys)/len(ys)
verify(abs(av)<0.15, 'simulated centered fluctuation mean')
verify(abs(vv-4*float(p*q)/3)<0.12, 'simulated fluctuation variance')
print('PASS',checks-2,'exact/finite assertions and 2 simulation diagnostics,',checks,'assertions total')
