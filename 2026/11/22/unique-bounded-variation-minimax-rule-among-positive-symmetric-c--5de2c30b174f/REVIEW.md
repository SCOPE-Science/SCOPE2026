# Scientific review

## Correctness — PASS
The proof covers the complete class of real pointwise Jordan-BV functions and all positive symmetric three-node rules of cubic exactness. Its critical facts are the step-function dual characterization of quadrature error, polynomial moment normalization \(2bd^2=1/12\), the global strict positivity inequality \(b>2(1/2-d)\), and the monotone two-branch minimax argument. The algebraic optimizer is uniquely selected on the entire admissible interval; two explicit jump functions attain the norm. The packaged checker tests exact polynomial identities, a rational root bracket and independent finite instances. Risks: point values at jumps must not be replaced by equivalence classes in \(L^1\); finite checks do not prove the global inequality.

## Originality — PASS, with historical-priority limits
Dragomir–Momoniat (2011/2013) give BV three-point bounds but fix the outer nodes to the integration endpoints. Klaričić Bakula et al. (2015) examine differentiable-function Euler/Grüss remainders with interior symmetric nodes. Komisarski–Wąsowicz (2022) give exactly the relevant cubic-exact symmetric parameter family, but their optimality criterion is for 3-convex functions and related inequalities; it does not assert the Jordan-BV minimax formula or cubic-root optimizer. Indexed mathematical-record searches for the exact moment condition, discrepancy, parameters, step extremizers and aliases returned closest works on different parameters or objectives. The statement is not implied by the inspected prior conclusions without a new discrepancy minimax analysis. The residual risk is an older unindexed equivalence in the quadrature/discrepancy literature, not eliminated by searches.

## Mathematical value — PASS
Degree-three exactness, positive weights, symmetry and three evaluations form a complete and classical quadrature design class. The theorem precisely quantifies the structural tradeoff between polynomial exactness and robustness to jumps, identifies a uniquely optimal implementable rule and two distinct sharp jump mechanisms, and shows classical three-point Gaussian and Simpson rules are suboptimal under Jordan variation. This is an exact natural invariant with an explicit proof and worst-case witnesses, not a selected parameter-table entry. The theorem is limited to its stated symmetric class and is not asserted for arbitrary node geometries.

## Closest literature and limitations
- S. S. Dragomir and E. Momoniat, RGMIA Research Report Collection 14, Article 33 (2011), https://rgmia.org/papers/v14/v14a33.pdf ; DOI https://doi.org/10.1016/j.mcm.2012.07.024. Full text covers endpoints and one interior evaluation.
- M. Klaričić Bakula et al. (2015), DOI https://doi.org/10.1186/s13660-015-0603-x. Full HTML text concerns corrected Euler/Grüss formulas, not BV optimization.
- A. Komisarski and S. Wąsowicz (2022), DOI https://doi.org/10.1007/s00010-022-00868-4. Full HTML text gives the same admissible family but analyzes 3-convex rather than BV errors.
- M. D. Stern (1967), DOI https://doi.org/10.1093/comjnl/9.4.396. Only abstract inspected, with derivative-based criteria; no full-text negative-coverage claim.

Self-review: passed. Independent audit: not yet performed.
