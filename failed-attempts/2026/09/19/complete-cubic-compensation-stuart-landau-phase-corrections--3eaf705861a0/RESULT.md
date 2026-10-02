# Complete cubic compensation of second-order Stuart–Landau phase corrections

## Statement

Consider the three identical Stuart–Landau oscillators treated explicitly in arXiv:2609.20632v1,
\[
\dot z_j=(a+ib)z_j-|z_j|^2z_j+\varepsilon e^{i\varrho}\sum_{k\ne j}w_{jk}z_k,
\qquad a>0,
\]
with straight isochrones, no self-coupling, and limit-cycle radius \(R=\sqrt a\). The source derives
\[
\dot\theta_j=\omega+\varepsilon f_j^{(1)}+\varepsilon^2f_j^{(2)}+O(\varepsilon^3)
\]
and proposes a restricted family of resonant cubic physical nonpairwise couplings that cancels only part of \(f_j^{(2)}\).

There is a larger resonant cubic controller that cancels the entire explicit second-order phase correction. For any distinct \(j,k,l\in\{1,2,3\}\), define
\[
\begin{aligned}
H_j=\frac{1}{4aR^2}\Big[&
-e^{2i\varrho}\big(
w_{jk}w_{kj}z_jz_k\bar z_k+
w_{jl}w_{lj}z_jz_l\bar z_l
\big)\\
&-e^{2i\varrho}\big(
w_{jk}w_{kl}z_jz_l\bar z_j+
w_{jl}w_{lk}z_jz_k\bar z_j
\big)\\
&-w_{jk}w_{kl}z_k^2\bar z_l
-w_{jl}w_{lk}z_l^2\bar z_k\\
&+2e^{2i\varrho}w_{jk}w_{jl}z_kz_l\bar z_j\\
&+\big(e^{2i\varrho}w_{jk}^2-w_{jk}w_{kj}\big)z_k^2\bar z_j\\
&+\big(e^{2i\varrho}w_{jl}^2-w_{jl}w_{lj}\big)z_l^2\bar z_j
\Big].
\end{aligned}
\]
Then the engineered physical system
\[
\dot z_j=(a+ib)z_j-|z_j|^2z_j
+\varepsilon e^{i\varrho}\sum_{k\ne j}w_{jk}z_k
+\varepsilon^2 H_j
\]
has phase dynamics
\[
\boxed{
\dot\theta_j=\omega+\varepsilon f_j^{(1)}+O(\varepsilon^3).
}
\]
Thus the second-order correction is exactly removable within the class of resonant cubic polynomial couplings. The partial cancellation reported by the source is a consequence of its restricted controller family, not a structural obstruction of resonant cubic coupling.

A key missing phase channel is
\[
\boxed{
z_k^2\bar z_j
\quad\longmapsto\quad
\sin\!\big(2\theta_k-2\theta_j+\xi\big).
}
\]
This is a nonlinear pairwise second harmonic. The source states that its displayed list enumerates the resonant cubic cases, but in the subsection on nonlinear pairwise coupling it lists only first-harmonic representatives. The \(z_k^2\bar z_j\) class is not included there, although it is permitted by the source's own general cubic formula \(z_pz_q\bar z_r\).

## Proof

For straight isochrones, the first-order phase projection of a perturbation \(H_j\) on the unperturbed cycle \(z_m=Re^{i\theta_m}\) is
\[
\mathcal P_j[H_j]
=
\frac1R\operatorname{Im}\!\left(e^{-i\theta_j}H_j\right).
\]
Hence a cubic monomial
\[
Cz_pz_q\bar z_r
\]
contributes
\[
R^2\operatorname{Im}
\left(
C e^{i(\theta_p+\theta_q-\theta_r-\theta_j)}
\right).
\]
Under the global phase rotation \(z_m\mapsto e^{i\phi}z_m\), the monomial transforms as \(z_k^2\bar z_j\mapsto e^{i\phi}z_k^2\bar z_j\), so it has the required \(S^1\)-equivariance. In particular,
\[
z_k^2\bar z_j
\mapsto
R^2\sin(2\theta_k-2\theta_j+\arg C),
\]
so the pairwise second harmonic is directly realizable by a resonant cubic physical coupling.

For \(j=1\), the source's explicit second-order correction is
\[
\begin{aligned}
4af_1^{(2)}={}&
w_{12}w_{21}\!\left[\sin2\varrho+\sin2(\theta_2-\theta_1)\right]\\
&+w_{12}w_{23}\!\left[
\sin(\theta_3-\theta_1+2\varrho)
+\sin(2\theta_2-\theta_3-\theta_1)\right]\\
&+w_{13}w_{31}\!\left[\sin2\varrho+\sin2(\theta_3-\theta_1)\right]\\
&+w_{13}w_{32}\!\left[
\sin(\theta_2-\theta_1+2\varrho)
+\sin(2\theta_3-\theta_2-\theta_1)\right]\\
&-w_{12}^2\sin(2(\theta_2-\theta_1)+2\varrho)\\
&-2w_{12}w_{13}\sin(\theta_2+\theta_3-2\theta_1+2\varrho)\\
&-w_{13}^2\sin(2(\theta_3-\theta_1)+2\varrho).
\end{aligned}
\]
Projecting the stated \(H_1\) term by term gives exactly the negative of this expression. The two coefficients
\[
e^{2i\varrho}w_{12}^2-w_{12}w_{21},
\qquad
e^{2i\varrho}w_{13}^2-w_{13}w_{31}
\]
combine, in one cubic monomial per neighbor, the shifted and unshifted pairwise second harmonics. The remaining cubic terms cancel the constant, first-harmonic, asymmetric \((2,-1,-1)\), and symmetric \((1,1,-2)\) contributions. Therefore
\[
\boxed{\mathcal P_j[H_j]=-f_j^{(2)}}.
\]

Because \(H_j\) is multiplied by \(\varepsilon^2\), only its first-order phase projection contributes at order \(\varepsilon^2\). Cross terms between the original \(O(\varepsilon)\) linear coupling and the new controller are \(O(\varepsilon^3)\), consistent with the order counting used by the source for its own engineered coupling. Therefore the full \(O(\varepsilon^2)\) term cancels.

## Cubic phase-signature completeness

For fixed target oscillator \(j\), a resonant cubic monomial \(z_pz_q\bar z_r\) has phase wavevector
\[
e_p+e_q-e_r-e_j.
\]
For three oscillators, the source's \(f_j^{(2)}\) uses only phase signatures belonging to this cubic image. The source already identifies cubic representatives for the constant, first-harmonic, and two nonpairwise signatures. The pairwise second-harmonic vectors
\[
-2e_j+2e_k
\]
are supplied by \(z_k^2\bar z_j\). Consequently the full explicit second-order correction lies in the first-order phase image of resonant cubic polynomials.

This observation is narrower than a general inverse-design theorem: it says that the particular correction in arXiv:2609.20632v1 can be removed while staying inside the simple \(S^1\)-equivariant cubic polynomial class used in that paper.

## Relation to prior work

General synchronization engineering and inverse phase-coupling design are established topics. Kori et al. developed nonlinear-feedback constructions for prescribed phase interaction functions, and Namura, Muolo, and Nakao later designed interaction functions that realize prescribed pairwise and higher-order Kuramoto dynamics for arbitrary smooth limit-cycle oscillators. Those general inverse-design principles are not claimed as new here.

Likewise, resonant cubic terms and second harmonics in Stuart–Landau normal forms are standard objects. The novelty claim is source-specific: the resonant cubic enumeration in arXiv:2609.20632v1 omits the \(z_k^2\bar z_j\) second-harmonic class, and including that class together with the other cubic signatures yields the explicit complete compensator above for the paper's Eq. (55).

The source's own design conclusion remains correct for its deliberately restricted two-type physical-nonpairwise controller with a single strength parameter. What changes is the broader conclusion: exact compensation is possible once the full resonant cubic coupling class is allowed.

## Limitations

The result applies to the explicit straight-isochrone, \(c=-1\), three-oscillator, no-self-coupling reduction used for Eq. (55) of arXiv:2609.20632v1. It does not prove that the same cubic formula works for curved isochrones, heterogeneous oscillators, or arbitrary oscillator models. It cancels the phase dynamics through second order only; the engineered physical system generally has nonzero \(O(\varepsilon^3)\) corrections.

The complete proof body of Namura–Muolo–Nakao (2026) was not fully inspected. Its accessible abstract establishes a broad exact interaction-design framework, so broad claims of novelty for exact phase-model synthesis are excluded. The present claim is restricted to the missing cubic phase class and the explicit source-specific polynomial compensator.

## Verification

`artifacts/verify_cubic_phase_cancellation.py` symbolically reconstructs the source's \(f_1^{(2)}\), independently projects every term of \(H_1\), and simplifies the sum to zero. It also exhausts the symmetric cubic monomials \(z_pz_q\bar z_r\) for oscillator 1 and confirms the second-harmonic phase vectors generated by \(z_2^2\bar z_1\) and \(z_3^2\bar z_1\).

## References

1. R. Muolo, H. Nakao, and C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1 (2026), https://arxiv.org/abs/2609.20632
2. E. Gengel, E. Teichmann, M. Rosenblum, and A. Pikovsky, *High-order phase reduction for coupled oscillators*, Journal of Physics: Complexity 2, 015005 (2021), https://doi.org/10.1088/2632-072X/abbed2
3. H. Kori, C. G. Rusin, I. Z. Kiss, and J. L. Hudson, *Synchronization engineering: theoretical framework and application to dynamical clustering*, Chaos 18, 026111 (2008), https://doi.org/10.1063/1.2927531
4. N. Namura, R. Muolo, and H. Nakao, *Optimal interaction functions realizing higher-order Kuramoto dynamics with arbitrary limit-cycle oscillators*, Chaos 36, 023120 (2026), https://doi.org/10.1063/5.0307452
5. I. León, R. Muolo, Y. Zhang, and M. Lucas, *Symmetry-based selection rules for higher-order interactions in coupled oscillators*, arXiv:2606.04904 (2026), https://arxiv.org/abs/2606.04904
