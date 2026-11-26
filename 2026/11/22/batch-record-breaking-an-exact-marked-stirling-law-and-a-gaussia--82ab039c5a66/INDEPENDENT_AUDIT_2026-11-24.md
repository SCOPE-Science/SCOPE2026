# Independent mathematical audit

## correctness

PASS

Before recovery, the gained count is exactly the within-suffix record count; at and after recovery the indicators agree. The rank of the maximum gives P(J=j)=m/[j(j−1)] and the censoring mass m/n. Permuting the pre-recovery block preserves each conditioning event, so the conditional count is the uniform-permutation Stirling count, including the empty block. The expectation is the sum of 1/(i−m)−1/i. On the infinite horizon the log-survival transform turns suffix record values into independent exponential spacings and the independent threshold into the maximum of m exponentials. Mixing the Poisson count gives the stated PGF, and coupling at recovery gives the TV bound. Geometric third absolute centered moments sum to O(log m), sufficient for Lyapunov (the word ‘summable’ in Step 4 should not be read as summable over all j). For macroscopic prefixes the survival m/floor(nt) and censoring yield the stated mark; conditional Bernoulli record counts have a uniform Berry–Esseen bound O_delta((log n)^−1/2) for lengths at least delta n, and shorter blocks have limiting probability at most delta/(alpha+delta). This proves asymptotic independence, including the mass at 1; at finite n, J=n also gives C_n=1 but its probability vanishes. The supplied permutation checker was inspected, not executed; it does not certify the limits.

## originality

PASS

The inspected single-arrival work covers more than the m=1 marginal: its stopped-run representation specifies the mark too. The frozen contribution starts at m≥2. The same conditional fixed-block count is prior, but the beta-maximum mixing, multi-arrival factorization and growing-prefix Gaussian limit with a dependent finite-horizon and asymptotically independent non-Gaussian mark are not statements of the inspected prior results. Credit is not for the Stirling or ordinary record CLT inputs.

## value

PASS

Deleting an initial block is a natural perturbation of a record process, and the time at which its effect ceases is a useful mark not provided by an unmarked law. The exact pair law distinguishes right censoring from observed recovery. In the macroscopic regime a nondegenerate censored tail survives despite Gaussian fluctuations of the count, and the leading fluctuations decouple. That structural distinction, together with the finite-to-infinite coupling in a separate regime, goes beyond recomputing the usual fixed-length Stirling count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
