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

The executable `verification/verify.py` is a standalone Python 3 + SymPy checker. It independently enumerates all simplices and their dihedral group orbits for \(5\le n\le12\), constructs both quotient cellular differentials, checks the chain identity, calculates the exact integral Smith factors of the second boundary, and verifies Euler characteristics and second Betti ranks. The corresponding exact output is `verification/run_output.txt`.

The mathematical proof for all \(n\ge5\) uses the published shellability theorem, fixed-point geometry, Armstrong's fundamental-group theorem, the Euler characteristic formula, Whitehead's homological theorem, and the integral Bockstein identity. The script cannot by itself prove the infinite claim or the category statement. No independent mathematical audit has been performed.
