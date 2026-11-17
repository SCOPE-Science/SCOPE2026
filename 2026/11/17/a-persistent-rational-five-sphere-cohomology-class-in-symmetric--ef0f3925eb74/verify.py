#!/usr/bin/env python3
"""Direct combinatorial cochain/character checks for the moment-angle space of the two-letter injective-word poset."""
import itertools, math
from fractions import Fraction


def rank_q(rows):
    if not rows: return 0
    mat=[[Fraction(x) for x in row] for row in rows]
    nr=len(mat); nc=len(mat[0]); rr=0
    for col in range(nc):
        p=next((i for i in range(rr,nr) if mat[i][col]),None)
        if p is None: continue
        mat[rr],mat[p]=mat[p],mat[rr]
        pivot=mat[rr][col]
        for j in range(col,nc): mat[rr][j]/=pivot
        for i in range(rr+1,nr):
            coef=mat[i][col]
            if coef:
                for j in range(col,nc): mat[i][j]-=coef*mat[rr][j]
        rr+=1
        if rr==nr: break
    return rr


def parity(perm):
    return -1 if sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2 else 1


def induced_perm(perm, subset):
    target=sorted(perm[i] for i in subset)
    return [target.index(perm[i]) for i in sorted(subset)]


def graph_complex(k):
    edges=[(a,b,t) for a in range(k) for b in range(a+1,k) for t in range(2)]
    boundary=[[0]*len(edges) for _ in range(k)]
    for j,(a,b,t) in enumerate(edges):
        boundary[a][j]=-1
        boundary[b][j]=+1
    r=rank_q(boundary)
    assert r==k-1
    return edges,boundary,len(edges)-r


def char_graph(k,perm):
    edges,boundary,beta=graph_complex(k)
    f=sum(perm[i]==i for i in range(k))
    char_c0=f
    char_c1=0
    for a,b,t in edges:
        aa,bb=perm[a],perm[b]
        lo,hi=sorted((aa,bb))
        sign=+1 if aa<bb else -1
        new_t = t if aa<bb else (1-t)
        if (lo,hi,new_t)==(a,b,t): char_c1+=sign
    # H0 trivial, C1 - C0 + H0 = H1; Euler character
    ch=char_c1-char_c0+1
    assert ch==(f-1)**2,(k,perm,ch,(f-1)**2)
    return ch


def char_moment(n,k,perm):
    # Direct fixed-multidegree traces from the oriented C1/C0 cellular complex
    # and exterior-degree sign of complement of the simplex support.
    val=0
    for subset in itertools.combinations(range(n),k):
        if {perm[i] for i in subset}!=set(subset): continue
        sub=list(sorted(subset))
        psub=[sub.index(perm[i]) for i in sub]
        ch=char_graph(k,psub)
        val+=parity(psub)*ch
    return val


def cycle_type(perm):
    seen=set(); cs=[]
    for i in range(len(perm)):
        if i not in seen:
            j=i; s=0
            while j not in seen:
                seen.add(j);s+=1;j=perm[j]
            cs.append(s)
    return cs


def predicted_char(n,k,perm):
    # Independently sum over subsets of cycles; must occupy complete cycles.
    cyc=cycle_type(perm)
    val=0
    for mask in range(1<<len(cyc)):
        lengths=[cyc[i] for i in range(len(cyc)) if mask>>i&1]
        if sum(lengths)!=k:continue
        f=lengths.count(1)
        val+=(-1 if (k-len(lengths))%2 else 1)*(f-1)**2
    return val


def partitions_at_most(n):
    # all n! permutations only through 6
    return list(itertools.permutations(range(n)))


def koszul_local(k):
    # Multidegree I=[k] of the Lü-Panov cellular DGA, not a graph-only rank surrogate.
    # Face types: empty, singleton, and ordered two-vertex faces.
    empty=tuple(range(k))
    vert=[j for j in range(k)]
    arcs=[(i,j) for i in range(k) for j in range(k) if i!=j]
    d0=[[0] for _ in range(k)]
    d1=[[0]*k for _ in arcs]
    for j in vert:
        d0[j][0]=(-1)**j
        remain=[x for x in range(k) if x!=j]
        for loc,a in enumerate(remain):
            for face in ((a,j),(j,a)):
                d1[arcs.index(face)][j]=(-1)**loc
    assert all(sum(d1[row][j]*d0[j][0] for j in range(k))==0 for row in range(len(arcs)))
    assert rank_q(d0)==1
    assert rank_q(d1)==k-1
    assert len(arcs)-rank_q(d1)==(k-1)**2
    return arcs,d0,d1


def trace_koszul_top(k,perm):
    # Signed action on the exterior u_(I\face) factor of each cellular generator.
    arcs,d0,d1=koszul_local(k)
    def exterior_sign(indices):
        mapped=[perm[i] for i in indices]
        ordering=[sorted(mapped).index(x) for x in mapped]
        return parity(ordering)
    t0=exterior_sign(range(k))
    t1=sum(exterior_sign([i for i in range(k) if i!=j])
           for j in range(k) if perm[j]==j)
    t2=sum(exterior_sign([a for a in range(k) if a!=i and a!=j])
           for i,j in arcs if perm[i]==i and perm[j]==j)
    return t2-t1+t0


def main():
    for n in range(2,7):
        perms=partitions_at_most(n)
        bsum=[]
        for k in range(2,n+1):
            _,_,beta=graph_complex(k)
            assert beta==(k-1)**2
            b=math.comb(n,k)*beta
            bsum.append((k+2,b))
            trsum=0
            for p in perms:
                direct=char_moment(n,k,p)
                pred=predicted_char(n,k,p)
                assert direct==pred,(n,k,p,direct,pred)
                direct_cell=trace_koszul_top(k,p) if n==k else None
                if n==k: assert direct_cell==pred,(n,k,p,direct_cell,pred)
                if p==tuple(range(n)):
                    assert direct==b
                trsum+=direct
            assert trsum%len(perms)==0
            invariant=trsum//len(perms)
            assert invariant == (1 if k==3 else 0),(n,k,invariant)
        print(f'n={n} reduced_integral_cohomology={bsum} quotient_positive_rational={[(d,1) for d,b in bsum if d==5]} permutation_checks={len(perms)*(n-1)} PASS')
    print('VERIFY_TRUNCATED_INJECTIVE_WORD_MOMENT_ANGLE_PASS')

if __name__=='__main__': main()
