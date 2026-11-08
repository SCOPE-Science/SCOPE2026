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
# Computational verification and limits

Run `python3 verify_matching_spread.py` with the standard Python library. The checker uses exact integer numerators for rational metric lengths and verifies:

- All six-state candidate extreme potentials and every maximizing assignment at 22 exact-rational instances for \(2\le k\le6\), including the exact odd-\(k\) threshold values.
- Independent enumeration from all signed tight spanning trees for \(k=2\) at \(\lambda=1/2\) and \(k=3\) at \(\lambda=1/3\), \(4/5\), and \(9/10\). It reconstructs respectively \(18\) and \(162\) distinct normalized extremal potentials and compares complete sets.
- The symbolic rational threshold identities for odd \(k\) through \(23\).

Observed terminal marker: `ALL_MATCHED_EQUILATERAL_SPREAD_CHECKS_OK`.

These are exact finite calculations and not an exhaustive proof for arbitrary \(k\) or real \(\lambda\). The universal claim follows from the analytic six-state and two-split replacement arguments in `RESULT.md`. No external or independent audit has been performed.
