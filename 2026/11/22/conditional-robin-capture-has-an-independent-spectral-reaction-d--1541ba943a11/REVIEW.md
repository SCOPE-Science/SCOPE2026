# Independent mathematical audit

## correctness

PASS

With diffusivity D and radiation coefficient kappa, solving DG_s''=sG_s with G_s(L)=0 and DG_s'(0)=kappa(G_s(0)-1) gives the displayed numerator and denominator, including G_0=kappa(L-x)/(D+kappa L). The normalized transform factors into the absorbing first-hit transform conditioned on hitting 0 first and the x-independent boundary-delay transform. Put a=kappa+D/L and phi(s)=Dq coth(qL)-D/L, q=sqrt(s/D). The coth partial fractions give a Lévy density (2D/L) sum_n nu_n exp(-nu_n t); its truncated first moment is finite by sum 1/nu_n<infinity, and its total mass is infinite. Thus the delay law is S_H for an independent rate-a exponential H. Each deterministic positive-length increment is almost surely positive (its atom at zero is lim_{s→infinity} exp(-h phi(s))=0), and a countable rational-interval argument proves a.s. strict increase of S. Sharing a uniform for H and sharing S and the independent conditioned first hit proves strict reactivity ordering. For the spectral construction, the zeros of the even denominator correspond to the positive simple eigenvalues of the Robin–Dirichlet Sturm–Liouville problem; the Robin quadratic form has the nonnegative boundary term eta |f(0)|^2. The denominator regarded as an entire function of z^2 has order at most 1/2, so the normalized product has no extra exponential. The paired eigenvalue factors are exactly Bernoulli/exponential transforms; p_n<1/n and rho_n>D pi^2 n^2/(4L^2) give summable means and the uniform N^(-2) bound. The weak-reactivity limit uses the rate D/L, still strictly positive. Finally log(sinh z/z)=z^2/6-z^4/180+O(z^6) gives the first-hit moments, while phi(s)=Ls/3-L^3 s^2/(45D)+O(s^3) in log[a/(a+phi)] gives the stated delay moments. Independent addition gives the total mean and variance.

## originality

PASS

The same-model boundary problem and hence the conditional Laplace transform under constant diffusivity and zero drift are already implicit in Wu. The existence of a position-independent continuation law is also a strong Markov consequence at the first hit of the reactive endpoint; do not credit factorization alone. The supported distinct contribution is the explicit spectral law of this successful boundary continuation together with its uniform certified truncation and strict cross-reactivity coupling under competing escape. The closest checked local result has a genuinely similar independent Bernoulli/exponential delay but different interruption/reset dynamics. General local-time and hitting-time spectral tools are prior; no inspected theorem gives this complete conditioned law and its two quantitative/ordering consequences. The inaccessible continuous Kent sources leave a specific risk for the spectral part, not a basis for a verdict about their coverage.

## value

PASS

For this natural competing-outcome model, the explicit independent sum makes the entire conditioned boundary delay usable, rather than giving only its mean or defining it by a boundary-value problem. The uniform N^(-2) Wasserstein guarantee gives a certified finite approximation independent of reactivity, and the common increasing-process representation proves strict ordering even though conditioning selects different rare outcomes at different reactivities. Together those are meaningful distributional and approximation results beyond the prior BVP or the routine first-hit split.

The dated certificate retains the supplied scientific assessment, sources and limitations.
