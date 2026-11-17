# Self-review

## Correctness — PASS

The monotonicity and translation-equivariance of the order statistic place each output difference between the minimum and maximum input differences on its window. For neighboring centers, the union of windows has exactly \(2r+2\) entries, so its oscillation is bounded by the sum of \(2r+1\) adjacent input differences; summing over centers gives the global upper bound. For the lower bound, the explicit rank interlacing \(L_1,\ldots,L_r,R_1,L_{r+1},\ldots,R_r,L_{2r},R_{r+1},\ldots,R_{2r}\) forces alternate-side median selections at each of the \(2r\) windows across a binary jump. Placing this and its reflection around two separated interfaces on a cycle gives \(2(2r+1)\) output jumps per two input jumps. All parameter ranges are quantified. The rational checker verified 96 sharp witness cases and 2,400 sampled bound instances; the proof, not the experiments, establishes every case.

## Originality — PASS, qualified

Restrepo–Chacón (1994) and Little–Jones (2011) prove *single-signal* total-variation diminution; the present quantity compares *two separately filtered signals*, and no substitution of the difference is legitimate for this nonlinear operator. Arias-Castro–Donoho (2006) analyze denoising and edge risk rather than sharp two-signal BV conditioning. Actual thematic searches of published mathematical findings for running medians, total-variation perturbation bounds and sliding order statistics returned no equivalent implication. The 1994 IEEE source was examined through its available abstract and bibliographic record; its complete paper was not substantively read. Historical nonlinear-filter and stack-filter stability literature could contain an unindexed equivalent formula. This qualified finding does not assert exhaustive publication priority.

## Mathematical value — PASS

The sharp two-input total-variation stability modulus of a common nonlinear smoothing operation is a natural signal-condition invariant. Its exact growth equal to window size, rather than nonexpansivity suggested by ordinary one-signal smoothing, has an explicit all-radius attaining mechanism. The theorem covers infinitely many radii and cycle lengths and exposes a structural boundary between variation diminution and variation-distance stability; it is not a fixed small numerical example.

## Scope and limits

The sharp equality claim concerns \(n\ge8r\) on a real periodic cycle; the upper bound itself holds for \(n\ge2r+1\). Extending sharpness to shorter cycles or to weighted medians and nonperiodic boundary rules is not claimed. Independent literature-priority checking remains useful.

Self-review: passed. Independent audit: not yet performed.
