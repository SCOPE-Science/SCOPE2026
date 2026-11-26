"""Exact, standard-library verification of the finite certificates in RESULT.md."""
from collections import deque
from fractions import Fraction
MAX_N=8194
terms=[1,1]
for n in range(1,MAX_N):
    num=(2*n+1)*terms[n]+3*n*terms[n-1]
    assert num%(n+1)==0
    terms.append(num//(n+1))
def ct(n):return terms[n]

def f(p,a):return (3*a if p else a)%8

def g(p,a):return (-a if p else a)%8

def step(state,bit):
    p,a,b=state
    return (0,f(p,a),g(p,a)) if bit==0 else (1,g(p,a),f(1-p,b))

for n in range(0,4096):
    a,b=ct(n)%8,ct(n+1)%8
    assert (ct(2*n)%8,ct(2*n+1)%8)==(f(n%2,a),g(n%2,a))
    assert step((n%2,a,b),0)==(0,ct(2*n)%8,ct(2*n+1)%8)
    assert step((n%2,a,b),1)==(1,ct(2*n+1)%8,ct(2*n+2)%8)

start=(0,1,1)
seen={start}; todo=deque([start])
while todo:
    s=todo.popleft()
    for bit in (0,1):
        t=step(s,bit)
        if t not in seen:
            seen.add(t);todo.append(t)
S=sorted(seen);assert len(S)==24
assert sum(s[0]==0 for s in S)==8
assert all(s[1]%2==1 and s[2]%2==1 for s in S)
assert all(s[1]%4==s[2]%4 for s in S if s[0]==0)
for root in S:
    reached={root};todo=deque([root])
    while todo:
        s=todo.popleft()
        for bit in (0,1):
            t=step(s,bit)
            if t not in reached:
                reached.add(t);todo.append(t)
    assert len(reached)==24
idx={s:i for i,s in enumerate(S)};size=len(S)
A=[[0]*size for _ in range(size)]
for s in S:
    for bit in (0,1):A[idx[step(s,bit)]][idx[s]]+=1

def multiply(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]
def plus(X,Y,c=1):
    return [[X[i][j]+c*Y[i][j] for j in range(size)] for i in range(size)]
def scale(X,c):return [[c*v for v in row] for row in X]
I=[[int(i==j) for j in range(size)] for i in range(size)]
A2=multiply(A,A)
# The displayed matrix annihilator bounds all non-Perron eigenvalues by sqrt(2).
polys=[A,A,A,plus(A,I,-1),plus(A,I),plus(A,scale(I,2),-1),
       plus(A2,scale(I,2),-1),plus(plus(A2,scale(A,2),-1),scale(I,2))]
P=I
for X in polys:P=multiply(P,X)
assert all(v==0 for row in P for v in row)
# 48 times the exact stationary distribution: every entry is a positive integer.
w=[3 if s[0]==0 else (1 if s[1]%4==s[2]%4 else 2) for s in S]
assert sum(w)==48
assert all(sum(A[i][j]*w[j] for j in range(size))==2*w[i] for i in range(size))
for a in (1,3,5,7):
    for b in (1,3,5,7):
        weight=sum(w[i] for i,s in enumerate(S) if s[1:]==(a,b))
        assert weight==(4 if a%4==b%4 else 2)

def mv(X,v):return [sum(X[i][j]*v[j] for j in range(size)) for i in range(size)]
initial=[int(s==start) for s in S]
v=initial
anchor=[]
for depth in range(1,25):
    v=mv(A,v)
    if depth in (8,16,24):
        a=sum(v[i] for i,s in enumerate(S) if s[1]==1)
        assert a==2**(depth-2)+2**(depth//2-1)
        anchor.append((depth,a))
assert anchor==[(8,72),(16,16512),(24,4196352)]
print('VERIFY_OK 24_states 4096_recurrence_cases polynomial_annihilator stationary_48 anchors',anchor)
