# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable Paley-cyclotomic equiangular-line census to v<=31 with certified Gerzon-gap extremal frame
- **Round:** 2026-09-07-first-light-01
- **Lane:** 217
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Design Theory
- **Method:** cyclotomic difference-set search with Fourier character-sum verification and Gram-spectrum replay

## Problem

Enumerate Paley-type and low-order cyclotomic partial difference sets in cyclic groups of order v<=31; construct the associated real equiangular line sets / equiangular tight frames via explicit Gram matrices; certify equiangularity and coherence by Fourier character sums with Gram-spectrum replay; tabulate maximal cardinalities against the Gerzon absolute bound.

## Attempted claim

Complete replayable census for cyclic v<=31: list of all Paley-type and cyclotomic PDS parameters realized, explicit Gram matrix per construction with character-sum certificate of two-valued equiangular spectrum, maximal-cardinality table N(v) against the Gerzon bound d(d+1)/2, and one exhibited Gerzon-gap extremal frame (concrete D set, Gram matrix, spectrum log) whose gap to Gerzon is exactly certified.

## Research outcome

Fallback-claim design lemma achieved: 9 certified Paley/QR constructions (5 complex ETFs + 4 real line sets) with Fourier coherence certificates, exact Gram matrices/spectra, full v<=31 cyclotomic-union census (392 sets), one-sided Gerzon intervals with one saturated extremal (6 lines in R^3); all replayed independently (VERIFY_ALL_OK).

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Theorems 1-2 verified independently from scratch: exact integer difference tables for q=7,11,19,23,31 give (q,(q-1)/2,(q-3)/4) with skew D cap -D empty, and for q=5,13,17,29 give (q,(q-1)/2,(q-5)/4,(q-1)/4) with symmetric D=-D; exact integer C^2=qI (deviation 0) replayed; Fourier |S_a|^2=(q+1)/4 and (2S_a+1)^2=q hold to <1e-9/<1e-6 with both signs present; Gram spectra {0 x(q-d), q/d x d} (complex) and {0 x(n-d), 2 x d} (real) and coherences sqrt(q+1)/(q-1), 1/sqrt(q) replayed to <1e-9; Gerzon arithmetic d(d+1)/2 and d^2 gaps match table.csv. These are machine-checked certificates (integer identities + numerics rounded to proven integers with residuals far below spacing), honestly distinguished from proof, and correct. Theorem 3 is false as stated: (a) compute.py census() branches on m=len(cosets): if m<=10 enumerates all 2^m unions, else only single cosets/complements/full set. For prime v with phi(v)>10 (13,17,19,23,29,31) the trivial-subgroup case m=phi(v)>10 is therefore NOT exhaustively searched, contradicting 'every subgroup H, every union S' and 'exhaustive over cyclotomy-based sets'. For composite v<=30 phi(v)<=8 so that slice is exhaustive, but the prime claim is not. (b) The prime-order summary 'only nontrivial proper examples are QR Paley/skew-Hadamard sets and complements/multiples' is factually false on the artifact's own data: results.json census['31'] contains ten (31,6,1) DS sets (e.g. [1,5,11,24,25,27]) with k(k-1)=30=1*30, i.e. classical Singer (31,6,1) perfect difference sets from the order-5 projective plane, plus eight distinct (31,15,7) DS beyond QR/complements. These are nontrivial proper DS distinct from QR (k=6 vs 15) and are omitted from the 'no sporadic' summary. verify.py step 3 only re-tests stored sets, not completeness, so it cannot rescue the completeness claim. Hence an essential inference fails. originality: Strongest headline identities are textbook: QR Paley skew-Hadamard (q,(q-1)/2,(q-3)/4) and Paley-type PDS (q,(q-1)/2,(q-5)/4,(q-1)/4) parameters (Paley 1933); symmetric conference C^2=qI and real equiangular lines N=q+1 in R^{(q+1)/2} with coherence 1/sqrt(q) and Gram spectrum {0,2} (Goethals-Seidel/conference-ETF correspondence); complex harmonic ETFs N=q in C^{(q-1)/2} with Welch-bound coherence sqrt(q+1)/(q-1); Gerzon bounds d(d+1)/2, d^2 and saturation 6 lines in R^3 (icosahedron, Gerzon/Lemmens-Seidel 1970s). Gaps in table.csv are pure arithmetic from those classical N,d. Gram spectra follow mechanically from C^2=qI (eigenvalues +-sqrt(q) -> 0,2). Singer (31,6,1) DS (Singer 1938) anticipates the extra prime-order census hits. Nearest live priors checked (King-Tang 1606.03259 pillar/SDP bounds; Greaves et al. 2012.13642 finite-field ETFs; Brady 2406.09550 PDS local search to order 147) are complementary methods and do not contain the combined table, but substantive priority comes from the classical priors, not from absence of the exact combined table. Recomputing known parameters with Fourie…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Sharp maximality claimed ONLY for d=3 (6 lines in R^3 saturate Gerzon); all other cells are one-sided achieved lower bounds with certified coherence. Census covers cyclotomic-union sets (unit-coset unions +/-0), not all 2^v subsets. Float steps certified by rounding to proven integers with residuals <2e-12; q=29 Fourier q-error 1.65e-12. Individual Paley parameters are classical; novelty is the uniformly certified census + Gram/coherence table + extremal witness.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
