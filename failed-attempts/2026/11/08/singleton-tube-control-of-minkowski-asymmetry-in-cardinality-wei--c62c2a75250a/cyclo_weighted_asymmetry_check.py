"""Exact vertex-support checks and independent LP corroboration for cyclic simplex sums.
Run: python cyclo_weighted_asymmetry_check.py   (requires scipy for the LP section).
"""
from fractions import Fraction
from itertools import permutations
from scipy.optimize import linprog

def intervals(n):
    return [(l,tuple((i+j)%n for j in range(l)))
            for l in range(1,n) for i in range(n)] + [(n,tuple(range(n)))]

def vertex_list(n,weights):
    terms = [(set(S),weights[l-1]) for l,S in intervals(n)]
    vertices=set()
    for order in permutations(range(n)):
        rank=[0]*n
        for k,i in enumerate(order): rank[i]=k
        coord=[0]*n
        for S,w in terms:
            coord[max(S,key=lambda i:rank[i])]+=w
        vertices.add(tuple(coord))
    return vertices

def exact_test(n,weights):
    vertices=vertex_list(n,weights)
    fullsum=n*sum(weights[:-1])+weights[-1]
    if any(sum(v)!=fullsum for v in vertices): raise AssertionError('wrong affine sum')
    tubes=intervals(n)[:-1]
    mins=[];maxs=[]
    for s,S in tubes:
        ss=set(S)
        a=min(sum(v[i] for i in ss) for v in vertices)
        b=max(sum(v[i] for i in ss) for v in vertices)
        exp_a=sum((s-l+1)*weights[l-1] for l in range(1,s+1))
        exp_b=fullsum-sum((n-s-l+1)*weights[l-1] for l in range(1,n-s+1))
        assert (a,b)==(exp_a,exp_b),(n,weights,S,a,b,exp_a,exp_b)
        mins.append(a);maxs.append(b)
    c=Fraction(fullsum,n)
    ratios=[Fraction(M-s*c,s*c-m)
            for (s,S),m,M in zip(tubes,mins,maxs)]
    expression=(sum((l-1)*weights[l-1] for l in range(2,n))
                +Fraction(n-1,n)*weights[-1]) / (
                sum(weights[l-1] for l in range(2,n)) +Fraction(1,n)*weights[-1])
    assert max(ratios)==expression
    assert all(r<expression for (s,_),r in zip(tubes,ratios) if s>1)
    # Independent Chebyshev-type LP in the transformed variables b=(lambda+1)*center.
    # Facet support extrema come from enumerated vertices, not the closed formula.
    A=[];B=[]
    for (_,S),m,M in zip(tubes,mins,maxs):
        row=[-int(i in S) for i in range(n)]+[float(m)]
        A.append(row);B.append(-float(M))
    eq=[[1.0]*n+[-float(fullsum)]]
    sol=linprog([0.0]*n+[1.0],A_ub=A,b_ub=B,A_eq=eq,b_eq=[float(fullsum)],
                bounds=[(None,None)]*n+[(1,None)],method='highs')
    assert sol.success,sol.message
    assert abs(sol.x[-1]-float(expression))<1e-7,(n,weights,sol.x[-1],expression)
    midpoint=[sol.x[i]/(sol.x[-1]+1) for i in range(n)]
    assert all(abs(x-float(c))<1e-6 for x in midpoint),midpoint
    return len(vertices),len(tubes)

if __name__=='__main__':
    tests=0;vertices=0;facets=0
    for n in range(3,8):
        for weights in (
            tuple([1]*n),tuple(range(1,n+1)),
            tuple(n+2-i for i in range(n)),
            tuple(1+(i*i+2*i)%7 for i in range(n))):
            nv,nf=exact_test(n,weights)
            tests+=1;vertices+=nv;facets+=nf
    print('CYCLIC_WEIGHTED_MINKOWSKI_ASYMMETRY_CHECKS_PASSED',
          'profiles=',tests,'distinct_vertices_total=',vertices,
          'tubes_checked=',facets)
