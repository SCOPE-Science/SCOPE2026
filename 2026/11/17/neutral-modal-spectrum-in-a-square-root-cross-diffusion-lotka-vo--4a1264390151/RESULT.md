# Neutral modal spectrum in a square-root cross-diffusion Lotka–Volterra system

## Finding

For the square-root cross-diffusion Lotka–Volterra PDE (27) of Broadbridge–Cherniha–Goard, let \(A=-d_{12}>0\), \(B=d_{21}>0\), \(k_1,k_2>0\), and let a Laplacian mode satisfy \(-\Delta\varphi=q^2\varphi\) with \(q^2\ge0\). The linearization at the positive homogeneous equilibrium \((k_1,k_2)\) has eigenvalues
\[
\lambda_\pm(q)=\pm i\omega(q),\qquad
\omega(q)^2=\left(1+\frac{Aq^2}{\sqrt{k_2}}\right)\left(1+\frac{Bq^2}{\sqrt{k_1}}\right).
\]
Thus every such spatial mode is spectrally neutral and its frequency strictly increases with \(q^2\); unlike the conventional diagonal-diffusion Lotka–Volterra PDE, every nonzero spatial mode lacks linear exponential damping. This claim concerns the linearized homogeneous-boundary problem only, not nonlinear stability or the paper's mixed-boundary example.

## Assumptions and scope

Use equation (27) in the cited model, with \(d_{12}<0\), \(d_{21}>0\), \(k_1,k_2>0\), and set \(A=-d_{12}\), \(B=d_{21}\). The calculation is for perturbations of the positive constant equilibrium \((\theta_1,\theta_2)=(k_1,k_2)\) on a domain with common periodic or homogeneous Neumann boundary conditions, so that the Laplacian has modes \(-\Delta\varphi=q^2\varphi\), \(q^2\ge0\). It does not analyze the paper's mixed, time-dependent boundary forcing, and it makes no nonlinear stability or global well-posedness claim.

## Proof

With the notation above, the two equations in (27) can be written
\[
\begin{aligned}
\partial_t\theta_1&=-2A\Delta\sqrt{\theta_2}
+\frac{2A}{B}\sqrt{\theta_1}\bigl(\sqrt{\theta_2}-\sqrt{k_2}\bigr),\\
\partial_t\theta_2&=2B\Delta\sqrt{\theta_1}
+\frac{2B}{A}\sqrt{\theta_2}\bigl(\sqrt{k_1}-\sqrt{\theta_1}\bigr).
\end{aligned}
\]
The reaction terms vanish at \((k_1,k_2)\). Write \(\theta_1=k_1+u\), \(\theta_2=k_2+v\) and retain only first-order terms. Since
\[
\sqrt{k_j+w}=\sqrt{k_j}+\frac{w}{2\sqrt{k_j}}+O(w^2),
\]
the linearized system is
\[
\begin{aligned}
u_t&=-\frac{A}{\sqrt{k_2}}\Delta v
+\frac{A}{B}\sqrt{\frac{k_1}{k_2}}\,v,\\
v_t&=\frac{B}{\sqrt{k_1}}\Delta u
-\frac{B}{A}\sqrt{\frac{k_2}{k_1}}\,u.
\end{aligned}
\]
On a mode with \(-\Delta=q^2\), the modal matrix is
\[
M(q)=
\begin{pmatrix}
0 & \dfrac{A}{B}\sqrt{\dfrac{k_1}{k_2}}+\dfrac{Aq^2}{\sqrt{k_2}}\\
-\dfrac{B}{A}\sqrt{\dfrac{k_2}{k_1}}-\dfrac{Bq^2}{\sqrt{k_1}} & 0
\end{pmatrix}.
\]
Its trace is zero. Because the off-diagonal entries have opposite signs, their product is negative; hence the positive determinant is
\[
\det M(q)=
\left(\frac{A}{B}\sqrt{\frac{k_1}{k_2}}+\frac{Aq^2}{\sqrt{k_2}}\right)
\left(\frac{B}{A}\sqrt{\frac{k_2}{k_1}}+\frac{Bq^2}{\sqrt{k_1}}\right)
=\left(1+\frac{Aq^2}{\sqrt{k_2}}\right)
\left(1+\frac{Bq^2}{\sqrt{k_1}}\right).
\]
Therefore the characteristic equation is \(\lambda^2+\omega(q)^2=0\), yielding the stated eigenvalues. Both factors in \(\omega(q)^2\) are positive and strictly increasing as functions of \(q^2\), so \(\omega(q)>0\) and the frequency strictly increases with \(q^2\).

For comparison, the conventional diagonal-diffusion Lotka–Volterra linearization at a positive coexistence equilibrium has modal matrix
\[
J_{\mathrm{LV}}(q)=
\begin{pmatrix}
-D_1q^2 & a\\
-b & -D_2q^2
\end{pmatrix},
\qquad a,b,D_1,D_2>0.
\]
For \(q^2>0\), its trace is \(-q^2(D_1+D_2)<0\) and its determinant is \(D_1D_2q^4+ab>0\), which forces both eigenvalues to have negative real part. The cross-diffusion model instead has a purely imaginary pair for every \(q^2\ge0\). This comparison concerns the full linearized PDEs with the stated boundary-mode assumptions, not just their spatially homogeneous reaction systems.

## Verification

The equilibrium substitution, first derivatives of the square-root reaction terms, and the modal determinant were checked symbolically from the displayed equations. The determinant factors exactly as \(\left(1+Aq^2/\sqrt{k_2}\right)\left(1+Bq^2/\sqrt{k_1}\right)\); no numerical fitting or finite-mode enumeration is used. The standard diagonal-diffusion comparison follows from its trace and determinant, not from numerical eigenvalue sampling.

## Relationship to prior work

Broadbridge, Cherniha and Goard derive the square-root cross-diffusion system in equation (27), give exact oscillatory solutions in their equation (29), and state that the stability status of steady states is the same as in the standard diffusive Lotka–Volterra model while perturbation rates differ. The modal formula above is a parameter-uniform linearization result for every Laplacian eigenvalue, not one of those exact solution families. It shows that the phrase “same stability status” must be restricted to the homogeneous reaction subsystem if it is intended to mean asymptotic damping of spatial modes: the conventional diagonal-diffusion model damps every nonzero mode, whereas equation (27) has no linear exponential damping for any mode.

## Limitations

The result is a linear spectral statement at a positive homogeneous equilibrium. It does not prove nonlinear Lyapunov stability, nonlinear well-posedness, existence of nonlinear patterns, or stability under the paper's mixed time-dependent boundary conditions. The literature comparison is best-knowledge rather than a proof of global novelty; the full 24-page preprint has been inspected for possible equivalent modal statements, but an unindexed equivalent analysis may still exist.

## References

1. Broadbridge, Cherniha and Goard, “Exact nonclassical symmetry solutions of Lotka–Volterra-type population systems,” *European Journal of Applied Mathematics*, published online 25 November 2022. DOI: https://doi.org/10.1017/S095679252200033X.
2. Author preprint: arXiv:2403.02644v1, first posted 5 March 2024, https://arxiv.org/abs/2403.02644.
