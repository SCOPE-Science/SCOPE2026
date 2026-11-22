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

Run `python3 verify.py` from this package. This Python-standard-library verifier (i) enumerates distinct two-deletion descendants from every even palindrome in the stated finite parameter ranges, (ii) independently reconstructs all candidate palindrome parents from each possible receiver using the two-branch decoder, (iii) checks equality of all inverse sets, including empty sets, and (iv) checks the maximum list and the number of maximizing receivers.

A replay on the actual included `verify.py` returned `VERIFY_OK cases=22 total_source_words=2609`. The tested ranges are binary alphabets with semilengths 1 through 9, ternary with 1 through 6, four-letter with 1 through 4, and five-letter with 1 through 3. This exhaustive finite verification does not certify any infinite family by itself. The all-alphabet and all-length result rests on the symmetric embedding and two outer-letter branch proof in RESULT.md.

All parent words are ordinary even palindromes; the channel performs exactly two arbitrary deletions. No independent mathematical audit has been performed; historical priority beyond the inspected literature is not established.
