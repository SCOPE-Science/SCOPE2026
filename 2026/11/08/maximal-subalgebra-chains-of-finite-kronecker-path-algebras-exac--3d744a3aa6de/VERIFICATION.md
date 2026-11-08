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

# Reproduction and scope

Run `python verify.py` with Python 3, requiring only the standard library. The program constructs reduced-row-echelon representatives for **all** linear subspaces in selected finite prime-field vector spaces, checks closure using the algebra multiplication, and dynamically counts chains by codimension-one containment. It verifies the formula without relying on a pre-enumerated subalgebra list or the theoretical recurrences to generate its chain totals.

Observed output:

```text
CHAIN_OK 2 0 subalgebras 5 chains 3
CHAIN_OK 2 1 subalgebras 13 chains 14
CHAIN_OK 2 2 subalgebras 43 chains 135
CHAIN_OK 2 3 subalgebras 185 chains 2604
CHAIN_OK 3 0 subalgebras 5 chains 3
CHAIN_OK 3 1 subalgebras 16 chains 19
CHAIN_OK 3 2 subalgebras 78 chains 344
CHAIN_OK 5 1 subalgebras 22 chains 29
VERIFY_OK
```

The program checks only these finite instances and does not verify all finite fields or the limiting distribution by exhaustive computation. The general conclusion is supported by the self-contained structural and asymptotic proof in `RESULT.md`. No independent mathematical audit has been performed.
