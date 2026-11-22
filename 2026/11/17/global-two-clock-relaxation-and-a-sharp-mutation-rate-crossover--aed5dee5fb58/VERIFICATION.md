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

Correctness PASS. Summing the exact balanced May–Leonard equations (alpha+beta=2) gives logistic S'=S(1-S), S>0 for nonzero nonnegative starting data. On the simplex, p_i'=-(alpha-1)S p_i(p_{i+1}-p_{i+2})+mu(1-3p_i). Entropy H=-sum log(3p_i) has exact H'=-mu(sum 1/p_i-9), strictly negative outside p=e, and mutation pushes boundary states immediately interior, yielding global frequency convergence. Writing u=p-e, B_i=-(u_(i+1)-u_(i+2))/3, B²|E=-I/3 and u'=-3mu u+(alpha-1)S Bu+(alpha-1)S N(u), N quadratic. For nonzero u, logarithmic radial slope -3mu+O(||u||) yields an integrable correction and a positive limit L=lim exp(3mu t)||u||. Removing exact rotation R=exp((alpha-1) B tau) gives convergent nonzero vector v with error O(exp(-3mu t)); restore O(exp(-6mu t)). Orthogonal split x-e=(S-1)1/3+S u gives the sharp crossover at mu=1/3, with S0=1 and p0=e correctly exceptional. Six independently chosen rational configurations checked mass/frequency/entropy identities exactly, not finite proof of globality.

## originality

PASS

Originality PASS best-of-knowledge. Jaramillo–Mrad–Stepien introduced linearly mutated May–Leonard, calculated local eigenvalues and Hopf features; normalized zero-sum RPS replicator-mutator dynamics with S=1 are known. A published stronger symmetric-competition entropy gradient covers alpha=beta=1, which makes the rotation vanish, but not alpha≠beta on the balanced skew-symmetric competition line, nor the general two-clock nonzero asymptotic vector and mu=1/3 rate transition. The known slice is credited and does not cover the asymmetric general theorem.

## value

PASS

Value PASS. The exact global convergence and nonvanishing rotating asymptotic profile separate total population recovery from composition mixing, exposing a sharp parameter threshold at which the dominant error mechanism switches. This quantifies a non-gradient cyclic ecology flow using a clear entropy and interaction picture, beyond routine local eigenvalue analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
