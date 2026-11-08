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

# Reproduction and limits

Run `python3 verify.py` using Python 3 and the standard library. It reconstructs the \(3\times4\) rectangular grid, enumerates exactly \(822\) nonempty matchings, and verifies an acyclic matching of \(406\) pairs with \(10\) critical simplices. It enumerates \(144{,}500\) nonempty barycentric face-poset chains, constructs each subgroup orbit chain group by canonicalizing under its actual edge permutation, checks \(d^2=0\), and computes every mod-two boundary rank using exact bit-vector Gaussian elimination. It independently calculates the signed Lefschetz traces on the original complex.

Expected final line: `ALL_VERIFY_OK`. The full successful output is `verification_output.txt`.

The finite computations directly prove only the finite combinatorial data. The mathematical proof uses acyclic discrete Morse theory, finite-group coinvariant exactness after inverting two, universal coefficients, Armstrong's orbit fundamental-group theorem, Hurewicz and the homological Whitehead theorem to derive the claimed integral homotopy equivalences. The checker does not independently certify general statements beyond this finite rectangle.

The geometric quotient is not the Borel construction and is not formed by naively taking vertex orbits of the original complex. Barycentric subdivision is necessary to obtain a no-inversions action with valid quotient cell boundaries. No external certificates or independent audit have been performed.
