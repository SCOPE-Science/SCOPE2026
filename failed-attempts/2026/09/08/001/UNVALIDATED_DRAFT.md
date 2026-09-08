# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Weak-Lefschetz defect census for Artinian monomial quotients
# QQ[x,y,z]/I of socle degree 5--6 in a 5-generated box:
# 579 S3-orbits, 6 generic failing strata with Hessian witnesses

## Abstract
We give a complete, exactly replayable Weak-Lefschetz census for one finite
box of Artinian monomial algebras `A=QQ[x,y,z]/I` with socle degree 5 or 6.
Let `F` be the set of input tuples `(x^a,y^b,z^c,m1,m2)` with
`3<=a,b,c<=5`, `deg(m_i) in {2,3,4}`, `m_i` outside `(x^a,y^b,z^c)` and
`m1,m2` incomparable, reduced to distinct minimal ideals.
Re-enumeration gives **579 distinct S3-orbits** (3246 counting permutations)
with socle 5--6. For `ell=x+y+z`, **573 orbits have maximal rank** at every
`A_d -> A_{d+1}` and **6 orbits fail** at one square degree, with
`det M_d(1,1,1)=0` while maximal rank requires nonzero, nonzero
`(n-1)`-minor proving rank exactly `n-1`, explicit kernel/cokernel vectors,
Macaulay-dual contraction witness `H=M^T`, identically-zero parametric
determinant `det M_d(a,b,c) == 0`, and persistence for `ell=(1,2,3)`.
All 6 failures have socle degree 6. Five fail at `d=2`, one (equigenerated)
fails at `d=3` without early socle. All Hilbert vectors are unimodal.
A supplementary 4-generated box `(x^a,y^b,z^c,m)`, `3<=a,b,c<=7`,
`deg<=6`, gives 56 S3-orbits with socle 5--6 and **zero failures**.
Verification is one stdlib+sympy script running in ~1 s; no floating point.

This is a **bounded defect table**, not a census of all socle 5--6 monomial
ideals (which is far larger). Individual failing ideals are small and we do
not claim each ideal is new to mathematics; the new citable content is the
closed-box S3-orbit table with genericity certificates and Hilbert vectors.

## 1. Setup
`R=QQ[x,y,z]`, `I` monomial Artinian iff `x^a,y^b,z^c in I` for some
`a,b,c`. Monomial QQ-basis of `A_d` = `{monomials degree d outside I}`
by direct divisibility test. Socle degree = max degree outside `I`.
Hilbert vector `HF=(h_0,...,h_e)`, `h_d=|basis_d|`.
For `ell=x+y+z`, `M_d` is `h_{d+1} x h_d` with `(M_d)_{n',n}=1` if
`n'=n+e_x` or `n+e_y` or `n+e_z` and both outside `I`, else 0.
Maximal rank is `min(h_d,h_{d+1})`. Rank over QQ is computed twice:
exact `Fraction` elimination and `sympy.Matrix.rank()`; 18351 maps agree.
For genericity write `ell=ax+by+cz`; `M_d(a,b,c)` has linear entries.
If some maximal minor is a nonzero polynomial, general `ell` has full rank.
If `det M_d(a,b,c)` is identically zero (square case) then every `ell`
drops rank: a true WLP failure, not a bad choice of `(1,1,1)`.
We prove the latter with `sympy` expansion for each failing stratum and
cross-check ranks at `(1,1,1),(1,2,3),(2,3,5),(1,5,9),(3,5,7)`.

Macaulay-dual witness. Use contraction action without coefficients:
dual basis `X^iY^jZ^k` for each monomial outside `I`,
`x o X^aY^bZ^c = X^{a-1}Y^bZ^c` if `a>0` else 0, etc.
Then `ell^perp: E_{d+1} -> E_d` has matrix `H_d = M_d^T` (0/1 entries).
Hence `rank H_d = rank M_d`; vanishing of `det H_d` certifies the same
drop. We call `H_d` the Hessian/contraction witness. It is exact over ZZ.
For non-square passing maps the same transpose relation holds.

Stratum label. Minimal generators always form an antichain, so abstract
divisibility posets are trivial here; we stratify by **S3-orbits of minimal
exponent sets** (complete invariant: S3-canonical tuple), which refines
poset isomorphism and records incidence (e.g. whether a `(2,1,1)`-type
mixed squares a variable inside or outside the support of a `(2,2,0)`-type
mixed). Canonical tuples are listed; verifier checks canonicity.

## 2. Family F and main theorem
**Definition (box F).** All tuples `(x^a,y^b,z^c,m1,m2)` with
`3<=a,b,c<=5`, `m_i` monomials of degree 2--4, `m_i` not in
`(x^a,y^b,z^c)`, neither `m1|m2` nor `m2|m1`. Reduce each tuple to its
minimal generating set; keep distinct ideals with socle 5 or 6.
S3-orbits under permuting variables give strata.

**Theorem (computed census, exact).**
*Enumeration of F yields 6975 admissible tuples, 3246 with socle 5--6
counting permutations, forming 579 distinct S3-orbits.*
*For `ell=x+y+z`: 573 orbits have `rank M_d = min(h_d,h_{d+1})` for all `d`
(pass, WLP holds witnessed by this `ell`); 6 orbits fail at exactly one
square degree with rank `n-1` vs `n`.*
*All 6 failures have socle 6, square failing matrices
(4x4 once, 5x5 twice, 6x6 once, 9x9 once, 10x10 once),
`det=0`, nonzero `(n-1)`-minor, 1-dim kernel/cokernel,
`det M_d(a,b,c) == 0` identically, and failure persists for
`ell=x+2y+3z`.*

Table of failing S3-canonical strata (all 5-minimal, all unimodal HF):

| ID | canonical I (S3-min) | HF | fail d: rank vs exp | socle dist (type) | mechanism |
|----|----------------------|----|---------------------|-------------------|-----------|
| F1 | (x^4,y^4,z^3,xz,yz) | [1,3,4,4,3,2,1] | d2: 3 vs 4 | deg2:{z^2}, deg6:{x^3y^3} (type 2) | early socle z^2 kills column |
| F2 | (x^4,y^4,z^3,xz^2,yz) | [1,3,5,5,4,2,1] | d2: 4 vs 5 | deg2:{z^2}, deg4:{x^3z}, deg6:{x^3y^3} (type 3) | early socle z^2 |
| F3 | (x^4,y^4,z^3,x^2z,yz) | [1,3,5,5,3,2,1] | d2: 4 vs 5 | deg3:{xz^2}, deg6:{x^3y^3} (type 2) | nontrivial 5x5, no deg-2 socle |
| F4 | (x^4,y^3,z^3,xz^2,yz^2) | [1,3,6,6,5,3,1] | d2: 5 vs 6 | deg2:{z^2}, deg6:{x^3y^2z} (type 2) | early socle z^2 |
| F5 | (x^5,y^4,z^3,x^3y,xy^2z) | [1,3,6,9,9,5,1] | d3: 8 vs 9 | deg5:{y^3z^2,x^2yz^2,x^2y^3}, deg6:{x^4z^2} (type 4) | no socle <=3, Laplace |
| F6 | (x^4,y^4,z^4,y^2z^2,x^2yz) | [1,3,6,10,10,6,2] | d3: 9 vs 10 | deg5:{xyz^3,xy^3z}, deg6:{x^3z^3,x^3y^3} (type 4) | no socle <=4, Laplace; equigenerated deg 4 |

Counts: F1 orbit has 3 perms, F6 has 3 perms, others 6 perms (total 30
failing ideals counting perms). Full 579-orbit table with HF and rank
profiles is `artifacts/census_orbits.json`.

**Lemma (4-generated box, negative).** All `(x^a,y^b,z^c,m)` with
`3<=a,b,c<=7`, `deg(m)<=6`, `m` outside pure ideal, socle 5--6: 239 ideals
(56 S3-orbits, socle 5:16 orbits, socle 6:40 orbits), zero failures for
`ell=x+y+z`. Hence in this range failure requires >=5 minimal generators.

*Proof status.* Both statements are finite exact computations: monomial
complement counting for HF/socle, integer matrices, exact ranks by two
algorithms, symbolic determinants. See Sec.5 for replay. No floating point,
no Gr\"obner bases needed for monomial ideals.

## 3. Flagship witness F6 (nontrivial equigenerated failure)
`I6=(x^4,y^4,z^4,y^2z^2,x^2yz)`, all five generators degree 4,
Artinian via `(4,4,4)`, socle 6, colength 38,
`HF=[1,3,6,10,10,6,2]`, unimodal, type 4 with socle only in degrees 5,6,
so failure at `d=3` is not a zero column/row.

Bases:
`A3=[z^3,y z^2,y^2z,y^3,xz^2,xyz,xy^2,x^2z,x^2y,x^3]` (10),
`A4=[yz^3,y^3z,xz^3,xyz^2,xy^2z,xy^3,x^2z^2,x^2y^2,x^3z,x^3y]` (10).

`M_3` for `ell=x+y+z` (rows A4 order above, cols A3 order above):
```
[1,1,0,0,0,0,0,0,0,0]
[0,0,1,1,0,0,0,0,0,0]
[1,0,0,0,1,0,0,0,0,0]
[0,1,0,0,1,1,0,0,0,0]
[0,0,1,0,0,1,1,0,0,0]
[0,0,0,1,0,0,1,0,0,0]
[0,0,0,0,1,0,0,1,0,0]
[0,0,0,0,0,0,1,0,1,0]
[0,0,0,0,0,0,0,1,0,1]
[0,0,0,0,0,0,0,0,1,1]
```
Exact `det=0` (both Fraction elimination rank 9 and `sympy` rank 9 vs 10).
Leading 9x9 principal minor (delete last row/col) `=-2 !=0`, so rank
exactly 9. Kernel vector (domain A3):
`v=[-1,1,1,-1,1,-2,1,-1,-1,1]^T`, `M_3 v=0`, i.e. Laplace equation
`-z^3+yz^2+y^2z-y^3+xz^2-2xyz+xy^2-x^2z-x^2y+x^3` is killed by `x+y+z`
in `A4`. Cokernel vector:
`w=[1/2,-1/2,-1/2,-1/2,1/2,1/2,1,-1,-1,1]^T`, `w^T M_3=0`.
Dual `H_3=M_3^T`, `det H_3=0`, `rank 9`.
Parametric `M_3(a,b,c)` (replace 1s by `a,b,c` per `x,y,z` steps) has
`det == 0` as a polynomial (sympy expansion gives 0), and ranks at
`(1,2,3),(2,3,5),(1,5,9),(3,5,7)` are all 9 vs 10. Hence generic WLP
failure, not an artifact of `(1,1,1)`.
Other degrees pass with nonzero maximal minors, e.g.
d0:1, d1: `det[[rows 0,1,3],[cols 0,1,2]]=1`,
d2: 6-minor `=1`, d4: 6-minor `=1`, d5: 2-minor `=1` (indices in verify log).

Up to S3 this is `(x^4,y^4,z^4,x^2y^2,xyz^2)`; the orbit has 3 perms.
It is a degree-4 equigenerated analogue of the Togliatti cubic
`(x^3,y^3,z^3,xyz)` (socle 4, `h=[1,3,6,6,3]`, d2:5 vs 6), lifted to
socle 6 with 5 generators.

## 4. Other failing strata (summary)
Full matrices, minors, kernel vectors for F1--F5 are in the verify log;
we highlight mechanisms to avoid overclaiming a single geometry.

* F1 (4x4): `M_2=[[0,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]`, `det 0`,
  3-minor `rows(0,1,2),cols(1,2,3)=1`, `ker=[1,0,0,0]` = class of `z^2`
  (socle in degree 2: `z^2 x,z^2 y,z^2 z in I`). Column zero
  parametrically. Trivial early-socle failure, but still generic and
  unimodal HF. Same for F2 (`ker=[1,0,0,0,0]`, socle `z^2`) and F4
  (`ker=[1,0,0,0,0,0]`, socle `z^2`).
* F3 (5x5): `M_2=[[0,1,0,0,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,0,1]]`,
  `det 0`, 4-minor `-1`, `ker=[-1,0,1,0,0]`. No socle in degree 2
  (socle in 3 and 6); failure mixes `z^2` and `xz` classes. Nontrivial
  despite small size.
* F5 (9x9, d3): bases in verify log; `det 0`, 8-minor `-2`,
  `ker=[1,-1,1,0,-1,-1,0,1,0]`, no socle `<=3`. Laplace-type, like F6,
  with pure powers `(5,4,3)`.

Thus 3/6 fails are early-socle (column-zero) and 3/6 are Laplace-type
without low socle. We separate the two; only F5,F6 (and F3) are
Togliatti-like in the sense of no explaining socle element.

## 5. Comparison to known families
* Cook--Nagel: level monomial almost complete intersections in 3 vars have
  WLP. Our F1--F6 are 5-generated (not ACI) and non-level (type 2--4), so
  outside that theorem; they appear as failing subtables, as expected.
* Equigenerated/Togliatti: the cubic `(x^3,y^3,z^3,xyz)` is equigenerated
  and fails; our F6 shows equigenerated failure persists at socle 6 with
  5 generators, while our 4-generated lemma shows 4 generators never fail
  in the surveyed pure-power range. This bounds the Togliatti threshold.
* Nagel--Petrovic random monomial algebras: high-probability WLP except
  one regime. Our exhaustive box replaces sampling: 573/579 pass (~99%),
  consistent with high-probability positivity, with explicit failing 1%.
* Almeida et al. higher Hessians/SLP geometry: we use Hessians only as
  concrete contraction matrices `H=M^T` with evaluated minors, not as a
  general geometric equivalence. For square failures `det H=0` vs required
  nonzero is the auditable drop.

No retrieved source gives an S3-orbit table for this box with parametric
genericity proofs; the delta is the bounded exhaustive format.

## 6. Limitations, uncertainty, and what is NOT claimed
* Box-restricted, not full socle 5--6. Outside `3<=a,b,c<=5`, `deg<=4`
  there are many more monomial ideals with socle 5--6 (e.g. with pure
  exponent 6+ or degree-5 extras); we make no claim there. The 579 orbits
  are complete only for minimal reductions of F-tuples.
* `ell` fixed to `x+y+z` for the census; genericity is proved
  a posteriori per failing stratum by `det(a,b,c)==0` + second-ell check.
  For passing strata, `x+y+z` being maximal implies WLP (existence), so no
  extra genericity needed.
* S3-orbits vs abstract divisor-poset isomorphism: all F ideals with 5
  minimals are 5-antichains as abstract posets; S3-type is strictly finer
  and is the auditable label. We do not claim distinct abstract poset
  types for the 6 fails.
* Originality: small failing ideals may coincide with known examples in
  unpublished notes/code; we claim only the closed-box table + genericity
  certificates as new reference material, subject to literature-check
  limits.
* No conjecture is needed; all rank claims are proved by exact arithmetic.
  Uncertainty is limited to completeness outside the box and to
  bibliographic novelty.

## 7. Reproducibility
Run `python3 artifacts/verify_wlp.py` (requires `sympy`, stdlib else).
It re-derives bases by monomial complement, Artinian pure powers, socle,
HF, rebuilds every `M_d` for `ell=x+y+z`, recomputes ranks by `Fraction`
elimination and `sympy`, evaluates failing determinants/minors/kernel
vectors, dual ranks, parametric determinants, second-ell ranks, S3 labels,
and re-enumerates F (579/3246/6) in ~1 s on a laptop. Full orbit table is
`artifacts/census_orbits.json` (canon, socle, HF, rank profile, fail flag,
perm count). No floating point, no external CAS.

## References
* Cook--Nagel, The weak Lefschetz property, monomial ideals, and lozenges,
  https://arxiv.org/abs/0909.3509
* Nagel--Petrovic, Weak Lefschetz and unimodality of random monomial
  algebras, https://arxiv.org/abs/2402.17618
* Almeida et al., On higher Jacobians, Laplace equations and Lefschetz
  properties, https://arxiv.org/abs/2311.02178
* Altafi--Boij, equigenerated monomial ideals/WLP via Togliatti
  (J. Algebra 556 (2020)), https://doi.org/10.1016/j.jalgebra.2020.02.020
