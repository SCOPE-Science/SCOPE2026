# Independent mathematical audit — Universal logarithmic dispersion fingerprint in degenerate mKdV-Burgers shocks

Audited on 2026-10-01 UTC.

**Disposition:** FAILED

## Correctness — PASS

Starting from the cited center-manifold law \(v'=-(3s/\mu)v^2+((1+18\kappa s^2/\mu^2)/\mu)v^3+O(v^4)\), setting \(y=1/v\) gives \(y'=3s/\mu-((1+18\kappa s^2/\mu^2)/\mu)y^{-1}+O(y^{-2})\). Since \(y\asymp\xi\), one integration yields the stated logarithmic coefficient. Fresh symbolic reconstruction also gives \(s-U=\mu/(3s\xi)+(\mu^2/(27s^3)+2\kappa/(3s))(\log\xi)/\xi^2+O(\xi^{-2})\) and the pairwise comparison limit.

## Originality — FAIL

A published 2026-09-18 SCOPE result, one day earlier, states the identical downstream inverse-tail and direct-tail formulas and the same translation-invariant dispersion recovery, while also adding the sharp upstream exponent and critical Jordan tail. The audited claim is therefore directly covered by stronger prior SCOPE work.

### Equivalent formulations

The formulas are not merely analogous: they are algebraically identical after notation matching.

Evidence: Resultary returned the 2026-09-18 finding 'Sharp dispersive tails of the degenerate mKdV–Burgers shock' in addition to this record. The earlier full RESULT contains the same inverse-tail coefficient and the same direct \( (\log\xi)/\xi^2 \) coefficient.

### Broader coverage

Prior coverage strictly dominates the audited claim.

Evidence: The earlier result includes the audited downstream logarithmic correction plus exact upstream rates, the monotonicity-boundary Jordan factor, and two translation-invariant dispersion diagnostics.

### Exact database or table

This is not a table lookup; the relevant publication database nevertheless contains an exact prior theorem.

Evidence: The exact earlier SCOPE record was found and its full scientific text inspected.

### Claim versus prior implication

The audited final theorem is a subset/corollary of the earlier result, so originality fails regardless of whether older literature also contains it.

Evidence: Earlier Eq. (7) equals the audited inverse-tail formula; earlier Eq. (8) equals the audited direct-tail formula; its recovery formula implies the audited pairwise comparison law.

### Source inspections

- **Sharp dispersive tails of the degenerate mKdV–Burgers shock** — COVERING, with strictly broader coverage.. Material read: Complete RESULT.md, including Statement, proof, downstream logarithmic correction, and originality scope. Evidence: The earlier theorem gives exactly \(1/(s-U)=(3s/\mu)\xi-(1/(3s)+6\kappa s/\mu^2)\log\xi+C+o(1)\) and the equivalent direct-tail coefficient.
- **Large-Time Behavior towards Composite Waves of Degenerate Shock and Rarefaction Wave for Modified KdV–Burgers Equation** — PRIOR for the local expansion; outcome does not depend on whole-document novelty because stronger SCOPE coverage is decisive.. Material read: Bibliographic/abstract access and the exact center-manifold formula reproduced in the audited source package; full primary text was not obtained. Evidence: The audited proof itself starts from the source's \(g(w)=3w^2+(1+18\nu)w^3+O(w^4)\).

### Checked sources

- Resultary 2026-09-18 sharp-dispersive-tails record
- arXiv:2609.20591
- Jacobs--McKinney--Shearer (1995) bibliographic record

### Residual risks

- Jacobs--McKinney--Shearer (1995) was not inspected in full; this cannot restore originality because the earlier SCOPE result already covers the claim.

## Scientific value — FAIL

The asymptotic coefficient is mathematically meaningful, but under the required value test a narrow exact invariant must not already be known or mechanically implied. Here the exact tail and comparison information were already published in a stronger theorem, so this record does not supply a new worthwhile gap.

## Limitations

- The analytic asymptotic calculation is correct for the stated monotone regime.
- The originality failure is decisive because a 2026-09-18 published SCOPE record states the same downstream formula and strictly broader sharp-tail package.
- Jacobs--McKinney--Shearer (1995) remains uninspected in full, but that access risk is not outcome-determinative.
