# Sharp two-shell radial sampling laws for affine least-squares extrapolation

## Finding

Fix an integer \(d\ge2\) and \(0<s\le1\). Let \(B_d\subset\mathbb R^d\) be the closed Euclidean unit ball. Consider **all** rotation-invariant Borel probabilities \(\mu\) on \(B_d\) with \(\int\|y\|^2\,d\mu(y)=s\). Let \(P_\mu\) be orthogonal projection in \(L^2(\mu)\) onto the \((d+1)\)-dimensional space of affine functions, with its unique affine representative evaluated on the entire ball. Its extrapolation norm is
\[
\Lambda(\mu)=\|P_\mu:L^\infty(\mu)\longrightarrow C(B_d)\|.
\]
This norm is well-defined even for singular or spherical-shell measures because \(s>0\) makes the affine Gram matrix positive definite.

Write \(Y=R\Theta\), where \(\Theta\) is independent uniform probability on the unit sphere and \(R\in[0,1]\). For \(a\ge0\), define
\[
\Psi_d(a)=\mathbb E\big|1+a\Theta_1\big|,
\qquad c=\frac ds.
\]
Define \(a_d\) as the unique root larger than \(\sqrt d\) of
\[
 a\Psi_d'(a)=2\big(\Psi_d(a)-1\big),
\]
and set
\[
\tau=\min\left\{1,\left(\frac{s a_d}{d}\right)^2\right\}.
\]
Then the **exact maximum**, over all eligible radial sampling laws, is
\[
\boxed{\ \sup_{\mu}\Lambda(\mu)=
\begin{cases}
\Psi_d(d/\sqrt s),&s\ge\tau,\\
1+\dfrac{s}{\tau}\big(\Psi_d((d/s)\sqrt\tau)-1\big),&s<\tau.
\end{cases}\ }
\]
The maximizing radial law is **unique**: for \(s\ge\tau\), it is \(R^2=s\) almost surely; for \(s<\tau\), it assigns probability \(s/\tau\) to \(R^2=\tau\) and the remaining probability to \(R=0\). Uniform angular direction is understood on every nonzero shell. These statements include all parameter boundaries, with \(s=1\) forcing the unit-sphere law.

For the disk (\(d=2\)), there is a genuine **three-regime transition**. The constant \(a_2\approx2.5365589892306\) is uniquely specified by
\[
\sqrt{a_2^2-1}+2\arcsin(1/a_2)=\pi.
\]
If \(0<s\le4/a_2^2\), the unique worst sampling law is the circle of radius \(\sqrt s\). If \(4/a_2^2<s<2/a_2\), it is a mixture of the origin and the circle of radius \(s a_2/2\), with outer-circle probability \(4/(s a_2^2)\). If \(2/a_2\le s<1\), it is a mixture of the origin and the boundary circle, with boundary probability \(s\). The exact transition points are approximately \(0.621684526710\) and \(0.788469737345\). In dimension three, \(a_3=3\), so the single-shell law is optimal for every \(0<s\le1\).

## Assumptions and scope

The dimension is any integer \(d\ge2\); \(\mu\) may have arbitrary Borel radial law, including atoms. Angular directions must be Haar-uniform and independent of radius; total mass is one and the fixed second moment is exactly \(s\in(0,1]\). The target norm is the supremum of the affine representative on the **full unit ball**, not merely on the support of \(\mu\). No positivity or density assumption is made. The sharpness and uniqueness statements concern optimization over the sampling laws, not uniqueness of norming input functions for a fixed law.

## Proof

**1. Projection kernel and reduction.** Rotation invariance implies \(\mathbb E Y=0\) and \(\mathbb E YY^{\mathsf T}=(s/d)I\). Consequently, the affine projection has the explicit reproducing kernel
\[
(P_\mu f)(x)=\int_{B_d}f(y)\left(1+\frac ds\langle x,y\rangle\right)d\mu(y).
\]
For fixed \(x\), the norm of this evaluation is the absolute \(\mu\)-integral of its kernel; choosing the sign of that kernel attains it. The expectation \(\mathbb E|1+(d/s)R\|x\|\Theta_1|\) is nondecreasing in \(\|x\|\), since it is an even convex function of the scalar coefficient. Hence the largest evaluation norm is on \(\|x\|=1\):
\[
 \Lambda(\mu)=\mathbb E\Psi_d((d/s)R).
\]
This is an exact identity, including for measures with atoms and shell support.

**2. The one-variable shape.** The first coordinate of \(\Theta\) has density
\[
 k_d(1-z^2)^{(d-3)/2}\mathbf 1_{(-1,1)}(z),\qquad
 k_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}.
\]
For \(0\le a\le1\), symmetry gives \(\Psi_d(a)=1\). For \(a>1\), direct integration yields
\[
 \Psi_d(a)=1+2k_d\int_{1/a}^1(az-1)(1-z^2)^{(d-3)/2}\,dz,
\]
\[
 \Psi_d'(a)=\frac{2k_d}{d-1}(1-a^{-2})^{(d-1)/2},\qquad
 \Psi_d''(a)=\frac{2k_d}{a^3}(1-a^{-2})^{(d-3)/2}.
\]
Put \(H_d(a)=a\Psi_d'(a)-2(\Psi_d(a)-1)\). For \(a>1\),
\[
H_d'(a)=a\Psi_d''(a)-\Psi_d'(a),\qquad
\operatorname{sgn}H_d'(a)=\operatorname{sgn}(d-a^2).
\]
Thus \(H_d\) rises strictly from zero on \((1,\sqrt d)\), decreases strictly thereafter, and tends to \(-\infty\): indeed \(\Psi_d(a)/a\to\mathbb E|\Theta_1|>0\) and \(\Psi_d'(a)\to\mathbb E|\Theta_1|\). This proves existence and uniqueness of \(a_d>\sqrt d\). It also shows that the ratio \((\Psi_d(a)-1)/a^2\) rises strictly up to \(a_d\) and decreases strictly afterward.

**3. Exact concave envelope.** Let \(T=R^2\) and \(g(t)=\Psi_d(c\sqrt t)\) for \(t\in[0,1]\), where \(c=d/s>1\). We have \(g(t)=1\) on \([0,c^{-2}]\). Above this interval,
\[
 g''(t)=\frac{a^2\Psi_d''(a)-a\Psi_d'(a)}{4t^2},\qquad a=c\sqrt t,
\]
so \(g\) is strictly convex for \(1<a<\sqrt d\), and strictly concave for \(a>\sqrt d\). By the ratio monotonicity proved in step 2, its **smallest concave majorant** on \([0,1]\) is the chord joining \((0,1)\) to \((\tau,g(\tau))\) on \([0,\tau]\), followed by \(g\) on \([\tau,1]\). If \(a_d\ge c\), the chord extends to \(\tau=1\). The chord is tangent at its non-endpoint junction when \(\tau<1\). Strict ratio monotonicity shows it touches \(g\) on the first segment only at its endpoints.

For every \(T\in[0,1]\) with \(\mathbb ET=s\), Jensen's inequality for the concave majorant bounds \(\mathbb E g(T)\) by the displayed two-case formula. If \(s\ge\tau\), the point law \(T=s\) attains it, and strict concavity beyond the chord forces uniqueness. If \(s<\tau\), the two-point law on \(\{0,\tau\}\) with weights \(1-s/\tau,s/\tau\) attains it; strict separation of the chord from \(g\) at interior points and its strict concavity beyond \(\tau\) force uniqueness. This also handles \(\tau=1\) and equality at \(s=\tau\).

**4. Disk thresholds.** In dimension two, angular integration gives
\[
 \Psi_2(a)=\frac2\pi\left(\sqrt{a^2-1}+\arcsin(1/a)\right),\quad a>1.
\]
Substitution in \(H_2(a)=0\) gives the stated unique equation for \(a_2\). Since \(a_2>2\), the conditions \(s\ge\tau\), \(s<\tau<1\), and \(\tau=1\) reduce respectively to the three parameter intervals displayed in the finding. In dimension three, the first spherical coordinate is uniform on \([-1,1]\), so \(\Psi_3(a)=(a+a^{-1})/2\) for \(a>1\), giving \(a_3=3\), \(\tau=s^2\le s\).

## Verification

The accompanying standard-library Python program `verify.py` independently integrates the spherical-coordinate density for multiple dimensions, checks the disk kernel by direct angular quadrature, locates the tangency roots, and compares the predicted envelope with all two-radius mixtures from a finite squared-radius grid. The output is:

```text
TANGENCY_ROOTS_OK 2.536558989231 3.0
DISK_THRESHOLDS 0.62168452671 0.788469737345
TWO_RADIUS_MOMENT_ENVELOPES_OK 30
DIRECT_CIRCLE_KERNEL_QUADRATURE_OK 5
THREE_DISK_OPTIMIZER_REGIMES_OK
ALL_RADIAL_AFFINE_EXTRAPOLATION_CHECKS_OK
```

These are finite numerical corroborations. The continuum theorem, exact optimizer uniqueness, and thresholds are proved analytically above, not by enumeration.

## Relationship to prior work

Classical weighted-ball orthogonal polynomials and their reproducing kernels, including Gegenbauer-type radial weights, have a substantial literature. Piñar–Xu (2007) and Xu (2015) describe polynomial structure and kernel techniques; Figueroa (2016) studies weighted Sobolev approximation of ball projections. The present statement instead optimizes the **affine extrapolation norm across all radial Borel sampling designs at fixed second moment**, and characterizes the unique extremal one- and two-shell laws, with the disk's two exact transitions. The results and proofs in the cited primary sources do not state these moment-constrained two-shell conclusions.

## Limitations

No claim is made about non-rotation-invariant designs, nonlinear polynomial subspaces, other prescribed moments, or projection norms measured only on the sampling support.

## References

1. M. Piñar and Y. Xu, *Orthogonal polynomials and partial differential equations on the unit ball*, arXiv:0712.3091v1 (first posted 2007-12-19), https://arxiv.org/abs/0712.3091.
2. Y. Xu, *Orthogonal expansions for generalized Gegenbauer weight function on the unit ball*, arXiv:1502.02379v1 (first posted 2015-02-09), https://arxiv.org/abs/1502.02379.
3. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, arXiv:1607.00930v1 (first posted 2016-07-04), https://arxiv.org/abs/1607.00930.
