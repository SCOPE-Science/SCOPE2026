# Scientific review

## Correctness — PASS

The statement fixes the stochastic model, sensors, posterior tie convention, all parameter intervals, and a single accuracy-plus-coverage objective. The posterior conditional on positive pooled OR and negative observed leaves is explicit; multiplying the exact Bayes decision gain by the probability of the known negative leaves gives the general \(G_{n,k}\) formula. For three sources, all ground-set submodularity inequalities reduce, by exchangeability, to the two root-present leaf curvature inequalities, the leaf curvature inequalities without root, and the three root–leaf marginal inequalities. Each is evaluated algebraically, including all equalities and intervals. The root-present two-leaf gap is exactly \(pq(1-5p)/3\). A direct rational enumerator verifies the formula and the full finite set of inequalities at multiple values, including the boundary \(p=1/5\) and weight equality. Numerical and finite checks do not establish the continuum theorem; the analytic argument does.

## Originality — PASS on inspected evidence, not certified priority

Jakkala and Akella, arXiv:2312.16750v1, Sections IV.B–E and VI.B–C, explicitly supply the OR-gate Bayesian network, per-building classification and an accuracy/coverage objective, but do not derive any exact prevalence or weight phase boundary. The paper's experiments switch to F1 and concentration thresholds, so the result is **not** a counterexample for their experimentally tested objective. Bhattacharya et al., *Selection of Sensors for Efficient Transmitter Localization* (2020), Appendix D, already show generic Gaussian multi-hypothesis accuracy non-submodularity; that fact is acknowledged, not claimed as a new theorem. Their Gaussian counterexample does not mathematically entail the minimum three-source OR instance, the \(p=1/5\) impossibility for any coverage weight, or the sharp phase boundary. Standard detection coverage is submodular; this result classifies why it cannot compensate for conditional-classification complementarity. Textual searches and mathematical-record searches found no matching exact claim, but absence from search is not proof of novelty. An author webpage lists a predecessor from 2022 without a verifiable exact first-public day. Other older discrete diagnostic-testing formulations may remain relevant; no independent priority adjudication was undertaken.

## Value — PASS

The result answers a directly motivated design question for the natural smallest pooled wastewater-junction model: precisely when an accuracy-plus-coverage objective has diminishing returns, and whether a weight on detection coverage can restore them. The exact irreparable low-prevalence regime and full prevalence–weight boundary have consequences for the applicability of general submodular-greedy guarantees, without pretending to predict an algorithm's actual performance. Two-source minimality, the exact gap, and the pooled detector's classification blind spot are structurally linked parts of the same result, not routine parameter slices.

## Boundaries and risks

Perfect assays, independent identical building priors, binary OR transport, equal per-building loss and unthresholded coverage are assumptions; real sewer sensing may violate all of them. Generic non-submodularity had already been known in other localization models, so the novelty resides in the exact OR-source classification and sharp cutoffs. Historical priority and applicability to the 2022 predecessor remain open.

Self-review: passed. Independent audit: not yet performed.
