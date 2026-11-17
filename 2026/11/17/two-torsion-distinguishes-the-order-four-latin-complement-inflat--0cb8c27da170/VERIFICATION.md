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
# Exact finite verification

The provided `verify.py` is a standalone Python 3 program requiring SymPy for integer Smith normal form. From the directory containing it run `python3 verify.py`. Compare its stdout to `verifier_output.txt`, which ends with `ALL EXACT CHECKS PASSED`. The program does not download data and does not depend on any previous computation, external certificate or unpublished package.

It enumerates all order-four Latin squares by finite row backtracking and every isotopic re-labelling of both representative tables. It constructs the full forty-eight-by-forty-eight signed triangle-to-edge boundary for each representative and computes its integer Smith normal form. It separately collapses a deterministic spanning tree of the one-skeleton, computes the triangle words in the free group on non-tree edges and applies exact elementary Tietze substitutions for each generator with a single occurrence in a cyclically reduced relator. The residual presentations are the trivial presentation (cyclic case) and a single generator with square relation (Klein case).

The two small group presentations and Smith computations are exact discrete mathematics, not statistical evidence or finite samples for an infinite theorem. Their verification depends on the soundness of the explicit algorithms and underlying Python/SymPy arithmetic; no independently trusted formal verification or independent mathematical audit is asserted. The general Hurewicz and Whitehead homotopy step is a paper proof, not a program output.
