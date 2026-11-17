# Global transient pulse and sharp misalignment gain in a planar coupled saddle flow

## Finding
For the coupled gentlest-ascent flow on a balanced-curvature planar quadratic saddle, every initial search direction except the incorrect eigenline converges to the target saddle, but the position may undergo arbitrarily large transient amplification. The full time-dependent Euclidean norm has a closed form, with a universal peak-centered hyperbolic-secant profile and a sharp algebraic blowup in the initial alignment error.

More precisely, if \(u_0=v_2(0)/v_1(0)\) is finite and nonzero, set \(t_*=\log|u_0|/(2\gamma\lambda)\). Then for every \(t\geq0\) and \(X(0)\ne0\),
\[
\frac{\|X(t)\|_2}{\|X(0)\|_2}
=\left(\frac{\cosh(2\gamma\lambda t_*)}{\cosh(2\gamma\lambda(t-t_*))}\right)^{\beta/(2\gamma)}.
\]
For \(|u_0|>1\), the unique maximum occurs at \(t_*\), has amplification \(\bigl((|u_0|+|u_0|^{-1})/2\bigr)^{\beta/(2\gamma)}\), and the original norm is first regained at \(2t_*\). For \(|u_0|\leq1\), the norm decreases from time zero and its maximum amplification equals one. In particular, as \(s=|v_1(0)|\downarrow0\), the maximal amplification is asymptotic to \((2s)^{-\beta/(2\gamma)}\), although every trajectory with \(s>0\) converges to the target.


**Sharp random-start risk.** If the initial unoriented line \([v(0)]\) is uniform (Haar) on \(\mathbb{RP}^1\), with any fixed nonzero initial position, the gain \(G=\sup_{t\ge0}\|X(t)\|_2/\|X(0)\|_2\) has an atom of mass \(1/2\) at one and the exact strict tail
\[
\mathbb P(G>z)=\frac1\pi\arcsin\bigl(z^{-2\gamma/\beta}\bigr),\qquad z\ge1.
\]
Thus \(\mathbb P(G>z)\sim z^{-2\gamma/\beta}/\pi\), and for every \(p>0\),
\[
\mathbb E[G^p]<\infty\quad\Longleftrightarrow\quad p<2\gamma/\beta.
\]
In particular, the expected maximal amplification is infinite for \(\beta\ge2\gamma\) despite almost-sure convergence of both the direction and position.

## Assumptions and scope
Let \(\lambda,\beta,\gamma>0\), let \(E(X)=\lambda(X_2^2-X_1^2)/2\), and let \(X(t)\in\mathbb R^2\), \(v(t)\in S^1\) solve the autonomous coupled flow
\[
\dot X=-\beta(I-2vv^{\mathsf T})\nabla E(X),\qquad
\dot v=-\gamma(I-vv^{\mathsf T})\nabla^2E(X)\,v.
\]
All assertions hold for arbitrary initial \(X(0)\) and unit \(v(0)\). Since \(v\) and \(-v\) induce identical physical states, write \([v]\in\mathbb{RP}^1\) for the unoriented search line. The target is \((0,[e_1])\). The term *position amplification* refers to the Euclidean ratio \(\|X(t)\|_2/\|X(0)\|_2\), defined when \(X(0)\ne0\); the zero-position trajectory is identically zero.

## Proof
**Direction reduction.** The Hessian is \(H=\operatorname{diag}(-\lambda,\lambda)\). Direct substitution into the second equation gives \(\dot v_1=2\gamma\lambda v_1v_2^2\) and \(\dot v_2=-2\gamma\lambda v_2v_1^2\). Thus \(v_1=0\) is invariant and, when \(v_1(0)\ne0\), the projective coordinate \(u=v_2/v_1\) satisfies
\[
\dot u=-2\gamma\lambda u,\qquad u(t)=u_0e^{-2\gamma\lambda t}.
\]
This explicitly proves \([v(t)]\to[e_1]\) whenever \(v_1(0)\ne0\), while \([e_2]\) remains fixed.

**Position integration.** For finite \(u\), the first equation is exactly
\[
\dot X=\frac{\beta\lambda}{1+u^2}
\begin{pmatrix}u^2-1&2u\\-2u&u^2-1\end{pmatrix}X.
\]
The coefficient matrix is a multiple of the identity plus a skew-symmetric matrix. Therefore, its symmetric part controls the Euclidean norm for every nonzero \(X\), irrespective of its initial angle:
\[
\frac{d}{dt}\log\|X(t)\|_2
=\beta\lambda\frac{u(t)^2-1}{1+u(t)^2}.
\]
Use \(\frac{d}{dt}\log(1+u(t)^2)=-4\gamma\lambda u(t)^2/(1+u(t)^2)\). Exact integration yields
\[
\frac{\|X(t)\|_2}{\|X(0)\|_2}
=e^{-\beta\lambda t}
\left(\frac{1+u_0^2}{1+u_0^2e^{-4\gamma\lambda t}}\right)^{\beta/(2\gamma)}.
\tag{1}
\]
If \(u_0\ne0\), substitute \(u_0^2=e^{4\gamma\lambda t_*}\) into (1) to obtain the stated hyperbolic-secant expression. The evolution is global: the direction is explicit and the position satisfies a linear equation with bounded continuous coefficients. Its asymptotic decay follows from (1).

**Sharp transient and global basin.** The logarithmic norm derivative is positive precisely when \(|u(t)|>1\), vanishes once when \(|u(t)|=1\), and is negative thereafter. For \(|u_0|>1\), this gives the unique positive peak time \(t_*\). Evaluation of (1) gives
\[
G(u_0)=\left(\frac{|u_0|+|u_0|^{-1}}2\right)^{\beta/(2\gamma)}.
\]
The hyperbolic-cosine symmetry about \(t_*\) gives \(\|X(2t_*)\|_2=\|X(0)\|_2\) and strict amplification on \((0,2t_*)\). For \(|u_0|\le1\), including \(u_0=0\), the norm never increases and \(G=1\). Writing \(|u_0|=\sqrt{1-s^2}/s\) proves \(G\sim(2s)^{-\beta/(2\gamma)}\) as \(s\downarrow0\). If \(v_1(0)=0\), then \(v(t)=\pm e_2\) and \(\dot X=\beta\lambda X\); hence every nonzero position diverges and the zero position is a second stationary state with the wrong search line. Consequently the entire basin of attraction of \((0,[e_1])\) in \(\mathbb R^2\times\mathbb{RP}^1\) is exactly \(\{(X,[v]):v_1\ne0\}\). This proves every asserted boundary, including the exceptional eigenline.


**Uniform-direction distribution.** Represent a Haar-random unoriented line by its acute angle \(\theta\in[0,\pi/2]\) to the unstable eigenline; then \(\theta\) is uniform with density \(2/\pi\), and \(|u_0|=\tan\theta\). For \(\theta\le\pi/4\) the gain is one. For \(\theta>\pi/4\), the preceding sharp-gain identity becomes \(G=(\sin2\theta)^{-\beta/(2\gamma)}\). Therefore, for \(z\ge1\), the event \(G>z\) is exactly
\[
\theta>\frac{\pi-\arcsin(z^{-2\gamma/\beta})}{2},
\]
whose uniform-angle probability is the claimed \(\pi^{-1}\arcsin(z^{-2\gamma/\beta})\). Its near-infinity asymptotic follows from \(\arcsin y\sim y\) at zero. The tail-integral identity for nonnegative random variables shows that \(\mathbb E[G^p]\) is finite precisely when \(\int_1^\infty z^{p-1-2\gamma/\beta}\,dz\) is finite, proving the exact moment threshold, including logarithmic divergence at equality.

For completeness, the full vector solution can also be reconstructed: if \(R(\phi)\) is planar counterclockwise rotation through \(\phi\), then
\[
X(t)=\rho(t)R\left(-\frac\beta\gamma(\arctan u_0-\arctan u(t))\right)X(0),
\]
where \(\rho(t)\) is the right-hand side of (1). Differentiating confirms both the radial and skew terms.

## Verification
The standalone `checker.py` symbolically reconstructs the exact coefficient matrix and projective direction equation, numerically integrates the unreduced four-coordinate system (two position plus two direction coordinates) for 192 parameter/initial-direction configurations, compares the vector solution at four times per configuration, checks peak/return identities, and compares the random-start tail formula with deterministic angular quadrature. It uses SymPy, NumPy, and SciPy. Run with `python checker.py`; it terminates with a `PASS` line if all assertions hold. Numerical checks corroborate but are not the proof; the preceding identities prove the result for all indicated positive parameters and times.

## Relationship to prior work
The coupled gentlest-ascent equations are established, not new: E and Zhou (2011) introduced the underlying search dynamics. Shi, Zhang, Zheng, and Zhu (2026), §2 and Theorem 5, establish local asymptotic stability for general coupled high-index saddle dynamics with initial projection restrictions; those estimates do not imply a complete basin or a sharp arbitrarily large transient gain and its Haar-initialization heavy tail in the balanced planar model. Bofill, Quapp, and Caballero (2013) study turning paths to transition states on nonlinear model potentials, without this closed-form misalignment law. Chu and Lin (2025) analyze Householder geometry, direction dynamics, and high-index generalizations, but not this global radius-pulse formula. The present assertion is confined to a concrete solvable planar saddle, not a general convergence theorem for arbitrary potentials.

## Limitations
The equal absolute Hessian eigenvalues \(-\lambda\) and \(\lambda\) are essential for the scalar-plus-skew position matrix. No analogous full-parameter assertion is made for arbitrary anisotropic, variable-Hessian, or accelerated saddle flows. The result concerns position norm and search-line dynamics, not monotonicity of the original saddle energy, nor a general trust-region guarantee. The publication-priority assessment is limited to the cited and searched literature; independent audit has not been performed.

## References
1. W. E and X. Zhou, *The Gentlest Ascent Dynamics*, Nonlinearity 24 (2011), arXiv:1011.0042, https://arxiv.org/pdf/1011.0042.
2. B. Shi, L. Zhang, X. Zheng, and S. Zhu, *Asymptotic stability of high-index saddle dynamics*, arXiv:2611.09049v1 (first public 2026-11-06), https://arxiv.org/html/2611.09049v1.
3. M. T. Chu and M. M. Lin, *Generalized Gentlest Ascent Dynamics Methods for High-Index Saddle Points*, SIAM Journal on Numerical Analysis (2025), https://doi.org/10.1137/24M1710905.
4. J. M. Bofill, W. Quapp, and M. Caballero, *Locating transition states on potential energy surfaces by the gentlest ascent dynamics*, Chemical Physics Letters 583 (2013), 203–208, https://doi.org/10.1016/j.cplett.2013.07.074.
