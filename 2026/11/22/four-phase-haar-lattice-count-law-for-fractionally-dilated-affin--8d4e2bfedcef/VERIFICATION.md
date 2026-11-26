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

Independently verified all mass polynomials, not just finitely many pairs (n,t). Represent lattice points by triples (i,j,-i-j). For a generic translation take coordinate fractional parts f=(x,y,{-x-y}); they sum to 1 or 2, and central inversion exchanges the two halves without changing the count. On f_1+f_2+f_3=1 they are uniform on the simplex. Removing the integers from the translation makes the counting triples sum to 1, with coordinate bounds [-n+b_i,n+a_i], b_i=1_{f_i>t}, a_i=1_{f_i>1-t}. Let B=sum b_i. Counting via three-variable stars-and-bars and subtracting single upper-bound violations gives C(3n+3-B,2)-sum_i C(n+2-B+b_i-a_i,2); double violations are impossible and the displayed ordinary binomial arguments are nonnegative for n>=1. A box in the simplex specified by intervals between 0,t,1-t,1 has normalized area sum_{J subset {1,2,3}}(-1)^|J|(1-sum of the three endpoints)_{+}², choosing upper endpoints only in J. Only the ordering at 1/2 and the nonpermanent events sum of endpoints=1 at 1/3,1/2,2/3 can change this polynomial labeling. In checks/3.py (Python 3 and SymPy) I enumerated the interval labels and aggregated exact coefficient pairs (coefficient of n, constant term) for the support and exact quadratic coefficients for the masses. All four tables, transitions, endpoints, means and variances agree, with no restriction to tested n or t. Counts converge almost surely as t approaches a transition since the finitely many count-change boundaries at that t have zero area. All listed positive masses are supported on distinct counts for n>=1 on the open phases. The scaling limit follows on dividing each support shift by n and merging coincident limiting atoms. The frozen interpolation argument should read its triple-intersection statement as referring to changes of incidences, not permanent concurrences; the separate exact simplex calculation resolves the event and uniform-in-n checks directly.

## originality

PASS

The supported distinct result is the full fractional-radius law for the specified hexagon and lattice, with all transition locations and quadratic masses. The mean and integer-radius count constancy are known and earn no separate novelty credit. Prior integer-polytope translation theory does not mechanically give the fractional laws, and the same-day planar diamond law is for a non-affinely-equivalent body. This is a bounded judgment; unresolved full-text access to Huxley–Žunić is recorded explicitly.

## value

PASS

In a natural six-facet lattice norm, area and integer multi-tiling identify the mean and integer endpoints but not the translated occupancy fluctuations. This uniform law gives the exact generic four-atom statistic and its distinct phase boundaries for all scales, including collapse to two or three atoms at the transitions. It is an exact, useful case for studying fractional departure from lattice multi-tiles, not just a sampled variance or single-radius recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
