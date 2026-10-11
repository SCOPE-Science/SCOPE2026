#!/usr/bin/env python3
from itertools import product

def comp_map(q):
    assert q % 2 == 0 and q >= 2
    c = {}
    for a in range(0,q,2):
        c[a]=a+1; c[a+1]=a
    return c

def dup2_rc(x,i,c):
    u=x[i:i+2]
    ins=(c[u[1]],c[u[0]])
    return x[:i+2]+ins+x[i+2:]

def forward_parents(q,n):
    c=comp_map(q)
    out={}
    for x in product(range(q), repeat=n):
        for i in range(n-1):
            y=dup2_rc(x,i,c)
            out.setdefault(y,set()).add(x)
    return out

def inverse_parents(y,q):
    c=comp_map(q)
    n=len(y)-2
    ps=set()
    starts=[]
    for i in range(n-1):
        if y[i+2]==c[y[i+1]] and y[i+3]==c[y[i]]:
            starts.append(i)
            ps.add(y[:i+2]+y[i+4:])
    return ps,starts

def construction(q,n):
    c=comp_map(q)
    a=0; b=c[a]
    base=(a,a,b,b)
    N=n+2
    y=tuple(base[i%4] for i in range(N))
    return y

def check_case(q,n):
    fwd=forward_parents(q,n)
    max_sz=0; max_y=None
    for y in product(range(q), repeat=n+2):
        inv,starts=inverse_parents(y,q)
        direct=fwd.get(y,set())
        assert inv==direct, (q,n,y,inv,direct)
        # Adjacent valid starts must yield the same parent.
        for i in range(len(starts)-1):
            if starts[i+1]==starts[i]+1:
                p1=y[:starts[i]+2]+y[starts[i]+4:]
                p2=y[:starts[i+1]+2]+y[starts[i+1]+4:]
                assert p1==p2
        if len(inv)>max_sz:
            max_sz=len(inv); max_y=y
    target=n//2
    assert max_sz==target, (q,n,max_sz,target,max_y)
    y=construction(q,n)
    inv,starts=inverse_parents(y,q)
    assert len(inv)==target, (q,n,y,len(inv),target,starts)
    # Construction has valid starts exactly at even positions.
    assert starts==list(range(0,n-1,2)), (q,n,starts)


def main():
    cases=[]
    for n in range(2,9):
        check_case(2,n); cases.append((2,n))
    for n in range(2,5):
        check_case(4,n); cases.append((4,n))
    for n in range(2,4):
        check_case(6,n); cases.append((6,n))
    for q in (2,4,6,8,10):
        for n in range(2,101):
            y=construction(q,n)
            inv,starts=inverse_parents(y,q)
            assert len(inv)==n//2
            assert starts==list(range(0,n-1,2))
    print(f"VERIFY_OK exhaustive_cases={len(cases)} construction_q<=10_n<=100")

if __name__=='__main__':
    main()
