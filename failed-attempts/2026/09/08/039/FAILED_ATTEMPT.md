# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Attainability of the diameter bound on algebraic connectivity for 4-regular diameter-2 graphs at Moore orders
- **Round:** 2026-09-07-first-light-01
- **Lane:** 136
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Spectral Graph Theory
- **Method:** Moore counting/defect plus quotient-interlacing with targeted witness construction and bounded verification

## Problem

Decide attainability of the Exoo et al. diameter upper bound on algebraic connectivity for connected 4-regular graphs of diameter D=2 at the Moore-bound orders n=15,16,17: prove a Moore-defect impossibility lemma restricting which orders can attain, and exhibit explicit attaining (or provably closest) witnesses with verified diameter and spectra, against the 19-vertex Robertson (4,5)-cage baseline.

## Attempted claim

For each n in {15,16,17}, determine with proof whether a connected 4-regular diameter-2 graph attains the Exoo et al. diameter upper bound on algebraic connectivity: a Moore-defect lemma rules out attainment outside at most the Moore order, and each attainable case is witnessed by an explicit adjacency matrix with BFS-verified diameter 2 and interval-enclosed algebraic connectivity meeting the bound (non-attaining orders carry a quantified gap).

## Research outcome

Closed the full n=15,16,17 attainability table negatively and more: the Exoo D=2 bound for d=4 degenerates to vacuous B=4+2√3≈7.4641, unattainable at EVERY order by Fiedler, with quantified gaps and verified diameter/spectrum witness records.

## Why this attempt failed

Failed axes: originality, value.

originality: No new structural result. The deliverable is formal substitution K=1 into published Exoo Eq.(2) plus textbook Fiedler bound a(G)<=n*delta/(n-1). Exoo et al. arXiv:2307.07308 Table 1 deliberately tabulates only D>=3 with no D=2 row; the omission is structural (even-diameter proof needs K>=2 and middle layer). Plugging K=1 to get 4+2*sqrt(3) and noting it exceeds d+1>=any 4-regular AC is immediate parameter substitution visible to any reader, not the promised Moore-defect impossibility lemma, quotient-interlacing, or n=15/16/17 attainability table. Draft admits: no Smith/interlacing lemma (induced-subgraph gap, conjecture only), no Robertson 19-vertex re-verification (Petersen substituted), 16-vertex SA unused. Cakiroglu Higman-Sims bound, Robertson cage, Hoffman-Singleton nonexistence supply only background. A timestamp or failed search does not establish priority for a two-line vacuity observation. value: Not independently worth finding later. Showing a formally-extrapolated number 7.46 exceeds the universal Fiedler ceiling 5 (hence exceeds every 4-regular AC, max 5 at K5) is a vacuity note explaining why D=2 is untabulated, not a boundary decision feeding degree-diameter/cage tables or Exoo conjectures. Scope n=15/16/17 is rendered irrelevant by the claim at every order; quantified gaps are just B minus Fiedler ceiling, not per-graph spectral gaps; witnesses are explicitly not needed for the proof. Falls under reject categories: textbook restatement (Fiedler) + mere parameter substitution (d=4,K=1) + unexplained enumeration (octahedron/K44/Petersen/random n=15 records). Neither target (attainable/unattainable table with bound-meeting witnesses) nor fallback (proved defect lemma + Robertson baseline + smallest attaining witness) was delivered.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Robertson 19-vertex cage baseline not re-verified (Petersen used instead); Smith/P4 interlacing lemma dropped as conjecture (induced-subgraph gap); 16-vertex SA residual-2 run is heuristic evidence only and unused by the proof; D>=3 attainability untouched.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
