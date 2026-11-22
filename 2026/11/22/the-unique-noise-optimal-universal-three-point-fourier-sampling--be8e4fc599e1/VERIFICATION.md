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

The exact arithmetic source `certify.py` and its actual run output `certify_output.txt` are included. Execute `python3 certify.py` from the extracted directory. It requires only Python 3 standard library modules and tests the exact symmetry classification, all complete column translation orbits, integer leading principal minors, rigorous trigonometric enclosure, and the rational strict eigenvalue bounds. The final output line starts with `PASS:` if every assertion is satisfied.

A separate source `independent_check.py` and its actual output `independent_output.txt` numerically evaluate all 6,900 three-by-three Fourier restrictions across the three universal representative row sets. Execute `python3 independent_check.py` with NumPy available. This confirms the 25 consecutive minimizing frequency triples and the diagnostic eigenvalues, but is a non-rigorous numerical cross-check.

The proof's exact reduction from 2,300 row triples to six affine row classes and from 2,300 frequency triples to 92 translation classes is implemented using explicit integer tuples, not sampled data. Strict separation uses rational integer determinant signs with a \(10^{-6}\) guard margin; the complex Fourier entry approximation error is proved below \(10^{-9}\) and Gram operator error below \(6\cdot10^{-9}\). Full-spark characterization is externally referenced to a proved prime-power theorem. No other modulus is included in the claim.
