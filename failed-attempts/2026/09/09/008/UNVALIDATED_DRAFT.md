# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Box-minimal double lex-non-shape witness among sparse {±1} quadratic pairs in Q[x,y]

## Abstract
We certify an exact, machine-checked boundary fact about lex Gröbner bases of the
sparsest nonlinear bivariate systems. Let **U** be the complete finite box of unordered
pairs {f, g} ⊂ Q[x, y] in which each of f, g has total degree exactly 2, has 2 or 3
nonzero terms, and has all nonzero coefficients in {+1, −1}. Then |U| = 19 900, and
the box-order-least zero-dimensional pair failing lex shape position under **both**
variable orders is

> **P\*** = { f = −y² − y − 1, g = −x² − x − 1 }, indices (0, 60).

Both reduced lex Gröbner bases of P\* equal {x²+x+1, y²+y+1}; neither has the shape
form {topvar − h(other), m(other)}. The ideal is zero-dimensional of quotient
dimension 4, with elimination degrees 2/2, resultant degrees 4/4 (squared
cyclotomic factors), and exactly 4 distinct affine complex zeros (multiplicity sum 4).

## 1. The box

Work in Q[x, y]. Monomials of total degree ≤ 2 are

    x², xy, y², x, y, 1,

of which x², xy, y² are the quadratic ("QUADS") ones. An admissible polynomial has
2 or 3 nonzero terms, at least one quadratic term, and every nonzero coefficient in
{+1, −1}. Supports: C(6,2) − C(3,2) = 12 two-term supports and
C(6,3) − C(3,3) = 19 three-term supports; with 4 resp. 8 signings this gives
12·4 + 19·8 = 48 + 152 = **200** polynomials. Unordered distinct pairs:
C(200, 2) = **19 900**. The enumeration is fixed by sorting on
(support-tuple, coefficient-tuple); under it index 0 is −y²−y−1 and index 60 is
−x²−x−1. The script `artifacts/check_pstar.py` regenerates this list from the
definition and asserts both counts.

## 2. Definitions

Fix lex(x>y) (x larger) and lex(y>x) (y larger). A zero-dimensional ideal I ⊂ Q[x,y]
is in **shape position** for lex(x>y) if its reduced lex Gröbner basis is exactly

    { x − h(y), m(y) }

for some h, m ∈ Q[y] (m monic); and symmetrically { y − h(x), m(x) } for lex(y>x).
Our test is structural on the sympy-computed reduced basis: exactly two polynomials,
exactly one univariate in the small variable, the other monic-linear in the large
variable with a single degree-1 term. Zero-dimensionality is certified jointly by
both Sylvester resultants being nonzero **and** the grevlex leading-term staircase
containing pure powers of both variables (finite quotient, dimension read off the
staircase).

## 3. Theorem (verified minimal double-non-shape witness)

**Claim.** Over the box U above, with the stated ordering:

1. (Box) U has 200 polynomials and 19 900 unordered pairs.
2. (P\* structure) For P\* = {−y²−y−1, −x²−x−1}: the reduced lex(x>y) basis is
   {x²+x+1, y²+y+1} and the reduced lex(y>x) basis is the same set; hence P\*
   fails shape position under **both** orders (each basis has two univariate
   nonlinear polynomials and no x−h(y) resp. y−h(x) element).
3. (Zero-dimensional invariants) ⟨P\*⟩ is zero-dimensional: quotient dimension 4
   (grevlex leading terms {(2,0),(0,2)}); elimination ideals
   ⟨y²+y+1⟩ ∩ Q[y], ⟨x²+x+1⟩ ∩ Q[x] (degrees 2, 2);
   Resₓ(f,g) = y⁴+2y³+3y²+2y+1 = (y²+y+1)² (degree 4),
   Res_y(f,g) = x⁴+2x³+3x²+2x+1 = (x²+x+1)² (degree 4), each divisible by the
   corresponding eliminant; affine variety over C = {(a,b) : a²+a+1 = b²+b+1 = 0},
   4 distinct points, multiplicity sum 4.
4. (Minimality) Every pair preceding (0,60) in box order is either inconsistent
   (GB {1}), positive-dimensional (a resultant vanishes / staircase infinite), or
   in shape position under at least one of the two lex orders. Hence P\* is the
   box-least zero-dimensional double-shape-failing pair.

**Proof — computed.** All four items are discharged by the replay script
`artifacts/check_pstar.py` (sympy 1.12 exact QQ Gröbner/resultant/factorization
plus staircase arithmetic), which prints VERIFY_OK in ~0.2 s and writes
`artifacts/pstar_cert.json` containing the box counts, both P\* bases, and the full
59-row prefix audit (status + shape bits per predecessor). Concretely:

- The recorded predecessor table shows the near-misses explicitly: pairs
  (0,8)–(0,15) are double-shape; (0,16)–(0,23) and (0,44)–(0,51) fail in x>y but
  are shape in y>x (e.g. Gyx = {x⁴+x²+1, y+x²+1}); (0,36)–(0,37), (0,42)–(0,43)
  are the reverse; inconsistent pairs (0,1)–(0,6), (0,24)–(0,27) and the
  positive-dimensional pair (0,7) (f vs. its negation up to sign, resultant zero)
  are excluded from the minimality competition as non-zero-dimensional.
- For P\* the script asserts the exact basis strings, checks monic-linear
  absence structurally, verifies both resultant/eliminant divisibilities, the
  squared factorizations (y²+y+1)² and (x²+x+1)², the staircase dimension 4, and
  the 2×2 root grid symbolically (solve + simplify-substitution).

## 4. Worked detail for P\*

Since f depends only on y and g only on x, the system is decoupled:
V(P\*) = Z(x²+x+1) × Z(y²+y+1). Each factor has the two primitive cube roots
ω, ω² (discriminant −3), so |V| = 4, all simple; quotient dimension 2·2 = 4.
Any reduced lex basis is {x²+x+1, y²+y+1} regardless of variable order, so no
linear element x − h(y) or y − h(x) can appear: double-non-shape is visible by
inspection once the bases are certified. The Sylvester resultants pick up
extraneous squares: Resₓ = (y²+y+1)², Res_y = (x²+x+1)² — a clean illustration of
resultant-versus-eliminant degree inflation (4 vs 2) on sparse inputs.

## 5. Scope, limits, and what is NOT claimed

- Claimed: the box combinatorics, the P\* bases/non-shape verdicts, its
  invariants, and box-least minimality — all replayed by `check_pstar.py`.
- **Not claimed:** the full 19 900-row stratification census. An inherited
  `stratification.csv` exists but its eliminant/resultant columns are corrupted
  (wrong sympy resultant API: tuple-vs-Poly confusion; univariate-extraction
  bugs), and one inherited summary's shape_yx column (identically 0) reflects a
  swapped-variable-call bug — e.g. pair (0,16) is shape in the y>x order, contrary
  to that column. Those files are retained as working notes only and carry no
  evidential weight here.
- Originality: per the lane brief, textbook/algorithmic sources (Cox–Little–O'Shea;
  Lazard; Faugère–Mou; Berthomieu–Neiger–Safey El Din; Demin–Rouillier–Ruiz; Dubé)
  give Shape Lemma theory and solvers but no census or minimal witness over this
  exact {±1} sparse-quadratic box; the checked-in census plus least-witness
  certificate is new as a boundary datum. No generality beyond the box is asserted.

## 6. Reproduction

    python3 output/artifacts/check_pstar.py
    # expect: BOX_OK ... PREFIX_OK ... GXY_OK ... GYX_OK ... ZD_OK ... ELIM_OK ...
    #         VARIETY_OK ... VERIFY_OK (~0.2 s, sympy 1.12)

Artifacts: `output/artifacts/check_pstar.py` (verifier),
`output/artifacts/pstar_cert.json` (box counts, P\* data, 59-row prefix audit).
Prior exploratory scripts and logs in `output/artifacts/` are superseded working
notes, preserved but not relied upon.
