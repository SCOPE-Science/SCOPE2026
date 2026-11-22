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

The finite computation can be repeated with `python3 verify.py` and `g++ -std=c++17 -O2 verify.cpp -o verify_bin && ./verify_bin`. Both implementations were independently executed against the included source files. They reproduce the full census, all-source distance distributions, Hamming pair counts and the distinct exactly-six and exactly-eight flip structures. `CHECKS.txt` records the observed outputs. The mathematical proof also uses published static blocking-set classifications, with the complete direct verification supplying a separate check of the static premise. There is no assertion of an independent external audit, generalized-order certification, or novelty beyond the specific stated result.
