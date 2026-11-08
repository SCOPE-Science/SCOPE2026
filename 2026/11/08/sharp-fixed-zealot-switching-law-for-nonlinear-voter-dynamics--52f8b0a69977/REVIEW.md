# Review of the fixed-zealot switching-time law

## Correctness — PASS

The proof specifies the all-individual rate-one selection clock, two opposing permanent zealots, fixed integer \(q\ge2\), and finite \(S\ge2\). The published transition-rate expressions specialize to the stated generator. Reversible weights \(\binom Sk^{1-q}\) satisfy detailed balance exactly, and the stopped backward equations telescope to the finite formula. A uniform \(O(S^{-1})\) estimate controls the prefix weights, while a central-binomial Gaussian Riemann sum and exponentially negligible tails prove the precise constant and power of \(S\). The embedded standard-library checker separately inverts the finite generator and compares the formula using exact fractions; 260 checks passed. Neither simulations nor finite computations are used as the infinite-population proof.

## Originality — PASS within inspected evidence; historical priority provisional

Mobilia (2015, arXiv:1506.04911, Sections II, IV and V.A) defines the same finite model, gives its exact stationary law, and studies the same first-switching event via a backward Fokker–Planck approximation, describing approximately exponential growth. This is the strongest antecedent and is directly acknowledged. The inspected treatment does not establish the present *exact fixed-zealot-count sharp coefficient and polynomial prefactor*, and its fixed-positive-density continuum approximation cannot be directly substituted into the singular one-zealot-per-party limit. The present discrete hitting-time identity plus localization supplies an analysis not contained in the stated prior conclusions.

The 2016 heterogeneous \(q\)-voter study and the 2014/2015 zealot evolutionary-game paper concern different transition structures or objectives. Targeted published-finding corpus and scholarly searches did not identify a dominating sharp fixed-zealot switching law. Negative searches are not a proof of world-wide novelty; inaccessible or unlocated treatments of this singular regime remain a priority risk.

## Value — PASS

The precise switching law quantifies the time needed for a finite well-mixed electorate to move completely between the two opposing consensus configurations when the number of committed agents remains fixed while the changeable population grows. It distinguishes the exponential factor \(2^{(q-1)S}\), the nontrivial \(S^{-(q-2)/2}\) prefactor, and the explicit \(q\)-dependent constant. This resolves a motivated quantitative gap left by qualitative exponential estimates, with an exact finite formula useful for benchmarking finite-state computations. It does not purport to model observed voting or yield practical societal predictions.

## Sources and limitations

Primary: Mobilia, *Nonlinear q-voter model with inflexible zealots*, Physical Review E 92, 012803 (2015), https://arxiv.org/abs/1506.04911, especially original Sections II, IV and V.A, with accepted manuscript https://eprints.whiterose.ac.uk/id/eprint/87063/1/QvotersZealots_Mobilia_PRE_Accepted_12June2015.pdf . Context: Mellor–Mobilia–Zia, *Characterization of the Nonequilibrium Steady State of a Heterogeneous Nonlinear q-Voter Model with Zealotry* (2016), https://arxiv.org/abs/1601.03766 ; Nakajima–Masuda, *Evolutionary dynamics in finite populations with zealots* (2014), https://doi.org/10.1007/s00285-014-0770-2 . The scope fixes \(q\), places exactly one zealot on each side, and uses the stated global selection time unit. Historical priority is provisional, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
