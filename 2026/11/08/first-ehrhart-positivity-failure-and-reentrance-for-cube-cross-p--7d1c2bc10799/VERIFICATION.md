---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For J_{p,q} the integral join-height section gives sum_{s=0}^t (t-s+1)^p * |s X_q cap Z^q| with |s X_q|=sum_j 2^j binom(q,j)binom(s,j). Therefore the Ehrhart series equals A_p(z)(1+z)^q/(1-z)^{p+q+2}. All ordinary coefficients can be computed exactly by integer arithmetic. Exhaustive p,q>=1, p+q<=17 (136 pairs) finds strict positivity through d=17 and precisely two d=18 failures (14,3), (16,1), each only at t^1, with coefficients -10397/510 and -897/170; p=14, q=2,3,4,5 has sign pattern +,-,-,+, and q4/q5 linear coefficients -76729/3990, 618397/67830. All boundary and quantifier ranges checked; no unbounded-dimension theorem.

## originality

PASS

The general Ehrhart join product identity is prior and directly yields the formula from Eulerian numerator and (1+z)^q. Nonetheless the sharp parameter-wide positivity comparison requires coefficient extraction and a finite complete sign classification absent from the cited source. A general existence counterexample cannot imply the exact first failure or reentrance. Liu–Tao–Xin prove join generating-series multiplication and that some joins of positive factors have negative coefficients (including a 100-times dilated four-cube). This general nonpreservation does not imply exact undilated U_p-X_q coefficient signs. The published all-p cube+unit-segment classification is a different segment lattice length and does not dominate arbitrary q cross-polytopes.

## value

PASS

Sharp minimum ambient dimension 18 and two exceptional parameter pairs furnish an exact sign boundary for a natural pair of standard polytope families; return of positivity as q increases is a concrete nonmonotonic phenomenon that motivates finer coefficient inequalities and disproves naive monotonicity within this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
