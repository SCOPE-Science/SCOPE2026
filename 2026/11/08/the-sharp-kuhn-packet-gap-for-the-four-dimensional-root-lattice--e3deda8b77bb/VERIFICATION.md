---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The original common-frame κ(B2^4,D4) requires one independent 4-frame and all 24 permutation-prefix simplices, each with its own enclosing ball. D4 consists of even-coordinate-sum integers; every squared norm is even. Any frame with max packet radius <sqrt(6)/2 would have all nonempty subset sums norm²<=4, forcing 4 independent vectors from the 48 D4 vectors of squared norm 2 or 4. Exact Gram-rank/backtracking enumeration of ALL ordered such prefix frames yields counts (1,48,816,1728,0), a legitimate exhaustive cutoff for all frames. A displayed determinant-2 D4 basis has for each permutation a midpoint ball through a diameter pair, 12 with radius²1 and 12 with radius²3/2. Thus κ=sqrt(3/2). Nearest integer rounding with an even-parity correction yields D4 covering radius at most1 and the integer vector (1,0,0,0) yields at least1. Independently ran exact integer recursion and verified every midpoint certificate and class count.

## originality

PASS

The original Kuhn packet invariant and subset-sum diameter lower bound are Xue prior work, but no inspected theorem already computes the four-dimensional D4 strict gap or exhibits its matching 24-simplex certificate. Nearby A4 and D3 calculations are for distinct lattices/dimensions, not a D4 implication.

## value

PASS

Gives a concrete, sharp, naturally motivated difference between the classical covering radius and the recently defined common-frame Kuhn-packet invariant on the important root lattice D4. The exact 48-vector obstruction, sharp basis, and all-24 simplex certificate provide an independently useful structural finite classification, not a mere calculation of known μ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
