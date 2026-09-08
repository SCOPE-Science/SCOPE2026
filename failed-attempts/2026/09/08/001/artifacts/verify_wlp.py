#!/usr/bin/env python3
"""Verification script for Lane-52 Weak-Lefschetz defect census.
Exact rational arithmetic only (stdlib Fractions + sympy for cross-check).
Replays: Artinian/socle/HF by monomial complement counting; M_d matrices
for ell=x+y+z; rank via Fraction elimination AND sympy; parametric
determinant (symbols a,b,c) for genericity; kernel/cokernel witnesses;
nonzero maximal minors; second-ell (1,2,3) cross-check; S3-orbit census
counts for family F; stratum labels.

Family F: input tuples (x^a,y^b,z^c,m1,m2) with 3<=a,b,c<=5,
deg(m_i) in {2,3,4}, m_i not in (x^a,y^b,z^c), m1,m2 incomparable.
Distinct minimal ideals with socle 5-6: 579 S3-orbits (3246 counting perms),
6 failing orbits (generic ell-defect). Runs in seconds.
"""
from fractions import Fraction
import itertools, time

try:
    import sympy as sp
    HAS_SYMPY = True
except Exception:
    HAS_SYMPY = False

# ---------- toolkit ----------
def divides(g, m):
    return g[0]<=m[0] and g[1]<=m[1] and g[2]<=m[2]

def in_ideal(m, gens):
    for g in gens:
        if divides(g, m):
            return True
    return False

def mons_deg(d):
    out=[]
    for i in range(d+1):
        for j in range(d+1-i):
            out.append((i,j,d-i-j))
    return out

def bases_socle(gens, Dmax=10):
    bases={d:[m for m in mons_deg(d) if not in_ideal(m, gens)] for d in range(Dmax+1)}
    # Artinian iff pure powers present
    for v in range(3):
        if not any(in_ideal(tuple((e if k==v else 0) for k in range(3)), gens) for e in range(1, Dmax+1)):
            return bases, None
    nonempty=[d for d in range(Dmax+1) if bases[d]]
    if not nonempty:
        return bases, -1
    return bases, max(nonempty)

def mult_matrix(bd, bd1, coeffs=(1,1,1)):
    idx={m:i for i,m in enumerate(bd1)}
    M=[[0]*len(bd) for _ in range(len(bd1))]
    for j,m in enumerate(bd):
        for coeff,dv in zip(coeffs,[(1,0,0),(0,1,0),(0,0,1)]):
            n=(m[0]+dv[0],m[1]+dv[1],m[2]+dv[2])
            if n in idx:
                M[idx[n]][j]+=coeff
    return M

def rank_frac(M):
    if not M or not M[0]:
        return 0
    A=[[Fraction(x) for x in row] for row in M]
    r=len(A); c=len(A[0]); rank=0; row=0
    for col in range(c):
        piv=None
        for i in range(row,r):
            if A[i][col]!=0:
                piv=i; break
        if piv is None:
            continue
        A[row],A[piv]=A[piv],A[row]
        pv=A[row][col]
        for i in range(row+1,r):
            if A[i][col]!=0:
                f=A[i][col]/pv
                for k in range(col,c):
                    A[i][k]-=f*A[row][k]
        row+=1; rank+=1
    return rank

def fmt(gens):
    def f(m):
        s=""
        for v,n in zip("xyz",m):
            if n==0: continue
            elif n==1: s+=v
            else: s+=f"{v}^{n}"
        return s or "1"
    return "("+", ".join(f(m) for m in gens)+")"

def canon(gens):
    return min(tuple(sorted([(g[p[0]],g[p[1]],g[p[2]]) for g in gens])) for p in itertools.permutations([0,1,2]))

# 6 failing S3-canonical ideals (socle 6), minimal 5-generated
FAILS = [
    [(0,0,3),(0,1,1),(0,4,0),(1,0,1),(4,0,0)],
    [(0,0,3),(0,1,1),(0,4,0),(1,0,2),(4,0,0)],
    [(0,0,3),(0,1,1),(0,4,0),(2,0,1),(4,0,0)],
    [(0,0,3),(0,1,2),(0,3,0),(1,0,2),(4,0,0)],
    [(0,0,3),(0,4,0),(1,2,1),(3,1,0),(5,0,0)],
    [(0,0,4),(0,2,2),(0,4,0),(2,1,1),(4,0,0)],
]
EXPECTED_HF = [
    [1,3,4,4,3,2,1],
    [1,3,5,5,4,2,1],
    [1,3,5,5,3,2,1],
    [1,3,6,6,5,3,1],
    [1,3,6,9,9,5,1],
    [1,3,6,10,10,6,2],
]
EXPECTED_BAD = [(2,3,4),(2,4,5),(2,4,5),(2,5,6),(3,8,9),(3,9,10)]

def check_one(idx, gens, exp_hf, exp_bad):
    print(f"\n--- Failing stratum F{idx+1}: {fmt(gens)} ---")
    gens=sorted(gens)
    # Artinian: pure powers
    for v,nm in enumerate("xyz"):
        e=[g[v] for g in gens if g[(v+1)%3]==0 and g[(v+2)%3]==0]
        assert e, f"missing pure power {nm}"
    print(f"  Artinian: pure powers present {[g for g in gens if sum(1 for x in g if x>0)==1]}")
    bases,socle=bases_socle(gens,10)
    assert socle==6, f"socle {socle} !=6"
    hf=[len(bases[d]) for d in range(socle+1)]
    print(f"  socle degree (monomial complement max): {socle}")
    print(f"  Hilbert vector: {hf}  expected {exp_hf}")
    assert hf==exp_hf, "HF mismatch"
    # socle distribution (type)
    soc={}
    for d in range(socle+1):
        s=[m for m in bases[d] if all(in_ideal((m[0]+dv[0],m[1]+dv[1],m[2]+dv[2]),gens) for dv in [(1,0,0),(0,1,0),(0,0,1)])]
        if s: soc[d]=s
    print(f"  socle distribution: {soc} (type {sum(len(v) for v in soc.values())})")
    # rank profile ell=(1,1,1), two methods
    for d in range(socle):
        M=mult_matrix(bases[d],bases[d+1],(1,1,1))
        r1=rank_frac(M)
        r2=sp.Matrix(M).rank() if HAS_SYMPY and M and M[0] else r1
        exp=min(len(bases[d]),len(bases[d+1]))
        mark="FAIL" if r1<exp else "pass"
        print(f"  d={d}: size {len(M)}x{len(M[0]) if M else 0} rank_frac={r1} rank_sympy={r2} expected={exp} [{mark}]")
        assert r1==r2, "rank methods disagree"
    # failing degree details
    d0,exp_rk,exp_max=exp_bad
    # exp_bad stored as (d, rank, expected); retrieve
    M=mult_matrix(bases[d0],bases[d0+1],(1,1,1))
    Ms=sp.Matrix(M)
    det=Ms.det()
    print(f"  failing d={d0}: bases_d={bases[d0]}")
    print(f"  failing d={d0}: bases_d+1={bases[d0+1]}")
    print(f"  failing M (rows=A_d+1, cols=A_d): {M}")
    print(f"  failing d={d0}: det(M)={det} (expected 0)")
    assert det==0, "failing determinant not zero"
    # nonzero (rank x rank) minor proving rank exactly exp_rk
    from itertools import combinations
    found=None
    for rs in combinations(range(len(M)),exp_rk):
        for cs in combinations(range(len(M[0])),exp_rk):
            v=Ms.extract(rs,cs).det()
            if v!=0:
                found=(rs,cs,int(v)); break
        if found: break
    print(f"  nonzero {exp_rk}-minor at rows{found[0]} cols{found[1]} = {found[2]} (proves rank exactly {exp_rk})")
    assert found is not None
    # kernel / cokernel witnesses (exact)
    ns=Ms.nullspace()
    lns=Ms.T.nullspace()
    assert len(ns)==1 and len(lns)==1, "nullity should be 1"
    kv=list(ns[0]); wv=list(lns[0])
    print(f"  kernel vec v ({len(kv)}): {kv}; M*v={list(Ms*ns[0])}")
    print(f"  cokernel vec w: {wv}; wT*M={list((lns[0].T*Ms))}")
    assert all(x==0 for x in list(Ms*ns[0]))
    # Hessian/dual: contraction matrix H = M^T (Macaulay dual, no coefficients)
    H=Ms.T
    print(f"  Macaulay-dual contraction matrix H=M^T size {H.rows}x{H.cols}, det(H)={H.det() if H.rows==H.cols else 'n/a (rect)'}; rank(H)={H.rank()} (equals rank M)")
    assert H.rank()==exp_rk
    # parametric genericity: det over QQ[a,b,c] identically zero
    a,b,c=sp.symbols('a b c')
    idx1={m:i for i,m in enumerate(bases[d0+1])}
    Mp=[[sp.Integer(0)]*len(bases[d0]) for _ in range(len(bases[d0+1]))]
    for j,m in enumerate(bases[d0]):
        for coeff,dv in zip((a,b,c),[(1,0,0),(0,1,0),(0,0,1)]):
            n=(m[0]+dv[0],m[1]+dv[1],m[2]+dv[2])
            if n in idx1:
                Mp[idx1[n]][j]=Mp[idx1[n]][j]+coeff
    pdet=sp.expand(sp.Matrix(Mp).det())
    print(f"  parametric det M(a,b,c) identically zero? {pdet==0}")
    assert pdet==0, "not a generic failure"
    # second ell (1,2,3) still fails
    M2=mult_matrix(bases[d0],bases[d0+1],(1,2,3))
    r2=rank_frac(M2)
    print(f"  second ell (1,2,3): rank={r2} vs {exp_max} [{'FAIL (generic)' if r2<exp_max else 'PASSES - ell-specific!'}]")
    assert r2<exp_max
    # stratum label: S3-canonical (complete invariant for orbit)
    print(f"  S3-canonical label: {fmt([tuple(g) for g in canon(gens)])}")
    assert tuple(sorted(gens))==canon(gens), "not canonical?"
    print("  OK")

def census_check():
    print("\n=== Full family-F census re-enumeration ===")
    mons=[]
    for d in (2,3,4):
        mons.extend(mons_deg(d))
    orbits={}; nperm=0; t0=time.time()
    for a in (3,4,5):
        for b in (3,4,5):
            for c in (3,4,5):
                base=[(a,0,0),(0,b,0),(0,0,c)]
                for i in range(len(mons)):
                    for j in range(i+1,len(mons)):
                        m1,m2=mons[i],mons[j]
                        if in_ideal(m1,base) or in_ideal(m2,base): continue
                        if divides(m1,m2) or divides(m2,m1): continue
                        gens=sorted(set(base+[m1,m2]))
                        bases,socle=bases_socle(gens,10)
                        if socle not in (5,6): continue
                        hf=tuple(len(bases[d]) for d in range(socle+1))
                        bad=tuple((d,rank_frac(mult_matrix(bases[d],bases[d+1],(1,1,1))),min(len(bases[d]),len(bases[d+1]))) for d in range(socle) if rank_frac(mult_matrix(bases[d],bases[d+1],(1,1,1)))<min(len(bases[d]),len(bases[d+1])))
                        # note: recompute M twice for clarity; fast enough
                        key=canon(gens)
                        if key not in orbits:
                            orbits[key]={"socle":socle,"hf":hf,"fail":len(bad)>0,"count":0}
                        orbits[key]["count"]+=1
                        nperm+=1
    fails={k:v for k,v in orbits.items() if v["fail"]}
    print(f"  distinct S3-orbits with socle 5-6: {len(orbits)} (expected 579)")
    print(f"  counting perms: {nperm} (expected 3246)")
    print(f"  failing orbits: {len(fails)} (expected 6)")
    assert len(orbits)==579 and nperm==3246 and len(fails)==6, "census counts mismatch"
    # check failing canonicals match hardcoded list
    for g in FAILS:
        assert canon(sorted(g))==tuple(sorted(g)), "hardcoded fail not canonical"
        assert tuple(sorted(g)) in orbits and orbits[tuple(sorted(g))]["fail"], "hardcoded fail missing"
    print(f"  census re-enumeration time {time.time()-t0:.1f}s: OK")

def main():
    print("Lane-52 verify_wlp.py: exact QQ replay. sympy present:",HAS_SYMPY)
    assert HAS_SYMPY, "sympy required for cross-check"
    t0=time.time()
    for i,(g,hf,bad) in enumerate(zip(FAILS,EXPECTED_HF,EXPECTED_BAD)):
        check_one(i,g,hf,(bad[0],bad[1],bad[2]))
    census_check()
    print(f"\nALL CHECKS PASSED in {time.time()-t0:.1f}s")

if __name__=="__main__":
    main()
