# Independent mathematical audit

## correctness

PASS

For a partial identity with support S, comparison of the domains of the two compositions requires x∈S iff f(x)∈S for every x in the domain of f. This condition is sufficient, so the commuting partial bijections are independent restrictions to S and its complement. Counting rank-j partial bijections gives R_m=m!L_m^(0)(−1); cancellation against the number of choices of S gives the two coefficient factors. Their convolution is L_n^(1)(−2) by squaring the ordinary Laguerre generating function, and the empty-set case is consistent. In the Perron formula the ratio at (α,x)=(1,2) versus (0,1) has prefactor e^(−1/2)2^(−3/4)sqrt(n) and exponential factor exp(2(sqrt(2)−1)sqrt(n)); uniform sampling supplies 2^−n. At k=n/2+s with s=x n^(3/4)+O(1), 2sqrt(k)+2sqrt(n−k)=2sqrt(2n)−sqrt(2)s²/n^(3/2)+O(s⁴/n^(7/2)), and [k(n−k)]^(−1/4)=sqrt(2)n^(−1/2)(1+o(1)). The remainder and coefficient equivalents are uniform for bounded x. This yields the local prefactor 2^(1/4)/sqrt(π) and exponent −sqrt(2)x². Compact Riemann sums and the unit integral of the limiting density give tightness and weak convergence, with variance parameter 1/(2sqrt(2)). This proves the limiting law, not a moment limit inferred from numerics. The recorded exhaustive checks are for n≤4 only; the large-n variance and probability ratios are diagnostics. The script and output were inspected, not run.

## originality

FAIL

The finite count is a direct consequence of the known centralizer split and the sharp probability equivalent is a direct ratio of two Perron evaluations. The conditional local limit is also a mechanical consequence of an existing stronger local-limit theorem that applies here. Let F(z)=exp(g(z))=(1−z)^−1 exp(z/(1−z)), g_j=1+1/j for j≥1, and a_k=[z^k]F. Cantón–Fernández–Fernández–Maciá, Theorem 5.7, makes both F and F² Hayman-admissible: the coefficients of g and 2g are bounded between positive constants, so choose R=1 and β=λ=0 in (5.14). These are strongly Gaussian and their Theorem C gives uniform local Gaussian probabilities. For independent tilted sizes X_r,Y_r with Pr(X_r=k)=a_k r^k/F(r), the exact conditional law given X_r+Y_r=n is the frozen rank law, by cancellation of the tilt. The sum is the Khinchin family of F². The individual mean m(r)=r g′(r)=(1−r)^−2−1 and variance σ²(r)=r m′(r)=2r(1−r)^−3. Set m(r)=n/2, so the sum's mean is n, with variance 2σ² and σ²∼n^(3/2)/sqrt(2). The two individual local probabilities at k and n−k divided by the sum probability at n therefore give (1/(sqrt(π)σ)) exp(−(k−n/2)²/σ²)(1+o(1)) uniformly on compact scaled windows, exactly the frozen limit. This uses the prior uniform LLT for all three factors without a new asymptotic lemma. No prior word-for-word statement of the semigroup experiment was needed for this implication.

## value

FAIL

The effect of conditioning on a natural rare commutation event is interpretable, but the exact count is the standard split, the sharp probability is a direct classical coefficient ratio, and the local law follows by conditioning two instances of a covered strongly Gaussian family at their joint mean. No independently useful unknown invariant or nonmechanical structural step remains among the stated claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
