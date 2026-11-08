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

# Reproducible finite verification

Execute `python3 verify_mcgee.py` with Python 3.10 or later and SymPy. It requires no input downloads. This exhausts all 553301 nonempty faces and their 4268208 covering incidences, using two different sequential vertex orders. For each order it explicitly constructs the matched oriented Hasse digraph and checks a complete acyclic topological sort. It constructs integer Morse boundaries by recursive elimination of signed unit incidences and calls exact Smith normal form. The recorded `verification_output.txt` contains the independent critical-cell, Smith-invariant and Betti outputs, ending `ALL_CHECKS_PASS`. The Euler characteristic and matching counts are additional exact cross-checks.

These computations constitute finite constructive evidence for this fixed 24-vertex complex. They do not test an infinite family, exclude an equivalent unindexed calculation, establish an equivariant homotopy type or prove that the space is a wedge of spheres. No independent mathematical audit has been performed.
