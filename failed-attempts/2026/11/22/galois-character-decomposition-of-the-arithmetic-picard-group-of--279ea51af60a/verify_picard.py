"""Exact rational certificate for the Picard-character decomposition of a split quartic K3 surface.
Run with Python 3, no third-party dependencies. All operations are integral or rational.
"""
from fractions import Fraction
from itertools import product

N=48
lines=[(t,m,n) for t in range(3) for m in range(4) for n in range(4)]

def exps(line):
    t,m,n=line
    eps=(t==1)
    return 2*m+int(eps),2*n+int(eps)

def meets(a,b):
    # Two distinct lines on A^4-B^4+C^4-D^4=0.
    t,m,n=a;u,p,q=b
    if t==u:
        return int(m==p or n==q)
    if t>u:
        a,b=b,a;t,u=u,t
    x,y=exps(a);v,w=exps(b)
    if (t,u)==(0,1):
        return int((x+w-y-v)%8==0)
    if (t,u)==(0,2):
        return int((x+w+y-v)%8==0)
    assert (t,u)==(1,2)
    return int((x+y-v-w)%8==0)

def act(idx,r):
    t,m,n=lines[idx]
    eps=int(t==1)
    return 16*t+4*((r*(2*m+eps)-eps)//2%4)+((r*(2*n+eps)-eps)//2%4)

def rank(matrix):
    # Exact row reduction over Q; never a modular heuristic.
    M=[list(map(Fraction,row)) for row in matrix]
    h=len(M);w=len(M[0]);i=0
    for j in range(w):
        p=next((k for k in range(i,h) if M[k][j]),None)
        if p is None: continue
        M[p],M[i]=M[i],M[p]
        v=M[i][j]
        M[i]=[x/v for x in M[i]]
        for k in range(i+1,h):
            if not M[k][j]:continue
            q=M[k][j]
            M[k]=[x-q*y for x,y in zip(M[k],M[i])]
        i+=1
        if i==h:break
    return i

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

G=[[-2 if i==j else meets(lines[i],lines[j]) for j in range(N)] for i in range(N)]
assert all(G[i][j]==G[j][i] for i in range(N) for j in range(N))
assert {sum(G[i][j] for j in range(N) if j!=i) for i in range(N)}=={14}
assert rank(G)==20
chars={
    'trivial':{1:1,3:1,5:1,7:1},
    'i':{1:1,3:-1,5:1,7:-1},
    'sqrt2':{1:1,3:-1,5:-1,7:1},
    'sqrt(-2)':{1:1,3:1,5:-1,7:-1},
}
char_ranks={}
for name,character in chars.items():
    P=[[0]*N for _ in range(N)]
    for j in range(N):
        for r in (1,3,5,7):
            P[act(j,r)][j]+=character[r]
    a=rank(matmul(G,P))
    char_ranks[name]=a
assert char_ranks=={'trivial':9,'i':7,'sqrt2':2,'sqrt(-2)':2}
assert sum(char_ranks.values())==20

H_groups={
 'Q':(1,3,5,7),
 'Q(i)':(1,5),
 'Q(sqrt2)':(1,7),
 'Q(sqrt(-2))':(1,3),
 'Q(zeta8)':(1,),
}
for name,H in H_groups.items():
    remaining=set(range(N));orbits=[]
    while remaining:
        j=min(remaining)
        orbit=tuple(sorted(set(act(j,r) for r in H)))
        assert all(act(i,r) in orbit for i in orbit for r in H)
        remaining.difference_update(orbit)
        orbits.append(orbit)
    B=[[int(i in orbit) for orbit in orbits] for i in range(N)]
    T=matmul(list(zip(*B)),matmul(G,B))
    expected={'Q':9,'Q(i)':16,'Q(sqrt2)':11,'Q(sqrt(-2))':11,'Q(zeta8)':20}[name]
    assert rank(T)==expected
    print(name,'Galois-line-orbits',len(orbits),'fixed-class-rank',expected)

print('Picard-character dimensions:',char_ranks)
print('Galois traces for r=1,3,5,7:',[sum(char_ranks[name]*character[r] for name,character in chars.items()) for r in (1,3,5,7)])
print('PASS: all rational ranks, incidence and character identities verified')
