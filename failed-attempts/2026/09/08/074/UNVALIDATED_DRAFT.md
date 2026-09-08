# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified partial classification of the 2520-pinned distinct-covering slice (minimum modulus ≥ 4)

## Abstract

Pin moduli to divisors of 2520 bounded by 30. There are 18 such moduli, so 2¹⁸ = 262144
modulus sets, and every check is CRT enumeration modulo some L | 2520 (at most 2520 classes).
For the minimum-modulus-≥ 4 sub-slice (16 moduli) we prove:

1. **Reciprocal sieve.** Of the 48 divisors L | 2520, exactly eight pass the necessary
   covering-count inequality Σ_{m ≥ 4, m | L} L/m ≥ L, namely
   {120, 180, 360, 420, 504, 840, 1260, 2520}; the other 40 are excluded by exact integer
   arithmetic.
2. **Complete UNSAT of two LCM classes.** No choice of residues covers ℤ_L for the full
   eligible set — hence for *any* subset of it — when (L, eligible) =
   (120, {4,5,6,8,10,12,15,20,24,30}) or (180, {4,5,6,9,10,12,15,18,20,30}).
   Both UNSAT runs are replayable exhaustions (1 433 516 and 1 207 709 DFS nodes).
3. **Explicit density witness.** Residues
   (4,3),(5,0),(6,2),(7,0),(8,1),(9,0),(10,2),(12,1),(14,2),(15,1),
   (18,6),(20,4),(21,3),(24,5),(28,6),(30,28)
   cover exactly 2422 of 2520 classes (density 1211/1260 ≈ 0.960317; 98 uncovered),
   verified by direct enumeration.
4. **Documented boundary.** The classes L ∈ {360, 420} are censused with 0 covers found
   but 12/10 residue-search timeouts respectively, so no theorem is claimed there; the
   classes {504, 840, 1260, 2520} and any minimal-LCM extremal are left open.

## 1. Definitions and scope

- A *distinct covering* is a finite set of congruences aᵢ (mod mᵢ) with distinct moduli
  mᵢ whose union is all of ℤ.
- Universe: U = {m : m | 2520, 2 ≤ m ≤ 30}, |U| = 18, lcm(U) = 2520.
- Sub-slice: U₄ = {m ∈ U : m ≥ 4}, |U₄| = 16.
- For an LCM class L | 2520, the *eligible set* is E(L) = {m ∈ U₄ : m | L}.
  Any covering with lcm dividing L and min ≥ 4 uses moduli ⊆ E(L), and covering ℤ is
  equivalent to covering ℤ_L.

## 2. Theorem (partial classification)

**Theorem.** Let L | 2520 and E(L) be as above, restricted to moduli ≥ 4.

- (i) If Σ_{m ∈ E(L)} L/m < L, no distinct covering with min ≥ 4 has lcm dividing L.
  This excludes every divisor of 2520 except {120, 180, 360, 420, 504, 840, 1260, 2520}
  (exact integer counts; §4 table).
- (ii) For L = 120 with E = {4,5,6,8,10,12,15,20,24,30} and for L = 180 with
  E = {4,5,6,9,10,12,15,18,20,30}, no residue choice covers ℤ_L — for the full set,
  hence for every subset (an extra modulus can always be assigned an arbitrary residue,
  so subset-coverability implies full-set-coverability).
- (iii) The residue list above covers exactly 2422/2520 classes with the 16 moduli of U₄.

*Proof.* (i) Counting: each class covers exactly L/m of L residues; full coverage needs
Σ L/m ≥ L. Machine table in §4, replayed by `artifacts/verify.py`.
(ii) Exhaustive DFS (§3) with node counts logged; replayed by `artifacts/verify.py`.
(iii) Direct enumeration; replayed by `artifacts/verify.py`. ∎

## 3. Method (auditable search)

Masks mod L are Python-int bitmasks; DFS branches on the first uncovered residue n with
the forced residue n mod m for each remaining modulus (smallest L/m first) and prunes by
Σ L/m < uncovered-count. This is complete: it explores every residue combination up to
the forced-choice symmetry. Node counts: 1 433 516 (L=120), 1 207 709 (L=180); a full
subset re-census (every reciprocal-passing subset of each class) independently returns
0 feasible / 0 timeouts.

## 4. Reciprocal-sieve table (LCM classes with min ≥ 4)

| L | E(L) | Σ L/m vs L | status |
|---|------|-----------|--------|
| 120 | 4,5,6,8,10,12,15,20,24,30 | 2814 ≥ 2520 (scaled) | UNSAT proved |
| 180 | 4,5,6,9,10,12,15,18,20,30 | 2814 ≥ 2520 | UNSAT proved |
| 360 | 4,5,6,8,9,10,12,15,18,20,24,30 | 3234 ≥ 2520 | open (0 covers, 12 timeouts in subset census) |
| 420 | 4,5,6,7,10,12,14,15,20,21,28,30 | 3144 ≥ 2520 | open (0 covers, 10 timeouts) |
| 504 | 4,6,7,8,9,12,14,18,21,24,28 | 2850 ≥ 2520 | open |
| 840 | 14 moduli | 3564 ≥ 2520 | open |
| 1260 | 14 moduli | 3564 ≥ 2520 | open |
| 2520 | 16 moduli | 3984 ≥ 2520 | open; best residue density 2422/2520 |
| all other 40 divisors | — | Σ < L | excluded by counting |

(Scaled column: Σ 2520/m over E(L); threshold 2520. Full per-divisor rows in WORKLOG §1
/ divcensus output.)

## 5. Relation to the literature (originality boundary)

Harrington et al. (arXiv:2605.18644) pin LCMs to 2ᵃ3ᵇ5ᶜ — no factor 7 — so the
7-inclusive classes here (notably L = 420, 840, 1260, 2520) lie outside it.
Agrawal et al. (arXiv:2208.09720) bound cardinality (≤ 10), not LCM divisibility.
Hough (arXiv:1307.0874) and Balister et al. (arXiv:1811.03547) give analytic bounds,
no LCM-pinned census. The UNSAT certificates for L = 120, 180 and the 2422/2520 witness
are new computational certificates, not transcriptions.

## 6. Limitations and open slice (uncertainty stated explicitly)

- No maximal-density claim: 2422/2520 is a lower bound on the full-16 maximum.
- No covering-existence verdict for U₁₆ as a whole (DFS capped at ~1.17M nodes/120 s).
- No minimal-LCM extremal: classes 360–2520 remain open, so the headline minimal-LCM
  question is NOT resolved.
- Conjecture (not claimed): the L = 360/420 timeouts are search weakness, not hidden
  coverings; reciprocal margins there are thin (3234, 3144 vs 2520).

## 7. Reproduction

- `output/artifacts/cover.py` — search/verification toolkit (stdlib only).
- `output/artifacts/verify.py` — replays every claimed number; prints ALL FINAL CHECKS PASSED
  (reciprocal census, 2422/2520 witness, both UNSAT runs). Rerun confirmed.
- Working scripts retained in `work/` (not part of the certificate): divcensus, hc/hill
  heuristics, brute_small/brute360/brute420_504 censuses, dfs_class driver.
