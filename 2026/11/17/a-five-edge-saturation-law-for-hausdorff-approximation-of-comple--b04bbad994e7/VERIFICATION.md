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

# Verification and limitations

For each \(3\le n\le40\), the attached checker constructs exact rational root-projection certificates and evaluates the complete necessary and sufficient \(\ell_1\)-ball first-order conditions. It checks 10,659 unordered root pairs in total, including 7,770 long-root exact certificates and 2,886 short-root feasible upper bounds. The all-pairs checks agree with the exact four-case maximum and the endpoint-locality shell formulas. It also independently tests the separation-four strict nonoptimality certificate needed for the second vertex shell.

An additional solver, using a nonnegative positive-minus-negative decomposition and constrained quadratic optimization, reproduces 38 exact certificate distances across orders three through ten with maximum squared-distance discrepancy \(2.51\times10^{-14}\). The independent implementation is a separate computational cross-check, **not** an independent mathematical audit. These checks cannot extrapolate to infinite dimensions on their own; the proof supplies all-parameter KKT certificates and convexity arguments.

Reproduce with `python3 verify_path_hausdorff.py` (Python 3, NumPy, SciPy). The exact rational checks use only the Python standard library, while the optional independent optimization stage needs NumPy/SciPy. The theorem has not been independently audited. Historical novelty is assessed on the accessible primary literature and public indexed mathematical findings, not certified as a complete historical search.
