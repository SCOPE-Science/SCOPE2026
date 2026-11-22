# Review of exact affine cyclotomic gap spectra

## Correctness — PASS
The proof supplies the exact coefficient formula for the integral quotient, proves the cyclic block words are nonzero, and proves an insertion lemma tracking **every** adjacent-support gap across changing block lengths. It handles the possibly shortened final block by using the leading coefficient. Consequently the universal affine identity is an actual proof, not a pattern extrapolated from experiments. The exact 15-block arithmetic and vector table were separately verified with 120 long divisions by the published standalone script, including complete coefficient multiplication and no unseen larger gaps. All quantifiers and endpoint conventions are specified in `RESULT.md`.

## Originality — PASS, qualified
Cafure–Cesaratto (2025) fully count gaps in two residue classes for **binary** cyclotomic polynomials, not ternary \(\Phi_{15p}\). The open-access *The ternary cyclotomic polynomials \(\Phi_{3pq}\)* has an effective coefficient-block recurrence and Table 9 counting coefficient **values**, plus the maximal gap, but no full adjacent-support gap vector. Zheng (2026-11-17) proves a broad extremal-gap theorem, including the already-known top column \(N_8=2Q\), which the present analysis does not claim as new. The complete eight-class histogram, four possible supports and explicit all-cofactor cyclic gap-slope formula were not found stated in these works or semantically matching published-finding corpus records.

The main residual originality risk is implicit derivability from older coefficient-block formulas. Ordered adjacency is not determined by coefficient-value counts, but a complete constructive coefficient formula can in principle recover it. Literature search cannot prove uniqueness. The 2025 paper, first public on 2025-07-25, is the qualifying motivating source; later papers were examined to evaluate overlap only.

## Mathematical value — PASS
The exact classification distinguishes four structurally meaningful congruence regimes and completely determines every support-gap multiplicity in the first nontrivial ternary family. It also establishes an all-odd-squarefree-cofactor affine increment mechanism with explicit finite cyclic data, enabling future gap classifications beyond the one table. The new result is more than the known maximal gap or a count of coefficients by value.

## Evidence and limits
Reproduction: `python3 verify_gap_hist.py`, standard library only. The infinite theorem is derived in the proof; 120 exact finite tests validate the arithmetic table. No claim of an independently reviewed mathematical proof, exhaustive historical search or broader general formula for all ternary indices is made.

Self-review: passed. Independent audit: not yet performed.
