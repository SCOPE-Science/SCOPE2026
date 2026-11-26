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

Three closed neighborhoods contain at most 15 vertices; the displayed four-set dominates. The parity coverage inequalities force two selections per parity. Antipodal same-parity pairs cover the opposite parity; distance-two pairs force the two uncovered opposite-parity vertices, which in turn cover the complementary neighborhoods. This gives precisely 16+24 optimizers in two isometry orbits. The 2,517 subsets of sizes 0–4 were independently enumerated, with all 120 pairs and 560 triples tested; full representative rows and the 400/160 missing-pattern split agree with the frozen tables. Independently, pair co-membership counts 1,1,4,4 follow from the two optimizer types. Triple co-membership is 1 for distance patterns (1,3,4) and (2,3,3) and 0 otherwise, which along with single vertex frequency 10 recovers all rows by inclusion-exclusion. No triple is shattered, so downward closure leaves exactly K16, homotopy equivalent to a wedge of 120−16+1=105 circles. In any depth-four tree the ten-concept positive first branch would need depth three; a next query either gives a singleton child or a four-concept child with pairwise disjoint remainders, whose depth is at most one. The displayed witness supplies depth three, and independent recursion also returns 3 and verifies all eight leaves.

## originality

PASS

Best-of-knowledge pass for the uniform trace law and the sharp adaptive–static learning gap on this specific optimum-code family, not for the covering-code classification. The same-family code literature is a real but unresolved source risk; available primary passages and the strongest distinct catalogue comparisons do not contain or imply these learning results as stated.

## value

PASS

The optimizer family is the complete natural radius-one covering problem on the four-cube, not a selected sample of concepts. Its uniform near-shattering is stronger than a VC dimension, and the sharp positive-branch obstruction plus adaptive witness explains when queries can outperform static shattering. Q4 is a natural small cutoff: for Q1 the optimizer family consists of singletons, for Q2 all pairs, and for Q3 antipodal pairs, giving equal static and adaptive dimensions in each of those smaller cases. The precise Q4 data are meaningful for comparison with other optimizer families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
