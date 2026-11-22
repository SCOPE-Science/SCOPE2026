# Exact zero-count staircase for the stationary heading–position time arrow of a trapped chiral swimmer

## Finding

For a stationary planar chiral active Brownian particle in a harmonic trap, compare the two experimentally distinguishable lagged orientation–position correlations
\[
A(t)=\mathbb E[\boldsymbol n_0\cdot\boldsymbol X_t]-\mathbb E[\boldsymbol X_0\cdot\boldsymbol n_t],\quad t\geq0.
\]
An exact elementary formula determines **every** positive-lag zero of this temporal asymmetry: in the weak-trap regime its zeros occur in pairs, with precisely countable parameter-dependent staircases and isolated zero-touching transitions. A critical equality between trap relaxation and orientation decorrelation separates finitely many from infinitely many sign changes. The count is independent of translational thermal diffusivity and swimming speed.

## Assumptions and scope

Let \(k,d,v>0\), \(D_t\geq0\), and \(\omega\in\mathbb R\). Consider the unique stationary planar process
\[
 d\boldsymbol X_t=(-k\boldsymbol X_t+v\boldsymbol n_t)dt+\sqrt{2D_t}\,d\boldsymbol B_t,\qquad
 \boldsymbol n_t=(\cos\Theta_t,\sin\Theta_t),\qquad
 d\Theta_t=\omega dt+\sqrt{2d}\,dW_t\pmod{2\pi}.
\]
The Brownian noises are independent and the stationary angle is uniform. For zero counting it is sufficient by reflection symmetry to set \(w=|\omega|\ge0\). Let
\[
 Z=[(k-d)^2+w^2][(k+d)^2+w^2],\qquad
 a=\frac{2d(d^2-k^2+w^2)}Z,\quad
 b=\frac{2w(d^2+k^2+w^2)}Z.
\]
When \(w>0\), \(Z>0\) and
\[
 \frac{A(t)}v=a(e^{-kt}-e^{-dt}\cos wt)+b e^{-dt}\sin wt.\tag{1}
\]
The initial root at \(t=0\) is excluded from all positive-root counts. Positive roots are **distinct** real times, even when a zero is tangent rather than sign-changing.

**Exact finite staircase.** Suppose \(0<k<d\) and \(w>0\). Define
\[
 \lambda=d-k,\quad \phi=\arctan(b/a)\in(0,\pi/2),\quad
 \delta=\arctan(\lambda/w)\in(0,\pi/2),
\]
\[
 z=\frac{w\lambda^{-1}\log(\cos\delta/\cos\phi)+\delta+\phi}{2\pi},\qquad
 M=\max\{0,\lceil z\rceil-1\}.
\]
Then the exact number of strictly positive roots is
\[
 \boxed{N=2M+\mathbf1_{\{z\in\mathbb Z_{\ge1}\}}.}\tag{2}
\]
There are exactly \(2M\) genuine sign changes. If \(z\) is a positive integer, the additional root is a quadratic tangency; otherwise every positive root is simple. In particular, for fixed \(d,w>0\), as \(k\uparrow d\),
\[
 N=\frac{w}{\pi(d-k)}\log\!\sqrt{1+\left(\frac{2d^2+w^2}{dw}\right)^2}+O(1).\tag{3}
\]
**Other regimes.** When \(k=d\) and \(w>0\), every positive root is simple and the full set is
\[
 \left\{\frac{2\pi j}{w},\,\frac{2\pi j-2\phi}{w}:j=1,2,\ldots\right\},
 \quad \phi=\arctan(b/a)\ \text{evaluated at }k=d.
\]
For \(k>d\) and \(w>0\), there are infinitely many alternating sign intervals. For \(w=0\), \(A(t)>0\) for all \(t>0\), at every \(k,d>0\); the apparent pole of \(a\) at \(k=d,w=0\) is removable.

## Proof

Use the stationary causal representation
\[
\boldsymbol X_t=v\int_0^\infty e^{-ks}\boldsymbol n_{t-s}\,ds+\sqrt{2D_t}\int_{-\infty}^t e^{-k(t-s)}d\boldsymbol B_s
\]
and the exact orientational covariance \(\mathbb E[\boldsymbol n_s\cdot\boldsymbol n_t]=e^{-d|t-s|}\cos(w(t-s))\). Independence makes the translational Brownian term orthogonal to each heading. For \(t\ge0\),
\[
\mathbb E[\boldsymbol X_0\cdot\boldsymbol n_t]
=v\operatorname{Re}\frac{e^{(-d+iw)t}}{k+d-iw},
\]
\[
\mathbb E[\boldsymbol n_0\cdot\boldsymbol X_t]
=v\operatorname{Re}\left[\frac{e^{-kt}}{k+d-iw}
+\frac{e^{(-d+iw)t}-e^{-kt}}{k-d+iw}\right].
\]
Subtract and rationalize. The real and imaginary parts of \((k+d-iw)^{-1}-(k-d+iw)^{-1}\) are exactly \(a\) and \(b\), proving (1), including its noise independence. Its initial slope is strictly positive:
\[
 A'(0+)=\frac{2v(d^2+dk+w^2)}{(k+d)^2+w^2}>0.
\]

For \(0<k<d\) we have \(a,b>0\). Put \(C=\sqrt{a^2+b^2}\), so \(a=C\cos\phi\), \(b=C\sin\phi\). Equation (1) becomes
\[
 A(t)=vC e^{-dt}\bigl[\cos\phi\,e^{\lambda t}-\cos(wt+\phi)\bigr].\tag{4}
\]
Thus positive zeros solve \(e^{-\lambda t}\cos(wt+\phi)=\cos\phi>0\). On the initial positive-cosine interval the left side decreases strictly from \(\cos\phi\), hence the only initial root is \(t=0\). Subsequent positive cosine lobes are indexed by \(j\ge1\); the function has exactly one positive maximum on each, attained at
\[
 t_j=\frac{2\pi j-\delta-\phi}{w}>0,\qquad
 m_j=e^{-\lambda t_j}\cos\delta.
\]
It has two transverse intersections with the horizontal level \(\cos\phi\) precisely when \(m_j>\cos\phi\), one quadratic tangency precisely at equality, and none otherwise. Strict inequality is equivalent to \(j<z\), equality to \(j=z\). Since the maxima decrease geometrically with \(j\), this proves (2), the parity of sign crossings and the uniqueness of the exceptional tangency. As \(k\uparrow d\), \(\delta\to0\) and \(\cos\phi\to [1+((2d^2+w^2)/(dw))^2]^{-1/2}\), yielding (3), with the integer rounding contributing only \(O(1)\).

At \(k=d\), the nonoscillatory and oscillatory decay rates coincide, and (4) reduces to \(A(t)=vC e^{-dt}[\cos\phi-\cos(wt+\phi)]\); its displayed zero set is immediate. At \(k>d\), the oscillatory \(e^{-dt}\) term in (1) dominates the \(e^{-kt}\) term for large time, forcing infinitely many alternating simple zeros. At \(w=0,k\ne d\), equation (1) has the positive value \(2vd(e^{-kt}-e^{-dt})/(d^2-k^2)\); its continuous \(k=d\) limit is \(vt e^{-dt}\). This covers all boundaries.

## Verification

The accompanying standalone `checker.py` validates the complex coefficient identity symbolically; compares (1) with 70 independently integrated stationary forward/past covariance pairs; and compares (2) with 150 independently evaluated lobe maxima. All checks passed. At \(k=1/2,d=1\), the exact positive-zero counts are \(0\), \(2\), and \(14\) for \(w=1,3,10\), respectively. For \(k=1/2,d=1\), the first tangency occurs at \(w\approx2.423532962951\), at time \(t\approx2.011639025438\) (reported numerics illustrate the analytic equality, not certify it). These finite tests do not replace the infinite root-count proof above.

## Relationship to prior work

Pattanayak, Shee, Chaudhuri and Chaudhuri obtain exact time-dependent **equal-time** position–orientation correlations for trapped chiral active particles (their Appendix A, especially Eqs. A17–A22). Barman studies a different **velocity–orientation** lag, explicitly imposing a deterministic initial position at the origin (his Section IV, Eqs. 13–16). Neither gives the stationary two-time forward-minus-backward **heading–position** statistic or its integer zero-count/tangency law. A positional lag-area correlation can have a related trap-versus-angle decorrelation boundary, but it uses a position–position antisymmetry and does not determine the mixed heading–position function or its exact finite-root staircase. Standard theory of damped trigonometric functions explains the crossing technique but does not supply this physical observable, coefficients, or parameter classification. Index searches found no covering implication, subject to the residual possibility of unindexed equivalent work.

## Limitations

The result is for the ideal isotropic harmonic model with stationary initialization, continuous heading observations and independent translational noise. It does not characterize finite-sample estimation, anisotropic traps, interacting swimmers or entropy production. The asymptotic formula is for fixed strictly positive chirality and rotational diffusivity as the two decay rates coincide. Root counts depend on actual model parameters; numerical sampling alone is insufficient near quadratic tangencies. Mathematical originality is assessed against inspected sources and indexed comparisons, not independently certified.

## References

1. A. Pattanayak, A. Shee, A. Chaudhuri and D. Chaudhuri, *Characterizing exact dynamics of a trapped active Brownian particle under torque in two and three dimensions*, arXiv:2603.26967 (first public submission 27 March 2026), subsequently published as *Exact dynamics and dimensional effects in torque-driven trapped active Brownian particles*, APS Open Science 1, 000187 (2026), DOI:10.1103/9yjb-kj12. https://arxiv.org/abs/2603.26967
2. H. Barman, *Confinement-Induced Delay in Chiral Active Brownian Particles*, arXiv:2510.15419, Section IV. https://arxiv.org/abs/2510.15419
