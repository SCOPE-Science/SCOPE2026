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

# Reproducibility

Run `python3 -S verify_petersen_python.py`, `g++ -std=c++17 -O2 verify_petersen_cpp.cpp -o verify_cpp`, then `./verify_cpp`. Both were compiled/executed or invoked from the exact embedded sources and agree on all ten optimum sizes and counts. Each reconstructs all line-graph distances and 105 bisectors from the literal base Petersen edges and exhausts all 32768 vertex subsets. The Python program checks the 1365 eleven-subsets and equality of the six optimal complements with all six Petersen perfect matchings. Captured exact outputs are included for convenience; the proof does not depend on trusting output logs without code. The result is finite only and has not been externally independently audited.
