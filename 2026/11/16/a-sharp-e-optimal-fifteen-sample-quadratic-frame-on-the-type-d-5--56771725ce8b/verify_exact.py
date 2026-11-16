"""Exact reproducibility of optimal quadratic sampling on D5 root lines.
Requires SymPy. All spectral conclusions are certified by rational algebra.
"""
from itertools import combinations
from collections import Counter, defaultdict
import sympy as s

n=5
edges=list(combinations(range(n),2))
t=s.symbols('t')
B_all=s.zeros(n,len(edges))
for k,(i,j) in enumerate(edges): B_all[i,k]=B_all[j,k]=1
assert B_all*B_all.T == 3*s.eye(n)+s.ones(n)
patterns=Counter(); representatives={}; valid=0
for inds in combinations(range(len(edges)),n):
    H=[edges[i] for i in inds]
    B=B_all[:,inds]
    if B.det()==0: continue
    valid+=1
    deg=tuple(sorted(sum(u in edge for edge in H) for u in range(n)))
    patterns[deg]+=1
    representatives.setdefault(deg,(H,B))
assert patterns=={
  (1,1,2,2,4):30,(1,1,2,3,3):60,
  (1,2,2,2,3):60,(2,2,2,2,2):12
}
assert valid==162
P={}; minimum_intervals={}
for deg,(H,B) in representatives.items():
    Q=B*B.T
    M=(4*t*t-5*t)*s.eye(n)-t*s.ones(n)+(1-t)*Q
    p=s.factor(M.det()/4**n)
    P[deg]=s.Poly(p,t)
    # Direct exact 15x15 matrix Gram (avoid introducing radicals via scaling columns).
    # Set offdiag variables y_ij=Q_ij/sqrt(2), then row coefficients
    # diag entries 1/2; offdiag entries +/-1; this is nonorthonormal.
    # Use a symmetrically scaled row-Gram to restore Frobenius geometry:
    # E E^T entry = (trace(A_v A_w)) where A_v=v v^T.
    selected=[]
    Hset=set(H)
    for e in edges:
        selected.append((e,+1))
        if e in Hset: selected.append((e,-1))
    assert len(selected)==15
    rowG=s.zeros(15)
    for a,(e,sg) in enumerate(selected):
        for b,(f,sh) in enumerate(selected):
            v={e[0]:1,e[1]:sg};w={f[0]:1,f[1]:sh}
            inner=sum(v.get(j,0)*w.get(j,0) for j in range(n))
            rowG[a,b]=s.Rational(inner**2,4)
    actual=s.Poly(rowG.charpoly(t).as_expr(),t)
    expected=s.Poly((t-1)**5*P[deg].as_expr(),t)
    assert actual==expected,(deg,actual,expected)
    assert actual.eval(0)==s.Rational((-1)**15,256)
    # Root location exactly certified by Sturm's theorem and rational endpoints.
    brackets={
      (1,1,2,2,4): (s.Rational(49,1000),s.Rational(50,1000)),
      (1,1,2,3,3): (s.Rational(75,1000),s.Rational(76,1000)),
      (1,2,2,2,3): (s.Rational(43,1000),s.Rational(44,1000)),
      (2,2,2,2,2): (s.Rational(75,1000),s.Rational(76,1000))
    }
    lo,hi=brackets[deg]
    assert P[deg].count_roots(0,lo)==0,(deg,'too-small root')
    assert P[deg].count_roots(lo,hi)==1,(deg,'isolation')
    assert P[deg].count_roots(hi,s.oo)==P[deg].count_roots(0,s.oo)-1,(deg,'remaining roots')
    minimum_intervals[deg]=(str(lo),str(hi))
    print('degree class',deg,'graphs',patterns[deg],
          'sampling sets',patterns[deg]*32,'characteristic P:',s.factor(P[deg].as_expr()),
          'least eigenvalue in',minimum_intervals[deg])

q4=s.Poly(16*t**4-52*t**3+53*t**2-17*t+1,t)
assert all(s.rem(P[typ],q4).is_zero for typ in [(1,1,2,3,3),(2,2,2,2,2)])
assert q4.count_roots(s.Rational(75,1000),s.Rational(76,1000))==1
assert q4.count_roots(0,s.Rational(75,1000))==0
# The other factor of the 5-cycle has no root below 0.076 either.
assert all(s.rem(P[typ],q4).is_zero for typ in [(1,1,2,3,3),(2,2,2,2,2)])
assert 2304==32*(60+12)
assert 960==32*30
assert 1920==32*60
assert 5184==2304+960+1920
assert 15504==s.binomial(20,15)
print('PASS: exact basis count, all four characteristic polynomial classes, Sturm root ordering, sharp count')
