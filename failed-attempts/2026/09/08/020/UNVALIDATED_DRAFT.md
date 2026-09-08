# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Least quadruplet–quintuplet diamond 30 apart below 10^9:
a certified 9-tuple witness at 685124351 with a Hardy–Littlewood density gap

## Abstract
Let H = (0, 2, 6, 8, 30, 32, 36, 38, 42): a prime quadruplet together
with, 30 higher, the canonical prime-quintuplet shape (0, 2, 6, 8, 12).
We prove H is admissible; we prove by complete segmented-sieve census
that n = 685124351 is the least integer below 10^9 with all nine values
n + H prime and the unique such integer below 10^9; we certify each of
the nine primes by deterministic Miller–Rabin (bases 2, 7, 61, valid
below 2^32) with an independent sympy cross-check; we compute the
Hardy–Littlewood singular series S(H) = 866.36 ± 0.31 (partial product
868.162 to 2000, 866.364 to 10^5) and show the leading-term HL prediction
below 10^9 is ≈ 1.229 versus ≈ 0.00142 for the naive independence model
(an ≈ 866× local-factor enhancement); and we supply a Selberg Λ² sieve
upper-bound certificate U = 1794237 (level D = 10^5, sifting primes
≤ 11) bracketing the certified count 1. All computations replay from the
four scripts in `artifacts/`.

## 1. Statement of results

**Theorem 1 (admissibility).** The 9-tuple
H = (0, 2, 6, 8, 30, 32, 36, 38, 42) is admissible: for every prime p,
the residues of H mod p do not cover all classes mod p. In particular
p = 2: {0}; p = 3: {0, 2}; p = 5: {0, 1, 2, 3}; p = 7: six classes
{0, 1, 2, 3, 4, 6}; and for p = 11, 13, 17, 19 the occupancy is
8, 8, 7, 8 < p, for p = 23, 29, 31, 37, 41, 43 machine-verified
occupancy 9 < p, and for p > 43 the nine offsets are pairwise distinct
mod p (since diam(H) = 42 < p) so ν_p = 9 < p.

**Proposition 2 (distinguished cap).** The symmetric one-point extension
of the twin-quad core obtained by capping from below,
B = (0, 2, 6, 8, 12, 30, 32, 36, 38), occupies all seven classes mod 7
and is therefore inadmissible. By contrast, H caps the core from above:
H[4:] − 30 = (0, 2, 6, 8, 12), the canonical admissible quintuplet.
Hence the +42 cap is the distinguished minimal one-point completion of
the twin-quad core to a quadruplet + canonical quintuplet.

**Theorem 3 (least and unique witness below 10^9).** n = 685124351 is
the least integer n ≥ 2 with all nine values n + h (h ∈ H) prime, and it
is the only such integer below 10^9. The nine primes are
685124351, 685124353, 685124357, 685124359, 685124381, 685124383,
685124387, 685124389, 685124393.

**Theorem 4 (primality certificates).** Each of the nine values passes
deterministic Miller–Rabin with bases (2, 7, 61) — deterministic for all
n < 2^32 (Jaeschke 1993; the test values are < 10^9 < 2^30) — with
per-value (d, s, base-by-base) logs in `artifacts/admissibility_mr.json`,
independently cross-checked by `sympy.isprime` (all True).

**Theorem 5 (density gap).** For H,
S(H) = ∏_p (1 − ν_p/p)(1 − 1/p)^{−9} = 866.36 ± 0.31
(partial product to 2000: 868.162; to 10^5: 866.364; tail in
[0.99964, 1], proved in §4). The naive leading-term prediction below
X = 10^9 is X/(log X)^9 ≈ 0.00142, while the Hardy–Littlewood
leading-term prediction is S(H)·X/(log X)^9 ≈ 1.229, i.e. an ≈ 866-fold
local-factor enhancement. The observed count 1 agrees with the HL order
of magnitude and is ≈ 700× the naive expectation (0.00142 in either
rounding).

**Theorem 6 (Selberg bracket).** A Λ² sieve at level D = 10^5 sifting
by primes {2, 3, 5, 7, 11} with optimal weights gives the rigorous upper
bound U = 1794237 (rounded up; main term X/G = X/770 ≈ 1298702, error
≈ 495523, small-n correction 11) for the number of n < 10^9 with all
nine n + H prime. It is nontrivial (U < 10^9) and consistent with the
certified count 1 (U ≥ 1). The value G = 770 holds exactly (closed form
∏ p/(p − ν_p)); the weights, λ_1 = 1, and the error ledger are in
`artifacts/selberg.json`.

**Neighborhood structure.** In [N0 − 50, N0 + 82] the primes are
303, 339 | 351, 353, 357, 359 | 381, 383, 387, 389, 393 | 399, …:
the lower four form a run of consecutive primes, and the upper five
form a run of consecutive primes with next prime 685124399 (gap 6).

## 2. Admissibility (proof)
Direct residue computation (replay: `admissibility_mr.py`).
H mod 2 = {0}; mod 3 = {0, 2}; mod 5 = {0, 1, 2, 3}; mod 7:
offsets mod 7 are 0, 2, 6, 1, 2, 4, 1, 3, 0, i.e. {0,1,2,3,4,6},
missing 5. Small-prime occupancies ν: 11→8, 13→8, 17→7, 19→8, and 23, 29, 31,
37, 41, 43 → 9 (machine-verified); for p > 43 the nine offsets are
pairwise distinct mod p because any two differ by at most 42 < p, so
ν_p = 9 < p. Hence admissible.
The competing bottom cap B mod 7 is {0,1,2,3,4,5,6} (full), so B is
inadmissible: the +42 top cap, not the symmetric bottom cap, is the
admissible completion.

## 3. Census: leastness and uniqueness (proof)
Two agreeing segmented sieves over [0, 10^9) with base primes to
√(10^9) < 31623 (3401 base primes, verified in both scripts) and
segment 5·10^6, testing offsets H:
(a) numpy pipeline `census.py`: exactly one hit, n = 685124351, in 1.7 s
(log `census.log`, record `census.json`);
(b) independent stdlib-only bytearray audit `census_audit.json` logic:
exactly one hit, same n, in 71.0 s.
Both scan in increasing order, so the single hit is both the least and
the unique witness below 10^9. A third pure-Python loop over survivor
positions (62 s) independently re-found n = 685124351 as the first hit.
Slicing-based marking `seg[start−low::p] = 0…` is the standard exact
segmented Eratosthenes step; correctness follows because every composite
below 10^9 has a prime factor ≤ √, hence appears among the 3401 base
primes and is marked in its segment.

## 4. Singular series and the density comparison (proof)
ν_p: 2→1, 3→2, 5→4, 7→6, 11→8, 13→8, 17→7, 19→8, and ν_p = 9 for all
p ≥ 23 (distinctness argument as above; machine-verified to 2000).
Partial products: 868.162 (p ≤ 2000), 866.364 (p ≤ 10^5).
Tail bound: for p > 9, log f(p) = Σ_{k≥1}(9 − 9^k)/(k·p^k); the k = 1
term vanishes and all k ≥ 2 terms are negative, so the tail product is
< 1; the k = 2 term −36/p² dominates and Σ_{p>10^5} 1/p² ≤ 10^{−5},
Σ 1/p³ ≤ 5.1·10^{−11}, giving tail ∈ [0.99964, 1]. Hence
S(H) ∈ [866.05, 866.37], reported as 866.36 ± 0.31 (conservative
rounding; script values in `singular.json`).
With X = 10^9, log X = 20.7233: naive X/(log X)^9 ≈ 0.0014187;
HL leading term S(H)·X/(log X)^9 ≈ 1.229. Ratio = S(H) ≈ 866.
Honest reading: this is agreement of the data (count 1) with the HL
order of magnitude versus the naive model — a calibration of the local
factors at an explicit witness, not an anomaly or a proof of HL.

## 5. Selberg certificate (proof)
Subset sieve on primes {2,3,5,7,11} (any H-hit with all values > 11
survives; n ≤ 11 contributes ≤ 11). Level D = 10^5 exceeds
∏P = 2310, so the support is all 32 squarefree divisors and
G = Σ ρ(d) = ∏ p/(p−ν_p) = 2·3·(5/1)·(7/1)·(11/3) = 770 exactly
(script verifies G against closed form to < 10^{−9} relative).
Optimal weights λ_e = μ(e)f(e)G_e/G with λ_1 = 1 (verified); main term
X/G ≈ 1298701.30; error Σ|λ_1λ_2|ω(lcm) ≈ 495522.83 with |r_d| ≤ ω(d);
U = main + error + 11 ≈ 1794235.13, reported rounded up as 1794237.
This is the standard Selberg upper-bound sieve (e.g. Friedlander–Iwaniec
Theorem 7.1); fp error is absorbed by the round-up. Nontrivial
(U ≪ 10^9) and consistent with count 1.

## 6. Reproducibility
- `artifacts/census.py` → `census.json` + `census.log` (numpy census).
- `artifacts/admissibility_mr.py` → `admissibility_mr.json`
  (residues, nine MR traces, sympy x-check, neighborhood prime list).
- `artifacts/singular.py` → `singular.json` (partial products, tail
  interval, leading terms; integral diagnostics included but not claimed).
- `artifacts/selberg.py` → `selberg.json` (G, weights, main/error/U).
- Independent bytearray audit → `artifacts/census_audit.json`.
Runtimes: census 1.7 s / audit 71 s; MR/sieve-series scripts seconds.

## 7. Limitations and honest scope
(i) The census proves leastness/uniqueness below 10^9, not infinitude
of such diamonds (open; implied by Dickson's/HL conjectures only).
(ii) The "≈700×/866× gap" is HL-vs-naive-model enhancement at one
explicit witness, not a discrepancy with HL (observed 1 vs HL 1.23
agrees). (iii) The Selberg bound is weak (≈1.79M vs truth 1) — it is a
correctness-checked bracket, not a sharp estimate; sifting only to 11
was chosen for a tiny exact-support certificate. (iv) The integral
diagnostics in `singular.json` (∫_2^X dx/(log x)^9 ≈ 4524·… shape and
truncated variants) are exploratory and NOT part of the claim; only the
leading-term comparison (0.00142 vs 1.229) is claimed. (v) Originality:
base n appears in OEIS A059925 (8-point parent) and the HL/Selberg
machinery is classical (Hardy–Littlewood 1923; Selberg; Maynard–Tao
context) — the new content is the 9-point capped diamond, its
least+unique certification, and the computed density bracket, per the
admission searches (9-offset and cap-value queries: No results).

## References
Hardy–Littlewood 1923 (Acta Math.); Jaeschke 1993 (det. MR below 2^32);
Friedlander–Iwaniec, Opera de Cribro (Selberg sieve); Maynard
arXiv:1311.4600; Ford–Green–Konyagin–Maynard–Tao arXiv:1412.5029;
OEIS A059925, A338866; Prime Pages glossary (constellation, k-tuple
conjecture).
