#!/usr/bin/env python3
"""Independent finite checks of the stated Rule-154 spectral-rank identities."""
from collections import deque, defaultdict

def step(x,n):
    y=0
    for i in range(n):
        a=(x>>((i-1)%n))&1; b=(x>>i)&1; c=(x>>((i+1)%n))&1
        y|=(a^c^(a&b))<<i
    return y

def predicted_rank(n,t):
    m=n//2; h=m&(-m)
    return (1<<n)-(1<<(m+1))+(1<<(m-min(t,h)+1))

def parity_sparse(x,n):
    return not(any((x>>i)&1 for i in range(0,n,2)) and
               any((x>>i)&1 for i in range(1,n,2)))

def rank_binary(columns):
    basis={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in basis:v^=basis[p]
            else:basis[p]=v;break
    return len(basis)

def shift_plus(x,m):
    return x^(((x<<1)|(x>>(m-1)))&((1<<m)-1))

def run():
    tested=0
    for n in range(2,17,2):
        N=1<<n; nxt=[step(x,n) for x in range(N)]
        indeg=[0]*N
        for y in nxt:indeg[y]+=1
        todo=deque(x for x in range(N) if indeg[x]==0)
        transient=bytearray(N)
        while todo:
            x=todo.popleft();transient[x]=1
            y=nxt[x];indeg[y]-=1
            if indeg[y]==0:todo.append(y)
        m=n//2; h=m&-m
        # Independent graph peeling and explicit half-ring linear prediction.
        for x in range(N):
            even=sum(((x>>(2*j))&1)<<j for j in range(m))
            odd=sum(((x>>(2*j+1))&1)<<j for j in range(m))
            if even and odd:
                expected=False
            else:
                a=even or odd
                expected=any(sum((a>>(r+h*j))&1 for j in range(m//h))%2
                             for r in range(h))
            assert bool(transient[x])==bool(expected),('nonperiodic',n,x)
        seen=list(range(N))
        for t in range(h+2):
            assert len(set(seen))==predicted_rank(n,t),('rank',n,t)
            tested+=1
            seen=[nxt[x] for x in seen]
        assert sum(transient)==N-predicted_rank(n,h)
    # Orthogonal binary-matrix rank calculation for the half-ring difference.
    matrix_cases=0
    for m in range(1,33):
        h=m&-m
        for t in range(h+2):
            cols=[]
            for j in range(m):
                z=1<<j
                for _ in range(t):z=shift_plus(z,m)
                cols.append(z)
            assert rank_binary(cols)==m-min(t,h),(m,t)
            matrix_cases+=1
    # Graph of possible unequal preimages; enumerate local transitions directly.
    states={'A':(0,0),'B':(0,1),'C':(1,0)}
    edges=defaultdict(set)
    for a,(u,U) in states.items():
        for b,(v,V) in states.items():
            for c,(w,W) in states.items():
                if (w^u^(u&v))==(W^U^(U&V)):
                    edges[a+b].add(b+c)
    expect={
      'AA':{'AA'}, 'AB':{'BA'}, 'BA':{'AB','AC'},
      'AC':{'CA'}, 'CA':{'AB','AC'}, 'BB':{'BA'},
      'BC':{'CB','CC'}, 'CB':{'BB','BC'}, 'CC':{'CA'}}
    assert dict(edges)==expect,(dict(edges),expect)
    print(f'VERIFY_OK ring_sizes=8 state_cases={sum(1<<n for n in range(2,17,2))} '
          f'power_ranks={tested} binary_matrix_cases={matrix_cases} pair_graph_edges={sum(map(len,edges.values()))}')
if __name__=='__main__':run()
