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

Run `python CHECKER.py` with Python 3 and NumPy installed. The program checks 2,469 exact rational step identities across small grids, tests arbitrary-data jump decomposition and compares numerically integrated interpolant variation at larger grids. It is a finite independent consistency check of barycentric signs, cell representation and predicted growth, not an exhaustive infinite proof.

The analytical proof uses the alternating-tail integral, parity of finite-tail remainders, a uniform reciprocal-denominator \(C^1\) estimate, and explicit harmonic-number sums. Finite numerical total variation is estimated by dense sampling and can underestimate actual Jordan variation; no strict numerical certificate for the infinite theorem is claimed. Independent mathematical audit: not performed.
