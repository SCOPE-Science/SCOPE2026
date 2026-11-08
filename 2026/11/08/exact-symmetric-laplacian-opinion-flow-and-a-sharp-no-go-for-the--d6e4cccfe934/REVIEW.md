# Scientific assessment

## Correctness — PASS

The claim is an operator identity, not an extrapolation from simulation. Each two-qubit exchange pair acts on an opinion observable at *both* endpoints: the adjoint dissipator identities produce the two symmetric conductance contributions. The diagonal Ising Hamiltonian commutes with each opinion observable, and the anchor dissipators give the specified affine drift. Summing over all ordered arcs yields the exact expectation system for arbitrary joint density matrices. Comparing off-diagonal coefficients proves the sharp no-go. Positive semidefiniteness of the symmetric Laplacian proves the variational, convergence, and consensus statements. Both exact three-agent witnesses were independently recomputed with rational arithmetic, and the supplied full-state generator checker passed 48 further finite tests. Tests corroborate the proof but are not its substitute.

## Originality — PASS, with delimited prior coverage

The primary paper (Chu, arXiv:2607.01452, §§3.1–3.4 and Appendix A) prints the full pair-exchange generator and derives a directed Friedkin–Johnsen first-moment equation by treating only those interactions in which the monitored agent is the *first* endpoint. Its Section 4.1.1 attributes deviations between the full system and that reduced equation to inter-agent correlation feedback. The full first-moment closure, the missing incoming-arc contributions, the no-go statement, and the incompatible consensus predictions are not stated there. The primary full text was inspected at the defining equations, inference, numerical comparison, and appendix.

Schulman and Sinclair (arXiv:2607.22991, §§1–2) explicitly study symmetric exclusion with reservoirs on general graphs; the diagonal Markov process here belongs to that established class. Mendonça (arXiv:1207.4106) treats the spin/exclusion correspondence. Accordingly, the mathematical identity for a generic exclusion process is **not** being presented as novel. The narrow original content assessed here is the published-opinion-model-specific contradiction and its exact analytical consequences, not a new theorem about exclusion in general. No searched indexed finding or accessible own-claim match established that precise comparison. The main residual risk is an overlooked independent erratum or equivalent diagnosis not indexed in searched sources. This is a same-model, not independent, assessment.

## Value — PASS

The claimed recovery of a directed opinion model is a foundational justification for the published quantum social-network formulation. The exact no-go rules it out for every genuinely interacting parameter choice under the written generator. It also revises the explanation of the numerical full-vs-reduced discrepancy: although the full process generates correlations, its expected opinions cannot receive any feedback from them. A connected directed network with different predicted consensus values, and a positive-stubbornness example with different equilibria, make this a substantive model-interpretation issue rather than a formatting or normalization observation. These results matter when selecting the generator for directional influence and when comparing classical and quantum predictions.

## Boundaries and residual risk

The claim concerns first moments of the *literal* Eq. 14 generator. It does not dismiss quantum correlations or imply that no alternative dissipators can produce a proper FJ lift. The classical exclusion correspondence is prior literature, and some equivalent model-specific discussions might be unindexed. The independent scientific audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
