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

Fixing one coordinate at zero leaves the bipartite path constraints plus unit rows; signing columns by the bipartition identifies the edge rows with an oriented incidence transpose, so the face vertices are integral. A strictly positive vertex must solve all d independent tight equations. The adjacent-sum matrix has determinant 2 and its integer image is the even-coordinate-sum sublattice, so exactly the strictly positive all-tight point with odd capacity sum can give a fractional vertex. A feasible all-tight point with a zero coordinate belongs to an integral face, not to this exceptional case. In slack coordinates the exceptional cone has integer points precisely at nonnegative integer slacks with total parity q. The two parity characters yield the displayed rational cone series; subtraction of the symbolic even and odd terms leaves a germ regular at zero with value 2^-d. To make the Brion argument precise, restrict the rational exponential functions to a generic one-dimensional line through zero and take the Laurent constant term. At integral vertices the only dilation dependence is exp(q<v,z>), giving a polynomial constant term independent of parity. The same holds for the untwisted exceptional-cone term, so the regular germ determines the global difference. The vertex denominator divides two, so nonzero difference forces minimal period two. The alternating formulas satisfy the cyclic equations, have minimum (s-m+1)/2, and odd capacity sum precisely at s congruent to m mod 2. The frozen checker and verification notes were read, not executed. A fresh integer-count and exact rational interpolation spot check confirmed four capacity regimes in d=3 and the sequence 0,1/32,0,1/32 at alternating d=5, s=1,2,3,4; its script and output were saved under branches/f205b12c-26b5-4ae2-a417-8c1c36c6b69a/ehrhart_spotcheck.py and ehrhart_spotcheck.txt. These finite checks do not replace the analytic proof.

## originality

PASS

The supported distinct claim is the arbitrary-positive-integral-capacity classification on an odd cycle, including exactly when the periodic term vanishes and the alternating threshold. The constant anomaly in the unit example, the parity filter method, and the previously known odd-cycle quasiperiod upper bound are credited, not claimed as new.

## value

PASS

The result gives a complete and directly usable test for polynomial versus exact period-two counting on a natural weighted cyclic family, and the amplitude when period two survives. It distinguishes feasibility of a geometric corner from its arithmetic integrality, resolves the sharp alternating threshold, and requires no interpolation to predict collapse. This goes beyond recomputing a unit example or bounding the period by the denominator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
