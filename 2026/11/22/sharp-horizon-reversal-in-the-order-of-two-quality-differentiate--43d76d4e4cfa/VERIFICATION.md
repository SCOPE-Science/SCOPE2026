---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently write B/m=e^(−at)+1_{t≥d}e^(−a(t−d)) and the swapped quality difference (Q_HL−Q_LH)/(mΔq)=e^(−bt)−1_{t≥d}e^(−b(t−d)). Their product integrates on [0,d] to E/c and on [d,H] to −(1+e^(−ad))(1−e^(−bd))(1−z)/c, where z=e^(−c(H−d)). This proves the contrast, including H=d, since (1+e^(−ad))(1−e^(−bd))=E+D>0. The contrast decreases strictly for H>d from m²Δq E/c>0 to −m²Δq D/c. Thus it crosses once iff a<b; when a=b it stays positive at finite H and tends to zero. Solving for z=D/(E+D) gives the claimed H_c and cancellation of mass and quality. As d→0, E/d→c and D/d→b−a, giving log(2b/(b−a))/c, while the contrast is O(d) uniformly on H≥d. As d→∞, D=e^(−ad)(1−e^(−(b−a)d)) and log(1+E/D)=ad+o(1), giving the other stated limit. Four-term numerical convolution quadrature independently agrees with both displayed response pairs and sampled boundary/regime cases.

## originality

PASS

The supported distinct result is the full sign law and the explicit singular crossover limit for this exact continuous-time quality-swap proxy, not the impulse-response algebra, general one-switch behavior, or a solution of the cited food-web model. The strongest indexed analogues compare different controls or objectives. General kernel representations supply an evaluation framework but no identified statement covers the specific sign and thresholds. The literature decision is provisional given inaccessible material.

## value

PASS

Holding times, total mass and qualities fixed isolates a genuine reversal in the cumulative observable, not an instantaneous-rate crossing or a comparison of different doses. The short-gap limit is useful for interpreting what a model or numerical study can detect: vanishing effect size does not push the crossover to zero. The theorem is elementary but supplies a fully solved benchmark for time-window sensitivity in a motivated two-memory model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
