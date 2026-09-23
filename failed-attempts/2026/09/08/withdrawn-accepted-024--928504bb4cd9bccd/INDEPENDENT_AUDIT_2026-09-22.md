# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `9d27acad0d956eafd4f0a32c93bcd68a68d58a6c`, matching the assignment guard. RESULT.md blob: `0773275da816c9fa44897ad872201320d291e49e`.

## Claim reviewed
Finite Murnaghan stabilization census for small padded cores. This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS FOR THE FINITE TABLE; STABILIZATION INTERPRETATION LIMITED. The prior independent audit replayed the n=6..10 character tables and all 1728 finite trajectories with no arithmetic mismatch. However, constancy only through n=10 is not itself a proof of the true stabilization threshold unless supported by a general bound; the record properly marks 59 trajectories still increasing at 10 but its 'stabilized-in-window' labels remain finite-window observations.

## Originality
FAIL/NARROW. Kronecker stability and explicit stabilization bounds are established in the literature. A small core-weight ≤4 census over n≤10 is therefore at most a finite illustration unless it improves a known bound or exposes a structural phenomenon not implied by existing stability theory.

## Scientific value
FAIL. Extending a known eventually-stable sequence only over n=6..10 and tabulating small-core trajectories is routine finite data. The recovered audit also found that short in-window plateaus can be misleading, so the census cannot safely stand in for exact stabilization thresholds. No new general bound, proof mechanism, or representation-theoretic consequence is supplied.

## Literature checked
- E. Briand, R. Orellana and M. Rosas, The stability of the Kronecker products of Schur functions: https://arxiv.org/abs/0907.4652
- S. V. Sam and A. Snowden, Proof of Stembridge's conjecture on stability of Kronecker coefficients: https://arxiv.org/abs/1501.00333

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
A bounded repair can relabel all finite plateaus as 'constant through n=10' and avoid suggesting an exact stabilization threshold absent a covering theorem. That does not create a new stability bound or structural result, so the value axis still fails.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `9d27acad0d956eafd4f0a32c93bcd68a68d58a6c`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
