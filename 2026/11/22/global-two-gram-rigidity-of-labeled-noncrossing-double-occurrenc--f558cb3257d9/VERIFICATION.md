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

The proof in `RESULT.md` uses three lemmas: adjacent-doublet existence in a noncrossing matching, the profile-level doublet-deletion update, and uniqueness of every directed bigram on the reduced noncrossing word. They imply a complete induction, so exhaustive finite cases are supplementary rather than a substitute for proof.

Run `python3 verify_noncrossing_bigram.py` from this directory with Python 3 standard library. The replay enumerates all labeled noncrossing sources through six labels and all double-occurrence sources through five labels. It checks exact Catalan counts, unique noncrossing bigrams, spectrum-only decoding, all unrestricted fiber multiplicities, the sharp first unrestricted collision, and no untested upper-order claims. Actual replay transcript is `verification_output.txt`.

No external or independent audit was performed; historical novelty remains qualified by possible unindexed equivalent literature. No computational run can certify that no such external source exists.
