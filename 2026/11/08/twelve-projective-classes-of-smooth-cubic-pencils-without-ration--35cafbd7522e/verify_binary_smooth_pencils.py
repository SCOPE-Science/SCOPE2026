"""Exact and reproducible census of smooth cubic pencils over F_2 with no F_2 base point.

Python >=3.10 and SymPy >=1.12. Run:
    python verify_binary_smooth_pencils.py

No external input or previous output is used. All 1023 nonzero cubics are tested
for geometric smoothness with exact Groebner bases over F_2. A second test
searches singularities over F_2, F_4, F_8, F_16 (a cross-check, not a
substitute for the algebraic-closure Groebner test). Every 2D subspace of
F_2^10 is then examined. The full PGL_3(F_2) group acts by substitution.
"""

from collections import Counter
from itertools import product
import sympy as sp

X, Y, Z = sp.symbols("X Y Z")
VARS = (X, Y, Z)
EXP = ((3,0,0), (0,3,0), (0,0,3), (2,1,0), (2,0,1),
       (1,2,0), (0,2,1), (1,0,2), (0,1,2), (1,1,1))
INDEX = {e:i for i,e in enumerate(EXP)}
MONS = tuple(X**a*Y**b*Z**c for a,b,c in EXP)
DIFFS = tuple(tuple(sp.diff(t, v) for t in MONS) for v in VARS)
POINTS = tuple(range(1, 8))  # nonzero binary triples are unique projective points
LINES = tuple(tuple(p for p in POINTS if (p & l).bit_count()%2 == 0)
              for l in range(1, 8))

EXPECTED = (
    ((7,249,254),1,(1,3,3),1,1),
    ((7,761,766),1,(2,2,3),1,1),
    ((15,199,200),1,(1,3,3),0,1),
    ((15,677,682),1,(2,2,3),0,2),
    ((15,721,734),1,(2,2,3),0,0),
    ((15,758,761),1,(2,2,3),0,0),
    ((31,172,179),1,(1,1,5),1,2),
    ((31,675,700),1,(1,2,4),1,2),
    ((31,705,734),1,(1,2,4),1,2),
    ((31,711,728),1,(1,2,4),1,1),
    ((31,750,753),1,(1,2,4),1,0),
    ((31,835,860),1,(1,2,4),1,1),
)


def geom_smooth(mask):
    # In characteristic 2 the cubic Euler identity is F = X F_X + Y F_Y + Z F_Z.
    # Thus the projective common zeros of its three derivatives are precisely
    # the projective singularities. A homogeneous ideal over a field has a
    # projective zero over the algebraic closure iff it is not zero-dimensional.
    partials = [sum(DIFFS[k][i] for i in range(10) if mask>>i&1)
                for k in range(3)]
    return sp.groebner(partials, X, Y, Z, modulus=2).is_zero_dimensional


def eval_mask_f2(mask, p):
    value = 0
    for i, exp in enumerate(EXP):
        if mask>>i & 1 and all((p>>k & 1) or exp[k]==0 for k in range(3)):
            value ^= 1
    return value


def rational_bitset(mask):
    return sum(1 << (p-1) for p in POINTS if eval_mask_f2(mask,p)==0)


def blocking(bitset):
    return all(any(bitset >> (p-1) & 1 for p in L) for L in LINES)


def gf_mul(a,b,m,irreducible):
    out=0
    while b:
        if b&1:out ^= a
        b>>=1
        a<<=1
        if a & (1<<m):a ^= irreducible
    return out


def extension_singular_masks():
    # Independent direct derivative evaluation over four field extensions.
    singular=set()
    for m,irreducible in ((1,0b11),(2,0b111),(3,0b1011),(4,0b10011)):
        q=1<<m
        mul=[[gf_mul(a,b,m,irreducible) for b in range(q)] for a in range(q)]
        pts=[(1,a,b) for a in range(q) for b in range(q)] + [(0,1,b) for b in range(q)] + [(0,0,1)]
        deriv_values=[]
        for p in pts:
            powers=tuple((1,c,mul[c][c],mul[mul[c][c]][c]) for c in p)
            at=[]
            for k in range(3):
                vals=[]
                for e in EXP:
                    if not e[k]%2:
                        vals.append(0)
                        continue
                    v=1
                    for h in range(3):
                        v=mul[v][powers[h][e[h]-(h==k)]]
                    vals.append(v)
                at.append(tuple(vals))
            deriv_values.append(at)
        for mask in range(1,1024):
            if mask in singular:continue
            support=[i for i in range(10) if mask>>i&1]
            if any(all(xor_values(row,support)==0 for row in at) for at in deriv_values):
                singular.add(mask)
    return singular


def xor_values(row,support):
    x=0
    for i in support:x ^= row[i]
    return x


def binary_rank(rows):
    span={0}
    for a in rows:
        if a in span:continue
        span |= {a^v for v in tuple(span)}
    return len(span)


def poly_mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(e[i]+f[i] for i in range(3))
            out[g]=out.get(g,0)^(c&d)
    return {e:v for e,v in out.items() if v}


def linear_images(rows):
    linear=[]
    for row in rows:
        linear.append({tuple(int(k==j) for k in range(3)):1
                       for j in range(3) if row>>j&1})
    ans=[]
    for exp in EXP:
        p={(0,0,0):1}
        for k in range(3):
            for _ in range(exp[k]):p=poly_mul(p,linear[k])
        ans.append(sum(1<<INDEX[e] for e,v in p.items() if v))
    return tuple(ans)


def change_coords(mask,images):
    out=0
    for i in range(10):
        if mask>>i&1:out ^= images[i]
    return out


def all_smooth_pencils(smooth):
    # Canonical representation of a 2D space is its three nonzero masks.
    # For any pair a,b, the third is a xor b; impose a<b<a xor b.
    pencils=set()
    for a in sorted(smooth):
        for b in sorted(smooth):
            if b<=a:continue
            c=a^b
            if c>b and c in smooth:pencils.add((a,b,c))
    return pencils


def net_extension_count(pencil,smooth):
    # Each admissible 3D space containing the pencil has four members
    # outside the pencil, all giving the same extension, hence divide by 4.
    a,b,c=pencil
    compatible=sum(v not in pencil and all(v^w in smooth for w in (0,a,b,c))
                   for v in range(1,1024))
    assert compatible%4==0
    return compatible//4


def main():
    assert len(EXP)==10 and len(set(EXP))==10
    assert len(POINTS)==len(LINES)==7
    assert all(len(L)==3 for L in LINES)
    assert len({L for L in LINES})==7
    smooth={v for v in range(1,1024) if geom_smooth(v)}
    assert len(smooth)==336, len(smooth)
    singular_by_extensions=extension_singular_masks()
    assert singular_by_extensions == set(range(1,1024))-smooth
    point_sets={v:rational_bitset(v) for v in range(1,1024)}
    assert all(point_sets[a]&point_sets[b]==point_sets[a]&point_sets[a^b]
               for a in range(1,1024) for b in (1,17,391,1023) if a!=b)
    pencils=all_smooth_pencils(smooth)
    assert len(pencils)==5544, len(pencils)
    basefree={t for t in pencils if not(point_sets[t[0]] & point_sets[t[1]])}
    assert len(basefree)==2016, len(basefree)
    # Second enumeration: inspect all Gaussian-binomial (10,2) subspaces
    # without prefiltering by geometric smoothness.
    all_planes=set()
    for a in range(1,1024):
        for b in range(a+1,1024):
            c=a^b
            if c>b:all_planes.add((a,b,c))
    assert len(all_planes)==174251
    assert {p for p in all_planes if all(v in smooth for v in p) and
            not(point_sets[p[0]] & point_sets[p[1]])} == basefree

    block_count={p:sum(blocking(point_sets[v]) for v in p) for p in basefree}
    extension_count={p:net_extension_count(p,smooth) for p in basefree}
    assert Counter(block_count.values())=={0:672,1:1344}
    assert Counter(extension_count.values())=={0:504,1:840,2:672}
    profile=Counter((tuple(sorted(point_sets[v].bit_count() for v in p)),
                     block_count[p],extension_count[p]) for p in basefree)
    assert sum(profile.values())==2016
    assert all(sum(point_sets[v].bit_count() for v in p)==7 for p in basefree)
    assert all(not(point_sets[a]&point_sets[b]) and
               not(point_sets[a]&point_sets[c]) and
               not(point_sets[b]&point_sets[c]) for a,b,c in basefree)

    matrices=[rows for rows in product(range(1,8),repeat=3)
              if binary_rank(rows)==8]
    assert len(matrices)==168 and len(set(matrices))==168
    transforms=[linear_images(rows) for rows in matrices]
    assert len(set(transforms))==168
    remaining=set(basefree)
    table=[]
    while remaining:
        rep=min(remaining)
        orbit={tuple(sorted(change_coords(v,images) for v in rep)) for images in transforms}
        assert orbit<=basefree and orbit<=remaining
        assert len(orbit)==168
        record=(rep,168//len(orbit),
                tuple(sorted(point_sets[v].bit_count() for v in rep)),
                block_count[rep],extension_count[rep])
        assert all(block_count[p]==block_count[rep] and
                   extension_count[p]==extension_count[rep] for p in orbit)
        table.append(record)
        remaining -= orbit
    table=tuple(table)
    assert table==EXPECTED, (table,EXPECTED)
    assert len(table)==12
    assert Counter(row[3] for row in table)=={0:4,1:8}
    assert Counter(row[4] for row in table)=={0:3,1:5,2:4}
    print('SMOOTH_FORMS',len(smooth),'SINGULAR_FORMS',len(singular_by_extensions))
    print('ALL_TWO_DIMENSIONAL_SUBSPACES',len(all_planes))
    print('ALL_SMOOTH_PENCILS',len(pencils))
    print('SMOOTH_BASEPOINTFREE_PENCILS',len(basefree))
    print('BLOCKING_HISTOGRAM',dict(sorted(Counter(block_count.values()).items())))
    print('SMOOTH_NET_EXTENSION_HISTOGRAM',dict(sorted(Counter(extension_count.values()).items())))
    for i,(rep,st,counts,blocking_number,extensions) in enumerate(table,1):
        print('CLASS',i,'member_masks',rep,'orbit',168,'stabilizer',st,
              'point_counts',counts,'blocking_members',blocking_number,
              'net_extensions',extensions)
    print('PROFILE_COUNTS',sorted(profile.items()))
    print('BINARY_SMOOTH_BASEPOINTFREE_CUBIC_PENCILS_PASS')

if __name__=='__main__':
    main()
