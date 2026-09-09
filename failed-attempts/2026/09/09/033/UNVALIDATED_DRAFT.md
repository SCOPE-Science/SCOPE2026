# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Height-equidistribution exclusion of the strictly preperiodic portrait (2,1) for cubic unicritical polynomials over quadratic fields

## Theorem
Let f_c(z) = z^3 + c. There is no parameter c in any number field K with
[K:Q] ≤ 2 for which the critical point 0 has exact preperiodic type
(m,n) = (2,1) (tail length 2, period 1). Equivalently, the Misiurewicz
equation G_{3,2,1}(c) = 0 has no root of degree ≤ 2 over Q.

## Proof
Write a_0 = 0 and a_{k+1} = f_c(a_k), so
- a_1 = c,
- a_2 = c^3 + c,
- a_3 = (c^3 + c)^3 + c.

Exact type (2,1) means a_3 = a_2 with a_0, a_1, a_2 pairwise distinct
(tail 0 → a_1 → a_2, then a_2 fixed).

The equation a_3 − a_2 = 0 is computed directly. Since
(a^3)^expansion (c^3+c)^3 = c^9 + 3c^7 + 3c^5 + c^3, we get
a_3 − a_2 = c^9 + 3c^7 + 3c^5 + c^3 + c − (c^3 + c)
= c^9 + 3c^7 + 3c^5
= c^5 · (c^4 + 3c^2 + 3).

Define the primitive factor G_{3,2,1}(c) = c^4 + 3c^2 + 3.

Lemma 1 (exactness). The exact-(2,1) parameters are precisely the roots
of G_{3,2,1}.
Indeed, c = 0 gives a_1 = 0 (type (0,1)), excluded. For c ≠ 0,
a_3 = a_2 holds iff G_{3,2,1}(c) = 0. If G_{3,2,1}(c) = 0 then:
a_1 = c ≠ 0 (as G(0) = 3 ≠ 0); a_2 − a_1 = c^3 ≠ 0;
a_2 = c(c^2+1) ≠ 0, since c ≠ 0 and c^2 ≠ −1 (if c^2 = −1 then
G = 1 − 3 + 3 = 1 ≠ 0; equivalently gcd(G, c^2+1) = 1).
Hence a_0, a_1, a_2 are distinct and a_3 = a_2, i.e. exact type (2,1).
The converse is immediate.

Lemma 2 (irreducibility). G_{3,2,1} is irreducible over Q.
By Eisenstein at p = 3: the non-leading coefficients (0, 3, 0, 3) are
all divisible by 3 while the constant 3 is not divisible by 9.
Hence every root c has [Q(c):Q] = 4.

Conclusion. If c ∈ K with [K:Q] ≤ 2, its minimal polynomial over Q has
degree ≤ 2 and would divide G_{3,2,1}, contradicting irreducibility.
So no such c has exact type (2,1). ∎

## Remarks on route and originality
- The audit plan envisioned a Call–Silverman/Ingram height inequality plus
  a Galois check. Step 1 (factorization) already closes the claim
  elementarily, so no height bound is invoked and none is claimed.
- Computed verification (sympy factor, irreducibility certificate,
  gcd exactness checks, discriminant 432, 50-digit numeric orbit replay)
  is in `artifacts/verify_G321.py` (prints VERIFY_OK).
- Originality scope: the proof itself is elementary algebra; the claimed
  novelty is only the explicitly recorded verdict for the named cell
  (d,m,n) = (3,2,1) over degree ≤ 2, for which the admission triage found
  no prior unconditional record (nearest results conditional, quadratic-only,
  qualitative, or periodic-critical). No claim is made about other cells or
  about the full Morton–Silverman program.
