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

# Reproducible finite checks

Run `python3 check_quantum_cubic.py` in the same directory as the checker. The program uses only the standard library and constructs the original quantum multiplication table on the nine PBW monomials, not an assumed closed counting formula. It computes the ranks of all nine-by-nine left-multiplication operators and their squares by finite-field elimination. Over \(\mathbb F_4\), all \(4^8=65,536\) radical elements were checked exhaustively, and distinct principal right ideals were classified by the canonical row-reduced span of \(fA\); the dimension profile was \((0:1,1:1,2:5,3:20,4:16,6:20)\). Over \(\mathbb F_7\), every one of the \(7^6=117,649\) elements of \(J^2\) was checked. Additional nonzero-linear-part cases over \(\mathbb F_7\) and \(\mathbb F_{13}\) were tested deterministically. The exact result is recorded in `verification_output.txt`, ending with `QUANTUM_CUBIC_JORDAN_CENSUS_DIRECT_CHECK_OK`.

The checker supports only its three explicitly implemented finite fields. It does not exhaustively enumerate the full radical over \(\mathbb F_7\) or all elements over arbitrary fields. The proof in RESULT.md, not sampling, establishes the general theorem. Independent audit and validation have not been performed.
