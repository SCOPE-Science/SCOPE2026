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

# Verification of the minimum projection spacing theorem

Run `python3 verify.py` from the directory containing this file. The checker uses only the Python standard library. It checks the exact inverse-Cartan Gram matrix and its row sums for dimensions three through nine, the simplification of the tetrahedral asymptotic coefficient, and independent midpoint quadrature of the exact two-dimensional simplex integral for the tetrahedron at thresholds zero and three near-optimal thresholds. With the delivered script, the program printed `ALL_CHECKS_PASSED`.

The numerical probabilities near the three-dimensional endpoint \(1/\sqrt{10}\), at deficits \(0.005,0.01,0.02\), respectively, are approximately \(0.00029532244\), \(0.00117641667\), and \(0.00466791768\). Their ratios to the proposed leading term approach one as the deficit decreases. The exact mathematical proof is given in `RESULT.md`; finite quadrature and finite-dimensional matrix checks do not establish the infinite-dimensional family of statements or total-variation convergence.

All algorithms and constants needed to repeat the supplied numerical checks are included here. These are mathematical self-checks, not an independent audit.
