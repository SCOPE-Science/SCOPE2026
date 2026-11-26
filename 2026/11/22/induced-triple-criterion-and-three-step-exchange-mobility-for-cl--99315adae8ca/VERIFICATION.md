---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

The theorem has a direct proof in `RESULT.md`. The supplied checkers build the graph with XOR differences `1,2,4,8,15` and independently implement simultaneous power-domination closure for all 65,536 sensor sets. The checks relevant to this theorem are the failure counts `(1,16,120,240,60)` at sizes zero through four, no failures at larger sizes, the induced matching criterion at size four, the unique extension of each failed triple to a containing induced matching, and the at-most-one-wave bound for every successful placement. The wave count does not include initial closed-neighborhood observation. The programs also check exchange-graph facts that are not used for this theorem.

```sh
python3 verify_python.py
c++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The expected final lines begin `PYTHON_VERIFY_OK` and `CPP_VERIFY_OK`. These are exhaustive checks on this finite labelled graph, not a claim about other graphs.
