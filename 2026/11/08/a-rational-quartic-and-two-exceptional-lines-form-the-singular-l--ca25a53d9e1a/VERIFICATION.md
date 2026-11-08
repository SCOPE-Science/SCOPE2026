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

# Verification of exact chart calculations

The included `verify_exponent7_singular.py` requires Python 3 and SymPy. Executing

```bash
python3 verify_exponent7_singular.py
```

on the packaged source returned `VERIFY_OK`. It rederives the stacked determinant, the finite/infinity graph matrices, verifies the derivative ranks and their 2-by-2 minor gcds, and checks identities equating the critical equations to the two explicit ideals. It also verifies that the common kernel section maps to the rational normal quartic and the endpoint graph matrices vanish as claimed.

The two local ideals directly show that the critical scheme is reduced and contains no extra component; the geometric finite-radicial-unramified criterion from Stacks Tag 04XV is applied in the written proof, not delegated to the symbolic checker. No independent audit has been carried out. Exact scope: a characteristic-zero complex threefold and its reduced singular support; no statement about the nonreduced singular scheme.
