# Scientific assessment

## Correctness — PASS

The exact tree-size recursion gives the discrete normalized flow and doubling transition. The cumulative first-jump hazard in the continuous process is exactly \(\log(1+1/(ky))\), matching the discrete doubling probability without approximation. A coupled one-step estimate, including possible subsequent continuous jumps, yields a finite-horizon \(L^1\) error of order \(1/m\) for fixed logarithmic duration. The continuous process is nonexplosive; a one-jump density provides accessible small sets and aperiodicity, while the explicit Lyapunov drift supplies geometric Harris ergodicity. Sending first the discrete size and then the logarithmic horizon to infinity proves the weak limit. The original established moment asymptotics and uniform integrability identify every moment of the resulting invariant law. Critical formulas were independently checked by 2,952 finite assertions in `verify.py`.

## Originality — PASS (historical-priority proviso)

Remark 1.2 of Björnberg–Mailler, arXiv:2501.18466, explicitly says weak convergence of the same scaled size has not been established by their moment method. Their Theorem/Proposition 1.1 gives moments and tightness, not a selected limit law. The generic Davis PDMP framework and Meyn–Tweedie Harris theorems do not themselves compute this discrete model's exact hazard coupling or state its weak limit. Targeted published-literature searches and mathematical-record comparisons did not identify the same implication or a broader result explicitly covering it. Unindexed subsequent work or a general theorem with an unrecognized direct specialization remains a residual priority risk.

## Mathematical value — PASS

The existence of the limiting law for \(B_n/n\) is a specific, natural gap stated in the model's primary paper. The result resolves weak convergence despite a lognormal-scale moment sequence for which a simple moment-determinacy argument is unavailable. The invariant-jump-process characterization and explicit one-step coupling give a usable probabilistic description that also explains the previously computed moment recursion. No assertion of a closed-form density, almost-sure convergence or a height theorem is made.

## Literature comparison and scope

Primary: Björnberg and Mailler, *A random recursive tree model with doubling events*, arXiv:2501.18466, initial posting 2025-01-30, especially Proposition 1.1, Remark 1.2, and §2.1. Methodological references: Davis (1984) on PDMPs, and Meyn–Tweedie (1993) on Foster–Lyapunov/Harris recurrence. Primary paper available in full HTML; generic methodological primary papers were compared through published abstracts and bibliographic descriptions. This qualification limits the completeness of the historical survey but does not alter the explicit published gap.

Self-review: passed. Independent audit: not yet performed.
