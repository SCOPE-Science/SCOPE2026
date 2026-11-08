# Scientific review: a sharp public-goods/opinion switching boundary

## Correctness — PASS

The underlying decision rule follows by exactly maximizing the strictly concave quadratic opinion payoff separately for each binary action and comparing the optimized values. For the prescribed alternating community actions, the two-step affine opinion map has Lipschitz constant at most \(c^2<1\), giving exactly one possible opinion pair. Its block-swap symmetry reduces that pair to two levels whose difference is \(d/(d+2cp)\). Testing both strict action choices gives the necessary and sufficient condition \(p<p_*\). At equality, the convention to defect at an action tie eliminates the alternating pattern. Strict thresholds make the two-step linearized map a genuine local contraction in **all** opinion coordinates, not merely on the two-block subspace. Both consensus equilibria are strict and attracting because \(1/2<\theta<1\). The exact four-player witness verifies the equations with nonzero switching margins. `CHECK.py` passed its symbolic and rational tests. No finite test is used to infer the all-size result.

## Originality — PASS (with residual risks)

The full main model and equilibrium analysis of Davidson et al. [1] concern consensus, existence of stationary states and sufficient global-defection convergence. Their exposed main theorems do not establish attracting simultaneous-update cycles or a sharp cross-influence cutoff. The general possibility of two-cycles is **not** new: the Boolean threshold analysis of Kuhlman et al. [2] covers a different, finite-state dynamical system, not the continuous-opinion public-goods memory map or the derived cutoff. Liang et al. [3] study action-dependent coordination/anti-coordination payoffs rather than the constant marginal action disadvantage of the public-goods game; its convergence results cannot be substituted as a theorem for this model. The distinct mathematical contribution is the exact existence, uniqueness in the alternating class, stable full-state realization and robustness for all even population sizes. Risks remain from unindexed equivalent formulas and more general piecewise-affine network theorems not exhaustively eliminated by the searches. Absence of a match is not asserted as proof of global novelty.

## Mathematical value — PASS

The mechanism identifies a concrete limit to consensus-based predictions for synchronous best response in public-goods games. An open parameter region on a connected **fully positive** network has two stable consensus equilibria and a stable temporal alternation of collective decisions, with a computable sharp boundary in the ratio of within- to between-community opinion influence. This is a structural dynamical classification rather than an arbitrary example or trivial parameter substitution. The threshold remains meaningful for every even group size and the example demonstrates nonzero margins and transverse stability. It is neither a claim about all attractors nor a universal convergence theorem.

## Closest literature and limits

[1] E. C. Davidson et al., *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1 (April 10, 2026). Full HTML main model and relevant results reviewed.

[2] C. J. Kuhlman et al., *Bifurcations in Boolean Networks*, DMTCS proceedings, 2012, DOI:10.46298/dmtcs.2975. Relevant PDF definitions and the synchronous limit-period theorem inspected.

[3] H. Liang et al., *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, arXiv:2505.03078v1 (May 6, 2025). The model and convergence framework inspected in accessible HTML.

Boundary \(p=p_*\) is an action-tie point, not a claim of a smooth local bifurcation. Attractors beyond the three exhibited and behaviors under asynchronous or stochastic updates are unclassified. The comparison with all prior mathematical literature is necessarily incomplete.

Self-review: passed. Independent audit: not yet performed.
