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

At almost every direction, differentiability of a support function gives a unique support point and tangential coordinate h'; the normal lines are parallel and their offset difference is |f'|. The support functions are Lipschitz, so zero distance is equivalent to constant f, hence to the indicated outer-parallel-body relation by support-function additivity. For the upper bound, the distribution f'' is a finite signed measure; the periodic finite-difference remainder integrated against its variation is bounded by a^2 TV(f'')/2, also for intervals exceeding one period. Optimizing the resulting 4 pi ||f||_infty/a + a TV(f'')/2 bound on the derivative integral gives the stated constant. Independently, periodic mollification and integration by parts give integral |f'|^2 <= ||f||_infty TV(f''), so the asserted constant is admissible but not optimal. The support-curvature measures have masses P(K), P(L), which gives TV(f'') <= P(K)+P(L)+2 pi delta. Equal perimeter implies mean f=0; the periodic variation is at least twice its oscillation, and for distinct bodies the oscillation strictly exceeds ||f||_infty. The normalized smooth narrow bump has half-variation 1 and sup norm tending to 1; choosing its amplitude sufficiently small preserves positive curvature and disk containment, and scaling gives sharpness at any fixed positive perimeter. The cosine perturbation has curvature radius at least 3/8, common perimeter 3 pi/2, delta=e_n of order n^-2, and distance 2 n e_n, excluding every larger small-distance exponent. The upper estimate is uniform at bounded distances, not a global pure square-root bound under arbitrarily large relative translations. The supplied quadrature and arithmetic checker was inspected, not executed; those tests are not the universal proof.

## originality

PASS

The distance, qualitative degeneracy example, support coordinates and interpolation ingredients are established or elementary. The distinct contribution supported by the comparisons is the joint sharp inverse coefficient and forward exponent for the synchronous normal-line distance at one perimeter, with both sharpness regimes realized under smooth convexity constraints, not priority for a standard interpolation estimate.

## value

PASS

This quantifies what can be recovered in the ordinary Hausdorff metric from an established but degenerate normal-line distance, and where the converse loses regularity. The strict but sharp inverse ratio and the different high-frequency obstruction at the same perimeter give genuinely useful geometric limits, even for smooth bodies in a fixed disk. The value is not a new qualitative convergence argument or an optimal forward numerical constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
