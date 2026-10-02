# Independent audit — 2026-10-01

## Final claim

For \(\nu\ge-1/2\) and \(r\ge0\), \(\Phi_\nu(2r)\ge \Gamma(r+1/2)/(\sqrt\pi\,2^\nu\Gamma(r+\nu+1))\), with equality exactly at \(r=0\) or \(\nu=-1/2\), via the stated single-crossing weighted-integral proof.

## Correctness — PASS

The Baricz--Pogány integral representation reduces the claimed bound to positivity of a weighted paired kernel. The normalized kernel has one interior sign change. The boundary-weight integral is exactly \(F(r)=\psi(r+1/2)-\log r+\operatorname{Ei}(-4r)\); its derivative is a Laplace transform of a one-sign-change kernel, so \(F\) increases and then decreases to zero and remains positive. Multiplying by a decreasing beta weight preserves positivity for all \(\nu>-1/2\), while \(r=0\) and \(\nu=-1/2\) give the stated equality cases. The current right side is algebraically identical, by Legendre duplication, to the right side in the earlier published theorem.

Checked sources:
- Earlier published finding dated 2026-09-20, A Kanter-type lower bound for the generalized Bessel sum at every real order, complete RESULT inspected.
- Baricz and Pogány, On a sum of modified Bessel functions, Mediterranean J. Math. 11 (2014), arXiv:1301.5429.
- Mattner and Roos, A shorter proof of Kanter’s Bessel function concentration bound, PTRF 139 (2007).
- Veestraeten, On Finite and Infinite Sums of the Modified Bessel Function of the First Kind, Mediterranean J. Math. 23 (2026).
- Resultary semantic search for generalized Kanter inequalities for \(\Phi_\nu\).

Residual risks:
- None.

## Originality — FAIL

Originality fails decisively. An earlier published finding dated 2026-09-20 states the same theorem for the same \(\Phi_\nu\), domain, equality cases and asymptotics. Its right side \(2^{-2r-\nu}\Gamma(2r+1)/(\Gamma(r+1)\Gamma(r+\nu+1))\) is exactly \(\Gamma(r+1/2)/(\sqrt\pi\,2^\nu\Gamma(r+\nu+1))\) by Legendre duplication. The earlier proof also uses the same one-sign-change kernel and the same boundary functional \(\psi(r+1/2)-\log r+\operatorname{Ei}(-4r)\).

### Equivalent formulations

Searches:
- Resultary query: generalized Kanter inequality Phi_nu modified Bessel gamma ratio
- Full comparison with the 2026-09-20 published RESULT

Evidence:
- The 2026-09-20 result appears as the second-highest semantic hit, immediately before the assigned 2026-09-21 record.
- After applying Legendre duplication, the two displayed lower bounds are identical.

Reasoning: The gamma-ratio and doubled-gamma formulations are equivalent, not distinct results.

### Broader coverage

Searches:
- 2026-09-20 all-real-order Kanter finding
- Baricz--Pogány 2014

Evidence:
- The 2026-09-20 theorem covers every \(\nu\ge-1/2\), \(r\ge0\), exactly the assigned domain.
- The 2014 source is the common motivating open problem.

Reasoning: The earlier finding is not merely broader in context; it exactly dominates the assigned final claim.

### Exact database or table

Searches:
- Earlier theorem statement and equality cases

Evidence:
- Same pointwise inequality, same equality at \(r=0\) and \(\nu=-1/2\), same strict interior case, same asymptotic sharpness.

Reasoning: There is no surviving exact numerical datum or parameter slice outside the prior theorem.

### Claim versus prior implication

Searches:
- Proof-by-proof comparison of the 2026-09-20 and 2026-09-21 findings

Evidence:
- Both reduce Baricz--Pogány’s integral to a one-sign-change kernel and both prove positivity through the identical digamma/exponential-integral boundary functional.
- The alternate beta-variable notation does not add a mathematically independent claim.

Reasoning: The assigned theorem is an equivalent restatement/rederivation of the earlier published theorem and therefore is covered under the required implication standard.

### Source inspections

- **A Kanter-type lower bound for the generalized Bessel sum at every real order** — Decisive exact coverage. Material read: Complete RESULT.md, including theorem, integral reduction, one-sign-change lemma, boundary functional, equality cases and originality section Method: Published-result full-text inspection Evidence: The prior RHS becomes the assigned RHS by Legendre duplication, and the proof mechanism is the same.

Checked sources:
- Earlier published finding dated 2026-09-20, A Kanter-type lower bound for the generalized Bessel sum at every real order, complete RESULT inspected.
- Baricz and Pogány, On a sum of modified Bessel functions, Mediterranean J. Math. 11 (2014), arXiv:1301.5429.
- Mattner and Roos, A shorter proof of Kanter’s Bessel function concentration bound, PTRF 139 (2007).
- Veestraeten, On Finite and Infinite Sums of the Modified Bessel Function of the First Kind, Mediterranean J. Math. 23 (2026).
- Resultary semantic search for generalized Kanter inequalities for \(\Phi_\nu\).

Residual risks:
- No correctness defect was found; rejection is due to exact prior coverage.

## Scientific value — FAIL

The generalized Kanter theorem is mathematically worthwhile, but this assigned record does not fill a remaining gap because the same result and proof mechanism were already published one day earlier. Re-expression of the identical bound in an equivalent gamma-ratio form is not an independent valuable contribution under the audit standard.

Checked sources:
- Earlier published finding dated 2026-09-20, A Kanter-type lower bound for the generalized Bessel sum at every real order, complete RESULT inspected.
- Baricz and Pogány, On a sum of modified Bessel functions, Mediterranean J. Math. 11 (2014), arXiv:1301.5429.
- Mattner and Roos, A shorter proof of Kanter’s Bessel function concentration bound, PTRF 139 (2007).
- Veestraeten, On Finite and Infinite Sums of the Modified Bessel Function of the First Kind, Mediterranean J. Math. 23 (2026).
- Resultary semantic search for generalized Kanter inequalities for \(\Phi_\nu\).

Residual risks:
- No correctness defect was found; rejection is due to exact prior coverage.

## Conclusion

The finding is scientifically rejected because the unchanged final claim is covered by an earlier published equivalent theorem; correctness evidence is preserved, but originality and independent scientific value fail.
