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

# Computational verification and boundaries

The reproducibility programs `verify_direct.py` and `verify_structural.py` use only the Python standard library. Reproduce their recorded outputs with `python3 verify_direct.py` and `python3 verify_structural.py` in the same directory. `verify_direct.py` enumerates subsets of the **actual** balanced crown graph, computes and tests closed-neighborhood identifying codes, and builds slide edges. It checks \(n=5\) through 9; the \(n=6\) components have every expected bipartite edge. `verify_structural.py` independently implements the partial-transversal ternary model, BFS component structure and edges for \(n=5\) through 12, and explicit legal path constructions over random pairs in the connected regime. Both output files are included and end in PASS. The two implementations do not share a graph generator.

The infinite-family connectedness is established by the mathematical proof in RESULT.md, not by finite computation. No machine-checked proof, unpublished source, or independent scholarly audit is claimed. Historical priority may be affected by the inaccessible 2020 article body.
