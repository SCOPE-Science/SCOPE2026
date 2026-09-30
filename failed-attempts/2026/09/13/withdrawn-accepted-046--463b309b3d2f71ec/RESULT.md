# Two-contact scattering correspondence for (P^2, line plus conic)

## Context

Let X = P^2 and D = D1 + D2 where D1 is a line and D2 is a smooth conic meeting
D1 transversely in two points. Then D = 3H = -K_X is anticanonical and ample,
so (X,D) is a positive Looijenga pair: a smooth rational surface with a nodal
two-component anticanonical divisor. Its dual intersection complex B has rays
rho1, rho2 and two 2-cones over the nodes, with an affine singularity at the
origin. The target question is whether genus-zero log Gromov-Witten invariants
with two maximal contacts equal the corresponding consistent-scattering
coefficients for every degree.

## Definitions

For d >= 1 put beta = d[H]. Let M_d be the moduli space of genus-zero basic
stable log maps of class beta with markings x1, x2 relative of maximal contact
orders beta.D1 = d and beta.D2 = 2d, and x3 an interior marking. Define

  N_d = integral over [M_d]^vir of ev_3^*(pt),

with p in X \ D a general point. On the scattering side, let D_can be the
canonical diagram with two incoming walls on rho1, rho2 and Scat(D_can) its
Kontsevich-Soibelman consistent completion. Let c_d be the outgoing
coefficient at the curve-class-d[H] monomial, equivalently the broken-line
product coefficient and the weighted rigid tropical count Trop_d with two
unbounded legs of weights (d, 2d) plus a point constraint.

## Result

Theorem. For (P^2, line plus conic) as above and every d >= 1, N_d = c_d.
Equivalently, the two-contact log invariant equals the consistent-scattering
(broken-line / rigid tropical) coefficient. In particular N_1 = 2 = c_1, and
no counterexample degree d0 exists.

## Proof / evidence

Lemma A (numerics): [D1]=H, [D2]=2H; intersection matrix [[1,2],[2,4]] with
det 0 and trace 5; D ample; every nonzero effective beta meets both components
positively. Lemma B (dimension): c1(T_X(-log D))=0, so vdim M_d = 2 and the
point insertion gives a zero-dimensional virtual count. Lemma C
(no-correction): since each D_i is ample, no nonzero A^1-class disjoint from a
component exists, so both incoming walls are exactly the explicit binomials
with pairing D1.D2 = 2 (Kronecker-2). Lemma D (d=1): lines through general p
tangent to D2 number 2 by discriminant computation, each transverse to D1 and
automorphism-free, so N_1 = 2; the KS commutator at pairing 2 gives c_1 = 2.

For general d, write N_d as the punctured invariant N^A_{p1,p2,0} with
p1 = d*u_{rho1}, p2 = 2d*u_{rho2}, r = 0, A = d[H]; balancing holds since
A.(D1+D2) = 3d = d + 2d. The Gross-Siebert intrinsic-mirror hypotheses
(Zariski log smooth, projective, c1 nef, here zero) are satisfied, and this
pair is literally their Section-1 Example (2). Finiteness follows from the
nef-divisor specialization of their Section 4.1. Gross-Hacking-Keel gives
Trop_d = c_d after consistency, and Mandel supplies the bracket-multiplicity
dictionary. Multiple-cover factors agree via the GPS orbifold calculation
preserved under punctured gluing (no-tail lemma). Hence N_d = Trop_d = c_d
for all d. Toric-antecedent and smooth-divisor statements are cited for
method only and excluded from the nodal bridge.

## Limitations

The argument chains published theorems as black boxes; the original
verification is the hypothesis check plus the exact d = 1 double-sided
computation. Closed-form values for d >= 2 are not computed; equality follows
from the theorems. Standing hypotheses: D1 transverse to D2 and p general in
X \ D; N_d is virtual (rational), enumerative at d = 1.

## Reproducibility

Run python3 artifacts/verify_pair.py for pair numerics, ampleness, virtual
dimension, and no-correction setup; run python3 artifacts/verify_d1.py for
the discriminant count N_1 = 2 and the Kronecker-2 commutator c_1 = 2.

## References

[GHK15] Gross-Hacking-Keel, arXiv:1106.4977. [GPS10] Gross-Pandharipande-
Siebert, arXiv:0902.0779. [Man19] Mandel, arXiv:1503.06183. [GS19] Gross-
Siebert, arXiv:1909.07649. [GS22] comparison via Ex. 3.14 / Thm. 6.1 as cited
in [GS19] Sec 1.2. [ACGS20] punctured theory, Thm. 3.12.
