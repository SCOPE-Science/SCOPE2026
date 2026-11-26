---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An independent exhaustive Python census (/workspace/checks/kempe_gp83.py, run with python3) checks all eight-edge subsets for perfect matchings and all pairs of distinct named states for a move. Properness forces the changed support for a given transposition to have degree two at each moved vertex; its connectedness is thus exactly the one-cycle condition. Projecting named adjacencies and dropping loops gives 33 matchings, 20 partitions and 27 quotient edges. The stated bijection sends the complete 16-state component edge set to the base-graph edge set; the other component is the claimed star. Breadth-first distances from all named states confirm components of size 24 and 96, edge totals 54 and 288, the degree histograms and radii/diameters 3 and 4. The frozen transcript is consistent with, but is not the basis of, the independent count.

## originality

FAIL

The 2026-10-12 source e12726c83181 already states and certifies the same one-cycle color-permutation quotient, including the exceptional self-copy, the star, and all quotient sizes. This is demonstrated equivalence of the central finding, not just familiarity with the two-class result or a similarity of titles. Earlier coverage of the auxiliary named-graph radii and diameters was not established.

## value

FAIL

The self-copy would be a useful structural fact if uncovered, but is an exact repeat of an already proved natural invariant. Most named-graph sizes and degree data are consequences of the older cycle profiles. The remaining matching count and named distances are correct ancillary census data; this record offers no separate mathematical motivation for needing those precise numbers beyond checking the known self-copy. They do not support retaining this as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
