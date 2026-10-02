---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The construction and inequalities are correct. The function defining the body is smooth, even and strictly convex; the sandwich between the scaled cross-polytope and the cross-polytope follows coordinatewise. The cross-polytope volume product is 32/3. The norm/trace argument gives Banach-Mazur distance at least 3/2 from centered parallelepipeds, and the symmetrization argument reduces translated parallelepipeds to centered ones. Scaling the inclusion gives the stated distance lower bound for the smoothed body, and polarity plus the sandwich gives the stated volume-product upper bound. The integer inequalities in the verifier confirm the numerical thresholds.

## originality

FAIL

Originality fails because the decisive phenomenon is already contained in the published equality characterization for the three-dimensional symmetric Mahler theorem: equality occurs when a body or its polar is a parallelepiped, so centrally symmetric octahedra are equality cases far from the parallelepiped class. Smooth strictly convex approximation and continuity then already rule out any positive stability gap measured only from parallelepipeds. The record's explicit smoothing and constants quantify this known obstruction but do not create it.

## value

FAIL

The exact numerical witness is clean, but it exposes an immediate boundary-condition error: the comparison class omits the polar equality branch already present in the known Mahler equality theorem. The smoothing and constants are routine once that branch is noticed. This is a useful falsification of the proposed cell, but under the required value standard it is not a substantive new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
