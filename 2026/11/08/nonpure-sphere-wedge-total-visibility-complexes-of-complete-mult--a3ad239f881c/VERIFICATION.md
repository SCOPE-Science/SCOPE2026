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

# Verification and reproducibility

Execute `python verify.py` using Python 3 with only the standard library. The script independently constructs the graphs from their part-size vectors; computes shortest-path distances while forbidding selected internal vertices, rather than using the closed formula to test visibility; tests every vertex subset; determines inclusion-maximal faces; compares two polynomial coefficient vectors; checks basis exchange of maximal faces in all-non-singleton cases; and evaluates reduced simplicial mod-two homology on small complexes.

Observed output:

```text
VERIFY_OK profiles=88 subsets=10764 facets=804 direct_BFS=PASS face_polynomials=PASS maximal_facets=PASS matroid_basis_exchange=5200 homology_mod2_cases=64 PASS
```

The tested profiles include two, three and four partite classes, mixtures of singleton and non-singleton classes and cases with no singleton parts. Some two-part cases are included as independent boundary cross-checks, although the mathematical claim restricts to at least three parts. The homology computation is over the field with two elements and covers only finite examples; it neither proves integral torsion-freeness nor proves an infinite family. Those claims follow from the matroid shellability theorem and the explicit suspension equivalence in the mathematical proof. The verifier is not an independent audit.
