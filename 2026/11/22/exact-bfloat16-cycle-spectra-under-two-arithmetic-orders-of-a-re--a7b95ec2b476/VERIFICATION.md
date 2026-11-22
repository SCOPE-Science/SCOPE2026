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

The code in `check.py` uses integer-scaled bfloat16 encodings, two independently implemented exact nearest-even rounding routes, and two independent finite functional-graph decomposition methods. The checked domain consists of every nonnegative bfloat16 code through `0x4000` (including subnormals). Run `python3 check.py` using the Python 3 standard library. The verifier checks every successor of both maps; no stochastic or sampled argument replaces its exhaustive finite proof.

The exact results: once-rounded periods \(1,18,24\), basin counts \(1,2,040,14,344\), maximal transient \(51\); staged periods \(1,1,3,3,3,3,3,3,3,3\), basin counts \(1,1,326,11,103,3,221,537,117,58,8,7,7\), maximal transient \(44\), and \(3,545\) differing immediate successors.

The conclusions apply only to the displayed evaluation semantics. This verification is reproducible computational evidence for an exhaustive finite theorem; it does not constitute an independent review or extend the result to real-valued chaos or a particular machine implementation.
