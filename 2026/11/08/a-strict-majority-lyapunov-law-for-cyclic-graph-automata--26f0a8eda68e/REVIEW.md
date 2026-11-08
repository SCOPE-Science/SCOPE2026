# Scientific review: a strict-majority Lyapunov law

## Correctness — PASS

The proof derives a one-round exact boundary-edge identity: only boundary edges connecting a mover to a successor-colored nonmover become monochromatic, while equal-color boundary edges cease to be monochromatic. Because three or more cyclic states prevent reciprocal successor relations on internal mover–mover edges, the total successor-neighbor demand bounds the number of gained boundary edges and gives the stated inequality. Summation over the bounded integer monochromatic-edge potential proves termination and the update budget for any finite graph. The complete tripartite three-cycle and bipartite two-color cycle directly verify both claimed boundary failures. The torus graph is eight-regular for side length at least three. A direct executable implementation of the definitions in the included verification script passed 1,319,754 exhaustive small-graph trajectories, 5,001 partial-update checks and the listed random and torus tests. No finite calculation is used as a replacement for the infinite graph-size proof.

## Originality — PASS within checked evidence

The 2026 motivating paper directly treats the Moore cyclic rule and empirically observes no long cycles at high thresholds, but the inspected threshold sections do not establish a deterministic, all-initial-state, arbitrary-graph potential inequality. The 1991 original threshold-range paper discusses large-scale lattice fixation and traveling-wave thresholds, not a finite-graph worst-case edge-count bound in the inspected relevant sections. The 2021 tree paper proves almost-sure statements for random initial states on infinite trees; these do not imply deterministic finite-graph fixation for all configurations. Binary threshold-network Lyapunov theorems allow period two and are not equivalent to the strictly oriented successor rule with three or more colors. Historical comparisons with finite-graph cyclic-automata work are incomplete because the primary 1997 article could not be accessed; that is an explicit residual priority risk, not evidence that the inaccessible article lacks an equivalent statement. No claim of exhaustive global priority is made.

## Mathematical value — PASS

This is a structural all-configuration stabilization result for a natural high-contact regime of a recently studied cyclic-dominance automaton. It gives a finite-time bound linear in the number of edges, survives arbitrary simultaneous eligible batches and heterogeneous local thresholds, identifies why three cyclic colors differ from binary majority dynamics, and shows that the strict majority hypothesis is a genuine universal transition rather than a convenient sufficient numerical cutoff. These features are not consequences of merely enumerating a small state space. The unresolved borderline Moore threshold remains separate.

## Closest literature and limitations

Relevant work: Muñoz–Nuño (2026, arXiv:2610.37990), Fisch–Gravner–Griffeath (1991, doi:10.1007/BF01890834), Bello–Sivakoff (2021, arXiv:2108.06404), and Matamala–Goles (1997, doi:10.1016/S0166-218X(97)84104-2). Only the first three had directly inspected primary text. The 1997 primary remained inaccessible after open-access and institutional-access attempts; it remains a plausible historical-overlap risk. No claim is made for directed/infinite graphs, the critical half-degree threshold, or sharpness of the Moore-specific time constant.

Self-review: passed. Independent audit: not yet performed.
