# Review of resonant crossings in two-stage refractory Brownian resetting

## Correctness: PASS

The three-state Markov generator yields a closed moment resolvent; direct symbolic partial fractions establish the exact cancellation residue and the repeated-root boundary. The strict sign-crossing classification follows from relative decay rates and an amplitude comparison at equal decay. For near-resonance logarithmic growth, the normalized positive-cosine lobes are strictly concave, two roots survive in each full lobe before the growing exponential envelope reaches them, and the transition contains only finitely many lobes. The included checker reconstructs the resolvent, compares 48 independent ODE integrations, and provides 10 finite zero-count checks. These finite checks are not used as an infinite proof.

## Originality: PASS, qualified

The general renewal setup and Laplace-domain moment method are known from Evans and Majumdar (arXiv:1809.01551); the all-distribution pathway treatment of García-Valladares et al. (arXiv:2310.19913) covers the same mechanism and studies a one-exponential refractory phase. Olsen and Löwen (arXiv:2406.10039) supply general time-dependent moment formulas and show nonmonotonicity for fixed-duration refractory waiting. Targeted full-text comparisons did not identify the two-stage Erlang exact strict-crossing boundaries or the near-cancellation logarithmic count in these works. They are potentially derivable from broader prior formulas, so unstated or unidentified equivalent results remain a concrete originality risk. The contribution is strictly the classification and its asymptotic count, not the general resolvent.

## Mathematical value: PASS

The isolated point of infinitely many oscillations despite a slower real spectral mode is an exact cancellation phenomenon, and the nearby number of observable transient crossings diverges logarithmically. These results give a precise phase diagram for relaxation of a natural observable in a simple two-stage inactivity model, distinguishing spectral complexification from observable spectral dominance. The particular boundary structure is motivated by the model's two-stage refractory mechanism, not a freely chosen numerical slice.

## Scientific limitations

The theorem assumes independent, equally rated exponential refractory stages, complete resets, and an initially active Brownian particle at the reset point. It concerns ensemble mean-square displacement only, not sample-path crossings; publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
