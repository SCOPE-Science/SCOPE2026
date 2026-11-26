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

A selected projected equation resets the one free coordinate exactly to d_i/s_i, so the law after every positive number of updates is Q_i=s_i^beta/sum_j s_j^beta on those atoms. Thus the moment is sum(s_i^(beta−q)|d_i|^q)/sum(s_i^beta), maximized only by saturation of all |d_i| for fixed s. For beta<q one positive row vanishing with another row fixed at 1 makes the risk unbounded over systems, not on a fixed system. For beta=q the denominator is strictly above 1 and the m-bound is approached by vanishing all except a unit row. For beta>q fix one unit row and the sum of the remaining s_i^beta. Strict concavity of z^(1−q/beta) bounds the numerator by its value with all remaining rows equal. For their common size t the derivative of the risk has the sign of beta−q−beta*t^q−q*(m−1)*t^beta, strictly decreasing from positive to negative. This proves interior attainment and all equality claims, including the unique unit row. The witness Gram matrix is I+(1,epsilon)^T(1,epsilon), so its condition number is at most sqrt(3). Its centered iterate error is zero or epsilon^(-1)−1, giving the claimed tail, inclusive at epsilon=1/(1+R), and moments. The uploaded checker was inspected, not run: its R=1/epsilon check is for the uncentered iterate and does not directly verify the stated clean-target tail. The independent exact centered-threshold checks are reproducible with python3 /workspace/reviews/evidence/reproduce.py, output 3. The result is for fixed m, exact projections and deterministic errors; no uniform bound over m or claim for more free coordinates follows.

## originality

PASS

Credit projected squared-norm sampling and the rank-one exact second-moment formula to the specialization of existing noisy SCRK analysis. Neither that result, the Gaussian-ensemble theorem nor the same-day residual-weighting result covers the sharp fixed-m frontier over all positive (beta,q), its supercritical equality geometry, or the stated deterministic single-corruption family tail. The pass is for the distinct sharp profile and witness, not the scalar reset or the existence of a second-moment bound.

## value

PASS

The frontier answers a calibration question for the projected sampling exponent, distinguishing a known second-moment safeguard from genuine high-moment robustness and giving a sharp extremizing geometry when the moment is uniformly finite. Its value is not the reset identity alone. The clean-target tail on a uniformly well-conditioned full system shows explicitly why conditioning the original matrix is insufficient to explain robustness after enforcing the trusted subsystem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
