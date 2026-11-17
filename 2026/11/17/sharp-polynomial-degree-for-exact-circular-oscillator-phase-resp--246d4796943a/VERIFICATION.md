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

Run `python verify_degree.py` with SymPy available. It checks the rational-coefficient exact degree-seven unit-circle example, both polar polynomial identities, the periodic phase-adjoint equation, the source's Cartesian iPRC, and eight additional finite-Fourier test profiles of degrees zero through seven. For the published degree-seven target it also checks the full degree-six candidate coefficient system (19 equations, 30 unknowns): ranks 18 and 19 after augmentation, hence rigorously inconsistent. All checks passed when executed from the freshly authored source directory. The Fourier lower bound and all-degree quantifiers are analytical; these finite computations are supporting checks only. No independent mathematical audit has been performed.
