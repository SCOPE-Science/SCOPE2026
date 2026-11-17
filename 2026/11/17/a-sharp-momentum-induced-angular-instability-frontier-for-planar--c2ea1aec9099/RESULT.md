# A sharp momentum-induced angular instability frontier for planar saddle search

## Finding

Consider heavy-ball, or momentum-accelerated, fixed-projector saddle-search dynamics for a two-dimensional quadratic Morse saddle. Even when the reflected-gradient flow is exponentially stable, its accelerated version can be exponentially unstable solely because an approximate negative eigendirection is rotated. For every pair of positive Hessian magnitudes \(u,v\), friction \(\gamma\), and forcing gain \(\omega\), the exact critical orientation error is

\[
\theta_* = \frac12\arccos\!\left(\frac{\sqrt{\gamma^4+4\omega^2uv}-\gamma^2}{\omega(u+v)}\right),\qquad 0<\theta_*<\frac{\pi}{4}.
\]

The equilibrium is globally exponentially attracting in position and velocity for \(0\le\theta<\theta_*\), non-attracting with an imaginary pair at \(\theta=\theta_*\), and linearly unstable for \(\theta>\theta_*\), over \(0\le\theta\le\pi/2\). The crossing is a simple transverse oscillatory crossing. Moreover, for unequal curvatures there is a distinct, earlier spectral coalescence at \(\theta_{\mathrm{coll}}=\frac12\arccos(2\sqrt{uv}/(u+v))\), and \(\theta_{\mathrm{coll}}<\theta_*\). The latter is a stability boundary, not an ordinary change of the two eigenvalues of the reflected Hessian from real to complex.

For \(u=v=\gamma=\omega=1\), the threshold equals \(0.45227844715\ldots\) radians (approximately \(25.91364619^\circ\)). Thus a \(30^\circ\) eigendirection error leaves first-order reflected-gradient search exponentially stable but makes its heavy-ball acceleration unstable.

## Assumptions and scope

Let \(u,v,\gamma,\omega>0\), and define the quadratic energy, exact negative eigendirection, and a *fixed* approximate eigendirection by

\[
E(x_1,x_2)=-\frac{u}{2}x_1^2+\frac{v}{2}x_2^2,\qquad e_-=(1,0),\qquad w=(\cos\theta,\sin\theta),\quad 0\le\theta\le\frac\pi2.
\]

The accelerated dynamics in physical time is

\[
\ddot x+\gamma\dot x+\omega(I-2ww^{\mathsf T})\nabla E(x)=0,
\]

with arbitrary real initial position and velocity. The exact saddle is the origin. The first-order comparator is \(\dot x=-\omega(I-2ww^{\mathsf T})\nabla E(x)\). The projector is held fixed; no claim is made for time-varying or coupled eigenspace updates, discretized acceleration, nonlinear effects precisely at the crossing, or higher-dimensional sharp angular conditions.

## Proof

Write \(c=\cos(2\theta)\), \(s=\sin(2\theta)\). The restored Hessian matrix is

\[
K=(I-2ww^{\mathsf T})\nabla^2E=\begin{pmatrix}uc&-vs\\ us&vc\end{pmatrix},
\qquad \operatorname{tr}K=(u+v)c=:T,\quad \det K=uv.
\]

The first-order comparator is exponentially stable if and only if \(T>0\): for a real two-by-two matrix with positive determinant, the eigenvalues of \(-\omega K\) have negative real part exactly when its trace is negative. Hence its exact fixed-angle frontier is \(\pi/4\).

The accelerated first-order position/velocity state matrix is

\[
A=\begin{pmatrix}0&I_2\\-\omega K&-\gamma I_2\end{pmatrix}.
\]

By a block determinant, its characteristic polynomial is

\[
P(\lambda)=\det((\lambda^2+\gamma\lambda)I_2+\omega K)
=\lambda^4+2\gamma\lambda^3+(\gamma^2+\omega T)\lambda^2+\gamma\omega T\lambda+\omega^2uv.
\]

For \(T>0\), all coefficients are positive, and the first nontrivial Routh--Hurwitz inequality, \(a_1a_2>a_3\), follows from \(2\gamma^3+\gamma\omega T>0\). The remaining strict Routh--Hurwitz inequality is precisely

\[
a_1a_2a_3-a_3^2-a_1^2a_4
=\gamma^2\omega\left[2\gamma^2T+\omega T^2-4\omega uv\right]>0.
\]

Thus stability for \(T>0\) is equivalent to \(F(T):=2\gamma^2T+\omega T^2-4\omega uv>0\). The function \(F\) is strictly increasing for \(T>0\), has one positive zero

\[
T_* =\frac{\sqrt{\gamma^4+4\omega^2uv}-\gamma^2}{\omega},
\]

and satisfies \(0<T_*<2\sqrt{uv}\le u+v\), since \(F(2\sqrt{uv})=4\gamma^2\sqrt{uv}>0\). As \(T=(u+v)\cos2\theta\) decreases strictly from \(u+v\) to \(0\) on the first quadrant of orientation errors, this gives the claimed unique threshold strictly below \(\pi/4\). For \(T\le0\), the positive constant determinant and the nonpositive \(\lambda\)-coefficient exclude a Hurwitz polynomial; in fact at \(T=0\) no imaginary-axis root exists, while at \(T<0\) every eigenvalue of \(K\) has nonpositive real part and the corresponding quadratic factor \(\lambda^2+\gamma\lambda+\omega\mu\) has a right-half-plane root. The strict instability also follows continuously from the positive-root pair just beyond \(T_*\).

At \(T=T_*\), put \(\nu^2=\omega T_*/2>0\). The critical equation \(F(T_*)=0\) gives \(\nu^2(\gamma^2+\nu^2)=\omega^2uv\) and therefore the *exact* factorization

\[
P(\lambda)=(\lambda^2+\nu^2)((\lambda+\gamma)^2+\nu^2).
\]

Hence the eigenvalues are \(\pm i\nu\) and \(-\gamma\pm i\nu\), all simple. The imaginary pair causes nondecaying oscillatory solutions, so the origin is not asymptotically attracting at equality. Implicit differentiation of \(P(\lambda,T)=0\) at \(\lambda=i\nu\) yields

\[
\frac{d\operatorname{Re}\lambda}{dT}\bigg|_{T_*}
=-\frac{\omega(\gamma^2+2\nu^2)}{2\gamma(\gamma^2+4\nu^2)}<0.
\]

Since \(dT/d\theta=-2(u+v)\sin2\theta<0\) at \(\theta_*\), the conjugate pair crosses the imaginary axis transversely toward instability as the orientation error grows.

Finally, the two eigenvalues of \(K\) coalesce exactly when \(T^2=4uv\). On \(0\le\theta\le\pi/4\), this occurs at the stated \(\theta_{\mathrm{coll}}\), and the strict inequality \(T_*<2\sqrt{uv}\) proves \(\theta_{\mathrm{coll}}<\theta_*\). In the balanced case \(u=v\), this coalescence occurs already at zero error.

## Verification

The independent symbolic calculation in `verification.py` reconstructs \(K\), its determinant and trace, and the exact quartic, including its factorization at the critical point. Its deterministic numerical checks cover 1,000 random positive parameter quadruples with six sample angles each, comparing the predicted stability classification with direct eigenvalues of the four-by-four state matrix and checking the polynomial coefficients. The unit-parameter case has a positive eigenvalue real part \(0.07069599\ldots\) at \(\theta=\pi/6\). Run `python verification.py` with NumPy and SymPy installed. Numerical tests support but do not replace the analytic proof.

## Relationship to prior work

Shi, Zhang, Zheng and Zhu (2026) analyze the perturbed momentum-accelerated high-index saddle flow and provide an explicit *sufficient* exponential-stability condition (Theorem 10). Their sufficient estimate gives neither the necessary-and-sufficient angular frontier nor its oscillatory loss mechanism. Luo, Zheng and Zhang (2023, subsequently published in 2025) study the full accelerated high-index saddle dynamics at exact eigendirections and its discrete local convergence; their analysis does not classify a fixed rotated, inexact projector. Chu and Lin (2025) analyze the Householder-reflection geometry and convergence of generalized *first-order* gentlest-ascent dynamics, not the above inertial threshold. The elementary Routh--Hurwitz and quadratic characteristic criteria themselves are classical; originality is claimed only for their sharp application to the specified inexact accelerated saddle-search problem, including the gap from its first-order analogue.

## Limitations

The theorem concerns one fixed approximate rank-one eigenspace in exactly two dimensions, a quadratic Morse saddle, and continuous-time heavy-ball acceleration. The neutral linear motion at equality is not a nonlinear Hopf-cycle existence theorem. The angle frontier is not a uniform theorem for arbitrary varying subspace errors. Scientific priority beyond the inspected literature is not independently certified.

## References

1. B. Shi, L. Zhang, X. Zheng and S. Zhu, *Asymptotic stability of high-index saddle dynamics*, arXiv:2611.09049v1, first posted November 6, 2026, particularly §2 and Theorem 10 of §5.2. https://arxiv.org/html/2611.09049v1
2. Y. Luo, X. Zheng and L. Zhang, *Accelerated high-index saddle dynamics method for searching high-index saddle points*, arXiv:2310.04656, first posted October 7, 2023, especially §3. https://arxiv.org/abs/2310.04656
3. M. T. Chu and M. M. Lin, *Generalized Gentlest Ascent Dynamics Methods for High-Index Saddle Points*, SIAM Journal on Numerical Analysis, DOI:10.1137/24M1710905, §§2–4. https://epubs.siam.org/eprint/6RBKIUEVWEEPYCJZVVBK/full
