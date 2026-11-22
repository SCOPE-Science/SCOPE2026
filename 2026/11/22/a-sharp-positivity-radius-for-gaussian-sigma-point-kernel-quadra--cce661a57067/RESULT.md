# A sharp positivity radius for Gaussian sigma-point kernel quadrature

## Finding

Let \(d\ge2\) be an integer, let \(\ell,\tau,a>0\), let \(\nu=N(0,\tau^2I_d)\), and use the Gaussian kernel and the \(2d+1\) distinct sigma-point nodes
\[
k(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{2\ell^2}\right),\qquad
X_a=\{0,\pm a e_1,\ldots,\pm a e_d\}.
\]
The unconstrained, unregularized Gaussian-kernel quadrature weights solve \(K w=q\), with \(K_{ij}=k(x_i,x_j)\) and \(q_i=\int k(x_i,y)\,d\nu(y)\). Put
\[u=\frac{\ell^2}{\ell^2+\tau^2}\in(0,1),\quad
s=e^{-a^2/(2\ell^2)}\in(0,1),\quad q_0=u^{d/2}.
\]
All \(2d\) outer weights coincide, and their exact value and the central weight are
\[
w_{\mathrm{out}}=q_0\frac{s^u-s}{(1-s^2)^2}>0,\qquad
w_{\mathrm{center}}=q_0\left[1-dF_u(s)\right],\quad
F_u(s)=\frac{2s(s^u-s)}{(1-s^2)^2}.
\]
For each \(d\ge2\) and \(u\in(0,1)\), the equation \(dF_u(s)=1\) has exactly one root \(s_*(d,u)\in(0,1)\). With
\[
a_*(d,\ell,\tau)=\ell\sqrt{-2\log s_*(d,u)},
\]
**every** quadrature weight is nonnegative if and only if \(a\ge a_*\), and every weight is strictly positive if and only if \(a>a_*\). At equality the central weight alone is zero; for \(0<a<a_*\) it alone is negative. In particular, for fixed \(\ell,\tau>0\), the unique positivity boundary obeys the sharp high-dimensional scaling
\[
\frac{a_*^2}{2\ell^2}=\frac{\log(2d)}{1+u}+o(1)
\qquad(d\to\infty).
\]
The exact weight formulas also imply that if \(a,\tau,d\) are fixed and \(\ell\to\infty\), then
\[
w_{\mathrm{out}}\to\frac{\tau^2}{2a^2},\qquad
w_{\mathrm{center}}\to1-\frac{d\tau^2}{a^2},
\]
the usual polynomial moment-matching sigma-point weights. These are limits, not identities at finite bandwidth.

## Assumptions and scope

The Gaussian measure is isotropic with strictly positive variance; the design is exactly the origin and all positive/negative axis points at one common radius. The kernel is strictly positive definite on these distinct nodes, so the stated weights are unique. The Gaussian-process prior mean function is zero and there is **no** observation nugget, positivity projection, subsequent renormalization, or requirement that the rule integrate constants exactly. Radius and length scales are in the same Euclidean units. The result concerns the signs of the **quadrature weights**, not positive definiteness of \(K\) (which holds for every positive radius), nor globally optimal choice of nodes or integration error.

## Proof

1. Gaussian convolution gives \(q(0)=q_0\) and \(q(\pm a e_j)=q_0\exp[-a^2/(2(\ell^2+\tau^2))]=q_0s^u\). Signed coordinate permutations preserve the Gram matrix and kernel-mean vector. Positive definiteness makes the solution unique, hence one central weight and one common outer weight.

2. The Gram row for the origin has off-center entries \(s\). In any outer row, the diagonal is \(1\), the opposite node on that axis has affinity \(s^4\), and the other \(2(d-1)\) outer points have affinity \(s^2\). Thus the two distinct equations are
\[
w_{\mathrm{center}}+2dsw_{\mathrm{out}}=q_0,\quad
sw_{\mathrm{center}}+[1+s^4+2(d-1)s^2]w_{\mathrm{out}}=q_0s^u.
\]
Eliminating the central weight makes the outer coefficient \(1+s^4-2s^2=(1-s^2)^2>0\), proving both weight formulas and strict positivity of the outer weights.

3. To establish the **unique** boundary, put \(x=-\log s>0\) and \(\beta=1-u\in(0,1)\). Direct simplification gives
\[
F_u(e^{-x})=\frac{e^{\beta x}-1}{2\sinh^2 x},\quad
\frac{d}{dx}\log F_u(e^{-x})
=\frac{\beta}{1-e^{-\beta x}}-2\coth x.
\]
For every \(x>0\), the function \(t\mapsto t/(1-e^{-tx})\) is increasing for \(t>0\): its derivative has numerator \(1-(1+tx)e^{-tx}>0\). Therefore
\[
\frac{\beta}{1-e^{-\beta x}}\le\frac1{1-e^{-x}}<2\coth x.
\]
For the strict right inequality, let \(y=e^{-x}\in(0,1)\) and multiply the positive denominators; it becomes \(2(1+y^2)>1+y\), or \(1-y+2y^2>0\), which is immediate. Hence \(F_u(e^{-x})\) decreases strictly with \(x\), equivalently \(F_u(s)\) increases strictly with \(s\). Moreover \(F_u(s)\to0\) as \(s\downarrow0\), whereas \(F_u(e^{-x})\sim\beta/(2x)\to\infty\) as \(x\downarrow0\). This gives one and only one root and all three sign regimes.

4. At that root, \(dF_u(s_*)=1\) and \(d\to\infty\) imply \(s_*\to0\), while
\[
F_u(s)=2s^{1+u}\frac{1-s^{1-u}}{(1-s^2)^2}=2s^{1+u}(1+o(1))\quad(s\downarrow0).
\]
Thus \(s_*=(2d)^{-1/(1+u)}(1+o(1))\). Taking negative logarithms gives the displayed asymptotic for the squared critical radius, including the constant \(\log 2\) within the logarithm.

5. For the flat-kernel limit, expand \(s=1-a^2/(2\ell^2)+O(\ell^{-4})\), \(1-u=\tau^2/\ell^2+O(\ell^{-4})\), \(s^u-s=a^2\tau^2/(2\ell^4)+O(\ell^{-6})\), and \((1-s^2)^2=a^4/\ell^4+O(\ell^{-6})\). Substitute into the exact weights, using \(q_0\to1\).

## Verification

Run `python verify.py` with Python 3 and NumPy. The included script independently constructs full \((2d+1)\)-square Gaussian Gram systems, solves them numerically, and compares all weights with the closed formulas for dimensions \(2\) through \(11\) over 360 parameter tuples. It additionally checks bracketed sign changes, scalar boundary equations, monotonicity at sampled points, qualified high-dimension approximations, and the polynomial flat limit. It reports 3,774 passing assertions. Finite checks support but do not replace steps 1--5 of the all-parameter proof.

## Relationship to prior work

Särkkä et al. (2015) present Gaussian-process quadrature and the familiar \(2d+1\) sigma-point geometry, including a separate polynomial-kernel correspondence. Karvonen and Särkkä (2018, section 4.3, page A710) **already apply a Gaussian kernel and standard Gaussian measure to exactly this origin-plus-axis-point design and explicitly observe that the origin's weight turns negative in high dimensions**. Neither the geometry nor the sign phenomenon is claimed here. That paper provides a general symmetry-based reduction and an optimization expression for the radial generator, not the displayed necessary-and-sufficient positivity radius, proof of uniqueness, or sharp \(\sqrt{\log d}\) law. Karvonen, Kanagawa and Särkkä (2019) provide broader Bayesian quadrature weight-positivity context, with their main constructive positivity result for one-dimensional locally optimal designs; it does not determine the present multidimensional radius frontier. The present finding is a quantitative sharpening of a specific instability already identified in the literature, not a new general positivity theorem.

## Limitations

The phase boundary need not maximize worst-case integration accuracy; it only guarantees nonnegative signed weights for the specified design, Gaussian measure, and Gaussian kernel. Large \(\ell\) makes the full Gram matrix ill-conditioned numerically even though it remains mathematically nonsingular for finite \(\ell\). Other node patterns, anisotropic targets, unequal axis radii, normalized kernel quadratures, and positive-nugget regularization are not classified. The \(o(1)\) asymptotic is for fixed \(u\in(0,1)\) as \(d\to\infty\) and need not be uniform near \(u=1\). Independent validation and exhaustive bibliographic priority assessment have not been performed.

## References

1. Särkkä, S., Hartikainen, J., Svensson, L. and Sandblom, F. (2015). *On the relation between Gaussian process quadratures and sigma-point methods*. arXiv:1504.05994v1 (22 April 2015). https://arxiv.org/html/1504.05994v1
2. Karvonen, T. and Särkkä, S. (2018). *Fully Symmetric Kernel Quadrature*. SIAM Journal on Scientific Computing 40(2), A697--A720, especially section 4.3. https://doi.org/10.1137/17M1121779 ; lawful author PDF: https://tskarvone.github.io/pdf/KarvonenSarkka2018-fss.pdf
3. Karvonen, T., Kanagawa, M. and Särkkä, S. (2019). *On the positivity and magnitudes of Bayesian quadrature weights*. Statistics and Computing 29, 1317--1333. https://doi.org/10.1007/s11222-019-09901-0
