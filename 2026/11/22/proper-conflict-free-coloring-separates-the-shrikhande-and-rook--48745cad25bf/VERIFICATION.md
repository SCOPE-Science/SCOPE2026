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

# Reproducibility and limits

From this folder, run `python3 check_coloring.py`. A second implementation can be compiled using `c++ -O2 -std=c++17 check_independent.cpp -o check_independent` and executed as `./check_independent`.

The Python checker verifies all fifteen nonzero differences of the Shrikhande step-set difference multiset, graph regularity, two common neighbors for every distinct pair, the structural local-neighborhood distinction, the proper edge-color restrictions and exactly-once open-neighborhood color occurrences. The C++ implementation independently rebuilds both graphs and checks the degree/common-neighbor/color certificates.

The nonexistence of smaller proper conflict-free colorings is established by the mathematical inequalities and palette argument in `RESULT.md`, not by extrapolating from finite search. The checks do not establish historical originality, graph-family generalizations, or third-party independent validation.
