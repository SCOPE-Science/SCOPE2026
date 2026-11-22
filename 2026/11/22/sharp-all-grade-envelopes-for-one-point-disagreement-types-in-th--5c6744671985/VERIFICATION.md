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

# Verification record

The exact script `check.py` and its captured output `check_output.txt` are included with the theorem. Execute `python3 check.py` in the same directory; it requires Python 3.8 or later with no third-party modules. Its final line is `VERIFY_OK`.

The verifier evaluates each one-point insertion type as a symmetric difference of two prefix bitmasks. For all \(n\le5\) it also derives the grade independently by comparing every named point with each insertion gap. It checks every permutation through \(n=9\) against the analytic lower and upper bounds, verifies the sum of its coefficients equals \((n+1)^2\), and tests the folded permutation and the entire claimed saturation rectangle for all \(n\le80\) and every \(0\le k\le n\). All executed assertions passed.

Finite enumeration is not a proof of the all-order claim: the unbounded proof requires the coordinate-rectangle bound, the exact odd/even prefix-intersection count, and the row-walk lower bound. The checker does not certify novelty or classify all upper-equality permutations; independent audit has not occurred.
