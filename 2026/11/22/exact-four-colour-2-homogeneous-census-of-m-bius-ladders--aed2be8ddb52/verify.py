#!/usr/bin/env python3
"""Exact enumeration certificate for 2-homogeneous colourings of Möbius ladders."""
from itertools import product

Q = tuple((a,b) for a in range(4) for b in range(4) if a != b)
S = tuple((u,v) for u in Q for v in Q if u[0]!=v[0] and u[1]!=v[1])
I = {s:i for i,s in enumerate(S)}
assert len(S)==84

def swapped(state):
    (a,b),(c,d)=state
    return ((b,a),(d,c))

def transition(s,t):
    u,v=s
    v2,w=t
    return int(v==v2 and v[0]!=w[0] and v[1]!=w[1]
               and len({u[0],w[0],v[1]})==2
               and len({u[1],w[1],v[0]})==2)

T=[[transition(s,t) for t in S] for s in S]
reps=[]
seen=set()
for i,s in enumerate(S):
    if i not in seen:
        j=I[swapped(s)]
        reps.append((i,j))
        seen.update((i,j))
assert len(reps)==42 and len(seen)==84
P=[[T[i][j]+T[i][k] for j,k in reps] for i,_ in reps]
N=[[T[i][j]-T[i][k] for j,k in reps] for i,_ in reps]
assert sum(sum(row) for row in T)==264

# Monic polynomial coefficients, increasing order in z.
def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def factors(fs):
    v=[1]
    for f,power in fs:
        for _ in range(power):v=multiply(v,f)
    return v

# det(I-zP), det(I-zN), determined by the stated factorization.
A=factors([
    ([1,-1],1),([1,0,1],3),([1,-2,-4],1),([1,-1,2],1),
    ([1,2,4],3),([1,0,-1,-2],3),([1,-1,-3,-3,4,8],2)])
B=factors([
    ([1,-2],1),([1,1],2),([1,-1,1,1],3),
    ([1,1,-1,7,2,0,-16],3)])
assert len(A)==37 and len(B)==31
A += [0]*(43-len(A)); B += [0]*(43-len(B))

def matmul(a,b):
    n=len(a)
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            z=a[i][k]
            if z:
                for j in range(n):out[i][j]+=z*b[k][j]
    return out

def char_coefficients(matrix):
    """Faddeev-LeVerrier: returns coefficients of det(I-zM)."""
    n=len(matrix)
    w=[[int(i==j) for j in range(n)] for i in range(n)]
    c=[1]
    for k in range(1,n+1):
        w=matmul(matrix,w)
        tr=sum(w[i][i] for i in range(n))
        assert tr%k==0, ('integer coefficient',k,tr)
        q=-tr//k
        c.append(q)
        for i in range(n):w[i][i]+=q
    return c

assert char_coefficients(P)==A, 'positive block characteristic polynomial'
assert char_coefficients(N)==B, 'negative block characteristic polynomial'
print('EXACT_CHARACTERISTIC_POLYNOMIALS 42+42 PASS')

# Newton sums of roots from exact det(I-zM) coefficients.
def powers(coeffs,nmax):
    p=[0]*(nmax+1)
    for n in range(1,nmax+1):
        p[n]=-sum(coeffs[k]*p[n-k] for k in range(1,min(n-1,len(coeffs)-1)+1))
        if n<len(coeffs):p[n]-=n*coeffs[n]
    return p

pp=powers(A,35);nn=powers(B,35)
count=[a-b for a,b in zip(pp,nn)]
print("small",count[:4]); assert count[1]==0 and count[2]==0
assert count[3:11]==[216,48,600,720,5544,8160,59400,98880]
print('GENERATING_FUNCTION_COUNTS m=3..35 PASS')

# Independent direct graph-based enumeration, not transfer-based.
def brute(m):
    V=tuple(range(2*m))
    edges=set()
    for j in range(m):
        edges.add(tuple(sorted((2*j,2*j+1))))
        if j+1<m:
            for r in (0,1):edges.add((2*j+r,2*(j+1)+r))
        else:
            edges.add(tuple(sorted((2*j,1))))
            edges.add(tuple(sorted((2*j+1,0))))
    nbr=[set() for _ in V]
    for x,y in edges:nbr[x].add(y);nbr[y].add(x)
    assert len(edges)==3*m and all(len(z)==3 for z in nbr)
    cnt=0
    for cs in product(range(4),repeat=2*m):
        if any(cs[x]==cs[y] for x,y in edges):continue
        if all(len({cs[x] for x in nbr[v]})==2 for v in V):cnt+=1
    return cnt
for m in (3,4,5):
    assert brute(m)==count[m], (m,brute(m),count[m])
    print('DIRECT_GRAPH_ENUMERATION',m,count[m],'PASS')

# Four-colour witnesses for every length, two short twist walks and a 2-loop.
a=((0,1),(2,3))
idx=I[a]
swapidx=I[swapped(a)]
adj=[[j for j,z in enumerate(trow) if z] for trow in T]
def findpath(src,dst,length):
    if length==0:return [src] if src==dst else None
    for j in adj[src]:
        q=findpath(j,dst,length-1)
        if q is not None:return [src]+q
    return None
walk2=findpath(idx,idx,2)
walk3=findpath(idx,swapidx,3)
walk4=findpath(idx,swapidx,4)
assert walk2 and walk3 and walk4
for m in range(3,80):
    base=3 if m%2 else 4
    j=(m-base)//2
    walk=walk2[:-1]*j + (walk3 if base==3 else walk4)
    assert len(walk)==m+1 and walk[0]==idx and walk[-1]==swapidx
    assert all(T[x][y] for x,y in zip(walk,walk[1:]))
print('TWIST_WITNESSES_ALL_PARITIES PASS')

# 3-palette transfer automaton: a twisted walk would be a 3-colour assignment.
C3=tuple((a,b) for a in range(3) for b in range(3) if a!=b)
S3=tuple((u,v) for u in C3 for v in C3 if u[0]!=v[0] and u[1]!=v[1])
I3={s:i for i,s in enumerate(S3)}
Z=[[transition(s,t) for t in S3] for s in S3]
Zr=[[I3[swapped(s)]] for s in S3]
for src in range(len(S3)):
    seen={src};front={src}
    while front:
        new={j for i in front for j,z in enumerate(Z[i]) if z and j not in seen}
        seen |= new;front=new
    assert Zr[src][0] not in seen, 'no 3-colour twisted path, any length'
print('THREE_COLOR_REACHABILITY_OBSTRUCTION ALL_LENGTHS PASS')
Zp=[[int(i==j) for j in range(len(S3))] for i in range(len(S3))]
for n in range(1,55):
    Zp=matmul(Zp,Z)
    assert sum(Zp[i][Zr[i][0]] for i in range(len(S3)))==0
print('THREE_COLOR_TWIST_OBSTRUCTION_CHECK 54 PASS')
print('VERIFY_OK')
