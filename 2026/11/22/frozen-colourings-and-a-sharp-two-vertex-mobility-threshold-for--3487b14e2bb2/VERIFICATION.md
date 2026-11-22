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

# Verification of the finite classification

The graph is specified by fourteen vertices, with Fano-incidence edges \(p_{i+d}\ell_i\) for \(d\in\{0,1,3\}\) modulo seven. Every edge has different closed endpoint neighbourhoods. The admissibility predicate checks properness and different four-bit colour signatures at all twenty-one edges. Exhaustively examining the complete set of named four-colour assignments establishes the exact state set; the search does not quotient by colour names.

`fano_lid_exact.cpp` uses partial-signature pruning with a proof of pruning soundness in `RESULT.md`, and builds its one-change and two-change graphs via base-four keys and disjoint-set unions. `lcf_lid_independent.cpp` uses a different fourteen-cycle plus chords, enumerates proper assignments recursively, applies the full signature test to complete assignments, and uses breadth-first search to obtain one-change components. It separately constructs the exact-two-change relation. The third file `isomorphism_check.py` validates the explicit vertex bijection and all twenty-one edges. In particular the independent enumeration counts 719,052 ordinary proper named four-colourings before the locally identifying filter, and 54,264 after it.

The scripts were compiled and run in the same directory from the packaged source, and their outputs matched `verification_output.txt`. Both agree on all support profiles, 185,808 one-change edges, 897,456 exact-two-change edges, and component size multiset \(6048\times1+8\times882+6\times6860\). The exact-two-change graph is connected. These are complete finite computations rather than simulations or tests of only representative assignments.

The four-colour minimum has a separate noncomputational proof by failure of Fano hypergraph two-colourability; the prior literature already implies that minimum. The new reconfiguration counts remain dependent on the validity of the included exhaustive algorithms, which have two independently implemented checks but have not undergone external validation. No unperformed checks are described as having passed.
