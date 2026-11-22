# Self-review

## Correctness — PASS

**Claim scope:** For each odd integer \(n\ge3\) and \(a,b>0\), the exact global minimax mean-square error among *deterministic, nonadaptive linear estimators* of a derivative, under the anchored cubic Taylor remainder and independent evaluation noise of variance at most \(b\), is \((3a^2b^2/16)^{1/3}(n/(n^2-1))^{2/3}\). All achieving schemes are symmetric two-site central differences with call counts differing by one and the unique radius described in RESULT.md.

**Reason:** Arbitrarily scalable degree-zero, degree-one, and degree-two polynomials force the three exactness equations. Averaging same-site weights is weakly risk improving, so a signed remainder interpolation makes the worst-case bias exactly attain the sum of absolute cubic contributions. Holder bounds this contribution below by the inverse square of the total coefficient \(\ell_1\) norm. The zero-sum exactness equation allows the positive and negative coefficients to be bounded separately by Cauchy--Schwarz; integer counts are maximized by the nearest-balanced allocation. Scalar minimization produces the global lower bound. The centered construction attains it, and the equality conditions rule out every other nonpermuted design. Numerical verification from embedded `verify.py` passed symbolic identities, exact moment constraints, integer sign partition identities, and 11,999 supplementary feasible-stencil comparisons.

**Limit:** Finite comparisons do not prove the continuous global claim; the proof is the universal inequalities and equality analysis. No assertion is made for nonlinear, adaptive, or correlated-noise schemes.

## Originality — PASS, qualified

**Closest literature:** H. Lam, H. Li, X. Zhang, arXiv:2007.04443 (8 July 2020), Section 2.1, Theorem 1 and complete displayed proof. It proves the universal lower bound and exact even-budget achievement, while expressly assuming an even budget for equality. The present odd sharp factor and equality classification require the additional integer zero-sum sign-partition inequality; they are not implied by the displayed theorem's odd lower bound alone. The new contribution is the full finite odd-budget determination, not the known even case. The primary source's exact assumptions, equations, and proof were inspected as HTML full text.

**Additional comparisons:** The broader noisy-gradient discussion of Berahas, Cao, Choromanski and Scheinberg, arXiv:1905.01332, was inspected at the level of abstract and bibliographic record only; it is contextual and was not treated as a full-text exclusion. Semantic mathematical-record and literature queries did not return an equivalent odd-budget theorem. A previously unindexed treatment, including a direct inference in the exact-design literature, remains a genuine priority risk. Lack of search hits is not the proof of originality.

## Value — PASS

The original minimax theorem supplies an exact even-budget design but only an unsharp bound for every odd finite budget, leaving the concrete issue of whether a leftover function evaluation can improve a fully optimal linear estimator. The exact all-odd classification answers that natural budget-allocation problem over **every possible deterministic linear stencil**, not merely the two-site family. At three calls, the optimal \(1:2\) split reduces the minimax risk by \(17.45\%\) against discarding the third call, and all optimal designs must use every call. The odd-versus-continuous-allocation penalty is sharp and explicit. The refinement is technically short and the relative gain vanishes quadratically as the budget grows; its value is a complete finite-resource theorem, not a claimed large asymptotic advance.

## Residual risks

The result shares the function class and much of the inequality chain with Lam--Li--Zhang, so its publication-level novelty may be judged modest, and nonindexed equivalent odd-budget results are possible. Full text of a broader contextual gradient-approximation publication was not obtained; the accessible abstract alone cannot establish noncoverage. A separate independent mathematical audit and publication-priority review are not performed.

Self-review: passed. Independent audit: not yet performed.
