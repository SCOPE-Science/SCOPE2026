---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

From the actual closed-support within-color and vertex-coverage cubical model, independent combinatorial enumeration reproduced c0=114,c1=432,c2=378,c3=0. An edge consumes two supports in its color, and with three moving edges no stationary vertex supports remain enough to cover 4 vertices, proving dimension<=2. Frozen CHECK.py and grouped_general.py were read: signed boundaries have 1,512 nonzero d2 entries and square to zero; 305 integral unimodular unit pivots leave a 2-divisible residual, dividing by two gives exactly two unimodular pivots and zero residual, i.e. SNF 1^305,2^2, rank d2=307. Graph of 0/1-cells connected, d1 rank=113; H1 free rank 432-307-113=12, H2=378-307=71, H1 torsion (Z/2)^2. Finite exhaustive integral arithmetic, not mod-two alone.

## originality

PASS

Original grouped Stirling complexes paper defines exactly this closed cubical complex but its K4 table studies different quotas, and explicitly leaves broad homology calculations to future work. Resultary semantic searches for K4 2,2,2 integral torsion and alternate robot-configuration descriptions returned the assigned finding but no earlier matching exact homology or stronger implication. No available established theorem yields the two Smith 2 factors.

## value

PASS

The smallest complete graph supporting this natural three-color quota gives two independent torsion classes in H1 of a cubical robot-complex family; this is an exact unknown integral invariant and shows rational/mod-two-only counts are insufficient. Its object, quota and integral invariant are motivated directly by the grouped Stirling construction; no general family theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
