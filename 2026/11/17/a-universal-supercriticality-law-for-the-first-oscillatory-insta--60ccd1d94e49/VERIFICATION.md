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

# Reproduction

From an extracted package containing `check_normal_form.py`, run `python check_normal_form.py` with Python 3 and SymPy. The check executes a free-parameter symbolic identity for the cubic radial coefficient and linear crossing; a direct symbolic Fourier reconstruction in a nontrivial algebraic sample; and a finite numerical observation of the leading small-circle radius. The exact derivation and the standard local Neimark–Sacker theorem establish the infinite-parameter statement, not the finite orbit. No independent audit has been performed.
