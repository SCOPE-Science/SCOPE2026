---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Checked the actual Higashine theorem: A_t corresponds to b^q=t, B_c ranges over all k, D_d over K, and the group types match. P is uniquely infinitely incident; any other plane contains at most three lines, from the conic of B directions and the pencil of D lines. The q² dual points on a smooth conic force conic preservation by Bézout; three K-points then force a K-rational Möbius map, with ∞ fixed as the missing K-point. The projectivity on H is uniquely determined by the conic action (four conic points form a frame). In the extension off H the B_c identity forces δ=a² and w=v²/a². Direct substitution gives all three claimed permutations, so the group is exact, with additive two-dimensional kernel and the finite affine section. Norm-one is necessary and sufficient to preserve the nonzero D label partition. Translations give C_{L_q(u),v}; surjectivity and coefficient comparison prove distinctness in (s,t), not in (u,v). Each s has q/2 preimages, already stated in the original. Projective conjugation preserves projection group isomorphism types. The statement is on geometric lines/reduced group, not the nonreduced stabilizer scheme. Replay: frozen Proof §§1–5; inspected VERIFICATION.md and CHECK.py without executing; finite field checks do not prove the geometric stabilizer.

## originality

PASS

The complete stabilizer of all geometric lines, its label restriction and labelled embedded non-reconstruction are distinct from previously inspected curve automorphism, line classification, and finite-plane incidence results.

## value

PASS

Determines the complete geometric symmetry group rather than selected symmetries, identifies exactly the information lost on forgetting group labels, and exhibits a full two-parameter family of distinct ambient curves still indistinguishable even with the labels. This is a concrete reconstruction obstruction, not just a relabelling of the known classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
