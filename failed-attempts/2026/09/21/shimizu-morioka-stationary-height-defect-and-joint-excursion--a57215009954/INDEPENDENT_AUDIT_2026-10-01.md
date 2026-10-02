# Independent mathematical audit — SCOPE-20260921-a57215009954

Final disposition: **FAILED**.

## Correctness
**PASS** — The conditional law follows from stationarity of every smooth function of \(z\): \(\mathbb E[x^2\mid z]=bz\). Differentiating the displayed polynomial coboundary gives \(W'=y^2-bz(z-1)\); completing the square yields the stated height defect. The zero-defect case forces \(y=0\), \(x^2=bz\), and then invariance forces the three equilibria. For a non-equilibrium stationary measure, the prior balance gives positive mass on \(z>1\); restricting the conditional law to that set forces positive mass where simultaneously \(z>1\) and \(x^2>b\). Thus the assigned statements are mathematically correct.

## Originality
**FAIL** — The September 20 published Shimizu-Morioka/Rucklidge record already proves, for the more general parameter \(\rho>0\), the same conditional law \(\mathbb E[x^2\mid z]=bz\), the stationary balance \(\mathbb E[y^2]=b\mathbb E[z(z-\rho)]\), equilibrium-only equality, and positive mass on \(z>\rho\). At \(\rho=1\), the assigned square-defect identity is merely completion of the square in that prior balance, and the purportedly stronger joint excursion follows in one line by applying the already-published conditional law on the already-published set \(z>1\). The current record is therefore mechanically covered by the prior published theorem.

### Equivalent formulations
The apparent new formulation is an equivalent specialization plus elementary algebra.

### Broader coverage
The earlier result dominates the load-bearing structure of the assigned claim.

### Exact database or table
This positive prior hit is decisive.

### Claim versus prior implication
The headline joint excursion is a direct corollary of already-published statements.

## Value
**FAIL** — Once the September 20 conditional law and height-excursion theorem are available, the new-looking square identity is an algebraic rewrite and the joint excursion is a direct conditional-expectation consequence. Those operations are useful exposition but do not constitute a separate motivated mathematical contribution.

## Source inspections
- **Exact stationary balances and a recurrence-height barrier for the Shimizu-Morioka/Rucklidge family** (https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-shimizu-morioka-rucklidge-recurrence-barriers--03af2ccdb58c): complete published RESULT.md, including the conditional law, first and second balances, equality classification, recurrence barriers, and proof Method: published-record full-text inspection. Assessment: DECISIVE_PRIOR_COVERAGE. Evidence: The earlier record supplies exactly the ingredients from which every substantive assigned statement follows at \(\rho=1\).

## Residual risks
- No correctness defect is asserted; failure is due to direct prior implication and lack of surviving independent value.
