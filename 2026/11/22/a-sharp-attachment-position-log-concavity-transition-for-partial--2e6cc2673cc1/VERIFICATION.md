---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 verify_petrial_p4.py` with standard Python 3. Direct binary adjacency-matrix rank enumeration tests every diagonal perturbation of both tree families at \(m=1,2,3\), i.e. \(2^{5}+2^{9}+2^{13}\) perturbations for each root location. The checker also tests exact integer polynomial coefficients, log-concavity defects for \(1\le m\le100\), the closed boundary identity and its sign. Expected terminal line: `VERIFY_OK`.

For the internally rooted family, the full positive coefficient vectors after dividing out \(z^{3m}\), with \(m=1,2,3,4,5,6\), are:

- \(m=1\): `2,13,17` (smallest defect 135)
- \(m=2\): `4,48,207,253` (smallest defect 1476)
- \(m=3\): `8,140,1092,3443,3509` (smallest defect 10864)
- \(m=4\): `16,368,4474,23848,55781,46585` (smallest defect 63840)
- \(m=5\): `32,912,16746,129910,482790,866481,600281` (smallest defect 295872)
- \(m=6\): `64,2176,62274,650276,3302090,9040152,12928003,7569397` (smallest defect 749440)

The first three coefficients at \(m=7\) are \(128,5056,242234\), with defect \(-5442816\). The all-order recurrence-free threshold proof, including strict endpoint positivity, is in `RESULT.md`. This file does not claim that a finite test proves an infinite theorem.
