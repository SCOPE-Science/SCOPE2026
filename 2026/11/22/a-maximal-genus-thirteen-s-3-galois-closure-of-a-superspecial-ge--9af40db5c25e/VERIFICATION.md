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

The standalone file `verify.py` uses only the Python 3 standard library. Execute `python3 verify.py` alongside this file. Its exact exhaustive outputs are:

```
F11 root patterns, G, C, Y: ({0: 4, 1: 5, 2: 2, 3: 0}, 12, 12, 12)
F121 root patterns, G, C, Y: ({0: 48, 1: 0, 2: 12, 3: 61}, 408, 210, 232)
GENUS13_S3_MAXIMAL_F121_VERIFIED
```

The F121 representation is valid because \(-1\) is a nonsquare in \(\mathbb F_{11}\). The finite test checks every \(t,u\) pair in each indicated field, not a sample. Its normal-closure fiber arithmetic assumes the mathematical proof of irreducibility, squarefree discriminant, and tame degree-six \(S_3\)-Galois structure in `RESULT.md`. It does not certify the general algebraic claims independently and is not an external audit.
