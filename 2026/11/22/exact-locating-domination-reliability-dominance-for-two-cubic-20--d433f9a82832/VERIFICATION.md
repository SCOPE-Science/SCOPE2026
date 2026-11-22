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

# Executable verification

Run `python3 checks/verify_python.py`; it reconstructs both cubic graphs from generalized Petersen edges, checks an explicit isomorphism from the Desargues \(\(GP(10,3)\)\) model to the two-subset-disjointness model, examines each of the \(2^{20}\) possible selected subsets separately for both graphs, and verifies all twenty-one coefficients. Expected marker: `PYTHON_EXACT_PASS`.

Compile `c++ -std=c++17 -O2 checks/verify_cpp.cpp -o verify_cpp` and run `./verify_cpp`. This constructs Desargues from disjoint pairs in a five-element set, the dodecahedral graph from its generalized Petersen edges, scans all twenty-bit integers for each graph, asserts all coefficients and their exact support comparison, and prints `CPP_EXACT_PASS`. The execution has no external data or package dependency.

Both checks were executed successfully with their complete assertions enabled. The enumerated predicate tests only nonempty and mutually distinct open-neighborhood signatures of the vertices **outside** the selected set, as required for ordinary locating domination. It does not inadvertently impose the identifying-code condition on selected vertices. The claimed reliability dominance follows algebraically from seven strictly positive coefficient differences and the Bernoulli subset probability. No infinite-family or probabilistic asymptotic statement is certified; the result is for two explicit finite graphs.

Independent scholarly audit: not performed.
