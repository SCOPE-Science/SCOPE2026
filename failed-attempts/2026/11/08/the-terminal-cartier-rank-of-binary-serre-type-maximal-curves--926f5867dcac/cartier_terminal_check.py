#!/usr/bin/env python3
"""Exact symbolic arithmetic checks of Cartier-terminal theorem; no external packages."""
def B(s):
    Q=4**s; m=(2*Q+1)//3
    return [(i,j) for j in range(3) for i in range((2*Q-4-m*j)//4+1)]
def cstep(pair,m):
    if pair is None:return None
    i,j=pair
    if j==0:return ((i-1)//2,0) if i%2 else None
    if j==1:return (i//2+(m-1)//2,0) if i%2==0 else ((i-1)//2,2)
    return ((i-1)//2,1) if i%2 else None

def terminal_theory(s):
    Q=4**s;m=(2*Q+1)//3
    return {((Q-4**t-3)//3,1):((2*(4**t-1)//3),0) for t in range(s)}

def terminal_direct(s):
    Q=4**s;m=(2*Q+1)//3
    out={}
    for i,j in B(s):
        terms=[]
        if j==0:terms=[(i,0)]
        if j==1:terms=[(i,1)]+[(i+m*(4**t),0) for t in range(s)]
        if j==2:terms=[(i,2)]+[(i+2*m*(4**t),0) for t in range(s)]
        survivors=[]
        for e,y_power in terms:
            if e%Q==Q-1:
                survivors.append(((e-Q+1)//Q,y_power//Q))
        if survivors:
            assert len(survivors)==1,(s,i,j,survivors)
            out[(i,j)]=survivors[0]
    return out

def terminal_iterated(s):
    m=(2*4**s+1)//3; out={}
    for p in B(s):
        t=p
        for _ in range(2*s):t=cstep(t,m)
        if t is not None:out[p]=t
    return out

for s in range(1,8):
    wanted=terminal_theory(s)
    assert all(p in B(s) and t in B(s) for p,t in wanted.items())
    assert terminal_direct(s)==wanted
    assert terminal_iterated(s)==wanted
    assert len(set(wanted.values()))==s
    assert all(cstep(t,(2*4**s+1)//3) is None for t in wanted.values())
    print(f'n={2*s+1} genus={4**s-1} terminal_rank={len(wanted)} nilpotency={2*s+1} OK')
print('ALL_TERMINAL_RANK_CERTIFICATES_OK')
