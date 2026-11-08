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

# Direct verification and limitations

The bundled `checker.py` requires only Python 3 and constructs the truncated positive Witt bracket explicitly, rather than reading any precomputed tables. Run `python3 checker.py` and compare the output with `checker_output.txt`.

The exhaustive prime-field tests cover all 125 elements over \(\mathbb F_5\) for ordered commuting pairs and, through full adjacency intersections, all ordered commuting triples and quadruples. Separately, all two-dimensional subspaces of the three-dimensional Lie algebra are enumerated as canonical reduced-row-echelon bases and checked for abelianness. A second full direct commutator-rank census covers all 16,807 elements over \(\mathbb F_7\). Integer Gaussian identities are cross-checked for \(p\in\{5,7,11\}\), \(r\in\{2,3,4\}\). These finite checks cannot certify unbounded prime, extension-degree, or tuple-arity quantifiers. The independent mathematical audit has not been performed.

The general result follows from the explicit centralizer and subspace-count proof in `RESULT.md`. No unsupported claim that an inaccessible related source is noncovering is made.
