---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For right equilateral triangular prism with h>0 and base circumradius 1, width is D times maximum absolute dot product over six axes (d_j,±h)/D, D²=h²+3. The fifteen absolute axis inner-products split into three, six, six pairs with magnitudes |3-h²|/D², (h²+3/2)/D², |h²-3/2|/D². Their maximum yields first overlap threshold q²=max(3,h²+9/4), N=3,9,6 closest unoriented pairs as h crosses sqrt(3)/2; critical contact graph has no triangles, preventing triple cap intersections near q. For q<=t<=D the twelve disjoint spherical caps have exact total probability 6(1-t/D); local tangent-plane lens area =8 sqrt(2)/(3 sqrt(q) sqrt(D²-q²)) (q-t)^(3/2)+o(...), with 2N lenses and normalized area 1/(4pi), giving coefficient 4 sqrt(2) N/(3pi sqrt(q) sqrt(D²-q²)). Independent rational Gram enumeration and mpmath spherical-cap lens quadrature at h=0.5,sqrt(3)/2,1.5 confirm contact counts and asymptotic normalization ratios near 1 (0.99973,0.99991,0.99989). Numerical quadrature corroborates, analytic geometry proves general h.

## originality

PASS

The general random polytope-width coarea framework and prism width decomposition in Abas are known, and published cap-overlap results for regular simplices and type-D root polytopes have comparable methods. These do not give the present exact triangular-prism height-dependent Gram-contact competition, critical h=sqrt(3)/2 ninefold coincidence, or sharp cusp coefficient. A full 92-page primary Abas manuscript was not accessible after arXiv/OA attempts and Oxford returned disconnected VPN; without claiming complete noncoverage, best-of-knowledge O pass remains with explicit significant residual risk, not automatic FAIL. No stronger same-axis theorem observed.

## value

PASS

The right equilateral triangular prism is a natural fundamental three-dimensional polytope family, and its random width upper-tail topology changes sharply with a physical aspect ratio. The explicit first collision threshold, three-to-nine-to-six pair multiplicity, full terminal linear interval and nonzero 3/2-power cusp coefficient give a motivated all-height phase diagram that can serve as an exact distributional reference, not merely a routine numeric integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
