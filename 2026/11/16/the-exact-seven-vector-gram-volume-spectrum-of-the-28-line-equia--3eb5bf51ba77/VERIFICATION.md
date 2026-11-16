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

# Verification

The exact symbolic reduction and graph-component criterion are proved in RESULT.md. C++17 fraction-free determinants over all 1,184,040 distinct seven-edge selections returned counts 662760, 508896, 12096, and 288 for integer minor magnitudes 0, 4096, 8192 and 12288, respectively. A separately written Python graph enumeration returned 662760, 508896, 12096 and 288 for unsigned incidence determinant magnitudes 0, 2, 4 and 6. Both checks were executed successfully and their success assertions are embedded in the standalone files.

Run `g++ -std=c++17 -O2 verify_28frame.cpp -o verify_28frame && ./verify_28frame` followed by `python3 verify_graph_count.py`. The code itself enumerates the entire specified finite set; it is not a claim about unbounded dimensions, and it does not certify novelty or independent external validation.
