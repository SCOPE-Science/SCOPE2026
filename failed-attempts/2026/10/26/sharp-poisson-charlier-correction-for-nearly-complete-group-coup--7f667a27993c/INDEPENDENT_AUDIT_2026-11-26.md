# Independent mathematical audit

## correctness

PASS

Counting ordered tuples of missed types gives μ_j=λ^j R_j up to r and μ_j=0 thereafter. With b_j=δ j(j−1)/2, in j≤r/2 the logarithm x_j=−log R_j is nonnegative, has |x_j−b_j|≤4t j³/r², and is at most t j²/r; Taylor's inequality for exp(−x_j) gives the stated fourth-degree bound, including the zero-moment-index case. Beyond r/2, 0≤R_j≤1 and j²/r>1/2 give the other bound including the cutoff tail. The generating series in z−1 gives ordinary factorial-moment inversion; the quadratic correction is the coefficient of −δλ²(z−1)² exp(λ(z−1))/2. Its masses have the signed Charlier convention stated in the record. The absolute coefficient norm of (z−1)^j is 2^j, so summing gives the claimed Touchard factor by absolute convergence. The reverse triangle inequality and convergence of the absolute Charlier moment (uniform integrability via bounded Poisson fourth moments) give the stated TV limit since rδ→t. Evaluation at k=0 gives the completion formula; for t>2, 1/n indeed outruns r^−2 on the critical scale. Supporting files were inspected, not executed; frozen finite tests are not the basis for these deductions.

## originality

FAIL

Verified stronger prior coverage, not merely an inaccessible citation. The known exact Poisson-binomial representation of the vacancy count puts this dependent-drawing problem under the second-order Charlier–Parseval theorem of Zacharovas and Hwang. Its explicit total-variation theorem, specialized using only the second and third factorial moments, implies a finite bound stronger than the entire frozen ℓ¹ bound, with the same δ (see derivation below). The sharp TV and completion formulas then follow immediately. Goldstein–Reinert alone would not have sufficed to reach this conclusion.

## value

FAIL

The correction and its accuracy would be useful for calibrating near-complete collection, but the claimed gap is already covered by the exact known vacancy representation and a strength-dominating application of an explicit general bound. The elementary factorial-moment inversion is a valid alternative derivation, but the finding does not establish a distinct theorem or comparative proof advantage. The stated asymptotic and completion consequences do not independently survive that coverage, so no substantive repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
