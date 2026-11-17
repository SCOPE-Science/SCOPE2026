#!/usr/bin/env python3
"""Exact finite checks for the three-cluster inball theorem.

Enumerates all candidate scalar potentials whose coordinates are drawn from
{0,t,1-t,1}, independently tests the metric constraints and connectedness
of the saturated constraint graph, and compares the resulting complete
vertex/contact list with the proposed formula. No floating-point arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from collections import defaultdict
from sympy import Matrix

def prediction(m, t):
    alpha = F(3*m,2) - F(m,1)/t
    scores = {r:F(m) + r*t*t - (m+r*t)**2/F(3*m) for r in range(m+1)}
    best=max(scores.values())
    R=sorted(r for r,s in scores.items() if s==best)
    return best,R,6*sum(comb(2*m,r) for r in R),(0 if any(r>0 for r in R) else 3*m-3)

def candidates(m,t):
    vals=tuple(sorted(set((F(0), t, 1-t, F(1)))))
    # independent state search; only the intra-cluster metric bound is used
    blocks=[v for v in product(vals, repeat=m)
            if max(v)-min(v)<=t]
    N=3*m
    seen=set()
    maxima=[]
    best=None
    for a,b,c in product(blocks,repeat=3):
        v=a+b+c
        if min(v)!=0 or max(v)!=1: continue
        # Only cross-cluster pairs have distance 1; every v_i lies in [0,1].
        # Determine tight graph connectedness via an independently built graph.
        parent=list(range(N))
        def find(i):
            while parent[i]!=i:
                parent[i]=parent[parent[i]];i=parent[i]
            return i
        def unite(i,j):
            x,y=find(i),find(j)
            if x!=y:parent[x]=y
        for i in range(N):
            for j in range(i+1,N):
                d=t if i//m==j//m else F(1)
                if abs(v[i]-v[j])==d: unite(i,j)
        if len({find(i) for i in range(N)})!=1:continue
        if v in seen:continue
        seen.add(v)
        S=sum(v); q=sum(z*z for z in v)-S*S/N
        if best is None or q>best:
            best=q;maxima=[v]
        elif q==best: maxima.append(v)
    # Compute rank of centered normal vectors from complete contact list
    if maxima:
        M=Matrix([[N*x-sum(v) for x in v[:-1]] for v in maxima])
        rank=M.rank()
    else:rank=-1
    return best,len(maxima),N-1-rank,len(seen)

def main():
    cases={
        2: [F(1,3),F(4,5),F(9,10)],
        3: [F(1,4),F(1,2),F(3,4),F(4,5),F(9,10)],
        # m=4 checked by the independent integer-profile loop below;
    }
    tested=0;total=0
    for m,ts in cases.items():
        for t in ts:
            ans=prediction(m,t)
            out=candidates(m,t)
            assert (out[0],out[1],out[2])==(ans[0],ans[2],ans[3]),(m,t,ans,out)
            tested+=1;total+=out[3]
            print('PASS',m,t,'max',ans[0],'rset',ans[1], 'contacts',ans[2], 'center_dim',ans[3], 'all_vertices',out[3])
    # Independent profile optimization checks for larger sizes and all
    # three-cluster lower/upper choices, including lower and upper splitting.
    profiles=0
    for m in range(2,16):
        for numerator in (1,2,3,4,5,6,7,8,9,10,11,12,14,17,19,23):
            t=F(numerator,25)
            if not 0<t<1:continue
            predicted=prediction(m,t)[0]
            max_val=F(-1)
            for upper_blocks in (1,2):
                lower_blocks=3-upper_blocks
                P=upper_blocks*m
                for low_t in range(lower_blocks*(m-1)+1):
                    for upper_inner in range(upper_blocks*(m-1)+1):
                        S=P+t*(low_t-upper_inner)
                        Q=P+t*t*low_t+(t*t-2*t)*upper_inner-S*S/F(3*m)
                        if Q>max_val:max_val=Q
            assert predicted==max_val,(m,t,predicted,max_val)
            profiles+=1
    print('EXACT_COMPLETE_TIGHT_GRAPH_CHECK_PASS cases=',tested,'vertices=',total)
    print('INDEPENDENT_TWO_SIDED_INTEGER_PROFILE_CHECK_PASS cases=',profiles)
    print('THREE_CLUSTER_INBALL_AND_CENTER_COLLAPSE_ALL_CHECKS_PASS')
if __name__=='__main__':main()
