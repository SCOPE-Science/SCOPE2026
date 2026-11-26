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

I checked the fixed F11 polynomial and its homogeneous gradient directly modulo 11, not just the named curve. Fermat's identity requires all three coordinates and their sum to be nonzero at each of the 91 rational curve points; the gradient vanishes only at [1:1:1]. Normalizing the 90 other gradient images gives 72 distinct lines. The direct integer replay /workspace/branches/tangent_exact.py starts with the three mandatory lines from incidence rows with one eligible line. It branches on an uncovered point by the first chosen incident line in a fixed order at that node, partitioning all possible covers. The only lower-bound prunings use pairwise disjoint remaining candidate sets (each needs a distinct chosen line) or the sum of the largest remaining coverage gains (which overcounts overlaps). It checks every cover of at most 18 lines, terminating fully after 264595 nodes, with nothing below 18 and exactly six at 18, each with profile {1:90,2:15,3:25,7:3}; see tangent_exact.log alongside the script. No global p=11 blocking-set shape theorem is needed for this direct completeness check. The separate triangle-only replay independently tested all 59640 triples (55129 noncollinear) and four coset patterns per noncollinear triple. The sign relation follows because v+uw=0 for the three open-side intersections with a line missing the vertices, so a blocking pattern cannot admit a line meeting all three complementary cosets. The triple replay gives exactly the same six subsets, all projective triangles, and includes the earlier explicit witness. In both outputs these are its six distinct coordinate-permutation images, so there is no stabilizer. Triangle replay and coefficient sets: /workspace/branches/7c47caf8-def0-4dcb-a83f-9fbaa65435e3/independent_replay.py and independent_replay.out. The uploaded verify.py and its notes were inspected but not executed.

## originality

PASS

Best of knowledge, the supported new claim is exhaustiveness inside this fixed rational tangent configuration: exactly one orbit and no further optimal subsets. Minimum size, one explicit projective-triangle cover, and the individual profile of that witness have prior coverage. Coordinate invariance already produces the images of the witness; it is not on its own an argument ruling out another orbit.

## value

PASS

For a named tangent-filling curve with a previously exhibited optimum, knowing the minimum did not tell whether many geometrically different optimal covers coexist. Exhausting actual tangent subsets settles this concrete rigidity question: every optimizer is obtained by permuting the coordinates of one known witness, with no other symmetry class. The fixed object, the optimization constraint, and the symmetry quotient are motivated by the existing construction; the answer determines the entire optimal design space rather than rechecking the known minimum or an abstract shape theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
