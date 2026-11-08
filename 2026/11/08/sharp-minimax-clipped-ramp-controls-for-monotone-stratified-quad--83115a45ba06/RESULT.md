# Sharp minimax clipped-ramp controls for monotone stratified quadrature

## Finding

Fix an integer \(n\ge 2\). Partition \([0,1]\) into \(n\) equal strata and take one independent uniform point in each. Among **all deterministic, square-integrable, mean-zero control functions chosen separately for each stratum before the unknown integrand is observed**, the unique rule minimizing the worst-case variance over measurable nondecreasing \(f:[0,1]\to[0,1]\) subtracts the same clipped ramp in every stratum:

\[
 g_n(u)=\min\left\{\frac{1}{2n},\max\left\{-\frac{1}{2n},u-\frac12\right\}\right\},\quad 0\le u\le 1.
\]

The exact minimax mean-squared error (equal to variance) is

\[
\boxed{V_n^*=\frac{3n^2-3n+1}{12n^4}
=\frac{1}{4n^2}\left(1-\frac1n+\frac{1}{3n^2}\right).}
\]

The equality-attaining integrands are unit step functions whose jump lies in the central \(1/n\) portion of any stratum, in local coordinates. For \(n=2\), \(V_2^*=7/192\), compared with the uncorrected equal-strata worst-case variance \(1/16\). The improvement is \(5/12\), or about \(41.7\%\), in worst-case variance. The complete statement concerns this fixed stratified design and additive, integrand-independent controls, **not all randomized quadrature methods**.

## Assumptions and scope

Write \(U_1,\ldots,U_n\) for independent \(\mathrm{Unif}[0,1]\) variables and \(X_j=(j-1+U_j)/n\). Define \(\mathcal F\) to be every measurable nondecreasing \(f:[0,1]\to[0,1]\), with endpoint values immaterial for integrals and random samples. A permissible control is any \(g_j\in L^2([0,1])\) determined independently of \(f\), with \(\int_0^1g_j(u)\,du=0\). The resulting estimator is

\[
 \widehat I_g(f)=\frac1n\sum_{j=1}^n\bigl(f(X_j)-g_j(U_j)\bigr),\qquad I(f)=\int_0^1 f(x)\,dx.
\]

It is unbiased for every integrable \(f\). Controls can be unequal and nonlinear; no prior information on the particular integrand is used. Uniqueness is up to Lebesgue-almost-everywhere equality of each control. The sample positions and their independence are fixed.

## Proof

**1. Reduction to one jump.** Let \(H=L_0^2([0,1])\), with \(\|\cdot\|\) the uniform-law \(L^2\) norm, and define centered jump functions

\[
 h_t(u)=\mathbf 1_{\{u>t\}}-(1-t),\qquad 0\le t\le1,
 \qquad \|h_t\|^2=t(1-t).
\]

An arbitrary \(f\in\mathcal F\) has a nonnegative Stieltjes jump measure of total mass at most one: its random-sample values, up to additive constants and null-set choices, are mixtures of global unit steps and a constant. Centered estimator errors depend affinely on this mixture. The square of their \(L^2\) norm is convex, so Jensen's inequality bounds the risk by the largest risk of a global unit step (including constant functions as zero-jump steps). Conversely, every unit step belongs to \(\mathcal F\), hence this bound is sharp.

For a jump within stratum \(j\) at local position \(t\), the other \(f(X_i)\) are constants. Independence therefore gives

\[
 n^2\operatorname{Var}\widehat I_g(f)
 =\sum_{i=1}^n\|g_i\|^2+t(1-t)-2\langle h_t,g_j\rangle.
\]

Thus the exact global worst-case objective, multiplied by \(n^2\), is

\[
 \mathcal R(g_1,\ldots,g_n)
 =\sum_{i=1}^n\|g_i\|^2+
 \sup_{1\le j\le n,\,0\le t\le1}
 \bigl[t(1-t)-2\langle h_t,g_j\rangle\bigr]. \tag{1}
\]

**2. A universal lower bound.** Put

\[
 a_n=\frac12-\frac{1}{2n},\qquad b_n=\frac12+\frac{1}{2n}.
\]

In (1), average the supremum over an independently uniform index \(J\in\{1,\ldots,n\}\) and a local jump position \(T\sim\mathrm{Unif}[a_n,b_n]\). Let \(m(u)=\mathbb E h_T(u)\). A direct calculation using the uniform distribution function of \(T\) gives

\[
 m(u)=\begin{cases}
 -\frac12,&u<a_n,\\
 n(u-\frac12),&a_n\le u\le b_n,\\
 \frac12,&u>b_n.
 \end{cases}
 \qquad \mathbb E[T(1-T)]=\frac14-\frac{1}{12n^2},
 \qquad\|m\|^2=\frac14-\frac{1}{6n}.
\]

Completing squares in each \(g_j\) yields

\[
\begin{aligned}
 \mathcal R(g_1,\ldots,g_n)
 &\ge\sum_{j=1}^n\left\|g_j-\frac mn\right\|^2
  +\mathbb E[T(1-T)]-\frac{\|m\|^2}{n}\\
 &\ge\frac14-\frac{1}{4n}+\frac{1}{12n^2}.
\end{aligned} \tag{2}
\]

Equality in the second inequality requires **every** \(g_j=m/n=g_n\) almost everywhere. This already proves uniqueness should the lower bound be attained.

**3. Attainment and sharpness.** For \(g_n=m/n\), put \(B_n(t)=t(1-t)-2\langle h_t,g_n\rangle\). Since \(\int_0^1g_n=0\), \(\langle h_t,g_n\rangle=\int_t^1g_n(u)\,du\), whence, except at the two breakpoints,

\[
 B_n'(t)=1-2t+2g_n(t)
 \begin{cases}>0,&0\le t<a_n,\\=0,&a_n<t<b_n,\\<0,&b_n<t\le1.\end{cases}
\]

So the supremum in (1) is attained for **every** \(t\in[a_n,b_n]\); the averaging in step 2 is therefore tight. From

\[
 \|g_n\|^2=\frac{1}{4n^2}-\frac{1}{6n^3},\qquad
 B_n(1/2)=\frac14-\frac{1}{2n}+\frac{1}{4n^2},
\]

we obtain \(\mathcal R(g_n,\ldots,g_n)=1/4-1/(4n)+1/(12n^2)\). Division by \(n^2\) proves the stated expression. Strictness in (2) proves uniqueness even against all asymmetric nonlinear choices. The equality jumps can occur in any stratum with the specified central local position.

## Verification

The accompanying standalone Python program `verify_minimax.py`, requiring only the standard library, integrates the clipped piecewise-linear controls using exact rational arithmetic. It verifies zero means, squared norms, averaged lower bounds, endpoint and central jump risks, and dense rational-grid comparisons at eight values \(n=1,2,3,4,5,8,12,20\), as well as one two-jump monotone test. The recorded execution completed **3,217 exact rational assertions**. These finite checks are consistency tests, not the infinite-dimensional proof; that proof is the argument above. The \(n=1\) check reproduces the earlier known unstratified control-variate value \(1/12\) and is not claimed as new.

## Relationship to prior work

Basak, Bect and Vazquez (arXiv:2203.00423, first posted March 1, 2022) proved separate sharp worst-case risks \(1/(12n)\) for the global linear control-variate rule and \(1/(4n^2)\) for equal-length independent stratification, but their Theorems 3.1 and 4.1 do not optimize arbitrary predeclared **stratumwise controls** under both mechanisms simultaneously. The present result fixes their natural equal-strata design and solves that full additive-control minimax problem. Bayne and Chakraborty (arXiv:1804.01197) combined controls and stratified sampling for molecular integrals without a universal bounded-monotone minimax law. Chopin and Gerber (arXiv:2210.01554) instead construct higher-order estimators under smoothness assumptions, including derivative-based controls; their guarantees do not dominate the discontinuous-step worst-case class considered here. These comparisons do not establish exhaustive novelty across all numerical-integration literature.

## Limitations

No claim is made for adaptive choice of controls after observing integrand values, dependent points, uneven strata, multiple points per stratum, arbitrary nonlinear estimators, or multivariate integrands. The \(n^{-2}\) worst-case rate is not improved: the relative gain is \(1/n-1/(3n^2)\), largest at small \(n\). Even a complete proof and exhaustive optimization in the stated estimator class do not establish unrestricted randomized-integration minimaxity or independence from all earlier work.

## References

1. S. Basak, J. Bect and E. Vazquez, *Integration of bounded monotone functions: Revisiting the nonsequential case, with a focus on unbiased Monte Carlo (randomized) methods*, arXiv:2203.00423 (first version March 1, 2022). https://arxiv.org/abs/2203.00423
2. N. Chopin and M. Gerber, *Higher-order Monte Carlo through cubic stratification*, arXiv:2210.01554 (first version October 4, 2022). https://arxiv.org/abs/2210.01554
3. M. G. Bayne and A. Chakraborty, *Development of composite control-variate stratified sampling approach for efficient stochastic calculation of molecular integrals*, arXiv:1804.01197 (first version April 4, 2018). https://arxiv.org/abs/1804.01197
4. E. Novak, *Quadrature formulas for monotone functions*, Proc. Amer. Math. Soc. 115 (1992), 59–68, as cited in Basak–Bect–Vazquez; primary full text not independently inspected for this comparison.
