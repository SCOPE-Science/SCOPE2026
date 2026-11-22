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

# Reproducibility of the graph critical group

The attached `verify_desargues_boundary.py` is a stand-alone Python 3 program requiring no third-party packages. Run `python3 verify_desargues_boundary.py` in the same directory as these files. The output must conclude `DESARGUES_STABLE_BOUNDARY_CRITICAL_GROUP_OK`.

It constructs all ten two-subsets and ten three-subsets of a five-element set, adds the thirty incidence edges and fifteen complementary Petersen edges, and verifies the resulting Laplacian and degree counts. It then uses invertible local-ring pivot operations to derive the Smith valuations separately at primes \(2,3,5,7\), for both an exceptional-component and a line-component deleted vertex. Its determinant target comes from an independent spectral identity presented in the proof, rather than from a generic determinant subroutine. Every local valuation is checked against the claimed global invariant factors, including determinant exponents.

The calculation establishes the finite graph statement. The use of algebraic geometry also assumes the classical realizable Desargues line configuration and Raynaud's component-group theorem for regular semistable unit-thickness smoothings. The code does not independently reconstruct a projective-coordinate realization or a family of smooth algebraic curves, nor does it replace these cited theorems. The cited classification literature is the source for those geometric premises.
