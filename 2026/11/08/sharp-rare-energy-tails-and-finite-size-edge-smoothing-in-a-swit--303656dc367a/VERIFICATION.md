---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The infinite-past convolution yields conditional Gaussian particles with common random variance V∈(a,b). Stationary phase flux has density g(v)= v/ (vbar Beta(p,q) Δ) ((v-a)/Δ)^(p-1)((b-v)/Δ)^(q-1), where p=r1/(2mu1), q=r2/(2mu2); beta normalization follows exactly. Given V=v, N E_N/v is chi²_N, yielding exact density. Stirling gives sqrt(N)/(2 sqrt(pi) s) exp[-N I(s|v)] uniformly over compact v∈[a,b] for fixed s. Minimizing I produces rates at a,s,b in lower/interior/upper regions. Watson endpoint Laplace gives N^(1/2-p), N^(1/2-q) and Gamma leading factors for fixed exterior s, with one more N^-1 for tail probabilities. Substitutions s=a+z/sqrt(N), v=a+y/sqrt(N) and analogously at b with Gaussian domination give the locally uniform edge profiles and N^((1-p)/2)/N^((1-q)/2) endpoint height laws.

## originality

PASS

Best-of-knowledge PASS for sharp out-of-support sample quadratic-energy density asymptotics and two finite-size Gaussian-smoothed energy edges. Biroli–Kulkarni–Majumdar–Schehr 2023/24 establishes the exact latent variance and Gaussian conditional joint law and related extremal/order statistics, which are explicitly credited; Biroli–Larralde–Majumdar–Schehr 2023 gives a generic conditional-iid sum interior limit, also credited. Neither inspected source states the sample-squared-position outside-support polynomial powers/leading constants and Gaussian edge profiles, though these are derivable by additional standard Watson/Laplace analysis; possible prior implicit coverage by broader scale-mixture saddle results remains.

## value

PASS

The sharp rare energy tails and finite-N boundary transition supply quantitative finite-population predictions from a natural switching gas, including separately identifiable dimensionless switching rates through distinct polynomial exponents. Exact constants and edge crossover profiles are useful even without a new general mixture theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
