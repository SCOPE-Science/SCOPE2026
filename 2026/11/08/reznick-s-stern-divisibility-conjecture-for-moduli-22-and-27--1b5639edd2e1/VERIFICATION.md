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

# Reproducibility and verification
Run `python3 verify_stern_22_27.py` with Python 3 (standard library only). The verifier constructs all primitive residue pairs modulo \(22\) and \(27\), verifies there are respectively \(360\) and \(648\), implements exactly the two Stern-pair binary transitions, computes all \(1008\) necessary levels with exact unbounded integers, and asserts their equality. It also checks total mass \(2^r\) at each step, repeats all levels using a second algorithm on all residue pairs, and checks \(r=0,\ldots,18\) by direct Stern recurrence.

Observed result: `VERIFY_OK states22=360 states27=648 Cayley_Hamilton_bound=1008 exact_levels=0..1007 independent_full_grid=PASS direct_Stern_levels=0..18 first10=[1, 1, 1, 1, 1, 1, 1, 1, 5, 13] counts_sha256=e7ca1f54991a09ebd233ffc4a45d8d30cfb2e37be2337307e037ddb3a924bd8d`.

The infinite assertion requires the explicit Cayley–Hamilton argument from `RESULT.md`; finite enumerations by themselves are not a proof. No external or independent audit is claimed.
