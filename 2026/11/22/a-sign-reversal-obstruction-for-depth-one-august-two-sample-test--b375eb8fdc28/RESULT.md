# A sign-reversal obstruction for depth-one AUGUST two-sample testing

## Finding

Consider the depth-one AUGUST two-sample statistic of Brown and Zhang, using its standard three-observation reference subsamples and upper-tail rejection. There exist distinct probability laws on the real line with everywhere positive, real-analytic densities for which **both** population symmetry signals are strictly positive but their negative product, the population statistic, is strictly negative. Specifically, let \(\Phi\) be the standard normal CDF and set

\[
F(x)=\Phi(x),\qquad G(x)=Q(\Phi(x)),\qquad
Q(u)=4u^4-5u^3+\frac{243}{700}u^2+\frac{1157}{700}u.
\]

Then the two depth-one population symmetry statistics, with the first sample drawn from \(G\) and the second from \(F\), satisfy

\[
a=\frac1{250}>0,\qquad
b=\frac{45549381047}{5150145000000}>0,\qquad
-ab=-\frac{45549381047}{1287536250000000}<0.
\]

For independent samples of sizes \(m,n\to\infty\) with \(m/(m+n)\to\lambda\in(0,1)\), the observed statistic converges to this strictly negative constant. Consequently, its distribution-free, right-tail null calibration at any fixed significance level \(\alpha\in(0,1)\), including \(0.05\), has **limiting rejection probability zero** under these nonidentical distributions. The result concerns the depth-one, standard three-reference-observation version, not higher-depth AUGUST or other two-sample procedures.

A supporting, exact finite-null identity for this same statistic is

\[
\mathbb E_0 S_{m,n}=\frac{17(m+n+1)}{35mn},\qquad m,n\ge4.
\]

## Assumptions and scope

Let \(X_1,\ldots,X_m\) be independent draws from \(G\), and independently let \(Y_1,\ldots,Y_n\) be draws from \(F\), with \(m,n\ge4\). For three real reference observations \(y_1,y_2,y_3\), write

\[
k(x;y_1,y_2,y_3)=2\mathbf1\{x<\operatorname{med}(y_1,y_2,y_3)\}-1.
\]

Define the two symmetry statistics as the exact (without-replacement) averages

\[
S_X=\frac1{m\binom n3}\sum_{i=1}^{m}\ 
\sum_{J\subseteq\{1,\ldots,n\},\ |J|=3}
k(X_i;Y_J),
\]

\[
S_Y=\frac1{n\binom m3}\sum_{j=1}^{n}\ 
\sum_{I\subseteq\{1,\ldots,m\},\ |I|=3}
k(Y_j;X_I),\qquad S_{m,n}=-S_XS_Y.
\]

For continuous laws, ties have probability zero. These are precisely the depth-one AUGUST coordinates produced by the two-cell Hadamard contrast and three-reference-observation hypergeometric probabilities. All statements use the original right-tail statistic \(S_{m,n}\), not a separately modified or absolute-value statistic.

## Proof

**1. Population coordinate formula.** For any continuous reference CDF \(H\), the probability that no more than one of three independent reference draws falls below \(x\) is \((1-H(x))^3+3H(x)(1-H(x))^2\). Thus the conditional mean of the kernel is

\[
h(H(x)),\qquad h(u)=1-6u^2+4u^3.
\]

Let \(Q=G\circ F^{-1}\), with \(F\) strictly increasing. The two population contrasts are

\[
a(Q)=\int_0^1h(u)\,dQ(u),\qquad b(Q)=\int_0^1h(Q(u))\,du.
\]

For \(\psi(u)=Q(u)-u\), integration by parts and exact cubic Taylor expansion give the structural identity

\[
a(Q)=12\int_0^1u(1-u)\psi(u)\,du,
\]

\[
b(Q)=-a(Q)+12\int_0^1\left(u-\tfrac12\right)\psi(u)^2\,du
+4\int_0^1\psi(u)^3\,du.
\]

It follows that the reflected contrasts need not have opposite signs: their sum is controlled by genuinely nonlinear terms, not merely by a sign reversal of the first-order perturbation.

**2. An admissible polynomial with same-sign nonzero coordinates.** The displayed quartic has \(Q(0)=0\) and \(Q(1)=1\). Its derivative is

\[
Q'(u)=16u^3-15u^2+\frac{243}{350}u+\frac{1157}{700}.
\]

To check strict positivity without a numerical plot, expand this cubic in the degree-three Bernstein basis on each indicated subinterval. The coefficient tuples are, respectively,

\[
\begin{array}{c|c}
[0,1/2]&(1157/700,\ 619/350,\ 111/175,\ 1/4)\\
[1/2,3/4]&(1/4,\ 81/1400,\ 149/2800,\ 1361/2800)\\
[3/4,1]&(1361/2800,\ 2573/2800,\ 501/280,\ 2343/700).
\end{array}
\]

Every coefficient is positive; since Bernstein basis polynomials are nonnegative and sum to one, \(Q'(u)>0\) throughout \([0,1]\). Thus \(Q\) is a strictly increasing CDF transformation. The two real-line densities are \(f(x)=\phi(x)\) and \(g(x)=\phi(x)Q'(\Phi(x))\), both positive and real analytic. In particular, \(F\ne G\).

Exact rational polynomial integration, with no numerical approximation, gives

\[
\int_0^1h(u)Q'(u)\,du=\frac1{250},\quad
\int_0^1h(Q(u))\,du=\frac{45549381047}{5150145000000}.
\]

Both are positive, hence the population signed product is strictly negative as stated. By the strong law for bounded, fixed-order two-sample U-statistics, \(S_X\to a(Q)\), \(S_Y\to b(Q)\), and \(S_{m,n}\to-a(Q)b(Q)<0\) almost surely when both sample sizes tend to infinity.

**3. Exact null and its positive rejection scale.** Under the common continuous null, the probability integral transform reduces all observations to independent uniforms. For one random uniform \(U\), \(\mathbb E h(U)=0\) and \(\mathbb E h(U)^2=17/35\). In the two-sample Hoeffding projections of \(S_X\), fixing the distinguished first-sample observation at \(u\) produces \(h(u)\), while fixing any one of the three reference observations at \(u\) produces \(-h(u)/3\). Consequently, with \(N=m+n\) and \(m/N\to\lambda\in(0,1)\),

\[
S_X=\Delta_N+O_p(N^{-1}),\quad
S_Y=-\Delta_N+O_p(N^{-1}),\quad
\Delta_N=\frac1m\sum_{i=1}^{m}h(U_i)-\frac1n\sum_{j=1}^{n}h(V_j).
\]

The ordinary independent-sample central limit theorem and the continuous mapping theorem therefore yield

\[
NS_{m,n}\ \xrightarrow{d}\ \frac{17}{35\lambda(1-\lambda)}\,\chi_1^2.
\]

The null distribution is exactly distribution-free because the statistic depends only on the relative ranks of the two continuous samples. Hence its fixed-level upper-tail critical values satisfy \(c_{m,n,\alpha}\to0\) (indeed, their \(N\)-multiples converge to positive chi-square quantiles). Under the exhibited alternative \(S_{m,n}\) converges to a fixed negative number, so \(\Pr_{F,G}\{S_{m,n}>c_{m,n,\alpha}\}\to0\). The same conclusion holds for asymptotically equivalent null calibration.

**4. Exact finite-null expectation.** In the product of the two U-statistics, the distinguished \(X\) observation appears among the three \(X\) references of the opposite statistic with probability \(3/m\), and the distinguished \(Y\) observation appears among the three \(Y\) references with probability \(3/n\). When neither appears, the product mean is zero. When exactly one appears, the conditional-projection calculation gives joint mean \(-17/105\). When both appear, conditioning on their values and integrating over the other independent references gives

\[
2\int_{0<x<y<1}(1-2x^2)(1-4y+2y^2)\,dx\,dy=-\frac{17}{45}.
\]

Combining these three overlap cases with their exact hypergeometric probabilities gives

\[
\mathbb E_0[S_XS_Y]=-
\frac{17}{35}\left(\frac1m+\frac1n+\frac1{mn}\right),
\]

and the stated positive null mean follows after negating the product.

## Verification

The accompanying `check.py` uses only standard-library exact fractions. It checks the polynomial CDF endpoints, all positive Bernstein coefficients, both population integrals, the sign and value of the limiting statistic, the cubic structural identity, the projection variance, the double-overlap integral, and exact uniform-interleaving enumeration for nine sample-size pairs. It reports 40 exact identities/checks passed. No finite enumeration is used as a substitute for the all-size U-statistic argument or the asymptotic proof.

Run with `python3 check.py`. The main theorem does not require simulation, external data or fitted parameters.

## Relationship to prior work

Brown and Zhang's first public AUGUST preprint (2021), its expanded 2023 journal version, and the accompanying supplementary proofs establish the hypergeometric construction, the negative-inner-product statistic, general two-sample U-statistic asymptotics and population cell-probability expressions. Their stated intuition concerns typically opposite symmetry signals; these sources do not exhibit the present strictly same-sign population pair with a negative test limit and zero limiting right-tail power. The general U-statistic theorem provides the convergence framework but not the sign-reversal existence certificate, quartic construction or exact finite-null mean proved here.

Zhang's earlier binary-expansion independence test concerns a different dependence-testing construction; it does not imply the sign of this two-sample negative inner product. The critical mathematical distinction from ordinary moment-matching blind spots is that **both** of the tested population coordinates are strictly nonzero, while their signed combination points away from the rejection tail.

## Limitations

This finding covers depth one with reference subsample size three, where the published statistic is a scalar negative product. It does not show the same phenomenon at higher depths or under alternate choices of subsampling and aggregation, and it does not rule out a separately designed two-sided or vector-norm test. The exact polynomial counterexample has a modest negative score, so the theorem does not quantify the finite sample size required to observe the limiting power failure. Originality comparisons cannot exclude all unpublished or unindexed analyses, and independent mathematical validation has not been performed.

## References

1. Brown, B., and Zhang, K. (2021). *The AUGUST Two-Sample Test: Powerful, Interpretable, and Fast*. arXiv:2109.14013, initial public version dated 2021-09-28. https://arxiv.org/abs/2109.14013
2. Brown, B., and Zhang, K. (2023). *AUGUST: An Interpretable, Resolution-based Two-sample Test*. *The New England Journal of Statistics in Data Science*, online 2023-12-15. https://doi.org/10.51387/23-NEJSDS54 ; https://nejsds.nestat.org/journal/NEJSDS/article/64/text
3. Brown, B., and Zhang, K. (2023). *Supplementary Material for AUGUST*, dated 2023-12-06, sections 0.2–0.4. https://nejsds.nestat.org/journal/NEJSDS/article/64/file/1257
4. Zhang, K. (2019). *BET on Independence*. *Journal of the American Statistical Association* 114, 1620–1637. https://doi.org/10.1080/01621459.2018.1537921
