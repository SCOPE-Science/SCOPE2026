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

# Reproducible checks

Run `python3 verify_eulerian.py` with Python 3 (standard library only). The script verifies the closed-form Eulerian expression using an independently computed recurrence for all \(3\le n\le400\). For levels \(1\le k\le12\), three consecutive-index blocks at distinct starting positions are exhaustively counted, and all \(2^k\) residues occur exactly once at each parity. The script tests 15,288 exact difference valuations for 2-adic branch maps, least-period obstructions and the immediately preceding preperiod obstruction.

Observed output:

```
VERIFY_OK Eulerian_recurrence_rows=398 dyadic_levels=1..12 complete_blocks=36 residue_inputs=49140 isometry_pairs=15288 sharp_preperiod=PASS least_period=PASS one_per_parity_fiber=PASS
```

## Limits

Finite checks alone cannot prove the theorem at unbounded powers of two. The all-level proof is the explicit valuation identity, finite-ring bijectivity, and earliest-start argument given in RESULT.md. No independent mathematical audit has been performed. The associated literature comparison remains subject to the stated access and historical-priority limitations.
