#!/usr/bin/env python3
"""Exact rational checks for complete multipartite metric-graph H1 evaluations.
Only standard-library fractions; no external data or symbolic packages required.
"""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement


def inverse(mat):
    n=len(mat)
    a=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(mat)]
    for i in range(n):
        k=next(k for k in range(i,n) if a[k][i])
        a[i],a[k]=a[k],a[i]
        scale=a[i][i];a[i]=[v/scale for v in a[i]]
        for j in range(n):
            if j!=i and a[j][i]:
                c=a[j][i];a[j]=[u-c*v for u,v in zip(a[j],a[i])]
    return [row[n:] for row in a]


def graph(sizes):
    part=[i for i,sz in enumerate(sizes) for _ in range(sz)]
    edges=[(a,b,Q(1)) for a,b in combinations(range(len(part)),2) if part[a]!=part[b]]
    return part,edges


def resistance(edges,n):
    lap=[[Q(0)]*n for _ in range(n)]
    for u,v,l in edges:
        g=1/l
        lap[u][u]+=g;lap[v][v]+=g;lap[u][v]-=g;lap[v][u]-=g
    h=inverse([row[:n-1] for row in lap[:n-1]])
    def r(a,b):
        if a==b: return Q(0)
        def g(i,j): return Q(0) if i==n-1 or j==n-1 else h[i][j]
        return g(a,a)+g(b,b)-2*g(a,b)
    return r


def integrated_resistance(x,edges,r):
    return sum((l*(r(x,u)+r(x,v))/2+l*(l-r(u,v))/6 for u,v,l in edges),Q(0))


def formula(sizes):
    N=sum(sizes);m=(N*N-sum(s*s for s in sizes))//2
    B=[Q(N-3,2)+Q(s,N)+Q((N-1)*m,N*(N-s)) for s in sizes]
    base=Q(m-N+1,6)
    J=sum((s*(N-s)*B[i] for i,s in enumerate(sizes)),Q(0))/2+Q(m*(2*m-2*N+1),6)
    def edge(i,j,t):
        q=Q(N-1,N)*(Q(1,N-sizes[i])+Q(1,N-sizes[j]))
        alpha=m-1-m*q
        return (1-t)*B[i]+t*B[j]+alpha*t*(1-t), alpha
    return N,m,B,base,J,edge


def peak(sizes):
    N,m,B,base,J,edge=formula(sizes)
    best=None; maxima=[]
    for i,j in combinations(range(len(sizes)),2):
        alpha=edge(i,j,Q(0))[1]
        d=B[j]-B[i]
        if alpha>0:
            t=max(Q(0),min(Q(1),Q(1,2)+d/(2*alpha)))
        else:t=Q(1) if B[j]>B[i] else Q(0)
        v=edge(i,j,t)[0]
        if best is None or v>best:best=v; maxima=[(i,j,t)]
        elif best==v:maxima.append((i,j,t))
    return best,maxima


def self_checks():
    tests=0;max_tests=0; geometry_tests=0;double_integral_tests=0
    for p in range(2,6):
      for sizes in combinations_with_replacement(range(1,6),p):
        if sum(sizes)>9:continue
        part,edges=graph(sizes); N,m,B,base,J,fun=formula(sizes)
        assert m==len(edges)
        r=resistance(edges,N)
        for u in range(N):
            expected=B[part[u]]+base
            got=integrated_resistance(u,edges,r)
            assert got==expected,(sizes,u,got,expected)
            tests+=1
        for u,v,l in edges:
            q=(Q(N-1,N)*(Q(1,N-sizes[part[u]])+Q(1,N-sizes[part[v]])))
            assert r(u,v)==q,(sizes,u,v,r(u,v),q)
            tests+=1
        for u in range(N):
          for v in range(u+1,N):
            if part[u]==part[v]:assert r(u,v)==Q(2,N-sizes[part[u]])
            tests+=1
        # Exact global edge-orbit comparison, including degenerate cases.
        v, winners=peak(sizes)
        M=max(sizes);D=N-M
        if D>=3:
            assert all(0<t<1 for i,j,t in winners),(sizes,winners)
            assert all(sorted((sizes[i],sizes[j]))==sorted(sizes)[-2:] for i,j,t in winners),(sizes,winners)
        elif D==2 and sizes!= (1,1,1) and sizes!=(2,2):
            assert v==max(B),(sizes,v,B)
        elif D==1:
            assert v==max(B)
        max_tests+=1
        # Independently subdivide a physical unit edge and integrate resistance
        # over the resulting unequal-length physical network.
        if N<=7:
            u,v,_=edges[len(edges)//2]
            t=Q(2,5)
            split=[(a,b,l) for a,b,l in edges if (a,b)!=(u,v)]
            x=N
            split.extend([(u,x,t),(x,v,1-t)])
            rr=resistance(split,N+1)
            actual=integrated_resistance(x,split,rr)
            predicted=fun(part[u],part[v],t)[0]+base
            assert actual==predicted,(sizes,actual,predicted)
            geometry_tests+=1
        if N<=6:
            # Independent Simpson integration of F(x) over every original
            # unit edge. F is quadratic on each edge; all values below are
            # obtained by fresh grounded inverse matrices.
            total=Q(0)
            Fvert=[integrated_resistance(v,edges,r) for v in range(N)]
            for a,b,l in edges:
                x=N
                halves=[(u,v,w) for u,v,w in edges if (u,v)!=(a,b)]
                halves.extend([(a,x,Q(1,2)),(x,b,Q(1,2))])
                rr=resistance(halves,N+1)
                mid=integrated_resistance(x,halves,rr)
                total+=(Fvert[a]+4*mid+Fvert[b])/6
            assert total==J,(sizes,total,J)
            double_integral_tests+=1
    special={
        (1,1,1):Q(1,4),
        (2,2):Q(1,3),
        (2,3):Q(7,18),
        (1,1,3):Q(235,588),
        (1,2,3):Q(2443,7260),
        (2,3,4):Q(711683,2262234),
        (3,3):Q(37,108),
    }
    for sizes,val in special.items():
        N,m,B,base,J,_=formula(sizes)
        candidate=peak(sizes)[0]
        got=(candidate+base)/m-J/(2*m*m)
        assert got==val,(sizes,got,val)
    print('EXACT_VERTEX_RESISTANCE_AND_ORBIT_CHECKS_PASSED',tests)
    print('ALL_PARTITION_LOCALIZATION_TESTS_PASSED',max_tests)
    print('INDEPENDENT_SUBDIVIDED_EDGE_INTEGRALS_PASSED',geometry_tests)
    print('INDEPENDENT_DOUBLE_RESISTANCE_INTEGRALS_PASSED',double_integral_tests)
    print('SEVEN_EXACT_SHARP_CONSTANTS_PASSED')
    print('ALL_MULTIPARTITE_H1_CHECKS_PASSED')

if __name__=='__main__':self_checks()
