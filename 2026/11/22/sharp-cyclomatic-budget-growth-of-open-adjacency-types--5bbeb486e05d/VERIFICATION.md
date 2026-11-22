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

# Verification and limits

The mathematical proof is in `RESULT.md`. Run `python3 artifacts/verify.py` in this package's root with standard Python 3. The checker counts open traces and independently obtains cyclomatic rank from connected components, exhaustively checks \(2{,}097{,}151\) graph/marked-set instances for labelled graphs on at most six vertices, and checks \(81\) exact cactus witnesses. The output `VERIFY_OK` confirms these finite checks. The infinite upper bound and parametric construction are mathematical arguments, not conclusions drawn from finite enumeration.

The public preprint references have verified initial public dates, but exhaustive historical coverage and independent review are not claimed. This verification reports no independent audit evidence.
