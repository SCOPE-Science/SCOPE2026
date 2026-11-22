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

PASS: With three independent normal angles theta_i of continuous density g on [0,pi] and iid bounded independent signed offsets H_i of variance v>0, Cramer/determinant expansion yields exact area T=(H1 a+H2 b+H3 c)^2/(2|abc|) with a=sin(theta2-theta3),b=sin(theta3-theta1),c=sin(theta1-theta2). The sine magnitudes satisfy triangle inequalities; bounding offsets by B yields T<=2B²(1/|a|+1/|b|+1/|c|), so T>t requires at least one O(1/t) projective angle collision. Distinct pair overlaps and projective seam collisions have probability O(t^-2) by bounded g. At a single ordinary collision theta2=theta1+z/t with third direction separated, exact area satisfies T/t -> (H1-H2)^2/(2|z|); allowed signed z interval has total width (H1-H2)^2. Integrating two directional signs yields 2v int_0^pi g² per unordered pair; all three pairs give 6v int g². Weighted collision flux produces independent pair uniformity, angular g² tilt, (H_i-H_j)²/(2v) offset-pair size bias, original unused line and independent fair sign and uniform W in (0,1); T/t conditional ->1/W. Tail integration gives positive moment finiteness precisely p<1, and Cauchy–Schwarz gives 6v int g²>=6v/pi equality only uniform g. Independently calculated area from three line-intersections formula and simulated 500k iid uniform offsets/normal angles: t P(T>t) at t=20,60,200 was approx .639,.643,.635 vs exact 2/pi=.6366. Numerical agreement is corroboration; general limit rests on bounded collision decomposition/dominated convergence. Atoms in offset distribution only produce zero limiting weight at identical offsets.

## originality

PASS

PASS best-of-knowledge with a named inaccessible older paper: Finch (2011) and a published sharp tangent-triangle tail theorem analyze three tangents to a fixed incircle conditioned to enclose it; their offsets are deterministic common-circle support values, not iid bounded independent signed marks, so tail constants and conditional measures cannot be specialized as an implication. Daley–Ebert–Swift (2014) prescribes independent *side directions* and fixes one side to length one, yielding a different scale/offset distribution; its accessible abstract explains that setup, but full scientific text was unavailable via arXiv/OA and protected Oxford returned vpn_disconnected. An unindexed random-line area theorem may cover the iid-offset model, so priority is qualified. The claim is the variance-only coefficient with g² angular bias and full marked disintegration, not merely existence of 1/t tails in some tangent models.

## value

PASS

PASS: Infinite-mean area and exact Pareto coefficient for a naturally sampled triple of planar lines are meaningful invariants; their universality in the entire bounded iid offset family through variance, and extremization over continuous direction densities, have concrete geometric probability interpretation. The complete rare-event marks identify the large-triangle mechanism and supply a reusable disintegration, not just elementary tail calculus or a narrow unmotivated constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
