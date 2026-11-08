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

The proof identifies the accessible orthogonal projector by generating the radial and first-harmonic cyclic spaces from the absorber layer. The missing radial central Walsh eigenvector occurs precisely for even dimensions. The exact position-basis kernel follows from a centered subset-incidence tight-frame identity; the survival/capture interpretation follows from strict decay on the complementary invariant subspace when every local loss rate is positive.

`artifacts/verify.py` is a standalone Python 3 standard-library checker. Run `python3 artifacts/verify.py`. It constructs a separate Walsh-eigenspace restriction Gram pseudoinverse, uses exact rational arithmetic for every entry in dimensions \(2\le d\le7\), and computes independent finite-field adjacency Krylov ranks. Expected successful output:

```
VERIFY_OK exact_projector_entries=21840 modular_krylov=6
```

These calculations verify finite cases, not the all-dimension theorem or worldwide originality. No independent scientific audit has been performed.
