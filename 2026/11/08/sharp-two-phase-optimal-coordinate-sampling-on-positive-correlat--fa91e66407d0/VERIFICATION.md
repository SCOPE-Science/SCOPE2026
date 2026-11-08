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

# Deterministic verification

Run `python artifacts/verify_friendship_sampling.py` using Python 3 with no external dependencies, from the package root. The program uses exact rational arithmetic to check the explicit sampler, both active eigenvalue identities, nonnegative radial determinant certificates, positivity of probabilities, rational-grid upper bounds for class-symmetric alternatives, a five-coordinate exact witness, an exact branch equality check at the sharp boundary, and the expected one-step quadratic energy-decrement identity.

The recorded replay output in `artifacts/verification_output.txt` is:

```
PASS exact rational analytical checks
admissible parameter designs: 343
radial/pair phases: 107 / 236
exact active-eigenvalue certificates: 343
symmetric rational-grid upper bounds: 34643
exact expected-energy identities: 46
witness m=2,s=1/2,t=1/5: hub=25/193, leaf=42/193, rate=21/193
scope: finite tests support; do not replace the general proof
```

The global result is proved analytically in RESULT.md using symmetry averaging, full spectrum decomposition, and exact optimization of the radial matrix and pair-limited branch. No computational search over finitely many instances can prove the infinite parameter claim; it is not being used that way. Independent mathematical audit has not been performed.
