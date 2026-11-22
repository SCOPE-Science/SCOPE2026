# Review of the five-car parking-function Fourier nullspace

## Correctness — PASS

The all-size forced-zero inclusion follows directly from Pollak's coset-transversal lemma, with nontrivial annihilator characters summing to zero on the quotient. The finite new part is an exact exhaustive enumeration of the 252 sorted frequency multisets of five coordinates in a six-element alphabet. Integer residue histograms are reduced modulo the monic cyclotomic polynomial \(\Phi_6\), never via approximate complex arithmetic. All 7776 characters are covered by multinomial orbit sizes. The supplied verifier also checks the parking inequalities against independent sequential simulation and confirms that each parking word selects a different diagonal coset. The five additional multisets have orbit sizes 60, 60, 120, 60, 60, giving nullity 1655 and rank 6121. No extrapolation beyond five cars enters the novel claim.

## Originality — PASS, bounded priority assessment

The 1996 Stanley paper was inspected materially, including the full Section 2: it states the Pollak transversal result, so that part is credited as existing. Its symmetric-group Frobenius-characteristic formulas are not the coordinate-modular additive Fourier multipliers classified here. The full published results on prime-power cyclic transversal defects and frustrated parking-order outcomes were compared: their hypotheses concern different cyclic groups and different parking protocols respectively. Index searches for exact parking-function Fourier zero patterns, six-element alphabet, orbit counts and rank 6121 did not yield a covering claim. This is a bounded negative comparison, not uniqueness proof. The remaining material risk is a previously unindexed root-of-unity specialization of a multivariate preference enumerator.

## Value — PASS

Parking-function preference vectors are canonical representatives of a diagonal quotient, making the baseline Fourier nullspace inevitable. Knowing whether that nullspace is **complete** is the natural exact recoverability question. The first four sizes show no extra loss, whereas the first mixed-prime alphabet (six residues, five cars) loses 360 further modes, with a complete orbit-level explanation and exact recovery rank. This is a motivated finite cutoff, not an arbitrary numerical slice; it demonstrates that the classical transversal property alone does not predict the full spectrum. It does not claim any larger-size classification.

## Closest literature and limitations

R. P. Stanley (1996), *Parking Functions and Noncrossing Partitions*, Section 2, https://math.mit.edu/~rstan/papers/nc.pdf. Diaconis and Hicks (arXiv:1611.09821, first public 29 November 2016) provide related probability context. The published report *Exact Fourier-notch survival under sparse defects of cyclic transversals* treats a distinct prime-power cyclic relocation problem, and *Outcome fibers and modal parking orders of frustrated parking functions* treats a different parking rule. Historical equivalent formulations remain possible; the exact bounded result carries no assertion of independent validation.

Self-review: passed. Independent audit: not yet performed.
