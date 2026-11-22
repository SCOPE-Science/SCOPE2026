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

The accompanying standard-library `verify.py` enumerates finite labelled internal graphs, their forbidden \(q\)-clique neighborhoods, and small old-to-new adjacency assignments. It compares direct extension counts with the transfer weights and the exact critical-arity census.

Recorded checks:
- \((q,r)=(3,4)\): 63 permitted internal graphs; type counts \(63,958,14646\) for \(m=0,1,2\), with critical counts \((41,16,6)\).
- \((q,r)=(3,5)\): 958 internal graphs; totals \(958,27626\) for \(m=0,1\).
- \((q,r)=(3,6)\): 27626 internal graphs; totals \(27626,1486597\) for \(m=0,1\).
- \((q,r)=(4,5)\): 1023 internal graphs; totals \(1023,32596,1038902\), with critical counts \((958,55,10)\).
- \((q,r)=(5,6)\): 32767 internal graphs; totals \(32767,2096731\), with critical counts \((32596,156,15)\).

The script terminates in `ALL_FINITE_DIAGRAM_TESTS_PASS`. Its exhaustive ranges are finite and are not a substitute for the general combinatorial proof in RESULT.md. No independent scientific validation is claimed.
