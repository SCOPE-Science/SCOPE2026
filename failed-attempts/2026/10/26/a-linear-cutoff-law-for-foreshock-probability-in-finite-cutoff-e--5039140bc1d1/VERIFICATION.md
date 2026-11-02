---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The child-failure fixed point x=p_rho+int_{m0}^rho f(u)(1-exp[-kappa mu(u)x])du follows by independent marks, all-generation branching and Poisson generating functions. Its Lipschitz constant is at most n=kappa E(mu)<1; x tends to zero and Taylor expansion uniformly in bounded productivity gives x~p/(1-n). Poisson root offspring then give F=1-exp[-kappa mu(rho)x], and positive endpoint density gives p~f(M)(M-rho). Independent quadrature and root-finding reproduced the coefficient under a strictly subcritical parameter set; no finite computation supports critical n=1.

## originality

FAIL

FAIL: Saichev and Sornette (2005) already derive the exact ALL-GENERATION maximal-aftershock probability from a Poisson-marked ETAS generating functional (equations 31-35), not merely an expected cascade count. Their formula is structurally valid for arbitrary independent child-mark laws, including finite truncated laws; Sornette and Werner (2005) explicitly give the normalized finite-upper-cutoff Gutenberg-Richter law and mean total progeny. Substituting this established law into the established fixed point and taking its derivative at an endpoint produces precisely this linear coefficient by a routine first-order expansion, with no new structural lemma. The earlier paper also explicitly gives a large-threshold tail factor 1/(1-n) in Eq.44. Although this exact finite-endpoint numerical coefficient is not printed there, the submitted result is a mechanically implied corollary of stronger prior distributional work, not an original theorem. No scientific repair was staged or claimed.

## value

PASS

The finite magnitude-endpoint slope is a physically meaningful boundary statistic: a hard upper cutoff necessarily destroys magnitude-independent foreshock probability and supplies a quantitative model comparison. It can be useful for interpreting ETAS within a fixed subcritical regime, even though it is an elementary consequence of prior generating-function theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
