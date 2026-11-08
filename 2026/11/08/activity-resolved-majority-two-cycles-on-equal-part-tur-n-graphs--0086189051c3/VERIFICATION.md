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

# Reproducibility and limits

Run `python3 check_bits.py` and `python3 check_profiles.py` in a directory containing the packaged files. Each program uses exact integer arithmetic and has no third-party dependencies. Compare their standard outputs byte-for-byte with `bits_output.txt` and `profiles_output.txt` respectively. An assertion failure indicates a mismatch. The programs compute the same invariants by different representations: complete labelled binary-state enumeration and binomial-weighted part-occupancy enumeration.

`check_bits.py` checks 21 parameter pairs with \(rq\leq18\). `check_profiles.py` checks 34 parameter pairs with \((q+1)^r\leq450000\), using \(2\leq r\leq7\) and \(2\leq q\leq7\). For every case, both fixed-point and primitive-two-cycle counts are checked by their full flipping-vertex activity distribution. Both captured outputs end with an explicit PASS marker.

The mathematical proof of the unrestricted theorem is in `RESULT.md`; finite program executions are additional evidence and cannot establish the result for all \(r,q\). Verification does not cover transient basin counts, unequal part sizes, or independently conducted scientific review.
