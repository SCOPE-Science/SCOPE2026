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

# Verification and scope

A portable Python 3 standard-library-only checker accompanies the theorem. Execute `python3 checker.py` after extracting both this document and the checker into the same directory. It derives coloured-word rank types recursively and compares their small cases with a separately implemented two-sided Ehrenfeucht–Fraïssé game, including equality, order and unary letter preservation. It checks 2,883 pairwise game cases, all binary word types up to length eight at ranks one to three, the sharp monochromatic thresholds at ranks one to six through length 64, and the even-length language's sharp finite horizon formula through \(N=63\).

Successful output: `SHARP_FO_WORD_HORIZON_CHECKS_OK direct_game_comparisons= 2883 binary_word_lengths_through= 8 unary_lengths_through= 64 verified_ranks=1..6`.

Finite enumeration cannot establish an infinite theorem. The proof is the middle-point induction and the long-order interval game in `RESULT.md`. Independent audit has not been performed; no external proof certification is claimed.
