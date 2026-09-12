# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Relative K1 of the tacnode in characteristic 7 vanishes

## 1. Setup and statement

Let k = F_7. Let

  A = (k[x,y]/(y^2 - x^4))_{(x,y)}

be the tacnode local ring, and work with its (x,y)-adic completion
Â = k[[x,y]]/(y^2 - x^4) for the normalization computation; the transfer
Â -> A is handled in Section 5. The normalization map is

  x |-> (u, v),   y |-> (u^2, -v^2),

with B = k[[u]] x k[[v]]. Let I = Ann_B(B/A) = ((Â:A)) be the conductor ideal,
viewed as an ideal of both Â (hence A) and B. The conductor square

      A  --->  B
      |        |
      v        v
     A/I ---> B/IB

is a Milnor square (I is contained in the Jacobson radical, B is integral over
A). By definition, K_1(A,B,I) is the relative term: the homotopy fiber of
K(A,I) -> K(B,IB) for the pair, equivalently the obstruction measured by the
Mayer-Vietoris sequence of the Milnor square. Concretely, with all rings below
commutative semilocal, K_1 = units (Section 3), so K_1(A,B,I) = 0 is equivalent
to: the unit kernel ker(A^x -> B^x) is exactly the standard kernel
ker((A/I)^x -> (B/IB)^x) lifted through the square, and the K_2-cokernel term
from B/IB vanishes.

**Theorem.** K_1(A,B,I) = 0. Equivalently, K_1(A) -> K_1(B) has the standard
unit kernel: every relative unit lifts through the conductor square A/I ->
B/IB, and no matrix in SL_2(A) or unit tuple survives nonzero in the relative
term.

This is branch (A) of the target; branch (B) (a surviving class detected by a
logarithmic-differential invariant) does not occur.

## 2. The conductor square explicitly

The normalization: in k[[u]], set x = u, y = u^2; in k[[v]], set x = v,
y = -v^2. Both satisfy y^2 - x^4 = 0, and since char k = 7 != 2 the two
branches are distinct (u^2 vs -v^2 differ). The subring
Â = {(f(u), g(v)) : f(0) = g(0), f'(0) = g'(0) = 0 in suitable coordinates}
is exactly k[[x,y]]/(y^2-x^4): an element (f,g) lies in Â iff it is a
polynomial in (u,v) resp. (u^2,-v^2) with matching constant terms, and the
tacnode condition forces vanishing linear terms on both branches (a cusp on
each branch, glued transversally in the tangent data). Hence fractional
elements with a lone linear term, e.g. (u, 0) or (0, v), are in Frac(Â) but
not in Â.

Conductor: (u^2, 0) = (x^2+y)/2 and (0,v^2) = (x^2-y)/2 (using 2^{-1} = 4 mod
7), both in Â since x^2 = (u^2,v^2) and y = (u^2,-v^2) are. These are exact
polynomial identities in k[u] x k[v] (verified in
output/artifacts/verify_tacnode_k1.py). Thus

  I = (u^2) x (v^2) = Ann_B(B/Â),

i.e. the conductor is I_Â = (x^2+y, x^2-y)/2 up to the unit 2. Indeed any
B-multiple of (u^2,0),(0,v^2) has vanishing constant and linear terms on each
branch, hence lies in Â; conversely (u,0) is not in Â and u*(u,0) = (u^2,0).

Quotients: B/IB = k[[u]]/(u^2) x k[[v]]/(v^2) =: R x R with
R = k[eps]/(eps^2), eps^2 = 0. For Â/I: Â is spanned mod I by {1, x, y} with
x^2, xy, y^2 all in I (x^2 = (u^2,v^2), xy = (u^3,-v^3), y^2 = (u^4,v^4), all
in (u^2)x(v^2); verified in the script). The map Â -> R x R sends
x |-> (eps, eps), y |-> (0,0), so its image is the diagonal
{(a+b eps, a+b eps)} ≅ R via a+bx |-> (a+b eps, a+b eps). The kernel is exactly
I (x^2, xy, y^2 map to 0 and I maps to 0; dimension count: dim_k Â/I = 2 =
dim_k R). Hence

  Â/I ≅ R,   B/IB ≅ R x R,   and the map is the diagonal d: R -> R x R.

The same holds for A (localization) since I is m-primary: A/I ≅ R.

## 3. K_1 of the corners is units; the unit maps

All four rings A, B, A/I, B/IB are commutative semilocal (A local; B a product
of two locals; quotients Artinian), so Quillen K_1 = units: K_1 = (-)^x.
The maps:

- B^x = k[[u]]^x x k[[v]]^x -> (R^x x R^x): reduction mod (u^2),(v^2), surjective
  with kernel 1 + (u^2)x(v^2).
- (A/I)^x = R^x -> (B/IB)^x = R^x x R^x is the diagonal on units, injective:
  verified by enumeration (|R^x| = 42, |image| = 42) in the script.
- A^x -> B^x: injective, since A subset B are domains' subrings (A is a domain:
  y^2 - x^4 = (y-x^2)(y+x^2) — wait, this factors! See remark below; the map
  is still injective because A -> Â -> B is injective: A -> Â is completion of
  a domain... precisely: k[x,y]/(y^2-x^4) with y^2-x^4 = (y-x^2)(y+x^2) is
  REDUCIBLE. The tacnode y^2 = x^4 is two tangent parabolas. So A is reduced
  with two minimal primes, its total quotient ring is k(x) x k(x'), and
  normalization is the product of the two branch normalizations; A -> B is
  injective. Good — reduced, not a domain, but A -> B injective regardless.)
- 1 + I_A -> 1 + I_B: an element 1 + t with t in I_A maps to (1+f, 1+g) with
  f in (u^2), g in (v^2); the congruence data match because I_A = I_B as
  ideals of B identified with Â... more precisely I as an ideal of B equals
  (u^2)x(v^2), and A/I -> B/IB is the diagonal, so the principal-unit kernels
  agree.

Consequence: ker(A^x -> B^x) injects into ker(R^x -> R^x x R^x) = 1, i.e. is
trivially standard. Explicitly, if a in A^x maps to 1 in B^x then a = 1. So the
unit-kernel part of K_1(A,B,I) is zero: K_1(A) -> K_1(B) is injective on the
nose, and a fortiori the relative term has no unit contribution.

## 4. Vanishing of the K_2 obstruction: K_2(R) = 0

The Mayer-Vietoris sequence of the Milnor square contains

  K_2(B) + K_2(A/I) ---> K_2(B/IB) ---> K_1(A) ---> K_1(B),

so K_1(A) -> K_1(B) injective (hence relative term zero) follows once the map
K_2(B) + K_2(R) -> K_2(R x R) = K_2(R) + K_2(R) is surjective. Since K_2
preserves finite products, it suffices that K_2(R) -> K_2(R) factors are hit,
i.e. it suffices that K_2(R) = 0 (then surjectivity is trivial). We prove
Quillen K_2(R) = 0 for R = F_7[eps]/(eps^2).

Step 1 — Milnor K_2^M(R) = 0, elementarily. R^x ≅ C_6 x C_7:
residue C_6 = F_7^x lifted via Teichmuller, times principal units
1 + (eps) ≅ (F_7,+) ≅ C_7 (since (1+a eps)(1+b eps) = 1+(a+b)eps as eps^2=0).
The script verifies R^x is cyclic of order 42 generated by gamma = 3+3eps
(order exactly 42). Hence R^x tensor R^x ≅ C_42 (generator z tensor z,
z = gamma). Milnor K_2^M(R) = (R^x tensor R^x)/<a tensor (1-a)>. It suffices to
show the Steinberg relations generate the whole C_42, i.e. with s = {z,z},
some integral combination of values v_a = log(a)log(1-a) is coprime to 42.
The script enumerates all 35 pairs (a, 1-a both units) and finds
gcd(values, 42) = 1, with an explicit Bezout witness. Hand-checkable
sub-relations suffice (all verified numerically in the script):

- a = 3 (constant): 1-a = -2 = 5; log(3) = 7 (3 = gamma^7 since gamma^7 =
  3^7(1+eps)^7 = 3·1 = 3 as 3^7 = 3·3^6 = 3 mod 7 and (1+eps)^7 = 1 in char 7);
  log(5): 5 = 3^5, and one computes log(5) = 35. So v = 7·35 = 245 = 35 mod 42:
  35 s = 0.
- a = 4 (constant): 1-a = -3 = 4... wait 1-4 = -3 = 4 mod 7. log(4) = 14
  (4 = 3^2? 3^2 = 9 = 2. Hmm, 4 = 3^4? 3^4 = 81 = 4 mod 7, yes; but the log is
  base gamma, not base 3. The script gives: a=4 relation yields 28 s = 0.)
  From 35 s = 0 and 28 s = 0: 7 s = 0.
- a = 2 + eps: the script gives v = 18, i.e. 18 s = 0. With 7 s = 0 and
  18 s = 0: gcd(7,18) = 1, so s = 0.

Thus every generator dies: K_2^M(R) = 0. The same computation with R replaced
by F_7 gives K_2^M(F_7) = 0 (values [0,5,4,5,0] mod 6; 5t = 0 and 4t = 0 force
t = 0), consistent with Steinberg/Matsumoto for finite fields.

Step 2 — Milnor = Quillen here. R = F_7[eps]/eps^2 is a quotient of the
polynomial ring F_7[t] (hence of a ring with many units / a field with ≥ 6
elements) by a nilpotent ideal, with residue field F_7 of 7 elements > 5.
By Maazen–Stienstra and van der Kallen's stability (K_2^M -> K_2 surjective for
commutative local rings with residue field of > 5 elements; Dennis–Stein
symbols generate), Quillen K_2(R) is generated by Dennis–Stein symbols
<d(a), d(b)> subject to relations that all factor through the Milnor quotient
plus lifts of field relations — all of which vanish by Step 1 and the
vanishing K_2^M(F_7) = 0. In particular the Dennis–Stein–van der Kallen
presentation gives K_2(R) as a quotient of K_2^M(R) = 0. Hence Quillen
K_2(R) = 0. (Equivalently, via Bloch's formula / K\"ahler differentials:
the Dennis–Stein filtration gives gr K_2(R) via Omega^1_{F_7} = 0 and
HH terms killed by 7 vs. the 6-torsion of the residue field; no nonzero
dlog(a)∧dlog(1-a) invariant exists. This is also why branch (B) is impossible:
any putative logarithmic-differential detector on B/IB lands in
Omega^1_{R/F_7} pieces tensored over a base with Omega^1_{F_7} = 0 and
relations forcing zero — there is simply no nonzero invariant to certify a
surviving class.)

Step 3 — finish. K_2(B/IB) = K_2(R) + K_2(R) = 0, so the connecting map to
K_1(A) is zero and ker(K_1(A) -> K_1(B)) = ker((A/I)^x -> (B/IB)^x) = 1.
Hence the relative term K_1(A,B,I), which sits in

  K_2(B/IB) ---> K_1(A,B,I) ---> ker(K_1(A) -> K_1(B)) ⊕ ... = 0,

vanishes. More precisely, in the MV long exact sequence the map into K_1(A) has
zero cokernel contribution and K_1(A) -> K_1(B) is injective, so the fiber term
K_1(A,B,I) = 0.

## 5. Transfer from Â to A

Completion A -> Â is faithfully flat, hence injective on units and on K_1 of
this conductor square (I is m_A-primary, so A/I ≅ Â/IÂ ≅ R; the square for A
and for Â have the same Artinian bottom row). The K_2-vanishing concerns only
the Artinian row R -> R x R, identical in both cases. Hence K_1(A,B_A,I_A) = 0
for the localization A as well. (B is the normalization in both cases up to
completion; the conductor data coincide since I is m-primary.)

## 6. Why branch (B) is impossible (no surviving matrix)

Any class in K_1(A,B,I) would, by Sections 3–4, have to come from K_2(R x R),
which is zero. Concretely: a matrix M in SL_2(A) mapping to elementary
matrices over each branch of B is a Mennicke symbol; its class dies because
the Dennis–Stein relations over R present a trivial group. No choice of unit
tuple or determinant data can evade this: det over A/I is the diagonal unit,
which injects, and SK_1-type terms vanish for these Artinian corners.
The dlog invariant dlog(a)∧dlog(1-a) that would certify non-liftability is
identically zero by the K_2^M(R) = 0 computation. Hence no counterexample
exists; the answer is (A).

## 7. Scope, originality, limitations

Scope: only the named tacnode y^2 = x^4 over F_7 with the given normalization;
not the split transverse node (whose B/IB = F_7 x F_7 has K_2 = 0 for a
different, easier reason, and whose A/I -> B/IB need not be injective on
units — a genuinely different square).

What is proved: full vanishing K_1(A,B,I) = 0, branch (A), with explicit
truncated-polynomial ledger (Section 2 identities, Section 4 Steinberg
computation) reproduced by output/artifacts/verify_tacnode_k1.py.

Limitations / what is not claimed: no computation of higher relative terms
K_i, i ≥ 2 (the MV sequence gives K_2(A,B,I) ≅ ker(K_2(B)+K_2(R)->K_2(R)^2),
uncomputed); no claim in characteristic ≠ 7 or for the cuspidal/cubic tacnode
in characteristic 2 (where 2^{-1} fails and the idempotent computation
changes); the Step-2 identification Milnor = Quillen invokes the published
Maazen–Stienstra / van der Kallen stability theorem rather than reproving it —
the original computational content is the explicit Steinberg generation
(gcd = 1) for R = F_7[eps]/eps^2, which the script checks exactly.

## Reproducibility

Run: python3 output/artifacts/verify_tacnode_k1.py
Expected: conductor identities OK; R^x cyclic C42 (gamma = 3+3eps); K_2^M(F_7)
= 0; K_2^M(R) = 0 over 35 Steinberg pairs with gcd 1; diagonal injective;
writes output/artifacts/ledger.json.
