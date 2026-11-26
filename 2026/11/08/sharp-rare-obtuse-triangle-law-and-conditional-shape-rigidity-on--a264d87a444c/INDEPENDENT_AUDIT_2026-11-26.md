# Independent mathematical audit

## correctness

PASS

For an obtuse angle at X, put T=X·Y, S=(1−T)/2, u=(Y−X)/||Y−X|| and V=u·Z. The event is V<−√S. Given X,Y, V has the fixed coordinate law, so S is Beta(k,k) and U=V² is independently Beta(1/2,k), k=(d−1)/2, with independent fair sign of V. Thus p_d=(3/2)Pr(U>S), since the three vertex events are disjoint up to nulls. At d=3 this is (3/2)E[U]=1/2; at d=5 it is (3/2)E[3U²−2U³]=17/70. In the t-coordinate let m=(d−3)/2. Integration by parts gives the cap endpoint term (1−s²)^(m+1)/[2(m+1)s], s=√((1−t)/2), an upper bound globally and relative error O(1/m) on fixed compacts about t=1/3. Multiplying by (1−t²)^m leaves phase F=(1−t)(1+t)²/2 and amplitude (1+t)/√(2(1−t)), integrable at both ends. The unique global maximum is F(1/3)=16/27, log curvature −27/8. The complement of a fixed neighborhood is exponentially smaller; the smooth interior Gaussian expansion has relative error O(1/m). Combining its √(2π/[m·27/8]) factor, the amplitude 2√3/3, 3c_d²/(d−1)=3/(2π)(1+O(d⁻¹)), and F^m=F^(d/2)F^(−3/2) gives the stated prefactor. The same localization gives variance 2/(27/8)=16/27 on the √d scale. In the conditional cap V+√S tends to zero by the one-sided cap ratio, and the orthogonal component along X+Y tends to zero by its conditional second moment ≤1/(d−1). This yields the three dot products and squared sides in the claimed order; conditioning on any obtuse vertex needs relabeling. The checker was inspected, not executed; the beta identities are independent finite checks, and the proof, not the sample grid, gives the limits.

## originality

PASS

The same sphere-surface exact cap integral is prior work. The supported distinct claims are the sharp high-dimensional equivalent with relative error, the atypical conditional shape, and the distinguished-coordinate CLT. These should not be presented as discovering the cap law, the Gram density, or ordinary Laplace asymptotics.

## value

PASS

A single high-dimensional chord triangle is a natural shape model. The exact prefactor quantifies a rare deviation for which a typical-pair calculation even misses the exponential rate. The conditional right-isosceles limit and scale of a distinguished side explain the geometry of the deviation, beyond evaluating an already known finite integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
