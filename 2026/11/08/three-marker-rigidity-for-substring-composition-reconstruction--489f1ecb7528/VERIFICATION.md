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

# Verification procedure and scope

Run `python verify.py` in Python 3 without dependencies. A successful fresh replay prints `VERIFY_OK polynomials=1820 words=17550 differences=4096 threshold=('10110010', '10010110')`.

The script evaluates all 1,820 zero-gap quadruples of aggregate zero count at most 12 and independently constructs all three composition-channel polynomials from actual words. It exhaustively groups the 17,550 weight-three words of lengths 3 through 26 by their complete contiguous-substring composition multisets, tests each reversal fiber, and checks the stated orbit formula. It independently tests the orientation identity on 4,096 quadruples with each gap in the range 0–7, and verifies one pair of nonreverse length-eight words of weight four with equal complete spectra. These are finite checks only. The arbitrary-length result rests on the exact polynomial factorization in `RESULT.md`, not on an assertion that an enumeration has covered all lengths.

All source dates are initial publicly identified dates where available; no independent mathematical audit or external certification is claimed. Historical-priority searches cannot prove absence of an unindexed equivalence.
