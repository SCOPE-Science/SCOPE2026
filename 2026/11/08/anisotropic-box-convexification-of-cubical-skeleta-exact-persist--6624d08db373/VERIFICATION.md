---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For d>=2,0<=r<d, ai>0, lambda>=0 and closed cubical faces, the coordinate endpoint-capacity criterion is iff at most r open central gaps in the enclosing Q_lambda. Sorting ai yields convexification iff s<=r with equality included. For surviving narrow axes, interval clamping to [delta_i,1-delta_i] and wider axes to 1/2 is a fixing strong deformation retract of X_lambda to the r-skeleton of an s-cube; it preserves endpoint-admissibility throughout. CW connectivity and Euler counts give wedge b_r(s) S^r (r=0: b+1 components). A face section with newly dropped coordinates fixed at 0 maps into earlier X_lambda and surjects onto later r-homology; finite-type persistence has births all 0 and deaths at tie-collapsed thresholds. The box is partitioned by gap vs endpoint membership; for a subset I with >r gaps, lengths factor exactly as stated. At lambda*=1/(2 a_(r+1)), t earlier gaps and m equal critical widths force h=r+1-t>=1 critical gaps, with all lower powers zero and positive K. Independent fresh sympy exact polynomial expansion independently verified leading coefficient and positivity for 540 random rational width/rank instances d=2..7, and Euler recurrence over 990 (s,r), 1530 groups total. This is bounded corroboration only; the all-d claim follows from the proof. The d=4,r=1,a=(1,2,3,5) barcode 17->5->1->0 matches the formulas, and lambda=0 and simultaneous ties have correct endpoint conventions. No observed mathematical gap.

## originality

PASS

Qualified best-of-knowledge: the isotropic sharp convexification threshold is already a corollary of the product-of-simplices central-witness theorem and static wedge Betti numbers are classical. The Resultary cubic subdivision/Minkowski-average theorem uses m-fold sums of the NONCONVEX skeleton, not one continuously scaled convex box; its cellular skeleton, fixed-count discrete averaging parameter, and Hausdorff outputs do not imply the claimed inclusion maps or anisotropic gap volume. The published simplex-offset staircase uses a SIMPLEX and has dimension-changing homology; it is not a reduction giving this persistent fixed-r cubical filtration. Meyers general finiteness theorems, inspected in full HTML theorem/selected proof sections, do not state this explicit module or tie-sensitive void asymptotic. Rowlands co-skeleton complement and iterated-hyperplane results use no lambda box-offset filtration. No decisive stronger coverage found. These are noncoverage comparisons of the specific inspected sections, not a claim of exhaustive historical priority.

## value

PASS

The r-skeleton of a cube is a canonical nonconvex model in digital/cubical topology. Its complete axis-aligned anisotropic offset filtration is a natural and motivated family, not an arbitrary slice: explicit topology, all inclusion maps, exact gap volumes, and a tie-sensitive extinction exponent quantify how dimension-dependent holes disappear. Knowing the static cubical Betti numbers or a convexification threshold does not determine these maps and volumes. This is a self-contained structural classification across every dimension and rank, suitable as a test case for weighted morphology, without claiming arbitrary convexifiers or a novel general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
