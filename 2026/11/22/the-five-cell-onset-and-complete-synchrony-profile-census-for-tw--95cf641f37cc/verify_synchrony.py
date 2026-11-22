"""Exact five-cell zero-Hopf synchrony census.
Run: python3 verify_synchrony.py
Place five_cell_representatives.json in the same directory.
Uses only the Python standard library. No numerical eigenvalue tolerances.
"""
from itertools import combinations_with_replacement, permutations, product
from collections import Counter
from pathlib import Path
import json


def determinant(M):
    """Fraction-free integer Bareiss elimination, valid for all integer matrices."""
    A=[list(row) for row in M]; n=len(A); sign=1; denom=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((i for i in range(k+1,n) if A[i][k]),None)
            if r is None:return 0
            A[k],A[r]=A[r],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num % denom==0
                A[i][j]=num//denom
            A[i][k]=0
        denom=pivot
    return sign*A[-1][-1]


def trace_power(A,power):
    n=len(A)
    if power==1:return sum(A[i][i] for i in range(n))
    if power==2:return sum(A[i][j]*A[j][i] for i in range(n) for j in range(n))
    if power==3:return sum(A[i][j]*A[j][k]*A[k][i]
                            for i in range(n) for j in range(n) if A[i][j]
                            for k in range(n) if A[j][k])
    if power==4:return sum(A[i][j]*A[j][k]*A[k][ell]*A[ell][i]
                            for i in range(n) for j in range(n) if A[i][j]
                            for k in range(n) if A[j][k]
                            for ell in range(n) if A[k][ell])
    raise ValueError(power)


def connectivity(A,strong=False):
    n=len(A)
    def reach(transpose,weak):
        seen={0};stack=[0]
        while stack:
            i=stack.pop()
            for j in range(n):
                edge=(A[j][i]>0 if transpose else A[i][j]>0)
                if weak:edge=(A[j][i]>0 or A[i][j]>0)
                if edge and j not in seen:
                    seen.add(j);stack.append(j)
        return len(seen)==n
    return reach(False,not strong) and (not strong or reach(True,False))


def spectral_parameters(A):
    """An if-and-only-if exact spectral test for the five-cell case.
    Characteristic polynomial must be t(t-2)(t-r)(t*t+c), c>0,
    r nonzero and != 2, with the same charpoly checked by Newton sums.
    """
    n=len(A)
    r=trace_power(A,1)-2
    if n==5 and r in (0,2):return None
    t=4+r*r-trace_power(A,2)
    if t<=0 or t%2:return None
    c=t//2
    if trace_power(A,3)!=8+r**3:return None
    if n==5 and trace_power(A,4)!=16+r**4+2*c*c:return None
    if determinant(A)!=0:return None
    return (r,c)


def all_matrices(n):
    choices=list(combinations_with_replacement(range(n),2))
    row_options=[]
    for a,b in choices:
        row=[0]*n; row[a]+=1;row[b]+=1
        row_options.append(tuple(row))
    for rows in product(row_options,repeat=n):
        yield rows


def canonical(A,perms):
    n=len(A)
    return min(tuple(A[p[i]][p[j]] for i in range(n) for j in range(n)) for p in perms)


def aut_count(A,perms):
    n=len(A)
    return sum(all(A[i][j]==A[p[i]][p[j]] for i in range(n) for j in range(n)) for p in perms)


def count(n):
    cnt=Counter();strong=Counter();total=0;strong_total=0
    for A in all_matrices(n):
        par=spectral_parameters(A)
        if par is not None and connectivity(A):
            cnt[par]+=1;total+=1
            if connectivity(A,True):strong[par]+=1;strong_total+=1
    return total,cnt,strong_total,strong


def check_representatives():
    reps=json.loads((Path(__file__).parent/'five_cell_representatives.json').read_text(encoding='utf-8'))
    assert len(reps)==191
    perms=list(permutations(range(5)))
    canons=set(); sums=Counter(); strong_sums=Counter(); orbit_sizes=Counter(); types=Counter()
    for index,entry in enumerate(reps,1):
        A=entry['matrix'];par=(entry['r'],entry['omega_squared'])
        assert len(A)==5 and all(len(row)==5 and sum(row)==2 and all(x in (0,1,2) for x in row) for row in A)
        assert spectral_parameters(A)==par and connectivity(A)
        can=canonical(A,perms)
        assert can==tuple(v for row in A for v in row) and can not in canons
        canons.add(can)
        aut=aut_count(A,perms)
        assert 120%aut==0 and 120//aut==entry['labelled']
        orbit_sizes[entry['labelled']]+=1
        types[par]+=1
        sums[par]+=entry['labelled']
        if connectivity(A,True):strong_sums[par]+=entry['labelled']
    assert len(canons)==191
    assert sum(sums.values())==21960 and sum(strong_sums.values())==6300
    assert orbit_sizes==Counter({120:175,60:16})
    return types,sums,strong_sums,orbit_sizes


def partitions(n):
    # All partitions via restricted-growth strings, one representative each.
    def grow(seq):
        if len(seq)==n:
            yield seq
        else:
            for nxt in range(max(seq)+2):
                yield from grow(seq+(nxt,))
    return list(grow((0,)))


def balanced(A, pi):
    # Equivalence classes define flow-invariant polydiagonals iff each pair
    # of cells in one class receives the same total input from each class.
    blocks=[[j for j in range(len(A)) if pi[j]==b]
            for b in range(max(pi)+1)]
    return all(sum(A[i][k] for k in C)==sum(A[j][k] for k in C)
               for B in blocks for i in B for j in B for C in blocks)


def synchrony_profile():
    reps=json.loads((Path(__file__).parent/'five_cell_representatives.json').read_text(encoding='utf-8'))
    p5=partitions(5)
    assert len(p5)==52
    hist=Counter();hist_strong=Counter();primitive=[];by_spectrum=Counter()
    for entry in reps:
        A=entry['matrix']
        nontrivial=sum(balanced(A,p) for p in p5)-2
        assert 0<=nontrivial<=50
        hist[nontrivial]+=1
        by_spectrum[(entry['r'],entry['omega_squared'],nontrivial)]+=1
        if connectivity(A,True):hist_strong[nontrivial]+=1
        if nontrivial==0:primitive.append(entry)
    assert hist==Counter({0:2,1:12,2:59,3:40,4:59,5:4,6:15})
    assert hist_strong==Counter({0:2,1:6,2:22,3:16,4:8,5:1,6:1})
    assert len(primitive)==2
    assert all(connectivity(z['matrix'],True) and
               (z['r'],z['omega_squared'])==(-1,1) and z['labelled']==120
               for z in primitive)
    expected=[
       [[0,0,0,0,2],[0,0,0,1,1],[1,0,1,0,0],[0,1,1,0,0],[0,0,0,2,0]],
       [[0,0,0,0,2],[0,0,1,1,0],[1,0,1,0,0],[1,1,0,0,0],[0,1,0,1,0]],
    ]
    assert [x['matrix'] for x in primitive]==expected
    reps4=json.loads((Path(__file__).parent/'four_cell_representatives.json').read_text(encoding='utf-8'))
    p4=partitions(4)
    assert len(p4)==15 and len(reps4)==9
    assert all(sum(balanced(A['matrix'],p) for p in p4)>=3 for A in reps4)
    return hist,hist_strong,by_spectrum


def main():
    assert determinant(((1,2),(3,4)))==-2
    assert determinant(((0,2),(3,4)))==-6
    assert determinant(((1,2),(2,4)))==0
    t4,s4,u4,v4=count(4)
    assert (t4,s4,u4,v4)==(216,Counter({(0,1):216}),72,Counter({(0,1):72}))
    t5,s5,u5,v5=count(5)
    assert t5==21960 and u5==6300
    assert s5==Counter({(-1,1):7620,(1,1):6900,(-1,2):3540,(-2,1):1800,(-2,2):1620,(-2,4):360,(-2,3):120})
    types,rep_labelled,rep_strong,orbit_sizes=check_representatives()
    assert s5==rep_labelled and v5==rep_strong
    assert types==Counter({(-1,1):66,(1,1):60,(-1,2):30,(-2,1):15,(-2,2):15,(-2,4):4,(-2,3):1})
    print('PASS: all 759375 five-cell matrices enumerated exactly')
    print('PASS: 21960 connected labelled matrices, 191 distinct relabelling classes')
    print('PASS: strongly connected 6300 labelled, 56 classes')
    print('PASS: seven spectral types, 175 trivial and 16 order-two automorphism groups')
    print('PASS: four-cell comparison 216 labelled, 9 classes, 3 strongly connected')
    print('PASS: 191 exact representatives, disjoint orbits covering all candidates')
    hist, hist_strong, by_spec=synchrony_profile()
    print('PASS: complete 52-partition synchrony profile', dict(sorted(hist.items())))
    print('PASS: strongly connected synchrony profile', dict(sorted(hist_strong.items())))
    print('PASS: exactly two five-cell synchrony-primitive classes; none at four cells')

if __name__=='__main__':main()
