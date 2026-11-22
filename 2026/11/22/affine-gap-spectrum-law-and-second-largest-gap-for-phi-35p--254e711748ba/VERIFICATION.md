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

# Exact reproducibility

Place `word_gaps_verify.py` beside `gap_spectrum_35.csv`; run `python3 word_gaps_verify.py` using the Python standard library. The program regenerates all 576 tabulated histogram entries using periodic coefficient words, and compares them byte-independent numerically against the CSV. It also checks that all 576 words have support, verifies every unit residue's second-largest-gap value and multiplicity, and checks quotient-divisibility identities plus full coefficient and histogram equality for the 72 values \(35q+r\), where \(q=1,2,3\) and \(r\) ranges over all 24 units. The run passed.

The exhaustive domain of the finite certificate is the 24 unit residues modulo 35. Infinite dependence on quotient \(q\) follows separately from the exact coefficient-word period-insertion proof, not from testing three sample quotient values. Neither originality nor mathematical peer certification is automated by this checker; independent audit has not been performed.
