---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The full-branch base map tau_a has uniform conditional images and branch lengths p/M,...,p/M,q, so its successive labels are iid and independent of uniform center initialization. Their center maps are M distinct inverse-branch graphs (y+k)/M and one expanding graph {My}; the contraction graphs do not meet and their intersections with the expanding graph are a finite set y=(Mj+k)/(M^2-1), null under the uniform stationary marginal. Thus the observed path recovers all branch labels modulo null sets common to all interior p. This invertible parameter-free coding transfers the categorical iid likelihood, f-divergences and Fisher information and makes the contraction count Bin(n,p) sufficient. The Koopman transfer identity U*=L and Kp=pL+qU yields invariant Lebesgue and reverse kernel Kq; stationary reversal path law is Pq. Substituting p prime=q into exact likelihood produces S_n=(2N_n-n)log(p/q), binomial fluctuation ratios, entropy and almost-sure law; Lyapunov (q-p)log M vanishes only at p=q. Independent rational moment/CDF stationarity identities checked M=2,3,4 at three probabilities each; source exact check script for path labels and fluctuation relations was inspected. Finite checks corroborate, not prove, all lengths.

## originality

PASS

The affine random-map model and its stationary Lebesgue center behavior are classical in Homburg–Kalle and Takahasi. A November 1 published Resultary theorem gives exact two-time covariance symmetry under p/q interchange, and its operator adjoint mechanism is strong relevant coverage; path reversal is a routine consequence of that operator. However none of the inspected earlier statements identifies the entire branch sequence from center pairs or establishes full-path parameter likelihood equivalence, sufficient statistics, exact finite-sample divergence formulas and infinite-law singularity. These are the surviving motivated contribution, with the general f-divergence and entropy identities credited as consequences of the specific observable coding.

## value

PASS

A process whose one-time observation law is parameter-independent nonetheless encodes the entire parameter-dependent iid switching sequence in its consecutive observations. Identifying the exact finite-horizon statistical experiment, information rate, infinite-path singularity and arrow-of-time threshold is a coherent and mathematically motivated distinction between static and dynamic observability. Adjoint reversibility itself is credited to established principles and the earlier covariance operator rather than claimed as new general theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
