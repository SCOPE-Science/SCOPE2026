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

# Verification scope

The supplied `verify.py` requires Python 3, SymPy and NumPy. It constructs the twelve actual signed-permutation rotation matrices and checks their multiplication closure. For the displayed algebraic fiducial, it verifies normalization, \(D=1/2\), \(C_v=0\), the group projector sum \(4I_3\), and \(\mathcal T(E_{ij})=E_{ij}+\delta_{ij}I_3\) **symbolically on all nine complex matrix units**. This exact finite-dimensional identity proves the optimal example and its reconstruction formula.

Fifty seeded numerical complex vectors are separately tested against the deductive nine-eigenvalue formula, comparing the computed real Gram spectrum. These trials only corroborate the formula; its universal validity rests on the character decomposition in `RESULT.md`. The trace argument proves the sharp bound for all unit fiducials. No unknown large-scale computation or external proof oracle is assumed.

No independent audit or historical priority certification has been performed. A plausible unindexed group-covariant design classification is the main remaining originality risk.
