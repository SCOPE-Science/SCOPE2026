# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Certified Weil data, bad set, and trivial rational torsion for the
general-model genus-2 curve C3 (emergent finding)

## Claim
Let

- C3: y^2 + (x^2+x)y = x^5 - x^4 - 2x^3 + 2x + 1 over Q,
- h(x) = x^2+x, g(x) = x^5-x^4-2x^3+2x+1,
- Y = 2y + h(x), F(x) = 4g(x) + h(x)^2 = 4x^5-3x^4-6x^3+x^2+8x+4.

Then:

1. **Discriminant / bad set (integer-certified).** The Sylvester resultant
   Res(F,F') = 359892992, so disc(F) = Res/4 = 89973248 = 2^9 · 17 · 10337
   (computed by exact integer Bareiss elimination and certified by trial-division
   factorisation). Every bad prime of the odd-degree model lies in {2, 17, 10337};
   in particular 5, 7, 11, 13 are good (disc is nonzero mod each).
2. **Residue portrait at 7 (two independent legs).** The affine F7-points are
   x=0:{y=1,6}, x=1:{y=2,3}, x=2:{y=4}, x=3:{y=3,6}, x=4:{y=4},
   x=5:{y=0,5}, x=6:{} — 10 affine points plus the point at infinity, so
   #C3(F7) = 11; independently #C3(F49) = 61, counted both on the general
   h(x)-model and on Y^2 = F(x), in agreement.
3. **Weil data / Jacobian orders.**
   (N1, N2, trace a, coeff b, #J(Fp)):
   - p=5:  (9, 33, −3, 8, 52),
   - p=7:  (11, 61, −3, 10, 84),
   - p=11: (12, 154, 0, 16, 138),
   - p=13: (11, 171, 3, 5, 133).
   In particular the genus-2 Weil polynomial at 7 is
   P_7(T) = 1 + 3T + 10T^2 + 21T^3 + 49T^4 with #J(F7) = 84.
4. **Trivial rational torsion.** J(Q)_tors = 1. Proof: reduction at a good prime
   q is injective on prime-to-q torsion, and gcd(84, 138, 133) = 1, with the
   residual prime divisors killed one by one — the 7-part via q=11
   (7 ∤ 138), the 11-part via q=7 (11 ∤ 84), the 13-part via q=7
   (13 ∤ 84), and the 2- and 3-parts via q=13 (2, 3 ∤ 133).
5. **Galois signatures (stdlib distinct-degree factorisation).** F mod 3 has
   type (2,3); mod 11 type (1,4); mod 13 irreducible (type (5)); mod 67 type
   (1,1,1,2) with roots {15, 28, 57}. Hence Gal(F/Q) contains a 5-cycle and a
   product of a disjoint 2-cycle and 3-cycle.

## Evidence (exact, replayable)
`python3 output/artifacts/verify.py` prints `VERIFY_OK` (stdlib only). It
recomputes the integer resultant by Bareiss elimination, factorises the
discriminant by trial division, counts #C3(F7) and #C3(F49) on both models,
counts the completed-square model over F25, F121, F169, derives all four Weil
rows, checks the F7 residue table entry by entry, runs the torsion lock
(including the gcd and coprimality checks), and runs exact Fp polynomial
arithmetic (distinct-degree factorisation) for the four signature moduli plus
the mod-13/mod-67 root witnesses.

## Method note (auditable derivation)
- disc(F) = Res(F,F')/lead (degree 5, sign +1): 9×9 Sylvester matrix from the
  exact integer coefficients, Bareiss fraction-free determinant = 359892992,
  divided by 4 gives 89973248; trial division to √n certifies 2^9·17·10337.
- Good reduction at p: p ∤ disc(F) for the odd-degree Weierstrass model.
- N1 by brute-force affine enumeration plus the unique point at infinity.
- N2 by arithmetic in F_{p²} = Fp[t]/(t²+1) (when −1 is a non-residue) or
  Fp[t]/(t²+2) otherwise, with Euler-criterion square test v^((q−1)/2) = 1.
- Weil identities for genus 2: N1 = p+1−a; N2 = p²+1−(a²−2b); #J(Fp) = P(1).
- Torsion via the standard reduction-injectivity argument above.

## What is NOT claimed
- No claim about C3(Q), the Jacobian rank, any Coleman integral, or any sieve
  elimination. The target three-point census remains open.
- The Galois constraint is stated only as element signatures, not as a
  determination of Gal(F/Q).

## Use for future work
Any future Coleman-plus-sieve attack on C3 must reproduce the four Weil rows
(especially trace −3 and #J(F7) = 84); the logged residue table fixes the 11
Chabauty disks; the discriminant fixes the bad set; J(Q)_tors = 1 removes the
torsion ambiguity from any future Mordell–Weil sieve setup.

## Limitations
- Bounded rational search (|a| ≤ 1000, b ≤ 500) found only x = 0; evidence only.
- No statement about C3(Q) or rank is made.
