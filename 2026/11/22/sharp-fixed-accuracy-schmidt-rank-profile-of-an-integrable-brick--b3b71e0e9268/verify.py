"""Exact finite folded-gate checks for the Yang--Baxter brickwork Schmidt sectors.
Source mathematical model: arXiv:2609.39401, Eq. (4), (19)--(23), (S22).
No external dependencies; uses integer arithmetic throughout.
"""
from collections import defaultdict
from itertools import product
from math import comb


def local_r(u,v):
    s,a=divmod(u,2)
    z,b=divmod(v,2)
    return 2*z+(a^((s^z)&b)), 2*s+b


def word_blockswap(t):
    target=list(range(t,2*t))+list(range(t))
    arr=list(range(2*t))
    moves=[]
    for i,x in enumerate(target):
        p=arr.index(x)
        while p>i:
            arr[p-1],arr[p]=arr[p],arr[p-1]
            moves.append(p-1)
            p-=1
    assert arr==target
    return moves


def folded_step(z,j):
    z=list(z)
    lk,lb=divmod(z[j],4)
    rk,rb=divmod(z[j+1],4)
    yk,zk=local_r(lk,rk)
    yb,zb=local_r(lb,rb)
    z[j]=4*yk+yb
    z[j+1]=4*zk+zb
    return tuple(z)


def sector_blocks(t):
    moves=word_blockswap(t)
    blocks=defaultdict(dict)
    # Identity vectorization has coefficient 1/2 for each four local states;
    # source O_x = |B,0><A,0| with local ket=2, bra=0.
    for data in product(range(4),repeat=2*t-1):
        z=tuple(5*u for u in data[:t])+(4*2+0,)+tuple(5*u for u in data[t:])
        for j in moves:z=folded_step(z,j)
        row=z[:t];col=z[t:]
        # k = the number of output-left identity sectors A; source has B in ket,
        # l = the number of output-right identity sectors A.
        k=sum((w//4)//2==0 for w in row)  # source has B, so contributes zero
        l=sum((w//4)//2==0 for w in col)
        assert 0<=k<t and 0<=l<=t
        key=(k,l)
        assert (row,col) not in blocks[key]
        blocks[key][(row,col)]=1
    return blocks


def exact_flat_check(t):
    blocks=sector_blocks(t)
    assert len(blocks)==t*(t+1)
    assertions=0
    for (k,l),entries in blocks.items():
        d=l-k
        g=abs(d)-int(d>0)
        m=1<<g
        count=len(entries)
        expected=comb(t-1,k)*comb(t,l)*(1<<(2*t-1))
        assert count==expected
        assert count%m==0
        lam=count//m
        # Nonzero eigenvalues of B B* all equal to lambda iff
        # (B B*)^2=lambda(B B*) and tr(B B*)=lambda*m.
        row_cols=defaultdict(set)
        for row,col in entries:row_cols[row].add(col)
        rows=list(row_cols)
        G={(i,j):len(row_cols[u]&row_cols[v]) for i,u in enumerate(rows)
           for j,v in enumerate(rows) if row_cols[u]&row_cols[v]}
        # sparse multiplication check
        nbr=defaultdict(list)
        for (i,j),v in G.items():nbr[i].append((j,v))
        for i in range(len(rows)):
            g2=defaultdict(int)
            for j,x in nbr[i]:
                for k2,y in nbr[j]:g2[k2]+=x*y
            for k2 in set(g2)|{k2 for (i2,k2) in G if i2==i}:
                assert g2[k2]==lam*G.get((i,k2),0),(t,k,l,i,k2,g2[k2],lam*G.get((i,k2),0))
                assertions+=1
        assert sum(G.get((i,i),0) for i in range(len(rows)))==m*lam
        assertions+=2
    return assertions

if __name__=='__main__':
    count=0
    for t in range(1,4):
        v=exact_flat_check(t);count+=v
        print(f't={t} exact folded count-block checks passed: {v}')
    print('PASS',count)
