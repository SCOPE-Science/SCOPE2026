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

The standalone standard-library Python program `verify_icosahedral_cut_transition.py` constructs the graph from a complete explicit edge list, tests every vertex subset for cut-complex membership by two methods, contracts signed integral simplicial chain complexes using only unit pivots, verifies residual chain identities, and computes a nonzero mod-two inclusion map by exact bitset reduction.

Running `python verify_icosahedral_cut_transition.py > verification_output.json` produces the embedded output. It establishes 638 integer unit cancellations and a zero residual boundary for the six-cut complex; 1293 integer unit cancellations and one residual coefficient 2 for the five-cut complex; and one explicit 44-term cycle whose inclusion is not nullhomologous modulo two.

These are finite exhaustive checks on 12 labeled vertices. The passage from the nonzero field map to integral surjectivity uses the universal coefficient theorem and the independently established absence of degree-three torsion. The certificate does not assert a homotopy wedge decomposition or independent audit.
