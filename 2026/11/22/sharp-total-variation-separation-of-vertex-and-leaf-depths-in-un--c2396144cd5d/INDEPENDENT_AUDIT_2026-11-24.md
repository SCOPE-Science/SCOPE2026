# Independent mathematical audit

## correctness

PASS

For label j≥2 the future event of remaining a leaf is independent of its depth and has probability (j−1)/(n−1). Multiplication by the label-depth pgf z H_{j−1}/(j−1) and normalization by E L_n=n/2 gives the size-biased leaf pgf. The identity mH_{m+1}−(m−1)H_m=(1+z)H_m telescopes to the stated shifted Bernoulli sum. The vertex law includes the independent Bernoulli(1/2) term; the total variation to the size-biased leaf law is one quarter of the sum of absolute successive atom differences, which unimodality makes twice the maximum atom before multiplication by one quarter. For ordinary trees the conditional leaf increment is Bernoulli(1−L_n/n), so total variance gives the recurrence (1−2/n)Var(L_n)+1/4, with Var(L_2)=0 and Var(L_n)=n/12 for n≥3. Sampling leaves via the same kernel contracts the TV of tree laws, bounded by E|2L_n/n−1|/2; the reverse triangle inequality gives exactly the claimed error, not equality for ordinary sampling. The Fourier local limit follows from the variance proxy v_n, the modulus bound and centered Bernoulli third absolute moments at most p(1−p); after rescaling t by 1/√v_n the modulus is dominated by an integrable Gaussian, and the bound is uniform in the atom because the Fourier phase has unit modulus. A nearest integer to the mean attains the asymptotic mode height; v_n=log n+O(1). The frozen checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the annealed ordinary-leaf TV bound and sharp leading constant, with an exact size-biased proxy. The confirmed adjacent catalogue claims concern different statistics or laws. Individual profile or tree-wise mean results cannot be credited as an annealed TV comparison. The relevant primary passages were not retrieved, so priority remains conditional on the available evidence.

## value

PASS

The two natural annealed laws have the same broad Gaussian scale but remain distinguishable in TV at an explicit leading rate. The exact leaf-size-biased proxy explains the nonzero separation and quantifies the effect of the sampling design. This answers a distribution-level question that a mean gap or an individual depth CLT does not resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
