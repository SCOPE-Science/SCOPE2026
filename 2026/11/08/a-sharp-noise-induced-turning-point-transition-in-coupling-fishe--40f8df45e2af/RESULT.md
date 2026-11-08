# A sharp noise-induced turning-point transition in coupling Fisher information

## Finding

Consider a stationary two-dimensional overdamped Langevin particle with harmonic coupling and an extra white-noise intensity in its second coordinate. Denote the dimensionless coupling by \(b\), the ratio of added noise to baseline thermal noise by \(d\), and the **single-snapshot Fisher information for \(b\) when \(d\) is known** by \(\mathcal I_{bb}(b,d)\). The parameter domain is \(-1<b<1\), \(d\geq0\).

There is exactly one critical intensity \(d_\star>0\), characterized algebraically below, such that:

- For \(0\leq d\leq d_\star\), \(\mathcal I_{bb}(b,d)\) is strictly increasing in \(|b|\in[0,1)\). At equality it has one stationary, non-extremal inflection point at positive coupling.
- For \(d>d_\star\), it has exactly two stationary points on \(0<b<1\): a strict local maximum at \(b_-(d)\) and a strict local minimum at \(b_+(d)\), with \(0<b_-<b_+<1\). There are no other positive-coupling stationary points.
- The critical pair is the unique solution of \(P(z_\star,d_\star)=\partial_zP(z_\star,d_\star)=0\) with \(0<z_\star<1\), \(d_\star>0\), where the explicit polynomial \(P\) is given below. Numerically,
  \[
  d_\star=33.219537333378728952\ldots,\qquad
  z_\star=0.138938640448661823\ldots,\qquad
  \sqrt{z_\star}=0.372744738995283236\ldots.
  \]
- As the noise ratio diverges,
  \[
  b_-(d)=\frac{2}{\sqrt{3d}}+O(d^{-3/2}),\qquad
  b_+(d)\longrightarrow\sqrt{\frac{9-\sqrt{57}}4}=0.602114\ldots.
  \]
  The pair is born with a square-root opening: for \(d\downarrow d_\star\) from above,
  \[
  b_\pm(d)^2=z_\star\pm\kappa\sqrt{d-d_\star}+O(d-d_\star),\qquad
  \kappa=\sqrt{-\frac{2\,\partial_dP(z_\star,d_\star)}{\partial_{zz}P(z_\star,d_\star)}}>0.
  \]

The result quantifies exactly when increasing the coupling ceases to increase the information about that coupling, and determines the full turning-point geometry. The stationary covariance and Fisher-information formula themselves are prior results and are not claimed as new.

## Assumptions and scope

For independent standard Brownian motions \(W_1,W_2\), take
\[
 dX_t=-K_bX_t\,dt+\sqrt2\begin{pmatrix}1&0\\0&\sqrt{1+d}\end{pmatrix}dW_t,\qquad
 K_b=\begin{pmatrix}1&b\\b&1\end{pmatrix},\qquad -1<b<1,\quad d\geq0.
\]
The thermal intensity and diagonal trap stiffness are set to one, as in the dimensionless model of Nascimento and Morgado. Both relaxation eigenvalues \(1\pm b\) are strictly positive, so the unique stationary law is centered Gaussian with positive-definite covariance \(\Sigma(b,d)\). The Fisher information is computed from one exact stationary observation of **both coordinates**, assuming \(d\) known while estimating \(b\):
\[
 \mathcal I_{bb}=\frac12\operatorname{tr}\bigl(\Sigma^{-1}\partial_b\Sigma\,\Sigma^{-1}\partial_b\Sigma\bigr).
\]
It is not the Schur-complement information for estimating \(b\) with unknown nuisance \(d\), and it is not pathwise Fisher information from a sampled trajectory.

## Proof

**1. Independent reconstruction of the stationary information.** The Lyapunov equation
\[
 K_b\Sigma+\Sigma K_b=2\operatorname{diag}(1,1+d)
\]
has the unique solution
\[
 \Sigma=\frac1{2(1-b^2)}
 \begin{pmatrix}
 2+d b^2&-b(2+d)\\
 -b(2+d)&2+(2-b^2)d
 \end{pmatrix}.
\]
The Gaussian Fisher identity gives, upon setting \(z=b^2\),
\[
 F(z,d):=\mathcal I_{bb}(\sqrt z,d)
 =\frac{(d+2)^2\left[4(1+d)(1+z)+d^2z(3-z)\right]}{(1-z)^2\left[4(1+d)+d^2z\right]^2},\qquad 0\leq z<1.
\]
These reproduce the stationary covariance and diagonal Fisher-information formula in the cited 2026 paper. Their derivation is checked independently in the included exact-symbolic program.

**2. Reduction to a concave cubic.** Exact differentiation yields
\[
 \partial_zF(z,d)=\frac{(d+2)^2P(z,d)}{(z-1)^3\left(d^2z+4d+4\right)^3},
\]
where
\[
\begin{aligned}
P(z,d)={}&2d^4z^3-(9d^4+12d^3+12d^2)z^2\\
&+(3d^4-16d^3-32d^2-32d-16)z\\
&-(4d^3+52d^2+96d+48).
\end{aligned}
\]
The denominator is negative for \(0\le z<1\), so the sign of \(\partial_zF\) is the opposite of the sign of \(P\). Moreover,
\[
 P(0,d)=-4(d+1)(d^2+12d+12)<0,\quad
 P(1,d)=-4(d+2)^4<0,
\]
and for \(d>0\) and \(0\le z\le1\),
\[
 \partial_{zz}P=12d^4z-18d^4-24d^3-24d^2<0.
\]
Thus \(P\) is strictly concave in the physical interval; any positive region is one interval bounded by exactly two simple zeros, and zero maximum entails a unique double zero. At \(d=0\), \(P(z,0)=-16z-48<0\).

**3. Exactly one threshold.** For \(d>0\), write
\[
 \frac{P(z,d)}{d^4}=A(z)-\frac{B_1(z)}d-\frac{B_2(z)}{d^2}-\frac{B_3(z)}{d^3}-\frac{B_4(z)}{d^4},
\]
where
\[
\begin{aligned}
&A(z)=2z^3-9z^2+3z,\\
&B_1(z)=12z^2+16z+4,\quad B_2(z)=12z^2+32z+52,\\
&B_3(z)=32z+96,\qquad B_4(z)=16z+48.
\end{aligned}
\]
All four \(B_j\) are uniformly strictly positive on \([0,1]\). Therefore the maximum
\[
 H(d)=\max_{0\le z\le1}\frac{P(z,d)}{d^4}
\]
is continuous and **strictly increasing** in \(d>0\). As \(d\downarrow0\), it tends to \(-\infty\); as \(d\to\infty\), it tends to \(\max_{[0,1]}A>0\), since \(A(z)>0\) for sufficiently small positive \(z\). Thus there is exactly one \(d_\star\) satisfying \(H(d_\star)=0\). Because the endpoint values of \(P\) are negative, the maximum at equality is an interior point \(z_\star\), with \(P=\partial_zP=0\). Strict concavity ensures that this pair is unique and that for \(d>d_\star\) precisely two interior roots \(z_-<z_+\) exist. The sign sequence \(-,+,-\) for \(P\) gives the asserted maximum followed by minimum for \(F\), while \(P<0\) below threshold gives strict monotonicity. At threshold the derivative vanishes only at one point and is positive elsewhere, so monotonicity remains strict.

**4. Singular limits.** Strict concavity of \(A\) on \([0,1]\) and its zeros at \(0\) and \((9-\sqrt{57})/4\) imply by uniform convergence that the roots \(z_-(d),z_+(d)\) converge to those two values as \(d\to\infty\). Balancing the leading terms \(3z\) and \(-4/d\) in \(P/d^4\) near zero gives
\[
 z_-(d)=\frac{4}{3d}+O(d^{-2}),\qquad
 z_+(d)=\frac{9-\sqrt{57}}4+O(d^{-1}).
\]
Taking square roots proves the claimed large-noise limits. Finally, \(\partial_d(P/d^4)>0\) at every interior point; at the critical root \(P=0\), this implies \(\partial_dP(z_\star,d_\star)>0\). Together with \(\partial_{zz}P(z_\star,d_\star)<0\), Taylor expansion at the nondegenerate double root gives the stated square-root splitting with an \(O(d-d_\star)\) remainder.

## Verification

Run `python verify.py` with Python, SymPy and mpmath. The checker rebuilds the covariance from the exact Lyapunov equation, calculates all three stationary Fisher entries from the Gaussian trace formula, verifies the derivative and normalized polynomial identities exactly, checks 152 rational derivative signs, and recomputes the critical double root to 50-digit working precision. The observed critical values are numerical approximations to an algebraically uniquely defined pair; they are not assumed in the proof. The exact root-count, uniqueness and asymptotics are proved analytically above rather than inferred from finite experiments.

## Relationship to prior work

Nascimento and Morgado, arXiv:2610.20963 (first submitted 2026-10-14), give the same dimensionless Langevin model, stationary covariance and full stationary Fisher matrix; their Eq. (26) is exactly \(F\) above. They observe qualitatively that sufficiently large added noise can create nonmonotonic dependence on coupling, without giving an onset threshold, an all-parameter count of extrema, or the singular branch asymptotics established here. This finding **does not claim novelty** for the Gaussian formula, its ordinary differentiation, the existence of nonmonotonicity, or the large-coupling divergence. Its claim is the unique sharp transition and global turning-point classification, including square-root bifurcation and large-noise branches.

Matsumoto, Sasa and Dechant, arXiv:2504.09981, consider the information-thermodynamic *learning rate matrix* of a Brownian gyrator. It is built from spatial probability currents and entropy flow, not the Fisher metric of the statistical parameter \(b\). Its Brownian-gyrator example consequently does not imply the parameter-information bifurcation here. The source's exact formula nevertheless provides an important potential priority limitation: the claimed classification follows from further nontrivial analysis of that formula, and should not be represented as a new probability law.

## Limitations

The result is restricted to the linear, stable, two-coordinate Gaussian model, stationary single-snapshot measurements of both coordinates, and known added-noise intensity. It does not describe transient FI, trajectory-level inference, nonlinear traps, or the joint-estimation Cramér–Rao bound when added-noise intensity is unknown. The critical intensity depends on the normalization where baseline thermal intensity is one; in physical units it applies to the *ratio* of added to baseline noise. The numeric constants are not independently certified by interval arithmetic, though their defining uniqueness is proved and symbolic identities are exact. Novelty is a qualified claim relative to the inspected literature, not a proof of exhaustive publication priority.

## References

1. E. S. Nascimento and W. A. M. Morgado, *Fisher information analysis of a Langevin System with Thermal and Athermal Noise*, arXiv:2610.20963v1 (first public 2026-10-14), https://arxiv.org/abs/2610.20963 and https://arxiv.org/html/2610.20963.
2. K. Matsumoto, S.-i. Sasa and A. Dechant, *Learning rate matrix and information-thermodynamic trade-off relation*, arXiv:2504.09981v3 (2025), https://arxiv.org/html/2504.09981v3.
