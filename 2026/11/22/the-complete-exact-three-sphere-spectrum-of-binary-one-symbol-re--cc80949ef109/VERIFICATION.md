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

# Verification

The symbolic proof is in `RESULT.md` and uses a block concatenation identity and exact overlap classification. Two standalone Python 3 standard-library programs use different enumeration directions: `verify_forward.py` generates all distinct descendants directly and checks 2046 binary source words at lengths 1–10; `verify_inverse.py` enumerates length-\(n+3\) words and traces every valid inverse reduction (delete a symbol unequal to its predecessor) exactly three times, checking all 510 sources at lengths 1–8. Both passed in the local replay on the embedded program contents.

Run `python3 verify_forward.py` and `python3 verify_inverse.py`. No third-party dependencies. The finite checks do not claim to establish the unbounded-\(n\) formula; the explicit induction in the proof does.
