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

# Verification and scope

Direct program `verify_exhaustive.py` iterates all four-column-type inputs for \(3\le n\le8\). It does not use the transfer matrix to obtain outcomes: each update is computed by independent majority-of-three operations on the two physical rows. It checks every attractor basin, the exceptional shifting family, and the maximum transient. Output: `exhaustive_output.txt`.

Exact matrix program `verify_transfer.py` verifies \(\operatorname{tr}(T^n)-2^{n+1}=4^n-2^n\) for \(3\le n\le21\), evaluates all pair-correlation numerators by separate exact matrix products, and compares them against word-by-word enumeration for \(3\le n\le9\). Output: `transfer_output.txt`.

Commands from the directory containing the scripts:

```
python3 verify_exhaustive.py
python3 verify_transfer.py
```

Both recorded program outputs end in `ALL_DIRECT_CHECKS_PASS` and `ALL_TRANSFER_CHECKS_PASS`, respectively. The proof in RESULT.md establishes the infinite family without extrapolation from these bounded tests. There is no independent external audit.
