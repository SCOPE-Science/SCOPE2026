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
# Reproducibility of exact finite checks

Run `python3 verify_crown.py` from the directory containing this file. The program requires Python 3 and the standard library only. For each integer \(4\le n\le8\), it constructs the graph from the deleted-perfect-matching adjacency rule, independently simulates the usual power-domination observation and forcing process for all \(2^{2n}\) vertex subsets, checks the exact shore-support characterization, derives both coefficient arrays and the minimal-set counts from direct enumeration, and uses explicit graph traversal to count all TAR components for budgets from \(2\) to \(n\). Every test is an assert-fail on disagreement.

Observed result:

```
CHECK n=4 powersets=256 PDS=247 minimal=28 TAR_tests=3
CHECK n=5 powersets=1024 PDS=993 minimal=45 TAR_tests=4
CHECK n=6 powersets=4096 PDS=4013 minimal=66 TAR_tests=5
CHECK n=7 powersets=16384 PDS=16187 minimal=91 TAR_tests=6
CHECK n=8 powersets=65536 PDS=65099 minimal=120 TAR_tests=7
VERIFY_OK orders=4..8 subsets=87296 power_dominating=86539 minimal=350 TAR_cases=25 exact_polynomials=PASS exact_components=PASS
```

The unrestricted theorem is proved by the explicit neighbor-count and TAR-path arguments in `RESULT.md`. Finite experiments alone do not prove it for arbitrary \(n\). No claim of independent mathematical certification is made.
