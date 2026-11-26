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

Independently solved the two local moment equations in RESULT.md lines 26–34: the traces are A=1−4t+3t² and B=1+2t−3t². The one-cell slope contribution has maximum 3/2 at t=1/2. The first-cell profile is 8t−9t² through t=2/3 (max 16/9 at 4/9) and 4t−3t² thereafter; reflection gives the last cell. An interior cell gives the middle profile 12t(1−t)−1 (max 2 at 1/2), while the outer branches peak at 5/3. Interior knot steps are reproduced with variation 1. On a finite interval a BV function is a constant plus the integral of step kernels against its finite signed derivative measure; the step map is L²-continuous in its location and the bounded projection commutes with that integral. Applying the triangle inequality to its finite vector of slopes and trace differences gives the full upper bound, and the indicated steps attain it on any mesh. The two-input result follows by linearity. This is the real, unweighted, distributional seminorm on the open interval, not the L¹-plus-variation norm or variation of a zero extension. The supplied checker was inspected but not executed; its expected finite tests are not required by the proof.

## originality

PASS

The exact cell-count transition for the full jump-inclusive variation of the broken affine orthoprojector survives the inspected comparisons. Neither a generic FE stability statement nor agreement on the operator alone gives these sharp output-variation constants.

## value

PASS

The underlying projection is standard and the input class is natural for discontinuous signals. A sharp bound for the actual TV amplification, including interfaces, calibrates reconstruction: it distinguishes one/two-cell edge effects from the interior obstruction, is uniform in grading, and is witnessed by simple inputs. It is not just a recomputation of an L¹ error, a conforming norm, or generic boundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
