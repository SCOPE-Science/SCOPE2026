from collections import defaultdict
from math import comb, sqrt

def commute_direct(a,b,N):
    A={i+2 for i in range(N) if a>>i&1}; B={i+2 for i in range(N) if b>>i&1}
    ab={x for x in range(3,N+2) if x in A and x-1 in B}
    ba={x for x in range(3,N+2) if x in B and x-1 in A}
    return ab==ba

def degree_polynomial(a,N):
    seen=0; lens=[]; h=0
    while seen<N:
        if a>>seen&1:
            end=seen
            while end<N and a>>end&1: end+=1
            lens.append(end-seen); seen=end
        else:
            left=seen>0 and ((a>>(seen-1))&1)
            right=seen+1<N and ((a>>(seen+1))&1)
            if not left and not right: h+=1
            seen+=1
    p=[1]
    for l in lens:
        q=p+[0]*l
        for i,c in enumerate(p):q[i+l]+=c
        p=q
    for _ in range(h):
        q=p+[0]
        for i,c in enumerate(p):q[i+1]+=c
        p=q
    return p+[0]*(N+1-len(p))

def dp_poly(N):
    # words of states 00,10,01,11; counts indexed by (rankA,rankB)
    v={(0,0,0):1}
    weights=[(0,0),(1,0),(0,1),(1,1)]
    for k in range(N):
        out=defaultdict(int)
        for (prev,ra,rb),c in v.items():
            for state,(da,db) in enumerate(weights):
                if k==0 or prev==0 or state==0 or prev==state:
                    out[(state,ra+da,rb+db)]+=c
        v=out
    sums=defaultdict(int)
    for (state,ra,rb),c in v.items():sums[(ra,rb)]+=c
    return dict(sums)

def brute(N):
    counts=defaultdict(int)
    for a in range(1<<N):
        runp=degree_polynomial(a,N)
        got=[0]*(N+1)
        for b in range(1<<N):
            if commute_direct(a,b,N):
                got[b.bit_count()]+=1
                counts[(a.bit_count(),b.bit_count())]+=1
        assert got==runp,(N,a,got,runp)
    return dict(counts)

if __name__=='__main__':
    for N in range(1,9):
        a=brute(N)
        b=dp_poly(N)
        assert a==b,(N,a,b)
        total=sum(a.values())
        recurrence=(1 if N==0 else 4 if N==1 else None)
        print('N',N,'pairs',total,'rank_diagonal',[(r,a.get((r,r),0)) for r in range(N+1)])
    for N in range(1,11):
        for r in range(1,N+1):
            z=N-r
            values=[sum(degree_polynomial(a,N)) for a in range(1<<N) if a.bit_count()==r]
            observed=max(values)
            expected=(1<<(z+1)) if z<r else (1<<z)
            assert observed==expected,(N,r,observed,expected)
            if z<r:
                assert values.count(observed)==comb(r-1,z),(N,r,values.count(observed))
    print('VERIFY_OK')
