---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With mixed spoke bits, every rim edge crossing the bit cut must point from 1 to 0, forbidding a path from a spoke-0 vertex to a spoke-1 vertex. This excludes a hub cycle, and a coherently directed rim also would cross in both directions. For constant spokes only the two directed rims must be dropped. Conditional summation over each rim edge gives the stated L_b with the signs in the stated edge encoding; contraction over the cyclic spoke indices yields the trace, and the four removed terms give the stated product correction. Fixed-size matrix products take O(n) arithmetic steps with O(n)-bit integers. The count is 3^n−3 from the eigenvalues 3 and 1 and the correction 4. Reversal forces odd characters to vanish and pairs the signs at even characters; the latter coefficients are 3^n−3 modulo 4, so all survive for even n. With b all ones, use J^2=−I and (D_1 J)^2=I: zero a for n divisible by four and two adjacent ones for n=2 mod 4 both give trace 2 and correction 4. Thus the least nonzero magnitude is 2, and the absolute maximum is the zero-frequency count. Fourier diagonalization gives rank and the stated restricted condition ratio; averaging reversal is a contraction fixing a nonzero range, so its norms are one and optimal. For odd n the all-one b product has odd off-diagonal parity and zero trace, with zero correction; precisely 2^(n−1) choices of a in that family have even total weight. This proves an upper bound, not the odd rank itself, including n=3.

## originality

PASS

The combinatorial fibres, unsigned count and the generic reversal argument are not original. The inspected sources do not supply the wheel-specific signed linear-step formula together with the sharp magnitude witness and explicit odd-rim failure of full even-character recovery. Passage-level comparison of the nearby graph-family records gives different orientation cubes or different signals, not a reparameterized wheel result.

## value

PASS

For convolution by an orientation indicator, the edge spectrum determines precisely which orientation signals can be recovered and at what conditioning. The new signed calculation supplies a linear-step individual coefficient evaluation and sharp conditioning where only reversal is lost, and a concrete additional obstruction in the other parity. That is useful beyond the known zero-frequency count or flip statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
