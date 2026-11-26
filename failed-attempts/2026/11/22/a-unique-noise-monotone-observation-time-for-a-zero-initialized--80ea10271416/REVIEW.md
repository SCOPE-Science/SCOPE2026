# Independent mathematical audit

## correctness

PASS

For the stated known-parameter zero-start Gaussian process, conditioning gives an integrated risk reduction J=G/(q+η), with q=Var(X_t) and G=∫Cov(X_s,X_t)²ds. Splitting the covariance integral at t recovers the displayed G. Its derivative has the sign of F_a; F_a(0)=0, its derivative has one switch at 1/2, and F_a(1)=2e^{2a}(2a−sinh(2a))<0. Thus G increases up to T_a and decreases thereafter. Differentiating G'/q' yields the asserted one-switch identity (q'=e^{−2at}). The response E=Gq'/G'−q falls before 1/2, rises on (1/2,T_a), behaves as −t/2 near zero, and diverges at T_a; J' has the sign of η−E before T_a and is negative after it. This proves uniqueness and strict noise ordering. Put z=1/η in G'(t)(1+zq(t))−zG(t)q'(t)=0: the t derivative at (T_a,0) is G''(T_a)<0, giving the stated leading displacement with an O_a(z²) remainder. Uniform covariance convergence at fixed η>0 reduces the Brownian design to t²(1−2t/3)/(t+η) with a single interior maximum and the displayed quadratic root. The high-noise root also obeys 2a(T_a−1)+log(sinh(2aT_a)/(2aT_a))=0; expansion gives 1−a/3+O(a²). The support files were inspected, not executed; these are analytic checks. No claim of noise or rate uniformity is inferred.

## originality

FAIL

The main observation-time theorem is covered by a distinct indexed result on quadratic-energy estimation for the identical process, measurement and parameters. Its gain is exactly 2J², so it has the identical argmax for all parameters, including the same characterization, uniqueness, strict increase, high-noise root and Brownian limit. The added first-order coefficient and small-a root expansion are direct local expansions of known equations, not a materially distinct design theorem. This is demonstrable mathematical coverage, not an inference of chronological priority from the same date.

## value

FAIL

Choosing a single noisy measurement time for trajectory reconstruction is a meaningful design problem, but the submitted contribution supplies no materially new design decision beyond the exactly equivalent energy-design optimizer. The risk function change is a Gaussian conditioning exercise for this shared ratio, and the two new local expansion terms follow directly from its explicit limiting equation and a simple root. The record offers no additional regime or comparison giving those expansions independent substantive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
