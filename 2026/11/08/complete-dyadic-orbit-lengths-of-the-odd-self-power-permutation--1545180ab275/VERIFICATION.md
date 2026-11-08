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

The script `verify_selfpower.py` uses only the Python standard library, ordinary modular exponentiation, and independent functional-graph traversal. It performs complete enumeration of odd classes modulo \(2^k\) for \(1\le k\le16\). For every enumerated starting point it checks that the least period agrees with the valuation formula. It also compares the global cycle counts with the closed census and checks the previously published two-step rooted-walk count. Separate iterative tests verify \(\nu_2(F^{2^j}(x)-x)\) at forty-bit precision for 127 odd inputs across eight stages.

Replay: `python3 verify_selfpower.py`.

Observed successful output:

```
VERIFY_OK k=1..16 complete_odd_cycles=PASS total_cycles=3626 valuation_tests=1016 max_cycles=PASS prior_two_walk_counts=PASS
```

The enumeration and sample valuations are finite checks, not proof for unbounded \(k\). The unrestricted claim is supported by the explicit 2-adic isometry and iterate-valuation argument in `RESULT.md`. No external proof system or independent audit was employed.
