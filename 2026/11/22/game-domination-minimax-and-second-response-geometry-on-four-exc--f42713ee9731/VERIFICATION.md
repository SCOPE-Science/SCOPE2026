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

# Finite minimax certificate and checks

The total dominated set is sufficient game state, because any legal move has to dominate at least one new vertex; no previously chosen vertex has such an effect. The `RESULT.md` proof gives the exact topologically ordered recurrence. Both verification files compute the same four graph models from independent descriptions and use exact integer arithmetic, with no network, solvers or numerical tolerances.

Execution in the delivered package's source directory:

```
python3 verify_minimax.py

g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_minimax.cpp -o verify_minimax
./verify_minimax
```

Both were executed successfully and printed `PYTHON_VERIFICATION_OK` and `CPP_VERIFICATION_OK`, respectively. The independent checkers agree on all 4 start pairs and the conditional second-response counts, including all anomalous distance-three categories. The Python program additionally checks every possible opening vertex, without assuming vertex transitivity. The C++ program computes *every* dominated-set mask bottom-up; unvisited masks are still computed to prevent reliance on a sampled state graph. See `NUMERICAL_CERTIFICATE.json` for exact structured expected results.

The finite proof depends only on the explicit graph constructions, the elementary game recurrence, exhaustive evaluation of each finite state mask, and the comparison of exact outputs. An unreachable mask in the C++ table is harmless; it is not an unproved case. This does not assert independent scientific validation or priority certification.
