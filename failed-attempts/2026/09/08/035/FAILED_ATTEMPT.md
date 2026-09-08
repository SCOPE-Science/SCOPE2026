# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified coherence-floor witnesses for overcomplete Grassmannian line packings in C^4 and C^5 with Welch-Levenshtein separation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 131
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Quantum Information Theory
- **Method:** coherence minimization with exact complex Gram PSD/rank verification and Welch-Levenshtein bound audit

## Problem

Survey Grassmannian line packings in C^4 (N=17-20) and C^5 (N=26-30), the first overcomplete rungs beyond SIC cardinalities 16 and 25, via coherence minimization over cyclotomic ansatzes and certify window-best upper bounds on minimal coherence mu*(N,d) by exact complex-Gram PSD/rank verification with Welch/Levenshtein separation logs.

## Attempted claim

Exhibit explicit N-line packings for at least one surveyed (N,d) rung with N beyond d^2 in C^4 or C^5 (N=17-20 with d=4; N=26-30 with d=5) with: (a) explicit unit vectors over cyclotomic integers, (b) exact maximal coherence mu proved from all pairwise overlaps, (c) Gram matrix proved PSD of rank at most d, and (d) logged gaps of mu above the Welch and Levenshtein lower bounds plus frame-potential cross-check, establishing a window-best certified upper bound on mu*(N,d).

## Research outcome

All nine surveyed overcomplete rungs solved with EXACT minimal coherences (stronger than the requested upper bounds): mu*=1/2 in C^4 (N=17-20) and mu*=1/sqrt(5) in C^5 (N=26-30), via MUB sub-packings with exact cyclotomic overlap census, Gram PSD/rank logs, Welch gap tables (0.03-0.05), zero orthoplex gap, and tight-frame cross-checks, replayable in seconds.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the exact numerical theorem is mechanically implied by two classical results the DRAFT itself concedes are classical. (a) Complete MUB sets in prime-power dimensions with coherence exactly 1/sqrt(d): d=4 gives 5 bases/20 vectors, d=5 gives 6 bases/30 vectors (Ivanovic 1981; Wootters-Fields 1989; standard Fourier/Hadamard MUBs). (b) Rankin/orthoplex bound mu>=1/sqrt(d) for N>d^2 (Rankin 1955; Conway-Hardin-Sloane). Combining them, any N with d^2<N<=d(d+1) has mu*(N,d)=1/sqrt(d) by subset monotonicity with gap 0 -- exactly the nine claimed rungs. This general folklore fact (MUBs saturate the orthoplex bound; orthoplex-achieving subsets) anticipates all nine values at once; listing N=17,18,19,20 and 26,...,30 separately adds no new extremal object. Explicit cyclotomic coordinates are the standard MUB matrices, and exact overlap rechecking is routine verification, not a new theorem statement or boundary. Admission's 'no prior source records this witness package' is a failed-search/packaging claim, which per audit rules does not establish priority over mechanical implication. value: FAIL: even taken as correct and (narrowly) unrecorded in this exact tabulated form, the result is a textbook restatement plus trivial parameter substitution, explicitly excludable. The entire content is: quote classical MUB coherence, quote classical orthoplex lower bound, observe equality on subsets. No new packing is constructed (parents are textbook MUBs), no bound is improved (gap 0 is the known equality case), no hard case is closed (optimality is one-line, no search/certificate needed beyond citing the bound), and the nine rungs are nine instantiations of one trivial subset observation. The 'certified witness package + audit pipeline' (coordinate files, float replay, Welch-gap table) is routine re-verification scaffolding, not an independently retrievable research advance; Welch gaps 0.03-0.05 merely restate the known strict separation of Welch vs orthoplex regimes. A future reader needs only the two classical theorems, not this enumeration.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: MUB existence, the Ivanovic/Wootters-Fields constructions, and the orthoplex/Welch bounds are classical results, not new; the novel contribution is the certified witness package and audit pipeline for these nine rungs, as scoped. Two C^4 entangled bases were discovered numerically then verified exactly (recognition is not part of the proof). Gram PSD/rank is structural from explicit vectors (overlap census is the certificate); eigenvalue logs are cross-checks only. No claim beyond N=17-20/d=4 a…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
