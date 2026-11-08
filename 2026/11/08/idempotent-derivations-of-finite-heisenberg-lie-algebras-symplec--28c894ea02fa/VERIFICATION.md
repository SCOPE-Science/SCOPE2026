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

The proof derives the compatible symplectic projection conditions directly from the Heisenberg bracket, counts complementary Lagrangian pairs and symplectic direct summands by group actions, and establishes asymptotics through a uniformly controlled Gaussian exponent. The standard-library executable `verify.py` independently tests finite examples without using those classification assertions to generate its candidate matrices.

Run `python3 verify.py`. Confirmed outputs are `(n,q)=(1,2)` with ranks `{0:1,2:16}`, `(1,3)` with `{0:1,2:36}`, `(1,5)` with `{0:1,2:150}`, and `(2,2)` with `{0:1,2:80,3:480,4:16}`, followed by `VERIFY_OK`. The dimension-three cases test a known boundary; the five-dimensional binary case is the new finite case. Prime-power arithmetic is checked separately, not exhausted over extension fields. No computation proves the infinite-field or infinite-dimensional statements by itself.
