# Scientific assessment: two-corner RPS extreme-tail law

## Correctness — PASS

The claim is restricted to fixed \(n\ge2\) and an exactly specified continuous null, so the endpoint spacings are uniformly Dirichlet. The paper reconstructs the published normalized recursive statistic as Pascal-weighted linear forms divided by positive normalizers. The normalizers are bounded uniformly over the simplex. Ordering all coordinates gives an explicit sector Jacobian, and an exact count of consecutive intervals in vanishing coordinate sets shows the unique sharp moment exponent \(2/(n+1)\). Only the two endpoint vertices attain it. Conditioning on the total mass outside one endpoint produces an independent uniform Dirichlet angular vector; dominated convergence gives the **full** leading tail coefficient, not merely its exponent. The reflected endpoint supplies the second identical term, while the rest has a strictly stronger exponential moment.

Independent numerical checks passed 4912 finite assertions for the Pascal identities, reversal symmetry, exact uniform minimum, interval counts and corner expansions. Separate two-corner quadrature for three spacings approaches the explicit beta constant. These checks corroborate but do not replace the general-dimensional analytic proof. No unproved finite enumeration is used to establish an infinite statement.

## Originality — PASS (qualified historical priority)

The original Eller–Shtembari preprint (arXiv:2111.02252, sections 2–3) defines the statistic, computes the one-observation exact CDF, and numerically parametrizes the CDF for larger samples. The known one-observation result is excluded from the novelty claim. The inspected sections do not supply the \(n\ge2\) exact extreme-tail prefactor or the two endpoint mechanisms.

Kosta–Windisch (arXiv:2411.13392, sections 4–5) provide general real-log-canonical thresholds and multiplicities for products of linear forms. Their framework can account for power exponents once the recursive product is suitably encoded, and is acknowledged as broader prior theory. It does not give this named statistic's concrete two-corner Dirichlet integral or explicit \(n=2\) beta prefactor. The 2022 Shtembari–Caldwell paper (arXiv:2211.03478) invokes RPS within multivariate procedures but its inspected construction does not yield the stated univariate tail coefficient. Searches of relevant published mathematical research records and earlier accessible ledger claims did not disclose an implication covering the complete coefficient statement; absence of a match is not proof of priority.

The complete text of a related 2023 doctoral thesis was not obtained, so it remains a genuine residual historical-coverage risk. General singular-integral machinery may supply a different route to the tail exponent and some qualitative asymptotics, but the specific prefactor is independently derived here.

## Value — PASS

The original test was calibrated by extensive simulations and smooth CDF interpolation down to approximately \(10^{-7}\). An exact positive fixed-sample far-tail coefficient and its essential-exponential form after bounded normalization are motivated, nontrivial calibration benchmarks outside that numerical regime. The extremal event geometry is informative: the far null tail is dominated by all observed points clustering next to either interval endpoint, rather than by arbitrary interior clusters. The exact exponential-moment threshold quantifies how raw-score tails deteriorate with increasing sample size.

## Limitations and closest literature

The law is pointwise for each fixed sample size and asymptotically extreme thresholds. It has no uniform-in-sample-size remainder, no exact finite-threshold quantile, no composite-null parameter-fitting statement, and no power guarantee. The leading coefficient is an explicit angular Dirichlet integral for general sample size, with a closed beta form for two observations. The closest scientific sources are Eller–Shtembari (2021), Kosta–Windisch (2024), and Shtembari–Caldwell (2022); the cited 2023 thesis remains uninspected.

Self-review: passed. Independent audit: not yet performed.
