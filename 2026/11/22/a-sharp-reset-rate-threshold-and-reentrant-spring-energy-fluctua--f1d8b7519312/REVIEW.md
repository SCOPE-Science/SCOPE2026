# Scientific review

## Correctness — PASS

The claim uses the specified two-dimensional thermal SDE and probe-only Poisson reset generator. Degree-two and degree-four stationary moment recurrences are solved exactly, with the reset indicator imposed only when the probe exponent is nonzero. The positive-denominator rational formula, mean signed spring jump, both ordered bath limits, strict quartic threshold and the two-extrema interval follow by exact symbolic elimination and Bernstein-coefficient inequalities. `verify.py` reconstructs the recurrences, endpoint expressions, Descartes certificate and generator substitutions in rational arithmetic. Gaussian inter-reset Monte Carlo is a separate corroboration, not a proof. Risk: the model is idealized; no numerical-to-infinite extrapolation is used.

## Originality — PASS, with residual priority risk

The source model, general mixed-moment recurrence, and one-coordinate kurtosis in Santra and Das (2026) are acknowledged as known; they do not themselves state a signed spring-energy-jump relative-noise crossover or the two-extrema classification. Olsen and Gupta (2024) study a distinct physically implemented partial-reset protocol and mean work; its work observable does not imply the current claim. published-finding corpus searches for aliases, spring energy, mixed fourth moments, resetting work and two extrema found nearby studies of positional kurtosis, memory-induced tails, fourth-order temporal irreversibility and one-coordinate work but no mathematically dominating statement. The key risk is an unindexed treatment of the same observable, not uncertainty about the cited moment method.

## Mathematical value — PASS

The signed potential change is a physically well-defined local quantity at a reset, which can be negative even with a positive mean. Its normalized variance controls reproducibility of reset-event spring exchange. The exact threshold shows that increasing bath memory can change from improving to worsening relative uncertainty as the reset rate passes a natural algebraic boundary; the interval theorem establishes actual nonmonotonic behavior and two separated extrema, rather than a mere endpoint comparison. These are qualitative structural results, not simple restatements of existing positional moments. No physical implementation-cost identity is claimed.

## Closest literature and limitations

Santra and Das (2026), Sections II–III and Appendix A, provide the same dynamics and general mixed-moment hierarchy, but not the stated energy-fluctuation classification. Olsen and Gupta (2024) provide thermodynamic resetting context for a different protocol. Equivalent but unindexed derivations cannot be excluded by database search alone. The results apply to positive rates and stationary pre-reset events of a single linear bath; long-run cumulative-work fluctuations and complete reset thermodynamics remain unproved.

Self-review: passed. Independent audit: not yet performed.
