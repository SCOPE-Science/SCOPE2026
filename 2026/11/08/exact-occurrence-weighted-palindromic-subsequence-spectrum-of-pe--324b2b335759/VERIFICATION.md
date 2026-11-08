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

# Verification of the occurrence-weighted spectrum

Run the self-contained verifier with `python3 palindrome_embedding_verifier.py` from the extracted directory. Its direct search constructs every strictly increasing index subset of each small test word and independently checks the selected letters form a palindrome. It verifies 36 complete profiles over alphabet sizes \(q=2,3,4,5\) and several repetition counts (including reverse letter orders), comparing 314 individual length counts against the formula. It independently checks 2,992 coefficients of the claimed rational generating function through polynomial multiplication against the closed coefficients. It also checks the maximum length and maximum occurrence count for all tested profiles.

The source is included verbatim in this package and requires only the standard Python library. The comparisons are finite regression and boundary tests. The formal proof in `RESULT.md` is required for the full infinite-parameter claim. There is no independent audit or formal proof-assistant certificate.
