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

At inclusive length two every nondegenerate 2-cell is a two-step unit-edge walk; there are no higher cells. Distinct endpoints give distance two by triangle exclusion and have a unique common neighbor by square exclusion. Each ordered shortcut is therefore an embedded free side of its sole triangle and can be removed with that triangle; opposite shortcuts are distinct. The residual complex has a pair of directed arcs and two disks along their bigon for each unoriented edge. A backtrack disk is a disk with the degenerate side collapsed to a point. With one disk per edge, collapse each disk against one arc to get the ordinary graph. The other disks have nullhomotopic attaching loops and add one sphere each. The two normalized disks have the identical primitive boundary b_uv; their difference generates the degree-two kernel on that edge, and graph automorphisms transport these differences with a sign when the edge is reversed. For H1 the sum b_uv is invariant under reversal. Quotienting the directed-edge chains by the sums gives exactly the signed ordinary graph chains, and every graph cycle lifts to a cycle because boundaries factor through that quotient. This proves primitivity, natural exactness, and the field-wise ranks. For C3, there are 12 triangles and 6 arcs; the three bigon relations and the triangular graph cycle give boundary rank four. For C4 there are 16 triangles and 12 arcs; eliminating the four ordered opposite-pair shortcuts leaves the four bigon relations and the square cycle, for total boundary rank nine. The excluded examples therefore give (0,8) and (0,7), respectively. These are integral arguments independent of the recorded finite-field tests.

## originality

FAIL

A distinct indexed result on the SAME ordered length nerves has a proof that specializes to the target cutoff without a new lemma. Its formal headline is for cyclic graphs and L>=3; this is proof-level coverage, not a claim that the headline includes L=2 or that the two same-date records have a known ordering. Its explicitly L>=2 tree calculation supplies the tree case. For cyclic graphs, its short-length lifting and Whitehead steps require 2L<g and continue to hold at L=2. Its explicit parity calculation becomes the target signed cycle. It also identifies the embedded graph on one directed arc per edge as a fundamental-group isomorphism; the backtrack disks identify the other arcs with the inverses, so the persistence map is precisely the projection of the doubled graph onto the ordinary graph. Thus the unsigned primitive kernel is a direct consequence. The elementary collapse is a shorter proof of these overlapping statements; the small excluded examples do not constitute a separate substantive remainder of the frozen claim.

## value

PASS

The first nontrivial length stage is a natural invariant of the filtration: the homotopy classification has branching and cycles built in, and the signed versus unsigned module distinction detects structure invisible to Betti numbers. The short-path collapse is a useful presentation. This assessment of the mathematical question's substance does not establish originality for the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
