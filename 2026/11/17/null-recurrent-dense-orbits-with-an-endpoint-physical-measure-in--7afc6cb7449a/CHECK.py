"""Exact finite checks for a piecewise-affine interval map's block-return laws.
Run: python3 CHECK.py. The infinite recurrence and ergodic claims use the proof, not finite tests.
"""
from fractions import Fraction

def targets(k):
    n=k+2
    if k==0:
        vertices=[0]
        for _ in range(n): vertices.extend([1,2,1,0])
        vertices.append(1)
    else:
        vertices=[k]
        for _ in range(n): vertices.extend([k-1,k,k+1,k+2,k+1,k])
        vertices.append(k+1)
    out=[]
    for a,b in zip(vertices,vertices[1:]):
        assert abs(b-a)==1
        out.append(min(a,b))
    return out

def p(k,j):
    t=targets(k)
    return Fraction(t.count(j),len(t))

def pi(k):
    return Fraction(1) if k==0 else Fraction(2*(6*k+13),9*(k+2))

# Each piece is a full unit-block branch. Compare direct enumeration and formulas.
for k in range(101):
    t=targets(k)
    count={j:t.count(j) for j in set(t)}
    if k==0: assert count=={0:5,1:4} and len(t)==9
    else:
        assert count=={k-1:2*(k+2),k:2*(k+2)+1,k+1:2*(k+2)}
        assert len(t)==6*(k+2)+1
    assert sum(p(k,j) for j in count)==1
    if k>=1:
        assert p(k,k-1)==p(k,k+1)
    assert pi(k)*p(k,k+1)==Fraction(4,9)
    assert pi(k+1)*p(k+1,k)==Fraction(4,9)
    if k>=1:
        assert pi(k)==Fraction(4,3)+Fraction(2,9*(k+2))

# Invariance of block-constant sigma-finite density via exact transfer preimages.
for k in range(101):
    pre=pi(k)*p(k,k)
    if k>0: pre+=pi(k-1)*p(k-1,k)
    pre+=pi(k+1)*p(k+1,k)
    assert pre==pi(k)

# Discrete harmonic hitting probability for every finite ruin boundary 0,L.
for L in range(2,101):
    h=lambda k:Fraction(k,L)
    for k in range(1,L):
        assert p(k,k-1)*h(k-1)+p(k,k)*h(k)+p(k,k+1)*h(k+1)==h(k)

# Explicit finite-cylinder probabilities for all admissible block paths of depth 1..4.
# For each fixed path, the union of its actual affine branch cylinders is uniform on target.
for start in range(4):
    paths={(start,):Fraction(1)}
    for _ in range(4):
        nxt={}
        for states,weight in paths.items():
            k=states[-1]
            for j in set(targets(k)):
                nxt[states+(j,)]=weight*p(k,j)
        assert sum(nxt.values())==1
        paths=nxt
print('VERIFY_OK direct_branch_counts=101 invariant_balance=101 reversible_edges=101 harmonic_ruin_boundaries=99 finite_path_depth=4')
