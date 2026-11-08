# Strict anticorrelation of nearest and farthest squared vertex distances in every regular simplex

## Finding
Let \(n\ge2\) be any integer and let \(X=(X_1,\ldots,X_n)\) be chosen uniformly (with respect to intrinsic volume) from the regular simplex
\[\Delta_{n-1}=\operatorname{conv}\{e_1,\ldots,e_n\}\subset\mathbb R^n.\]
Define the squared distances to its nearest and farthest vertices by
\[R_n=\min_i\|X-e_i\|_2^2,\qquad T_n=\max_i\|X-e_i\|_2^2.\]
Write \(H_n=\sum_{j=1}^n j^{-1}\) and \(J_n=\sum_{j=1}^n j^{-2}\). Then their **exact covariance**, for every \(n\ge2\), is
\[
\boxed{\operatorname{Cov}(R_n,T_n)=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)}-\frac{2(H_n^2+J_n-2H_n)}{n(n+1)(n+2)}+\frac{4(n-1)}{n^3(n+1)(n+2)}+\frac{4(1-H_n)}{n^3(n+1)}<0.}
\]
Moreover,
\[\operatorname{Cov}(R_n,T_n)\sim-\frac{2(\log n)^2}{n^3},\qquad
\operatorname{Corr}(R_n,T_n)\sim-\frac{\sqrt{3/2}}{\pi}\frac{(\log n)^2}{\sqrt n}.\]
Thus the two squared vertex-distance extrema have strictly **negative** covariance in every dimension, though their correlation tends to zero. The exact mean identities are
\[\mathbb ER_n=1+\frac2{n+1}-\frac{2H_n}{n},\qquad
\mathbb ET_n=1+\frac2{n+1}-\frac2{n^2}.\]

## Assumptions and scope
The coordinates refer to the standard unit-vector simplex with edge length \(\sqrt2\), and \(X\) is uniform on its intrinsic \((n-1)\)-dimensional volume. Every regular simplex of the same edge length is congruent to this one; rescaling to edge length \(\ell>0\) multiplies both squared distances by \(\ell^2/2\), the covariance by \(\ell^4/4\), and leaves the correlation unchanged. No large-dimension approximation is used to establish strict negativity.

## Proof
Set \(Q=\sum_i X_i^2\), \(M=\max_iX_i\), and \(m=\min_iX_i\). The exact Euclidean distance identity gives \(R_n=1+Q-2M\) and \(T_n=1+Q-2m\). Since \(X\) is Dirichlet with all parameters equal to one, its mixed monomial moments are
\[\mathbb E\prod_i X_i^{a_i}=\frac{(n-1)!\prod_i a_i!}{(n+\sum_i a_i-1)!}\]
for nonnegative integer exponents. In particular,
\[\mathbb EQ=\frac2{n+1},\quad
\operatorname{Var}Q=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)}.\]

A standard simplex-volume argument gives \(\Pr(m>t)=(1-nt)^{n-1}\) for \(0\le t\le1/n\). Conditional on \(m>t\), the shifted and rescaled vector \((X_i-t)/(1-nt)\) is again uniform on the simplex. Consequently,
\[
\mathbb E[Q\mathbf1_{\{m>t\}}]=(1-nt)^{n-1}\left(nt^2+2t(1-nt)+\frac{2(1-nt)^2}{n+1}\right).
\]
Integrating in \(t\), using the beta integral, and subtracting \((\mathbb EQ)(\mathbb Em)\) yields
\[\operatorname{Cov}(Q,m)=\frac{2(1-n)}{n^3(n+1)(n+2)}.\]
The minimum has \(\mathbb Em=1/n^2\) and \(\operatorname{Var}(m)=(n-1)/(n^4(n+1))\). Conditional on \(m=t\), one coordinate is equal to \(t\); after deleting it, the remaining coordinates are \(t+(1-nt)\) times a uniform \((n-2)\)-simplex point. The maximum of \(n-1\) uniform Dirichlet coordinates has expectation \(H_{n-1}/(n-1)\), hence
\[\mathbb E[M\mid m=t]=t+(1-nt)\frac{H_{n-1}}{n-1}.\]
Integration now gives
\[\operatorname{Cov}(M,m)=\frac{1-H_n}{n^3(n+1)}<0.\]

For \(\operatorname{Cov}(Q,M)\), write \(M=\int_0^1\mathbf1_{\{M>t\}}\,dt\) and apply inclusion-exclusion to \(\{M>t\}\). If a prescribed set of \(k\) coordinates exceed \(t\), where \(0\le t\le1/k\), its probability is \((1-kt)^{n-1}\), and conditional on it the expected quadratic norm is
\[kt^2+\frac{2kt(1-kt)}{n}+\frac{2(1-kt)^2}{n+1}.\]
Integrating the resulting polynomial and using
\[\sum_{k=1}^n(-1)^{k+1}\binom nk\frac1k=H_n,\qquad
\sum_{k=1}^n(-1)^{k+1}\binom nk\frac1{k^2}=\frac{H_n^2+J_n}{2},\]
we obtain
\[\operatorname{Cov}(Q,M)=\frac{H_n^2+J_n-2H_n}{n(n+1)(n+2)}.\]
Combining these four exact quantities in
\[\operatorname{Cov}(R_n,T_n)=\operatorname{Var}(Q)-2\operatorname{Cov}(Q,M)-2\operatorname{Cov}(Q,m)+4\operatorname{Cov}(M,m)\]
proves the asserted formula.

**Strict sign for all dimensions.** For \(n\ge7\), the harmonic sums satisfy
\[H_n^2+J_n-2H_n\ge(H_n-1)^2\ge(H_7-1)^2>2+\frac27\ge\frac{2n(n-1)}{(n+1)(n+3)}+\frac{2(n-1)}{n^2}.\]
On multiplying by \(2/[n(n+1)(n+2)]\), the final bound says that \(2\operatorname{Cov}(Q,M)\) strictly exceeds the sum \(\operatorname{Var}Q-2\operatorname{Cov}(Q,m)\). Since \(\operatorname{Cov}(M,m)<0\), the target covariance is strictly negative. For \(n=2,3,4,5,6\), direct substitution gives, respectively,
\[-\frac{11}{180},\quad-\frac{14}{405},\quad-\frac{6799}{302400},\quad-\frac{15083}{945000},\quad-\frac{25303}{2116800},\]
which are all strictly negative. This settles every integer \(n\ge2\).

**Asymptotic rate.** The classical harmonic estimates \(H_n=\log n+\gamma+O(n^{-1})\) and \(J_n=\pi^2/6+O(n^{-1})\) give
\[\operatorname{Cov}(R_n,T_n)=-\frac{2(\log n)^2}{n^3}(1+o(1)).\]
The exact standard simplex-spacing formulas
\[\operatorname{Var}(M)=\frac{nJ_n-H_n^2}{n^2(n+1)},\qquad \operatorname{Var}(m)=\frac{n-1}{n^4(n+1)}\]
imply \(\operatorname{Var}(R_n)\sim2\pi^2/(3n^2)\) and \(\operatorname{Var}(T_n)\sim4/n^3\). Dividing the covariance by their geometric-mean standard deviation yields the correlation asymptotic.

## Verification
The accompanying file `verify.py` checks the five finite sign cases with exact rational fractions, verifies the inclusion-exclusion evaluation of \(\mathbb E[QM]\) by a separate finite beta-integral sum through thirteen coordinates, verifies the global sign inequality for additional dimensions, and reconstructs Euclidean nearest/farthest squared-distance covariance independently from seeded Dirichlet samples. It reports `SIMPLEX_NEAREST_FARTHEST_COVARIANCE_CHECKS_PASSED`. The all-dimensional sign follows from the displayed analytic inequality, not from the finite computations.

## Relationship to prior work
Baci, Kabluchko, Prochno, Sonnleitner and Thäle (2020) develop central and extreme-value limit theorems for uniformly distributed points in high-dimensional simplices, including the normalized exponential representation and related quadratic and maximum-coordinate limit laws. Holst (1979) develops central limit theory for sums of random spacings, and Hall (1984) proves broader spacing-sum limit theorems. These established representations and marginal asymptotics are not the result claimed here. The claim is the exact *finite-dimensional mixed covariance* between squared distances to nearest and farthest vertices, the strict sign in every dimension, and its first nonzero logarithmic asymptotic. A general asymptotic-independence theorem alone does not determine this finite-dimensional sign or leading covariance rate.

## Limitations
The distribution is uniform and the simplex is regular. The assertion concerns **squared Euclidean distances**, not the unsquared distances, and is not claimed for arbitrary Dirichlet parameters or irregular simplices. Independence is not claimed at finite \(n\). The analysis is mathematical, but a complete historical-priority search of all spacing-statistic literature is not available; an equivalent mixed-moment identity may exist under different terminology. No independent mathematical audit has occurred.

## References
1. A. Baci, Z. Kabluchko, J. Prochno, M. Sonnleitner, C. Thäle, *Limit theorems for random points in a simplex*, first arXiv version 11 May 2020, https://arxiv.org/abs/2005.04911.
2. L. Holst, *Asymptotic normality of sum-functions of spacings*, Annals of Probability 7 (1979), 1066–1072, https://doi.org/10.1214/aop/1176994901.
3. P. Hall, *Limit theorems for sums of general functions of m-spacings*, Mathematical Proceedings of the Cambridge Philosophical Society 96 (1984), 517–532, https://doi.org/10.1017/S0305004100062459.
