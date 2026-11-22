# Exact finite-sample skewness and its two-observation maximum for a uniformity statistic

## Finding

Let \(U_1,\ldots,U_n\) be independent uniform random variables on \((0,1)\), and let \(T_n\) be the simple-null characterisation-based uniformity statistic of Ebner, Liebenberg and Visagie, defined precisely below. For every integer \(n\geq1\), its **exact third cumulant** is

\[
\boxed{\kappa_3(T_n)=\mathbb E[(T_n-2/15)^3]=\frac{502883n^2+174043n-416895}{40540500n^2}.}
\]

With the exact second cumulant \(\kappa_2(T_n)=(218n-49)/(8100n)\), its ordinary standardized skewness is

\[
\boxed{\gamma_n=\frac{18(502883n^2+174043n-416895)}{1001\sqrt n\,(218n-49)^{3/2}}.}
\]

Among **all positive integer sample sizes**, the skewness is uniquely maximized at \(n=2\). It is strictly decreasing along the integers \(n=2,3,\ldots\), remains strictly larger than its limit at every such \(n\), and tends to

\[
\gamma_\infty=\frac{502883/40540500}{(109/4050)^{3/2}}
=2.8094456942\ldots.
\]

Numerically \(\gamma_1=2.1283031943\ldots\), \(\gamma_2=3.2446500578\ldots\), \(\gamma_3=3.2309965412\ldots\), and \(\gamma_{10}=2.9834073356\ldots\). Thus even at ten observations the exact standardized third moment is about \(6.19\%\) larger than its asymptotic counterpart. No claim about actual quantile-approximation error follows from skewness alone.

## Assumptions and scope

Fix an arbitrary integer \(n\ge1\). The null distribution is **fully specified and continuous**, so that \(U_1,\dots,U_n\) are independent \(\operatorname{Uniform}(0,1)\). Define

\[
H_t(u)=(2u-1)\mathbf 1_{\{u\ge t\}}-t(1-t),\quad
T_n=n\int_0^1\left(\frac1n\sum_{i=1}^n H_t(U_i)\right)^2\,dt.
\]

This is the statistic in equation (4) of Ebner, Liebenberg and Visagie (2021, 2022). There is **no estimated parameter** in the null, no growing-dimension regime, and no inference about tests after parameter fitting. The formulas hold for all positive integer \(n\), including the purely mathematical \(n=1\) case.

## Proof

**1. Canonical quadratic kernel.** Put \(J(u)=u^2/2-u^3/3\) and define

\[
h(u,v)=\int_0^1H_t(u)H_t(v)\,dt
=(2u-1)(2v-1)\min\{u,v\}-(2u-1)J(u)-(2v-1)J(v)+\frac1{30}.
\]

Since \(\mathbb E H_t(U)=0\) for each \(t\), it follows that \(\mathbb E[h(u,U)]=0\) for each \(u\in(0,1)\). Let \(a(u)=h(u,u)\), \(\mu=\mathbb Ea(U)=2/15\), and \(b(u)=a(u)-\mu\). Expanding the square gives

\[
T_n-\mu=\frac1n\left(\sum_{i=1}^n b(U_i)+2\sum_{1\le i<j\le n}h(U_i,U_j)\right).
\]

The kernel is bounded and all integrals and moments below exist.

**2. Connected index configurations.** Denote independent uniform variables by \(U,V,W\) and define five rational contractions:

\[
\begin{aligned}
c_0&=\mathbb E[b(U)^3]=\frac{86677}{13513500},\\
c_1&=\mathbb E[b(U)b(V)h(U,V)]=\frac{15931}{11583000},\\
c_2&=\mathbb E[b(U)h(U,V)^2]=\frac{280583}{121621500},\\
c_3&=\mathbb E[h(U,V)^3]=\frac{225809}{162162000},\\
c_4&=\mathbb E[h(U,V)h(U,W)h(V,W)]=\frac{502883}{324324000}.
\end{aligned}
\]

For reproducibility, on \(0<u<v\) the kernel is a polynomial with \(\min\{u,v\}=u\). Each two-variable expectation is an integral of polynomial terms over the two ordered regions. For the last contraction integrate the polynomial product over all six orderings, or six times over \(0<u<v<w<1\). Every rational is evaluated exactly by the included independent, standard-library polynomial checker; no numerical integration is used.

Expand the cube of the centered quadratic kernel representation. Since \(\mathbb E[h(u,U)]=0\), any index pattern with an off-diagonal edge incident to an otherwise unpaired vertex vanishes. The only surviving patterns are the triple diagonal, two diagonals and one pair, one diagonal with a repeated pair, the triple repeated pair, and the triangle of three distinct pairs. Their ordered multiplicities give

\[
\mathbb E[(T_n-\mu)^3]
=\frac{n c_0+12\binom n2c_1+24\binom n2c_2+8\binom n2c_3+48\binom n3c_4}{n^3}.
\]

Substitution and exact rational simplification yield the stated cubic-cumulant formula. In particular the constant term as \(n\to\infty\) is \(502883/40540500\), matching the asymptotic third cumulant calculated in the original paper.

**3. Variance, normalization, and strict integer maximum.** The same canonical decomposition gives

\[
\operatorname{Var}(T_n)=\frac1n\operatorname{Var}(a(U))+
\frac{2(n-1)}n\mathbb E[h(U,V)^2]
=\frac1n\frac{169}{8100}+
\frac{2(n-1)}n\frac{109}{8100}
=\frac{218n-49}{8100n}.
\]

Dividing the exact third moment by the \(3/2\)-power of this variance yields \(\gamma_n\). Extend its displayed expression to real \(x\ge1\). Direct differentiation and simplification give

\[
\gamma'(x)=
-\frac{9(149806549x^2-355004333x+20427855)}{1001x^{3/2}(218x-49)^{5/2}}.
\]

The numerator polynomial and its derivative are positive at \(x=3\), and its second derivative is positive everywhere. Hence \(\gamma'(x)<0\) for every \(x\ge3\). The remaining discrete comparison is exact: 

\[
\gamma_2^2-\gamma_3^2=
\frac{14038148030846784406}{158775012314273730375}>0.
\]

Also \(\gamma_2>\gamma_1>0\) by direct substitution. This proves unique maximization at \(n=2\) and strict integer decrease for all \(n\ge2\). Because this decreasing sequence converges to its stated limit, every finite \(\gamma_n\) with \(n\ge2\) strictly exceeds that limit. The \(n=1\) value is below it; it is not hidden in the monotonicity statement.

## Verification

Run `python3 check_moments.py` from the directory containing this result and its checker. The checker requires only Python's standard library. It independently represents the kernel as sparse rational-coefficient polynomials; evaluates all five contractions by integrating monomials over ordered simplices; compares the mean, variance and the closed cubic formula; tests integer sample sizes through 150; and checks the rational skewness inequalities and derivative certificate. It prints a PASS banner and the five exact fractions. A separate Monte Carlo sanity comparison at sample sizes 1, 2, 3, 5 and 10 agreed within expected random error; simulation is not proof.

The ordered-simplex integral used by the checker is

\[
\int_{0<u<v<w<1}u^av^bw^c\,du\,dv\,dw
=\frac{1}{(a+1)(a+b+2)(a+b+c+3)}
\]

for nonnegative integers \(a,b,c\). The analogous two-variable identity is \(1/((a+1)(a+b+2))\), providing directly inspectable arithmetic certificates.

## Relationship to prior work

Ebner, Liebenberg and Visagie defined the same statistic and computed the first four **limiting** null cumulants, including \(\kappa_{3,\infty}=502883/40540500\), as inputs to a Pearson-system approximation. Their preprint contains asymptotic theory, simulated finite-sample quantiles and power; it does not give the exact third moment for each finite \(n\), nor the sample-size-two skewness maximum. The published journal abstract confirms this focus, but its full version was not examined.

A separate exact second-order dependence calculation for this same statistic establishes its finite-sample variance and covariances with classical quadratic empirical-process statistics. That coverage supplies the variance displayed here, not the new cubic moment, its five contractions, or the skewness extremum. Generic canonical \(V\)-statistic moment expansions supply a method, not these evaluated constants and all-size inequalities.

## Limitations

The result concerns the known-continuous-null statistic only. It does not assert better achieved type-I error, quantified tail-approximation improvements, finite-sample critical values, an exact fourth cumulant, or asymptotics after fitting parameters. The exact third moment is a mathematical shape correction; using it in a calibrated distributional approximation requires additional work. Novelty is assessed against accessible material and remains subject to independent literature review, particularly for older generic moment calculations and versions of the journal article not fully inspected.

## References

1. Ebner, B., Liebenberg, S. C., and Visagie, I. J. H. (2021). *A new omnibus test of fit based on a characterisation of the uniform distribution*. arXiv:2108.06391v1, first public 13 August 2021. https://arxiv.org/abs/2108.06391
2. Ebner, B., Liebenberg, S. C., and Visagie, I. J. H. (2022). *A new omnibus test of fit based on a characterization of the uniform distribution*. *Statistics* 56(6), 1364–1384. https://doi.org/10.1080/02331888.2022.2133121
