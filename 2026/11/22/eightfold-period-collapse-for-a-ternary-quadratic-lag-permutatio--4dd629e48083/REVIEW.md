# Scientific assessment

## Correctness — PASS

The claim is the equality \(\operatorname{Fix}(T_k^{8k})=\operatorname{Fix}(T_k^{4k})\) over \(\mathbb F_3\) for all integers \(k\ge2\). The map is invertible. Every period-\(8k\) state gives an eight-row cyclic column difference system. Column masks have weights divisible by three; the zero mask propagates and implies the zero state. The remaining 84 masks are exhaustively enumerated with two independent constructors, yielding 96 distinct arrows. Four repeat-four-row masks are the only possible cyclic vertices; their 80-vertex complement has no three-edge walk, and they have no edges to the complement. Rotation-equivariance closes the otherwise twisted column path. Each allowable mask has three nonzero entries per four rows, so summing four consecutive differences forces \(4k\)-periodicity. The reverse fixed-set inclusion is tautological. The attached standalone checker reconstructs the finite certificate and checks every state for \(k=2,\ldots,11\); the bounded tests are supplemental, not the universal proof.

## Originality — PASS, qualified

Full relevant sections of Finch's arXiv:2610.34300v1 establish the fourfold fixed-point count, not the new equality with the eightfold fixed set. The published primitive short-period census refines only the sector of periods dividing \(4k\). The published fivefold, sixfold and sevenfold exclusions concern different iterates. Their complete relevant claims were compared by implication, not just title. published-finding corpus semantic queries for eightfold collapse, fixed sets, period doubling and eight-row support graphs did not return an equivalent or dominating theorem. In particular, the explicit \(k=2\) eight-cycle already has period \(4k\), so it does not imply an exact all-lag eightfold count. Unindexed earlier treatments, including the inaccessible complete text of some historical related recurrence work, remain residual priority risks; search absence is not a proof of uniqueness.

## Mathematical value — PASS

The eighth multiple is the first nontrivial even repeat after the known fourfold periodic sector and the five-, six- and sevenfold exclusion window. It is a natural period-doubling test for this nonlinear arithmetic permutation. The theorem supplies a sharp complete obstruction to the appearance of any new \(8k\)-periodic states, together with an explicit exact census inherited from the fourfold theorem, at all lags. The proof exposes a small, rigid cyclic core of the eight-row carry-support graph. This is structurally more informative than a bounded numerical census or a reformulation of the earlier fourfold count. It does not describe arbitrary periods.

## Closest literature and remaining risks

Finch (2026), arXiv:2610.34300v1, §3, Proposition 7 and Theorem 8; the published complete primitive-cycle census for periods dividing \(4k\); and the five-, six-, and sevenfold exclusion studies were compared. Any implicit proof of the same eightfold rigidity in earlier work would defeat originality; full access to every older related source was not available. The finite certificate can be rerun with ordinary Python and has no external dependencies.

Self-review: passed. Independent audit: not yet performed.
