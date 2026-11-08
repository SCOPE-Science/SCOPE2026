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

# Reproduction and logical scope

Run `python3 verify.py` from the extracted files. No nonstandard packages are needed. It directly builds the set of distinct subsequences of each prefix and tests the palindrome property, then compares the complete length profiles to the closed finite formula. It also greedily scans the periodic host for each tested palindrome and compares the first matching prefix with its claimed minimum. Checks completed successfully on 56 prefixes, 430 length cells and 1915 greedy minima. These finite checks are supplementary to the proof of all \(q\ge3\) and all lengths in `RESULT.md`.

All mathematical assumptions are stated in `RESULT.md`. There is no numerical or external certificate whose data are needed to close the proof; no independence claim is made. A human bibliographic and mathematical review has not been performed.
