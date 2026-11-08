"""Exact classification of F_2-smooth nets of binary ternary cubics.

Run with Python >=3.10 and SymPy >=1.12:
    python verify_smooth_cubic_nets.py

The Gröbner test is exact and over the algebraic closure. An independent
finite-extension evaluation is an additional consistency check, not a
replacement for the Gröbner test.
"""
import itertools
from collections import Counter
import sympy as sp

x, y, z = sp.symbols('x y z')
variables = (x, y, z)
exponents = ((3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),
             (1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1))
monomials = [x**a*y**b*z**c for a,b,c in exponents]
derivatives = [[sp.diff(m, u) for m in monomials] for u in variables]


def smooth(mask):
    partials = [sum(row[j] for j in range(10) if mask & (1 << j))
                for row in derivatives]
    gb = sp.groebner(partials, *variables, modulus=2)
    # A homogeneous ideal has no projective zero over the algebraic closure
    # iff its affine zero scheme is zero-dimensional (the origin only).
    return gb.is_zero_dimensional


def extension_points(q):
    # Projective points: [1,a,b], [0,1,b], [0,0,1]
    return [(1, a, b) for a in range(q) for b in range(q)] + [
        (0, 1, b) for b in range(q)] + [(0, 0, 1)]


def finite_field_mult(a,b,degree,poly):
    out=0
    while b:
        if b & 1:out ^= a
        b >>= 1
        a <<= 1
        if a & (1<<degree):a ^= poly
    return out


def finite_check(smooth_masks):
    # These are irreducible polynomials for degree m over F_2.
    polynomials={1:0b11,2:0b111,3:0b1011,4:0b10011}
    rejected=set()
    for degree,poly in polynomials.items():
        q=1<<degree
        multiply=[[finite_field_mult(a,b,degree,poly) for b in range(q)]
                  for a in range(q)]
        pts=extension_points(q)
        def dval(mask,point,var):
            a,b,c=point
            powers=((1,a,multiply[a][a]),(1,b,multiply[b][b]),
                    (1,c,multiply[c][c]))
            value=0
            for j,ex in enumerate(exponents):
                if not (mask>>j)&1 or not ex[var]%2: continue
                out=1
                for k in range(3):
                    out=multiply[out][powers[k][ex[k]-(k==var)]]
                value ^= out
            return value
        for mask in range(1,1024):
            if mask in rejected:continue
            if any(all(dval(mask,p,k)==0 for k in range(3)) for p in pts):
                rejected.add(mask)
    assert rejected == set(range(1,1024)) - smooth_masks, (
        len(rejected),len(smooth_masks),len(rejected ^ (set(range(1,1024))-smooth_masks)))
    return len(rejected)


def full_span(basis):
    result={0}
    for v in basis:result |= {t^v for t in tuple(result)}
    return result


def subspace_key(vectors):
    return tuple(sorted(full_span(vectors)-{0}))


def level_up(previous, allowed):
    allowed_set=set(allowed)
    out=set()
    for basis in previous:
        W=full_span(basis)
        for v in allowed:
            if v in W:continue
            if {t^v for t in W} <= allowed_set:
                out.add(tuple(sorted((W | {t^v for t in W}) - {0})))
    return out


def binary_rank(rows):
    basis=[]
    for value in rows:
        for w in basis:value=min(value,value^w)
        if value:basis.append(value)
    return len(basis)


def times(p,q):
    result={}
    for e,co in p.items():
        for f,do in q.items():
            mon=tuple(e[i]+f[i] for i in range(3))
            result[mon]=result.get(mon,0)^(co&do)
    return {mon:co for mon,co in result.items() if co}


def linear_transform(rows):
    powers=[{tuple(i==j for j in range(3)):1 for i in range(3) if (row>>i)&1}
            for row in rows]
    # Images of all ten cubic monomials.
    lookup={e:i for i,e in enumerate(exponents)}
    images=[]
    for e in exponents:
        result={(0,0,0):1}
        for j,power in enumerate(e):
            for _ in range(power):result=times(result,powers[j])
        images.append(sum(1<<lookup[mon] for mon in result))
    return images


def transform_mask(mask,transformation):
    result=0
    for j in range(10):
        if (mask>>j)&1:result ^= transformation[j]
    return result


def orbit_partition(planes,transformations):
    unseen=set(planes)
    classes=[]
    while unseen:
        representative=min(unseen)
        orbit={tuple(sorted(transform_mask(f,t) for f in representative))
               for t in transformations}
        assert orbit <= unseen
        assert 168 % len(orbit)==0
        classes.append((representative,len(orbit),168//len(orbit)))
        unseen-=orbit
    return classes


def independent_basis(members):
    basis=[]
    for m in members:
        if m not in full_span(basis):basis.append(m)
    assert len(basis)==3
    assert subspace_key(basis)==members
    return tuple(basis)


def rational_count(mask):
    total=0
    for p in range(1,8):
        value=0
        for j,e in enumerate(exponents):
            if (mask>>j)&1:
                value ^= int(all(((p>>k)&1) or e[k]==0 for k in range(3)))
        total += (value==0)
    return total


def main():
    smooth_masks={v for v in range(1,1024) if smooth(v)}
    assert len(smooth_masks)==336
    assert finite_check(smooth_masks)==687
    bydim={1:set((v,) for v in smooth_masks)}
    for d in (2,3,4):
        bydim[d]=level_up(bydim[d-1], sorted(smooth_masks))
    assert tuple(len(bydim[d]) for d in (1,2,3,4))==(336,5544,864,0)
    transformations=[linear_transform(rows) for rows in itertools.product(range(1,8),repeat=3)
                     if binary_rank(rows)==3]
    assert len(transformations)==168
    assert len({tuple(t) for t in transformations})==168
    classes=orbit_partition(bydim[3],transformations)
    assert len(classes)==8
    assert Counter(sz for _,sz,_ in classes)=={8:3,168:5}
    assert sum(sz for _,sz,_ in classes)==864
    # Certify exactly the eight orbit representatives and their stabilizers.
    expected_spectra=[(3,)*7, (1,1,3,3,3,5,5), (2,2,2,3,3,4,5),
                      (1,2,2,3,4,4,5), (3,)*7, (1,2,2,3,4,4,5),
                      (3,)*7, (1,1,2,4,4,4,5)]
    for ix,(representative,sz,stab) in enumerate(classes,1):
        basis=independent_basis(representative)
        assert len({tuple(sorted(transform_mask(f,t) for f in representative))
                    for t in transformations})==sz
        spectrum=tuple(sorted(rational_count(f) for f in representative))
        assert spectrum == expected_spectra[ix-1], (ix,spectrum)
        print('CLASS',ix,'basis_masks',basis,'members',representative,
              'orbit_size',sz,'stabilizer',stab,'F2_point_spectrum',spectrum)
    print('SMOOTH_NET_CLASSIFICATION_PASS',len(smooth_masks),len(bydim[2]),
          len(bydim[3]),len(classes))

if __name__=='__main__':main()
