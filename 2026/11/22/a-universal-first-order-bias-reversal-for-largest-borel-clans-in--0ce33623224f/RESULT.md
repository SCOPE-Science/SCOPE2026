# A universal first-order bias reversal for largest Borel clans in near-critical generalized Poisson samples

## Finding

**Theorem.** Fix \(\mu>0\) and \(a>0\). For each integer \(n>a\), let \(\delta_n=\sqrt{a/n}\), \(\theta_n=1-\delta_n\), and let \(X_{n,1},\ldots,X_{n,n}\) be independent generalized Poisson variables with parameters \((\lambda_n,\theta_n)=(\mu\delta_n,1-\delta_n)\). Here \(\mathbb E[X_{n,j}]=\mu\) for every \(n\). Resolve the natural compound-Poisson representation of these observations into independent Borel-family sizes \(B_{n,i}\), over all original founders across the observations, and let \(L_n\) be their largest size (set \(L_n=0\) if there is no founder).

For \(z>0\), define
\[
I(z)=\int_z^\infty u^{-3/2}e^{-u/2}\,du,
\quad
J(z)=\int_z^\infty u^{-3/2}e^{-u/2}\left(1-\frac u3\right)\,du,
\quad c=\frac{\mu a}{\sqrt{2\pi}}.
\]
For each compact \(K\subset(0,\infty)\), the following asymptotic is **uniform** for \(x\in K\):
\[
\boxed{\mathbb P(L_n/n\le x)=e^{-cI(ax)}\left[1-\delta_n cJ(ax)+O_{\mu,a,K}(n^{-1})\right].}
\]
In particular, the leading CDF \(e^{-cI(ax)}\) is a nondegenerate law on positive reals, and its **signed first finite-sample correction** changes direction exactly once, at the universal rescaled threshold \(z_*=1.888985943515\ldots\). Precisely, \(z_*\in(0,3)\) is the unique solution of
\[
\frac{e^{-z/2}}{\sqrt z}=\frac23\sqrt{2\pi}\,\operatorname{erfc}\!\left(\sqrt{z/2}\right).
\]
For any fixed \(x<z_*/a\), the finite-\(n\) CDF is strictly **below** its limit for all sufficiently large \(n\); for any fixed \(x>z_*/a\), it is strictly **above** its limit for all sufficiently large \(n\). At the threshold \(x=z_*/a\), the error is \(O(n^{-1})\). Away from the threshold the error is asymptotically a nonzero constant times \(n^{-1/2}\).

## Assumptions and scope

The generalized Poisson probability mass function is
\[
\mathbb P(X=k)=\frac{\lambda(\lambda+k\theta)^{k-1}}{k!}e^{-\lambda-k\theta},
\qquad k=0,1,2,\ldots,
\]
with the \(k=0\) mass interpreted as \(e^{-\lambda}\). For the present parameters \(\lambda>0\), \(0<\theta<1\), the familiar Galton–Watson representation is a Poisson number of independent Borel-clans, whose individual sizes satisfy
\[
p_k(\theta)=\mathbb P(B=k)=\frac{(\theta k)^{k-1}}{k!}e^{-\theta k},\qquad k\ge1.
\]
Pooling founders across the \(n\) independent observations yields a Poisson number \(M_n\) of clans with mean \(n\mu\delta_n\). Conditionally on \(M_n\), their sizes are iid \(\operatorname{Borel}(1-\delta_n)\). The statistic is **the largest founding clan**, not the maximum of the \(n\) total observations and not the total progeny across all clans. Parameters \(\mu,a\) are fixed strictly positive constants; the conclusion concerns \(n\to\infty\) and \(x\) bounded away from both zero and infinity.

## Proof

**1. Exact finite-size maximum CDF.** Poisson marking/thinning gives, without approximation,
\[
\mathbb P(L_n/n\le x)=\exp\!\left\{-n\mu\delta_n\sum_{k>nx}p_k(1-\delta_n)\right\}.
\tag{1}
\]
The strict inequality \(k>nx\) treats integer thresholds exactly (the first included index is \(\lfloor nx\rfloor+1\)). The empty-forest convention is included in (1).

**2. Borel coefficient expansion.** Put \(\delta=\delta_n\), \(\theta=1-\delta\), and \(q=\theta e^{1-\theta}\). Stirling's formula with its uniform remainder yields, for integer \(k\ge1\),
\[
p_k(\theta)=\frac{q^k}{\theta\sqrt{2\pi}\,k^{3/2}}\left[1+O(k^{-1})\right],
\qquad \log q=\log(1-\delta)+\delta
=-\frac{\delta^2}{2}-\frac{\delta^3}{3}+O(\delta^4).
\tag{2}
\]
For \(y=k/n\ge x_0>0\), use \(n\delta^2=a\) and \(\theta^{-1}=1+\delta+O(\delta^2)\) to obtain
\[
p_k(1-\delta)=\frac{e^{-ay/2}}{\sqrt{2\pi}\,k^{3/2}}
\left[1+\delta\left(1-\frac{ay}{3}\right)+R_n(y)\right].
\tag{3}
\]
For each fixed positive \(x_0\) the remainder satisfies a weighted summability bound
\[
\sum_{k>nx_0} k^{-3/2}e^{-ak/(2n)}|R_n(k/n)|=O_{a,x_0}(\sqrt n\,n^{-3/2}\delta^2)=O_{a,x_0}(\delta^2 n^{-1/2}).
\]
Indeed, (2) includes the \(O(1/k)\) factorial error, which is \(O(1/n)\) on this range. Expand the nonpositive exponential \(\exp[-(a\delta/3)y+O(\delta^2 y)]\) with an integrated error bounded by \(C\delta^2(1+y^2)e^{-ay/4}\); this bound is summable for all \(y\ge x_0\). Thus (3) may be integrated termwise on every tail bounded away from zero. This weighted estimate, rather than a pointwise expansion for arbitrarily huge \(k\), justifies the infinite tail.

**3. Uniform first correction.** Riemann summation on \((x,\infty)\), uniformly for \(x\) in a fixed compact subset of \((0,\infty)\), has error \(O(n^{-1})\) for the smooth integrable functions \(y^{-3/2}e^{-ay/2}\) and \(y^{-3/2}e^{-ay/2}(1-ay/3)\). Substituting (3) into the exponent of (1), changing variables \(u=ay\), and using \(n\mu\delta\,n\cdot n^{-3/2}=\mu\sqrt a\), gives
\[
n\mu\delta\sum_{k>nx}p_k(1-\delta)=\frac{\mu a}{\sqrt{2\pi}}
\left[I(ax)+\delta J(ax)+O_{a,K}(\delta^2)\right].
\tag{4}
\]
Since \(\delta^2=a/n\), exponentiating (4) proves the asserted uniform CDF expansion and its \(n^{-1/2}\) coefficient.

**4. Exactly one sign switch.** Integration by parts and the complementary error function give
\[
\begin{aligned}
I(z)&=\frac{2e^{-z/2}}{\sqrt z}-\sqrt{2\pi}\,\operatorname{erfc}(\sqrt{z/2}),\\
J(z)&=\frac{2e^{-z/2}}{\sqrt z}-\frac43\sqrt{2\pi}\,\operatorname{erfc}(\sqrt{z/2}).
\end{aligned}
\]
Furthermore,
\[
J'(z)=-z^{-3/2}e^{-z/2}(1-z/3).
\]
Thus \(J\) decreases strictly on \((0,3)\), increases strictly on \((3,\infty)\), tends to \(+\infty\) as \(z\downarrow0\), is strictly negative at \(z=3\), and tends to \(0\) from below as \(z\to\infty\). It therefore has **exactly one** zero, inside \((0,3)\), and the stated transcendental equation follows. The leading CDF-bias coefficient in (4) is \(-c e^{-cI(ax)}J(ax)\), whose sign changes there. The coefficient is nonzero everywhere else, giving sharp \(n^{-1/2}\) pointwise order. At the root (4) leaves an \(O(n^{-1})\) remainder; no sharper order is asserted there.

## Verification

A standalone Python 3 script, `check_borel_max.py`, uses only the standard library. It computes the **exact** finite-\(n\) CDF from Poisson–Borel probabilities (evaluating factorials via `math.lgamma`), compares three increasing sample sizes against the leading asymptotic and signed first correction at four positive thresholds, and checks the predicted direction change. It also verifies the numerical root of \(J\). Run from the directory containing the files:

```sh
python3 check_borel_max.py
```

The analytic proof is independent of these finite numerical comparisons. The printed precision of the approximate root is numerical, not a separate certified decimal interval.

## Relationship to prior work

Faroughi, Li and Ren (online 18 September 2024, [1]) give the generalized-Poisson distribution and its familiar compound-Poisson/Borel representation, but their results do not calculate the **largest founder-clan CDF** in the moving critical window or its explicit signed finite-size coefficient. These background formulas are not new here.

The classical inverse-Gaussian limit for appropriately rescaled generalized-Poisson **total counts** is already documented by Wolfram Research [2]; it does not imply the signed first correction for the **maximum clan**. Basrak, Milinčević and Žugec [3] analyze extremes of observation marks arriving in clusters, including Borel cluster sizes in the Hawkes background, but their propositions concern the maximum of **marks**, not this maximum of **tree sizes**, and do not give the one-crossing correction in (4). General Poisson point-process convergence and inverse-Gaussian Lévy-jump intensities are standard; the present contribution is the specified **model-dependent first correction and its universal unique zero**, not a general extreme-value theorem.

## Limitations

Only the fixed \(a>0\), fixed \(\mu>0\) near-critical path \(\delta_n=\sqrt{a/n}\) is studied. Uniformity is restricted to compact positive thresholds. The theorem does **not** establish that the exact finite-\(n\) CDF has precisely one crossing with its limit; lattice steps can matter near the limiting zero. The correction is first order only, with no asserted nonzero second coefficient at the zero. Historical priority beyond the inspected sources remains provisional; independent mathematical validation has not been performed.

## References

[1] P. Faroughi, S. Li, J. Ren, *Generalized Poisson random variable: its distributional properties and actuarial applications*, **Annals of Actuarial Science**, online 18 September 2024, DOI: 10.1017/S1748499524000198, https://doi.org/10.1017/S1748499524000198.

[2] Wolfram Research, *PoissonConsulDistribution*, documentation originally 2010, modified 2016, https://reference.wolfram.com/language/ref/PoissonConsulDistribution.html (properties and relations, inverse-Gaussian limit).

[3] B. Basrak, N. Milinčević, P. Žugec, *On extremes of random clusters and marked renewal cluster processes*, arXiv:2203.13507 (25 March 2022); **Journal of Applied Probability** 60 (2023), 367–381, https://arxiv.org/abs/2203.13507.

[4] A. Eberle, *Stochastic Analysis*, lecture notes (2019), section on Poisson points and inverse-Gaussian subordinators, https://wt.iam.uni-bonn.de/fileadmin/WT/Inhalt/people/Andreas_Eberle/StoAn_19/StochasticAnalysis2019.pdf.
