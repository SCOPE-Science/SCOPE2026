# Independent mathematical audit

## correctness

PASS

On symmetric second moments the update is Φ(C)=TCTᵀ+hσ²C₁₁e_me_mᵀ. Rank-one initial matrices span the symmetric space, so decay for every deterministic input is equivalent to spectral radius below one. For h≥2 Jensen on the mean with initial state e₁ rules out decay. For 0<h<2 the unforced spectral radius is (1−h)². The resolvent feedback series for real λ above this radius is strictly decreasing from infinity to zero; at h=1 it is a single nonzero inverse-power term. The unique feedback root is an eigenvalue and no larger modulus can satisfy the feedback equation, since the absolute value of the complex series is bounded by the positive series at its modulus. The response coefficient is binom(k,n)(1−h)^(k−n)(κh)^n for k≥n. Euler's identity for the binomial-square series and 1−(1−h)²=h(2−h) give the stated gain at λ=1 and show that equality is not asymptotically stable. For continuous time the rank-one resolvent feedback is G binom(2n,n)/(s+2)^(2n+1) in Re(s)>−2, so its positive-real-axis-side root s=−2+[G binom(2n,n)]^(1/(2n+1)) has maximal real part. With r=1−h, on r≤0 the numerator (1+r)^(2n+1) increases and P_n(r²) decreases. For r>0 the denominator after factoring (1+r)^(2n) is a binomial collision probability whose Fourier integral strictly decreases as r/(1+r) increases. These pieces join continuously and yield strict monotonicity on the whole interval, the stated endpoint limits, and precisely one crossing when G<G_c,n.

## originality

PASS

General covariance spectral criteria and step nesting do not supply the exact family-specific polynomial. The closest accessible paper includes overlapping continuous two- and three-dimensional lateral-noise models, and the 2012 nonnormal numerical article may well cover the two-dimensional member. The inspected comparisons do not give the exact all-length discrete law for a single closing noise. No novelty is assigned to an isolated two-dimensional case or to no reentry alone.

## value

PASS

This is a natural feedback family: a nonnormal deterministic shift transfers the noise injection back to its sensing coordinate, and mean stability can coexist with mean-square numerical instability. The result replaces a dimension-growing covariance spectral test with an explicit one-parameter polynomial threshold that decides every step for any chain length, and supplies the exact continuous/discrete comparison. General Lyapunov step nesting is useful background but is not itself the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
