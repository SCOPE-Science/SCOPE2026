# Independent mathematical audit

## correctness

PASS

The sum of incidence segments is the image of a cube, so is exactly the convex hull of its endpoint-selection degree vectors. The support-function widths add; division by binom(n,k)*sqrt(k) gives the absolute averages of unit Gaussian sums. For two k-sets, correlation is J/k with the stated hypergeometric overlap; direct absolute-normal covariance gives C and hence the exact second moment formula. In Gaussian L^2 the degree-two coefficient of |z|-mu is E[|Z|(Z^2-1)]/2=mu/2. The residual has only even degrees at least four, so its averaged squared norm is at most (1-2/pi) E[(J/k)^4]. Counting ordered marked overlap labels gives E[(J)_r]=(k)_r^2/(n)_r; the four fourth-moment terms yield O(1/(nk^2)+1/n^2+k^2/n^3+k^4/n^4), little-o of 1/n+k^2/n^2 for growing sublinear k. Expansion of subset squares gives inclusion weights k/n on diagonals and k(k-1)/(n(n-1)) on off-diagonals before division by k. In particular the averaged degree-two term equals (n-k)/(n-1)*(Q_{n-1}-(n-1))/n + (k/n)*(X_n^2-1), where Q and the standard normal X_n are exactly independent by orthogonal Gaussian decomposition. The chi-square CLT and the residual bound now give both scalings and constants; the third cumulant proves nonnormality for positive finite c. For proportional rank, conditioning on X_n yields exactly f_{k/n}(X_n). Its variance is C(k/n) by sharing X_n across two conditional copies, and Var(H) minus that variance tends to zero because J/k concentrates at k/n. Thus the limit is a random conditional folded-normal mean, not a folded-normal draw, with f_1(X)=|X|. Finally fixed k uses the first Hoeffding projection, variance C(1/k)>0 by sharing one coordinate, giving k^2 C(1/k) including k=1. Gaussian directions are not rescaled to the sphere. The supplied finite rational and sampling checker was inspected, not executed; the limit proof does not rely on it.

## originality

PASS

Liu's rank-k degree-sequence zonotope is exactly the same body, and the Gaussian absolute covariance and fixed-order CLT are classical. The distinct finding is the variable-rank stochastic width law, especially the independent Gaussian plus centered chi-square at k on the order of sqrt(n), with the supercritical and proportional-rank reductions. The strongest indexed analogues mix Gaussian and non-Gaussian effects in different geometries and use different generators, growth regimes or direction normalizations. The inspected growing-order U-statistic Gaussian approximation gives a quantitative first-projection regime, not the mixed limit. No exact or stronger statement covering this crossover was found in the checked material.

## value

PASS

A known, natural family of polytopes provides a quantitative example where a width's second Gaussian chaos undergoes a change in the source of its fluctuations as hyperedge rank grows. The critical law identifies how an independent sample-energy Gaussian and a one-dimensional centered chi-square coexist; neither the one-coordinate mean, the fixed-rank CLT nor a variance estimate reveals that distribution. The proportional-rank conditional law is an additional exact explanation of nonconcentration for these polytopes. The value is the new rank-scale description, not a redefinition of the body or a general inference theorem for arbitrary kernels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
