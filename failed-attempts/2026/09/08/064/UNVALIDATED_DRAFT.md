# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Partial theorem: a certified [36,11,12] witness, residual classification lemmas,
# and a new reduction link for the live-open binary BKLC cell (36,11)

## 1. Status of the target interval

The Brouwer/Grassl table BKLC(2,36,11) reads Lb = 12 / Ub = 13 (open). This was
re-verified live during this investigation (CodeTables.de, page last change
30.12.2011): the Lb = 12 chain runs subcode-of-[36,13,12] <- shortening-of-
[37,14,12] <- parity-extension-of-Morri [36,14,11]; the Ub = 13 chain runs
shortening-to-[34,9,13] -> truncation-to-Heijnen [33,9] = 12 (Heijnen 1993 thesis:
no binary [33,9,13]). The interval is **not closed here**: neither a [36,11,13]
witness nor a [36,11,13]-nonexistence proof is obtained. What is delivered is the
admitted fallback package, strengthened in one place (a new cross-cell reduction).

## 2. Certified result 1 — independent [36,11,12] witness (exact, replayed)

**Theorem A (witness).** There exists a binary linear [36,11,12] code with full
support. Its exact weight enumerator is

    W(z) = 1 + 66z^12 + 192z^13 + 168z^14 + 64z^15 + 61z^16 + 256z^17 + 432z^18
         + 256z^19 + 61z^20 + 64z^21 + 168z^22 + 192z^23 + 66z^24 + z^36.

*Construction (new matrix, classical route).* Start from the narrow-sense binary
BCH code of length 31 and designed distance 11 (zeros alpha^1..alpha^10 over
GF(32) = GF(2)[x]/(x^5+x^2+1); four degree-5 minimal polynomials give a
degree-20 generator, hence dimension 11). Exhaustive enumeration of all 2^11
codewords measures its true minimum distance 11. Appending an overall parity bit
gives [32,11,>=12] (measured enumerator 12:496, 16:1054, 20:496, 32:1 —
doubly-even), and appending 4 repeated columns gives [36,11,>=12]; the minimum
is measured exactly as 12 (66 minimum words), rank 11, full support (coordinate
union over all codewords = all 36 positions).

*Verification.* `output/artifacts/witness_36_11_12.json` stores the 11x36
generator matrix (integer bitmasks) and the enumerator above.
`output/artifacts/verify_witness.py` (stdlib only) recomputes rank, full
support, and the full enumerator from the stored matrix and asserts
[36,11,12]: replayed VERIFY OK. `output/artifacts/bch_witness.py` rebuilds the
witness from scratch (finite-field arithmetic + exhaustive enumeration).

This witness is independent of the tabled Lb chain (Morii subcode route): it
uses the BCH/parity/lengthening route instead.

## 3. Certified result 2 — residual classification (exact integer arithmetic)

**Lemma B (first-order residual; proved).** Let C be a putative binary
[36,11,13]. Since C meets its minimum distance, it contains a weight-13 word c.
The residual code Res(C;c) (restrict C to the complement of supp(c), keeping
codewords that vanish on supp(c)... in the standard binary-residual convention
Res has length 36-13 = 23 and dimension 10) satisfies d(Res) >= ceil(13/2) = 7.
Griesmer numbers recomputed exactly here: G(10,9) = 25 > 23, so d(Res) <= 8.
Hence **d(Res) in {7, 8}**: every putative [36,11,13] has its residual in one of
exactly two subfamilies. Residuals with d* >= 9 are **eliminated** (proved
elimination of a nontrivial residual subfamily = admitted fallback item (ii)).

**Lemma C (second-order cascade; exact).** From a [23,10,7-or-8] code, a further
residual step gives [16-or-15,9,d**] with d** >= 4; G(9,6) = 17 > 16 excludes
d** >= 6 at length 16, leaving d** in {4,5} — Griesmer-consistent, no kill
claimed. Griesmer table recomputed in `griesmer.py`: G(11,13) = 33 <= 36
(nonexistence not mechanically implied — consistent with admission),
G(11,12) = 30, G(11,14) = 34, G(10,14) = 33, G(10,16) = 36, G(10,18) = 42,
G(10,7..9) = 20,21,25, G(9,4..6) = 13,16,17, G(7,13) = 30. Certificate:
`output/artifacts/cert_griesmer_residual.json`.

## 4. New reduction link — (36,11) implies (36,10) (proved)

**Lemma D (even-weight subcode reduction; proved).** A putative [36,11,13] C
contains a binary [36,10,d''] even-weight subcode with d'' in {14,16} (itself if
C is all-even, else ker(parity|_C); even weights of C are >= 14 since 13 is odd;
d'' >= 18 is excluded by G(10,18) = 42 > 36; odd d'' is impossible for an
even-weight code). In particular **[36,11,13]-existence implies
[36,10,14]-existence**: the neighboring open cell (36,10) (itself the subject of
a prior open attempt) would fall as a corollary. Contrapositively, a future
nonexistence proof for [36,10,14] kills [36,11,13] in Fork B outright, leaving
only the all-even Fork A (C itself [36,11,>=14], G(11,14) = 34 <= 36, allowed).
Certificate: `output/artifacts/cert_structure_lemmas.json`.

## 5. Honestly recorded non-results (what was tried and did NOT close the cell)

- **MacWilliams/Krawtchouk averaged LP: no bound claimed.** A from-scratch
  float two-phase simplex was built, but cross-checks disagreed (unscaled
  max-A13 = 195.06 vs rhs-scaled primal = dual = 306.34): the Krawtchouk
  coefficients span 1e1..1e13 and the float simplex stalls. The LP code was
  removed from the artifacts and is **not** cited as proof of anything; the
  failure is logged in WORKLOG.md.
- **Shortening cascade to Heijnen anchor: consistent, no contradiction.**
  Shortening a putative [36,11,13] twice gives [34,9,>=13], compatible with the
  closed tabled value d(34,9) = 13; the Heijnen [33,9,13]-nonexistence anchor is
  real but does not contradict the putative code. Recorded against nonexistence.
- **Bounded construction hunt (800 candidates, exact 2^11 check each):**
  400 double-circulant + 400 random systematic [36,11] codes; best minimum
  distance 10; no [36,11,13] found (run logged in WORKLOG.md; hunt script
  removed from artifacts as it certifies nothing).

## 6. Reproducibility

All proofs replay with stdlib-only Python (numpy not needed), run from
`output/artifacts/`: `python3 bch_witness.py` (rebuild),
`python3 verify_witness.py` (verify), `python3 griesmer.py`,
`python3 structure_lemmas.py`. Total runtime under one minute.

## 7. Separation of proof / computation / conjecture

- Proof (hand-checkable): Lemmas B, D constructions (residual dimension/length
  count, parity-functional kernel, Griesmer lookups once values are recomputed).
- Computed evidence (machine-replayed): Theorem A witness + enumerator;
  Griesmer table values; hunt log (negative).
- Conjecture (not claimed): none about the cell's true value; the interval
  Lb = 12 vs Ub = 13 remains open. The bet of this report is only that Lemma D
  usefully couples the two neighboring open cells.
