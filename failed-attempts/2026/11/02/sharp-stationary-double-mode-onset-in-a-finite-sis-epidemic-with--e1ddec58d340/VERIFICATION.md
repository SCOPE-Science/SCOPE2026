---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Detailed balance gives π_{k+1}/π_k=(n−k)(a+bk)/(k+1). The sign above one is a concave quadratic in k (decreasing affine at b=0), with initial sign na−1 and limiting sign negative at k=n. If na≥1 there is one modal component. If na<1 the first edge is strictly downhill, and a separated positive-count component exists exactly when at least one k≥1 edge strictly rises, i.e. b>min h(k). The positive edges form one block; exact ties can widen a plateau but cannot create a second rising block. In particular equality at b_c gives a nonincreasing law and n=2 allows a second mode at the upper endpoint. With c=1−na, the derivative of h has sign (1+a)k²+2ck−nc, which gives z_* and the clipped two-candidate rule. At a=λ/n with fixed 0<λ<1, z_*=√(cn)−c+O(n⁻¹ᐟ²), h(z_*)=c/z_*² and integer rounding costs O(n⁻⁵ᐟ²) by the second derivative near z_*; this gives the stated expansion. The minimizing k is an edge index, not necessarily the exact position of a mode. The mean-field drift has opposite signs at 0 and n and is concave (strictly decreasing affine when b=0), so it has one feasible zero. The conventional 1/(n−1) comparison is not a bifurcation in that imported ODE. Frozen checker and recorded results were read but not executed; the candidate test there uses a float square root. `python3 /workspace/branches/review_reproduction.py 2` separately verified exact derivative signs, ties at every adjacent-mass equality in its finite grid, and strict and plateau modal witnesses.

## originality

FAIL

The current indexed corpus records the exact same count-mode theorem, with a stronger lattice formula and more precise asymptotics, in 0844626cea2d. The difference between SIS and finite-capacity logistic terms is a rate normalization, not a different transition law or statistic. This is a finding of demonstrable coverage, not a ruling about who derived it first: the equivalent indexed record has a later catalog path. The inaccessible earlier papers do not justify the negative decision and no earlier exact theorem is inferred from them.

## value

FAIL

The exact local-mode question and square-root onset would be valuable as a distinct classification, but the theorem, two-candidate rule and scale are already furnished by the exact indexed population-count theorem. Reexpressing the rates in epidemic notation and giving a rational witness do not add a new scientific conclusion or a viable narrower repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
