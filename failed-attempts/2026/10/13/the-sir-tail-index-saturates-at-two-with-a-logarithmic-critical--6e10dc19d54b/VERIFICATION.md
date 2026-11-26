---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Condition on X, so P(X/Y>z|X)=min(1,(X/z)^q), and put a=theta/z^2, s=q/2. Since theta/X^2 is unit exponential, the exact tail is 1−exp(−a)+a^s Gamma(1−s,a), with Gamma(1−s,a)=∫_a^∞ exp(−t)t^(−s)dt. Differentiating this exact expression, not an asymptotic equivalent, gives f(z)=q a^s Gamma(1−s,a)/z; the moving-limit terms cancel. The integral tends to Gamma(1−s) for s<1, grows as log(1/a) for s=1, and is equivalent to a^(1−s)/(s−1) for s>1. In the last case the 1−exp(−a) term also contributes at order a, giving s/(s−1), not 1/(s−1), for the survival constant. Division of the exact leading terms gives z h(z)→min(q,2). For every real r>0, Tonelli and independence factor E[Z^r] as theta^(r/2) times ∫_0^∞ t^(−r/2)e^(−t)dt times ∫_0^1 q y^(q−r−1)dy. The two integrals have strict cutoffs r<2 and r<q, respectively, and their finite values are Gamma(1−r/2) and q/(q−r), as claimed. There is no finite variance; when q≤1 the mean itself is not finite. The mathematical conclusions hold; the wording at RESULT.md line 236 about differentiating regular variation is not valid in general, but the cited exact density justifies this step here. The uploaded numerical checker was inspected, not executed and is not used as proof.

## originality

FAIL

The leading asymptotics, including the log and its coefficient at q=2, are direct substitutions in the published exact SIR formulas using preexisting tabulated expansions of the very same special function. The fractional moment formula is a direct product of standard factor moments. This is stronger-result coverage of the core finding, not a claim that Gómez et al. printed the three-regime theorem or all real-order moments verbatim.

## value

FAIL

The tail index and the distinction between an exact power and a logarithmically modified power matter for extreme-value work. As a standalone finding, however, this fixed-q list is obtained by reading the leading term from a standard table for the exact function already in the model, and the moment and hazard assertions require only factorization and division. The source already correctly states regular variation; there is no contradicted index theorem being corrected. The record neither addresses the moving-parameter crossover nor derives another nonroutine consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
