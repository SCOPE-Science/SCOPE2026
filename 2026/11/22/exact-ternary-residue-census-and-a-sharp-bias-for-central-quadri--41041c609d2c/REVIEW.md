# Mathematical review

## Correctness — PASS

The coefficient/central-index normalization is explicit. Reduction via Frobenius holds over \(\mathbf F_3\) for every ternary digit of every nonnegative index. The bounded carry range is proved, not assumed. Two finite reachable graphs are fully displayed, and a standalone implementation independently generates their nodes and digit edges. The final-parity filter selects exactly the appropriate branch. Both closed recurrences have been checked on enough exact levels to combine their degree-two/degree-three annihilators with the eighteen-state characteristic polynomial, giving a finite-to-infinite proof by Cayley–Hamilton. Positivity and the sharp dominant exponential root follow from elementary recurrence analysis. The direct polynomial coefficients checked through \(n=728\) are independent computational cross-checks, not substitutes for that proof.

## Originality — PASS within inspected evidence

The exact object differs from a fixed-index prime-square quadrinomial congruence. Mechacha's arXiv:2307.16768v1 and Belbachir–Otmani (Integers 23, A27) were read in their substantive theorem/proof portions. Hoggatt–Smith's historical central-triangle paper and OEIS A005190 were inspected for tables and recurrence statements. Their stated conclusions do not give the complete \(3\)-residue census of the central diagonal at every ternary power or the rational signed-bias series. The general automata approach can in principle generate such results but does not logically imply these particular exact formulas without nontrivial specialization. Searches of a mathematical research index and older available claims found no same-statement match. This is not a priority proof: an equivalent hidden in an older general algorithm or indexed with different terminology is a realistic risk.

## Mathematical value — PASS

The central coefficient is the maximal coefficient of the classical quadrinomial row, so its modular distribution is a canonical arithmetic statistic. The theorem simultaneously identifies a Fibonacci support, all three exact residue counts, a strict signed-class preference, and the sharp secondary scale. The two nonzero classes are asymptotically balanced yet not exactly balanced, a meaningful refinement of simple modular nondivisibility. These are infinite all-scale structural identities rather than a small parameter table.

## Boundaries

The result does not extend to all cutoffs, arbitrary four-term coefficients, or modulus nine; automated general methods could have equivalent implicit coverage. Independent auditing has not been performed.

Self-review: passed. Independent audit: not yet performed.
