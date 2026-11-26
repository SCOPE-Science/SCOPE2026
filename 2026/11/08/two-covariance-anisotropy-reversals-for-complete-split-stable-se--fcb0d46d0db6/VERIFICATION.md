---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The cube-plus-clique-simplex hull gives a Beta(p,q+1) law for the sum of the clique coordinates, with independent conditional uniform cube and simplex factors. The volume contrast eigenvalues are (q+1)(q+2)/(12D(D+1)) and 1/(D(D+1)). The block-constant covariance is a diagonal term on the independent block plus the rank-one covariance of its two conditional means. Its off-diagonal is nonzero, its upper-left entry is above both contrast eigenvalues, and its lower-right is below both. For the vertex law, a uniform binary cube vertex is selected with probability 2^q/(p+2^q), and otherwise a uniform clique vertex is selected. The contrast eigenvalues are 2^{q-2}/N and 1/N; the two block means again give a nonzero cross-covariance and the two diagonal bounds place both spectral extremes in the block-constant matrix. The determinants and trace ratios then give the stated U and T formulas. The monotone trace-ratio map on kappa>1 makes F_q the exact comparison polynomial. An independent symbolic expansion checked the leading coefficient, the q=2,3,4 factorizations, and the evaluations at 0, 2 and 2^q/q. For q>=4 the signs there are positive, positive and negative; positive cubic leading coefficient supplies the negative root and a root above 2^q/q, with the smaller positive root between 2 and 2^q/q. To check that the middle interval is nonempty even on the integer lattice, put q=4+m, t=q^2+k, p=t/q+z/(1+z); expanding -q^3(1+z)^3 F with 2^q replaced by t gives 112 nonzero coefficients, all positive, including constant 46080. This covers p in [t/q,t/q+1), including ceil(t/q). In the joint scale p~c*2^q/q both trace ratios diverge and their ratio tends to 3(1+c)^2/(16c); sampling at fixed c just to either side of 1/3 and 3 brackets the two known roots and gives their limits. Direct substitution likewise gives both fixed-parameter regimes.

## originality

PASS

The audited contribution is the two-law comparison, including the sharp two-reversal phase and limiting constants, not the first computation of uniform-volume moments for this family. Distinct same-family Resultary results were inspected and materially overlap with the volume side. Neither supplies the distinct-vertex comparison or mechanically gives the cubic root classification and joint-scale thresholds. The same-day records are compared on content, not presumed chronology.

## value

PASS

For a canonical full-dimensional graph polytope, choosing uniform vertices versus uniform volume changes which law is more anisotropic twice, even with Euclidean normalization fixed. The exact cubic determines borderline comparisons and the distinct exponential scales explain why fixed-parameter comparisons miss the intermediate regime. This is a usable all-family characterization rather than a routine moment calculation or a collection of small numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
