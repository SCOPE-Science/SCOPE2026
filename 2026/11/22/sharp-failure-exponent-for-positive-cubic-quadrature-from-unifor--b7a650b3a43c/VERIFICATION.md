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

Ignore isolated zeros when listing the negative sign intervals. If their total length is less than 1−g, terminal-only negative regions exclude both Gauss nodes, which cannot both be even-multiplicity zeros of a nonzero cubic. The all-negative pattern already has excessive length. For a single interior interval, the affine factor in (x−a)(x−b)(alpha+gamma x) is nonnegative on the support, so nonpositive mean forces 1+3ab≤|a+b|, whence the half-width squared is at least (|midpoint|−1/3)^2+2/9. For the mixed pattern, write the terminal root as −t and the width of the interior negative interval as v. Under the putative shorter length, g<t≤1 and 0<v<t−g. Completing the square bounds the necessary nonnegative quantity a+b+c+3abc by −t+1/(3t)+3tv²/4<(3t²−1)(t²/4−1/3)/t<0. Reflection covers the opposite pattern. The exact zero-mean witness (x+g)^2(g−x) saturates the support bound and forces failure on the event all nodes are below g, modulo a null event. The distinct nodes form a full-dimensional simplicial hull by the Vandermonde determinant. An outside target violates a facet inequality; for each triple and orientation the remaining nodes are iid conditionally, so the support bound gives the stated union bound. Boundary membership has probability zero because the triple-root cubic mean is a nonidentically-zero polynomial of three continuous roots. For an interior target, mixing in a sufficiently small positive multiple of the sample centroid leaves another point of the hull, hence gives a representation with all weights positive. These facts imply both the stated finite bounds and the root limit.

## originality

PASS

Pass for the sharp depth calculation for the uniform three-coordinate moment curve and its numerical cubic-quadrature consequence. Hayakawa–Lyons–Oberhauser already provide the general depth-to-convex-hull failure bound, even for singular laws; once the depth is known it gives the same rate and a stronger finite upper bound than this record. The distinct mathematical work is the sharp cubic sign-support calculation, not the general random-hull or depth mechanism. No inspected source supplies that depth for this law or otherwise implies the cubic numerical constant without an additional extremal argument.

## value

PASS

The exact depth distinguishes quadratic from cubic exactness for the same random-node law and sets a sharp exponential confidence scale for cubic positive quadrature. The extremal polynomial and sign analysis identify the precise obstruction in a natural fixed moment problem; this is useful independently of the standard convex-hull reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
