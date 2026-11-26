# Independent mathematical audit

## correctness

PASS

Independently reconstructed RESULT.md Steps 1–5. K_n is binomial with mean tending to lambda; the one-count frequency divided by mu_n tends to lambda by its binomial variance bound, and the row mean differs from mu_n by o_P(1) since mu_n/n tends to zero. Writing r=mu_n u_n, the two PGF remainders in the numerator and denominator have expectations n mu_n exp(-mu_n)(exp(r)-1) and n exp(-mu_n)(exp(r)-1-r). Markov at scales mu_n and r gives A_n/mu_n → lambda and (B_n-K_n)/r → lambda in probability. Each fixed K_n=k has limiting probability bounded away from zero, so these estimates survive conditioning; at k=0, r T_n → 1, at k>0, T_n → lambda/k. Tightness of K_n proves compactified weak convergence, with the undefined all-zero event negligible. For the calibration, set G=E[u^X], H=E[u^(2X)]/G^2. Use the centered, mean-normalized versions alpha, beta, gamma of X, X u^(X-1), u^X. The Taylor bias coefficient is E[alpha^2+gamma^2+alpha gamma-alpha beta-beta gamma]; PGF differentiation gives these five moments (in order) as 1/mu, H-1, u-1, u-1+1/mu, uH-1. The variance of beta-gamma is H[(1-u)^2+1/mu], and Cov(alpha,beta-gamma)=1/mu, yielding the stated first-order delta variance. H/n → 1/lambda, also in probability under mean plug-in. For lambda=1 the acceptance interval has its lower endpoint strictly between 1/25 and 1/24 and its upper endpoint above one; the endpoints have zero limiting mass, so the K=0 and K≥25 events give the stated exact limiting size. The on-disk checker was inspected, not run; the limit rests on the analytical argument.

## originality

PASS

Best-of-knowledge pass for the published-statistic-specific reciprocal-Poisson law, the no-zero scaling, and the resulting exact Gaussian size failure; not for the test, the delta coefficients, or rare binomial-to-Poisson convergence.

## value

PASS

The critical zero frequency is a natural boundary of the denominator, not an arbitrary numerical slice. An explicit escape atom and exact 36.79% null size identify the mechanism and a sharp failure of a real calibration rule while leaving its fixed-parameter domain intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
