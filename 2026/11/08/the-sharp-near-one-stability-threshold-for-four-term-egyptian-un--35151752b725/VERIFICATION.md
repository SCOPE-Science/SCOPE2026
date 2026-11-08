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

The executable `check_egyptian4.py` reconstructs every triple prefix compatible with a non-special four-term sum above \(41/42\), without any arbitrary bound on denominators. For a partial prefix of length \(j<3\), the mathematical inequality \(x_{j+1}<(4-j)/(41/42-s_j)\) is the loop's finite stopping rule. The fourth denominator is minimized exactly using \(m=\max\{x_3,\lfloor1/(1-s_3)\rfloor+1\}\). The program checks the complete seven-group maxima and the unique largest non-special sum \(599/600\). A separate four-coordinate recursion checks all 103 non-special quadruples whose sums lie strictly between \(41/42\) and one. It also samples rational parameters on both sides of the sharp boundary and proves the rational identities independently by exact arithmetic.

To replay, run `python3 check_egyptian4.py` using the Python standard library only. Its captured output is in `verification_egyptian4.txt`.

**Limit.** The rational tests of specific real parameters do not prove a real-interval claim; the inequalities in the paper do. The complete finite enumeration is exhaustive by its mathematically proved denominator bounds, not by an experimental range cutoff. No external review or infinite formal certification is asserted.
