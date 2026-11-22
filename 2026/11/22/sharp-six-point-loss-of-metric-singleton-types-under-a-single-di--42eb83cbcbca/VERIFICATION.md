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

# Verification scope

The finite checker `artifacts/verify.cpp` is complete over every distance assignment on \(n=2,3,4,5,6\) labelled parameter points with marked pair \((0,1)\) initially at distance one. It verifies every triangle inequality before and after the prescribed change and counts all possible new-point labels with integer arithmetic using the proved independent-support formula. It also checks each six-point negative instance against the two-shore shape and counts its internal two-distance signatures. The output `artifacts/verified_output.txt` records the exact totals.

Compile and run in the extracted package root:

```
g++ -O2 -std=c++17 artifacts/verify.cpp -o verify
./verify
python3 artifacts/verify.py
```

The independent Python program directly tests all \(3^6\) new-point distance vectors for each of three explicit six-point representative metrics, checking both full metric triangle conditions and the conditional defect classes. Both programs completed with `VERIFY_OK` when executed from the packaged sources. The proof of the infinite two-shore family is the explicit all-parameter count in `RESULT.md`; no finite verification certifies an infinite statement by itself.

The first-five-point sharpness and six-point exhaustive classification use integer enumeration only, without random sampling or floating-point tolerances. The result does not enumerate all higher-order metrics or assert independent historical novelty certification. Independent audit: not yet performed.
