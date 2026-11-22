---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For coefficients c_k=n^{-1}1_{k<n}, g_k=p(1−p)^k, contraction triangle inequality gives an ℓ1 bound. The same unilateral shift S on ℓ∞ with sign-vector f(k)=sgn(c_k−g_k) attains equality for all n and p, so F_n(p)=2[(1−p)^n+Σ_{k<n}(g_k−1/n)_+]. For p=λ/n compact-uniform Riemann sums yield Φ(λ)=2e^(−λ) at λ≤1 and Φ=2[1−(1+log λ)/λ+e^(−λ)] at λ>1. Its derivative has a unique zero log λ=λ²e^(−λ), λ*=1.6946009205; initial interval [0,n/√(np)] mass testing rules out minimizing p with np→∞ and the geometric tail rules out np→0. Thus every minimizer np→λ*, minimum→κ≈.5646229252. Independent scipy bounded one-dimensional minima n=50,200,1000 tend to this root and limit; exact verifier script inspected. This is a universal operator-norm statement, not an individual T ergodic convergence claim.

## originality

PASS

Best-of-knowledge originality relative to compared statements and actual independent material, not a proof of absolute priority. The matching-kernel probabilistic alias ℓ1 uniform-vs-geometric distribution is exact, but a conditional cluster lens or convergence equivalence does not imply the unique minimax λ*=1.6946, κ=.5646.

## value

PASS

A fundamental uniform quantifier obstruction separates Abel and Cesàro operator averages even after optimal discount tuning. The exact minimax κ, a single extremal unilateral shift, and unique rate λ*/n are mathematically informative for quantitative ergodic approximation; not a mere restatement of classical convergence equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
