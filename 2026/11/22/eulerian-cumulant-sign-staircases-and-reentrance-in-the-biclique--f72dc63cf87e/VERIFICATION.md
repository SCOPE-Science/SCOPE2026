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

# Reproducibility and limitations

The included file `verify_cumulants.py` uses only Python's standard library. Invoke `python verify_cumulants.py` from the directory containing the script. It enumerates valid independent sets on selected complete bipartite graphs, directly computes rational joint moments, and evaluates the set-partition cumulant formula independently of the claimed simplification. The expected output is:

```
MIXED_CUMULANTS_EXACT: 392
K_3_2_REENTRANT_SIGNS: [-1, 1, -1]
```

The tests cover \(2\leq m\leq6\), \(1\leq n\leq7\), \(2\leq r\leq\min(m,5)\), and four exact activities. The proof in `RESULT.md` covers all stated graph orders and all real positive activities; the numerical zero approximations are not part of the exact certificate. Verification does not constitute an independent audit.
