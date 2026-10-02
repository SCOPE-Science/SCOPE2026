# Review status

Fresh independent audit completed on 2026-10-01 UTC.

Disposition: **failed**.

- Correctness: **PASS** — The transfer-matrix state explicitly stores frontier connectivity and persistent left/right boundary-touch flags. I checked the transition logic, independently brute-forced the same recurrence for 1-by-1 and 2-by-2 boxes, and reproduced exact agreement there; the archived 8-by-8 endpoint logs satisfy crossed+uncrossed=200^144 and the stated integer inequalities. Monotonicity of the increasing crossing event then proves the whole p interval.
- Originality: **PASS** — Best-of-knowledge: targeted Resultary and literature searches found no exact bond-percolation 8-by-8 endpoint table at p=0.495 and p=0.505. Exact finite-square percolation polynomials exist in nearby literature for site percolation, and finite-size crossing probabilities are extensively studied, but the inspected sources do not imply these exact bond values.
- Scientific value: **FAIL** — The box size 8 and window width 0.005 are a narrow finite instance with no demonstrated boundary, extremal role, or reusable structural consequence. Exactness and reproducibility alone do not supply a substantive mathematical reason for this particular finite slice.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for structured source comparisons and residual risks.
