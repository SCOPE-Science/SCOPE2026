# Sharp orthogonal design and angular bifurcation for paired squeezed-Gaussian ambiguity windows

## Finding

For \(s>1\), define the unit-norm squeezed Gaussian \(g_s(t)=(2s)^{1/4}e^{-\pi s t^2}\). Let \(g_{s,\theta}\) denote a fractional-Fourier rotation of this window whose ambiguity modulus has principal axes rotated by \(\theta\). For \(R>0\), \(s_1,s_2>1\), and weights \(w_1,w_2>0\), define the worst-case two-window ambiguity floor on the closed disk
\[
\mathfrak m_R(\theta_1,\theta_2)=\min_{x^2+\xi^2\le R^2}\left(w_1|\mathcal A g_{s_1,\theta_1}(x,\xi)|+w_2|\mathcal A g_{s_2,\theta_2}(x,\xi)|\right),
\]
with \(\mathcal A g(x,\xi)=\int_{\mathbb R}g(t+x/2)\overline{g(t-x/2)}e^{-2\pi i\xi t}\,dt\). Put
\[
 c_j=\frac{\pi R^2}{4}(s_j+s_j^{-1}),\quad d_j=\frac{\pi R^2}{4}(s_j-s_j^{-1}),\quad A_j=w_j e^{-c_j},\quad
 x_* = \left[\frac{\log(A_2d_2/(A_1d_1))}{d_1+d_2}\right]_{[-1,1]},
\]
where brackets mean clipping to the indicated closed interval. Then **the only maximizing relative orientations** modulo \(\pi\) satisfy
\[
 \boxed{\theta_2-\theta_1\equiv\pi/2\pmod\pi},
\]
and the exact sharp floor is
\[
\boxed{\max_{\theta_1,\theta_2}\mathfrak m_R(\theta_1,\theta_2)=A_1e^{d_1x_*}+A_2e^{-d_2x_*}.}
\]
This is an equality classification for all positive weights and all unequal or equal nonisotropic Gaussian squeezings, not just a suggested angular discretization.

**Angular bifurcation.** In the equal-weight case \(w_1=w_2\) with \(s_1>s_2>1\), write \(\eta_j=s_j-s_j^{-1}\) and
\[
 R_0^2=\frac{2\log(\eta_1/\eta_2)}{\pi(s_1-s_2^{-1})},\qquad
 x_\infty=\frac{s_1+s_1^{-1}-s_2-s_2^{-1}}{\eta_1+\eta_2}\in(0,1).
\]
For \(0<R\le R_0\) the worst directions form one unoriented line, namely the first Gaussian's high-decay axis \(\varphi\equiv\theta_1\pmod\pi\), and \(x_*=-1\). For \(R>R_0\), there are exactly two distinct unoriented worst directions,
\[
 \varphi-\theta_1\equiv\pm\frac12\arccos(-x_*(R))\pmod\pi,
 \quad x_*(R)=x_\infty-(1+x_\infty)\frac{R_0^2}{R^2}.
\]
Thus the splitting is of square-root order in \(R^2-R_0^2\). The two directions pass through \(\pm\pi/4\) exactly when \(R^2=R_0^2(1+x_\infty)/x_\infty\). These formulas give an exact geometric change in the frequency directions that control the optimal direct-inversion denominator.

## Assumptions and scope

All spaces are over \(\mathbb R\); \(s_j>1\) means genuine squeezing and \(R,w_j>0\). The ambiguity convention and the Gaussian normalization are exactly those above. A rotation parameter is only defined modulo \(\pi\) for a centered elliptical ambiguity modulus. The optimized quantity is the *positive weighted sum of ambiguity magnitudes* on a fixed closed Euclidean disk, not the sum of squares, a stochastic noise covariance, a sampled-STFT frame bound, or the entire nonlinear phase-retrieval condition number. The weights are fixed, not optimized. The statement makes no uniform assertion when a squeezing approaches \(1\), when \(R\downarrow0\), or when the number of windows exceeds two.

## Proof

**1. Gaussian identity and radial reduction.** Completing squares in the defining integral gives
\[
 |\mathcal A g_{s,\theta}(r\cos\varphi,r\sin\varphi)|
 =\exp\!\left[-\frac{\pi r^2}{2}\left(s\cos^2(\varphi-\theta)+s^{-1}\sin^2(\varphi-\theta)\right)\right].
\]
It is strictly decreasing in \(r>0\) at every fixed \(\varphi\). Hence the disk minimum is always on \(r=R\). Using \(\cos^2u=(1+\cos2u)/2\), rotating the angular origin, and writing \(t=2(\varphi-\theta_1)+\pi\), \(\beta=2(\theta_2-\theta_1)\), the boundary floor is
\[
 M(\beta)=\min_{t\in[0,2\pi]}\{A_1 e^{d_1\cos t}+A_2e^{d_2\cos(t-\beta)}\}.
\]

**2. Exact two-bump polarization lemma.** For arbitrary \(A,B,a,b>0\), define \(F_\beta(t)=Ae^{a\cos t}+Be^{b\cos(t-\beta)}\). At \(\beta=\pi\), let \(x=\cos t\), so the minimum equals \(\min_{-1\le x\le1}(Ae^{ax}+Be^{-bx})\). Its second derivative is strictly positive and its derivative vanishes only at \(\log(Bb/(Aa))/(a+b)\). Therefore its unique minimizing cosine is the clipped value \(x_*\) above.

To prove *global* optimality rather than only stationary optimality, exchange the labels if necessary (also reversing \(\beta\)); this maps \(x_*\) to \(-x_*\), so one may assume \(x_*\le0\). At every \(\beta\ne\pi\), choose the sign of \(\sin t\) with \(\cos t=x_*\) so that
\[
 \cos(t-\beta)=x_*\cos\beta-\sqrt{1-x_*^2}|\sin\beta|\le x_*\cos\beta.
\]
If \(x_*<0\) and \(\beta\ne\pi\), then \(x_*\cos\beta<-x_*\), yielding \(F_\beta(t)<Ae^{ax_*}+Be^{-bx_*}\). If \(x_*=0\), the inequality is strict for \(\sin\beta\ne0\); when \(\beta=0\), choosing \(t=\pi\) gives \(Ae^{-a}+Be^{-b}<A+B\). Thus **equality occurs if and only if \(\beta\equiv\pi\pmod{2\pi}\)**. Applying this lemma with \(A=A_1,B=A_2,a=d_1,b=d_2\) proves the sharp design and all optimal orientations.

**3. Exact bifurcation and angular classification.** With equal weights and \(s_1>s_2>1\), the un-clipped cosine is
\[
 x_{\mathrm{raw}}(R)=\frac{c_1-c_2+\log(d_2/d_1)}{d_1+d_2}
 =x_\infty-\frac{4\log(\eta_1/\eta_2)}{\pi R^2(\eta_1+\eta_2)}.
\]
Since \(0<x_\infty<1\), this increases strictly from \(-\infty\) to \(x_\infty\) and never reaches \(+1\). Its unique crossing of \(-1\) occurs at the displayed \(R_0\), because \((c_1-c_2)+(d_1+d_2)=\pi R^2(s_1-s_2^{-1})/2\). Therefore clipping is active exactly when \(R\le R_0\). At the optimal relative orientation, \(\cos t=x_*\) is equivalent to \(\cos 2(\varphi-\theta_1)=-x_*\), giving one line at the boundary case \(x_*=-1\) and two lines in the interior. Finally, \(\arccos(1-h)\sim\sqrt{2h}\) yields the square-root opening, and \(x_*=0\) gives the stated crossing radius. No compactness or boundary cases are omitted.

## Verification

Run `python3 verification/check_gaussian_pair.py` with standard Python. It directly minimizes the original two-dimensional-window angular expression on a dense mesh with local golden-section refinement, checks 16 parameter/radius regimes, and compares the optimal perpendicular value with the closed formula and four nonperpendicular orientations for each regime. The diagnostic is `GAUSSIAN_PAIR_DESIGN_PASS cases=16 nonorthogonal_checks=64`. These are finite consistency checks; the analytic proof above establishes the all-parameter theorem.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486 (first posted 2024-10-07), Section 2.1, Eq. (7) and Remark 2.1, derive the positive sum-of-ambiguities inversion formula and design a family of equally spaced Gaussian rotations using a common dilation. Their displayed largest-disc calculation uses unions of equal-level ellipses, whereas the claim here optimizes the **pointwise minimum of the positive sum** over a disk for precisely two windows of **arbitrary, possibly unequal dilation and positive weight** and classifies all orientations and the splitting of worst directions. Their Sections 3.1.1–3.1.3 estimate noise via a positive denominator threshold but do not state the above exact denominator maximization.

Hardin, Kendall, and Saff, *Polarization Optimality of Equally Spaced Points on the Circle for Discrete Potentials*, arXiv:1208.5261 (2012), Theorem 1, obtain equispaced max-min configurations for **one shared nonincreasing convex geodesic kernel**. Here the two exponential-cosine kernels may differ in both scales and weights, and \(u\mapsto e^{a\cos u}\) is not convex throughout \([0,\pi]\); their hypotheses do not directly establish this sharp law or the unequal-squeezing bifurcation. Grohs, Liehr and Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620 (2022), instead prove phaseless lattice uniqueness for four-window systems; it makes no two-Gaussian disk-maximin statement.

## Limitations

This is a sharp *window-geometry denominator* theorem, not proof that the two-window STFT measurements uniquely recover arbitrary signals from a discrete lattice or minimize all sources of reconstruction error. It does not optimize the weights, cover isotropic Gaussians, or imply the equally spaced configuration is optimal for more than two unequal windows. No priority guarantee against every specialist polarization or optical-design formulation is claimed; all literature comparisons are to identified inspected works.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first public version 2024-10-07, https://arxiv.org/abs/2410.05486.
2. D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization Optimality of Equally Spaced Points on the Circle for Discrete Potentials*, arXiv:1208.5261, 2012, https://arxiv.org/abs/1208.5261.
3. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, first posted 2022-07-21, https://arxiv.org/abs/2207.10620.
