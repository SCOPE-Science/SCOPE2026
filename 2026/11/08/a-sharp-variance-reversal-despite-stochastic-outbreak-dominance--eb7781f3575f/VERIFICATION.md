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

# Reproduction and verification

Run `python verify.py` with Python 3.9 or newer and `sympy>=1.10`. No external data files or internet access are needed. The script enumerates all \(2^9=512\) edge configurations per graph and each of the six possible initial vertices. It independently computes a rooted component-size distribution from vertex-subset connectivity recurrences, using exact symbolic arithmetic, and verifies the resulting probability laws against direct enumeration.

It then checks the integer edge-state count table, the exact threshold polynomials, the first two raw moments, and the variance difference. It verifies the coefficient list for \((1+u)^{12}Q(u/(1+u))\), whose one change of sign implies at most one positive root by Descartes' rule. Since \(Q(0)>0\) and \(Q(1)<0\), this proves exactly one variance crossing in the entire open interval. Numerical root isolation is only for reporting the location, not for proving uniqueness.

The code reproduces two rational test points to confirm the sign reversal, and all calculations require only the two nine-edge graph definitions supplied in the proof. The exact computations establish this finite-six-vertex comparison; there is no general claim for all finite cubic graphs. Earlier historical publication priority is not certified and no independent external scientific validation has been performed.
