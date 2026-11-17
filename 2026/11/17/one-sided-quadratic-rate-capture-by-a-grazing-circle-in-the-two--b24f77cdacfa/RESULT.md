# One-sided quadratic-rate capture by a grazing circle in the two-neuron Matsuoka flow

## Finding
At the marginal-center parameter of a rectified two-neuron Matsuoka model, the outermost orbit of an exact inner periodic annulus is approached from immediately outside at a **sharp inverse-square rate in the number of returns**. The leading constant is explicit and doubles in the return-map loss when both neurons graze simultaneously.

Let \(L_c\) be the smaller of the two first-grazing amplitudes, let \(m\in\{1,2\}\) be the number of neurons attaining that minimum, and put
\[
\omega=\sqrt{\frac{b-\tau_x/\tau_y}{\tau_x\tau_y}},\qquad
C=\frac{2\sqrt2\,m\sqrt{a_{12}a_{21}}}{3\tau_x\omega\sqrt{L_c}}.
\]
On the return section defined below, every sufficiently small outer perturbation \(\delta_0>0\) launched in the exact center plane has a sequence of positive amplitude excesses \(\delta_n\) satisfying
\[
\delta_{n+1}=\delta_n-C\delta_n^{3/2}+O(\delta_n^2),\qquad
\lim_{n\to\infty}n^2\delta_n=\frac4{C^2}.
\]
The amplitude does not cross into the inner annulus. The stable-mode coordinates at the successive sections are \(O(n^{-3})\). In particular the grazing orbit is one-sided attracting but remains neutrally stable toward the interior; the attraction is not exponential.

## Assumptions and scope
For \(i\ne j\) in \(\{1,2\}\), consider the autonomous four-dimensional differential equation
\[
\tau_x\dot x_i=-x_i-by_i-a_{ij}\max(x_j,0)+s_i,\qquad
\tau_y\dot y_i=-y_i+\max(x_i,0).
\]
All time constants, adaptation and inhibitory weights are positive. Assume
\[
\rho:=\sqrt{a_{12}a_{21}}=1+\frac{\tau_x}{\tau_y}<1+b,
\]
and that the unique solution \((h_1,h_2)\) of
\[
(1+b)h_1+a_{12}h_2=s_1,\qquad a_{21}h_1+(1+b)h_2=s_2
\]
has strictly positive components. This last condition is the precise interior-equilibrium assumption; no symmetric-weight or equal-input hypothesis is needed.

Introduce transformed coordinates \((P,Q,U,V)\) through
\[
\begin{aligned}
x_1&=h_1+\sqrt{a_{12}}(P+U),& y_1&=h_1+\sqrt{a_{12}}(Q+V),\\
x_2&=h_2+\sqrt{a_{21}}(P-U),& y_2&=h_2+\sqrt{a_{21}}(Q-V).
\end{aligned}
\]
Write \(\kappa^2=b\tau_y/\tau_x>1\), and define
\[
I=(U-V)^2+(\kappa^2-1)V^2,\qquad L=\sqrt{\frac{I}{1-\kappa^{-2}}},\qquad
L_1=\frac{h_1}{\sqrt{a_{12}}},\quad L_2=\frac{h_2}{\sqrt{a_{21}}},\quad L_c=\min(L_1,L_2).
\]
The section is the local oriented return section \(U=0\), \(V>0\), with \(P,Q\) near zero. For every small \(\delta_0>0\), take initial state \(P=Q=U=0\) and \(V=(L_c+\delta_0)\sqrt{\kappa^2-1}/\kappa^2\). Let \(\delta_n=L_n-L_c\), where \(L_n\) is computed from \(I\) on its \(n\)-th positive-oriented return. The theorem applies to this entire one-parameter family, and to sufficiently close initial section states satisfying the stated invariant stable-mode cone.

## Proof
**1. Linear center and stable modes.** In the jointly active region \(x_1,x_2>0\), the coordinates decouple exactly:
\[
\tau_x\dot P=-(1+\rho)P-bQ,\quad \tau_y\dot Q=P-Q,\qquad
\tau_x\dot U=(\rho-1)U-bV,\quad\tau_y\dot V=U-V.
\]
The \((P,Q)\) matrix has negative trace and positive determinant, hence exponential stability. At \(\rho=1+\tau_x/\tau_y\), the center mode obeys \(\ddot U+\omega^2U=0\), and direct differentiation gives \(\dot I=0\) there. On the exact center plane \(P=Q=0\), the central trajectory has \(U=\pm L\) at its two extrema and \(V=U/\kappa^2\) at each extremum. It remains jointly active for \(0<L\le L_c\). It is periodic with period \(T=2\pi/\omega\). At \(L=L_c\), one or both membrane potentials touch zero quadratically but never cross it; continuity of the vector field preserves the same periodic solution.

**2. Rectification forcing and its sign.** Let \(\zeta_i=(-x_i)_+\). Rewriting \(\max(x_i,0)=x_i+\zeta_i\) gives, exactly and not merely to first order, the extra center forcing
\[
\Delta\dot U=\frac{\sqrt{a_{21}}\zeta_1-\sqrt{a_{12}}\zeta_2}{2\tau_x},\qquad
\Delta\dot V=\frac{\zeta_1/\sqrt{a_{12}}-\zeta_2/\sqrt{a_{21}}}{2\tau_y}.
\]
Consequently
\[
\dot I=2(U-V)\Delta\dot U+2(\kappa^2V-U)\Delta\dot V.
\]
At a graze by neuron 1, \(U=-L_c\), and at a graze by neuron 2, \(U=L_c\); at both \(V=U/\kappa^2\). The leading action variation at either graze is strictly negative. The neutral circle is therefore attracting from the outer side.

**3. Sharp penetration integral.** For an outer amplitude \(L=L_c+\delta\) with \(\delta\downarrow0\), at each grazing extremum the freely continued active solution has an excess negative membrane potential of the form
\[
-\sqrt{a_{ij}}\left[\delta-\frac{L_c\omega^2}{2}(t-t_*)^2\right]_+ +O(\delta^{3/2})
\]
within the \(O(\sqrt\delta)\) switching interval. In the above expression only the leading parabola is used for the integral; the physical clipping and stable-coordinate displacements are \(O(\delta^{3/2})\), which change that integral by \(O(\delta^2)\). The elementary parabolic integral is
\[
\int\zeta_i(t)\,dt=\frac{4\sqrt2\sqrt{a_{ij}}}{3\omega\sqrt{L_c}}\delta^{3/2}+O(\delta^2).
\]
At each active graze, the action derivative equation therefore gives
\[
\Delta I=-\frac{4\sqrt2\rho(1-\kappa^{-2})\sqrt{L_c}}{3\tau_x\omega}\delta^{3/2}+O(\delta^2).
\]
There are \(m\) separated grazing events in one full cycle, and their leading effects add. Since \(I=(1-\kappa^{-2})L^2\), division by \(2(1-\kappa^{-2})L_c\) yields the asserted amplitude loss coefficient \(C\).

**4. From the local return to all returns.** Let \(z=(P,Q)\) on the section and \(B=\exp(M_sT)\) for the stable \((P,Q)\) matrix \(M_s\). The switching intervals above and variation of constants give the uniform local map
\[
\delta^+=\delta-C\delta^{3/2}+O(\delta^2),\qquad
z^+=Bz+O(\delta^{3/2})
\]
for \(\|z\|\le K\delta^{3/2}\), with all remainders uniform on a small one-sided section neighborhood. Indeed the stable forcing during each grazing interval has size \(O(\delta)\) and duration \(O(\sqrt\delta)\); its accumulated effect is \(O(\delta^{3/2})\), and its feedback into the parabolic clipping integral is \(O(\delta^2)\). Crossing times and the oriented section are regular away from those quadratic grazing extrema. Choose an equivalent norm in which \(\|B\|<1\) and then choose \(K\) large; shrinking the section neighborhood gives a forward invariant cone \(\|z\|\le K\delta^{3/2}\). The initial center-plane states lie in this cone.

For every sufficiently small positive \(\delta\), \(0<\delta^+<\delta\). The sequence cannot tend to a positive limit because the loss remains strictly negative; thus \(\delta_n\to0\). Defining \(w_n=\delta_n^{-1/2}\), the return map implies \(w_{n+1}-w_n=C/2+O(\delta_n^{1/2})\). Cesàro averaging yields \(w_n/n\to C/2\) and therefore \(n^2\delta_n\to4/C^2\). The cone yields \(z_n=O(\delta_n^{3/2})=O(n^{-3})\). This proves the claim without assuming a priori that infinitely many outer excursions persist.

## Verification
Run `python check.py` from the supplied package with NumPy, SciPy and SymPy installed. The checker verifies algebraic conservation and stable-mode matrix identities, then evaluates two independently specified parameter sets, with one and two simultaneous grazes. As outer excess decreases from \(0.002\) to \(0.0002\), the measured one-period loss divided by \(\delta^{3/2}\) approaches \(5.008270656\ldots\) in the one-graze case and \(8.373081115\ldots\) in the two-graze case. The checker intentionally performs finite diagnostics only; the infinite inverse-square assertion is proved above.

## Relationship to prior work
Muramatsu and Kori, arXiv:2405.08409 (2024), Eq. (30i) and Section V, identify the exact center threshold and describe the outermost grazing circle as attracting from outside and neutral inside. Those qualitative facts are credited rather than presented as new. The present contribution is the explicit **one- versus two-graze loss coefficient**, its asymmetric-weight formula, and the resulting sharp \(n^{-2}\) approach law with a stable-mode \(n^{-3}\) estimate.

The general grazing-normal-form literature of di Bernardo, Budd and Champneys (2000 preprint; 2001 Physica D) already explains the appearance of three-halves corrections for continuous piecewise-smooth flows. The three-halves exponent alone is **not** new. The result here treats a neutral periodic family (rather than a single hyperbolic cycle), computes the model-specific coefficient including the simultaneous-graze multiplicity, and closes the nonlinear iteration required for the algebraic capture constant.

## Limitations
The theorem is a local, one-sided result for sufficiently small outer perturbations of the first-grazing periodic orbit on the specific marginal-center parameter surface. It does not classify arbitrary initial states, large-amplitude motion, or other parameter surfaces; it does not assert a new generic grazing exponent. Two distinct graze times are essential to additive multiplicity, and the equality case is included explicitly. The analytic proof gives a leading-order asymptotic, not a uniform global numerical error bound. Possible mathematically equivalent specialized calculations outside inspected sources remain a literature-priority risk; independent external verification has not been performed.

## References
1. K. Muramatsu and H. Kori, *Bifurcation analysis of a two-neuron central pattern generator model for both oscillatory and convergent neuronal activities*, arXiv:2405.08409v1, 2024-05-14. https://arxiv.org/abs/2405.08409; https://doi.org/10.1063/5.0220075.
2. M. di Bernardo, C. J. Budd and A. R. Champneys, *Normal form maps for grazing bifurcations in n-dimensional piecewise-smooth dynamical systems*, Physica D 160 (2001), 222–254. https://doi.org/10.1016/S0167-2789(01)00349-9.
3. M. di Bernardo, C. J. Budd and A. R. Champneys, *Grazing and Border-Collision in Piecewise-Smooth Systems: A Unified Analytical Framework*, Phys. Rev. Lett. 86 (2001), 2553–2556. https://doi.org/10.1103/PhysRevLett.86.2553.
