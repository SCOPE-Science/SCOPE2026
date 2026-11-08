#!/usr/bin/env python3
"""Exact arithmetic checks for the Stern-polynomial monicity transfer theorem.
No dependencies beyond the Python standard library.
"""
from collections import deque

S0=(1,1,1)

def step(s, bit):
    d,a,b=s
    c=a if d==-1 else b if d==1 else 0
    if bit==0:
        return (max(0,d)-1,a,c)
    return (d+1-max(0,d),c,b)

q=deque([S0]); states={S0}
while q:
    s=q.popleft()
    for bit in (0,1):
        t=step(s,bit)
        if t not in states:
            states.add(t);q.append(t)
assert len(states)==10
ordered=sorted(states)
# Represent polynomials in z as coefficient tuples.
def add(*terms):
    out=[0]*max(map(len,terms))
    for t in terms:
        for j,x in enumerate(t):out[j]+=x
    return tuple(out)
def mul(x,y):
    out=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):out[i+j]+=a*b
    return tuple(out)
def shift(a):return (0,)+a

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)
Q=(1,-1,-1,-1)
R=mul((1,-1),Q)
Nw={
 (-1,0,0):(0,),(-1,1,0):(1,0,-1,-1),(-1,1,1):(1,0,-1),
 (0,0,0):(0,),(0,0,1):(0,0,1),(0,1,0):(1,-1,0,-1),
 (0,1,1):(1,-1,1,-1),(1,0,0):(0,),(1,0,1):(0,1),(1,1,1):(1,0,-1),
}
Nc={
 (-1,0,0):(0,),(-1,1,0):(1,-1),(-1,1,1):(1,-1,1,-1),
 (0,0,0):(0,),(0,0,1):(0,1,-1),(0,1,0):(0,1,-1),
 (0,1,1):(0,2,-2),(1,0,0):(0,),(1,0,1):(1,-1),
 (1,1,1):(1,-1,1,-1),
}
assert set(Nw)==set(Nc)==states
for s in ordered:
    for nums,obs in [(Nw,s[1]),(Nc,step(s,1)[1])]:
        left=trim(nums[s]); right=trim(add(tuple(obs*x for x in R),shift(nums[step(s,0)]),shift(nums[step(s,1)])))
        assert left==right,(s,nums==Nw,left,right)
assert trim(Nw[S0])==trim(mul((1,-1),(1,1)))
assert trim(Nc[S0])==trim(mul((1,-1),(1,0,1)))
# Enumerate from initial state: double one binary word each step.
counts={S0:1}; U=[]; V=[]
for k in range(1,23):
    u=sum(count for st,count in counts.items() if st[1])
    if k==1:
        v=1
    else:
        v=sum(count for st,count in prev_counts.items() if step(st,1)[1])
    U.append(u);V.append(v)
    if k>=4: assert U[-1]==sum(U[-4:-1]);assert V[-1]==sum(V[-4:-1])
    prev_counts=counts.copy()
    new={}
    for st,count in counts.items():
        for bit in (0,1):
            dst=step(st,bit)
            new[dst]=new.get(dst,0)+count
    counts=new
assert U[:10]==[1,2,3,6,11,20,37,68,125,230]
assert V[:10]==[1,1,1,3,5,9,17,31,57,105]
# Independently compute actual Stern polynomials via dense coefficients, and compare with binary digit state.
N=32768
poly=[()] * (N+1)
poly[0]=(0,);poly[1]=(1,)
for n in range(2,N+1):
    if n%2==0:poly[n]=(0,)+poly[n//2]
    else:
        a,b=poly[n//2],poly[n//2+1]
        poly[n]=tuple((a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0) for j in range(max(len(a),len(b))))
for k in range(1,16):
    lo,hi=1<<(k-1),1<<k
    mon=sum(poly[n][-1]==1 for n in range(lo,hi))
    odd_mon=sum(poly[n][-1]==1 for n in range(lo,hi,2) if n%2)
    odd_mon=sum(poly[n][-1]==1 for n in range(lo|1,hi,2))
    assert mon==U[k-1],(k,mon,U[k-1])
    assert odd_mon==V[k-1],(k,odd_mon,V[k-1])
for n in range(1,N):
    s=S0
    for bit in bin(n)[3:]:s=step(s,int(bit))
    d=len(poly[n+1])-len(poly[n])
    a=int(poly[n][-1]==1);b=int(poly[n+1][-1]==1)
    assert (d,a,b)==s, (n,s,d,a,b)
print('VERIFY_OK reachable_states=10 formal_transfer_identites=20 polynomial_indices=32767 exact_block_levels=22 monic_prefix='+str(U[:9])+' odd_monic_prefix='+str(V[:9]))
