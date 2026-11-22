# The sharp least-variable degree-two Blaschke covering with one prescribed outermost zero

## Finding
For a degree-two finite Blaschke product \(B\), the boundary restriction is an orientation-preserving two-fold covering of the unit circle. Let its angular-speed variance be
\[\mathcal V(B)=\frac{1}{2\pi}\int_0^{2\pi}(|B'(e^{i\theta})|-2)^2\,d\theta.\]
Fix \(r\in(0,1)\) and require that the *maximum* modulus of the two zeros of \(B\), counted with multiplicity, equal \(r\). Then there is exactly one minimizing unordered zero configuration up to simultaneous rotation:
\[\{a,b\}=\{re^{i\phi},-s(r)e^{i\phi}\},\qquad \phi\in\mathbb R,\]
where \(s(r)\in(0,r)\) is the unique solution of
\[s(1+rs)^2=r(1-s^2)^2.\tag{1}\]
The sharp minimum is
\[\boxed{V_*(r)=2\left(\frac{r^2}{1-r^2}+\frac{s(r)^2}{1-s(r)^2}-\frac{2rs(r)}{1+rs(r)}\right).}\tag{2}\]
The radius \(s(r)\) is strictly increasing and has endpoint laws
\[s(r)=r-4r^3+32r^5+O(r^7)\quad(r\downarrow0),\qquad \lim_{r\uparrow1}s(r)=\frac{3-\sqrt5}{2}.\tag{3}\]
In particular, equal-modulus opposite zeros are never optimal at prescribed outermost modulus \(r\). Products are unique modulo rotation of the domain, an arbitrary unimodular constant, and interchange of the two zeros.

## Assumptions and scope
Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(\mathbb T=\partial\mathbb D\), and a degree-two finite Blaschke product means
\[B(z)=\eta\prod_{c\in\{a,b\}}\frac{z-c}{1-\overline c z},\quad |\eta|=1,\quad a,b\in\mathbb D,\]
with repeated zeros allowed. The two zeros are treated as an unordered multiset. No normalization of \(B(0)\), the critical point, or the boundary phase is imposed. The constraint is \(\max\{|a|,|b|\}=r\), not that both moduli equal \(r\). The result is an exact sharp minimization within this complete constrained degree-two family, not an assertion for degree three or higher.

## Proof
**Step 1 (boundary speed and Fourier identity).** Differentiating the argument of an individual Blaschke factor shows that on \(\mathbb T\),
\[|B'(e^{i\theta})|=P_a(\theta)+P_b(\theta),\quad P_c(\theta)=\frac{1-|c|^2}{|e^{i\theta}-c|^2}.\]
Each \(P_c\) has mean one and Fourier coefficients \(\widehat{P_c}(k)=\overline c^{\,k}\) for positive \(k\) with the convention \(\widehat f(k)=(2\pi)^{-1}\int f(\theta)e^{-ik\theta}d\theta\). Thus, by Parseval (absolute convergence holds since \(|a|,|b|<1\)),
\[\mathcal V(B)=2\sum_{k\ge1}|a^k+b^k|^2.\tag{4}\]
If \(a=r\) after rotation, \(b=t e^{i\psi}\), \(0\le t\le r\), geometric-series summation yields
\[\frac{\mathcal V}{2}=\frac{r^2}{1-r^2}+\frac{t^2}{1-t^2}+2\operatorname{Re}\frac{rt e^{i\psi}}{1-rt e^{i\psi}}.\tag{5}\]

**Step 2 (strict angular optimization).** For \(q=rt\in(0,1)\) and \(u=\cos\psi\),
\[\operatorname{Re}\frac{q e^{i\psi}}{1-q e^{i\psi}}=\frac{qu-q^2}{1-2qu+q^2},\qquad \frac{\partial}{\partial u}=\frac{q(1-q^2)}{(1-2qu+q^2)^2}>0.\]
Thus the unique minimizing relative phase for \(t>0\) is \(\psi=\pi\) (modulo \(2\pi\)). For \(t=0\) the phase is immaterial, and the next step excludes that endpoint.

**Step 3 (unique interior radial optimizer).** At the antipodal phase (5) becomes the smooth one-dimensional objective
\[F_r(t)=2\left(\frac{r^2}{1-r^2}+\frac{t^2}{1-t^2}-\frac{2rt}{1+rt}\right),\quad 0\le t\le r.\]
Its derivative is
\[F'_r(t)=4\left(\frac{t}{(1-t^2)^2}-\frac{r}{(1+rt)^2}\right).\tag{6}\]
Introduce \(H_r(t)=t(1+rt)^2/(1-t^2)^2\). This function is continuous and strictly increasing for \(0\le t\le r<1\) (every positive factor increases there), with \(H_r(0)=0\) and \(H_r(r)>r\). Therefore (6) changes sign exactly once, at the unique \(s(r)\in(0,r)\) satisfying (1), from negative to positive. It is the unique global minimizer. This also proves that no pair with one zero at the origin or equal radii can attain equality. Substituting into \(F_r\) proves (2) and the complete extremizer classification.

**Step 4 (endpoints and monotonicity).** The equation can be written \(s/(1-s^2)^2=r/(1+rs)^2\). Its left side strictly increases in \(s\); at fixed \(s<1\), the right side strictly increases with \(r\) because its derivative is \((1-rs)/(1+rs)^3>0\). Consequently \(s(r)\) increases strictly. Substituting \(s=r+Ar^3+Cr^5+O(r^7)\) into (1) and matching the coefficients of \(r^3,r^5\) yields \(A=-4\), \(C=32\); analyticity near \(r=0\) follows by the implicit-function theorem. For \(r\uparrow1\), monotonicity gives a limit \(L\in(0,1]\). The limiting relation is \(L(1+L)^2=(1-L^2)^2\). It excludes \(L=1\), and reduces to \(L=(1-L)^2\), whose unique solution in \((0,1)\) is \((3-\sqrt5)/2\). This proves (3).

## Verification
The auxiliary self-contained `checker.py` evaluates (1) by monotone bisection, tests the analytic Fourier and rational formulas against direct periodic quadrature, checks strict interior optimality against boundary configurations, checks the small-radius series and the golden-ratio endpoint, and reports only finite numerical diagnostics. These diagnostics are not used to establish the continuous-in-radius theorem; Steps 1–4 prove it.

## Relationship to prior work
Kovalev and Yang (2020, arXiv:2007.09760, Theorems 1.2 and 1.4) classify extremal *pointwise minimum and maximum* boundary derivative values for finite Blaschke coverings. That is an \(L^\infty\)-type extremal problem with a different constraint; it does not imply the fixed-zero-radius squared mean-speed variance minimizer in (1)–(3). Gluchoff and Hartmann (2013, Chapter 9, Theorems 7–10) compare interior Hardy means for zeros constrained to a *common radius*, and their quantity is not the boundary derivative-speed variance. Our allowed zero radii are unequal at equality, so the relevant assertion is not their equal-radius angular-ordering special case. Classical Poisson-kernel Fourier identities underpin (4), but neither identity alone determines the asymmetric global optimum.

## Limitations
The result applies only to degree-two Blaschke products and the squared boundary-speed variation under the exact outermost-zero-radius constraint. It does not classify higher-degree optimal zero configurations or give best possible pointwise-speed oscillation. Earlier literature concerning Poisson-kernel frame energy, optimal angular-speed distribution, or conformal covering distortion may offer equivalent formulations and therefore remains a historical-priority risk. Independent validation has not been performed.

## References
- L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760, first public 19 July 2020, https://arxiv.org/abs/2007.09760.
- A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative*, in *Blaschke Products and Their Applications*, Fields Institute Communications 65 (2013), DOI:10.1007/978-1-4614-5341-3_9, https://doi.org/10.1007/978-1-4614-5341-3_9.
- S. R. Garcia, J. Mashreghi and W. T. Ross, *Finite Blaschke products: a survey*, 2018, https://scholarship.richmond.edu/mathcs-faculty-publications/181/.
