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

Run `python3 verify.py` using Python 3.9 or later, from the directory containing this file and the script. It has no third-party dependencies. The actual packaged checker passed 15,506 finite assertions.

Checks comprise exact rational pseudoinverse identities on cycles (including opposite-vertex resistances and trace-inverse moments), direct weighted-Laplacian Fourier eigenvector substitutions, phase-side minimization tests, and finite-size numerical convergence to the derived constants. Exact arithmetic covers stated rational identities for the tested sizes. Floating-point tests have explicit tolerances. The assertion count counts finite identities and diagnostic comparisons, not distinct mathematical theorems.

The symbolic proof in RESULT.md, especially strict convexity on the unrestricted conductance simplex and endpoint-controlled asymptotics, is the basis of the infinite claims. The checker cannot certify their validity for all real orders, sizes, and prices. An independent mathematical audit has not been performed.
