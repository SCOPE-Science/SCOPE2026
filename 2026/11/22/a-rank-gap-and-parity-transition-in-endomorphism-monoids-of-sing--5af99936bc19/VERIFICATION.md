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

# Verification of the endomorphism classification

The all-field argument is contained in RESULT.md, Proof Steps 1–5, starting from the original basis multiplication identity. The standalone Python 3 program `verify_cayley_loop_endomorphisms.py` uses independent finite-field arithmetic and directly tests multiplicativity rather than applying the claimed classification to filter candidates.

Execute `python3 verify_cayley_loop_endomorphisms.py` in a directory containing the embedded program. It exhaustively checks the entire space of 512, 65,536 and 262,144 linear maps for the examples of dimensions three and four over the binary field and dimension three over the field of order four. Exactly 5, 6 and 7 maps pass, respectively. The last printed line is `CYCLIC_CAYLEY_ENDOMORPHISMS_VERIFIED`. Additional direct composition checks examine all classified maps in dimensions 3–6 over the binary field.

These checks are finite and neither prove the all-dimensional result nor establish publication priority. The proof uses the kernel of \(I+S\), coordinatewise support dichotomy, characteristic-two injectivity of the squaring map, and the cyclic square relations; algebra-ideal splitting follows from the unique square-zero line and the coordinate-sum quotient. The scope is characteristic two with cycle length at least three. Independent validation has not been performed.
