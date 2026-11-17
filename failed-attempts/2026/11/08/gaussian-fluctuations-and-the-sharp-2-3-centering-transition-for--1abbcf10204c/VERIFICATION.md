---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For aligned harmonic Zipf rates and weights, the rescaled discovered mass Y_n(a) is a sum of independent Bernoulli variables with mean S_n(a)=sum_j(1−exp(−a/j))/j. Its deterministic exact root a_n is unique. Euler–Maclaurin expansion of the infinite mean and finite tail gives a_n=B_n+B_n²/n(1+o(1)), B_n=exp(theta H_n−2gamma). The variance satisfies aV_n(a)→1/2 and a triangular-array Lyapunov estimate yields the exact-root-centered hitting-time N(0,1/2) law. Bias (a_n−B_n)/sqrt(B_n)∼B_n^(3/2)/n creates theta=2/3 shift e^(−2gamma). Independently solved finite roots at several n and theta and checked the predicted bias ratios approach one. Finite checks do not prove the CLT.

## originality

FAIL

FAIL: A previously published November 2 2026 full result on precisely the same finite harmonic-Zipf weighted quorum model proves the SAME exact-root-centered Gaussian limit N(0,1/2), same second-order cutoff shift, and same sharp theta=2/3 phase diagram. The alternate explicit centering B_n=exp(theta H_n−2gamma) differs from the prior c_theta n^theta by O(n^(theta−1)); at sqrt(n^theta) scale this is negligible. Prior boundary mean c_theta² when divided by n^(theta/2), becomes c_theta^(3/2)=e^(−2gamma) under sqrt(B_n) normalization. The new more precise small-theta root remainder is a standard refinement of the same expansion and not an independently new claim.

## value

FAIL

FAIL: The scientifically motivated exact-root Gaussian quorum theorem and 2/3 bias threshold were already completely proved for the identical model. The slightly adjusted finite-H_n center and Euler–Maclaurin remainder improvement do not establish a separately motivated unknown natural invariant, structural boundary or useful independent classification; mathematical correctness/reproducibility cannot rescue an already covered full theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
