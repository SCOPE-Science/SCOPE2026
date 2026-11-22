# Two competing jet-sampling radii and a sharp Gamma boundary law for weighted Bergman monomials

## Finding

A value and its first complex derivative at one disk point carry a natural two-dimensional measurement space. For the normalized analytic monomial of degree \(n\ge2\) in every standard weighted Bergman space, the fraction of squared norm captured by the optimal two-jet approximation can be optimized over **all disk locations** by testing just **two explicit radii**. There are exactly two interior local maxima, with a strict local minimum between them; asymptotically the smaller radius is the uniquely optimal one.

Let \(\beta>1\) and \(a_n=(\beta)_n/n!\). The normalized space has kernel \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\) and orthonormal monomials \(e_n(z)=\sqrt{a_n}z^n\). At \(w\in\mathbb D\), set
\[
J_w=\operatorname{span}\{K_\beta(\cdot,w),\partial_{\overline w}K_\beta(\cdot,w)\},\qquad
P_{n,\beta}(x)=\|\operatorname{Proj}_{J_w}e_n\|^2,\quad x=|w|^2.
\]
For \(0<x<1\), the **exact projection fraction** is
\[
\boxed{P_{n,\beta}(x)=a_n x^{n-1}(1-x)^\beta
\left[x+\frac{(n-(n+\beta)x)^2}{\beta}\right].}
\]
The formula extends continuously to \(P_{n,\beta}(0)=0\). Write
\[
t_{n,\beta}=\sqrt{\frac{n(\beta+1)}{n+\beta}},\qquad
x_-=\frac{n-t_{n,\beta}}{n+\beta+1},\quad
x_0=\frac n{n+\beta},\quad
x_+=\frac{n+t_{n,\beta}}{n+\beta+1}.
\]
Then \(0<x_-<x_0<x_+<1\); the **only** interior extrema are strict local maxima at \(x_-,x_+\) and a strict local minimum at \(x_0\). Consequently
\[
\boxed{\sup_{w\in\mathbb D}\|\operatorname{Proj}_{J_w}e_n\|^2=
\max\{P_{n,\beta}(x_-),P_{n,\beta}(x_+)\}.}
\]
All maximizing nodes are precisely the rotations of the maximizing radius or radii in this formula. The residual squared error is one minus the displayed sharp fraction.

For every fixed \(\beta>1\), the smaller radius \(x_-\) is the **unique** optimal squared radius for all sufficiently large degrees. With \(c_\beta=\beta+1+\sqrt{\beta+1}\), its exact high-degree law is
\[
\boxed{\lim_{n\to\infty}n\sup_{w\in\mathbb D}\|\operatorname{Proj}_{J_w}e_n\|^2=
\frac{2c_\beta^{\beta+1}e^{-c_\beta}}{\Gamma(\beta+1)},\qquad
n(1-x_-)\longrightarrow c_\beta.}
\]
For ordinary Bergman space (\(\beta=2\)), the limiting sharp constant is \(0.933350239090664\ldots\).

## Assumptions and scope

For \(\alpha=\beta-2>-1\), use the normalized area measure \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\). Here \(\beta>1\), \(n\ge2\), \(w\in\mathbb D\), and both value and first-derivative representers at the **same** point are available with unrestricted complex projection coefficients. The value/derivative span is two-dimensional even at \(w=0\). The result is not a two-distinct-node optimization, nor a claim of simultaneous stable reconstruction for an entire polynomial band. The two-candidate finite-degree formula is exact without asserting that one particular candidate wins at every finite degree.

## Proof

**1. Exact Gram reduction.** Since
\[
K_\beta(z,w)=\sum_{j\ge0}a_jz^j\overline w^j,\quad
\sum_{j\ge0}a_jx^j=(1-x)^{-\beta},
\]
the value and first-derivative representatives, after a harmless nonzero radial scaling and common rotation of the coefficients, correspond to the sequences \((\sqrt{a_jx^j})_{j\ge0}\) and \((j\sqrt{a_jx^j})_{j\ge0}\). Normalize their squared coefficients to the negative-binomial probability distribution
\[
p_j=(1-x)^\beta a_jx^j,\qquad
\sum_jp_j=1,\quad
\mu=\frac{\beta x}{1-x},\quad
\sigma^2=\frac{\beta x}{(1-x)^2}>0.
\]
The two-by-two Gram matrix, divided by its common positive normalization, has entries \(1,\mu,\mu^2+\sigma^2\). Its determinant is \(\sigma^2\), so exact Gram inversion against the \(n\)-th coordinate gives
\[
P_{n,\beta}(x)=p_n\left(1+\frac{(n-\mu)^2}{\sigma^2}\right).
\]
Substituting the displayed mean and variance gives the boxed closed expression. When \(w=0\), both the value and derivative of \(e_n\) vanish for \(n\ge2\); hence the continuous extension to zero is correct. The other endpoint has limit zero since \(\beta>1\).

**2. Exact global critical-point census.** Direct differentiation, without cancelling any interior factor, gives
\[
\begin{aligned}
P'_{n,\beta}(x)=\frac{a_n}{\beta}x^{n-2}(1-x)^{\beta-1}
\bigl[n-(n+\beta)x\bigr]\\
\cdot\bigl[(n+\beta)(n+\beta+1)x^2-2n(n+\beta)x+n(n-1)\bigr].
\end{aligned}
\]
The quadratic discriminant is \(4n(n+\beta)(\beta+1)\); its roots are exactly \(x_-,x_+\). Both lie strictly between zero and one because \(n\ge2\), \(\beta>1\), and \(t_{n,\beta}<\min\{n,\beta+1\}\). The linear factor vanishes at \(x_0\). The inequalities \(x_-<x_0<x_+\) follow from \((n+\beta)t_{n,\beta}>n\). Thus the derivative signs, from left to right, are \(+,-,+,-\). In particular, the two local maxima are strict, there are no other interior critical points, and both endpoint values are zero. The exact global maximum is therefore the larger of the two explicitly evaluable critical values; every possible equality radius is listed.

**3. Two Gamma boundary peaks.** Fix \(\beta>1\). Uniformly for \(c\) in compact subsets of \((0,\infty)\), the Gamma ratio \(a_n\sim n^{\beta-1}/\Gamma(\beta)\) and the substitution \(x=1-c/n\) give
\[
nP_{n,\beta}(1-c/n)\longrightarrow
F_\beta(c)=\frac{c^\beta e^{-c}}{\Gamma(\beta)}
\left[1+\frac{(c-\beta)^2}{\beta}\right].
\]
The two finite-degree candidate points have \(n(1-x_-)\to c_+=\beta+1+\sqrt{\beta+1}\) and \(n(1-x_+)\to c_-=\beta+1-\sqrt{\beta+1}\). Both constants are positive. At these points the bracket equals \(2c_\pm/\beta\), so
\[
F_\beta(c_\pm)=\frac{2c_\pm^{\beta+1}e^{-c_\pm}}{\Gamma(\beta+1)}.
\]
Put \(t=\sqrt{\beta+1}>1\). Their ratio satisfies
\[
\log\frac{F_\beta(c_+)}{F_\beta(c_-)}
=t^2\log\frac{t+1}{t-1}-2t>0,
\]
because \(\log((1+u)/(1-u))>2u\) for every \(0<u<1\), applied to \(u=1/t\). The two finite-degree critical heights converge after multiplication by \(n\) to distinct limits, hence \(P_{n,\beta}(x_-)>P_{n,\beta}(x_+)\) for every sufficiently large \(n\). The exact two-candidate census now proves eventual unique radial optimality and the stated sharp Gamma constant, without assuming any uniformity in \(\beta\).

## Verification

`check_jet.py` is an independently formulated, Python-standard-library checker. For integer positive kernel powers and rational squared radii it computes the projection from the original value/derivative kernel Gram matrix using exact rational arithmetic, compares it with the closed formula, and verifies the factored derivative against direct differentiation. It also checks the critical-point ordering for nonintegral weights and samples the Gamma asymptotic. Running `python3 check_jet.py` passed **1010 finite assertions**. The analytic proof above, rather than these finite examples, establishes the theorem for every stated \(n\) and \(\beta\).

## Relationship to prior work

Aadi, Cruz, Hartmann and Kellay (arXiv:2202.07263v1, 15 February 2022) develop multiplicity-two and higher Bergman sampling through projection onto jet spaces, with general geometric covering/separation criteria; their inspected introduction, main theorems and local estimates do not optimize the capture of a single normalized monomial at one jet node or identify the two competing radii and limiting constant. Qu, Qian and Deng (arXiv:2006.03290v1, 5 June 2020) and Qian (arXiv:2201.07228v1, 18 January 2022) establish existence of best multiple-kernel approximations but not this explicit radius classification. Qu and Dang (published online 27 May 2019) introduce weighted Bergman adaptive approximation algorithms; accessible article material was limited to abstract and bibliographic entries, leaving a historical-priority risk.

The closest published Gaussian Fock result, *Two optimal radii for sparse first-jet sampling of Gaussian Fock monomials*, concerns Poisson rather than negative-binomial coefficients and a different radial limit. The published *Reentrant collision–separation transitions in equal-radius two-kernel Bergman approximation* considers two free evaluation nodes for a quadratic target, including their coincident limit at fixed radius, but neither its degree-two statements nor its angular phase diagram imply the present all-degree, all-weight two-jet optimum and Gamma constant. All such comparisons concern statements, not mere keyword matches.

## Limitations

The finite-degree formula is an exact maximum of two explicit critical values; the proof does not assert that the smaller radius wins at **every** finite degree. Eventual dominance is proved for each fixed weight, with no uniform cutoff in the weight. The result does not optimize unrestricted sets of two distinct nodes, higher jets, or a full multi-degree reconstruction problem. The highest-priority historical uncertainty concerns a possible earlier equivalent negative-binomial/Meixner Christoffel-function optimization and the inaccessible full text of the 2019 algorithm paper. Independent review is not implied by the present calculations.

## References

1. W. Qu and P. Dang, *Reproducing kernel approximation in weighted Bergman spaces: Algorithm and applications*, Mathematical Methods in the Applied Sciences **42** (2019), 4292–4304, first online 27 May 2019. DOI: https://doi.org/10.1002/mma.5648.
2. W. Qu, T. Qian and G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2006.03290v1, 5 June 2020, https://arxiv.org/abs/2006.03290.
3. T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2201.07228v1, 18 January 2022, https://arxiv.org/abs/2201.07228.
4. D. Aadi, C. Cruz, A. Hartmann and K. Kellay, *Multiple sampling and interpolation in Bergman spaces*, arXiv:2202.07263v1, 15 February 2022, https://arxiv.org/abs/2202.07263.
5. *Two optimal radii for sparse first-jet sampling of Gaussian Fock monomials*, available at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-optimal-radii-for-sparse-first-jet-sampling-of-gaussian-fock--004936b83577.
6. *Reentrant collision–separation transitions in equal-radius two-kernel Bergman approximation*, available at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-reentrant-collision-separation-transitions-in-equal-radius-two-k--221a576916eb.
