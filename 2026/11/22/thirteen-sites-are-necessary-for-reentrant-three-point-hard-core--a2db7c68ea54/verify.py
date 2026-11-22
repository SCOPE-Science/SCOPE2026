"""Exact certificate for the first two-threshold hard-core tree occupancy effect.
Run with Python 3.10 or newer: python verify.py. Standard library only.
"""
from fractions import Fraction
from math import gcd, lcm


def trim(p):
    p = tuple(p)
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)


def sub(a, b):
    return add(a, tuple(-z for z in b))


def variations(signs):
    s = [v > 0 for v in signs if v]
    return sum(a != b for a, b in zip(s, s[1:]))


def desc_variations(p):
    return variations(reversed(p))


def primitive_positive_scale(q):
    """Multiply by a POSITIVE rational to obtain relatively prime integers."""
    den = 1
    for v in q: den = lcm(den, v.denominator)
    vals = [int(v*den) for v in q]
    div = 0
    for v in vals: div = gcd(div, abs(v))
    return trim(tuple(v // div for v in vals))


def remainder(a, b):
    """Remainder a modulo b over exact rationals, ascending coefficients."""
    a = list(map(Fraction, a)); b = list(map(Fraction, b))
    while len(a) >= len(b):
        k = a[-1]/b[-1]; offset = len(a)-len(b)
        for j, v in enumerate(b): a[offset+j] -= k*v
        while a and a[-1] == 0: a.pop()
    return tuple(a or [Fraction(0)])


def sturm_positive_roots(p):
    """Exact number of DISTINCT positive roots (all signs exact)."""
    p = trim(p)
    seq = [p, primitive_positive_scale(tuple(Fraction(i*p[i]) for i in range(1,len(p))))]
    while len(seq[-1]) > 1:
        r = remainder(seq[-2], seq[-1])
        if r == (0,): break
        seq.append(primitive_positive_scale(tuple(-v for v in r)))
    return variations(s[0] for s in seq) - variations(s[-1] for s in seq)


def rooted_types(max_n):
    # Unique rooted unlabelled trees are multisets of smaller rooted trees.
    types = [()]; sizes = [1]; A = [(1,)]; B = [(0,1)]
    count = [0]*(max_n+1); count[1] = 1
    witness_count = 0; ambiguous = []
    for n in range(2, max_n+1):
        candidates = [i for i, sz in enumerate(sizes) if sz < n]
        new = []
        def rec(remaining, first, chosen):
            if remaining == 0:
                new.append(tuple(chosen)); return
            for j in range(first, len(candidates)):
                i = candidates[j]
                if sizes[i] > remaining: break
                chosen.append(i)
                rec(remaining-sizes[i], j, chosen)
                chosen.pop()
        rec(n-1, 0, [])
        count[n] = len(new)
        for children in new:
            types.append(children); sizes.append(n)
            a,b = (1,), (0,1)
            for v in children:
                a = mul(a, add(A[v],B[v]));b = mul(b, A[v])
            A.append(a);B.append(b)
            # Only degree>=2 vertices can be a median of three distinct nodes.
            if len(children)>=2:
                witness_count += 1
                p = sub(b,a)
                if desc_variations(p)>=2:
                    nroots=sturm_positive_roots(p)
                    ambiguous.append((n,p,nroots))
                    assert nroots < 2, (n,p,nroots)
    expected=[0,1,1,2,4,9,20,48,115,286,719,1842,4766]
    assert count==expected, (count,expected)
    return count, witness_count, ambiguous


def brute_counts(n, edges, marked):
    aa=[0]*(n+1);bb=[0]*(n+1)
    for mask in range(1<<n):
        if any(((mask>>u)&1) and ((mask>>v)&1) for u,v in edges):continue
        k=mask.bit_count()
        if (mask>>marked)&1: bb[k]+=1
        else: aa[k]+=1
    return trim(aa),trim(bb)


def eval_poly(p, z):
    ans=0
    for k in reversed(p):ans=ans*z+k
    return ans


def brute_cumulant_sign(n, edges, triple, activity):
    # Separate occupancy-moment calculation, no Markov factorization assumed.
    w=0; singles=[0]*3; pairs=[0]*3; abc=0
    ij=[(0,1),(0,2),(1,2)]
    for mask in range(1<<n):
        if any((mask>>u)&1 and (mask>>v)&1 for u,v in edges):continue
        weight=activity**mask.bit_count();w+=weight
        vals=[(mask>>v)&1 for v in triple]
        for i in range(3):singles[i]+=weight*vals[i]
        for k,(i,j) in enumerate(ij): pairs[k]+=weight*vals[i]*vals[j]
        abc+=weight*vals[0]*vals[1]*vals[2]
    k=Fraction(abc,w)-Fraction(singles[0]*pairs[2]+singles[1]*pairs[1]+singles[2]*pairs[0],w*w)+Fraction(2*singles[0]*singles[1]*singles[2],w**3)
    return (k>0)-(k<0), k


def main():
    count, marked, ambiguous=rooted_types(12)
    assert marked==0 or marked>0
    assert len(ambiguous)==2
    assert all(n==11 and r==0 for n,_,r in ambiguous), ambiguous
    edges=[(1,0),(1,2),(1,4),(1,6),(0,8),(2,3),(4,5),(6,7),(8,9),(8,11),(9,10),(11,12)]
    a,b=brute_counts(13,edges,0)
    assert a==(1,12,56,129,153,86,17,1),a
    assert b==(0,1,10,40,80,80,32),b
    p=sub(b,a)
    assert p==(-1,-11,-46,-89,-73,-6,15,-1)
    assert desc_variations(p)==2 and sturm_positive_roots(p)==2
    assert eval_poly(p,3)<0 and eval_poly(p,4)>0 and eval_poly(p,14)>0 and eval_poly(p,15)<0
    for z,sgn in ((1,1),(4,-1),(15,1)):
        sign,val=brute_cumulant_sign(13,edges,(0,2,9),z)
        assert sign==sgn,(z,val)
    print('TREE_CERTIFICATE_OK')
    print('rooted_counts_n1_to_n12',count[1:])
    print('interior_rooted_candidates',marked)
    print('sturm_ambiguous',ambiguous)
    print('witness_A',a,'witness_B',b,'witness_P',p)
    print('witness_two_positive_roots',sturm_positive_roots(p))
    print('direct_triple_signs',[(z,brute_cumulant_sign(13,edges,(0,2,9),z)[0]) for z in (1,4,15)])

if __name__=='__main__':main()
