# A sharp finite-size critical layer for diagonal sections of \(\ell_p\)-balls

## Finding
For integers \(n\ge2\) and real \(p>2\), let \(B_p^n=\{x\in\mathbb R^n:\sum_{j=1}^n|x_j|^p\le1\}\). Its normalized central-section functional is
\[
A_{n,p}(a)=\frac{\operatorname{vol}_{n-1}(B_p^n\cap a^\perp)}{\operatorname{vol}_{n-1}(B_p^{n-1})}\qquad(a\in S^{n-1}).
\]
Let \(d_n=(1,\ldots,1)/\sqrt n\) and \(b_n=(1,1,0,\ldots,0)/\sqrt2\). The comparison value at \(b_n\) is exactly \(B(p)=A_{n,p}(b_n)=2^{1/2-1/p}\). Put
\[
G(p)=\sqrt{\frac{6\Gamma(1+1/p)^3}{\pi\Gamma(1+3/p)}},\qquad
\kappa(p)=\frac{\Gamma(5/p)\Gamma(1/p)}{\Gamma(3/p)^2}-3,
\]
and \(L(p)=\log(G(p)/B(p))\). Let \(p_0\in(26,27)\) be the unique root \(G(p_0)=B(p_0)\), the established Oleszkiewicz exponent.

**Theorem (pairwise finite-size crossover).** On a fixed open neighborhood of \(p_0\), with constants uniform in \(p\) and with a uniform first derivative in \(p\),
\[
A_{n,p}(d_n)=G(p)\left(1+\frac{\kappa(p)}{8n}+O(n^{-2})\right).
\]
There is a \(\delta>0\) such that for every sufficiently large integer \(n\) there is exactly one \(p_n\in(p_0-\delta,p_0+\delta)\) satisfying \(A_{n,p_n}(d_n)=A_{n,p_n}(b_n)\). The diagonal section is larger for \(p\in(p_0-\delta,p_n)\), and the two-coordinate section is larger for \(p\in(p_n,p_0+\delta)\). Moreover,
\[
\boxed{\quad p_n=p_0-\frac{C_*}{n}+O(n^{-2}),\qquad
C_*=\frac{\kappa(p_0)}{8L'(p_0)}=195.0172976114\ldots>0.\quad}
\]
Here \(p_0=26.2650319766\ldots\), \(L'(p_0)=-0.000759695564540\ldots\), and \(\kappa(p_0)=-1.18523020803\ldots\). In particular, for each fixed real \(s\), the near-critical scaling satisfies
\[
\lim_{n\to\infty}n\left[\frac{A_{n,p_0+s/n}(d_n)}{A_{n,p_0+s/n}(b_n)}-1\right]
=L'(p_0)s+\frac{\kappa(p_0)}8.
\]
The convergence is uniform when \(s\) ranges over any compact set. Thus the limiting sign switches at \(s=-C_*\).

## Assumptions and scope
The dimension \(n\) tends to infinity through positive integers. The comparison is **only between the two named central hyperplanes**; no claim that either is globally maximal among all hyperplanes for \(p<p_0\) is made. The existence, uniqueness, and sign comparison of \(p_n\) are asserted on a fixed neighborhood of \(p_0\) for all sufficiently large \(n\); they are not assertions for every finite dimension or for all \(p>2\). All volumes use Euclidean \((n-1)\)-dimensional measure, with the common normalization shown above. The first public motivating source is dated November 5, 2026 (UTC), and has primary MSC2020 classification 52A40.

## Proof
**1. Section density identity and exact competing value.** Define
\[
\beta_p=2\Gamma(1+1/p),\qquad f_p(x)=\exp(-\beta_p^p|x|^p).
\]
The normalization \(2\Gamma(1+1/p)/\beta_p=1\) makes \(f_p\) a probability density. For independent variables \(Y_j\) with density \(f_p\), the established section-density representation (Meyer–Pajor; see [1, Equation (10)]) states that \(A_{n,p}(a)\) equals the density at zero of \(\sum a_jY_j\). Hence \(A_{n,p}(d_n)\) is the central density of \(n^{-1/2}\sum_{j=1}^nY_j\). For the two-coordinate vector, a direct integral gives
\[
A_{n,p}(b_n)=\sqrt2\int_{\mathbb R}f_p(x)^2\,dx=2^{1/2-1/p}.
\]

**2. Variance and fourth cumulant.** For every \(r>-1\),
\[
\mathbb E|Y|^r=\frac{\Gamma((r+1)/p)}{\beta_p^r\Gamma(1/p)}.
\]
In particular its variance is
\[
\sigma_p^2=\frac{\Gamma(1+3/p)}{12\Gamma(1+1/p)^3},
\]
so the Gaussian limiting central density \((\sqrt{2\pi}\,\sigma_p)^{-1}\) equals \(G(p)\). The standardized fourth cumulant is the stated \(\kappa(p)\). Odd cumulants vanish by evenness.

**3. Uniform density Edgeworth estimate, including the parameter derivative.** Fix a compact interval \(I\subset(25,28)\) containing \(p_0\) in its interior. Let \(\phi_p(t)=\mathbb E e^{itY}\). Taylor expansion at zero, uniformly in \(p\in I\) and after one \(p\)-derivative, gives
\[
\log\phi_p(t)=-\frac{\sigma_p^2t^2}{2}
+\frac{\kappa(p)\sigma_p^4t^4}{24}+O_I(t^6).
\]
The branch is the real logarithm near zero. All required moments and their parameter derivatives are continuous and uniformly bounded because \(f_p\) and its parameter derivatives have superpolynomial tails. The density \(f_p\) and its parameter derivative have uniformly integrable second spatial derivatives, so Fourier integration by parts gives \(|\phi_p(t)|+|\partial_p\phi_p(t)|\le K_I(1+|t|)^{-2}\). For each fixed \(\eta>0\), the strict nonlattice inequality \(\sup_{p\in I,\,|t|\ge\eta}|\phi_p(t)|<1\) follows from continuity, absolute continuity of \(f_p\), and the uniform decay. These facts justify separating Fourier inversion into a small-frequency Gaussian region and an exponentially negligible complement, also after \(\partial_p\).

In the small-frequency region, inserting \(t/\sqrt n\) and raising the characteristic function to the \(n\)-th power yields
\[
\phi_p(t/\sqrt n)^n=e^{-\sigma_p^2t^2/2}
\left[1+\frac{\kappa(p)\sigma_p^4t^4}{24n}
+O_I\left(\frac{t^6+t^8}{n^2}\right)\right],
\]
with the error integrable against Gaussian weight and uniform in \(p\) and its first derivative (take, for example, \(|t|\le n^{1/12}\)). Fourier inversion and the Gaussian fourth moment \(\int t^4e^{-\sigma_p^2t^2/2}dt/\int e^{-\sigma_p^2t^2/2}dt=3/\sigma_p^4\) give
\[
A_{n,p}(d_n)=G(p)\left(1+\frac{\kappa(p)}{8n}+O_I(n^{-2})\right),
\]
with the same \(O_I(n^{-2})\) assertion after one derivative with respect to \(p\).

**4. Transversality and negative fourth cumulant.** Writing \(\psi=\Gamma'/\Gamma\), direct differentiation gives
\[
L'(p)=\frac{3[\psi(1+3/p)-\psi(1+1/p)]-2\log2}{2p^2}.
\]
The trigamma bound \(\psi'(x)\le\pi^2/6\) for \(x\ge1\) implies \(3[\psi(1+3/p)-\psi(1+1/p)]\le\pi^2/p<2\log2\) for \(p\in(25,28)\). Therefore \(L'(p)<0\) there. This independently verifies that the published critical root is simple.

For completeness, \(\kappa(p_0)<0\) does not depend on a numerical sign guess. Let \(q=1/p\le1/25\). The convergent expansion \(\log\Gamma(1+z)=-\gamma z+\sum_{k\ge2}(-1)^k\zeta(k)z^k/k\), valid for \(|z|<1\), yields
\[
\log(\kappa(p)+3)
\le\log(9/5)+2\zeta(2)\frac{(5q)^2}{1-5q}
\le\log(9/5)+\frac{\zeta(2)}{10}<\log3.
\]
Thus \(\kappa(p)<0\) for all \(p\ge25\). Here the middle upper bound uses \(|5^k+1-2\cdot3^k|\le4\cdot5^k\), \(\zeta(k)\le\zeta(2)\), and \(1/k\le1/2\) for \(k\ge2\).

**5. Unique finite-dimensional crossing and sharp coefficient.** Define \(H_n(p)=\log[A_{n,p}(d_n)/B(p)]\). On a fixed interval \(J=[p_0-\delta,p_0+\delta]\subset I\), the uniform derivative estimate gives
\[
H_n(p)=L(p)+\frac{\kappa(p)}{8n}+O_J(n^{-2}),\qquad
H_n'(p)=L'(p)+O_J(n^{-1}).
\]
The derivative is strictly negative on \(J\) for all sufficiently large \(n\), and \(H_n\) has opposite signs at its endpoints. The intermediate value theorem gives a unique root \(p_n\), with the claimed side inequalities. Substituting \(p=p_0+s/n\) in the preceding expression proves the uniform critical-window limit. Finally, Taylor expansion at \(p_0\) and \(H_n(p_n)=0\) give
\[
p_n-p_0=-\frac{\kappa(p_0)}{8L'(p_0)n}+O(n^{-2})=-\frac{C_*}{n}+O(n^{-2}),
\]
where the displayed exact formula defines \(C_*>0\). This proves the theorem.

## Verification
Run the accompanying standard-library verifier as `python3 verify.py`. It numerically reconstructs \(p_0\), \(L'(p_0)\), \(\kappa(p_0)\), and \(C_*\). It also independently evaluates the finite-dimensional central density by nested Simpson integration of the characteristic-function Fourier integral for several exponents and dimensions; in each case, the observed remainder agrees with the predicted \(O(n^{-2})\) scale. These finite numerical comparisons check arithmetic and normalization, not the infinite-dimensional error estimate, which is proved analytically in Step 3.

## Relationship to prior work
Brazitikos–Eskenazis [1] establish the dimension-free maximal-section threshold and the asymptotic diagonal behavior. Oleszkiewicz [2] introduced the critical comparison; König [3] proved a sufficient finite-dimensional condition \(n\ge650/(p_0-p)\) for \(5\le p<p_0\), explicitly noting that the constant is not optimal. König [4] analyzes a larger family of section normals through Fourier bounds. These are substantive antecedents. The present theorem gives the **sharp asymptotic shift of the pairwise finite-size crossing itself**, including its unique local crossing and uniform critical-window law; it does not simply replace the 650 sufficient bound uniformly in the full interval. Standard Edgeworth theory supplies the technique for extracting the correction, but it does not by itself identify the geometry-specific critical parameter or its exact crossing constant.

## Limitations
The crossover concerns \(d_n\) versus \(b_n\), not every possible hyperplane. No globally optimal hyperplane is asserted on the subcritical side, no exact finite-\(n\) crossing is supplied, and the theorem does not cover small \(n\) or parameter values remote from \(p_0\). The reported decimals are approximations to exact gamma/digamma expressions. Historical priority remains provisional: the original Oleszkiewicz chapter and some older Fourier-convexity literature were not exhaustively inspected for equivalent higher-order statements.

## References
[1] S. Brazitikos and A. Eskenazis, *The dimension-free threshold for maximal sections of* \(\ell_p\), arXiv:2611.07619v1, first posted November 5, 2026, https://arxiv.org/abs/2611.07619.

[2] K. Oleszkiewicz, *On p-pseudostable random variables, Rosenthal spaces and* \(\ell_p^n\) *ball slicing*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 1807 (2003), pp. 188–210, https://doi.org/10.1007/978-3-540-36428-3_16.

[3] H. König, *On hyperplane sections and projections in* \(\ell_p^n\), arXiv:2403.14456v1, March 21, 2024, https://arxiv.org/abs/2403.14456.

[4] H. König, *On maximal hyperplane sections of the unit ball of* \(\ell_p\) *for* \(p>2\), arXiv:2409.06432v1, September 10, 2024, https://arxiv.org/abs/2409.06432.
