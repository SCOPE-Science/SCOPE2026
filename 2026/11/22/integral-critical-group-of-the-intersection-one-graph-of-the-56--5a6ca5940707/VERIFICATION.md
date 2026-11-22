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
# Reproduction and limitations

Run `python3 verify.py` with Python 3 and no third-party dependencies. The implementation reconstructs all 56 exceptional divisor classes, their pairwise intersections, the complete distance-two relation to the ordinary Gosset graph, and the Geiser pairing. It asserts the full Gram-matrix identity and computes the reduced Laplacian determinant by exact fraction-free elimination. It then computes the full Smith valuation spectra modulo \(2^{12}\), \(3^{10}\), and \(7^8\), independently for deleted vertices 0, 17, and 55, and checks that these agree.

The factorization of the determinant follows separately from the Laplacian spectrum and the matrix-tree theorem, so the program verifies both the integral invariant factors and the required determinant consistency. Every modular pivot valuation is below the modulus precision and the sum of valuations equals the exact determinant valuation, ruling out unaccounted higher exponents. The program checks all 56 geometric vertices, not a random sample.

Expected completion marker: `DEGREE_TWO_DEL_PEZZO_INTERSECTION_ONE_CRITICAL_GROUP_VERIFIED_OK`.

Scope: characteristic-zero smooth degree-two del Pezzo surfaces, and the unweighted graph of intersection-one exceptional curves only. The code is an exact verification of a finite universally shared graph; it is not an external proof of historical priority or an independent mathematical audit.
