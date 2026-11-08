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
# Reproducibility and exact limits

Run `python3 heawood_dominance_verify.py`. The only prerequisite is a Python 3 standard library. The accompanying output file records one completed execution.

The verifier constructs the \(21\)-edge Fano incidence graph from cyclic differences, reconstructs the dominance faces both as complements of dominating sets and as subsets avoiding all closed graph neighborhoods, and checks agreement on all \(16,384\) subsets. It checks the exact face vector and all maximal faces. It constructs two discrete-Morse matchings by independent toggle orders and runs a full directed topological sort over all \(52,304\) face-cover incidences for each matching. Both matchings leave precisely one critical zero-cell and one critical six-cell.

For the integral generator it builds all \(128\) oriented facets of a sevenfold zero-sphere join, checks all signed boundary coefficients cancel, and proves that the all-point and all-line faces have no seven-dimensional cofaces. The coefficient-one evaluation supplies an integral primitivity witness; no finite-field-only inference is used. The verifier also enumerates all \(5,040\) point permutations to classify the \(168\) Fano collineations and checks the incidence-preserving duality and its orientation sign. This establishes the integral homology action of the full \(336\)-element automorphism group.

The homotopy conclusion invokes Forman's acyclic-matching theorem. Exhaustive verification concerns only the specified finite graph, not any infinite family. No independent external audit has been performed.
