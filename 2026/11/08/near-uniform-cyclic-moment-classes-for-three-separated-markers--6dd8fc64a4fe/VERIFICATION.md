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

The substantive theorem is proved in `RESULT.md` by a three-to-one marked-gap parameterization and an exact cube-root-of-unity computation. Independently, `verify.py` enumerates actual unordered index triples without using the proof's gap compositions, rejecting any triple with a circular spacing below \(h\), and compares every syndrome count with the stated closed formula. Run `python verify.py` with Python 3 and no third-party libraries.

Observed output:

```
VERIFY_OK 247 independent parameter checks (6 <= n <= 42, h >= 2)
```

The verified domain of the computation is finite, but the written arguments apply to every \(h\ge2\), \(n\ge3h\). No independent audit, machine formalization or external certification has been performed. Possible historical coverage beyond the inspected sources remains an originality limitation.
