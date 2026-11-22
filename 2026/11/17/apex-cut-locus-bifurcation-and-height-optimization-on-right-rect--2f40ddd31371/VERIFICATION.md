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

C PASS: For a centered apex over [-a,a] x [-b,b], every apex-to-base path must enter the base through some edge. Its two segments have lower bound |v-q|+|p-q|, attained by a lateral-face straight chord followed by the base segment. Unfolding across each of four actual edges yields sites (+/-C_a,0),(0,+/-C_b); the straight image segment crosses inside the edge because C_a-x>=sqrt(h^2+a^2) and similarly on y edges. The four-site distance minimum is therefore globally exact, with no unexamined multi-face path. Bisector equations C_a x-C_b y=aC_a-bC_b produce the H-shaped Voronoi cut locus, branch nodes (+/-u,0), u=a-bC_b/C_a; at a=b they merge. Convex squared distance on each Voronoi cell reduces farthest-point candidates to its vertices. The branch-node squared distance exceeds the corner/lateral maximum by 2b sqrt(h^2+b^2)(sqrt(h^2+a^2)+bC_b/C_a)/C_a>0, so exactly the branch nodes maximize. L=2a-2bt+4b sqrt(1+t^2); t increases from b/a to 1 and derivative changes at t=1/sqrt(3). This proves the strict threshold a/b>sqrt(3), unique h_*^2=3a^2+3b^2-4sqrt(3)ab and min L=2a+2sqrt(3)b, with square constant case. Independent calculation compared the four-site maximum on 10,004 base grid locations in four parameter sets. Grid sampling is only corroboration, not proof.

## originality

PASS

O PASS (qualified): General source-image/Voronoi algorithms were already published by Miller–Pak; the a=b square-base restriction is also covered by an existing right-regular-pyramid note. Neither the inspected general theorem/algorithms nor the regular-base note states the complete nonsquare two-node cut tree and the sharp sqrt(3) height bifurcation. A general algorithm can derive a special case, but does not by itself state the explicit classification and optimal height. No stronger prior that already supplies both formulas was identified in the targeted searches. Specialist priority risks remain.

## value

PASS

V PASS: The cut locus of a source on a convex polyhedral surface is a natural intrinsic metric invariant. The two-trivalent-to-one-four-valent branch bifurcation, exact farthest surface points and sharp shape/height optimization supply geometry unavailable from the generic source-image method. The formula is an exact full-family classification, not a selected arbitrary numerical case; a square's height-independent length is a meaningful boundary phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
