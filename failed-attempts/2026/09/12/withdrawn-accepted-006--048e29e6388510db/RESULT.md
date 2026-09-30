# Exact witnessed 4-rank census for all-positive two-prime real quadratics below 2500

## Context
The 2-primary part of class groups of real quadratic fields is governed by genus theory (2-rank), Rédei-matrix theory (4-rank), and Gerth's narrow-versus-wide unit-norm correction, with asymptotic behaviour predicted by the Cohen–Lenstra–Gerth heuristics (Fouvry–Klüuners, Milović, Smith governing fields). Explicit finite witnessed tables testing these predictions in fixed two-prime windows remain sparse. This record closes the all-positive window: discriminants that are the product of two primes both congruent to 1 mod 4.

## Definitions
- Fields: K = Q(sqrt(pq)) with p < q odd primes, p ≡ q ≡ 1 (mod 4), pq < 2500. There are exactly 81 such pairs.
- Since pq ≡ 1 (mod 4) and is squarefree, disc(K) = pq with two prime discriminants; genus theory gives 2-rank exactly 1.
- Ordinary 4-rank r4(K) = F2-dimension of Cl(K)[4]/Cl(K)[2]; here r4 ∈ {0,1}, equal to 1 iff 4 divides the ordinary class number h(K).
- Narrow class number h+ from signed reduced indefinite forms via rho-cycle classes (Buell); ordinary h = h+ if the fundamental-unit norm N = N(eps_K) is −1, else h+/2.
- Rédei block: for two primes the 1×1 block has rank 0 iff Legendre symbol (p/q) = +1, rank 1 iff −1. Narrow 4-rank prediction is 1 − rank.
- Witnesses: integer (x,y) with x² − Dy² = t and x ≡ y (mod 2) (ring-of-integers parity for D ≡ 1 mod 4).

## Result (headline claim)
For every K = Q(sqrt(pq)) with p < q both 1 mod 4 and pq < 2500 (81 fields), the ordinary 4-rank is 0 or 1. Exactly 13 fields have r4 = 1, at pairs (p,q): (5,29), (5,89), (5,101), (5,181), (5,229), (5,349), (5,401), (5,461), (13,53), (13,61), (13,101), (13,173), (17,53); the other 68 have r4 = 0. In (legendre, N, r4) counts: (−1,−1,0)×46, (+1,+1,0)×22, (+1,−1,1)×8, (+1,+1,1)×5. Every (p/q) = −1 field has N = −1 and r4 = 0; every (p/q) = +1 with N = −1 has r4 = 1; of the 27 (p/q) = +1, N = +1 fields exactly 5 have r4 = 1 (D = 505, 905, 2005, 689, 793, each with h+ = 8, h = 4). The naive rule r4 = 1 − rank(Rédei) corrected by subtracting 1 whenever N = +1 is therefore false; the correct rule proved here is r4 = 1 − rank when N = −1, and r4 = 1 iff 4 | (h+/2) when N = +1, decided per field by the rho count.

## Proof / evidence
Pure-stdlib replayable pipeline, independently re-executed by the auditor:
1. Pair enumeration by sieve: exactly 81 pairs p < q, 1 mod 4, pq < 2500; Legendre symbols by Euler criterion give the Rédei rank.
2. Class numbers from signed rho-cycles (census.py): set of signed reduced forms (a,b,c) with b²−4ac = D and |sqrt(D)−2|a|| < b < sqrt(D); rho operator by brute-force k; per-field asserts of closure and bijectivity; cycle count equals h+; ordinary h via N. Re-ran: counts above, zero N = −1 mismatches against narrow prediction.
3. Unit-norm certification (certify_norms.py): period l of sqrt(D); l odd gives integer convergent of norm −1 (N = −1, 54 fields); l even plus Legendre-approximation completeness over the first 2l convergents certifies N = +1 (27 fields). Auditor additionally verified N signs against minimal-unit search including half-integer (x+y√D)/2 units.
4. Known-value validation (validate_known.py): reproduces h+ for D = 5, 12, 13, 29, 316, 65, 85, 145; ALL OK.
5. Witnesses (build_witnesses.py → witnessed_table.json): r4 = 1, N = +1 (5 fields): norms in {±4p, ±4q}; r4 = 1, N = −1 (8 fields): norms −4p²/±4q²-type square-of-generator norms with y > 0; r4 = 0, leg = −1 (46 fields): Legendre log; r4 = 0, leg = +1 (22 fields): N = +1 certificate plus rho ordinary h ∈ {2,6}. Every norm identity verified by substitution and parity.
6. Final replay (verify.py): re-derives pair list, Legendre symbols, norm identities, parity, and r4 consistency; prints ALL 81 FIELDS REPLAY OK and VERIFY_OK (auditor reproduced).
7. Independent analytic cross-check (auditor): L(1,kronecker(D,·)) via digamma/Hurwitz plus minimal regulator R = log(eps) including half-integer units (e.g. D = 85 half-unit (9+√85)/2) yields h = sqrt(D)/2·L/R matching all 81 claimed h values to < 0.02 (e.g. D = 65 → 2, D = 85 → 2, D = 145 → 4, D = 2305 → 16).

## Limitations
- Class numbers rest on the implemented rho-cycle theorem (standard result, validated on 8 known values plus per-field closure/bijectivity asserts) rather than an independent computer-algebra system; the analytic class-number-formula agreement above is the independent check.
- Norm-witness y-minimality is claimed only within searched bounds (y ≤ 400000 with spot extensions); existence and correctness are exact by substitution, minimality is not claimed.
- Scope is exactly the 81-field window; no claim about 8-ranks, densities beyond calibration use, or other congruence classes.

## Reproducibility
Run from output/artifacts: python3 census.py; python3 certify_norms.py; python3 validate_known.py (expect VALIDATION_ALL_OK); python3 verify.py (expect ALL 81 FIELDS REPLAY OK and VERIFY_OK). Witnessed table: witnessed_table.json. Scripts are pure stdlib (plus sympy/mpmath only for the auditor's independent cross-check, not required for replay).

## References
- Rédei–Reichardt rank formula and Lagarias unit-norm method (general theory used as tool).
- Gerth 4-rank criteria; Fouvry–Klüuners and Milović 4-rank densities; Smith governing fields (asymptotics, not finite tables).
- Buell, Binary Quadratic Forms (rho-cycle classes); Davenport–Heilbronn/Legendre approximation for norm completeness.
- LMFDB Number Fields (per-field data only; no window 4-rank witness vector).
