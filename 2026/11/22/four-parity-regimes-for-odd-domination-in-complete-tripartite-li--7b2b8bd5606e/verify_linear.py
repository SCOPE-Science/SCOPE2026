"""Independent binary Gaussian solver for odd dominating sets of tripartite line graphs.
Uses closed neighborhoods directly, not the theoretical parity-vertex classification.
"""
from collections import Counter
from itertools import product
from math import comb


def graph(a,b,c):
    parts=[0]*a+[1]*b+[2]*c
    E=[(u,v) for u in range(len(parts)) for v in range(u+1,len(parts)) if parts[u]!=parts[v]]
    rows=[]
    for x,(u,v) in enumerate(E):
        row=0
        for y,(s,t) in enumerate(E):
            if x==y or len({u,v,s,t})<4:row|=1<<y
        rows.append(row)
    return E,rows


def solve(E, rows):
    m=len(E)
    aug=[r|(1<<m) for r in rows]
    piv=[];pr=0
    for bit in range(m):
        r=next((z for z in range(pr,m) if (aug[z]>>bit)&1),None)
        if r is None:continue
        aug[pr],aug[r]=aug[r],aug[pr]
        for z in range(m):
            if z!=pr and (aug[z]>>bit)&1:aug[z]^=aug[pr]
        piv.append(bit);pr+=1
    assert all(not((r&((1<<m)-1))==0 and ((r>>m)&1)) for r in aug)
    free=[bit for bit in range(m) if bit not in piv]
    assert len(free)<=13,(m,len(free))
    for choice in product(range(2),repeat=len(free)):
        sol=sum(v<<bit for v,bit in zip(choice,free))
        for p,bit in reversed(list(enumerate(piv))):
            row=aug[p];prior=(row&sol).bit_count()&1;value=((row>>m)&1)^prior
            sol|=value<<bit
        assert all((r&sol).bit_count()%2==1 for r in rows)
        yield sol


def predicted(a,b,c):
    N=a*b+a*c+b*c
    parity=(a&1,b&1,c&1)
    result=Counter()
    if sum(parity)==0:result[N]=1
    elif sum(parity)==3:
        result.update([N,a*b,a*c,b*c])
    elif sum(parity)==2:
        v=[k for k in (a,b,c) if k&1];h=next(k for k in (a,b,c) if not k&1)
        x,y=v
        for i in range(1,x+1,2):
            for j in range(1,y+1,2):
                w=i*j+(x-i)*(y-j)+h*(x+y-i-j)
                result[w]+=comb(x,i)*comb(y,j)
    else:
        x=next(k for k in (a,b,c) if k&1);y,z=[k for k in (a,b,c) if not k&1]
        for i in range(1,y+1,2):
            for j in range(1,z+1,2):
                w=x*(y+z-i-j)+i*j+(y-i)*(z-j)
                result[w]+=comb(y,i)*comb(z,j)
    return result


def connected(mask,E):
    selected=[i for i in range(len(E)) if (mask>>i)&1]
    if not selected:return False
    visited={selected[0]}
    while True:
        new={j for j in selected if any(set(E[j])&set(E[i]) for i in visited)}
        if new<=visited:break
        visited|=new
    return len(visited)==len(selected)

cases=[(1,1,1),(2,2,2),(1,1,2),(1,2,2),(3,2,2),(3,3,2),(1,3,3),(1,2,4),(2,2,3),(3,1,4),(1,1,4),(3,3,4),(1,4,4),(3,4,4)]
for shape in cases:
    E,rows=graph(*shape)
    solutions=list(solve(E,rows))
    got=Counter(x.bit_count() for x in solutions)
    assert got==predicted(*shape),(shape,got,predicted(*shape))
    count_connected=sum(connected(x,E) for x in solutions)
    parities=sum(s&1 for s in shape)
    assert count_connected==({0:1,1:0,2:1,3:4}[parities])
    print(f'K_{shape} m={len(E)} odd={len(solutions)} connected={count_connected} profile={sorted(got.items())}')
print('ALL_GAUSSIAN_CASES_PASS')
