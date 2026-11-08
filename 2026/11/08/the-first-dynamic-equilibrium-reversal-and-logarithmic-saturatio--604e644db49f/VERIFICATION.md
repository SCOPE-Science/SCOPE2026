---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

The standalone `ladder_gap_checker.py` requires Python 3 with no nonstandard dependencies. It uses `fractions.Fraction` for root bisection, exact Taylor endpoint sums, quadrature sums, and all decisive inequalities. To run it, execute `python ladder_gap_checker.py`. The packaged copy was replayed successfully from disk and all ten strict comparisons passed.

## Finite certificate method

For each blockade \(b\in\{1,\ldots,10\}\), the root of the published static equation is bracketed with 51 dyadic bisections, and the reciprocal scaled density is bounded by monotonic pieces. The dynamic density is bracketed with a composite trapezoid quadrature of its published exponential integral, an explicit \(b^3/(2N^2)\) error, and alternating Taylor polynomials of degrees 39 and 40 at each rational node. No floating-point number appears in a decision comparison. The closest case, \(b=9\), passes strict separation of the two exact intervals.

## Infinite-parameter theorem

The \(W(2b)\) asymptotic and logarithmic deficit are justified by the exact equation \(-\log q=2b\operatorname{artanh}(q(1-q))\) and uniform bounds on \(q\). No finite computation purports to prove the infinite-parameter limit. Published prior work already supplied the exact density formulas and the limiting constant for the dynamic model.

## Scope of validation

The finite interval certificate was run and checked. Mathematical correctness and historical originality have received self-review only; independent audit, replication by another party, and broader historical validation have not been performed. This does not certify that the two densities stay in the same order beyond \(b=10\).
