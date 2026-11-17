# Review of the matched SIRD mortality-response theorem

## Correctness

**PASS.** The exact conserved mass balance gives \(d=t(1-x)/(1+t)\) and the active living population \(N_\infty=(1+t x)/(1+t)\). Integrating the two incidence equations yields the stated, distinct scalar final-size maps. Positivity and strict concavity give unique physical fixed points. The implicit-function expansions produce the first corrections \(sr\log(1/s)-(1-s)\) and \((1-s)(sr-1)\), and the active equality coefficient \(-(1-s)^2/(2s)\). Strict signs and derivatives for sufficiently large \(t\) follow from analytic remainders. The checker passes symbolic coefficient identities and multi-precision examples. No global monotonicity is asserted.

## Originality

**PASS within inspected evidence, subject to priority risk.** Melo and Santos identify active-population normalization and analyze mortality numerically. The separate published result *Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks* proves uniqueness for the full multigroup model and geometric error bounds; it does not provide or imply the matched active-versus-fixed mortality-response asymptotics. The first-order sign wedge is not an algebraic restatement of general uniqueness. Exact title/term/parameter and published-finding corpus semantic searches found no dominating result. The original manuscript was located through indexed sections and abstracts but could not be retrieved in complete form, so an unindexed treatment of the same sign reversal remains a residual risk. General SIRD comparative statics should be examined by a future independent reviewer.

## Mathematical value

**PASS.** The mortality rate both reduces infection lifetime and changes the active force-of-infection denominator. Comparing the two normalizations using identical initial data isolates that feedback, yielding a sharp region in which long-run mortality responds in opposite directions. The result identifies a qualitative modeling risk even when both models agree on the infinite-mortality limit. It is not a claim of global heterogeneity or an arbitrarily selected numerical cutoff: the region depends naturally on initial susceptibles and transmission/recovery ratio.

## Limits

The equality boundary was verified at second order, but the upper fixed-denominator equality boundary is not the subject of the theorem. The theorem concerns two identical initial communities and sufficiently large mortality. Full primary-paper text was not available in this review, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
