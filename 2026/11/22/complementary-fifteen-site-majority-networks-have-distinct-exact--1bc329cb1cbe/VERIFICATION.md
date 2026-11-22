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

The labelled vertex set is the lexicographically indexed set of fifteen edges of \(K_6\). Both graphs and their transition functions are defined in `RESULT.md` and constructed from first principles in the standalone scripts.

`python3 verify_iterates.py` directly enumerates every one of the \(32768\) input states for both graphs, checks \(F^5=F^3\), finds the exact first periodic-entry time and least period, and derives every individual attractor basin from the minimum representative of its terminal orbit. It asserts the complete first-entry histogram and basin-size spectra.

`c++ -O2 -std=c++17 verify_paths.cpp -o verify_paths && ./verify_paths` independently constructs neighbor lists, traverses the functional digraph and discovers all cycles and predecessor paths. It separately asserts the histograms and the maximum entrance depth three.

Both scripts were run from their actual source files with all checks passing. Exact integer arithmetic is used throughout; there are no random samples. Their independence is algorithmic (iterate equality versus graph-cycle traversal), not external peer review. The result is limited to two fifteen-vertex graphs. No conclusion is claimed for arbitrary orders or different update conventions.
