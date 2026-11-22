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

Verified precise linear order P_n=T_(n-1)...T_1, n>=2, and all-pair Gini seminorm modulo constants. Every real signal has a positive layer-cake binary-cut decomposition, so cut tests suffice. Each local averaging loses at least |a-b| in Gini; for a binary vector the carry recursion has at least geometric dissipation 1+1/2+...+2^{-(k-1)} after choosing the minority side, while a suffix block of k trailing 1s makes every triangle inequality an equality. This proves gamma_n exactly, not via finite sampling. Direct algebra comparing adjacent k choices gives small cases and strict minimum at floor(n/2) for n>=9, asymptotic n²(1-gamma)->8. Independently exhausted all nontrivial binary initial vectors at n=2..11, including gamma_5=3/4, gamma_8=53/60, gamma_9=29/32; all matched. Source RESULT.md blob 53c0ef1a689e0ec16bc672078d23291a0e3605fe.

## originality

PASS

A natural but specific exact one-sweep Gini norm and phase change in sharp binary extremizers are not supplied by cited Euclidean gossip convergence or stochastic Gini-decay theory; broad exact-seminorm search found only the submitted same-record match.

## value

PASS

The complete-pair absolute-difference dispersion is an interpretable consensus metric. A sharp contraction factor for a fixed deterministic sweep, its optimizing cut-size transition at n=9, and n^-2 asymptotic deficit are exact, nontrivial information not recoverable from generic monotonicity or spectral estimates; independently useful for designing and comparing gossip schedules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
