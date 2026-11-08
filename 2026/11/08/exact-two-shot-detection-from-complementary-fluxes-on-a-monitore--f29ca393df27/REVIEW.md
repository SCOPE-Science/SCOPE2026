# Scientific review: complementary-flux monitored quantum triangle

## Correctness — PASS

The claim explicitly fixes the three-site hopping orientation, target projector, two-stage flux order, sampling interval and arbitrary off-target initial vector. The Fourier decomposition of the published Hamiltonian yields two rank-one no-click factors with overlap magnitude \(1/2\); trace and determinant determine both singular values exactly. A positive derivative proves the global worst-case two-probe optimum. The spectral-radius lower bound follows from the determinant; an exact characteristic polynomial proves attainment. At the revival boundary both unitaries are scalar, so detection is impossible. All nonrevival survival tails obey a strict contraction bound. The bundled standalone checker reproduced exact symbolic identities and 1,071 finite numerical diagnostics using full matrix exponentials. The analytical proof is independent of finite sampling.

## Originality — PASS, with stated residual risk

Wang et al. [1] already establish the triangle Hamiltonian and dark-state behavior with *fixed* magnetic flux; no novelty is assigned to the spectral diagonalization or the general dark-state concept. Thiel et al. [2] establish dark/bright decomposition for a repeated *fixed* unitary. Kessler et al. [3] replace fixed probe intervals by random intervals but do not cyclically switch flux Hamiltonians. Wang et al. [4] change spatial couplings instead. Liu et al. [5] analyze periodic local no-click measurements driven by repeated powers of a *single* survival operator, not by the alternating two-flux product. Direct implication comparison shows none supplies the matrix product with *two complementary noncommuting failure operators* or the exact global two-shot minimax, strict all-state detection criterion and optimal spectral radius for this protocol. Semantic searches in published research records and public literature found no covering claim. A generalized periodically monitored quantum-dynamics theorem not indexed or fully searched remains a residual publication-priority risk; this does not assert definitive uniqueness.

## Mathematical value — PASS

Fixed-flux monitoring has a physically meaningful dark-state obstruction: some normalized states escape detection indefinitely. Complementary controlled fluxes eliminate the obstruction with a finite quantitative uniform contraction, without changing measurement target or resorting to full-site tracking. The exact optimizing interrogation interval, worst-case two-probe guarantee and globally optimal asymptotic spectral radius are sharp, experimentally interpretable operational bounds for the natural minimal chiral cycle. This is not merely a small parameter substitution into a known stationary formula.

## Closest sources and limits

[1] Q. Wang et al., arXiv:2402.15843v1, 2024-02-24; full text Sections 3 and 6 and relevant appendices inspected via https://pmc.ncbi.nlm.nih.gov/articles/PMC11508062/ . [2] Thiel et al., arXiv:1906.08112, full open text inspected, fixed-H protocol. [3] Kessler et al., arXiv:2012.01763, full open text inspected, random probing time but fixed-H protocol. [4] Q. Wang et al., DOI 10.1103/PhysRevResearch.5.013202, accessible primary text inspected, spatial perturbations. [5] Liu et al., DOI 10.1103/PhysRevResearch.4.023129, primary 22-page full text inspected, Sections I–III and application/summary, repeated fixed survival operator. Scope excludes noise, arbitrary controls, graph enlargement and experimental validation. The completed work remains subject to independent assessment.

Self-review: passed. Independent audit: not yet performed.
