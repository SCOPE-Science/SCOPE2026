# Independent mathematical audit

## correctness

PASS

There are V_i V_j eligible cross edges with rate 1/n each. For X_n=V/n this gives density rates n x_i x_j and increments −(e_i+e_j)/n, with fluid solution u(t)1, u=(1+2t)^{-1}. The scaled martingale has jumps O(n^{-1/2}) and its bracket converges uniformly on bounded intervals to the integral of B(u1). To check the needed moment bound, its optional squared-jump sum is at most 2/n times the total attempt count, a Poisson variable of mean 3nT; this bounds the second moment of the optional quadratic variation. The martingale maximal inequality and Lipschitz Gronwall bound then give bounded fourth moments of the fluctuation supremum. Thus drift Taylor remainders vanish in the path CLT and fluctuation products are uniformly integrable, which is necessary for the actual covariance limit. The linear drift and bracket matrices are −u(I+11ᵀ) and u²(I+11ᵀ); integrating the common and contrast variance equations gives 2(u−u⁴)/3 and u log(1+2t)/2, with zero initial data. Their difference divided by three is the cross-part covariance. Its numerator H(y)=4(1−y^{-3})−3 log y, y=1+2t, starts at zero, increases to y=4^{1/3}, then decreases to −∞. Independent replay: python /workspace/independent_checks.py (adsorption routine) obtains 1.347345267068252110 from the principal Lambert W root in z=y^{-3}, the other real branch giving t=0. This is a fixed-finite-time limiting transition; moment convergence establishes matching finite-n signs at each fixed interior nonzero point, not a universal finite-size transition or a jamming statement. Read the submitted notes and both checkers without executing them.

## originality

PASS

The kinetic skeleton and density-dependent framework are prior work. The earlier 7/8 record has the same physical-time jump model and fluid equations but expressly does not prove a fluctuation theorem. Exact-match searches and passage comparisons identified no distinct source giving the stated common and contrast covariances and their sign classification for the balanced dense irreversible process. Same-day equilibrium covariance results use materially different probability laws.

## value

PASS

The result gives a structural difference between total vacancy fluctuations and class-imbalance fluctuations, leading to an exact sign reversal under the same irreversible deposition law. Neither the known fluid law nor terminal matching efficiency can predict this transient covariance. The sign classification also predicts signs of large finite systems at fixed times away from the zeros without overclaiming a universal finite-size threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
