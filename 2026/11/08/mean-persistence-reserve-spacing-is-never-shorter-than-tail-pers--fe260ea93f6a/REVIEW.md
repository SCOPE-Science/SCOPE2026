# Review of optimal separation under two persistence criteria

## Correctness — PASS

The state-space definition fixes all three transitions, and the absorbing generator gives exact expressions for both expected extinction time from two occupied reserves and the logarithmic survival-decay rate. The proof checks all parameter quantifiers, the strict regime \(0<a<b\), boundary optima, and positivity of required denominators. The critical inequality between marginal thresholds is proved by \(U(U-\Delta)+4e^2>0\), not inferred from sampling. `verify.py` replayed 2,518 assertions involving exact backward equations, symbolic identities and bounded parameter sweeps. Finite tests support the derivation; the paper proof, not the sweeps, establishes universality.

## Originality — PASS, with limits

Wagner–Ross–Possingham (arXiv:math/0309255, publicly available in 2003) establish the competing marine-reserve colonization/catastrophe processes and optimize a *discrete-time* quasi-stationary eigenvalue. Their full accessible preprint specifies transitions allowing a single reserve to be removed by a catastrophe, rather than an independent fatal systemwide shock. This finding neither claims the source model nor spectral optimization as new. Its distinctive statement is the exact continuous-time **ordering between the two optimizer locations** and the three sharp amplitude regimes.

McCarthy–Thompson–Possingham (2004 online), Grimm–Wissel (2004) and Blowes–Connolly (2012) are related to persistence criteria or spatial risk spreading, but accessible claims do not imply this two-state generator's strict ordering. Their full text was not all available; no whole-document absence is asserted and historical priority remains a risk. Public bibliographic comparisons and semantic mathematical searches, including broader equivalences, found no directly dominating assertion; a failed query is not a proof of novelty.

## Mathematical value — PASS

An initial-state mean lifetime and a late-horizon decay rate are non-equivalent objectives. Under a biologically interpretable ordering of spatial decay scales, the result determines which optimum is farther apart *for every parameter choice*, and gives exact, nonempty thresholds for boundary versus interior recommendations. The intermediate interval, in which only the mean criterion favors positive separation, is meaningful as an objective-selection effect. It is not a routine exercise about optimizing a single rational function because the universal strict order requires comparing independent resolvent and principal-eigenvalue sensitivities.

## Scope and verification limits

The model is an idealized continuous-time absorbing occupancy chain with exactly two symmetric patches; it assumes exponential kernels, individual local extinctions and systemwide common-catastrophe killing. No assertion covers models with only partially destructive catastrophes, other distance-decay exponent orders, external recruitment, arbitrary finite horizons, or empirical reserve decisions. The scientific review is internal and does not establish independent validation or historical priority.

Self-review: passed. Independent audit: not yet performed.
