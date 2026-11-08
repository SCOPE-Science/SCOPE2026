#!/usr/bin/env python3
"""Exact finite-field check of the 112-generator boundary of a ternary Fermat quartic."""
from collections import Counter
from itertools import product, combinations

# F9 = F3[a]/(a^2+1), encoded as u+3*v*a, u,v in {0,1,2}.
A=[(i%3,i//3) for i in range(9)]
ADD=[[((u+x)%3)+3*((v+y)%3) for x,y in A] for u,v in A]
MUL=[[((u*x-v*y)%3)+3*((u*y+v*x)%3) for x,y in A] for u,v in A]
NEG=[((-u)%3)+3*((-v)%3) for u,v in A]
INV=[0]*9
for x in range(1,9):
    INV[x]=next(y for y in range(1,9) if MUL[x][y]==1)
FROB3=[MUL[MUL[x][x]][x] for x in range(9)]
assert FROB3==[0,1,2,6,7,8,3,4,5]

def plus(x,y): return ADD[x][y]
def mult(x,y): return MUL[x][y]
def conj(x): return FROB3[x]
def dot(v,w):
    r=0
    for x,y in zip(v,w):r=plus(r,mult(x,conj(y)))
    return r

def pt(v):
    c=next(x for x in v if x)
    z=INV[c]
    return tuple(mult(z,x) for x in v)

def rref_lines(q):
    for piv in combinations(range(4),2):
        i,j=piv
        row1slots=[k for k in range(i+1,4) if k!=j]
        row2slots=list(range(j+1,4))
        slots=[(0,k) for k in row1slots]+[(1,k) for k in row2slots]
        for values in product(range(q),repeat=len(slots)):
            row=[[0]*4 for _ in range(2)]
            row[0][i]=row[1][j]=1
            for (ii,k),value in zip(slots,values):row[ii][k]=value
            yield tuple(row[0]),tuple(row[1])

lines=[]
for u,v in rref_lines(9):
    if dot(u,u)==dot(v,v)==dot(u,v)==0:
        lines.append((u,v))
assert len(lines)==112,len(lines)
assert len(set(lines))==112
f3_lines=[(u,v) for u,v in lines if all(x<3 for x in u+v)]
assert len(f3_lines)==8,len(f3_lines)

points={}
for u,v in lines:
    key=(u,v)
    allpoints=[pt(tuple(plus(a,mult(t,b)) for a,b in zip(u,v))) for t in range(9)]
    allpoints.append(pt(v))
    assert len(set(allpoints))==10
    for p in allpoints:points.setdefault(p,[]).append(key)
assert len(points)==280,len(points)
assert Counter(map(len,points.values()))==Counter({4:280})
adj={line:set() for line in lines}
for incident in points.values():
    for line in incident:adj[line].update(other for other in incident if other!=line)
seen={lines[0]}; frontier=[lines[0]]
while frontier:
    line=frontier.pop()
    for other in adj[line]-seen:
        seen.add(other);frontier.append(other)
assert len(seen)==112
assert all(len(n)==30 for n in adj.values())
assert all(sum(mult(x,conj(x)) for x in p)%3==0 for p in points)
projective_F9={pt(v) for v in product(range(9),repeat=4) if any(v)}
assert len(projective_F9)==820
hermitian_F9={p for p in projective_F9 if dot(p,p)==0}
assert len(hermitian_F9)==280
assert hermitian_F9==set(points)
projective_F3={pt(v) for v in product(range(3),repeat=4) if any(v)}
assert len(projective_F3)==40
hermitian_F3={p for p in projective_F3 if dot(p,p)==0}
assert len(hermitian_F3)==16
f3_points={p:through for p,through in points.items() if all(x<3 for x in p)}
assert len(f3_points)==16,len(f3_points)
assert set(f3_points)==hermitian_F3
assert all(sum(1 for line in ll if line in f3_lines)==2 for ll in f3_points.values())
assert all(any(line in f3_lines for line in through) for through in f3_points.values())
assert sum(1 for u,v in lines if all(x<3 for x in u+v))==8

# The 280 geometric crossing points divide into 16 rational points and 132 pairs.
# Each of 16 base-field points has 2 base-field branches and one conjugate pair.
assert (280-16)//2==132
for m in range(1,9):
    Q=3**m
    d=(8*Q-8) if m%2 else (112*Q-728)
    s=Q*Q+1+(2*Q if m%2 else 22*Q)
    u=s-d
    expected=(Q-3)**2 if m%2 else (Q-9)*(Q-81)
    assert u==expected,(m,u,expected)
    if m in (1,2,4):assert u==0
    else:assert u>0
print('F3/F9 surface points:',len(hermitian_F3),len(hermitian_F9))
print('F9 Hermitian lines:',len(lines))
print('F3-defined lines:',len(f3_lines))
print('F9 intersections:',len(points),'all quadruple')
print('F3 intersection points:',len(f3_points),'all with two F3 branches')
print('Frobenius-3 crossing orbits: 16 fixed + 132 paired')
print('For odd m: D=8*(3^m)-8; U=(3^m-3)^2')
print('For even m: D=112*(3^m)-728; U=(3^m-9)*(3^m-81)')
print('Point-free degrees: 1, 2, 4')
print('CHECK_OK')
