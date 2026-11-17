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

The exact four-mark generator is irreducible in continuous time for -1<=rho<1, with independent uniform headings redrawn on tumbles; stationary X is a damped stochastic convolution. The no-event decomposition gives Cov(V_t,V_(t+u))=s0 exp(-gamma |u|). The degree-four generator system yields Var X=s0/[mu(mu+gamma)]+D/mu and kappa4=6 s0^2/[mu^4(alpha+1)^2(alpha+3)]*[c(alpha+1)/(2+alpha(1-rho))-1]. Strict derivative in rho and one-sided rho->1 limit give unique sign threshold precisely when c(alpha+1)>2, with nonergodic endpoint excluded. An independently written exact SymPy four-mark stationary solver verified five rho settings, the zero at rho=7/10 and kappa4(9/10)=2/7 for mu=1,gamma=4,a=1,b=3. Thermal OU term changes only variance.

## originality

PASS

The distinct claim is the explicit covariance-invisible correlated-speed family and exact realizable fourth-cumulant sign boundary, not the known generic observation that matched autocovariances need not imply matching higher cumulants. Parent stationary RTP theory independently redraws speeds and covers rho=0 only; matched angular-telegraph or inertial-kurtosis results treat different state transitions. Priority best-of-knowledge with stated Markov-modulated-noise risk.

## value

PASS

A covariance-indistinguishable non-Gaussian signature and a sharp feasible cumulant sign reversal are natural observables for stochastic active-matter model identifiability, not an arbitrary parameter table. The threshold exposes a real model ambiguity even when the full two-time force statistics are fixed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
