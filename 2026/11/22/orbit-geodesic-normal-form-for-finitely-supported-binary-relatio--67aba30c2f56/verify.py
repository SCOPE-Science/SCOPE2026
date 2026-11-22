"""Independent exhaustive finite instances of orbit-geodesic formulas.
Only equality-atom relation orbit bits are enumerated; no result is
asserted for infinitely many atoms solely from testing.
Usage: python verify.py
"""
from itertools import product
from random import Random
INF=10**8

def shortest(n,edge):
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for i,j in edge:d[i][j]=min(d[i][j],1)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j]>d[i][k]+d[k][j]: d[i][j]=d[i][k]+d[k][j]
    return d

def check(m,bits,N=3):
    # bit order: m*m parameter arcs, m generic->parameter,
    # m parameter->generic, diagonal generic, offdiagonal generic.
    b=[(bits>>i)&1 for i in range(m*m+2*m+2)]
    E={(i,j) for i in range(m) for j in range(m) if b[m*i+j]}
    L={i for i in range(m) if b[m*m+i]}
    R={i for i in range(m) if b[m*m+m+i]}
    diagonal=b[m*m+2*m]; offdiagonal=b[m*m+2*m+1]
    edges=set(E)
    for x in range(m,m+N):
        edges.update((x,i) for i in L)
        edges.update((i,x) for i in R)
        if diagonal:edges.add((x,x))
        if offdiagonal:edges.update((x,y) for y in range(m,m+N) if x!=y)
    d=shortest(m+N,edges)
    dc=shortest(m,E)
    for i in range(m+N):
        for j in range(m+N):
            if i<m and j<m:
                z=dc[i][j]
                for q in R:
                    for p in L:
                        z=min(z, dc[i][q]+2+dc[p][j])
            elif i>=m and j<m:
                z=min((1+dc[p][j] for p in L),default=INF)
            elif i<m and j>=m:
                z=min((1+dc[i][q] for q in R),default=INF)
            elif i==j:
                z=0
            else:
                z=1 if offdiagonal else min((2+dc[p][q] for p in L for q in R),default=INF)
            z=min(z,INF)
            assert z==d[i][j], (m,bits,i,j,z,d[i][j],L,R,E)
    assert all(v==INF or v<=m+1 for row in d for v in row)


def run():
    count=0
    for m in range(4):
        for bits in range(1<<(m*m+2*m+2)):
            check(m,bits)
            count+=1
    rng=Random(930219)
    for _ in range(3000):
        m=4
        bits=rng.getrandbits(m*m+2*m+2)
        check(m,bits)
        count+=1
    # exact sharp witnesses of maximum finite distance m+1
    for m in range(8):
        if m==0:
            check(0,1<<(0*0+0+1))
        else:
            E={(i,i+1) for i in range(m-1)}
            bits=sum(1<<(m*i+j) for i,j in E)
            bits|=1<<(m*m+0)      # generic to first parameter
            bits|=1<<(m*m+m+(m-1))  # last parameter to generic
            check(m,bits)
            L={0};R={m-1}
            edges=set(E)|{(m,0),(m+1,0),(m-1,m),(m-1,m+1)}
            d=shortest(m+2,edges)
            assert d[m][m+1]==m+1
    print('VERIFY_OK',count,'exhaustive m<=3, sampled m=4; sharp examples m=0..7')
if __name__=='__main__':run()
