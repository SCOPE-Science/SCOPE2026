# Independent mathematical audit

## correctness

PASS

In the uniform Prüfer word of length n−2, a leaf is a missing letter, and odd degree means an even letter count. For distinct i,j one word position contributes 0 on i, −1 on j and 1 otherwise to the joint missing-letter/sign moment, giving w_n. The marginal missing and parity moments are u_n and v_n, so the off-diagonal covariance is (w_n−u_nv_n)/2 and the diagonal is u_n(1−v_n)/2. Summing gives the total. The off-diagonal sign follows from the strict base comparison for n≥3; the same-vertex sign is positive in that same range, and both signs degenerate at n=2. The total vanishes at n=2,3. For n≥4 strict convexity of x↦x^(n−2) on [0,1] gives 1+(n−1)b^(n−2)>n[(1+(n−1)b)/n]^(n−2) for b=(n−3)/(n−1); this is exactly the total sign inequality. Two-letter missing and parity transforms give v_n and z_n and hence the reported variances. Nondegeneracy follows from stars and paths, and the first-order expansion in 1/n gives the stated two variance limits and covariance limit, hence the Pearson limit. This is about uniform labeled Cayley trees. The frozen verifier was inspected, not executed; a separate exact check via acyclic labeled edge sets at n=2..6 reproduced the moments and diagonal/off-diagonal covariances (python /workspace/branches/independent_checks.py 1).

## originality

FAIL

The earlier Resultary finding 841548d3e0e4 states the exact mixed generating function for the total leaf count and a fixed vertex's Prüfer count. Substituting z=−1 and using exchangeability gives the exact aggregate covariance, and its Eq. (13) at z=−1 gives the local covariance. The strict sign contrast is then a direct finite corollary: the off-diagonal sign is a base comparison and the total sign is the strict power-mean inequality for two bases (see claim_vs_prior_implication). No new structural sign argument beyond this implication is required. The n=2,3 cases and Pearson limit add routine degenerate cases and marginal-moment evaluations, not a distinct surviving claim. This is mathematical coverage, not a claim about derivation history.

## value

FAIL

Comparing local and total dependence for canonical tree counts is a meaningful question, but the exact contrast here is a single parity specialization and strict convexity comparison of the existing generating formula. The additional decimals and degenerate small cases do not supply a separate useful exact result beyond that direct implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
