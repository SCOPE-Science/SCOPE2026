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

Both normalized densities integrate to one on their active intervals. For H=F−v, the continuous curve has H(0)=H(1)=0 and is strictly concave on each side of activation. Thus if H(d)≥0 there is no sign-changing interior zero; H(d)=0 makes a contact with H>0 on both sides. If H(d)<0, the strictly monotone secant slopes from each anchored endpoint give at most one interior zero per side, with existence exactly when the respective slope H′(0+)>0 or H′(1−)<0. Substitution gives w>L, w<U0 and w<U1. At w=L concavity at both anchored segments makes both slope inequalities strict, proving nonemptiness; L>0 follows from strict concavity of F1 and U0<1. U1 falls strictly from +∞ to 0 as d ranges from 0 to 1, and solving z=c+(1−c)/U0 gives the unique switch. Independent symbolic limits give (1−exp(−a))/2 for width/d at the initial end and a/2 for width/(1−d)^2 at the terminal end; the matched linear terms cancel at the latter. Replayed the example with H(d)=−1/18 and roots 0.312578367542804 and 0.638317443294359. Replay: `python3 /workspace/branches/independent_certificates.py 3`. This is not validation of a field model.

## originality

PASS

The supported contribution is the exact all-parameter delayed equal-rate mixture window, its switch, and its different boundary-layer scalings, not the cumulative mass–volume framework or discovery of mixed flushing shapes. Checked literature establishes the framework and empirical variation, and the closest indexed mathematical model treats a different mechanism and a single crossing; inaccessible full text remains a named risk.

## value

PASS

This is a motivated mechanism for nonmonotone cumulative mass surplus despite decreasing release within each source. The exact feasible weight window quantifies when a second crossing can occur and shows why estimation of the effect becomes far more sensitive as activation approaches the event end. Those are informative comparisons within a natural idealized model, not a prescription for capture-system design or a rediscovery of observed mixed curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
