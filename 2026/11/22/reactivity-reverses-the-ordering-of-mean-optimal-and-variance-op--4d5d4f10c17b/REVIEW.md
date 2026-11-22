# Review: reactivity-dependent reversal of optimal search speeds

## Correctness — PASS
The analytic argument checks the original exact dimensionless moments of Jeon--Go--Kim [1] and separately proves uniqueness of the mean speed minimizer for every positive reactivity. Global weak-reactivity lower bounds give compactness after cube-root scaling, allowing uniform second-order perturbations; the stronger-capture limit localizes every minimizer to a logarithmic neighborhood, where strict convexity proves variance-minimizer uniqueness. The coefficients differ at second order under weak capture, and the logarithmic offsets differ under strong capture. The delivered `check.py` uses standard-library decimal arithmetic to run 122 assertions on derivatives, geometric-return moment reconstruction, numerical minimizers, asymptotic coefficients and hyperbolic bounds. Finite checks are not the infinite proof.

## Originality — PASS (publication priority qualified)
The full accessible original paper [1], including exact moment equations and mean-speed optimal asymptotics, is closely related and receives explicit credit. The assessed contribution is an independently justified two-objective ordering reversal for the same stochastic model. A stochastic-gate paper [2] and publicly indexed sticky-boundary active-escape result [3] concern different target mechanics or optimization variables, and do not directly imply this two-regime ordering. The full text of [3] was not accessible; a broader unpublished or unindexed optimization theorem remains possible.

## Mathematical value — PASS
The previously known exact search-time mean and variance support a practically motivated question: whether speed settings that optimize typical absorption also optimize reliability. The strict reversal, with asymptotic separation constants in two physical regimes, gives a nontrivial transport design boundary. This is not a new closed moment formula, a claim of general single-crossing uniqueness, or merely a numerical table.

## Scientific scope and limits
The claim holds for uniform initial positions and orientations, the one-dimensional two-state Poisson run-and-tumble particle, sticky walls, and a stationary partially absorbing central target. It compares unstandardized variance to mean. No intermediate-reactivity variance uniqueness, number of reversal crossings, or independent audit is asserted.

## Closest literature
[1] Jeon, Go and Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, arXiv:2310.04016v1 (2023-10-06), Eqs. (28), (113).
[2] Mercado-Vásquez and Boyer, *First hitting times between a run-and-tumble particle and a stochastically-gated target*, arXiv:2102.11787v1 (2021).
[3] *Sharp mean–variance Pareto frontier and relative-risk optimum in sticky active escape*, publicly indexed 2026-11-02; full text inaccessible during comparison.

Self-review: passed. Independent audit: not yet performed.
