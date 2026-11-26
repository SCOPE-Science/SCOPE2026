---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The original node polynomial is W=(x²−1)U_{n−1}; W(cos θ)=−sin θ sin(nθ), and its derivative at the nodes is n(−1)^i, doubled at the endpoints. Multiplying W by (x−y)/x yields the frozen cardinal identities; the moved cardinal is uniformly bounded since its normalizing value tends to sin(πα)/(πα)>0. For bounded angular offset t and K<=|k|<=n/4, the unchanged cardinals have common numerator |sin(πt)||1−α/t| plus O(n^−2), uniformly since sin(πt)/t removes the singularity. The denominator divided by π|k| is 1+O(1/|k|+k²/n²) after the factor n is included, and the perturbed-node weight ratio is 1+Oα(1/|k|). The resulting errors are summable with O(1) total, as are the few small-index terms (removable divided differences) and the O(1/n) far-index terms. The two harmonic tails yield the factor 2/π. When n|x|→∞ the overall replacement factor tends to 1, the finitely many nearby-index corrections vanish, and the rest are bounded by O(1/K) times the classical Lebesgue constant. This controls the global upper limit while a fixed local offset yields the lower limit. On the shift side t>=α the profile is at most 2/π; for 0<=t<α it is at most 2α, exceeded on the opposite side near zero. Opposite-side offsets u>=1 are bounded by (2/π)(1+α), and on [1/2,1] the profile decreases. For 0<u<1/2, the stationarity ratio decreases from infinity to zero: its derivative sign is that of 2sin(z)cos(z)−z(1+cos²(z))<0 at z=πu. The unique interior maximizer therefore gives the strict claimed gain. Read VERIFICATION.md and verify.py without running them; these finite diagnostics do not justify the global asymptotic.

## originality

FAIL

The indexed Nov. 17 record gives the exact formula, stationarity equation, and opposite-side norming offset for any interior node whose index proportion tends to a in (0,1). The frozen result is its central even-degree specialization, with no surviving unduplicated mathematical assertion.

## value

FAIL

The one-node effect is mathematically motivated, but the frozen result only recomputes an already available exact invariant on a less general grid. It supplies no distinct boundary, analysis of a new regime, improved error term, or other independently useful conclusion. No repair is justified within the existing claimed contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
