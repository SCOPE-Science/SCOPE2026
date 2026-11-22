# Sharp successive-degree Bernstein stability and the rigid interlacing extremizer

## Finding

For each integer \(n\geq1\), let the classical Bernstein operator on real functions \(f:[0,1]\to\mathbb R\) be
\[
 (B_nf)(x)=\sum_{j=0}^{n}\binom nj x^j(1-x)^{n-j}f(j/n).
\]
With \(\operatorname{Lip}(f)=\sup_{s\ne t}|f(s)-f(t)|/|s-t|\), the **exact pointwise degree-increment norm** is
\[
 \sup_{\operatorname{Lip}(f)\leq1}|(B_{n+1}-B_n)f(x)|=\frac{2x(1-x)}{n+1}
 \qquad(0\leq x\leq1).
\]
Consequently the **exact global seminorm operator norm** is
\[
 \sup_{\operatorname{Lip}(f)\leq1}\|(B_{n+1}-B_n)f\|_{\infty}=\frac1{2(n+1)}.
\]
There is one explicit function \(h_n\), independent of \(x\), satisfying \(\operatorname{Lip}(h_n)=1\) and
\[
 (B_{n+1}-B_n)h_n(x)=\frac{2x(1-x)}{n+1}
 \quad\text{for every }x\in[0,1].
\]
Moreover, at **any one interior evaluation point** \(0<x<1\), every real \(1\)-Lipschitz function attaining the absolute pointwise norm is exactly \(h_n+c\) or \(-h_n+c\), for some constant \(c\in\mathbb R\). Thus the extremizer is rigid up to sign and additive constants, even when only a single interior point is prescribed.

Equivalently, for the laws \(\mu_{n,x}\) of \(n^{-1}\operatorname{Bin}(n,x)\),
\[
 W_1(\mu_{n,x},\mu_{n+1,x})=\frac{2x(1-x)}{n+1},
\]
with a common \(1\)-Lipschitz Kantorovich potential \(h_n\) for all \(x\) and the preceding rigidity at interior \(x\).

## Assumptions and scope

The input functions are real, defined on the entire unit interval, and have finite Lipschitz seminorm. Constants are immaterial because both Bernstein operators preserve constants. The integer \(n\geq1\) and parameter \(x\in[0,1]\) are arbitrary. The Wasserstein distance is for the usual absolute-value cost on \([0,1]\).

Define the **interlacing tent spline** \(h_n\) as the unique continuous function with \(h_n(0)=0\), linear on the subintervals of the union of grids \(\{j/n:0\le j\le n\}\cup\{k/(n+1):0\le k\le n+1\}\), and slope \(+1\) on
\[
 [j/n,(j+1)/(n+1)]\quad(0\le j<n),
\]
and slope \(-1\) on
\[
 [(j+1)/(n+1),(j+1)/n]\quad(0\le j<n).
\]
The grid intervals partition \([0,1]\). In particular,
\[
 h_n(j/n)=\frac{j(n-j)}{n(n+1)}\quad(0\le j\le n),
 \qquad
 h_n((j+1)/(n+1))=\frac{(j+1)(n-j)}{n(n+1)}\quad(0\le j<n).
\]

## Proof

**1. Coupling and universal bound.** Fix \(x\in[0,1]\). Let \(Z_1,\ldots,Z_{n+1}\) be independent Bernoulli variables with success probability \(x\). Put \(K=Z_1+\cdots+Z_n\), \(U=Z_{n+1}\), \(X=K/n\), and \(Y=(K+U)/(n+1)\). Then \(X\sim\mu_{n,x}\), \(Y\sim\mu_{n+1,x}\). For every \(1\)-Lipschitz \(f\),
\[
 |(B_{n+1}-B_n)f(x)|=|\mathbb E(f(Y)-f(X))|\leq\mathbb E|Y-X|.
\]
Conditional on \(K=j\), the displacement magnitudes are \(j/[n(n+1)]\) when \(U=0\), and \((n-j)/[n(n+1)]\) when \(U=1\). Using \(\mathbb EK=nx\) gives
\[
 \mathbb E|Y-X|=
 \frac{(1-x)\mathbb EK+x(n-\mathbb EK)}{n(n+1)}
 =\frac{2x(1-x)}{n+1}.
\]
This proves the stated pointwise upper bound for all admissible \(n,x,f\).

**2. One extremizer works at every point.** For each \(0\le j\le n\), \(j/n\) is the trough between the adjacent nodes \(j/(n+1)\) and \((j+1)/(n+1)\), with boundary coincidences at \(j=0,n\). By construction,
\[
 h_n(j/(n+1))-h_n(j/n)=\frac{j}{n(n+1)},
 \qquad
 h_n((j+1)/(n+1))-h_n(j/n)=\frac{n-j}{n(n+1)}.
\]
Thus \(h_n(Y)-h_n(X)=|Y-X|\) for *every* possible outcome of the coupling. Its piecewise slopes have absolute value one, so it is globally \(1\)-Lipschitz. Taking expectation gives equality for all \(x\), including the endpoints where both sides vanish. The maximum of \(2x(1-x)/(n+1)\) over \(x\in[0,1]\) occurs uniquely at \(x=1/2\) and is \(1/[2(n+1)]\).

**3. Rigidity of pointwise extremizers.** Fix \(0<x<1\), so every event \(\{K=j,U=u\}\) has strictly positive probability for \(0\le j\le n\), \(u\in\{0,1\}\). If \(f\) is \(1\)-Lipschitz and equality holds in the absolute pointwise bound, equality holds in both
\[
 |\mathbb E(f(Y)-f(X))|\le\mathbb E|f(Y)-f(X)|\le\mathbb E|Y-X|.
\]
Since the probability space is finite and every atom is positive, all nonzero increments \(f(Y)-f(X)\) must have magnitude \(|Y-X|\) and one common sign \(\varepsilon\in\{-1,1\}\). Each consecutive pair of distinct nodes in the interlaced grid occurs as an endpoint pair \((X,Y)\) for one of these atoms. Therefore \(f\) has increments \(\varepsilon\) times the corresponding increments of \(h_n\) along every consecutive grid interval. Furthermore, a \(1\)-Lipschitz function attaining the full distance between endpoints of an interval must be linear on that interval with slope \(+1\) or \(-1\) according to the endpoint order: for an interior point, the two Lipschitz inequalities add to the endpoint distance and hence both are equalities. It follows that \(f=\varepsilon h_n+c\) on all of \([0,1]\). Conversely these two families attain the bound.

**4. Transport statement.** Every coupling of \(\mu_{n,x}\) and \(\mu_{n+1,x}\) has average absolute displacement at least \(|\int h_n\,d\mu_{n+1,x}-\int h_n\,d\mu_{n,x}|\), by the \(1\)-Lipschitz property. The explicit Bernoulli coupling has exactly this cost by step 2. Hence its cost is optimal and gives the displayed \(W_1\) value without assuming a transport-duality theorem. The same rigidity applies to its Lipschitz maximizing potentials.

## Verification

The standalone `verify_bernstein.py` uses only Python's standard library and exact rational arithmetic. For every \(1\le n\le23\) it reconstructs the two interlaced grids, verifies the slopes and nodal values of \(h_n\), and checks the polynomial identity at eight rational evaluation points. Independently it evaluates \(W_1\) by integrating absolute differences of the two discrete cumulative distribution functions over the common grid, again with exact rational arithmetic. Both families of checks pass in 184 cases. The identities for *all* degrees and all real evaluation points are proved in the previous section; finitely many computations are not treated as an infinite proof. Reproduce using `python verify_bernstein.py`.

## Relationship to prior work

Classical Bernstein operators, preservation of Lipschitz constants, and approximation of individual functions in Hölder norms are established subjects. Brown, Elliott, and Paget (1987) established preservation of Lipschitz classes by each \(B_n\), as precisely restated and attributed in Gonska–Prestin–Tachev–Zhou; the published latter article provides direct, separately stated estimates for \(B_nf-f\). Those statements do not imply the **exact successive-degree difference**, an extremizer attaining equality at **every evaluation point**, or rigidity from **one** point. Aldaz–Kounchev–Render study generalized Bernstein bases and convergence; their construction does not compare these two consecutive classical Bernstein laws in the Lipschitz-to-uniform norm. Classical one-dimensional transport comparison supplies a general method for computing \(W_1\), but not the present closed formula or the common-potential rigidity without the interlacing calculation.

## Limitations

The theorem is about neighboring degrees, ordinary equally spaced Bernstein sampling and real \(1\)-Lipschitz inputs; it does not assert an exact coefficient for arbitrarily separated degrees, Hölder exponents strictly below one, Bernstein–Durrmeyer kernels, or multivariate operators. The result is a mathematical argument and reproducible finite check, not a claim of historical priority beyond the literature examined; additional inaccessible or unindexed earlier equivalents may exist.

## References

1. H. Gonska, J. Prestin, G. Tachev, D.-X. Zhou, *Simultaneous approximation by Bernstein operators in Hölder norms*, Mathematische Nachrichten (first published 2012-11-23), DOI: 10.1002/mana.201100284. Accessible author manuscript: https://www.math.uni-luebeck.de/mitarbeiter/prestin/ps/bernstein2.pdf. Relevant: introductory Theorems A–E, Theorem 1, Lemmas 2–4 and proof section.
2. B. M. Brown, D. Elliott, D. F. Paget, *Lipschitz constants for the Bernstein polynomials of a Lipschitz continuous function*, Journal of Approximation Theory 49 (1987), 196–199, DOI: 10.1016/0021-9045(87)90087-6. Its cited preservation statement is available in reference 1, Lemma 4; the complete original article was not accessed.
3. J. M. Aldaz, O. Kounchev, H. Render, *Bernstein operators for exponential polynomials*, arXiv:0805.1618, first submitted 2008-05-12, https://arxiv.org/abs/0805.1618. Relevant: classical benchmark and generalized Bernstein existence/convergence results.
4. S. S. Vallender, *Calculation of the Wasserstein Distance Between Probability Distributions on the Line*, Theory of Probability and Its Applications 18 (1974), 784–786, DOI: 10.1137/1118101. Used as transport background, not for a binomial-specific formula.
