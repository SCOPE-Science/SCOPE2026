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

# Verification record

The proof is self-contained in `RESULT.md`. The key unbounded step is cutoff compatibility: at any larger divisor cutoff, the two inputs and their candidate generator have identical local unit flags and radical-vector equalities, with zero coordinates appended, so the finite principal-intersection identity remains valid before taking the directed union.

Run `python VERIFY.py` with Python 3 and no external packages. It enumerates the finite subrings with cutoffs 2, 6, 12, 18, 24 and 30, checks the direct-product multiplication and zeta inversion, constructs every principal ideal from all ring multiples, and verifies every pairwise intersection. Observed output:

```
PASS N=2 basis=2 elements=4 principal-pairs=16
PASS N=6 basis=4 elements=16 principal-pairs=256
PASS N=12 basis=6 elements=64 principal-pairs=4096
PASS N=18 basis=6 elements=64 principal-pairs=4096
PASS N=24 basis=8 elements=256 principal-pairs=65536
PASS N=30 basis=8 elements=256 principal-pairs=65536
STABLE N=2 TO M=24 pairs=16
STABLE N=6 TO M=12 pairs=256
STABLE N=6 TO M=30 pairs=256
STABLE N=12 TO M=24 pairs=4096
VERIFY_OK 139536
```

The finite experiments do not exhaust the infinite ring. No independent mathematical audit or external formal certification has been performed. Source-priority evaluation is limited to the cited paper sections and relevant discoverable literature; a general idealization theorem might subsume the abstract intermediate argument.
