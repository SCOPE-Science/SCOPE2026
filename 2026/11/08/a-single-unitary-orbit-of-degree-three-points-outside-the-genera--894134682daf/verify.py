"""Exact GF(64) check of degree-three off-generator Hermitian surface points.
GF(64)=F_2[z]/(z^6+z+1). Pure standard-library finite-field arithmetic.
"""
from collections import Counter
MOD=0x43

def mul(a,b):
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&64: a^=MOD
    return z

M=[[mul(a,b) for b in range(64)] for a in range(64)]
def power(a,n):
    out=1
    while n:
        if n&1: out=M[out][a]
        a=M[a][a];n>>=1
    return out
INV=[0]+[power(i,62) for i in range(1,64)]
P3=[i for i in range(64)]
POW3=[power(i,3) for i in P3]
POW4=[power(i,4) for i in P3]
POW16=[power(i,16) for i in P3]
F4=[i for i in P3 if POW4[i]==i]
assert len(F4)==4

def rank(v):
    R=[list(v),[POW4[x] for x in v],[POW16[x] for x in v]]
    r=0
    for c in range(4):
        j=next((j for j in range(r,3) if R[j][c]),None)
        if j is None: continue
        R[r],R[j]=R[j],R[r]
        inv=INV[R[r][c]]
        R[r]=[M[inv][x] for x in R[r]]
        for j in range(3):
            if j!=r and R[j][c]:
                k=R[j][c]
                R[j]=[a^M[k][b] for a,b in zip(R[j],R[r])]
        r+=1
        if r==3: break
    return r

def points():
    for x in P3:
      for y in P3:
       for z in P3:
        if 1^POW3[x]^POW3[y]^POW3[z]==0:
          yield (1,x,y,z)
    for y in P3:
      for z in P3:
        if 1^POW3[y]^POW3[z]==0:
          yield (0,1,y,z)
    for z in P3:
      if 1^POW3[z]==0:
        yield (0,0,1,z)
    # (0,0,0,1) is not on X

def planes():
    # normalized projective vectors over F4
    for a in F4:
      for b in F4:
       for c in F4:
        yield (1,a,b,c)
    for b in F4:
      for c in F4: yield (0,1,b,c)
    for c in F4: yield (0,0,1,c)
    yield (0,0,0,1)

PL=list(planes())
assert len(PL)==85
TAN=set(a for a in PL if sum(int(x!=0) for x in a)%2==0)
assert len(TAN)==45
counts=Counter()
incidence=Counter()
for v in points():
    r=rank(v); counts[r]+=1
    if r==3:
        matches=[a for a in PL if (M[a[0]][v[0]] ^ M[a[1]][v[1]] ^ M[a[2]][v[2]] ^ M[a[3]][v[3]])==0]
        assert len(matches)==1
        assert matches[0] not in TAN
        incidence[matches[0]]+=1
assert counts=={1:45,2:1620,3:2880},counts
assert len(incidence)==40
assert set(incidence.values())=={72}
print('VERIFY_HERMITIAN_ORBIT_OK', 'X_F64=',sum(counts.values()),'ranks=',dict(counts), 'secant_planes=',len(incidence), 'off_line_each=',set(incidence.values()))
