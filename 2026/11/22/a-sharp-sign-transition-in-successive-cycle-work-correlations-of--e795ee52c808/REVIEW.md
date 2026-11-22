# Self-review

## Correctness — PASS

The cycle decomposition follows directly from the stationary linear Langevin equation and gain-one feedback. Direct integration of the active-force exponential kernel yields the exact adjacent covariance and its geometric decay over longer cycle separations. The only negative cross-cycle Isserlis term arises because the current measurement error appears with coefficient \(-e^{-a\tau}\) in the next cycle's pre-feedback position. The two product forms of \(G_{a,b}\), including the equal-rate limit, rigorously establish strict monotonicity and the amplitude boundary. The included `verify.py` was executed successfully with direct quadrature, Monte Carlo cross-checks and parameter tests; numerical tests are corroboration, not the infinite-parameter proof. The stationary setting and Gaussian hypotheses are essential.

## Originality — PASS, with residual risk

The full accessible text of Bahng–Lee–Ghim arXiv:2508.16866 was inspected through its active-bath model, extracted-work equation, variance/covariance dynamics, feedback-gain analysis, conclusions and appendices. It treats mean extracted work and power, not the lag-dependent covariance between *two* distinct cycle works. Paneru et al., Nature Communications 11, 1012, was inspected through its methods and work-fluctuation sections: it gives variance of one-cycle extracted work in a thermal information engine, not the derived active-bath adjacent-lag sign threshold or positive geometric higher lags. The related Paneru et al. PRE 102, 032126 abstract discusses fluctuation–dissipation/uncertainty bounds but lacks the same colored active bath; its full-text implication was not exhaustively checked. Relevant published-index results on work variance under harmonic partial resetting and four-time colored-noise fingerprints have different generators and observables, hence do not logically dominate this theorem. The work is a specific full-shift specialization, but it requires a previously unreported two-cycle comparison; unindexed equivalent formulas remain an originality risk.

## Value — PASS

Work noise, rather than mean work alone, matters for reliable cyclic engines. A naturally motivated measured observable—the lag of extracted work—has two competing mechanisms with opposite signs, and the strict two-regime switch gives an exact bath-memory-versus-measurement-precision design boundary. The positive lags beyond one cycle distinguish persistent bath correlations from one-step feedback error without claiming thermodynamic performance guarantees. This is a qualitative model classification rather than a routine numerical specialization or a mere restatement of one-cycle variance.

## Scope and residual risk

The theorem is restricted to a Gaussian active Ornstein–Uhlenbeck drive, iid Gaussian observation errors, stationary operation, instantaneous full-shift feedback and strictly positive amplitude and measurement variance. Unindexed earlier Gaussian feedback-correlation calculations could contain an implicit equivalent result, and a relevant thermodynamic-uncertainty publication was inspected only at the abstract level; neither comparison was represented as comprehensive negative coverage. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
