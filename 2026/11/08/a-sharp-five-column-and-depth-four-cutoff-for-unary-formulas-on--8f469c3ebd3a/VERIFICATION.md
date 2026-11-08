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

# Verification

The scientific certificate is finite and may be replayed from the accompanying files using Python 3 without third-party libraries:

```
python3 checker.py
python3 direct_check.py
```

`checker.py` builds all 255 nonempty supports of the eight binary column triples. It checks 3072 pointed support worlds, validates that successive modal types refine the preceding types, and verifies the displayed depth-by-width table through depth five. Identical depth-four and depth-five type counts, together with the explicitly checked refinement property, show that the partition is a fixed point. `direct_check.py` does not use support compression; it independently processes every valuation on the labelled three-by-m grid for each m from 1 through 5. It checks 8, 64, 512, 4096 and 32768 valuations, respectively, yielding the same type counts.

The proof in `RESULT.md` establishes that these finite computations suffice for all column counts via a surjective bounded-morphism support map. It also constructs finite modal-depth characteristic formulas, so the type census determines the full Boolean formula algebra. No statement about more than one proposition, additional modalities, or independent human verification is made.
