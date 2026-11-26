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

Equal rates give a uniform next available triple and P(2 from X)=(X-1)/(s-2). For d=X-Y the conditional mean contracts by (s-3)/(s-2); the product p_k is the displayed gamma ratio and is uniformly asymptotic to (s_k/(2n))^(1/3) at both cutoffs (shifting the lower cutoff by at most two sites is immaterial). The stopped martingale d_k/p_k has variance O(n) and absorption above n^(1/2)-3 would require magnitude of order at least n^(2/3), hence has probability O(n^(-1/3)). To the upper cutoff, the deterministic variance sum is asymptotic to 2n by a mesh-three integral; the expected imbalance correction is O(n^(1/2)), and the normalized maximum step is o(1), giving the martingale CLT. The further normalized variance to n^(1/8) is O(n^(-1/6)); Doob controls the entire interval. Survival to that lower cutoff forces normalized imbalance o(1), an event of vanishing probability because the frozen Gaussian has no atom at zero. At absorption within the interval R_n=|d| and hence |d/p_k|/sqrt(2n)=(R_n/(2n)^(1/4))^(2/3)(1+o(1)). The CDF and density follow. 'Unique terminal state' is read per trajectory, not as a deterministic common configuration. `python3 /workspace/reproduce.py` independently checked the labeled transitions for n=2..6; at n=6 it gave R=0 with probability 25/28 and R=3 with probability 3/28. This is not a simulation proof of the limit.

## originality

FAIL

A distinct indexed result states the same terminal law in a stronger critical-window family. Its theorem specializes exactly to the entire balanced claim. This is a failure of distinct claim coverage against the current record set, not a demonstration that the compared record historically preceded the frozen work, nor an assertion of dependence in either direction.

## value

PASS

This would be a substantive terminal distribution for a natural greedy matching model: it gives a non-Gaussian scale substantially smaller than the general matching bound and explains how a mesoscopic Gaussian imbalance controls boundary depletion. No independent valuable remainder beyond the covered law is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
