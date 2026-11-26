---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Expanding z^S over selected short bonds counts each forced nonoverlapping r-set once. Removing its endpoints cannot erase any crossing, and order-preserving relabeling preserves the rest. Shifting sorted left endpoints by 0,...,r-1 gives the path coefficient binom(2n-r,r). Differentiating gives the exact factorial identity including n=0 and r=0. The r=1 identity and uniform single-chord deletion give the stochastic comparison, hence every nondecreasing f has nonpositive covariance. The short-count variance is 2(n-1)/(2n-1). Independently, generate the matching by ranking two independent uniform endpoints for each of n labeled chords. A crossing pair has probability 1/3, the conditional crossing probability given one interval of length l is 2l(1-l), and its variance is 1/45; incident pairs yield the stated crossing variance, disjoint pairs covariance zero. These moments give the covariance and correlation as claimed. The same rank model expresses C_n as a second-order U-statistic with nonzero first projection, giving the marginal Gaussian CLT (also Flajolet–Noy Theorem 3). Fixed-r deletion changes the centering by O(n) and the standard deviation ratio by o(1). Sequential forced-bond counting gives a_{n,r}<=1 and each fixed-r factor tends to one. In the mixed transform use z=exp(is): the same factorial expansion is absolutely dominated by 2^r/r!, so the joint characteristic functions converge to the product by the continuity theorem. Inspected VERIFICATION.md and verify.py without executing frozen code. Independent bounded replay: python3 /workspace/independent_checks.py checks 238 binomial moment/crossing cells for n=0..6 plus moments and threshold inequalities; it is not evidence of joint convergence by itself.

## originality

FAIL

The two earlier October 18 indexed records give the cyclic factorial transfer and joint independent limit. Removing the single wrap adjacency converts their full finite enumerator to the frozen linear one exactly, and the wrap-edge probability vanishes asymptotically. The sign claim for all increasing f is an immediate deletion coupling after the resulting r=1 identity. Marmor also explicitly uses the same linear forced-short-edge argument and treats the fixed-crossing family, though he does not state the entire frozen package verbatim.

## value

FAIL

The mixed law and joint decoupling would be worthwhile for understanding local versus global chord statistics, but those statements are already available and the linear convention removes only one edge with a direct exact conversion. The added monotone test-function wording is a routine consequence of that transfer and single-chord deletion, rather than a distinct useful unresolved statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
