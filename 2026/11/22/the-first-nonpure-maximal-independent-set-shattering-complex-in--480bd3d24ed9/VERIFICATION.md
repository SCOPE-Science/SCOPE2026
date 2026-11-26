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

Reconstructed the concept class as inclusion-maximal independent sets, not maximum independent sets or neighborhoods. Independently tested each trace T on an independent support S of size at most five by branching on witnesses: every omitted vertex must have a neighbor in an independent set containing T and avoiding S minus T. This condition is necessary and sufficient by maximal extension, so the test does not depend on enumerating the supplied concept list. It recovers the four face vectors (1,2), (1,4), (1,8,16), (1,16,88,160,104); no size-five face shatters and larger ones are excluded by heredity. The facet size-counts are respectively {1:2}, {1:4}, {2:16}, {2:8,4:104}. The union of the four stated isometry orbits equals the actual Q4 facets, with sizes 8,16,24,64, and the distance test agrees for every triple. All cube automorphisms are translations followed by coordinate permutations: an automorphism fixing zero is determined by its permutation of the neighbors, since the distance vector to zero and its neighbors determines any vertex. This proves the first nonpure case with the scope stated, not a pattern for larger cubes. The Python 3.8 minimum in the notes is too low for int.bit_count(), but the complete finite certificates are otherwise appropriately described. Replay recipe: /workspace/branches/independent-math.md, section 4.

## originality

PASS

The strongest distinct same-day result explicitly proves the same Q4 polynomial, VC dimension and size/count profile of facets including their antipodal pairs as part of a perturbation comparison; those numerical facts and Q4 nonpurity are materially shared, not an independently distinct contribution. Same-day metadata does not resolve priority. The supported distinction is the complete cubical orbit/representative characterization of Q4 supports together with the exact first-nonpure boundary through Q1–Q3. The comparison theorem's orbit classification is for the modified folded cube, not Q4. No inspected earlier primary text provides that combined classification; the inaccessible Ignatov chapter leaves a named priority risk.

## value

PASS

The useful result is a complete symmetry-reduced criterion for every query support, together with the first failure of purity along a natural sequence, not another measurement of the number of maximal independent sets or the already shared Q4 coefficient vector. In dimension four an antipodal pair becomes a genuine smaller maximal face even though larger faces exist; this identifies exactly how equal-size facets, and hence matroidal structure, fail at the boundary. Choosing one representative per isometry orbit makes the classification usable in subsequent comparisons with perturbations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
