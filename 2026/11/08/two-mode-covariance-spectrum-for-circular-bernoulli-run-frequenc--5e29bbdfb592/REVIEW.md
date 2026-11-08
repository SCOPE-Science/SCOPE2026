# Review of the circular run-frequency covariance theorem

## Correctness — PASS

Condition on an exact length-\(r\) run and partition all possible starts of a length-\(s\) run into one coincident, two touching, \(n-r-s-3\) independent, and incompatible starts. This proves every covariance entry for \(n\ge 2R+3\). Its two-mode decomposition, eigenvalue product \(-\Delta_R\), and geometric-series limits follow by direct algebra. Positive definiteness follows from the attainable all-zero and one-run count vectors. Rational exhaustive checks verify representative boundary cases without substituting for proof.

## Originality — PASS, qualified

The strongest direct primary predecessor is Inoue–Aki (2005), Section 4: Theorem 4.1 gives a joint generating function and Theorem 4.4 a general mixed-moment recurrence for circular success-run counts. Such recurrences imply that the covariance entries can be *computed*, so raw moments are not asserted to be absent from prior work. The inspected sections do not state a rank-two normalization, exactly two exceptional eigenvalues, or an off-diagonal length-sum phase diagram. Huffer–Sethuraman–Sethuraman (2008) treats different infinite Bernoulli-string models. The publicly indexed fixed-composition run-transition and run-count results have different sampling laws or one total-run statistic, not the full iid count-spectrum theorem. Unexamined implicit algebraic equivalences within historical generating functions remain a residual priority risk.

## Value — PASS

The result identifies only two collective second-moment interaction modes across arbitrarily many short run lengths, despite strong local pattern overlap. Its all-pairs covariance sign cutoff and explicit limiting exceptional eigenvalues provide useful finite-sample constraints and a compact covariance representation for run-frequency statistical analyses. These are structural features beyond any one computed moment or arbitrary parameter slice.

## Scope and independence

The theorem concerns iid *circular* Bernoulli samples and the subvector of lengths \(1,\ldots,R\) with \(n\ge2R+3\). It does not assert the same low-rank spectrum for more heavily wrapping run windows, non-iid trials, or fixed-composition sampling. No independent review has occurred.

Self-review: passed. Independent audit: not yet performed.
