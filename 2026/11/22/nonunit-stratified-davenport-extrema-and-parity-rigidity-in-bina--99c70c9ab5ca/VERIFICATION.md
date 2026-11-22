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

The theorem is proved mathematically in `RESULT.md`. The companion `verify.py` is an independently encoded, finite check based on direct integer-bitmask multiplication over the truncated polynomial ring and a complete proper-subsequence test. Execute with `python3 verify.py`. The supplied `verification_output.txt` is the result of running this exact file.

Checks include 81,340 finite assertions; full tests of the irreducibility deletion criterion at depths one through five and lengths up to four; exhaustive cutoffs, inverse maximal-profile checks, and stratified maxima through depth four; group generation through depth twelve; and 1,000 randomized longer instances. These tests do not certify the theorem at untested depth and do not provide independent scholarly review.
