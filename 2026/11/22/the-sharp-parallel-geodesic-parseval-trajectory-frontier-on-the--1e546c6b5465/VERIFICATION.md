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

# Mathematical verification

The analytic proof uses exact Fourier orthogonality on each loop and exact finite-root-of-unity orthogonality across loops. Maximum longitudinal-frequency fiber width is computed for every primitive winding, and the fixed-loop-cost bound is reduced to a primitive lattice-vector minimization. The all-integer proof covers arbitrary \(N\ge1\) and \(L\ge2\).

The included `check_torus.py` tests 12,544 cases of the fiber cardinality and discrete Gram orthogonality, plus exhaustive length minimizations for band sizes one through seven. Running `python check_torus.py` reports `PASS`. These are finite verification checks, not substitutes for the proof. No independent audit has been performed.
