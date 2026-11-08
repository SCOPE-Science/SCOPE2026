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

# Reproducibility of the stated graph theorem

`verify.py` uses no external Python packages. It reconstructs each expanded graph, independently lists all length-three cliques, and compares them with the complete forbidden-circuit list. It enumerates every nonempty face and computes exact binary simplicial ranks. The covered graphs are the one-edge graph, four-vertex path, four- and five-cycles, two disjoint edges, a five-vertex star, \(K_{2,3}\), a triangle, a triangle with a pendant vertex, and \(K_4\). For thirteen of the fourteen sample automorphisms it evaluates signed fixed faces by integral permutation signs, and also verifies the remaining sample; in total fourteen character checks. All checks pass and the output ends with `ALL_VERIFY_OK`.

The unrestricted mathematical proof, rather than the finite checks, establishes the theorem. The triangle-containing case is certified by a single explicit edge contraction followed by a cone collapse. The triangle-free branch uses the pointed-complex theorem, and the full top homology module uses orientation-twisted duality. The script verifies mod-two homology and integral signed Lefschetz traces in the finite examples, not all integral homology groups for all graphs, and it does not give a direct list of elementary collapses for each input graph.

The checked output is embedded as `VERIFY_OUTPUT.txt`; run `python3 verify.py` to reproduce it exactly.
