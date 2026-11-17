"""Exact rational/polynomial verification of two six-vertex contact graphs.

Dependencies: Python >=3.9 and SymPy >=1.10.  Run: python verify.py
Two distinct algorithms: edge-state enumeration and vertex-set connectivity recursion.
"""
from collections import Counter
from itertools import combinations
from sympy import Symbol, Poly, Rational, cancel, expand, factor, nroots

p = Symbol('p')
N = 6
PRISM = ((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5))
BIPARTITE = tuple((u,v) for u in range(3) for v in range(3,6))

def direct(E):
    """Bernstein edge-state counts: coefficient for e open edges / 6."""
    table = [[0] * 10 for _ in range(N+1)]
    for mask in range(1<<len(E)):
        parent = list(range(N))
        def find(a):
            while parent[a]!=a: a=parent[a]
            return a
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                parent[find(u)]=find(v)
        roots = [find(v) for v in range(N)]
        sizes = Counter(roots)
        e = mask.bit_count()
        for v in range(N):
            for k in range(1, sizes[roots[v]]+1):
                table[k][e] += 1
    return table

def tails(t):
    return {k:expand(sum(Rational(c,6)*p**e*(1-p)**(9-e)
                          for e,c in enumerate(t[k]))) for k in range(1,N+1)}

def independent_vertex_recursion(E):
    """Independently compute component law through rooted induced-subgraph reliability.

    c(S) = Pr[retained induced graph on S is connected].  For a root r in S,
    c(S)=1-sum(c(U)*(1-p)^cross(U,S\\U)) for proper U subset S containing r.
    Pr[full-graph root component S]=c(S)*(1-p)^cross(S,V\\S).
    """
    edge_set = {frozenset(e) for e in E}
    def cut(A,B):
        return sum(frozenset((a,b)) in edge_set for a in A for b in B)
    polys = [0]*(1<<N)
    for size in range(1,N+1):
        for vv in combinations(range(N),size):
            mask=sum(1<<v for v in vv); root=vv[0]
            if size==1:
                polys[mask]=1
                continue
            term=1
            sub=(mask-1)&mask
            while sub:
                if sub & (1<<root):
                    U=[v for v in vv if sub>>v&1]
                    W=[v for v in vv if not (sub>>v&1)]
                    term-=polys[sub]*(1-p)**cut(U,W)
                sub=(sub-1)&mask
            polys[mask]=expand(term)
    ans={k:0 for k in range(1,N+1)}
    for S in range(1,1<<N):
        A=[v for v in range(N) if S>>v&1]
        B=[v for v in range(N) if not(S>>v&1)]
        # Every root in A has connected component exactly A.
        ans[len(A)]+=Rational(len(A),N)*polys[S]*(1-p)**cut(A,B)
    return {k:expand(v) for k,v in ans.items()}

tp,tb=direct(PRISM),direct(BIPARTITE)
sp,sb=tails(tp),tails(tb)
rp=independent_vertex_recursion(PRISM)
rb=independent_vertex_recursion(BIPARTITE)
for k in range(1,N+1):
    assert expand(sp[k]-sum(rp[j] for j in range(k,N+1)))==0, ('prism',k)
    assert expand(sb[k]-sum(rb[j] for j in range(k,N+1)))==0, ('bipartite',k)
expected={
  2: 0,3:0,
  4: p**3*(1-p)**3*(4-3*p),
  5: p**4*(1-p)**3*(5-4*p),
  6: p**5*(1-p)**3*(6-5*p),
}
for k,target in expected.items():
    assert expand((sb[k]-sp[k])-target)==0, k
assert all(tb[k]==tp[k] for k in (2,3))
assert [tb[4][e]-tp[4][e] for e in range(10)] == [0,0,0,24,54,36,6,0,0,0]
assert [tb[5][e]-tp[5][e] for e in range(10)] == [0,0,0,0,30,36,6,0,0,0]
assert [tb[6][e]-tp[6][e] for e in range(10)] == [0,0,0,0,0,36,6,0,0,0]

# Tails include Pr[X >= k].  E[X]=sum_k S_k and E[X²]=sum_k(2k-1)S_k.
def moments(s):
    mean=expand(sum(s.values()))
    m2=expand(sum((2*k-1)*s[k] for k in s))
    return mean,m2,expand(m2-mean**2)
mp,mp2,vp=moments(sp)
mb,mb2,vb=moments(sb)
assert expand((mb-mp)-p**3*(1-p)**3*(4+2*p+2*p**2-5*p**3))==0
Q=Poly.from_list([245,-1123,1717,-823,168,-832,596,248,-26,-161,-34,-4,20],p).as_expr()
assert expand((vb-vp)-p**3*(1-p)**3*Q)==0
assert expand((mb2-mp2)-p**3*(1-p)**3*(28+24*p+30*p**2-55*p**3))==0

# Exact Descartes certificate for a single root in (0,1).
# q(p) transformed by p=u/(1+u); coefficients are integer, one sign change.
u=Symbol('u')
R=Poly(cancel((1+u)**12*Q.subs(p,u/(1+u))),u)
assert list(reversed(R.all_coeffs()))==[20,236,1242,3679,6235,4684,-2428,-8366,-7038,-3191,-870,-135,-9]
assert Q.subs(p,0)==20 and Q.subs(p,1)==-9
assert Poly(Q,p).count_roots(0,1)==1
root=[z for z in nroots(Q,maxsteps=250) if abs(float(z.as_real_imag()[1]))<1e-10 and 0<float(z.as_real_imag()[0])<1]
assert len(root)==1
print('PASS: independent 512-edge-state and vertex-subset connectivity recurrences for both graphs')
print('PASS: exact tails k=2..6, full stochastic dominance, two moment identities, variance sign')
print('PASS: 1 positive Descartes root of Q(u/(1+u)) on u>0 and exactly one p in (0,1)')
print('critical p ~',root[0])
print('V_B-V_P at p=1/4:',(vb-vp).subs(p,Rational(1,4)))
print('V_B-V_P at p=1/2:',(vb-vp).subs(p,Rational(1,2)))
