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

# Verification record

The exact mathematical domain is finite simple undirected root graphs of minimum degree at least two. The claim separates the all-order endpoint–forest equivalence, proved in `RESULT.md`, from the complete finite Petersen line-graph enumeration.

`verify_kneser.py` independently constructs \(P=\mathrm{KG}(5,2)\), then for every one of the \(32768\) edge-sensor masks compares (i) synchronous power domination on the fifteen-vertex line graph, (ii) original-graph induced forest via a disjoint-set data structure, and (iii) avoidance of the ten star and twelve pentagon maximal-failure masks. It fully enumerates all simple cycles and all minimum, inclusion-minimal and reconfiguration configurations. The full reproducible output is `kneser_verification.json`.

`verify_petersen.cpp` uses the outer pentagon, inner star and spokes as a separate Petersen representation. It performs complete synchronous propagation and forest tests for all \(32768\) masks and independently constructs the minimum-pair token-jumping and the budget \(2,3,4\) token-addition/removal component graphs.

Commands: `python3 verify_kneser.py` and `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_petersen.cpp -o checker && ./checker`. Programs were extracted and replayed from the final JSONL contents, rather than a previous build.

**Verified finite outputs:** no singleton power dominators; \(15\) optimum pairs; \(325\) successful triples with \(140\) inclusion-minimal; \(1305\) successful four-sets; all \(1645\) states up to cardinality four become connected under four-budget TAR. The optimum exchange graph consists of five triangles; three-budget TAR consists of five size-forty components plus 140 isolates.

**Limits:** These computations are exhaustive for exactly one fifteen-vertex graph, not for an infinite family. The general proof is textual and requires \(\delta(H)\ge2\). No external independent audit, external certification or automated formal proof is asserted.
