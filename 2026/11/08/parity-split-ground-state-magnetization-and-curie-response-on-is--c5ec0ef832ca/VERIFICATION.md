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

# Verification

For each integer \(n\ge3\), the two-rim triangulation identity and each rim parity yield the exact ground frustrated-edge count. Equality conditions reduce the configurations to alternating rims for even \(n\), and one forced defect on each rim for odd \(n\). Defect locations uniquely determine the bottom ring up to global spin inversion, which proves the full spin-sector count. Finite Gibbs fluctuation-response yields the Curie coefficient after the zero-temperature limit at fixed \(n\).

The standalone script `verify.py` (Python 3 standard library) independently computes the labeled Hamiltonian by exhaustive search for \(3\le n\le9\) and via squared-cycle dynamic programming with spin-sector tracking for \(3\le n\le80\). A clean invocation `python3 verify.py` passed 319 exact assertions. These experiments are finite consistency checks and cannot certify the all-size theorem by themselves.

Only the complete equal-positive-coupling classical zero-field ground-state distribution and the specified finite-volume response limit are proved. No independent audit or expert validation was performed.
