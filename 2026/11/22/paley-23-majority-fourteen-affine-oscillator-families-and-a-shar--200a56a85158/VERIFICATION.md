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

The complete finite functional-graph calculation uses three executable checks from the actual embedded package. From the package root, run `g++ -std=c++17 -O3 verification/census.cpp -o census && ./census > verification/census.out`; this exhaustively visits all \(8{,}388{,}608\) states and computes the exact transient, cycle, and basin data. Run `g++ -std=c++17 -O3 verification/iterates.cpp -o iterates && ./iterates > verification/iterates.out`; its different Euler-criterion implementation independently verifies the exact time-resolved first-entry census and the universal identity \(F^{14}=F^{10}\), including sharpness. Then run `python3 verification/classes.py > verification/classes.out` for the exact 253-element affine-group partition, every class's basin size, half-complementarity of all cycles, and the four terminal-state classes.

All three programs were executed successfully on extracted delivered files. The expected final lines are `INDEPENDENT_ITERATES_OK` in the iterate output and `AFFINE_BASIN_CLASS_OK` in the affine-class output. The census outputs enumerate the actual recurrent cycles and terminal inputs; the independent iterate program checks the same time/period histogram without using that output. The proof is exhaustive for this finite network; it does not certify any other tournament order. Independent external mathematical audit: not performed.
