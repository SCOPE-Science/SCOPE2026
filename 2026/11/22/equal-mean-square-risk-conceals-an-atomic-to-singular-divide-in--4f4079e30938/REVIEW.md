# Independent mathematical audit

## correctness

PASS

For q=1−η, each batch sends x to qx+ηZ and the epoch multiplier is q^m. Given a frozen partition, the randomly ordered batch means sum to zero and have exchangeable covariance v_P on the diagonal and −v_P/(m−1) off it. Thus weighted epoch noise has conditional mean zero and variance η²v_PΓ_m(q); sampling without replacement gives E[v_P]=s²(n−b)/(b(n−1)) via the one- and two-label inclusion probabilities. Conditional zero means eliminate frozen cross-epoch covariances, even though unconditional independence can fail. The fresh process has the same marginal noise variance with independent epochs. Summing the weighted variances proves the stated all-horizon identity, also for q<0 and q=0 (empty sum at epoch zero). For (1,1,−1,−1), two of three pair partitions have zero noise; the third gives equiprobable ±η². Contraction yields the annealed fixed-partition mixture and the fresh iid three-digit series, with the stated variance and objective gap. The aligned sign component cannot reach zero for r≤1/3 by first-digit dominance. The fresh support images have gaps δ(1−3r)/(1−r) for r<1/3. Separation compares ball masses with cylinders at levels differing by bounded offsets, so the strong law gives the asserted local dimension; using equal weights gives the support dimension. At r=1/3 the intervals tile and the biased ternary digit frequencies give a Lebesgue-null set of full measure. For the local dimension there, consecutive depth-k ternary intervals have probability ratio 4 or 1/4: carries exchange trailing 2s with 0s of equal weight. Balls at radius 3^−k have mass comparable to the containing cylinder. A point has at most two addresses, proving no atoms. The bounded series permits cumulant addition, with digit κ4=0 and κ6=−2/9. The η=1 discrete exception is correctly excluded from continuous-law claims. Uniqueness in the frozen case is conditional on a partition, with its uniform marginal prescribed for the annealed mixture. The source's 'independent positions' in the without-replacement calculation means distinct labels; the displayed probabilities and proof do not assume independent inclusions. RESULT.md lines 54–111 and the bounded checks described in VERIFICATION.md and verify.py were inspected; the uploaded script was not executed and its finite tests cannot prove the law or priority.

## originality

PASS

To the best of the examined evidence, the distinct contribution is the comparison of these partition policies on the same scalar finite sum: equal all-epoch unconditional moments and a minimal explicit atomic versus singular-continuous example, including a full-support critical law with Gaussian fourth moment. Sampling variance, contraction, and biased ternary dimension themselves are known. Neither shuffle-once nor a known unbatched recursion gives this policy comparison. No priority is inferred from same-day dates or an exact self-hit.

## value

PASS

This is a minimal controlled test of two natural implementations of minibatch reshuffling. The same observable objective risk at every horizon conceals a stationary point mass at the optimum under one implementation and a continuous singular law under the other. Full interval support and Gaussian fourth moment still do not diagnose the fresh law at the exact touching threshold. Four labels are the least allowing at least two batches of size at least two. This is a benchmark about what moment analyses miss, not a claim of general convergence-rate dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
