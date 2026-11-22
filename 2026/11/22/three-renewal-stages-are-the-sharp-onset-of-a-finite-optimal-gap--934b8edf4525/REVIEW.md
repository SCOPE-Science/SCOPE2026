# Scientific assessment

## Correctness: PASS

The claim concerns stationary equal-rate Erlang renewal calls with exactly two equal windows and a nonempty detection requirement in each. The proof derives the joint no-event probability through a phase-cycle generator with a killed final transition in each recorded interval. It explicitly computes the one-, two- and three-stage laws, then differentiates the three-stage exponentially damped sinusoid. The first stationary maximum is strictly above the infinite-gap limit, later maxima have exponentially smaller positive excursions, and the endpoint is strictly worse. A direct finite-state, standard-library checker performed 533 assertions over representative positive inputs. This corroboration is not used as the proof of universal quantifiers. Residual risk: the stated model is highly idealized; results should not be extended to unequal windows or nonstationary processes without new analysis.

## Originality: PASS (provisional priority)

The closest mathematical source, Nolan (2017), gives general Erlang renewal phase-matrix *joint distributions* and nonadjacent coincidence functions, and consequently supplies a general starting point for computing two-window probabilities. It does not state an optimized nonempty-window confirmation probability, a sharp one/two/three-stage distinction, the explicit globally optimal positive three-stage silent gap, or its strict monotonicity. These are not merely different notation for an existing optimized claim. The closest acoustic sources (Stevenson et al. 2014, Balantic and Donovan 2019, Van Helsdingen et al. 2024) emphasize calling dependence, surveillance scheduling, or underdispersed cues, but do not treat this exact Erlang gap-design objective. Existing probability machinery is credited, and the broader renewal-optimization literature remains a priority risk rather than being claimed exhaustively excluded.

## Value: PASS

Repeated acoustic confirmation matters for survey reliability, and published acoustic scheduling work explicitly contemplates two distinct positive recording occasions. The result shows a qualitative change in the optimal design caused *solely by renewal-stage structure*, at fixed positive recording duration: memoryless calls make gap irrelevant, Erlang-two calls favor ever-increasing separation, and Erlang-three calls require a finite specific gap. It supplies exact non-asymptotic timing at every positive recording length and a universal bounded optimal-gap interval; for the dimensionless example of unit recording length, two-confirmation probability improves from 0.0571145654 to 0.1063476560 versus contiguous windows. This is a natural model-specific design benchmark, not a generic claim that regular calling always improves detection.

## Closest literature and limitations

The reference probability matrices overlap with Nolan (2017), whose derivation is not rediscovered. The analysis differs from the continuous-time stationary two-state availability and Poisson or independent-hourly-detection models appearing elsewhere. The conclusion depends on stationary phases, equal window lengths, a single caller with perfectly detected instantaneous calls and no endpoint deadline. More general renewal and surveying theories may contain an equivalent optimizer statement. Full primary web texts and precise compared claims, methods, and residual risks are recorded in AUDIT.json and RESULT.md.

Self-review: passed. Independent audit: not yet performed.
