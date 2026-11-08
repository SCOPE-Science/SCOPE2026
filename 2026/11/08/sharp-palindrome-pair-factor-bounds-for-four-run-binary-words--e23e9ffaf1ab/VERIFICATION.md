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
# Reproduction and scope

Run `python verify.py` using a standard Python 3 interpreter. The program enumerates 1,470 binary words with at most four runs through length 14, independently tests all distinct substring palindrome-pair decompositions, and checks the explicit three-/four-run counts. It then examines 395,010 positive quadruples of total lengths four through 57, checking the sharp maxima and all 223 predicted equality quadruples for lengths at least eight. Expected exact output: `VERIFY_OK direct_words=1470 run_quadruples=395010 extremizers=223 range_n=1..57`.

These are finite reproducibility checks, not proofs for all lengths. The all-length proof rests instead on the exact four-run factor-category count and the four disjoint cases with balancing inequalities provided in `RESULT.md`. The unrestricted five-or-more-run problem is not decided here.
