# Integral points on C0: y^2 = x^6 + 3x^4 − 5x^2 + 7: emptiness and denominator lemma

## Context

Target investigation: determine the integral-point set of the even-sextic
bielliptic genus-2 curve C0: y^2 = f(x), f(x) = x^6 + 3x^4 − 5x^2 + 7, via
quadratic Chabauty at one good ordinary prime plus Mordell–Weil sieve.
During the Step-1-style local-solubility check, evaluation of f mod 4 showed
C0 is everywhere locally insoluble at 2, mooting the Coleman/sieve campaign.
The emergent finding below answers the target's finite-value question (the
complete list C0(Z)) outright by an elementary certificate. No quadratic
Chabauty machinery (Coleman integrals, rho, Strassman bounds, p-adic height
decomposition, sieve log, 2-descent rank certificate) is claimed.

## Definitions

- C0: affine curve y^2 = f(x), f(x) = x^6 + 3x^4 − 5x^2 + 7 over Z.
- C0(Z): integer pairs (x, y) with y^2 = f(x).
- For a rational x = a/b in lowest terms (coprime integers, b > 0), put
  N(a,b) = a^6 + 3a^4 b^2 − 5a^2 b^4 + 7b^6, so y^2 = N(a,b)/b^6.

## Result

**Theorem 1 (integral-point determination).** C0(Z) = ∅: there is no integer
pair (x, y) with y^2 = x^6 + 3x^4 − 5x^2 + 7.

**Theorem 2 (rational-point denominator lemma).** If an affine point of C0
over Q exists with x = a/b in lowest terms (b > 0), then 4 divides b.

## Proof / evidence

Theorem 1: squares mod 4 are {0, 1}. For x even, x^2 ≡ 0 mod 4 so
f(x) ≡ 7 ≡ 3 mod 4; for x odd, x^2 ≡ 1 mod 4 so
f(x) ≡ 1 + 3 − 5 + 7 = 6 ≡ 2 mod 4. Hence f(x) ∈ {2,3} mod 4 for all
x ∈ Z, never a square. Strengthening: f takes only residues {3,6,7} mod 8
(resp. mod 16: {3,6,7}), disjoint from quadratic residues {0,1,4}
(resp. {0,1,4,9}); every odd 2-adic square is 1 mod 8, so C(Z_2) = ∅.

Theorem 2: b^6 = (b^3)^2 is a square in Q, so N(a,b)/b^6 is a square in Q
iff N(a,b) is a square in Q; an integer that is a square in Q is a square
in Z (lowest terms: N = (r/s)^2 with gcd(r,s)=1 forces s=1). If 4 ∤ b:
(A) b odd, a even: N ≡ 7b^6 ≡ 3 mod 4, non-residue;
(B) both odd: N ≡ 1+3−5+7 = 6 ≡ 2 mod 4, non-residue;
(C) v_2(b)=1 (so a odd): b^2 ≡ 4 mod 8, b^4 ≡ b^6 ≡ 0 mod 8,
a^2 ≡ a^4 ≡ a^6 ≡ 1 mod 8, so N ≡ 1 + 3·4 = 13 ≡ 5 mod 8 while
squares mod 8 are {0,1,4}. The three cases exhaust 4 ∤ b and are verified
over all residue classes plus an exhaustive mod-8 scan showing every
(a,b) mod 8 with not-both-even and b ≠ 0 mod 4 is obstructed.

Model data: |disc(f)| = 4714544128 = 2^10 · 7 · 811^2 ≠ 0 (exact Bareiss
determinant of the 11×11 Sylvester matrix of (f, f′); sympy cross-check
disc = −4714544128), so the affine model is smooth (genus-2 degree-6 model).
Weighted P(1,3,1) projective closure has Y^2 = X^6 at Z = 0, i.e. two
Q-rational points at infinity [1:±1:0], smooth there; emptiness is an
affine-integral statement.

## Limitations

- No quadratic-Chabauty computation, p-adic height decomposition,
  Mordell–Weil sieve log, or 2-descent rank proof is supplied.
- LMFDB / Bianchi–Padurariu-411 untabulated status for C0 unverified
  (API queries returned no usable rows).
- C(Q) not determined; Theorem 2 plus finite searches are constraints and
  negative evidence only.
- Method is elementary congruence, not the target's QC machinery; the
  finite-list content (the empty set) is what is proved.

## Reproducibility

Stdlib-only, exact integer arithmetic (python3):

- `python3 output/artifacts/verify_c0_empty.py` → VERIFY_OK
  (mod-4 exhaustion, Bareiss disc ≠ 0, mod-8/16 witnesses, brute force
  |x| ≤ 50000 empty).
- `python3 output/artifacts/verify_denominator.py` → VERIFY_OK
  (cases A/B/C over all residues, exhaustive mod-8 scan, squareness sanity).
- `python3 output/artifacts/verify_c0_supplement.py` → VERIFY_OK
  (disc factorisation, E1′ disc −3244 = −4·811, F_5/F_11 reduction tables,
  E1′ traces/ordinarity, mod-4/8 recheck, p=7 bad-reduction exclusion).

## References

- J. Balakrishnan, N. Dogra, An effective Chabauty–Kim theorem.
  https://arxiv.org/abs/1803.10102
- F. Bianchi, O. Padurariu, Rational points on rank 2 genus 2 bielliptic
  curves in the LMFDB. https://arxiv.org/abs/2212.11635
- K. Finnerty, Quadratic Chabauty Experiments on Genus 2 Bielliptic Modular
  Curves in the LMFDB. https://arxiv.org/abs/2507.03784
- L. A. Betts et al., Local heights on hyperelliptic curves and quadratic
  Chabauty. https://arxiv.org/abs/2401.05228
