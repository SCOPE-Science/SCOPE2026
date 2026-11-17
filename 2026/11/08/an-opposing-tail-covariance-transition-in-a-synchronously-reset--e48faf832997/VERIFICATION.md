---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For stationary simultaneous Poisson resetting, the common last-reset age T is Exp(1) after normalization, and counts conditional on T are multinomial with disjoint tails q_b(T). Therefore Cov(C+,C-)=N[(N-1)J(b)-Np_b²], J=E[q_b(T)²], p_b=e^{-b}/2. Strict variance J-p_b²>0 gives exact population sign threshold. Split at T=b² and 1 to obtain Var(q_b(T))=b² log(1/b)/(2π)+O(b²), hence Ncrit~π/(2b² log(1/b)); the K0 joint density has corner asymptotic J~2^{-3/4}b^{-1/2}e^{-sqrt(2)b}/sqrt(π), establishing large-b threshold. With b_N²=c/(N log N), Cov/N→(c-π)/(4π). All claims are for N>=2, b>0; no uniqueness in b or claim of sign at c=π. Independently evaluated the age integral and K0 polar integral for b=0.1,1,4, agreeing numerically. Source code check.py was inspected, not treated as an infinite proof.

## originality

PASS

Best-of-knowledge PASS for the precise new component only; earlier mathematically overlapping statements are credited in the four comparisons. Full source limitations and residual risks recorded, no failed search treated as proof.

## value

PASS

A stationary common resetting environment makes opposite-tail indicators exclusive within a particle yet positively dependent across distinct particles. The exact, sign-changing finite-population threshold and logarithmically corrected N log N critical window describe a genuine collective fluctuation transition not quantified by the previously known one-particle Laplace law. The sharp asymptotic constant π is a usable boundary for later counting-limit work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
