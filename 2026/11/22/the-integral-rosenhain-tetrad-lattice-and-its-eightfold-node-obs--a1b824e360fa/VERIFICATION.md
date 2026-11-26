---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the usual geometric Rosenhain tetrads in characteristic not two, the enumeration is complete: of the 35 binary two-dimensional linear subspaces, 15 are isotropic, and each of the other 20 has four cosets. The four coordinate sums vanish modulo two on every affine plane, while the second difference of the displayed quadratic refinement equals the symplectic pairing, hence has sum one on each nonisotropic plane. This proves inclusion in the stated mod-eight and parity kernel. The zero node and the four differences of coordinate nodes from zero generate the target of order 128. I independently filtered all 1,820 four-subsets by zero XOR and nonisotropic direction, obtained all 80 rows (matching the CSV including its selected rows), computed the signed minor +128 and obtained the full integer Smith list 1^11, 2^4, 8. Inclusion and the equality of indices prove the exact criterion. The first coordinate of each basis image is odd, giving order eight for every node. The claim concerns formal coefficients, not a quotient of divisor classes.

## originality

PASS

Best of current knowledge, the supported distinct claim is the integral span and coupled order-eight obstruction of the 80 nonisotropic tetrads. The underlying configuration is classical. The strongest indexed analog uses complementary, isotropic directions and has exponent four; the matching index is not matching lattice information.

## value

PASS

The 80 generators are the complete canonical nonisotropic incidence family on the Kummer node set. Researchers using integral combinations can now decide membership by five explicit moments and know the optimal coefficient for reconstructing any node. Rank, binary parity and even knowledge of the index alone would miss the coupled order-eight obstruction, and the complementary Göpel lattice of the same index has a genuinely different exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
