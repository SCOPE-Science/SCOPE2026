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

# Reproduction and scientific limits

Run `python3 verify_cubic.py` using Python's standard library. The expected deterministic output is in `verification_output.txt`, with final marker `CUBIC_EXTERIOR_DIRECT_GF2_PASS`.

The script implements exterior monomial multiplication directly over \(\mathbb F_2\). It exhaustively enumerates \(2^{20}=1,048,576\) six-generator cubic coefficients to obtain the complete distribution of ranks of the degree-one annihilator map, and checks all nonzero possible multiplication-rank profiles in that dimension against the theorem. For canonical divisible cubics, it separately checks the full graded multiplication-rank profiles in dimensions \(5,6,7,8\), covering every admissible alternating rank for those dimensions. It uses no scientific packages or external downloaded data.

The all-dimension rank polynomial, finite-field counts for every even prime power, and geometric assertions are proved in `RESULT.md` from a splitting lemma, alternating-form normal form, Künneth rank identity, Gaussian counting and a projective incidence bundle; the finite checks do not certify the infinite statements. Historical priority has not undergone independent exhaustive verification; the classical binary six-dimensional orbit counts are not claimed as new. External independent audit has not been performed.
