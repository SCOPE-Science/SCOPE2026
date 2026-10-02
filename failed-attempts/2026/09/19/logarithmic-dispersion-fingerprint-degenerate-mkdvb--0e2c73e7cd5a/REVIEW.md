# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

**Disposition:** FAILED

## Correctness — PASS

Starting from the cited center-manifold law \(v'=-(3s/\mu)v^2+((1+18\kappa s^2/\mu^2)/\mu)v^3+O(v^4)\), setting \(y=1/v\) gives \(y'=3s/\mu-((1+18\kappa s^2/\mu^2)/\mu)y^{-1}+O(y^{-2})\). Since \(y\asymp\xi\), one integration yields the stated logarithmic coefficient. Fresh symbolic reconstruction also gives \(s-U=\mu/(3s\xi)+(\mu^2/(27s^3)+2\kappa/(3s))(\log\xi)/\xi^2+O(\xi^{-2})\) and the pairwise comparison limit.

## Originality — FAIL

A published 2026-09-18 SCOPE result, one day earlier, states the identical downstream inverse-tail and direct-tail formulas and the same translation-invariant dispersion recovery, while also adding the sharp upstream exponent and critical Jordan tail. The audited claim is therefore directly covered by stronger prior SCOPE work.

The structured originality comparison, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.json`.

## Scientific value — FAIL

The asymptotic coefficient is mathematically meaningful, but under the required value test a narrow exact invariant must not already be known or mechanically implied. Here the exact tail and comparison information were already published in a stronger theorem, so this record does not supply a new worthwhile gap.

## Limitations

- The analytic asymptotic calculation is correct for the stated monotone regime.
- The originality failure is decisive because a 2026-09-18 published SCOPE record states the same downstream formula and strictly broader sharp-tail package.
- Jacobs--McKinney--Shearer (1995) remains uninspected in full, but that access risk is not outcome-determinative.
