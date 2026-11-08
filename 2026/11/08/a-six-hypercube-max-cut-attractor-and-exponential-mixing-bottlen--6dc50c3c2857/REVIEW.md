# Scientific review

## Correctness (C): PASS

The exact local flip criterion is derived from the odd-sized closed neighborhood, not inferred from simulation. The explicit multi-affine cut formula proves the maximum and its full equality set. A constructive two-part sweep gives a finite directed path of at most \(2n\) flips from every starting state. The six hypercube faces of the global-optimum set communicate by neutral, reversible moves, and no energy-decreasing trajectory can leave the set. Exact boundary-edge counts give the stationary escape flux. Starting from the stationary measure conditioned on one face yields the total-variation mixing lower bound without assuming independent phase exits.

Two independent executables provide finite corroboration: direct transition-graph strongly connected components for \(1\le n\le4\) and exhaustive constructive reachability and face-boundary checks for \(1\le n\le6\). They reproduce the attached recorded outputs. The general theorem is proved symbolically for arbitrary \(n\ge2\); neither finite test purports to certify the infinite case.

## Originality (O): PASS, qualified

The primary foundational comparison is Rouquier–Regnault–Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1, whose accessible text specifies this update law, proves the general energy monotonicity, and analyzes cliques, cycles, paths, trees and bipartite mechanisms. It does not provide the exact six-hypercube recurrent class or exponential mixing obstruction on balanced complete tripartite graphs. Papp–Wattenhofer's *Stabilization Time in Minority Processes* (2019, DOI:10.4230/LIPIcs.ISAAC.2019.43) is a particularly important negative implication comparison: their switchability requires a **strict** decrease in conflicts, while every move inside the recurrent class here is a neutral tie move. Closest research-record and related graph-dynamics comparisons have different updating rules or graph families.

The general energy identity is credited rather than claimed as new; the original contribution assessed is its sharp tripartite consequence together with the exact neutral-flip graph and stationary flux. Historical priority is qualified because unindexed zero-temperature antiferromagnetic reconfiguration literature might contain an equivalent result. The accessible 2014 game-theoretic comparison was not read in full.

## Mathematical value (V): PASS

A complete characterization of global recurrent behavior on a standard dense regular graph is intrinsically useful for understanding stochastic anti-coordination. The theorem exposes a strong structural separation: every state has a directed path to global optimality using at most \(2n\) flips, yet equilibrium on the unique attractor needs more than \(\lfloor3\cdot2^n/4\rfloor\) random updates to mix. The exact six-face geometry and face-exit rate \(2/(3\cdot2^n)\) explain the exponential bottleneck despite frequent local motion. These are not consequences of correctness or enumeration alone.

## Scope and residual risks

No matching upper mixing bound, exact spectral gap or generalization to unequal tripartite parts is asserted. The full historical literature cannot be exhaustively excluded. Reproducible finite checks are included but do not constitute independent validation.

Self-review: passed. Independent audit: not yet performed.
