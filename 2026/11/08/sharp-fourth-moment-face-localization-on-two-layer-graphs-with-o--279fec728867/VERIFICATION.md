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

# Reproducible exact checks

Run `python3 verify.py` with a standard Python 3 installation. The script uses rational arithmetic, no external libraries or files, and produces `ALL_OVERLAPPING_SQUARE_PRISM_CHECKS_PASSED` on success. It checks the universal algebraic deficit identity on 200 exact coefficient families, directly enumerates all independent signs in 20 small prism tests, checks 87,369 nonzero integer path profiles of the key positive-part lemma, and checks each square extremizer and the opposing sign.

Only finitely many examples are computationally checked. The proof in RESULT.md establishes the universal moment bound and all equality cases for every admissible finite base graph. The relative-publication novelty comparison remains subject to ordinary bibliographic limitations; independent audit has not been performed.
