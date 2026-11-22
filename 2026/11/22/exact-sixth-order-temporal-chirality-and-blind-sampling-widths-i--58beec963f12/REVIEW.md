# Scientific review

## Correctness

**PASS.** The proof specifies a stationary positive-rate three-state Markov cycle and an independent Brownian displacement process. The temporal contrast is reduced exactly to the cyclic generator's three-time diffusivity moment. Explicit spectral projectors yield the antisymmetric Vandermonde coefficient; conditional independence of nonoverlapping Gaussian increments and elementary finite-interval integration then give the stated formula. The factor controlling all positive blind widths is isolated without numerical root-finding. An independently implemented symbolic/matrix/quadrature script passed 66 checks. Finite checks supplement, not replace, the analytic proof. Degeneracies in rates, diffusivity contrasts and gaps are included and restricted accurately.

## Originality

**PASS, with publication-priority risk.** Grebenkov (2019, arXiv:1903.04783) gives a general switching-diffusion propagator and analyzes mainly two-state time-averaged MSD; Slezak, Burnecki and Metzler (2019, arXiv:1904.08737) give broader heterogeneous-diffusion mixtures; Lucente et al. (2023, arXiv:2306.14558) examine high-order time arrows. A separately published stroboscopic-reversibility result for biased finite Markov rings directly anticipates the hidden chain's exceptional sampled widths. None of the material inspected states the present integrated three-window sixth-order identity, its exact Vandermonde directionality, or the if-and-only-if blind-width classification. Nevertheless these are consequences of known propagators plus a nontrivial spectral calculation, and a broader equivalent publication remains possible. The related Markov-ring publication was available as a scientific index summary rather than full text, so an implicit stronger implication has not been ruled out independently.

## Mathematical value

**PASS.** Heterogeneous transport can show perfectly Brownian MSD yet contain irreversible hidden mobility dynamics. The theorem identifies a concrete experimentally accessible order of measurement that detects the cycle direction relative to calibrated state diffusivities, proves that pairwise squared-increment covariances cannot do so, and gives a sharp infinite lattice of sampling widths where the diagnostic fails. The failure times depend only on the *rate imbalance*, not on the three mobility values; this is a structurally motivated temporal-aliasing boundary, not an arbitrary parameter slice. The result is limited to the stated statistic and model, with no claim about practical sample complexity.

## Closest literature and limits

The general generator/multi-time formalism of Grebenkov (2019) is the strongest primary antecedent; the existing published biased-ring sampling-alias theorem is the strongest exact temporal-boundary antecedent. The proof does not establish any universal minimality of sixth order among all imaginable nonlinear measurements, nor full time reversibility of integrated observations at blind widths. The few relevant inaccessible/full-text-unchecked sources are carried as residual originality risks. Source dates are the verified original public submission dates, not subsequent journal dates.

Self-review: passed. Independent audit: not yet performed.
