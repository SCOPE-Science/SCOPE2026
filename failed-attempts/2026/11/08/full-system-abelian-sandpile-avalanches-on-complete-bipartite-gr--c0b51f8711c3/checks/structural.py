"""Checks maximal-avalanche/recurrent-auxiliary bijection & rational Green function.
Run with python3 checks/structural.py. Standard library only.
"""
from fractions import Fraction as Q
from itertools import product


def graph(a,b):
    m=a-1
    nbr=[tuple(range(m,m+b)) for _ in range(m)]
    nbr += [tuple(range(m)) for _ in range(b)]
    return nbr,[b]*m+[a]*b


def rec_burn(x,nbr,deg,which_part):
    # Sink is in A if which_part[0]=='A', else in B.
    n=len(x); part,split=which_part
    pending=set(range(n)); z=list(x)
    for i in range(n):
        if part=='A':
            # sink A is adjacent to every B: B are indexed after A nonsinks.
            if i>=split:z[i]+=1
        else:
            # sink B is adjacent to every A: A indexed before B nonsinks.
            if i<split:z[i]+=1
    while True:
        options=[v for v in pending if z[v]>=deg[v]]
        if not options:break
        v=options[0];pending.remove(v);z[v]-=deg[v]
        for u in nbr[v]:z[u]+=1
    assert len(pending)==0 or all(z[v]<deg[v] for v in pending)
    return not pending


def rec_A(x,a,b):
    nbr,deg=graph(a,b)
    return rec_burn(x,nbr,deg,('A',a-1))


def rec_H(x,a,b):
    # H=K_(a-1,b), B's t is sink; H nonsink A has a-1 vertices and Bother b-1.
    m=a-1; N=m+(b-1)
    nbr=[tuple(range(m,N)) for _ in range(m)]
    nbr += [tuple(range(m)) for _ in range(b-1)]
    deg=[b]*m+[a-1]*(b-1)
    return rec_burn(x,nbr,deg,('B',m))


def stabilize(x,nbr,deg):
    x=list(x);od=[0]*len(x)
    while True:
        avail=[i for i in range(len(x)) if x[i]>=deg[i]]
        if not avail:return od
        i=avail[0];x[i]-=deg[i];od[i]+=1
        for j in nbr[i]:x[j]+=1


def gauss(A, y):
    A=[[Q(v) for v in row]+[Q(t)] for row,t in zip(A,y)]
    n=len(A)
    for i in range(n):
        pivot=next(k for k in range(i,n) if A[k][i]!=0)
        A[i],A[pivot]=A[pivot],A[i]
        div=A[i][i];A[i]=[v/div for v in A[i]]
        for j in range(n):
            if j==i:continue
            k=A[j][i]
            if k:A[j]=[u-k*v for u,v in zip(A[j],A[i])]
    return [row[-1] for row in A]


def run(a,b):
    m=a-1;N=m+b; t=m
    nbr,deg=graph(a,b)
    # Independently enumerate all auxiliary recurrent configurations.
    Hdeg=[b]*m+[a-1]*(b-1)
    good=0
    for y in product(*(range(v) for v in Hdeg)):
        if not rec_H(y,a,b):continue
        good+=1
        x=list(y[:m])+[a-1]+[v+1 for v in y[m:]]
        assert rec_A(x,a,b)
        z=list(x);z[t]+=1
        assert stabilize(z,nbr,deg)==[1]*N
    assert good==b**(a-2)*(a-1)**(b-1),(a,b,good)
    # Exact rational Green function, not a Monte Carlo mean.
    lap=[[deg[i]*(i==j)-int(j in nbr[i]) for j in range(N)] for i in range(N)]
    e=[int(i==t) for i in range(N)]
    od_mean=gauss(lap,e)
    expect=[Q(1,b)]*m+[Q(a+b-1,a*b) if j==0 else Q(a-1,a*b) for j in range(b)]
    assert od_mean==expect,(a,b,od_mean,expect)
    assert sum(od_mean)==Q(a+b-1,b)
    return a,b,good,sum(od_mean)


if __name__=='__main__':
    tests=[(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3)]
    for a,b in tests:print('PASS',run(a,b))
    print('STRUCTURAL_GREEN_OK',len(tests))
