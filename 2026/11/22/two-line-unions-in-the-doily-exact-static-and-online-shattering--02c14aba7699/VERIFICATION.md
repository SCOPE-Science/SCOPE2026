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
# Verification and limits

The mathematical proof and its exact finite certificates are in `RESULT.md`. Run `python3 verify_symplectic.py` and `python3 verify_orbits.py`; compile `verify_matchings.cpp` with C++17 and execute it. The two independent incidence models must both give the polynomial \(1+15z+105z^2+375z^3+495z^4\), 15 triangular facets, reduced mod-two Betti ranks \((0,0,15,226)\), and Littlestone dimension \(5\).

`depth5_tree.json` is separately tested for 31 nonterminal query nodes and 32 consistent, pairwise distinct leaf hypotheses. All 15 five-point symmetry orbits have fewer than 32 traces; the two complete verifiers also check every five-point subset without using symmetry. The highest boundary rank uses exact arithmetic over \(\mathbb F_2\), not numerical eigenvalues.

No assertion about integral torsion, homotopy equivalence, extension to other generalized quadrangles or independent external auditing is supported by the finite evidence.
