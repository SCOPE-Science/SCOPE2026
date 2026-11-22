"""Finite exact 4-vertex metric-graph certificate for the radial kernel family.
Run: python3 checker.py .  No third-party packages required.
The checker exhausts all 64 edge colorings and verifies the eleven determinant
polynomials over the integers. Infinite claims use the proof in RESULT.md.
"""
from itertools import combinations, permutations
from math import sqrt, cos, pi

EDGES = tuple(combinations(range(4), 2))
REPRESENTATIVES = [
    ((), (2,)),
    (((0,1),), (0,3,-1)),
    (((0,1),(0,2)), (-1,4,-1)),
    (((0,3),(1,2)), (0,0,4,-2)),
    (((0,1),(0,2),(1,2)), (0,0,3,-1)),
    (((0,1),(0,2),(0,3)), (-1,3)),
    (((0,1),(0,3),(1,2)), (-1,2,2,-1)),
    (((0,1),(0,2),(0,3),(1,2)), (0,-1,4,-1)),
    (((0,2),(0,3),(1,2),(1,3)), (-2,4)),
    (((0,1),(0,2),(0,3),(1,2),(1,3)), (0,-1,3)),
    (EDGES, (0,0,0,2))
]

def plus(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))

def neg(a): return tuple(-v for v in a)

def minus(a,b): return plus(a,neg(b))

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return tuple(out)

def determinant3(g):
    a,b,c=g[0];d,e,f=g[1];h,i,j=g[2]
    return plus(minus(mul(a,minus(mul(e,j),mul(f,i))),
                      mul(b,minus(mul(d,j),mul(f,h)))),
                mul(c,minus(mul(d,i),mul(e,h))))

def det_polynomial(long_edges):
    long_edges=set(map(lambda e:tuple(sorted(e)),long_edges))
    def d(i,j): return (0,1) if tuple(sorted((i,j))) in long_edges else (1,)
    # H=2G, with G the Gram matrix for vectors p_i-p_0, i=1,2,3.
    H=[]
    for i in range(1,4):
        H.append([tuple(2*x for x in d(0,i)) if i==j
                  else minus(plus(d(0,i),d(0,j)),d(i,j))
                  for j in range(1,4)])
    det=determinant3(H)
    assert all(x%2==0 for x in det)
    
    coeffs=[x//2 for x in det]
    while len(coeffs)>1 and coeffs[-1]==0: coeffs.pop()
    return tuple(coeffs)  # 4 det G

def canon(edges):
    es={tuple(sorted(e)) for e in edges}
    return min(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in es))
               for p in permutations(range(4)))

classes={canon(edges) for mask in range(64)
         for edges in [[e for i,e in enumerate(EDGES) if (mask>>i)&1]]}
assert len(classes)==11
assert {canon(edges) for edges,_ in REPRESENTATIVES}==classes
for edges,expected in REPRESENTATIVES:
    got=det_polynomial(edges)
    assert got==expected,(edges,got,expected)

# Check the positive-semidefinite realization at each candidate t, for
# representative patterns, to high numerical precision. These diagnostics are
# supplementary to the analytic principal-minor argument.
resonances={2:(0,0,4,-2),3:(0,3,-1),
            (3+sqrt(5))/2:(-1,2,2,-1),2+sqrt(3):(-1,4,-1)}
feasible={2:1,3:2,(3+sqrt(5))/2:1,2+sqrt(3):2}
for t,expected_count in feasible.items():
    count=0
    for edges,poly in REPRESENTATIVES:
        d=lambda i,j:(t if tuple(sorted((i,j))) in edges else 1.0)
        G=[[d(0,i) if i==j else (d(0,i)+d(0,j)-d(i,j))/2
            for j in range(1,4)] for i in range(1,4)]
        principal=[G[i][i] for i in range(3)]+[
            G[i][i]*G[j][j]-G[i][j]**2 for i,j in combinations(range(3),2)]
        det=sum(poly[k]*t**k for k in range(len(poly)))
        if abs(det)<1e-8 and min(principal)>-1e-8:
            count+=1
    assert count==expected_count,(t,count,expected_count)

# Exact rational-resonance relation using quadratic-minimal polynomials:
# tau=8*t/(1+t)^2 -1, with t in {2,phi^2,3,2+sqrt3}.
for t,tau in [(2,7/9),((3+sqrt(5))/2,3/5),(3,1/2),(2+sqrt(3),1/3)]:
    assert abs(8*t/(1+t)**2-1-tau)<1e-12
pentagon=[(2/sqrt(5)*cos(2*pi*j/5),2/sqrt(5)*__import__('math').sin(2*pi*j/5)) for j in range(5)]
for i,j in combinations(range(5),2):
    dist2=sum((pentagon[i][k]-pentagon[j][k])**2 for k in (0,1))
    assert min(abs(dist2-(2-2/sqrt(5))),abs(dist2-(2+2/sqrt(5))))<1e-12
print('PASS: 64/64 edge colorings, 11/11 exact determinant identities,')
print('6 feasible four-point graph shapes, four exact parameter resonances,')
print('and 10/10 regular-pentagon squared distances.')
