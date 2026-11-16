# Scientific review: graded Walsh sampling on Shidoku

## Correctness
PASS. The claimed row set is exhaustively enumerated in two different ways (288 grids). The identity \(K_d(u,v)=\sum_{j=0}^d\binom{a(u,v)}j\) is derived by counting common positive Boolean placements, so \(\operatorname{rank}_{\mathbb R}E_d=\operatorname{rank}_{\mathbb Q}K_d\). The delivered exact integer matrices satisfy symmetry, scaled idempotence, Gram annihilation, and the prescribed trace for degrees one, two, and three, establishing nullity lower bounds over \(\mathbb Q\). Ranks over \(\mathbb F_{1009}\) establish matching lower bounds, including full rank 288 at degree four. The code verifies these statements directly, not by trusting floating-point spectra. Probability-law nonidentifiability follows from the constant feature and an interior perturbation.

## Originality
PASS under bounded comparison. Arnold–Lucas–Taalman (2010) describe the Boolean variables, constraint ideal, and 288-solution enumeration, and Arnold–Field–Lucas–Taalman (2013) classify symmetry orbits, but neither gives the real degree-filtered sampling ranks. Known four-clue unique-completion counts can imply degree-four recovery, but not the exact quadratic rank 151 nor the 24-dimensional cubic moment kernel. A related exact finite Sudoku-placement complex result concerns topology of compatible placements for one symbol, not multi-board probability marginal ranks. The statistical-indicator study by Fontana–Rogantin (2009) is materially relevant; only its public abstract/extract was accessible, and undiscovered overlapping calculations remain a historical-priority risk. Novelty is not inferred simply from a failed keyword search.

## Mathematical value
PASS. The canonical smallest nontrivial Sudoku family provides a motivated exact benchmark for determining an unknown distribution by low-order local events, a problem distinct from unique completion of a single puzzle. The complete filtration \((1,25,151,264,288)\) identifies the sharp interaction threshold and quantifies exactly how many independent signed directions remain invisible even after observing all three-clue marginals. The degree-two and degree-three ranks and cubic 24-dimensional blind space are nontrivial structural facts rather than repetitions of the known 288-solution or four-clue counts.

## Closest literature and limitations
Closest: Arnold–Lucas–Taalman, *Gröbner Basis Representations of Sudoku* (2010); Arnold–Field–Lucas–Taalman, *Minimal complete Shidoku symmetry groups* (2013); Fontana–Rogantin, *Indicator function and sudoku designs* (2009). No larger-order formula, optimal noise conditioning, or independently verified historical priority is claimed. The inaccessible Fontana–Rogantin complete chapter and unindexed computations are specific residual risks.

Self-review: passed. Independent audit: not yet performed.
