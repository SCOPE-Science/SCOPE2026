# Scientific review

## Correctness — PASS

The odd-prime rank and lifting formula is the published Lucas valuation theorem [Murru–Sanna, arXiv:1603.09310v3, Theorem 1.5], specialized to discriminant \(P^2+4\). Its three cases, including ramification and parity at \(2\), are explicitly reconstructed in the proof. The Möbius transform is computed for all positive indices, and its support is exactly the rank times a prime power; the minimal repair multiplier is forced by rational denominators. Splitting in the quadratic characteristic algebra gives the necessary and sufficient criterion. Nonnegativity of every transform proves almost realizability. Tests are finite corroborations, not substitutes for the universal argument.

## Originality — PASS (with residual priority risk)

The September 2026 paper by Chuysurichay et al. establishes the classical Fibonacci and Lucas cases, not this entire \(P\ge2\) family, and expressly identifies general Lucas recurrences as a direction. Murru–Sanna's prior theorem gives raw valuations but not Dold spectra or orbit-count transforms; the latter calculations require the new convolution analysis. The 2021 general survey and Minton's linear-recurrence theorem do not treat the nonlinear prime-part transform. A published mathematical record about split companion Lucas sequences concerns \(V_n\) with square discriminant, not first-kind \(U_n\) with nonsquare discriminant. Unindexed previous derivations and incomplete inspection of Minton's original full text remain risks.

## Mathematical value — PASS

The theorem resolves a natural infinite-parameter branch of the generalization suggested in the motivating paper. Its exact quadratic splitting law, dichotomy at prime \(2\), minimal repairs and universal nonnegative orbit counts answer substantially more than a single numerical instance, while not claiming classification of arbitrary \(Q\). The arithmetic-to-dynamics correspondence gives a usable uniform criterion for a standard number-theoretic family.

## Reproducibility and limitations

The attached programs verify hundreds of parameter-prime pairs and exact transforms to bounded indices. The global theorem uses Lucas valuation and rank identities and Dirichlet's theorem. General Lucas second parameters, possible unindexed equivalent results, and independent validation are outside scope.

Self-review: passed. Independent audit: not yet performed.
