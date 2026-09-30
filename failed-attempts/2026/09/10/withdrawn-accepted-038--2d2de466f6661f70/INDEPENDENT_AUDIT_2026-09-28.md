# Independent Audit — 2026-09-28

**Record:** `2026/09/10/038`  
**Title:** 64-cap concurring bush datum at R0=65536 with claimed decoupling ratio at least 3/2  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `a6e2520e066d3200aac9512dfc506caf1bbcb3af`  
**Disposition:** **FAILED**

## Independent checks

- Read the repository's RESULT/METADATA and artifact inventory rather than accepting its prior PASS audit.
- Compared the admissibility claim with the canonical decoupling setup in which the Fourier-side decomposition uses cap-supported pieces.
- Separated numerical plausibility from a proof-grade lower bound.

## Three-axis assessment

- **Correctness — FAIL**: The headline is a certified lower bound for the canonical cap decoupling ratio, but the filed per-cap functions are untruncated Gaussians with nonzero Fourier tails outside their nominal caps, so they are not exact cap-supported pieces. More decisively, the numerator and denominator are estimated by Monte Carlo plus finite boxes; '-2 standard errors' is not a deterministic lower confidence certificate, and the denominator tail/truncation correction is asserted negligible rather than rigorously bounded. The record therefore does not prove R(f*)≥3/2 for an admissible canonical-cap datum.
- **Originality — UNRESOLVED**: A focused search did not locate this exact 64-cap numerical experiment, but an invalidated certificate cannot support a scientific priority claim. The only surviving content is exploratory numerical evidence, for which priority was not exhaustively established.
- **Scientific Value — FAIL**: As an exploratory Monte Carlo bush experiment the datum may guide future work, but the record is framed as a citable certified obstruction. Without exact cap support and rigorous integration/tail bounds it does not meet that claimed scientific use.

## Sources compared

- Repository record 038 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/038/RESULT.md — States the Gaussian/Monte-Carlo construction and explicitly notes that it is not a deterministic interval proof and would require a truncation correction.
- Bourgain–Demeter, The proof of the l2 Decoupling Conjecture: https://doi.org/10.4007/annals.2015.182.1.9 — Canonical decoupling is formulated through frequency pieces associated to caps; the record's noncompact Gaussian pieces require a justified localization/truncation step before constituting such a datum.
- Bhargava–Chan–Lim–Pang, A study guide for the l2 decoupling theorem for the paraboloid: https://arxiv.org/abs/2402.14756 — Provides the standard canonical-cap framework against which the witness was checked.

## Limitations

- This audit does not assert the numerical estimate is false; it finds that the stated rigorous lower bound is not established.
- A repair would require an exactly admissible cap-supported construction and proof-grade interval/tail control, followed by a fresh three-axis audit.

This audit is independent of the repository's pre-existing `AUDIT.json`. GitHub was read only as evidence; no repository changes were made by this audit run.
