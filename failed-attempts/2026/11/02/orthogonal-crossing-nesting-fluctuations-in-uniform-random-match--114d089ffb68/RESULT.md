# Orthogonal crossing–nesting fluctuations in uniform random matchings

## Finding

Let a uniformly random perfect matching of \(\{1,\ldots,2n\}\) have \(n\) edges. Let \(X_n\) and \(N_n\) denote the numbers of crossing and nesting **pairs of edges**, respectively. For every integer \(n\ge2\),

\[
\begin{aligned}
\mathbb E[X_n]=\mathbb E[N_n]&=\frac{n(n-1)}6,\\
\operatorname{Var}(X_n)=\operatorname{Var}(N_n)&=\frac{n(n-1)(n+3)}{45},\\
\operatorname{Cov}(X_n,N_n)&=-\frac{n(n-1)}{18},\\
\operatorname{Corr}(X_n,N_n)&=-\frac5{2(n+3)}.
\end{aligned}
\]

The **joint limit** is more informative than the marginal normal laws:

\[
\frac{\sqrt{45}}{n^{3/2}}
\left(X_n-\frac{n(n-1)}6,\ N_n-\frac{n(n-1)}6\right)
\xrightarrow{d}(Z_1,Z_2),
\]

where \(Z_1\) and \(Z_2\) are **independent standard Gaussian** variables. Indeed, in a uniformly randomly edge-labeled matching, any crossing indicator and nesting indicator associated with *different* unordered pairs of edge labels are independent, including pairs sharing one edge. Indicators corresponding to the same pair are mutually exclusive.

## Assumptions and scope

A crossing consists of edges \((a,b)\), \((c,d)\) with \(a<c<b<d\) after reordering the two edges by their left endpoints. A nesting has \(a<c<d<b\). The remaining case \(a<b<c<d\) is an alignment. There are no coincident endpoints. The probability space is the uniform law on the \((2n-1)!!\) perfect matchings; labels assigned to the \(n\) edges only in the proof do not change the unlabeled statistics. For \(n=1\) both counts vanish, so their correlation is undefined and the correlation claim starts at \(n=2\).

## Proof

**1. Independent-chord representation.** Independently sample \(n\) pairs of uniform random points in \((0,1)\), sort the two points within each pair, and then sort all \(2n\) points. Every labeled matching of the resulting ranks is equally likely by exchangeability of the endpoints; deleting the auxiliary edge labels gives a uniform unlabeled matching. Write one sampled edge as \(Z=(u,v)\) with \(0<u<v<1\), and define the three gaps

\[
(a,b,c)=(u,v-u,1-v).
\]

The gap vector has the \(\operatorname{Dirichlet}(1,1,1)\) law. For independent second edge \(Z'\), the conditional crossing and nesting probabilities are

\[
p_X(Z)=2b(a+c),\qquad p_N(Z)=b^2+2ac.
\]

The first formula counts one endpoint inside and one outside the edge. The second counts both second-edge endpoints inside the edge, or one on each external side. Thus these formulas include both orientations and all boundary cases (ties have probability zero).

**2. Exact one-edge projection moments.** For integers \(i,j,k\ge0\), the Dirichlet moment formula reads

\[
\mathbb E[a^i b^j c^k]=\frac{2i!j!k!}{(i+j+k+2)!}.
\]

Direct expansion (also reproduced in the standalone verifier) gives

\[
\begin{aligned}
\mathbb E p_X=\mathbb E p_N&=\frac13,\\
\mathbb E p_X^2=\mathbb E p_N^2&=\frac2{15},\\
\mathbb E[p_Xp_N]&=\frac19.
\end{aligned}
\]

Consequently, \(\operatorname{Var}(p_X)=\operatorname{Var}(p_N)=1/45\) and **\(\operatorname{Cov}(p_X,p_N)=0\)**. This last identity is the critical mixed-projection cancellation. It is an exact expectation, not an asymptotic approximation.

**3. Indicator dependence and exact second moments.** Give each sampled edge a label. For unordered pairs \(e=\{i,j\}\) of edge labels, write \(I^X_e\) and \(I^N_e\) for the crossing and nesting indicators. Each has expectation \(1/3\). If \(e=f\), mutual exclusion gives \(\operatorname{Cov}(I^X_e,I^N_e)=-1/9\). If \(e\cap f=\varnothing\), independence of the four underlying edges gives covariance zero. If \(e\ne f\) and \(|e\cap f|=1\), condition on the shared edge. The two other edges are conditionally independent, so

\[
\mathbb E[I^X_e I^N_f]=\mathbb E[p_X(Z)p_N(Z)]=\frac19.
\]

These Bernoulli indicators are therefore independent, not merely uncorrelated. Summing over the \(\binom n2\) diagonal pairs yields

\[
\operatorname{Cov}(X_n,N_n)=-\frac19\binom n2=-\frac{n(n-1)}{18}.
\]

For indicators of the same type the diagonal variance is \(2/9\); two distinct pairs sharing an edge have covariance \(\operatorname{Var}(p_X)=\operatorname{Var}(p_N)=1/45\), and disjoint pairs are independent. Exactly \(n(n-1)(n-2)\) ordered pairs of distinct two-element edge-label sets share one label. Therefore

\[
\operatorname{Var}(X_n)=\operatorname{Var}(N_n)
=\frac29\binom n2+\frac{n(n-1)(n-2)}{45}
=\frac{n(n-1)(n+3)}{45}.
\]

The stated means and correlation follow.

**4. Joint central limit theorem.** Write \(\mu=1/3\), \(g_X(Z)=p_X(Z)-\mu\), and \(g_N(Z)=p_N(Z)-\mu\). The exact order-two Hoeffding decompositions are

\[
\begin{aligned}
X_n-\binom n2\mu &=(n-1)\sum_{i=1}^{n}g_X(Z_i)+R_{X,n},\\
N_n-\binom n2\mu &=(n-1)\sum_{i=1}^{n}g_N(Z_i)+R_{N,n}.
\end{aligned}
\]

For either coordinate, the residual is the sum of canonical degenerate two-edge kernels. Distinct residual summands have covariance zero even if they share a label, because the expectation conditional on either individual edge is zero. Their common variance is \(2/9-2/45=8/45\). Hence

\[
\mathbb E[R_{X,n}^2]=\mathbb E[R_{N,n}^2]=\frac8{45}\binom n2=O(n^2).
\]

Dividing by \(n^{3/2}\) makes both residuals converge to zero in \(L^2\). The i.i.d. vectors \((g_X(Z_i),g_N(Z_i))\) are centered, bounded, and have covariance matrix \(\frac1{45}I_2\). The ordinary bivariate i.i.d. central limit theorem, the prefactor \((n-1)/n\to1\), and Slutsky's theorem prove the displayed joint Gaussian limit with independent components. No inference of joint independence from separate marginal central limit theorems is used.

## Verification

The complete standalone Python 3 standard-library program `verify.py` independently enumerates all perfect matchings through \(n=7\), checks both exact means, variances and cross-covariance, checks the mixed-pair independence with auxiliary edge labels, and evaluates the Dirichlet polynomial integrals as exact rational numbers. Its separate run on the embedded source produced `PASS: 652 exact assertions, matchings exhaustively enumerated through n=7.` This finite verification is a check of the explicit formulas, not the proof of the infinite family or the central limit theorem.

## Relationship to prior work

Flajolet and Noy established exact marginal crossing mean and variance and a **univariate** crossing Gaussian limit. Their crossing variance matches the expression above and is not claimed as new. Chen, Deng, Du, Stanley and Yan studied the symmetry of maximum crossing and nesting sizes. Klazar studied identities for the joint crossing/nesting count distributions. Kasraoui and Zeng derived the **full joint crossing/nesting enumerating polynomials** via continued fractions (Proposition 4.4), so the existence of a bivariate finite-size law and the fact that its moments can in principle be extracted are prior results. Baik and Jenkins proved asymptotic independence for **maximal crossing and nesting sizes**, not for the total numbers of crossing and nested edge pairs. The contribution assessed here is the explicit mixed-label indicator orthogonality and a joint Gaussian limit for the **total two-edge counts**. No broad first-ever priority assertion is made.

## Limitations

The convergence is weak convergence of centered, scaled totals; it does not assert finite-sample independence, convergence in total variation, or a quantitative joint convergence rate. In fact their exact finite covariance is negative for every \(n\ge2\). The result concerns uniform matchings, not nonuniform matchings or the extremal sizes of crossing/nesting sets. Full historical priority has not been independently established; the known bivariate generating polynomial determines finite mixed moments and is a genuine broad-coverage precedent. The March 2000 technical report has a month-level report date and a dated manuscript, not an independently verified day-specific public release date.

## References

- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914 (March 2000), Section 2 and Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
- W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, first arXiv posting January 14, 2005, https://arxiv.org/abs/math/0501230
- M. Klazar, *On Identities Concerning the Numbers of Crossings and Nestings of Two Edges in Matchings*, first arXiv posting March 1, 2005, https://arxiv.org/abs/math/0503012
- A. Kasraoui and J. Zeng, *Distribution of Crossings, Nestings and Alignments of Two Edges in Matchings and Partitions*, Electronic Journal of Combinatorics 13 (2006), R33, published April 4, 2006, Section 4, Proposition 4.4. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r33/pdf
- J. Baik and R. Jenkins, *Limiting Distribution of Maximal Crossing and Nesting of Poissonized Random Matchings*, first arXiv posting November 1, 2011, https://arxiv.org/abs/1111.0269
