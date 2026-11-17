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

# Verification and reproducibility

The exact, fully reproducible finite check uses the two included programs and the two included output files. In a C++17 environment, run `g++ -O3 -std=c++17 check_all_edges.cpp -o check_all_edges` followed by `./check_all_edges`; this calculates the baseline and **all 38 edge deletions**, using \(524288\) labelled states per graph. In a Python environment with NumPy and NetworkX, run `python independent_numpy.py`; this independently verifies four-regularity, girth five, the 24 graph automorphisms, the four edge-orbit multiplicities and the five representative dynamical censuses.

The C++ checker recomputes every successor via integer bit masks, validates every initial state has reached a fixed state or two-cycle by the reported time, calculates the last nonempty first-entry bin and directly tests eventual unanimity for every initial state. It computes complete results for all edge deletions, without deducing their values from automorphisms.

The Python checker independently constructs the graph with separate neighbor data and computes an array successor map using NumPy vectorization, determines first-entry times for all states, and verifies the edge-orbit partition from a graph isomorphism iterator. The row counts and all four representative classes agree with the C++ output. The implementation is exact finite arithmetic; neither random sampling nor floating-point inference is used. Computational proof of the displayed finite census rests on inspecting and executing the source code, not on treating the output logs alone as a proof.

The general result of eventual period at most two on symmetric threshold systems is credited to Goles and Olivos; the present computational checks establish the sharper *specific* entry times and counts. No external or independent mathematical certification has been performed.
