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

Run `python3 verify_transfer.py` with SymPy. It reconstructs the 81-state transfer and involution, calculates the 45-dimensional even and 36-dimensional odd characteristic polynomials with exact integer/rational operations, and compares the first eight paired orbit counts and spectral root bounds.

Run `python3 verify_direct.py` using only the standard Python library. It independently enumerates every one of the \(3^{2n}\) ternary firing-phase assignments for each seam at \(n=3,4,5\), and all \(6^6\) bounded chip configurations for \(n=3\), checking the original chip-firing update rule directly through three iterations. See `verification_output.txt` for actual stdout.

The infinite statements require the mathematical proof, especially the phase-to-chip bijection, transfer symmetry decomposition and complex-root sign argument. Finite tests only check instances. This is not an independent audit; no outside validation or scientific certification has been performed.
