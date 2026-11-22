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

# Verification procedure

Run `python3 verify.py` from this directory (Python standard library). The enumerator builds local incoming-to-outgoing successor bijections at every vertex and retains only single Euler tours; it is independent of the stated overlap calculation. Every binary length-\(n+1\) motif for orders \(2,3,4,5\) is compared as an exact `Fraction`. The resulting cycle counts are respectively \(1,2,16,2048\), consistent with the BEST enumeration.

For every motif through order eleven, exact probability bounds, dyadic denominator, expected window-sum identity, and previously established forbidden-support set are checked. An additional separate exact symbolic cofactor computation, outside the standard-library standalone checker, compared all nonconstant motifs through order five to independently built contracted Laplacians and passed.

These finite enumerations provide reproducibility, not proof for infinitely many orders. The analytical proof in `RESULT.md` supplies the all-order quantifiers and computational bound. No independent scientific audit has been performed.
