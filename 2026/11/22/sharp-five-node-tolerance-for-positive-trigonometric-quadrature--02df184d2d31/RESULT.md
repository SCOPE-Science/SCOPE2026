# Sharp five-node tolerance for positive trigonometric quadrature

## Finding

Let \(h=2\pi/5\), and perturb the five equally spaced circular nodes by
\[
\theta_j=h(j+\delta_j),\qquad j=0,1,2,3,4,\qquad |\delta_j|\le\alpha<1/2.
\]
The unique real weights \(w_j\) that exactly integrate every trigonometric polynomial of degree at most two against normalized circular Lebesgue measure satisfy
\[
\sum_{j=0}^{4}w_j e^{\mathrm i k\theta_j}=\begin{cases}1,&k=0,\\0,&k=\pm1,\pm2.\end{cases}
\]
Define the explicit constant
\[
\alpha_*:=\frac12\left(\frac5\pi\arccos\sqrt{\frac{\cos(\pi/5)}2}-1\right)
=0.2014594224605106\ldots.
\]
For **every** admissible perturbation, all five weights are strictly positive if and only if \(0\le\alpha<\alpha_*\), and they are all nonnegative if and only if \(0\le\alpha\le\alpha_*\). At the critical radius, the perturbation
\[
(\delta_0,\delta_1,\delta_2,\delta_3,\delta_4)=(-\alpha_*,\alpha_*,0,-\alpha_*,\alpha_*)
\]
produces \(w_2=0\). For every \(\alpha>\alpha_*\) with \(\alpha<1/2\), an admissible perturbation yields \(w_2<0\). This is a worst-configuration, not a probabilistic, statement.

## Assumptions and scope

The underlying measure is \(\mathrm d\theta/(2\pi)\) on the circle. Angles are interpreted modulo \(2\pi\); for proof purposes use the ordered lifts \(\theta_0<\cdots<\theta_4<\theta_0+2\pi\), guaranteed for \(\alpha<1/2\). The approximation space is exactly the real five-dimensional span of \(1,\cos\theta,\sin\theta,\cos2\theta,\sin2\theta\). The five weights are interpolatory and uniquely determined; there is no freedom to select another five-node exact weight vector. All claims are in exact arithmetic. The sharpness construction can be cyclically rotated to target any chosen node.

## Proof

**Uniqueness and a sign formula.** Write \(z_j=e^{\mathrm i\theta_j}\). The trigonometric Vandermonde system for frequencies \(-2,-1,0,1,2\) becomes an ordinary Vandermonde system after multiplying each column by \(z_j^2\). Its determinant is nonzero because the five nodes are distinct. For the central index \(j=2\), the corresponding Laurent cardinal function has constant Fourier coefficient
\[
w_2=\frac{z_2^2 e_2(z_0,z_1,z_3,z_4)}{\prod_{\ell\ne2}(z_2-z_\ell)},
\]
where \(e_2\) is the second elementary symmetric polynomial on the four indicated variables. Introduce
\[
x=\frac{\theta_1-\theta_0}{2},\qquad y=\frac{\theta_4-\theta_3}{2},\qquad
\Delta=\frac{\theta_3+\theta_4-\theta_0-\theta_1}{2}.
\]
Pairing the six terms in \(e_2\) gives
\[
e_2=2e^{\frac{\mathrm i}2(\theta_0+\theta_1+\theta_3+\theta_4)}F,
\qquad F=\cos\Delta+2\cos x\cos y.
\]
Using \(e^{\mathrm ia}-e^{\mathrm ib}=2\mathrm i e^{\mathrm i(a+b)/2}\sin((a-b)/2)\), the denominator is \(16z_2^2e^{\frac{\mathrm i}2(\theta_0+\theta_1+\theta_3+\theta_4)}P\), where
\[
P=\prod_{\ell\ne2}\sin\frac{\theta_2-\theta_\ell}{2}>0.
\]
There are exactly two positive and two negative factors in \(P\). Thus \(w_2=F/(8P)\) and \(\operatorname{sign}w_2=\operatorname{sign}F\). In particular the sign of this weight does not depend on the displacement of its own node. Cyclic rotation yields the same formula for every target index.

**Exact minimization over the perturbation box.** It suffices first to consider \(0\le a\le1/4\). Let \(u_j=\delta_j\). Direct substitution gives
\[
x=\frac\pi5(1+u_1-u_0),\quad y=\frac\pi5(1+u_4-u_3),\quad
\Delta=\frac\pi5(6+u_3+u_4-u_0-u_1).
\]
Throughout this box, \(\pi\le\Delta\le7\pi/5\), and \(0<x,y\le3\pi/10\); in particular \(\sin\Delta\le0\), \(\sin x,\sin y,\cos x,\cos y>0\). Consequently,
\[
\frac{5}{\pi}\frac{\partial F}{\partial u_1}=\sin\Delta-2\sin x\cos y<0,
\qquad
\frac{5}{\pi}\frac{\partial F}{\partial u_3}=-\sin\Delta+2\cos x\sin y>0.
\]
Every minimizer therefore has \(u_1=a\) and \(u_3=-a\). Under these two constraints,
\[
\frac\pi5\le x,y\le\frac{(1+2a)\pi}5\le\frac{3\pi}{10},\qquad
\pi\le\Delta\le\frac{6\pi}5.
\]
Therefore \(-\sin\Delta\le\sin(\pi/5)\), while
\[
2\sin x\cos y\ge 2\sin(\pi/5)\cos(3\pi/10)
=2\sin^2(\pi/5)>\sin(\pi/5),
\]
and the same strict lower bound holds for \(2\cos x\sin y\). Hence
\[
\frac5\pi\frac{\partial F}{\partial u_0}=\sin\Delta+2\sin x\cos y>0,
\qquad
\frac5\pi\frac{\partial F}{\partial u_4}=-\sin\Delta-2\cos x\sin y<0.
\]
It follows that the **unique** minimizing choice of the four other displacements is
\(u_0=-a,\ u_1=a,\ u_3=-a,\ u_4=a\), and
\[
\min_{|u_\ell|\le a,\,\ell\ne2}F
=2\cos^2\frac{(1+2a)\pi}5-\cos\frac\pi5.
\]
This minimum decreases strictly as \(a\) increases in \([0,1/4]\), starts positive at \(a=0\), and crosses zero precisely at the displayed \(\alpha_*\in(0,1/4)\). This proves strict positivity for \(a<\alpha_*\) and nonnegativity at \(a=\alpha_*\), uniformly in every configuration. At equality, \(F=0\), hence \(w_2=0\). For any \(\alpha>\alpha_*\), choose \(a\in(\alpha_*,\min\{\alpha,1/4\})\) and the same four-coordinate extremizer, obtaining \(F<0\) and hence a negative exact weight. Cyclic symmetry gives the five-weight assertion.

## Verification

The companion standalone Python script `verify.py` computes Fourier-interpolatory weights by complex Gaussian elimination and independently evaluates the four-point sign formula. It checks the exactness equations, the boundary configuration, a negative-weight witness, and reproducible randomly sampled configurations across seven jitter radii. Run `python verify.py` alongside this document. All finite-precision tolerance checks are sanity checks; universal positivity and the exact boundary follow only from the above analytic argument.

## Relationship to prior work

Neumayer, Schäfer and Ullrich establish existence of positive exact quadrature with sufficiently many random samples, including trigonometric applications, but their random oversampling conclusions do not give the exact five-node deterministic perturbation threshold. Yu and Townsend investigate general perturbed periodic grids and construct negative weights for sufficiently large numbers of nodes at every nonzero relative jitter; that statement neither implies nor contradicts a positive fixed-five-node radius, and their general sufficient estimates do not give this sharp minimax constant. Peherstorfer gives broad structural descriptions of positive trigonometric quadrature, without deriving the sharp componentwise five-grid displacement threshold here. The exact sign reduction and four-variable global minimization are the distinguishing claims. Earlier equivalent results in unindexed or differently formulated literature remain possible.

## Limitations

No analogous sharp radius is claimed for seven or more Fourier nodes, or for multidimensional grids, arbitrary nonequispaced reference nodes, floating-point computed weights, noisy observations, or other polynomial degrees. The positivity classification concerns the unique weights exact for all harmonics of degree at most two, not an arbitrarily chosen positive rule using fewer moments or additional nodes.

## References

1. S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (first posted 2026-10-23), https://arxiv.org/html/2610.32699v1 .
2. A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722 (first posted 2022-02-09), https://arxiv.org/abs/2202.04722 .
3. F. Peherstorfer, *Positive trigonometric quadrature formulas and quadrature on the unit circle*, arXiv:1001.2451 (first posted 2010-01-14), https://arxiv.org/abs/1001.2451 .
