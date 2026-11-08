# Scientific review: a single pendant vertex and majority oscillations

## Correctness — PASS

The exact claim counts states fixed by the second iterate but not the first, for all labelled one-leaf cycles with \(n\ge3\) under synchronous open-neighbor majority with tie retention. The leaf's two temporal phases are forced by the core's two phases. This gives a bijection from periodic states to words in four local phase-pair symbols with precisely one exceptional local transfer. The finite 16-state transfer identity \(A^2(A^6-2A^5+2A^3-2A^2+I)=0\) is verified by the standalone integer-matrix program, and six starting traces prove the all-length formula by recurrence uniqueness. Fixed states reduce exactly to cyclic binary words without isolated bits. A separate direct-update implementation exhaustively checks all \(2^{n+1}\) states for \(3\le n\le13\). Small experiments are not used as infinite proof. Reproduction requires Python 3 and SymPy for the symbolic checker; the independent direct checker uses the standard library only.

## Originality — PASS, with residual priority risk

The nearest recorded mathematical claims are the exact all-sites sunlet decoration and the homogeneous radius-one majority cycle. They imply respectively an all-sites formula and a bare-cycle formula, neither of which gives the one-pendant defect formula by specialization, because their graph families do not contain a single pendant insertion. Mathematical-record searches using both name-based and statement-based variants found no matching exact one-leaf census; searches cannot establish absolute novelty. Tošić–Agha's 2004 full-text treatment concerns regular one-dimensional cellular spaces and establishes the homogeneous cycle classification, not the irregular one-leaf network. Kaaser–Mallmann-Trenn–Natale (2015), inspected in its accessible arXiv text, addresses convergence time, not the number of initially periodic configurations. Nakar–Ron (2022) focuses on homogeneous one-dimensional majority automata, not a single graph defect. A theoretically possible unindexed exact equivalent is a residual historical-priority risk, not proof of overlap absence. No stronger covering theorem was found in the materially inspected sources.

## Mathematical value — PASS

This is a sharp one-defect sensitivity theorem in a natural deterministic opinion model: a single private leaf changes the number of least-period-two states from at most two to Fibonacci-order exponential growth while leaving the fixed-point count exactly unchanged. The explicit congruence correction, existence cutoff \(n=4\), and rigorous entropy rate \(\log\varphi\) are intrinsic infinite-family invariants. The result is not merely an additional sample count, a change of notation, or a corollary of the completely leaf-decorated cycle.

## Closest literature and limitations

Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 2015-08-14) prove general voting-time bounds; Tošić and Agha (DOI:10.1007/978-3-540-30479-1_89) classify homogeneous one-dimensional majority states; Nakar and Ron (arXiv:2205.08972v1) study spatial structure in homogeneous majority automata. All were compared at the level of hypotheses and conclusions. No external review of the theorem is claimed. Basins, eventual rather than initial period-two states, and other tie conventions are outside scope.

Self-review: passed. Independent audit: not yet performed.
