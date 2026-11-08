# Exact negative return–occupation-imbalance covariance in a symmetric random-walk bridge

## Finding

For each integer \(n\ge1\), take a uniformly sampled nearest-neighbor bridge \((S_t)_{0\le t\le 2n}\) on \(\mathbb Z\), with \(S_0=S_{2n}=0\) and increments in \(\{-1,+1\}\). Let \(K_n\) be the number of returns to zero at positive times, including the final time. Let \(A_n\) be the number of steps whose midpoint is strictly positive, and \(D_n=A_n-n\). Then

\[
\operatorname{Cov}(K_n,D_n^2)
=-\frac{n(n-1)}{12}\frac{4^n}{\binom{2n}{n}}.
\]

The covariance vanishes for \(n=1\) and is strictly negative for every \(n\ge2\). In addition, the exact Pearson correlation converges as \(n\to\infty\) to

\[
\operatorname{Corr}(K_n,D_n^2)\longrightarrow
-\frac{\sqrt{5\pi}}{8\sqrt{4-\pi}}
\approx-0.5347160729.
\]

## Assumptions and scope

All \(\binom{2n}{n}\) bridges with \(n\) up-steps and \(n\) down-steps have equal probability. A step is counted in \(A_n\) when \(S_{t-1}+S_t>0\); no step midpoint equals zero. An excursion is the maximal segment between consecutive visits to zero; \(K_n\) counts these excursions, including the final segment. In particular, \(A_n\in\{0,2,\ldots,2n\}\) and \(D_n\in\{-n,-n+2,\ldots,n\}\). The correlation statement requires \(n\ge2\), when both variances are positive.

## Proof

**Excursion decomposition.** A signed irreducible excursion of length \(2\ell\), \(\ell\ge1\), has \(2C_{\ell-1}\) realizations, where \(C_j=\binom{2j}{j}/(j+1)\) is Catalan. With \(z\) marking half-length and \(u\) marking the number of excursions,

\[
E(z)=\sum_{\ell\ge1}2C_{\ell-1}z^\ell=1-\sqrt{1-4z},\qquad
B(z,u)=\frac1{1-uE(z)}.
\]

Put \(s=\sqrt{1-4z}\). Since \(B(z,1)=s^{-1}\), its \(z^n\) coefficient is \(W_n=\binom{2n}{n}\). Derivation with respect to \(u\) gives

\[
\sum_{n\ge0}\left(\sum_{\mathrm{bridges}}K_n\right)z^n
=\left.\frac{\partial B}{\partial u}\right|_{u=1}
=\frac{E}{s^2}=s^{-2}-s^{-1}.
\]

Thus with \(q_n=4^n/W_n\), \(\mathbb E K_n=q_n-1\).

**Signed-occupation reduction.** Conditional on the ordered excursion half-lengths \(\ell_1,\ldots,\ell_k\), the positive/negative signs of the excursions are independent fair choices. Hence

\[
D_n=\sum_{i=1}^k\varepsilon_i\ell_i,
\qquad \mathbb E[D_n^2\mid\ell_1,\ldots,\ell_k]
=\sum_{i=1}^k\ell_i^2=:Q_n.
\]

In particular, \(\mathbb E D_n^2=\mathbb E Q_n\) and \(\mathbb E K_nD_n^2=\mathbb E K_nQ_n\). Let \(\mathcal D=z\,d/dz\) and

\[
F(z)=\mathcal D^2 E(z)=2zs^{-1}+4z^2s^{-3}.
\]

Marking one excursion by its squared half-length gives the *unnormalized* mixed-moment series

\[
Q(z,u)=\sum_{n\ge1}W_n\,\mathbb E[u^{K_n}Q_n]z^n
=\frac{u F(z)}{(1-uE(z))^2}.
\]

At \(u=1\), \(Q(z,1)=F/s^2\). Differentiating and then adding back \(Q(z,1)\) produces the key cancellation

\[
\left.\frac{\partial Q}{\partial u}\right|_{u=1}+Q(z,1)
=\frac{2F}{s^3}=4z(1-4z)^{-2}+8z^2(1-4z)^{-3}.
\]

The coefficient of \(z^n\) on the right is \(4^n n(n+3)/4\). Direct coefficient extraction from \(F/s^2\) gives

\[
\mathbb E D_n^2=\mathbb E Q_n=\frac{n(n+2)}3.
\]

Consequently

\[
\begin{aligned}
\operatorname{Cov}(K_n,D_n^2)
&=\frac{4^n}{W_n}\frac{n(n+3)}4
-\left(\mathbb E K_n+1\right)\mathbb E D_n^2\\
&=q_n\left(\frac{n(n+3)}4-\frac{n(n+2)}3\right)
=-\frac{n(n-1)}{12}q_n.
\end{aligned}
\]

**Variance and correlation.** A second derivative of \(B(z,u)\) gives \(\mathbb E (K_n)_2\), resulting in

\[
\operatorname{Var}(K_n)=4n+2-q_n-q_n^2.
\]

To identify the \(D_n\) variance, let \(v\) mark the positive occupation half-length. Positive and negative irreducible excursions have OGFs \((1-\sqrt{1-4zv})/2\) and \((1-\sqrt{1-4z})/2\), respectively. Therefore the bivariate bridge OGF is

\[
\frac2{\sqrt{1-4zv}+\sqrt{1-4z}}
=\sum_{n\ge0}C_nz^n\sum_{j=0}^nv^j.
\]

Hence the Chung–Feller uniform sojourn law holds directly: \(A_n/2\) is uniformly distributed on \(\{0,1,\ldots,n\}\). Elementary finite power sums yield

\[
\operatorname{Var}(D_n^2)
=\frac{4n(n+2)\bigl(n(n+2)-3\bigr)}{45}.
\]

Finally, the central-binomial estimate \(q_n=\sqrt{\pi n}\,(1+O(n^{-1}))\) yields \(\operatorname{Var}(K_n)\sim(4-\pi)n\), \(\operatorname{Var}(D_n^2)\sim4n^4/45\), and \(\operatorname{Cov}(K_n,D_n^2)\sim-\sqrt\pi\,n^{5/2}/12\), which give the stated correlation limit.

## Verification

The accompanying standard-library program `check_bridge.py` independently enumerates every bridge for \(1\le n\le8\), checks the exact moments and covariance using rational arithmetic, and checks the Chung–Feller occupation counts. A separate dynamic excursion decomposition verifies the mixed-moment identity for \(1\le n\le80\), with numerical correlation diagnostics for larger \(n\). Run `python check_bridge.py` from the extracted directory. These finite checks support, but do not replace, the generating-function proof.

## Relationship to prior work

The uniform occupation marginal is the classical Chung–Feller theorem. Lindell and Holst (2007), Proposition 3.1, supply a broad multivariate generating-function framework for excursion-length interval counts in tied-down walks; this framework is relevant to the length component of the present calculation, but does not directly state the signed-sojourn mixed moment, its exact negative covariance, or the nonzero limiting correlation. Assaf, Forman, and Pitman (2013) examine simple-walk occupation and local-time profiles via the quantile transform; Lupu, Pitman, and Tang (2013, revised 2015) study Brownian bridge Vervaat transforms. These provide motivation and context rather than a statement equivalent to the exact finite bridge covariance here.

## Limitations

The claim concerns only a uniform, unweighted nearest-neighbor bridge with equal up and down steps. It does not assert a correlation theorem for general random walks, nonzero endpoints, or continuous-time bridges. Known general excursion-length generating functions can potentially be specialized to infer this mixed moment after additional signed-excursion and coefficient calculations; consequently an implicit-priority risk remains. No independent external mathematical audit has been carried out.

## References

1. A. Lindell and L. Holst, *Distributions of the Longest Excursions in a Tied Down Simple Random Walk and in a Brownian Bridge*, Journal of Applied Probability 44 (2007), 1054–1067, https://doi.org/10.1239/jap/1197908824.
2. S. Assaf, N. Forman, and J. Pitman, *The quantile transform of a simple walk*, arXiv:1307.4967 (first posted 2013-07-18), https://arxiv.org/abs/1307.4967.
3. T. Lupu, J. Pitman, and W. Tang, *The Vervaat transform of Brownian bridges and Brownian motion*, arXiv:1310.3889 (first posted 2013-10-15), https://arxiv.org/abs/1310.3889.
4. C. Godrèche, *Two-time correlation and occupation time for the Brownian bridge and tied-down renewal processes*, arXiv:1704.04406 (first posted 2017-04-14), https://arxiv.org/abs/1704.04406.
5. Classical Chung–Feller uniform sojourn-time identity; a self-contained generating-function derivation is given above.
