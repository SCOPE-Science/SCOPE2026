# Scientific self-review

## Correctness — PASS

The proof derives the exact invariant bipartition-constant dynamics \(u\mapsto u-(r+s)h\sin u\) and checks that the nonconstant two-cycle returns in the full phase lift, rather than only modulo phase. The graph Laplacian's top eigenvalue equals \(r+s\) by Perron–Frobenius for the signless Laplacian; differentiation at both orbit points gives the same Jacobian \(I-h\cos a L\). Squaring yields every return multiplier, so the exact open stability window and all-unit collision follow by elementary inequalities. Convex minimax balancing of the extreme nonzero eigenvalues proves the unique optimized contraction, and explicit expansions prove the edge and scalar parabolic laws. The executable finite checks passed 92 assertions; the all-size result rests on the proof, not the enumeration.

## Originality — PASS, subject to stated priority risk

The motivating 2026 Huygens article establishes small-parameter Lyapunov descent, fixed-point convergence and a Morse–Smale criterion, not the large-step period-two branch. Its 2026 follow-up treats rings inside the Lyapunov regime. Preceding exact analyses cover the general bipartite *local* bifurcation near onset and the entire branch on *even cycles*. Those cases and their proof techniques are treated as prior work, not independent novelties. The assessed advance is the entire sharp stability interval, exact graph-optimal decay and endpoint laws across connected **biregular bipartite** graphs, including stars and hypercubes, not implied by any inspected stronger statement. Specialized older results may still affect priority.

## Mathematical value — PASS

The loss of the discrete Lyapunov guarantee is an intrinsic dynamical threshold. The theorem resolves what happens afterward for a natural, graph-theoretically characterized family: global parameter continuation of a specific two-cycle, an all-mode threshold, optimal spectral decay involving algebraic connectivity, and a simultaneous neutral collision. The explicit star and cube formulas extend the result beyond previously known even-cycle calculations. The theorem does not overstate global basins, uniqueness of all orbits or transverse nonlinear stability at the neutral endpoint.

## Closest literature and limits

The closest primary sources are arXiv:2610.10993v1 and arXiv:2610.19953v1. Earlier local weighted-bipartite bifurcation work and exact even-cycle specializations have overlapping conclusions; the new statement explicitly isolates the non-implied graph-family extension. Other work in discrete Kuramoto and coupled-map theory remains a residual historical priority risk. The verification is same-model only, not independent.

Self-review: passed. Independent audit: not yet performed.
