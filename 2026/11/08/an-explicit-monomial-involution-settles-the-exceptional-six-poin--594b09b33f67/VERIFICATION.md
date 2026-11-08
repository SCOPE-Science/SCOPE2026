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

# Executable exact checks

The reproducible program `verify_equivalence.py` uses Python's standard library, implementing \(\mathbb F_8\) as \(\mathbb F_2[\alpha]/(\alpha^3+\alpha+1)\). It builds the full length-\(49\) generator matrices using the exact lattice-point lists, confirms dimension six for both, constructs the permutation \(\phi(x,y)=(x^{-1},x^{-3}y)\) and nonzero weight \(x^3\), checks the permutation of all \(49\) coordinates is bijective, and validates the pointwise row identity with reversal of the four polynomial coefficients. Run `python3 verify_equivalence.py` from the extracted package. Its successful recorded stdout appears in `verification_output.txt` with final line `VERIFY_OK`.

These checks are exhaustive for the particular \(49\) torus coordinates; no heuristic or sampled comparison is involved. The main theorem also has a shorter standalone symbolic proof: on \(\mathbb F_8^*\), \(x^7=1\), so \(x^3(x^{-3}y)^{-1}=x^6y^{-1}=x^{-1}y^{-1}\). The row-coefficient reversal is invertible. An exact test for finite field size eight is not a claim about other ground fields. Independent scientific audit has not been performed.
