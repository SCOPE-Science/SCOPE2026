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
# Computational checks and proof boundaries

The main claim is a theorem for all nonempty finite simple graphs (static support criterion and rank dichotomy) and all positive path lengths (exact dimensions). It is proved in `RESULT.md`, independently of finite computation.

Run from the directory containing these files:

```sh
python3 check_parity.py

g++ -O2 -std=c++17 check_parity.cpp -o parity_checker
./parity_checker
```

The Python verifier constructs both parity classes for path orders 1–16, independently computes exact Littlestone ranks by complete version-space splits, and uses direct trace enumeration at orders 1–12 to check the private-neighbor criterion. It also tests that criterion on every labeled simple graph of orders 1–5 (1,099 graphs total), for both parities and every support. The C++ verifier independently reconstructs the hypothesis family and enumerates every support trace and complete online split at path orders 1–12. The recorded stdout in `check_python.txt` and `check_cpp.txt` is from successful executions of those code files. The boundary cases n=1,2,3,4 are explicitly checked.

A finite program cannot certify the unbounded graph and path statements. Those statements depend on the parity-correction lemma, the universal maximum-independent-set bound, and the exact endpoint recursion proved in the result. No external audit or machine-checked infinite proof has been performed.
