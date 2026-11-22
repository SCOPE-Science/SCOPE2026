---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

C PASS. For F_b(x)=bx-sgn x on (-1,1), b in (1,2), the two positive-slope branch images partially overlap: density is 1/(2b) outside overlap and 1/b within it, so uniform input is not uniform output; endpoints b=1 (partition) and b=2 (double cover) preserve normalized Lebesgue. Hence genuinely alternating uniform-gain pairs are (2,1),(1,2). With A=F2 and B=F1, almost everywhere B²=id, A∘B=A and A=id+B. The phase-two system reduces to signed dyadic doubling; transfer P_A x=x/2, and E[x²]=1/3 determine all exact phase covariances and their opposite lag-two signs. The paired sum S_m=sum_{j=1}^m A^j(W), W=A(U), has covariance 1/(3*2^k), variance m-4/3+4/(3*2^m), and differs by <=2 from sum of independent fair binary digits, giving standard CLT. Independent deterministic midpoint integration 2^18 subdivisions confirmed eight even/odd correlations and four block variances; algebra and Bernoulli coding prove all lags and weak convergence. Threshold preimages are null, distinct gains, range [1,2].

## originality

PASS

PASS best-of-knowledge. Earlier Bula and Radin periodic-threshold neuron articles study periodic orbits and attracting intervals; the accessible 2024 full paper does not give two-phase Lebesgue rigidity, all-lag autocorrelation or paired-sum CLT. Binary doubling and transfer identities are classical, not claimed original. The combination furnishes a new exact statistical signature for alternating gains whose one-time marginals are indistinguishable. The relevant 2015 paper full text was inaccessible, and unindexed coding treatments remain a priority risk.

## value

PASS

PASS: a two-period neuronal map can have identical phase-wise uniform marginals yet a lag-two correlation that changes sign between phases. The uniqueness of gain choices and complete exact covariance plus finite-window variance/CLT give a motivated classification and useful counterexample to marginal-only statistical identification, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
