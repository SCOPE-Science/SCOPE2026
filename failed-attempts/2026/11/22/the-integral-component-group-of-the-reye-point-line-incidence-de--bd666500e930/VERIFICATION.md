---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the classical cube model, each of the eight vertices lies on three edge lines and one body diagonal, the three axis points each lie on four parallel edge lines, and the center is on the four body diagonals. This is a connected 12_4,16_3 incidence graph. For an independent construction, identify the four even cube vertices with V4 and index each odd vertex q by w=q+111. Label the center by zero and the axis points by the three nonzero vectors 111+e_i. The line through even v and odd w+111 has third point labeled v+w. Building this V4 block-incidence graph and taking its exact integer Smith form yields 18 units and 2,8,8,24,24,24,24,96,96, independently at two roots. The determinant is 391378894848=2^29·3^6 and the full polynomial independently matches the stated one. The abstract curve made by gluing distinct markings on rational components is stable (valencies three and four), with genus 48−28+1=21. The node-smoothing parameters can all be chosen of order one by unobstructed deformation of a stable nodal curve, giving a regular split semistable family after algebraization; the conditional Néron identification is the ordinary graph component-group theorem. There is no inference about smoothing a spatial union of lines.

## originality

FAIL

A distinct indexed same-day record, aac34df26b9f, explicitly computes the complete integral cokernel for all four reduced Latin squares of order four, including the unique V4 square. The cube-parity relabeling gives a literal graph isomorphism from Reye to that table's incidence graph. The comparison also makes the same abstract genus-21 gluing and unit-thickness Néron identification. Thus substantive equivalent coverage is demonstrated, without determining priority or chronological order between the two records.

## value

FAIL

The Reye incidence object and exact component group are natural, but the proposed standalone value is the same complete integral invariant of an already covered graph and its standard application to the same abstract gluing. The graph identification is an elementary relabeling of the classical cube triples, not a new classification or a separate embedded degeneration. No distinct nonroutine exact invariant or geometric conclusion remains in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
