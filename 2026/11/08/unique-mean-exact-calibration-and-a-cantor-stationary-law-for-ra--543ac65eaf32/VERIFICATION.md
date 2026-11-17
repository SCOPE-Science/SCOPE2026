---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The exact subflow maps are z->exp(-ah/p)z and z->exp(-bh/(1-p))z+1-exp(-bh/(1-p)); coupling provides Wasserstein contraction of laws. Solving the invariant-mean equation and using strict decrease of (1-e^{-hx})/x forces uniquely p=a/(a+b). At this p, q=e^{-(a+b)h} and iid Bernoulli(r=b/(a+b)) bits give z_{n+1}=qz_n+(1-q)B_n, exact mean semigroup and variance pr(1-q)/(1+q)*(1-q^{2n}). Independently enumerated exact rational paths for p=2/5,q=1/3 and checked mean 535/891 and variance 1312/10935 at chosen finite n. Separated affine branches for q<1/2 prove Cantor support and dimension by standard self-similar/cylinder entropy laws; q=1/2 has binary digit law. The first-level gap correctly requires q<min(p,r), not only q<1/2. The finite tests do not prove dimension, which follows from the stated cylinder argument.

## originality

PASS

Scheme-specific unique rate-proportional sampling p=a/(a+b) yielding exact semigroup mean, exact finite-time variance and coarse-step forbidden-equilibrium region are not covered by the inspected randomized-splitting finite-horizon literature. Classical Bernoulli convolution support and dimension are credited, not claimed as new abstract results.

## value

PASS

This minimal CTMC numerical splitting model demonstrates a sharp conceptual distinction between exact mean evolution and pathwise/measure-level fidelity. It gives exact finite-horizon RMS error and a threshold beyond which individual numerical probability vectors avoid the true equilibrium, a useful benchmark and diagnostic for randomized integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
