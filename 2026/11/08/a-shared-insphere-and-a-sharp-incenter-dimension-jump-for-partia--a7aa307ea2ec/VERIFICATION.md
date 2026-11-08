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

# Reproducibility and scope

Run `python check.py` in an environment with `numpy>=1.21` and `scipy>=1.9` installed (see `requirements.txt`). The executed program returned:

`PASM_INBALL_CHECKS_PASSED 64 128 linear programs, ranks and witnesses`

For all ordered shapes from one-by-one through eight-by-eight, the script independently creates every prefix halfspace of the partial-ASM polytope and every nonnegativity/row/column constraint of the matching polytope; it solves 128 Chebyshev linear programs. It checks the claimed optimal formula, explicit optimal centers, and ranks of constraints active at relatively interior centers, together with nonunique-center witnesses and the complete two-by-two segment. LP accuracy is numerical and does not certify higher dimensions. The written proof gives an exact universal argument relying only on the cited published inequality description and elementary Euclidean halfspace geometry.

No independent mathematical audit has been performed.
