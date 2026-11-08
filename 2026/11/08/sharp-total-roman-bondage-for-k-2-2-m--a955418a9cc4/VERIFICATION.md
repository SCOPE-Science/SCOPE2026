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

Run `python3 verify.py` using Python 3.9 or newer. No third-party dependencies are required.

The checker builds each complete tripartite graph from labelled parts and checks every deleted-edge subset through cardinality three for \(m=2\), and through cardinality four for \(m=3,4\). Every remaining graph without isolated vertices must have at least one adjacent dominating edge. The complete search visits respectively \(299\), \(2517\), and \(6196\) subsets, including respectively \(299\), \(2514\), and \(6192\) isolate-free subsets. It then directly checks the displayed edge-deletion constructions for \(m=1,\ldots,50\), and independently enumerates total Roman labelings to confirm the baseline and increased weights for \(m=1,\ldots,5\).

Expected output:

```
EXHAUSTIVE_OBSTRUCTION_OK 2 299 299
EXHAUSTIVE_OBSTRUCTION_OK 3 2517 2514
EXHAUSTIVE_OBSTRUCTION_OK 4 6196 6192
EXPLICIT_DELETION_WITNESSES_OK m=1..50
DIRECT_TOTAL_ROMAN_OK 1 3 4
DIRECT_TOTAL_ROMAN_OK 2 4 5
DIRECT_TOTAL_ROMAN_OK 3 4 5
DIRECT_TOTAL_ROMAN_OK 4 4 5
DIRECT_TOTAL_ROMAN_OK 5 4 5
VERIFY_OK
```

The exhaustive cases are exact and finite. Extension to arbitrary \(m>4\) follows only after applying the four-representative reduction in the written proof. The additional finite upper-bound and label-enumeration checks are corroborative, not evidence of an unbounded exhaustive calculation. This is a reproducible self-review, not an independent audit.
