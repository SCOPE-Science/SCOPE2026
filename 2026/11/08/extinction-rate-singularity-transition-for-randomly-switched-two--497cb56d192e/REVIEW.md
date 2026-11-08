# Scientific review: extinction-rate singularity transition

## Correctness

**PASS.** The model maps the three-coordinate simplex to itself, and satisfies all three F-stochastic conditions with the same explicit functions \(\varphi(x,y)=(x+y)^2/2\) and \(g(t)=t^2/2\). The two-step reduction is exact: after the first update the surviving proportions are the selected offspring proportions, and then \(s_{n+1}=c_{\xi_{n-1}}s_n^2\). Taking logarithms and summing a geometric series establishes the pathwise exponent and a bounded error between the exponent-scaled limit and the finite iterate. Binary cylinder calculations and the strong law establish the measure classification, while the standard entropy estimate for dyadic cylinders proves the exact dimension. Independent symbol contributions give the stated moments. The finite checker passed; it is not a substitute for the analytic proof.

## Originality

**PASS within inspected evidence.** The 2024 F-stochastic operator papers establish stability, Markov-chain constructions and path-measure properties; the 2023 sexual-system paper considers random switching and convergence. The present result instead identifies the **distribution of the samplewise double-exponential decay exponent** as an affine biased dyadic measure, with a uniform–singular transition, dimension and full mutual-singularity classification. Those source conclusions do not imply an explicit exponent law without the specific quadratic reduction. The classical Bernoulli dimension theorem is acknowledged, not presented as novel. Closest comparison: Souissi–Mukhamedov (2024), DOI 10.1007/s44198-024-00172-6, Definition 3.1 and Theorems 3.3–3.6; Jamilov et al. (2024), DOI 10.1002/mma.10191, Theorem 3.5 and Section 4; Jamilov et al. (2023), DOI 10.1016/j.heliyon.2023.e17913, Theorem 4.1. Searches do not prove publication priority. A previously unindexed calculation of this particular switched family remains a risk.

## Mathematical value

**PASS.** Extinction is already known in broad two-sex stochastic systems, but its **random sharp asymptotic speed** is a natural observable not determined by existence of a common extinct equilibrium. Here identical deterministic attractors coexist with sharply different pathwise-rate laws: uniform versus singular continuous, and distinct biases have mutually singular laws even though their supports coincide. The theorem covers continuous offspring parameters and all interior initial states, and supplies a deterministic finite-step error bound rather than only an asymptotic description. General random quadratic models outside this family are not classified.

## Limitations and verification status

The switching must be iid with two positive-probability choices and distinct reproduction contractions; degenerate initial compositions and more general environmental processes are outside scope. The Bernoulli measure dimension computation uses standard mathematics. No claim of independent validation or exhaustive publication-priority coverage is made.

Self-review: passed. Independent audit: not yet performed.
