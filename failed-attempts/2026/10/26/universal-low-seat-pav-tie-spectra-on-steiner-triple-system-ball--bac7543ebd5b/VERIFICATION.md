---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Expand the Thiele weight in the first three binomial coefficients of the ballot intersection. The sums are k(v-1)/2, binom(k,2) and tau by replication, pair coverage and definition. Harmonic weights give coefficients 1, -1/2 and 1/3. Nondecreasing concave weights permit all signs: harmonic weights give positive, weights (1,2,2) give negative and linear weights give zero. Two blocks cannot fit in a four-set; three cannot fit in a five-set, since their union has size at least six. Counting intersecting block pairs and then block–committee incidences gives all three table rows, including the two exceptional orders and the five-seat winning proportion. For six seats each point has induced block-degree at most two, so at most four blocks fit. An independent enumeration from the two definitions checked all 105 pairs and 5,005 six-sets per design and returned Bose (315,2100,2170,420,0) and projective (420,1680,2800,0,105); the five-set vectors were both (1008,1680,315). The maxima and their multiplicities therefore agree with the finding.

## originality

FAIL

No identical election-spectrum statement was encountered, but the only design-dependent entry in either six-seat table is the Pasch count, already explicitly given for the exact same Bose and projective witnesses in Resultary record 8a313964a774. The other entries follow by triangular binomial inversion of incidence moments fixed by the STS parameters. In detail, the six-set factorial moments M_0 through M_3 at v=15 are 5005, 7700, 3430 and 420: count subsets, contained blocks, pairs of blocks split by whether they meet, and noncollinear triples of pairwise block-intersection vertices, respectively. M_4 is exactly the Pasch count: all six points must have block-degree two, forcing every pair of the four blocks to meet in a different point. The prior values 0 and 105 therefore recover the full frozen tables and winning counts mechanically. At three through five seats the analogous moments stop at degree at most two and are fixed by replication and pair coverage. For fixed k the conversion to Thiele and PAV scores is binomial interpolation on intersections of size at most three, not a new incidence invariant.

## value

FAIL

The structured voting example is natural and the counts are correct. But the small-seat formulas are parameter incidence identities and the specific six-seat boundary simply recovers the already established Pasch distinction in the same two systems by affine scoring and binomial inversion. The independently reproduced tables add no nonmechanically determined invariant for either witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
