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

Logit coordinates m=(u+v)/2, d=(u-v)/2 give the exact tanh recurrence, transverse increase d>0 and Taylor m’=-m+m³/6+md²/2+O(|m|(m²+d²)²), d’/d=3−m²/2−d²/6+O((m²+d²)²). In a fixed small exit tube d grows by factors bounded between 2 and 4, so sum(d_j²) is uniformly bounded. w_j=m_j^-2 has increments 1/3+w_j d_j²+controlled terms; discrete Gronwall bounds w_j ~ j and yields uniform sum(m_j²)=3log N+O(1) by summing weighted perturbations. Then sum log(d_{j+1}/d_j)=Nlog3-(1/6)sum(m_j²)+O(1)=Nlog3-(1/2)logN+O(1), giving the sharp two-term clock. Nonexceptional diagonal starts reach the small tube after a fixed transient with positive transverse derivative; center m=0 is invariant and gives only main log clock. Exceptional backward-orbit starts other than z=1/2 are expressly excluded, and fixed thresholds are essential.

## originality

PASS

Best-of-knowledge original as an exact statement/implication after direct comparison of primary material and relevant published mathematical results; significant inaccessible or indirect antecedents are retained below rather than equated to novelty proof.

## value

PASS

Nonhyperbolic bifurcation produces a divergent loglog correction to a finite-time separation observable. It fills a sharp gap between known scalar critical relaxation and the hyperbolic a>8 escape theorem and requires nonlinear pre-exit uniform estimates, not just differentiating the diagonal map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
