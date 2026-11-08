# Self-review

## Correctness — PASS

The source of the single-excursion Laplace law is explicit Brownian motion observed at an independent exponential time, with rate parameter \(\sqrt{r/D}\). The two Voronoi cell sums and quantizer-jump sums reconstruct the parity transition and mean spatial reward for **all** possible landing sites, not only neighbors. The two-state transition matrix is irreducible and aperiodic for strictly positive parameters. Holding-time and spatial rewards have finite moments, allowing a Markov-additive strong law and its physical-time normalization. Brownian hitting-time bounds control the last incomplete excursion. The exact sign follows from the strictly increasing function \(x\coth x\). The small- and large-rate limits use justified series and exponential estimates. The extracted checker is finite supportive evidence, not the proof.

## Originality — PASS, with residual priority risk

The primary 2024 Alston–Bertrand nearest-site model fixes a **single** spatially uniform Poisson rate. Its diffusivity optimization does not imply the current for two last-site-dependent reset rates; their same-rate specialization has zero current by reflection here. Ghosh et al. (2023) and Liu et al. (2024) use a fixed one-rate clock and a spatially asymmetric ratchet potential; Roberts et al. (2024) study a separate finite-time return phase. Here free diffusion between resets has zero potential force, and the last-projected-site type changes the next exponential clock. Existing general Markov reward laws imply the form of a stationary reward/time ratio once the model-specific conditional rewards are supplied, but do not determine the hyperbolic-sine values, the necessary-and-sufficient ratchet criterion, or the weak-reset coefficient. Searches of published records did not reveal a dominating exact statement. The residual risk is an unindexed or terminology-mismatched special treatment of this two-sublattice, site-memory mechanism.

## Mathematical value — PASS

A natural physical variant of local resetting is to let the next binding attempt depend on the type of last encountered binding site. The theorem isolates a joint symmetry-breaking mechanism: neither inequivalent site spacing nor unequal kinetic rates alone produces directed transport, but their combination always does, with no current reversals under common rate scaling. The strict sign law is global in all positive parameters, and the quadratic rare-reset onset together with strong-reset suppression forces a finite transport optimum. This is an interpretable exact transport classification, not merely an algebraic change of variables or an unmotivated finite parameter slice.

## Scope and risk

The label is the previous reset site, not the instantaneous nearest site. No claim of optimal-rate uniqueness, centered diffusivity, full current fluctuations, or independent publication-priority certification is made. The comparison with other ratchet mechanisms is limited to materially inspected accessible text and the identified records.

Self-review: passed. Independent audit: not yet performed.
