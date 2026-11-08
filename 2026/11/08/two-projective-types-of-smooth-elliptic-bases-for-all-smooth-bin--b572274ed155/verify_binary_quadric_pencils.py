#!/usr/bin/env python3
"""Exact binary-quadratic-form pencil census and projective orbit certificate.
Requires Python >=3.10 and SymPy for the four affine Jacobian-ideal tests.
The monomial ordering and generators are printed in the accompanying proof.
"""
from collections import Counter
from itertools import combinations
from functools import reduce
import sympy as sp

MONOMIALS = [(i, i) for i in range(4)] + list(combinations(range(4),2))
REPS = {(192,352):(560,6,(9,9,9)),
        (192,353):(3360,6,(9,9,9)),
        (192,357):(5040,2,(5,5,9)),
        (192,358):(5040,4,(5,9,9)),
        (198,367):(336,0,(5,5,5))}

def quad(q, vec):
    return sum(((q >> i) & 1) * ((vec >> a) & 1) * ((vec >> b) & 1)
               for i,(a,b) in enumerate(MONOMIALS)) & 1

def pfaffian(coeff):
    return (((coeff>>0)&1)*((coeff>>5)&1) ^
            ((coeff>>1)&1)*((coeff>>4)&1) ^
            ((coeff>>2)&1)*((coeff>>3)&1))

def is_smooth(q):
    return pfaffian(q>>4)==1

def rank_gf2(vectors, dim=4):
    basis={}
    for v in vectors:
        for bit in reversed(range(dim)):
            if not (v>>bit)&1:continue
            if bit in basis:v^=basis[bit]
            else:
                basis[bit]=v;break
    return len(basis)

def alt_rank(q):
    rows=[0]*4
    for t,(i,j) in enumerate(MONOMIALS[4:]):
        if (q>>(t+4))&1:
            rows[i]^=1<<j
            rows[j]^=1<<i
    return rank_gf2(rows)

def pencil(a,b):
    t=sorted((a,b,a^b))
    return t[0],t[1]

def transformed(q, matrix):
    # matrix[i] is the linear form substituted for x_i (bitmask).
    values=[quad(q,row) for row in matrix]
    new=values[:]
    for i,j in combinations(range(4),2):
        new.append(quad(q,matrix[i]^matrix[j]) ^ values[i] ^ values[j])
    return sum(v<<i for i,v in enumerate(new))

def groebner_unit_on_each_chart(a,b):
    x=sp.symbols('x0:4')
    mon=[x[i]*x[j] for i,j in MONOMIALS]
    f=sum(mon[t] for t in range(10) if (a>>t)&1)
    g=sum(mon[t] for t in range(10) if (b>>t)&1)
    d=[sp.diff(f,z) for z in x]
    e=[sp.diff(g,z) for z in x]
    minors=[d[i]*e[j]-d[j]*e[i] for i,j in combinations(range(4),2)]
    certificates=[]
    for i in range(4):
        v=[z for k,z in enumerate(x) if k!=i]
        eqs=[sp.expand(h.subs(x[i],1)) for h in [f,g,*minors]]
        gb=sp.groebner(eqs,*v,order='lex',modulus=2)
        certificates.append(tuple(map(str,gb.exprs)))
        assert gb.contains(sp.Integer(1)),(a,b,i,gb.exprs)
    return certificates


def count_extension_base(a,b, degree, irreducible):
    """Direct F_(2^degree) projective base point census (not a zeta extrapolation)."""
    q=1<<degree
    def mul(u,v):
        z=0
        while v:
            if v&1:z^=u
            v>>=1
            u<<=1
            if u&q:u^=irreducible
        return z
    def ev(mask,coords):
        acc=0
        for t,(i,j) in enumerate(MONOMIALS):
            if mask>>t&1:acc^=mul(coords[i],coords[j])
        return acc
    count=0
    for pivot in range(4):
        # First nonzero coordinate (at pivot) fixed to 1.
        from itertools import product
        for after in product(range(q),repeat=3-pivot):
            x=(0,)*pivot+(1,)+after
            if ev(a,x)==ev(b,x)==0:count+=1
    return count


def matrix_product(A,B):
    return tuple(reduce(
                     lambda v,j:v^(B[j] if (A[i]>>j)&1 else 0),
                     range(4),0) for i in range(4))

def matrix_order(A):
    identity=tuple(1<<i for i in range(4))
    prod=identity
    for n in range(1,33):
        prod=matrix_product(prod,A)
        if prod==identity:return n
    raise AssertionError('not a finite-order 4x4 invertible matrix')

def certify_stabilizer_groups():
    groups={
      (192,357):[(1,2,4,8),(3,2,12,8),(4,8,1,2),(12,8,3,2)],
      (192,358):[(1,2,4,8),(8,4,2,1),(10,13,11,5),(5,11,13,10)]}
    for rep,items in groups.items():
        H=set(items)
        assert len(H)==4
        assert all(pencil(transformed(rep[0],A),transformed(rep[1],A))==rep for A in H)
        assert all(matrix_product(A,B) in H for A in H for B in H)
        orders=Counter(matrix_order(A) for A in H)
        assert orders==({(192,357):{1:1,2:3},(192,358):{1:1,2:1,4:2}}[rep])
        print('stabilizer group',rep, 'orders',dict(orders))

def main():
    assert sum(pfaffian(c) for c in range(64))==28
    assert all(is_smooth(q)==(alt_rank(q)==4) for q in range(1024))
    forms={q for q in range(1024) if is_smooth(q)}
    assert len(forms)==448
    pts=[sum(1<<(v-1) for v in range(1,16) if quad(q,v)==0)
         for q in range(1024)]
    assert Counter(pts[q].bit_count() for q in forms)=={5:168,9:280}
    all_pencils={pencil(a,b) for a in forms for b in forms
                 if a<b and (a^b) in forms}
    assert len(all_pencils)==14336
    # Independent polar-only enumerator: 56 admissible polar pencils,
    # 16*16 quadratic refinements per polar pencil.
    polars=[c for c in range(64) if pfaffian(c)]
    polar_pencils={pencil(a,b) for a in polars for b in polars
                   if a<b and (a^b) in polars}
    assert len(polar_pencils)==56 and len(all_pencils)==56*16*16
    assert all(sum(pts[q].bit_count() for q in (a,b,a^b))==15+2*(pts[a]&pts[b]).bit_count()
               for a,b in all_pencils)
    assert Counter((pts[a]&pts[b]).bit_count() for a,b in all_pencils)=={
        0:336,2:5040,4:5040,6:3920}

    transformations=[]
    for i in range(4):
        for j in range(4):
            if i!=j:
                M=tuple((1<<k)^(1<<j if k==i else 0) for k in range(4))
                transformations.append(tuple(transformed(q,M) for q in range(1024)))
    assert len(transformations)==12
    unseen=set(all_pencils)
    orbit_info=[]
    while unseen:
        rep=min(unseen)
        unseen.remove(rep)
        seen={rep}; queue=[rep]
        while queue:
            a,b=queue.pop()
            for action in transformations:
                c=pencil(action[a],action[b])
                if c not in seen:
                    assert c in unseen
                    unseen.remove(c);seen.add(c);queue.append(c)
        size=len(seen)
        bases=Counter((pts[a]&pts[b]).bit_count() for a,b in seen)
        profiles=Counter(tuple(sorted(pts[q].bit_count() for q in (a,b,a^b)))
                         for a,b in seen)
        assert len(bases)==len(profiles)==1
        onlybase=next(iter(bases)); onlyprofile=next(iter(profiles))
        orbit_info.append((rep,size,onlybase,onlyprofile))
    assert len(orbit_info)==5
    for rep,size,base,profile in orbit_info:
        assert rep in REPS
        assert (size,base,profile)==REPS[rep]
        assert 20160%size==0
        print('orbit',rep,'size',size,'stabilizer',20160//size,
              'base_F2',base,'members_F2',profile)
    assert sum(e[1] for e in orbit_info)==14336
    certify_stabilizer_groups()
    # The two smooth-base orbits: all 8 projective Jacobian ideal charts
    # certify no singular geometric points (unit ideal over algebraic closure).
    for rep in ((192,357),(192,358)):
        proof=groebner_unit_on_each_chart(*rep)
        print('smooth base',rep, 'four ideal bases',proof)
        count4=count_extension_base(*rep,degree=2,irreducible=0b111)
        count8=count_extension_base(*rep,degree=3,irreducible=0b1011)
        assert (count4,count8)==({(192,357):(8,14),
                                 (192,358):(8,4)}[rep])
        print('extensions',rep,'F4',count4,'F8',count8)
    # The remaining orbits have base-point counts 0 or 6; if the base
    # were geometrically smooth, it would be a genus-1 curve, so by Hasse
    # it would have 1..5 rational points. Thus those bases are singular.
    assert {base for rep,sz,base,_ in orbit_info if rep not in ((192,357),(192,358))}=={0,6}
    # Elementary parity of a quadratic in at least 3 parameters gives a
    # zero outside the origin over F2; thus no all-smooth vector space
    # can have dimension >= 3 (apply polar Pfaffian).
    # Verify this parity directly on F2^3 by testing every coefficient tuple.
    for mask in range(1<<6):
        values=[]
        for v in range(1,8):
            a,b,c=tuple((v>>i)&1 for i in range(3))
            values.append((a*((mask>>0)&1)^b*((mask>>1)&1)^c*((mask>>2)&1)
                           ^ a*b*((mask>>3)&1)^a*c*((mask>>4)&1)
                           ^ b*c*((mask>>5)&1)))
        assert 0 in values
    print('BINARY_QUADRIC_PENCIL_SMOOTH_BASE_ORBITS_PASS',len(all_pencils),
          len(orbit_info),5040,5040,10080)

if __name__=='__main__': main()
