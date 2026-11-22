# Scientific review: A Fibonacci consensus basin and exact relaxation shells in pinned majority dynamics

The claim is the **complete all-size finite-time fixation distribution** and the **entire Fibonacci-sized all-zero basin** under one pinned-zero site, as stated consistently in the result and metadata. The known qualitative fixed-only result, number of fixed configurations, and sharp maximum fixation time are treated as contextual, not new.

## Correctness: PASS

Each pinned configuration corresponds bijectively to one even-parity \(n\)-bit wall word. The pinned site creates two virtual zero boundaries in the wall update, so maximal one-runs erode inward independently by one from each end. The length restriction \(2t+1\) exactly characterizes fixation by time \(t\); a linear finite-run language gives the two rational series and an even-parity projection. All-zero attraction requires only even-length initial one-runs, whose ordinary generating function is \(1/(1-z-z^2)\). The n-even/n-odd terminal shell counts are proved by the only admissible maximally long wall runs. Two independent scripts exhaustively agree with full-state dynamics through \(n=15\), with the integer series additionally checked through \(n=16\); experiments are not substituted for unrestricted proof.

## Originality: PASS (qualified)

The most important same-object source is Inokuchi and Sato (2000), Lemma 3.88 and Theorem 3.90, which cover the zero-zero fixed-boundary Rule 232, its fixed-point count recurrence and sharp transient bound. Those assertions are **not** new. The source does not give all the separate first-fixation layers nor the complete basin of the unanimous pinned opinion. Tosic and Agha (2004) and Nakar and Ron (2022) consider broader qualitative/cyclic majority structure; the previously published cyclic Rule 232 exact histogram uses a different boundary map, with a two-to-one reconstruction and exceptional alternating two-cycle, and does not directly cover the present pinned problem. Actual multiple published-finding corpus and scientific-source searches also checked boundary aliases, run-language reformulations, Fibonacci-basin matches and potential broad coverage. The unresolved risk is an older unindexed or differently formulated exact pinned-time or basin enumeration; no absolute priority is asserted.

## Value: PASS

The exact fraction of starts resulting in complete agreement with a single immutable site is a natural basin-reliability statistic; remarkably it decays as \((\varphi/2)^n\), despite complete eventual stabilization and the fixed site's perpetual participation. The rational cumulative-series formula resolves every finite-time stabilization layer uniformly across all sizes. This is a meaningful refinement of the already-known maximal-time and fixed-state counts, rather than an arbitrary numerical slice or a new name for a classical recurrence.

## Scientific limitations

Only radius-one synchronous majority, a single pinned-zero site, and uniform nonpinned starting bits for the probability limit. No stochastic/asynchronous dynamics, multiple pins, or historical independence certification. Finite checks confirm rather than prove the unrestricted derivation.

Self-review: passed. Independent audit: not yet performed.
