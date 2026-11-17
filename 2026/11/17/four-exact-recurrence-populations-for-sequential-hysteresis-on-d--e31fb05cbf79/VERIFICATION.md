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

The two verification programs work from the completely stated sequential bit-update rule. `verification/profile_certificate.py` independently traces recurrent count profiles and sums the exact binomial multiplicities for all 1,600 ordered parameter pairs between one and forty. It separately checks all sixteen uniform cases in each of four symbolic threshold regimes. Its recorded output is `verification/profile_output.txt`.

`verification/independent_exhaustive.cpp` independently enumerates the entire labelled binary functional graph for each of 75 ordered pairs with \(1\le a,b\le9\) and total vertices at most seventeen. It strips transient vertices via indegree elimination, follows all remaining cycles and compares actual least-period populations with the theorem. Its recorded output is `verification/independent_output.txt`.

Commands:
```
python3 verification/profile_certificate.py
g++ -std=c++17 -O2 -Wall -Wextra verification/independent_exhaustive.cpp -o check_full
./check_full
```

The computations are finite cross-checks and do not alone establish the all-size theorem. The proof in `RESULT.md` independently reduces all recurrent orbits to three hub-status cases and a complete sixteen-state uniform finite test covering all arm sizes.
