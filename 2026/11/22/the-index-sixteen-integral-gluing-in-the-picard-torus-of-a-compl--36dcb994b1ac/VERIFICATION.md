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
# Exact verification

Run `python3 verify_quadrangle.py` with Python 3.10+ and SymPy 1.12+ in a directory containing the standalone file. The program constructs the six line labels, three diagonal pair partitions, thirteen graph vertices, eighteen oriented branches, and an exact integral six-cycle basis. It checks every permutation's signed chain action and all pairwise group-composition identities. The three primitive rank-two Klein-four eigenlattices are explicitly recomputed and checked to form an index-sixteen quotient of exponent two, and all five finite-field Frobenius normal forms are certified by determinant-one-or-minus-one changes of basis. Integer Smith forms are also checked for seven finite values as auxiliary regression tests, not as a universal proof. The rational-point formulas follow from exact fixed-line/branch/singularity counts. The complete successful output is included as `checker_output.txt`.

## Limits
No inspection or replay of any earlier or separate result constitutes evidence for this claim. No independent validation is performed; underlying general Picard theory and classical projective geometry are cited in RESULT.md. The result does not assert novelty of the general normalization method or the abstract correspondence of integral character lattices and finite-field tori.
