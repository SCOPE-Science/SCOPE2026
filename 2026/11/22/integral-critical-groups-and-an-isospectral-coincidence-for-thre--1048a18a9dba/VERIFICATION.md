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

# Computational verification and limitations

The standalone `verify.py` script reconstructs each graph directly from the source's nineteen labeled triples. The nine ordinary double points are obtained as the complement of the fifty-seven used pairs among the sixty-six unordered line pairs. Each exceptional component contributes exactly three graph edges.

For each 30-by-30 reduced Laplacian, the checker computes the exact Bareiss determinant and compares it with three-root cofactor calculations and the independently derived eleven-line-vertex Schur determinant. It then performs elementary row and column operations over the finite local ring \(\mathbb Z/p^9\mathbb Z\) for the primes \(2,3,5,7,61,307\), checks the complete multiplicity lists, and verifies the reconstructed invariant-factor orders. The optional SymPy comparison uses the integer Smith normal form on three different root deletions and recomputes both characteristic polynomials and prime factorization. Optional NetworkX checks verify pairwise nonisomorphism and automorphism-group orders.

Expected final output: `ORCHARD_B12_C2_C7_EXACT_INTEGRAL_COMPONENT_GROUPS_OK`. All checks succeeded for the embedded script before review, including both optional libraries. `certificates/smith_data.json` contains the numerical certificates and their finite scope. No finite calculation is being used as a substitute for any asserted all-degree or all-characteristic theorem: this is an exact computation for precisely three specified finite graphs.

The Néron interpretation is conditional on a proper regular split semistable smoothing with unit node thickness. There is no assertion about arbitrary smoothings or ground-field twists. No independent audit has been performed.
