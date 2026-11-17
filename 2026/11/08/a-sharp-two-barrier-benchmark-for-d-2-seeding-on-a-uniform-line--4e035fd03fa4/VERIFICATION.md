---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For equal-weight regular grids Dn⊂[0,1], ordinary k-means++ chooses X uniform and second point with D² weights; there are precisely two seeds, no Lloyd update, optimal comparison centers may be real. The continuum conditional density is (y−x)²/V(x), V=x²−x+1/3≥1/12. Splitting the Voronoi integral at (x+y)/2 and independently integrating exact polynomials reproduces Q(x)=(-66x^6+198x^5−135x^4−60x³+105x²−42x+7)/360 and E C=−3/400+11√3 π/1215. The continuum optimal two-mean cost is 1/48 at 1/4,3/4; uniform Riemann-sum convergence of both expected sampling objective (denominator bounded below) and compact minimization justifies limit from grids. Hence exact ratio 176√3 π/405−9/25≈2.0046569489>2. Independent symbolic integral and Q polynomial differences checked to zero. Does NOT claim a worst-case data set optimizer, finite-n formula or post-refinement cost.

## originality

PASS

Arthur–Vassilvitskii defines D² seeding; Bamas–Nagarajan–Svensson analyzes global D^α approximation guarantees; neither inspected result supplies this canonical uniform-line k=2 exact integral, and the two-dimensional worst-case construction cannot by itself imply the one-dimensional closed constant. Resultary exact-constant search returned only the candidate; other two-facility lotteries use different sample rules. A failed search does not establish historical priority.

## value

PASS

Two-seed k-means++ on the uniform interval is a canonical, geometry-minimal test of a widely used random initializer. Its exact expectation and strict >2 limiting ratio show that even this noise-free regular input defeats a putative factor-two bound. The excess is small and no practical algorithmic improvement claimed; the exact natural baseline is still a meaningful mathematical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
