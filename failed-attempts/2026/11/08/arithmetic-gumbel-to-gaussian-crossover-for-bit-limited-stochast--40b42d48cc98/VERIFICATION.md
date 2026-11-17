---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

With K=2^r and eps=1/(qK), floor(K(j-eps*j))=Kj-ceil(j/q), so transition j->j-1 has exactly p_j=ceil(j/q)/K (valid because j<qK) and independent geometric holding times. Their product pgf, first two moments and q-fold exponential-block decomposition follow directly. Fixed q gives maxima of exponentials and the stated q-averaged Gumbel shifted by -log(q); uniform coupling requires n/K->0. For q->infinity a Lyapunov ratio bounded by const/min(q,n)^(1/2) proves Gaussian, including q>=n negative-binomial range. A small exact rational check with n=11,q=2,K=8 matches the stated kernel and geometric moments. Correctness is supported by the proof, not logs.

## originality

FAIL

Decisive prior statement-level coverage: the published 2026-11-02 finite-bit stochastic-rounding decay theorem already gives an exact geometrical holding-time kernel, shifted convolution of coupon collectors, q-fold averaged Gumbel and many-deficit self-averaging, although expressed in a decrement-rounding model. Under state translation m=j+q-1 and parameter L=q,K=2^r its transition probability floor(m/L)/K equals ceil(j/q)/K for every state j>=1. Thus its exact finite Markov law already implies the present pgf, moments, and fixed-q Gumbel law. The new Gaussian claim as q diverges is a routine Lyapunov CLT for these same already-specified independent geometric holding times and supplies no separately motivated new invariant. The physical implementations differ, but the final mathematical absorbing-time claims coincide by an exact kernel reduction.

## value

FAIL

The broad finite-bit precision-to-termination question is worthwhile, but this submitted exact law repeats a previously published chain after an affine state relabeling. The remaining normal approximation is a standard triangular-array CLT for the same known exact independent waiting times, without additional structural or application-specific consequence. Novelty, code quality and kernel reparameterization cannot establish independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
