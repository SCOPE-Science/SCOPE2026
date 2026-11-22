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

# Reproducibility and limits

The included executable `verify_book_chords.py` requires Python 3 and no external libraries. Run `python3 verify_book_chords.py` after extracting the file alongside the result document. It generates the full anchored vertex sets at each tested size, counts squared coordinate distances directly, and independently builds their predicted coefficient histogram by exact integer polynomial multiplication.

The checker tested \(786{,}420\) ordered vertex pairs for \(m=1,\ldots,8\) and integer coefficient identities through \(m=100\). Successful output reads `BOOK_CHORD_SPECTRUM_PASS ordered_pair_tests= 786420 symbolic_dimensions=100`. These computations are finite consistency checks only. The all-dimensional proof is the slice-vertex classification, factorization of the polynomial, and standard independent-variable limit theorems. No machine-checked infinite proof or independent mathematical audit is claimed.
