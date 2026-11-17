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

## Reproducibility checks

Run `python3 verify_punctured_rook.py` to build each literal adjacency matrix and test 12 exact kernel dimensions and sharp order 72 on five punctured boards. The 60 successful comparisons and graphs are recorded in `verify_punctured_rook.out`.

Run `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` to reproduce 3,400 deterministic-seed vertex-level trajectories from four punctured boards; recorded output is in `verify_direct.out`. These state samples check predicted orders, not every possible configuration. The decomposition in `RESULT.md` proves the all-size formula.

Neither check constitutes independent review or an external audit. The exact field assumption is characteristic three; numerical checks use the prime field only, and extension-field validity follows from base change of the proven matrices.
