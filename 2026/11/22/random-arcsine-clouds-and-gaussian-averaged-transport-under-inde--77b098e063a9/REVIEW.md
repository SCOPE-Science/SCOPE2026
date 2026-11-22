# Scientific review: Random arcsine clouds and Gaussian averaged transport under independent linear phase kicks

## Correctness — PASS

The domain is the infinite tight-binding lattice, a delta-site launch, independent Gaussian linear-slope kicks of strictly finite positive noise parameter, and fixed positive hopping strength and step duration. The exact Fourier propagator is a unit-modulus cosine with a random complex phasor amplitude. Jacobi–Anger and standard Bessel sums give the entire conditional site distribution and the exact conditional spatial variance. The exact finite-step phasor correlation sum yields the stated averaged variance. A bounded martingale difference decomposition, the ergodicity of a wrapped Gaussian walk, and the vector martingale central limit theorem give a circular Gaussian phasor limit with explicitly calibrated covariance. Conditional characteristic functions converge to random arcsine measures, and integrating out the Rayleigh radius gives the Gaussian measured-position limit. Uniform fourth moment bounds justify the non-self-averaging relative variance. The supplied independent numerical lattice evolution and seeded simulations check formulas, not the infinite-limit proof.

## Originality — PASS, qualified

Wang, arXiv:2605.06701, derives the noise-averaged second-moment growth rate and the phasor representation for the very same linear phase-kick model. These are explicitly treated as **prior** results. The claim here is the random limiting conditional measure, the exponential distribution of single-history cloud width, and their relation to the averaged Gaussian position law. The directly related full text was inspected, including its model and the transport discussion, and did not state those conditional-profile or width laws. Di Molfetta–Debbasch, arXiv:1409.2122, studies an annealed Gaussian limit of a different *coined* quantum walk with random gauge fields; its statement does not imply the Bessel-square conditional law of this model. Publicly indexed related results on two-periodic quantum walks, stochastic translations in coined walks, and quantum-Lindblad dephasing address different dynamics. The search and implication comparisons support a novel synthesis, not a claim of exhaustive priority. Unindexed equivalent literature and any unavailable versions of plausible papers remain risks.

## Value — PASS

A mean diffusion coefficient cannot distinguish typical and averaged spreading; here sample-to-sample fluctuations remain order one even as the averaged measured particle law becomes Gaussian. The theorem gives two observables of direct interest to random-force quantum transport—conditional spatial shape and single-history width—not merely a coefficient recomputation. The random arcsine versus Gaussian mixture mechanism makes ensemble diffusion and lack of typical-wavepacket self-averaging mathematically compatible and experimentally distinguishable. The result does not assert extensions to temporally correlated kicks or finite rings.

## Closest sources and limits

- P. Wang, *Diffusive transport from spatially correlated random phase kicks*, arXiv:2605.06701 (first public version 2026-05-11). Model and averaged spreading are credited.
- G. Di Molfetta and F. Debbasch, *Discrete-time quantum walks in random artificial gauge fields*, arXiv:1409.2122. The random gauge-field setting is related, but its coined one-step unitary is not this phase-kicked continuous-time tight-binding step.
- A. M. Childs, *Random and quantum walks in one dimension*, lecture notes. Standard coherent Bessel spreading, not the random conditional limit.

Self-review: passed. Independent audit: not yet performed.
