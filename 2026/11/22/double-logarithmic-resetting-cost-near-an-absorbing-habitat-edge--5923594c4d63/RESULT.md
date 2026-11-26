# Double-logarithmic resetting cost near an absorbing habitat edge

## Finding
Consider a one-dimensional growing population with diffusion coefficient \(D=1\), per-capita birth rate \(g=1\), absorption at both ends of \((-b,b)\), and Poisson relocation at rate \(r\) to one fixed interior site \(a\), where \(b=\pi/2\). The reset-free system is exactly at its linear persistence boundary. Write \(\delta=b-a\) and \(L=\log(1/\delta)\). For every sufficiently small positive \(\delta\) (in particular for \(0<\delta\le1/50\)), there is exactly one positive resetting intensity \(r_*(\delta)\) at which the principal linear growth rate vanishes. The rate is negative for \(0<r<r_*(\delta)\) and positive for \(r>r_*(\delta)\). Moreover,

\[
\sqrt{r_*(\delta)-1}=\frac2\delta\left[L+\log L+\log 2+o(1)\right],\qquad\delta\downarrow0.
\]

Thus \(r_*(\delta)\sim4\delta^{-2}\log^2(1/\delta)\). The second, \(\log\log(1/\delta)\), term is explicit and necessary for a vanishing absolute error inside the rescaled brackets. The result concerns the **recovery rate** required to offset resetting to a site very close to an absorbing habitat boundary; it does not claim a new closed form for the already known critical half-width at a fixed reset rate.

## Assumptions and scope
Fix \(b=\pi/2\), a reset point \(a=b-\delta\in(0,b)\), and \(r>0\). The backward mean-population generator on Dirichlet functions is
\[
(A_{r,a}f)(x)=f''(x)+(1-r)f(x)+rf(a),\quad -b<x<b,\quad f(-b)=f(b)=0.
\]
The **principal growth rate** \(\lambda(r,a)\) is the real spectral bound of this positive, eventually compact semigroup. It is simple, with a strictly positive interior eigenfunction. Positive, zero, and negative rates refer only to growth/decay of the linear mean-population semigroup, not to the stochastic probability of eternal survival.

The limiting position \(a\uparrow b\) is taken from inside the habitat. At \(r=0\), the unreset population is critical for every \(a\); the uniqueness assertion applies only to **positive** resetting intensities. The numeric sufficient neighborhood \(\delta\le1/50\) is chosen for a convenient explicit proof and is not asserted sharp.

## Proof
**1. Spectral sign criterion.** Let \(A_0=f''+(1-r)f\) on the same Dirichlet interval. Its spectral bound is exactly \(-r<0\), since the principal Dirichlet Laplacian eigenvalue is \(-1\). The positive rank-one addition \(rf(a)\) has one principal eigenvalue, characterized by
\[
1=rU_s(a),\qquad U_s=(s-A_0)^{-1}\mathbf 1,\qquad s>-r.
\]
Indeed, an eigenfunction must be a positive multiple of \(U_s\); the positive scalar \(rU_s(a)\) is continuous and strictly decreasing in \(s\), diverging as \(s\downarrow-r\) and tending to zero as \(s\to\infty\). Consequently, \(\operatorname{sign}\lambda(r,a)=\operatorname{sign}(rU_0(a)-1)\).

For \(0<r<1\), putting \(q=\sqrt{1-r}\), the Dirichlet solution of \(-U_0''+(r-1)U_0=1\) yields
\[
U_0(a)=\frac{\cos(qa)/\cos(qb)-1}{1-r}.
\]
Since \(0<qb<\pi/2\), negative spectral growth is equivalent to
\[
F_<(r,a):=\cos(qb)-r\cos(qa)>0.
\]
At \(r=1\), \(U_0(a)=(b^2-a^2)/2\). For \(r>1\), writing \(k=\sqrt{r-1}\),
\[
U_0(a)=\frac{1-\cosh(ka)/\cosh(kb)}{r-1};
\]
positive spectral growth is equivalent to
\[
H(k,a):=\log\cosh(kb)-\log\cosh(ka)-\log(1+k^2)>0.
\]
These formulas follow by solving the displayed second-order boundary-value problem; the denominator signs and the principal-resolvent branch are explicit.

**2. No lower-rate crossing near the boundary.** Assume \(0<\delta\le1/50\). For \(0<r<1\), elementary trigonometry gives \(\cos(qb)=\sin(b(1-q))\ge1-q=r/(1+q)\ge r/2\). Also, since \(0\le\sin z\le z\) for \(z\ge0\),
\[
0\le\cos(qa)-\cos(qb)=\int_a^b q\sin(qx)\,dx\le q^2 b\delta.
\]
Therefore
\[
F_<(r,a)=(1-r)\cos(qb)-r[\cos(qa)-\cos(qb)]
\ge r(1-r)(1/2-b\delta)>0,
\]
because \(b/50<1/2\). At \(r=1\), \((b^2-a^2)/2=b\delta-\delta^2/2<1\). Thus all \(0<r\le1\) have negative spectral growth.

**3. Exactly one higher-rate crossing.** Take \(K=10\). For \(k>0\), the mean-value integral and \(\tanh z\le z\) imply
\[
H(k,a)=\int_a^b k\tanh(kx)\,dx-\log(1+k^2)
\le b\delta k^2-\log(1+k^2).
\]
For \(0<k\le K\), concavity of the logarithm gives \(\log(1+k^2)\ge [\log(101)/100]k^2\); hence \(H<0\), since \(b/50<\log(101)/100\). For \(K\le k\le3/\delta\), the sharper bound \(\tanh z<1\) gives \(H<k\delta-\log(1+k^2)\le3-\log(101)<0\).

For \(k\ge3/\delta\), differentiate and use monotonicity of \(\tanh\):
\[
H'(k)=b\tanh(bk)-a\tanh(ak)-\frac{2k}{1+k^2}
>\delta\tanh(bk)-\frac2k
\ge\delta[\tanh(3b/\delta)-2/3]>0.
\]
(The strict last inequality holds throughout \(0<\delta\le1/50\).) Moreover, \(H(k,a)=k\delta-2\log k+o(1)\to+\infty\). Hence \(H\) has exactly one positive zero \(k_*(\delta)>3/\delta\). Its sign is negative below this zero and positive above, proving uniqueness and both growth-rate signs, with \(r_*=1+k_*^2\).

**4. Sharp singular inversion.** At this zero, the identity \(\cosh(k_*b)=(1+k_*^2)\cosh(k_*a)\) becomes
\[
k_*\delta=\log(1+k_*^2)+\eta_*,\quad
\eta_*:=\log(1+e^{-2k_*a})-\log(1+e^{-2k_*b}),\quad
0<\eta_*\le e^{-2k_*a}.
\]
Because \(k_*>3/\delta\) and \(a\to b>0\), \(\eta_*=o(1)\), and also \(\log(1+k_*^2)=2\log k_*+o(1)\). Put \(y=k_*\delta/2\); then \(y-\log y=L+\log2+o(1)\), with \(y\to\infty\). Inverting the strictly increasing function \(y-\log y\) on \((1,\infty)\) gives \(y=L+\log L+\log2+o(1)\), proving the claimed expansion. This is a genuine **near-boundary, high-reset-rate** limit; it does not replace the exact finite-parameter critical equation.

## Verification
Execute `python3 checker.py` using only the Python standard library. The script independently brackets the positive root of the hyperbolic criticality equation at several rational gap values, verifies sign changes and residuals, and prints the asymptotic scaled difference. These finite computations support the analytic derivation but are not substitutes for the all-parameter proof in the preceding section.

## Relationship to prior work
Menon, de Castro and Anteneodo (2025), §III.1, Eq. (9), Fig. 3 and Appendix B, derive the exact critical half-width and describe the positive crossover in the intermediate reset-position range \(\arccos(\pi/4)<|a|<\pi/2\), which includes the entire neighborhood considered here. Thus both the qualitative crossover and the specialized criticality equation \(\cosh(kb)=(1+k^2)\cosh(ka)\) are prior work. The contribution here is the explicit near-boundary asymptotic, including the \(\log L\) and \(\log 2\) terms inside the rescaled brackets, together with a self-contained proof identifying the unique positive root and its spectral sign on a quantified neighborhood. The earlier formula implicitly determines this asymptotic but does not state it. Standard Lambert-function asymptotics provide a recognizable inversion mechanism, not an independently claimed discovery. Prior results on randomized reset destinations and fixed second moments concern different optimization questions.

## Limitations
The analysis assumes an absorbing external region, constant diffusion and growth, exact Poisson resets to a single fixed point, and a habitat held at the reset-free critical half-width. It does not establish a unique positive crossover at every interior reset site, nor a finite-population extinction probability. The original paper's exact implicit critical equation means historical novelty of the derived singular inversion warrants independent priority review; no empirical effect size is inferred.

## References
1. L. Menon Jr., P. de Castro, and C. Anteneodo, *Critical habitat size of organisms diffusing with stochastic resetting*, arXiv:2505.03727v1 (first public 2025-05-06), https://arxiv.org/html/2505.03727v1, §III and Appendix B.
2. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, J. Phys. A 44 (2011), 435001, https://doi.org/10.1088/1751-8113/44/43/435001.
3. F. Johansson, *Computing the Lambert W function in arbitrary-precision complex interval arithmetic*, arXiv:1705.03266 (2017), https://arxiv.org/abs/1705.03266 (background on inversion branches, not needed for the self-contained proof).
