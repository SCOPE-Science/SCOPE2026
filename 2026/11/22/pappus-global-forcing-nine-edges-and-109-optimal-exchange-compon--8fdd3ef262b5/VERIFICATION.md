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

The theorem is an exact finite statement about a labelled graph of eighteen vertices and twenty-seven edges. Four standalone programs were run from their delivered source texts, and their outputs reproduced the embedded reference files.

- `verify_affine.cpp`: builds the affine-incidence graph, exhausts \(\binom{27}{k}\) subsets for each \(1\le k\le9\), checks all \(861\) perfect-matching-pair symmetric differences, enumerates every optimum single-edge exchange, verifies the 109 component decomposition and all 108 two-replacement bridges.
- `verify_lcf.cpp`: uses a separate Hamiltonian LCF graph presentation, independently enumerates the \(42\) matchings, checks raw observation signatures, reconstructs the exchange graph and all component and bridge assertions.
- `verify_nice_cycles.py`: enumerates perfect matchings by permutations of line endpoints, generates all alternating-cycle components, verifies the 603-cycle size histogram, and checks equivalence of the two forcing predicates for 10,000 deterministic masks. The finite loop checks are not used as substitutes for the general equivalence proof.
- `verify_isomorphism.py`: verifies an explicitly supplied eighteen-vertex bijection between the affine and LCF graph encodings and checks preservation of all 27 edges.

Both C++ programs search all smaller cardinalities without sampling and agree on the numerical conclusions. The result concerns only \(P\); it does not certify any other graph or priority of publication. Independent scholarly assessment remains unperformed.
