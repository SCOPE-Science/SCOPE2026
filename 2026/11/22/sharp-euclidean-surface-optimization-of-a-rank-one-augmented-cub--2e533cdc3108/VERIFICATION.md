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

The corrected files are /workspace/repairs/1/RESULT.md and verify.py. The frozen exact optimum is correct, but the final displayed digit of the surface quotient with ellipsis was wrong: independent Decimal bisection and evaluation gave t*=0.4286306377334204013764… and 5.7626370245621151604897…, not 5.762637024562116…. Replay via python3 /workspace/branches/reproduce_decisive.py. Splitting x into capped coordinates and nonnegative excess gives the maximum-over-subsets inequality and the measure-zero-wall volume decomposition. Maximizing a subset sum on each summand gives the full simplex-times-cube face, including the singleton (whose deleted-subset inequality argument in the frozen proof was incomplete) and full subset. The lower coordinate facets are copies of the smaller body. All faces have codimension one and exhaust the defining inequalities. The simplex Gram matrix has determinant k t^(2k−2), with the empty Gram determinant 1 for k=1. At zero the subset inequalities of size at least two become redundant, and the volume and area polynomials have the cube limits. In 3D direct expansion gives the displayed derivative cubic, whose negative constant and positive other coefficients make it strictly increasing on t≥0, with exactly one positive root. The derivative sign and positivity of the volume ensure the global equality statement after unit-volume scaling. The repaired script's symbolic identity agrees with the independent expansion; uploaded hull code was inspected, not run, and is only supplementary.

## originality

PASS

The repaired assessment claims a distinct exact 3D fixed-volume optimizer, not novelty for the volume polynomial or the orthant-accessible subset-facet spectrum. The corrected result explicitly credits the orthant reduction to the earlier cube–crosspolytope geometry.

## value

PASS

A Euclidean surface optimum for the natural interpolation between the normalized cube and simplex need not occur in the interior or be unique. Here it does, with a sharp exact equality shape, demonstrating that moving away from either pure endpoint can improve the fixed-volume surface within the family. The full facet bookkeeping explains that interpolation. This value assessment is for the surviving sharp optimization, not the correction of one digit or the Gram formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
