# Independent mathematical audit

## correctness

PASS

The upper orthant volume given a center is the product of its complementary coordinates. Therefore the conditional degree is Bin(n-1,Z), and Y=-log Z is Gamma(d_n,1). At L=log n, the density ratio at L+s tends to exp((c-1)s); the degree tail tends to the Poisson tail at lambda=exp(-s). Extend by zero on s<=-L. A fixed epsilon smaller than both c-1 and r+1-c gives domination by exp((c-1-epsilon)s) for s<0 and exp(-(r+1-c-epsilon)s)/r! for s>0, using the binomial factorial moment. For the constant, express the Poisson tail as the integral of exp(-u)u^(r-1)/Gamma(r) over 0<u<lambda and integrate lambda^(-c) first over lambda>=u; this gives Gamma(r+1-c)/[(c-1)Gamma(r)]. To pass from the mean count to existence, restrict centers to |Y-L|<=K. The number of eligible centers, before requiring any degree event, is binomial with expectation O_K(n f_d(L)), where Stirling gives n f_d(L)=n^[c(1-log c)+o(1)]=o(1). The difference between the restricted mean and restricted existence probability is at most the expected number of pairs of eligible centers, O_K((n f_d(L))^2), regardless of degrees sharing leaves. The complement costs at most its expected qualifying count, made arbitrarily small relative to n f_d(L) by the same integrable envelope after n tends to infinity. The exact factor n f_d(L)=L^(d_n-1)/Gamma(d_n) retains all second-order dimension effects. For the star mean, the center must be the coordinate minimum in each independent coordinate, with probability (r+1)^(-d_n). Its mean diverges throughout the stated strict split interval, with nonemptiness from x/log x>e for x=r+1>=3. The proof's minimum statement for x/log x is understood on x>1; the application is on x>=3. No probability limit at c=e or c=r+1, star-mean limit at the split's upper endpoint without further assumptions, or moving-r assertion is established. The frozen script checks finite rank expectations, a binomial polynomial identity and integrals, not the rare-event reduction; it was inspected, not run.

## originality

PASS

Best-of-knowledge pass for the directed degree rare-event relative equivalent and the quantitative distinction between the star mean and its existence probability. The threshold for fixed degrees and the exact elementary star expectation are not the distinct contribution. The classical 1995 full text remained inaccessible after bounded lawful attempts; priority beyond its described threshold is unresolved, not presumed in either direction.

## value

PASS

This answers a natural rare-maximum question for a standard random partial order with relative, not just logarithmic, accuracy and without a second-order dimension assumption. The split interval gives a precise warning that a diverging expected star count need not predict any star in a typical order. The proof resolves a dependence issue rather than applying an unjustified independent rare-star approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
