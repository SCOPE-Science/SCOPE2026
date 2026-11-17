---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Weyl operators orthogonally diagonalize the analysis Gram matrix, so rank equals the number of nonzero ambiguity coefficients, with singular values squared p|A_g|². Cyclotomic irreducibility of 1+X+...+X^{p-1} makes a p-term phase sum zero exactly for a permutation of the prime field. Centering a nonzero translation of cx^5+dx^3+ex yields Ay^4+By²+Dy with A=5ca, B=(5/2)ca³+3da, D=-b. For p≡1 mod4, the m=(p-1)/4 power sum forces A=0; p≡3 mod4≥11, m=(p+1)/4 forces B=0 and t=(p+5)/4 forces D=0, leaving a noninjective even quartic. At p=7, power sums force B=0 and (D/A)^2=2, and explicit value lists show both possibilities sufficient: d=5ca² and b=±ca give exactly four additional zero Weyl indices when d/c∈{3,5,6}. p≤5 is checked with x^p=x and nonpermuting quadratics. Independent exact finite-field enumeration over every (c,d,a,b) for primes 2,3,5,7,11,13 passed, including precisely 18 exceptional pairs at p=7. The all-prime claim depends on these power-sum proofs, not enumeration.

## originality

PASS

PASS best knowledge for parameter-wise Gabor rank and Weyl kernel law of quintic–cubic phase masks, including the p=7 coefficient resonance. General Gabor lifting/ambiguity criterion and Hermite permutation-polynomial methods are known; inspected prior examples concern cubic, quartic chirps or graph-supported windows. Lüke 1996 polynomial-phase correlation paper was inaccessible in full and might contain relevant zeros; retained as a concrete priority risk.

## value

PASS

PASS: the complete all-prime rank/kernel classification gives an exact natural observability invariant for polynomial-phase Gabor measurement design, and the isolated seven-prime arithmetic resonance precisely characterizes a loss of four additional matrix directions. It separates generic maximal unimodular-window rank from exceptional small-characteristic behavior, beyond a simple finite table or routine normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
