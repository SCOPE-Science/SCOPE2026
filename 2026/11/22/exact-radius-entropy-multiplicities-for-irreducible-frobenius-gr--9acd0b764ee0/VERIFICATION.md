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

The proof is the normal-subgroup, commuting-image, and scalar-entropy argument in `RESULT.md`. The standalone `check.py` uses only the Python standard library, constructs the relevant finite groups and independently enumerates generator-image candidates. It checks the full homomorphism identity for every candidate on every ordered pair in each finite group. It then verifies counts of commuting-image pairs and triples and brute-force Laurent width counts for radius one to three at three field sizes.

Run `python check.py` to reproduce these finite computations. They test representative groups and finite radii, not the infinite universal theorem. The scalar Laurent entropy formula is a published theorem, and the unrestricted group classification is argued in `RESULT.md`. No external independent audit is asserted.
