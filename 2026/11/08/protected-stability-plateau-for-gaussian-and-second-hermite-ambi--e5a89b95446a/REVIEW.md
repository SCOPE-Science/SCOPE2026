# Scientific review

## Correctness — PASS
The exact normalized second-Hermite ambiguity formula is the established \(e^{-s/2}L_2(s)\). The critical new identities \(L_2(s)^2-1=s(s-4)(s-2)^2/4\) and \(D'(s)=-(s-1)(s^2-8s+14)\) establish all stationary-point signs and boundary cases. The polynomial derivative of \(F_{1/4}\) yields its three strict monotonicity intervals and unique second crossing. For larger disks, the lower envelope consists of a strictly decreasing interior-minimum branch and a strictly increasing endpoint branch, proving the unique intersection and all asymptotics. The checker verifies the precise polynomial identities using rational arithmetic, independently integrates the Hermite ambiguity, and tests both optimizer branches. Finite tests are not substituted for this continuous proof. At the isolated radius \(T=2\), optimizer nonuniqueness is accounted for explicitly.

## Originality — PASS relative to investigated sources
Alaifari–Yang (arXiv:2410.05486; inspected introduction, Hermite-window §2.2 and stability discussion) state the general Laguerre ambiguity formula and propose window coverage but do not give the sharp Gaussian/second-Hermite weighted minimax. Bertolini–de Dios Pont–Pineau–Ramos–Taylor (arXiv:2605.20527; inspected full accessible HTML introduction and main results) prove a distinct local signal-space stability theorem. The Gaussian/first-Hermite disk minimax problem uses a linear Laguerre factor and is not a theorem covering the second-Hermite protected plateau, the exact exit radius, or the fourth-power limit. Semantic searches of published mathematical records for the second-Hermite minimax and its exact exit condition returned no implication covering this claim. This does not establish comprehensive publication priority; unexplored optimal-design terminology remains a risk.

## Value — PASS
The two-window squared ambiguity gain is the exact pointwise denominator in an experimentally motivated direct-inversion procedure. A previously unquantified second-order phenomenon is established: after an ordinary Gaussian-only regime, a *single precisely quarter-weighted design* protects the worst-case margin on a disk whose dimensionless squared radius expands from \(4\) to \(8.8327\ldots\) at zero additional loss, before the bottleneck splits into two equalized active radii. The full optimizer and asymptotic \(T^4e^{-T}/4\) are sharp and useful for deciding window allocation rather than relying on qualitative coverage plots.

## Remaining limitations
The result does not bound nonlinear signal reconstruction, sampling error or stochastic estimation beyond the explicitly defined pointwise linearized gain. Source inspection establishes novelty only relative to available texts. An equivalent earlier design calculation under different vocabulary is possible. Independent review and independent priority assessment have not been performed.

Self-review: passed. Independent audit: not yet performed.
