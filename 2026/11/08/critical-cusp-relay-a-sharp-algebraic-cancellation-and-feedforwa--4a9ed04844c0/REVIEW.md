# Scientific assessment

## Correctness — PASS

The logistic-to-hyperbolic-tangent substitution is exact. The terminal scalar equations are autonomous and monotone, with cubic damping, so the two terminal amplitudes have the same \(t^{-1/2}\) leading term. The signed quadrature is the exact time translation between solutions of one scalar ODE. The relay input is a weighted difference of those solutions; its balanced coefficient follows by integrating the scalar damping over the time-shift interval, not by fitting numerical data. The final stable first-order relay equation passes asymptotic coefficients unchanged. The uniformly local exponential-kernel estimate also proves the near-balanced crossover. The proof covers all stated initial conditions and weights; it does not claim crossover rates at a cancellation of the displayed scaling function.

## Originality — PASS with priority limitations

The closest same-system source, Boudourides (arXiv:2609.10580), was read through its introduction, spectral theorem, multistability theorem, two-block cusp theorem, discussion, and appendices. It proves steady-state and spectral statements but no transient relay exponent, exact time-shift coefficient, or cusp cancellation crossover. Kaye's scalar framework (doi:10.1098/rsif.2026.0267) provides the threshold mechanism but not this network. General positive-feedback convergence results and cubic critical-relaxation results in other models have different objects and do not imply the exact three-node weighted cancellation formula. Actual database queries for equivalent feedback normalizations, exponent pairs, opposite terminal forcing, and time-shift cancellations did not identify a dominating claim. The remaining risk is uncatalogued literature on asymptotic cancellation in coupled critical scalar flows; no exhaustive priority certification is asserted.

## Value — PASS

The minimal nontrivial feedforward graph has two independent recurrent terminal classes and a relay; a one-terminal graph cannot exhibit cancellation between opposing critical inputs. The claim distinguishes three genuinely different rates in one natural nonhyperbolic network and gives the crossover scale at which the exponent changes. It exposes information not contained in the standard homogeneous cusp or first-order spectral analysis: relay asymptotics depend on signed initial-condition time memory even though every activation converges to the same equilibrium. The quadrature makes that memory computable without numerically solving the full network.

## Limits

Logistic cusp, three-node reducible row-stochastic network, opposing nonzero terminal signs, deterministic flow. The precise exponent need not survive feedback into terminal classes. Numerical confirmation is finite; independent verification is not claimed.

Self-review: passed. Independent audit: not yet performed.
