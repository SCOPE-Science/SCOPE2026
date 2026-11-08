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

The statement counts total \([1,2]\)-dominating subsets of labelled rook graphs. Its formula is independently verified on explicit finite boards by the two accompanying self-contained Python 3 programs.

`verify_direct.py` computes open neighborhoods from the rook adjacency rule, then checks every subset; its `DIRECT_CHECK_PASS 13` footer attests to the 13 tested boards. `verify_profiles.py` uses a disjoint algorithm: it fixes eventual row occupancies, permits only column patterns satisfying all neighborhood constraints, and counts labelled column sequences with a dynamic program; `PROFILE_DP_PASS 19` attests to 19 tested boards. Captured results are in `direct_output.txt` and `profiles_output.txt`. These outputs were obtained by running the embedded source scripts directly.

The infinite-family claim depends on the proof's three exhaustive cases, not the tested finite range. The software does not certify historical originality or provide independent mathematical review. No external audit has been performed.
