# Independent mathematical audit — SCOPE-20260914-031

Disposition: **failed**.

## Correctness
**PASS** — The transfer-matrix state explicitly stores frontier connectivity and persistent left/right boundary-touch flags. I checked the transition logic, independently brute-forced the same recurrence for 1-by-1 and 2-by-2 boxes, and reproduced exact agreement there; the archived 8-by-8 endpoint logs satisfy crossed+uncrossed=200^144 and the stated integer inequalities. Monotonicity of the increasing crossing event then proves the whole p interval.

## Originality
**PASS** — Best-of-knowledge: targeted Resultary and literature searches found no exact bond-percolation 8-by-8 endpoint table at p=0.495 and p=0.505. Exact finite-square percolation polynomials exist in nearby literature for site percolation, and finite-size crossing probabilities are extensively studied, but the inspected sources do not imply these exact bond values.

### Equivalent formulations
The claim is an exact finite-graph reliability/crossing probability statement; equivalent formulations as a two-terminal boundary reliability polynomial were searched conceptually, with no exact matching value found.

### Broader coverage
The broader finite-size literature motivates the object but does not mechanically imply the exact bond values used here.

### Exact database or table
Absence of a table is not itself novelty proof; originality rests on the model mismatch and statement comparison with the inspected finite-size sources.

### Claim versus prior implication
The prior results are scaling/numerical or site-percolation exactness results, not a theorem implying this bond-percolation certificate.

### Source inspections
- **Effective boundary extrapolation length to account for finite-size effects in the percolation crossing function** (https://doi.org/10.1103/PhysRevE.54.2547): not covering exact certified endpoint values. Numerical high-precision crossings up to large rectangles; no exact 8-by-8 rational table.
- **Exact percolation probabilities for a square lattice: Site percolation on a plane, cylinder, and torus** (https://arxiv.org/abs/2204.01517): different percolation model. Exact polynomials are for site percolation, not bond percolation.

## Scientific value
**FAIL** — The box size 8 and window width 0.005 are a narrow finite instance with no demonstrated boundary, extremal role, or reusable structural consequence. Exactness and reproducibility alone do not supply a substantive mathematical reason for this particular finite slice.

## Residual risks
- The 8-by-8 full DP was not independently reimplemented to completion in a distinct algorithm during this run; correctness instead rests on code reconstruction, small-box brute-force agreement, exact conservation, and the two archived endpoint runs.

## Checked sources
- record artifacts/dp_engine.py, verify_endpoints.py, run_lo.log, run_hi.log
- Resultary search
- Ziff 1996
- arXiv:2204.01517
