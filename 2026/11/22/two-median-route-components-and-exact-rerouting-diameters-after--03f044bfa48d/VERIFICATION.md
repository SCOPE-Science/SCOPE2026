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

Independently checked RESULT.md §§Assumptions and Proof and inspected VERIFICATION.md and VERIFY.py without executing the supplied code. Both boundary extreme routes survive, so the Manhattan lower bound is attained and all shortest routes are monotone. A route visits the failed vertex exactly when h_j <= i <= h_(j+1); alternatively, on the diagonal i+j the east coordinate is strictly below or strictly above i. A one-vertex move changes that diagonal coordinate by at most one and swaps adjacent unlike steps, so cannot cross the deleted level. The two allowed profile sets are the claimed order-ideal intervals. Removing and adding differing cells through the intersection gives exact Hamming/L1 length, and majority membership is an ideal in the interval and is the unique metric median. The cube on the difference of the extreme ideals gives an upper dimension bound, and the distance between the extremes gives the same lower bound for every isometric cube embedding; this proves the diameter and dimension formulas even for singleton components. Splitting at the north step from height j (upper) or the east step from abscissa i (lower) gives exactly the stated two binomial products in each sum; splitting forbidden paths at the failed vertex checks their total. At a=b=2, i=j=1 both intervals have one route and diameter zero. The proof is all-size; the recorded BFS is only finite corroboration.

## originality

PASS

Credit the staircase representation to intact-grid work and credit equivalent coverage of the structural and metric part by the arbitrary-fault sign-fiber theorem. The distinct supported contribution is the explicit simultaneous enumeration and geometry for an arbitrary single interior hole, particularly the individually resolved component-size formulas; these counts are not supplied by the broader theorem or by planar reachability. The overlapping same-day text itself credits a previously available one-fault classification with these sizes and diameters and does not name an independent earlier source for them. The snapshot does not establish within-day priority; no priority claim is made for the structural assertions.

## value

PASS

The one strict interior fault is the smallest change that separates feasible shortest routes while preserving their length. Exact separate route populations and move budgets at an arbitrary location quantify how that single change fragments the routing problem, including extreme asymmetric and singleton cases. The concrete all-position classification is useful independently of novel median-graph theory; neither a reachability algorithm nor the total number of avoiding routes answers these separate sector questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
