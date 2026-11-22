# A sharp two-slip positivity frontier for odd Fourier quadrature

## Finding

Let \(n\ge5\) be odd, \(m=(n-1)/2\), \(h=2\pi/n\), and \(0\le\alpha<1/2\). Starting from the equispaced periodic nodes \(jh\), \(0\le j<n\), move only the adjacent nodes \(0\) and \(h\) *outward* to \(-\alpha h\) and \((1+\alpha)h\), leaving the other nodes unchanged. Let \(w_j\) be the unique quadrature weights exact for every complex trigonometric polynomial of degree at most \(m\), using the normalized circle integral.

Define, for \(0<a<1/2\),
\[
H_n(a)=\sin\!\left(\frac{\pi a}{n}\right)\left[\csc\!\left(\frac{\pi(1-a)}{n}\right)+\csc\!\left(\frac{\pi(1+a)}{n}\right)+\csc\!\left(\frac{\pi(2+a)}{n}\right)\right].
\]
There is precisely one \(\alpha_n\in(0,1/2)\) satisfying \(H_n(\alpha_n)=1\). **All** quadrature weights are strictly positive for \(0\le\alpha<\alpha_n\); at \(\alpha=\alpha_n\) exactly \(w_2\) and \(w_{n-1}\) are zero; for \(\alpha_n<\alpha<1/2\) both are negative. The critical radii are strictly increasing through odd \(n\), and
\[
\frac14<\alpha_n<\frac{\sqrt3-1}{2},\qquad
\alpha_n=\frac{\sqrt3-1}{2}-\frac{\sqrt3\pi^2}{24n^2}+O(n^{-4}).
\]
In particular the two locally displaced samples can remain positivity-safe substantially beyond the one-quarter full-grid conditioning frontier. The endpoint \(n=3\) satisfies the same formulas with \(\alpha_3=1/4\) and only one distinct zero weight, already consistent with known three-node positivity theory.

The result also gives all weights explicitly and the exact noise amplification, not just a sign test.

## Assumptions and scope

The nodes are \(\theta_0=-\alpha h\), \(\theta_1=(1+\alpha)h\) and \(\theta_j=jh\) for \(2\le j<n\), understood modulo \(2\pi\). The quadrature objective is \(I(f)=(2\pi)^{-1}\int_0^{2\pi}f(\theta)\,d\theta\). We require exactness on \(\mathcal T_m=\operatorname{span}_{\mathbb C}\{e^{ik\theta}:-m\le k\le m\}\). Because the nodes are distinct modulo \(2\pi\) for \(0\le\alpha<1/2\), the trigonometric Vandermonde matrix is nonsingular and the weights are uniquely defined. Their sum is one. The statement does not cover simultaneous perturbations of additional grid points or non-interpolatory oversampled formulas.

## Proof

**Step 1: exact weights by two-row Fourier replacement.** Set \(x=\pi/n\) and write \(D_m(t)=\sum_{k=-m}^m e^{ikt}=\sin(nt/2)/\sin(t/2)\). The original uniform-grid cardinal functions are \(\ell_j(t)=D_m(t-jh)/n\). Reflection about the angular midpoint \(h/2\) interchanges the displaced nodes and permutes the unchanged nodes. Consequently uniqueness forces \(w_0=w_1=t\).

Equate coefficients of the uniform nodal values in the old trapezoidal formula and in the perturbed formula. The coefficient of the old node zero yields \(t(A+B)=1\), where
\[
A=\frac{\sin(\pi\alpha)}{\sin(\alpha x)},\quad
B=-\frac{\sin(\pi\alpha)}{\sin((1+\alpha)x)},\quad
S=A+B>0.
\]
Thus \(w_0=w_1=1/S\). For each \(2\le j<n\) the coefficient identity gives
\[
w_j=\frac1n\left[1-\frac{(-1)^j\{\csc((j+\alpha)x)+\csc((j-1-\alpha)x)\}}{\csc(\alpha x)-\csc((1+\alpha)x)}\right]. \tag{1}
\]
This identity is direct from \(D_m(-\alpha h-jh)\) and \(D_m((1+\alpha)h-jh)\). The denominator in (1) is positive since \(0<\alpha x<(1+\alpha)x\le\pi/2\). At \(\alpha=0\) the continuous limit is \(w_j=1/n\).

**Step 2: identify the first two weights that can change sign.** All weights with odd \(j\ge3\) exceed \(1/n\). For even \(j\ge2\), define
\[
g_n(y)=\csc((y+\alpha)x)+\csc((y-1-\alpha)x),\quad 2\le y\le n-1.
\]
The function \(\csc(t)\) is strictly convex on \((0,\pi)\); both arguments lie there, so \(g_n\) is strictly convex. Reflection \(y\mapsto n+1-y\) preserves \(g_n\), hence \(g_n(2)=g_n(n-1)\) and \(g_n(y)<g_n(2)\) for strictly interior \(y\). Formula (1) implies that nonnegativity of *every* weight is equivalent to \(w_2\ge0\), with equality only at the reflected two boundary indices. After multiplying its inequality by \(\sin(\alpha x)>0\), this becomes \(H_n(\alpha)\le1\).

**Step 3: one and only one crossing.** The functions \(\sin(\alpha x)/\sin((1-\alpha)x)\) and \(\sin(\alpha x)/\sin((k+\alpha)x)\), \(k\in\{1,2\}\), are each strictly increasing in \(\alpha\in(0,1/2)\). For the latter, the derivative is exactly \(x\sin(kx)/\sin^2((k+\alpha)x)>0\); for the former, the numerator increases and the denominator decreases inside \((0,\pi/2)\). Thus \(H_n\) increases continuously from zero to a value strictly greater than one at \(\alpha\uparrow1/2\). A unique threshold \(\alpha_n\) follows, with the strict sign classifications above.

**Step 4: monotonicity in grid size and asymptotics.** For fixed \(a\in(0,1/2)\) each ratio \(\sin(ax)/\sin(bx)\), for \(b\in\{1-a,1+a,2+a\}\), increases strictly with \(x\in(0,\pi/3]\): the function \(t\cot t\) decreases on \((0,\pi)\), so \(\partial_x\log(\sin(ax)/\sin(bx))>0\). Hence decreasing \(x=\pi/n\) makes \(H_n(a)\) smaller and its unique unit crossing larger. At \(n=3\), trigonometric identities give \(\alpha_3=1/4\); therefore \(\alpha_n>1/4\) for odd \(n\ge5\). At \(n=5\), the radius is exactly \(\alpha_5=1/3\): at this displacement the three surviving nodes \(-h/3\), \(4h/3\), and \(3h\) are equally separated by \(2\pi/3\) modulo the circle, so the unique degree-two interpolatory rule puts weight \(1/3\) at each and zero at the other two. This geometric decimation verifies the crossing without numerical root solving. The pointwise limit as \(n\to\infty\) is
\[
H_\infty(a)=\frac a{1-a}+\frac a{1+a}+\frac a{2+a}.
\]
Its unique unit root is \(a_*=(\sqrt3-1)/2\). Since \(H_n>H_\infty\), the finite thresholds are smaller. Expanding \(\sin(ax)/\sin(bx)=(a/b)[1+(b^2-a^2)x^2/6+O(x^4)]\) uniformly near \(a_*\) and applying the implicit function theorem gives \(\alpha_n=a_*-\sqrt3\pi^2/(24n^2)+O(n^{-4})\).

**Step 5: exact independent-noise amplification.** Let sample noise be independent, centered, with common variance \(\sigma^2\). The variance contributed to the quadrature by noise is \(\sigma^2\sum_j w_j^2\). With
\[
Q=\frac{D_m((1+2\alpha)h)}n=-\frac{\sin(2\pi\alpha)}{n\sin((1+2\alpha)\pi/n)},
\]
one has the exact identity
\[
\sum_{j=0}^{n-1}w_j^2=\frac1n+\frac{4+2Q-4S/n}{S^2}. \tag{2}
\]
Indeed the two shifted cardinal coefficient vectors each have squared norm one; their inner product is \(Q\), and their summed inner product with the original two standard coordinate vectors is \(2S/n\). Subtracting the two shifted vectors from the two original coordinate vectors gives squared norm \(4+2Q-4S/n\). Its coefficient in the weights is \(1/S\), and its entries sum to zero, so it is orthogonal to the uniform weight vector. This proves (2). For every positive \(\alpha\), the correction is strictly positive because the new weights are not uniform. Thus (2) is an exact cost of keeping a local timing error without readjusting samples.

## Verification

Run `python verify.py` with `mpmath` installed. It reconstructs the Fourier moment system independently at 65-digit precision, compares its solution with (1), checks the exact norm identity (2), tests every weight's sign against the unique root, verifies the increasing threshold across odd sizes \(3\le n\le31\), and checks the asymptotic expansion numerically at larger sizes. The recorded run passed 411 consistency checks. These finite calculations are supplementary; the all-size and continuous-parameter claims are proved by the cardinal, convexity and monotonicity arguments above.

## Relationship to prior work

Austin and Trefethen (arXiv:1612.04018, 2016) analyze convergence of trigonometric interpolation and quadrature for general perturbed equispaced grids. Yu and Townsend (arXiv:2202.04722, 2022), especially Section 4, prove that alternating disturbances at many nodes can produce negative weights for arbitrarily small positive perturbation at sufficiently large grid size. The present setting instead modifies exactly two adjacent nodes and determines its precise, dimension-dependent nonnegativity radius. Neither cited general convergence statement nor the multi-node negative construction implies this localized exact frontier. Van den Bos and Sanderse (DOI:10.1016/j.cam.2021.113430, 2021) give a general polynomial-moment geometric framework for node additions/replacements; their Sections 2 and 4 do not give these odd Fourier-grid csc identities or the closed monotone threshold. Related three-node special cases of perturbation positivity are known; the novel claim is the uniform odd-size family \(n\ge5\), the increasing frontier and its limiting constant.

## Limitations

The result addresses equal-and-opposite outward motion of two *adjacent* nodes, not arbitrary two-node perturbations. It does not improve worst-case guarantees for perturbations at every node, and it does not assert error bounds for nonsmooth integrands. The noise identity assumes independent homoscedastic sample noise; it is not an accuracy statement for deterministic discretization error. An equivalent formulation under older barycentric, Fourier sampling or trigonometric moment literature is a residual publication-priority risk; no independent external validation is claimed.

## References

1. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018, first posted December 13, 2016. https://arxiv.org/abs/1612.04018
2. A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722, first posted February 9, 2022. https://arxiv.org/abs/2202.04722
3. L. M. M. van den Bos and B. Sanderse, *A geometrical interpretation of the addition of nodes to an interpolatory quadrature rule while preserving positive weights*, J. Comput. Appl. Math. 391 (2021), 113430. https://doi.org/10.1016/j.cam.2021.113430
