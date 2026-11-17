# Exact Jacobi-weighted quadratic projection gain in total variation

## Finding
For every \(\alpha>-1\), let \(\mu_\alpha\) be the probability measure on \([-1,1]\) with density \(c_\alpha(1-t^2)^\alpha\), where
\[
c_\alpha=\frac{\Gamma(\alpha+3/2)}{\sqrt\pi\,\Gamma(\alpha+1)}.
\]
Let \(P_{2,\alpha}\) denote \(L^2(\mu_\alpha)\)-orthogonal projection onto real polynomials of degree at most two. For a real \(BV((-1,1))\) input, set \(V(f)=|Df|((-1,1))\). Write
\[
r=\alpha+1>0,\quad k=2r+3,\quad B=k^2+1-2r,
\quad z_+=\frac{B+\sqrt{B^2-4k^2(2r+1)}}{2k^2(2r+1)}.
\]
The exact, attained homogeneous bounded-variation operator norm is
\[
\boxed{\sup_{V(f)>0}\frac{V(P_{2,\alpha}f)}{V(f)}=\frac{(2r+1)c_\alpha}{2r}(1-z_+)^r\left(k\sqrt{z_+}+\frac1{k\sqrt{z_+}}\right).}
\]
Here \(0<z_+<1\), and each of the two one-jump functions \(f=\mathbf1_{[\sqrt{z_+},1]}\) and \(f=\mathbf1_{[-\sqrt{z_+},1]}\) attains the norm. The optimal jump lies strictly away from the center for every \(\alpha>-1\).

There are two distinct endpoint laws:
\[
\lim_{\alpha\downarrow-1}\|P_{2,\alpha}\|_{V\to V}=\frac53,
\qquad
\lim_{\alpha\to\infty}\frac{\|P_{2,\alpha}\|_{V\to V}}{\alpha+1}=\sqrt{\frac2{\pi e}}.
\]
The gain is not monotonic with the Jacobi parameter: its value at \(\alpha=-1/2\) is approximately \(1.4439635015\), below both its limiting value \(5/3\) at \(\alpha\downarrow-1\) and its value approximately \(1.6331820958\) at \(\alpha=0\). Consequently it has an interior global minimum, without any claim of uniqueness.

## Assumptions and scope
The input is a real-valued Lebesgue-a.e. class of bounded variation on the open interval, equivalently a signed finite distributional derivative measure plus an additive constant. Because the interval is bounded, such inputs belong to \(L^2(\mu_\alpha)\). Boundary point-values are irrelevant; neither their jumps nor their artificial boundary extensions contribute to \(V(f)\). The output is its continuous polynomial representative, with \(V(Pf)=\int_{-1}^1|(Pf)'(x)|\,dx\). The norm is homogeneous modulo constants; no restriction to monotone inputs is made. The weight and variation norms are different: the Jacobi weight is used for the projection but the output derivative is integrated against unweighted Lebesgue measure.

## Proof
**Orthogonal kernel and jump response.** Put \(q=2r+1\), \(T(t)=c_\alpha(1-t^2)^r\), and \(H_t=\mathbf1_{[t,1]}\). Symmetric beta integration gives \(\mathbb E[X^2]=1/q\) and \(\mathbb E[X^4]=3/[q(q+2)]\), so \(1,x,x^2-1/q\) is an orthogonal basis for the projected space. Integration by parts of the first and second centered moments of \(H_t\) gives
\[
(P_{2,\alpha}H_t)'(x)=\frac{qT(t)}{q-1}\bigl(1+(q+2)tx\bigr)
=K(1-t^2)^r(1+ktx),\quad K=\frac{(2r+1)c_\alpha}{2r}.
\]
These formulas hold for every \(-1<t<1\). Consequently its output variation depends only on \(s=|t|\) and is
\[
V(PH_t)=K(1-s^2)^r\Psi(ks),\quad
\Psi(a)=\int_{-1}^1|1+ax|\,dx=
\begin{cases}2,&0\le a\le1,\\a+a^{-1},&a>1.\end{cases}
\]

**Global maximization.** On \(0\le s\le1/k\), the expression is strictly decreasing away from \(s=0\). For \(s>1/k\), its derivative has the same sign as
\[
-k^2(2r+1)s^4+(k^2+1-2r)s^2-1.
\]
This is quadratic in \(s^2\), with positive discriminant \(4(4r^4+12r^3+17r^2+20r+16)\). To establish that the off-center branch strictly exceeds the centered height \(2K\), test \(s=k^{-1/2}\). The desired inequality is
\[
\left(1-\frac1k\right)^{(k-3)/2}\left(\sqrt k+\frac1{\sqrt k}\right)>2\qquad(k>3).
\]
Indeed \(\log(1-1/k)>-1/(k-1)\). With \(y=\sqrt k\), \(x=(y^2+1)/(2y)>1\), and \(\log x\ge2(x-1)/(x+1)\), the remaining sufficient inequality reduces after multiplication by positive denominators to
\[
(y+1)(3y^3-13y^2+15y-1)>0,\qquad y>\sqrt3.
\]
Writing \(u=y-2\), the cubic equals \(3u^3+5u^2-u+1\), which is at least \(1\) for \(\sqrt3-2\le u\le0\) and at least \(19/20\) for \(u\ge0\). Thus the centered height cannot maximize. The derivative polynomial has exactly two critical roots in \((1/k,1)\) (one minimum, one maximum), because the profile decreases at \(1/k\), exceeds its centered value in the interior, and tends to zero at \(1\). The larger root is \(z_+\); its square root is the unique positive global maximizing location. Reflection provides the negative maximizing location.

**Extension to arbitrary bounded variation.** Up to null sets, every real \(BV\) function admits a signed jump-integral representation \(f(u)=c+\int_{(-1,1)}H_t(u)\,d(Df)(t)\). Applying the polynomial projector and differentiating (the kernel and its derivative are bounded for each fixed \(r>0\)) gives
\[
(Pf)'(x)=\int_{(-1,1)}(PH_t)'(x)\,d(Df)(t).
\]
Fubini and the variation triangle inequality imply \(V(Pf)\le\sup_tV(PH_t)\,|Df|((-1,1))\). A jump at either maximizing location has \(V(f)=1\), so the inequality is sharp.

**Singular parameter limits.** As \(r\downarrow0\), the radical gives \(z_+=1-5r/2+O(r^2)\), the beta normalization gives \(K\to1/2\), and \((1-z_+)^r\to1\). Since \(k\sqrt{z_+}\to3\), the gain approaches \((3+1/3)/2=5/3\). As \(r\to\infty\), \(z_+=1/(2r)+O(r^{-2})\), \(K\sim\sqrt{r/\pi}\), \((1-z_+)^r\to e^{-1/2}\), and \(k\sqrt{z_+}\sim\sqrt{2r}\). Their product is \(r\sqrt{2/(\pi e)}(1+o(1))\). Continuity and the strict intermediate comparison prove the nonmonotonicity and existence of an interior minimizing parameter.

## Verification
The accompanying standalone `verify_jacobi_bv.py` checks the beta moments, the derivative stationary polynomial and discriminant symbolically, independently integrates weighted jump moments, exhausts dense jump grids over nine Jacobi parameters, tests randomized signed combinations of jumps, and checks both endpoint asymptotic regimes. Execute `python verify_jacobi_bv.py` with Python, SymPy, mpmath and their standard dependencies. Finite tests are not substitutes for the global proof above.

## Relationship to prior work
A published comparison on quadratic symmetric-Jacobi least-squares projection determines the sharp **pointwise range violation** of projected monotone inputs. Its exact reproducing kernel is compatible with the first step above, but its objective optimizes output values at selected points rather than total absolute derivative across the entire interval; the range theorem does not imply this variation norm or the weight-concentration asymptotics. An independently recorded discrete quadratic least-squares variation theorem has an unweighted infinite-grid limit equal to the special \(\alpha=0\) numerical value above; that special value is not asserted as new. The present claim instead determines the entire continuously weighted Jacobi family, including its singular weak-endpoint and high-concentration regimes. Kaber studies large-degree Gibbs overshoots of a fixed sign discontinuity; Kopotun and collaborators survey shape-preserving approximation, and Calderón–Urbina study Jacobi Abel-summability kernels. None of those inspected primary texts states the claimed sharp finite-degree total-variation norm.

## Limitations
Only symmetric Jacobi weights, polynomial degree exactly two, real scalar inputs and unweighted output total variation are treated. No higher-degree, nonsymmetric-weight, weighted-output variation or parameter-minimizer uniqueness result is claimed. Related older material may remain unindexed, so exhaustive historical priority is not established.

## References
- K. A. Kopotun, D. Leviatan, A. Prymak, and I. A. Shevchuk, *Uniform and Pointwise Shape Preserving Approximation by Algebraic Polynomials*, arXiv:1109.0968v1, public 2011-09-05. https://arxiv.org/abs/1109.0968
- S. M. Kaber, *The Gibbs Phenomenon for Jacobi Expansions*, Communications in Applied Analysis 10 (2006), 133–148. https://www.acadsol.eu/en/articles/10/2/3.pdf
- C. P. Calderón and W. Urbina, *On Abel Summability of Jacobi Polynomials Series, the Watson Kernel and Applications*, arXiv:1207.4524v1, public 2012-07-18. https://arxiv.org/abs/1207.4524
- *Sharp two-branch monotone range envelope for quadratic symmetric Jacobi projection*, public scientific record. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-two-branch-monotone-range-envelope-for-quadratic-symmetric--68d5f845db4a
