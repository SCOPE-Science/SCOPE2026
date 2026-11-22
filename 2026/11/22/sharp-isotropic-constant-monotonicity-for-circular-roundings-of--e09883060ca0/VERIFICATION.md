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

# Reproducibility

Run `python3 check_parallel_polygon.py` using a Python 3 environment with SymPy. The program checks two exact polynomial identities independently of numerical geometry and reconstructs area and inertia by line-and-arc Green integration at nine polygon orders and seven radii. The completed local run passed 272 algebraic and numerical assertions.

The infinite family and strict positivity are **analytically** established: \(\sin\alpha-\alpha\cos\alpha>0\), followed by \(f'(\alpha)>0\) and \(g'(\alpha)>0\), imply the strictly negative derivative certificate. Finite quadrature cannot certify all side counts and radii. No independent mathematical audit or expert validation is claimed.
