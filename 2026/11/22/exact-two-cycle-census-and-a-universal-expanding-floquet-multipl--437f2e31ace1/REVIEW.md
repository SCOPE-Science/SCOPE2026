# Scientific review

## Correctness — PASS

The real two-cycle equations are equivalent to a sum-and-product quadratic whose discriminant is \(\Delta\). Necessity and sufficiency, including the double-root boundary, are proved explicitly. The complete two-step Jacobian product has characteristic polynomial \((\lambda-1)(\lambda-(1+a)^2)-u^2\Delta\); evaluation at \(1\) forces a real multiplier greater than \(1\). Evaluation at \(-1\) gives the exact saddle/nonhyperbolic/repeller divisions. The global invertible linear conjugacy to the published two-parameter map preserves the spectra. A SymPy checker passed symbolic identities, the exact rational witness and 129 deterministic finite tests. These finite checks only corroborate, and do not substitute for, the proof.

## Originality — PASS within the inspected literature

Primary source [1], inspected at the original map (Section 2), Theorem 5 and its numerical discussion, does not present the global primitive-two-cycle census or its exact full-state Floquet polynomial. In fact the full-state stability statement differs: the present exact expanding multiplier excludes the purported attracting negative-gain branch. The closest earlier positive-cone recurrence [2] proves results under nonnegative coefficients and states; the signed quadratic term in [1] violates those hypotheses. The cubic positive-coefficient extension [3] also does not imply this all-real signed result. Semantic searches for exact recurrence, period-two rigidity, equivalent Floquet criteria and general quadratic delay equations returned different models, not a documented implication. Unindexed classical equivalent formulations remain a genuine priority risk, and this review does not assert a proof of worldwide novelty.

## Mathematical value — PASS

The natural stability question is directly raised by the bifurcation analysis of [1]. The result completely classifies every primitive period-two state for all real nonzero model parameters, identifies exact separating curves, and gives a fully checkable counterexample to full-state attraction in the claimed branch. This is an exhaustive structural phenomenon rather than a finite simulation or an arbitrary parameter slice. The quadratic-delay formulation reveals why the no-sink conclusion is robust to adding arbitrary constant and linear polynomial terms.

## Closest works and limits

[1] L. Liu and X. Zhong, *Mathematics* 12 (2024) 2423, https://doi.org/10.3390/math12152423, Sections 2–4, especially Theorem 5. [2] J. Bektešević, M. R. S. Kulenović and E. Pilav, *Applied Mathematics and Computation* 227 (2014), 50–65, https://doi.org/10.1016/j.amc.2013.10.048, nonnegative-coefficient and first-quadrant dynamics. [3] Same authors, *Advances in Difference Equations* 2015:176, https://doi.org/10.1186/s13662-015-0503-x, cubic positive-coefficient recurrence. No higher-period or global-basin classification is established, and unindexed equivalent literature remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
