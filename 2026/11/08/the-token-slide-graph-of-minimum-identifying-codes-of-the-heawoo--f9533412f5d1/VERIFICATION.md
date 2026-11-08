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

# Finite verification certificate

The graph has fourteen numbered vertices. Each certificate integer is a subset mask, with bit `v` indicating vertex `v`. All sets are **exactly** of size seven. `states.txt` lists all accepted masks in ascending order. `jumps.txt` lists each legal unordered replacement edge as two increasing integer masks; `slides.txt` is the subset in which the replaced vertices are adjacent in the original graph. There are no extra dependencies or compressed files.

From a directory containing the three text certificates and the two checkers, run:

```sh
python3 verify_python.py
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Successful executions print lines beginning `PYTHON_VERIFY_OK` and `CPP_VERIFY_OK`, respectively. Both checkers reconstruct the entire code set using the explicit Fano incidence relation, test the identifying condition for every candidate mask of size zero to seven, and verify every expected certificate row. They independently compute all connected components, degrees and shortest-path eccentricities. In particular, the 224-state jump component has eccentricity exactly six at each of its vertices. The Python checker uses set operations and combinations of cardinalities; the C++ checker uses integer neighbor masks and scans every mask from zero to 16383.

Proof dependence: the enumeration is exhaustive because every subset of a fourteen-element set appears in these finite loops. It is not an inferential statistical sample. The theorem's large-component distance spectrum and slide-star decomposition rely on this complete finite certificate, while the two 22-vertex cone structures also have a direct incidence argument. The checkers do not make claims for other graph orders or alternative identification conventions. No independent scholarly audit is claimed.
