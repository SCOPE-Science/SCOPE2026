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

In the unit-directed prey-to-consumer chain with existing basal-to-apex shortcut, the trophic levels are prey averages and the original squared incoherence is (n-2)²/(2n). Every admissible missing forward edge is either internal i->j with j<=n-2 and skip h>=1, or apex-targeting i->n-1. In the internal case, local prey-average shifts of -h/2 propagate to the penultimate node and -h/4 to the apex, giving q_int²=[h²+(k-h/2)²]/[2(n+1)], k=n-2. Completing square gives unique nearest integer h=floor((2k+2)/5); half-ties are arithmetically impossible. Apex additions have q_apex²=2(k²-ki+i²)/[3(n+1)]>=k²/[2(n+1)], strictly above the attainable internal optimum for k>=2. The h=1 option shows strict improvement; leading ratio tends to 4/5. Independent Fraction computations recomputed each admissible edge for n=4..11 and verified all argmin sets.

## originality

PASS

A prior exact one-added-link trophic-incoherence theorem for rooted out-trees is a closely related stronger graph-family statement, but its baseline requires every nonbasal node to have exactly one prey and q0=0. The submitted graph ALREADY contains the basal-to-apex omnivory edge, so its apex has two incoming prey and nonzero q0 before the new link; the older theorem cannot be reapplied to this second-edge setting. Johnson et al. define the metric and model food-web stability; Klaise-Johnson examine random motif assembly and omnivory rather than the deterministic all-n two-omnivory optimum. No inspected source supplies the unique optimal skip h=floor((2n-2)/5) and 4/5 ratio in this precise graph/metric. Priority is best-of-knowledge only.

## value

PASS

The motivating structural question is whether one additional feeding link can restore coherence after an apex shortcut already disrupts the chain. For every size, the exact non-apex optimal skip spans roughly 2/5 of the chain, its placement is translation-independent within allowed internal positions, and it reduces squared incoherence by asymptotically 20%. This is a natural complete constrained network-optimization classification on the established prey-average q metric, not an unsupported inference of biological stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
