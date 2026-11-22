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

Exact-rational Python 3 diagnostic: `python3 verify.py` returns `ALL_CHECKS_PASS`. It checks four rank-one coupling orientations with the same positive coupling matrix and compares direct matrix iteration against the scalar recurrence at seven rational initial states for twelve iterations each. A separate test checks the nilpotent endpoint on admissible off-diagonal Hermitian matrices.

Analytical coverage is the complete finite-dimensional positive semidefinite order interval, not the tested rational grid. The main exact identities are the spectral bound \(0\preceq H(I-H)\preceq I/4\), the identity \(BHB^*=\sigma^2(v^*Hv)P\), and the fixed-coupling overlap parameter \(\lambda=\sigma^2|v^*u|^2\). The scalar parameter-four entropy and arcsine measure are classical results cited, not independently reproved by finite testing.

Self-review completed; external or independent audit has not been performed.
