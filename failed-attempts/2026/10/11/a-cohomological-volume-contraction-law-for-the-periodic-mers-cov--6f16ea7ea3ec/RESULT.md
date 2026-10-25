# A cohomological volume-contraction law for the periodic MERS-CoV model
## Finding
For the periodic in-host MERS-CoV model
\[
\dot T=\lambda(t)-eta(t)D vT-d(t)T,\qquad
\dot I=eta(t)D vT-d_1(t)I,
\]
\[
\dot v=d_1(t)M(t)I-c(t)v,\qquad
\dot D=\lambda_1(t)-eta_1(t)eta(t)D vT-\gamma(t)D,
\]
let \(\Phi(t)\) be the principal fundamental matrix of the variational equation along a positive solution, normalized by \(\Phi(0)=I_4\). Then
\[
\det\Phi(t)=rac{T(t)D(t)}{T(0)D(0)}
\exp\!\left[-\int_0^t\left(d_1(s)+c(s)+rac{\lambda(s)}{T(s)}+rac{\lambda_1(s)}{D(s)}ight)\,dsight].
\]
Hence, if the solution is strictly positive and \(\omega\)-periodic,
\[
\det\Phi(\omega)=
\exp\!\left[-\int_0^\omega\left(d_1(t)+c(t)+rac{\lambda(t)}{T(t)}+rac{\lambda_1(t)}{D(t)}ight)\,dtight]
<
\exp\!\left[-\int_0^\omega(d_1(t)+c(t))\,dtight]<1.
\]
If \(\mu_1,\ldots,\mu_4\) are the Floquet multipliers of the stroboscopic monodromy matrix, then
\[
\prod_{j=1}^4|\mu_j|=\det\Phi(\omega),
\]
so at least one multiplier satisfies
\[
|\mu_j|<\exp\!\left[-rac14\int_0^\omega(d_1(t)+c(t))\,dtight].
\]
Thus every positive locked cycle has a rigorously contracting tangent direction; in particular it cannot be a fully repelling periodic orbit.

## Assumptions and scope
The coefficient functions are the positive continuous \(\omega\)-periodic functions used in the source model. Positivity of \(T(t)\) and \(D(t)\) on the time interval under consideration is required because the proof uses \(\log T\) and \(\log D\). No differentiability of the coefficient functions beyond continuity is needed. The finite-time identity applies to every positive solution, not only periodic ones.

The Floquet conclusion concerns a strictly positive solution with the same period \(\omega\) as the coefficients. It is a determinant constraint on the four-dimensional stroboscopic monodromy matrix. It does not assert that all four multipliers lie inside the unit circle.

## Proof
The Jacobian trace of the vector field along a positive trajectory is
\[
\operatorname{tr}J(t)
=-d(t)-d_1(t)-c(t)-\gamma(t)-eta(t)D(t)v(t)-eta_1(t)eta(t)v(t)T(t).
\]
The first and fourth state equations give the logarithmic identities
\[
rac{d}{dt}\log T
=rac{\lambda(t)}{T(t)}-eta(t)D(t)v(t)-d(t),
\]
\[
rac{d}{dt}\log D
=rac{\lambda_1(t)}{D(t)}-eta_1(t)eta(t)v(t)T(t)-\gamma(t).
\]
Substitution yields the pointwise cohomological identity
\[
\operatorname{tr}J(t)
=-\left(d_1(t)+c(t)+rac{\lambda(t)}{T(t)}+rac{\lambda_1(t)}{D(t)}ight)
+rac{d}{dt}\log(T(t)D(t)).
\]
Liouville's formula for the variational equation gives
\[
\det\Phi(t)=\exp\!\left(\int_0^t\operatorname{tr}J(s)\,dsight).
\]
Integrating the cohomological identity therefore gives the finite-time determinant formula in the finding.

For an \(\omega\)-periodic positive solution, \(T(\omega)D(\omega)=T(0)D(0)\), so the endpoint ratio is one. Every integrand \(\lambda/T\) and \(\lambda_1/D\) is strictly positive, which gives the strict upper bound by deleting those two terms. Finally, Liouville's formula identifies the determinant with the product of the four Floquet multipliers; because the determinant is positive, its value equals the product of their moduli. If all four moduli were at least the fourth root of the displayed baseline bound, their product would contradict the strict determinant inequality.

## Verification
The bundled `verify.py` reconstructs the pointwise cohomological identity with an exact symbolic linear-combination checker using only the Python standard library. It also evaluates the source's coefficient averages in the baseline multiplier bound, obtaining
\[
\exp\!\left[-\int_0^{\pi/5}(d_1(t)+c(t))\,dtight]
=0.904357108638\ldots.
\]
A separate numerical replay of the source's displayed coefficient set, initialized from the displayed state and converged to its forcing-locked cycle, gave a monodromy determinant \(0.665268082639\ldots\); direct quadrature of the exact formula agreed to about \(7	imes10^{-13}\). This numerical value is an illustration only and is not used in the proof.

## Relationship to prior work
Keyoumu, Ma, and Guo introduce the periodic four-dimensional MERS-CoV/DPP4 system and prove existence of a positive periodic solution by coincidence degree. Their proof integrates the state equations to obtain a-priori bounds, but it does not state a variational determinant or Floquet-product law. Tang, Ma, and Bai study the autonomous predecessor and prove equilibrium stability, not the seasonal positive-cycle monodromy identity. The later CTL extension again focuses on existence of periodic oscillations and does not state this determinant law.

Earlier within-host virus literature uses Floquet theory for periodic therapy, notably at infection-free periodic states. That general methodology does not imply the source-specific cancellation
\[
\operatorname{tr}J+ d_1+c+\lambda/T+\lambda_1/D=rac{d}{dt}\log(TD),
\]
which is the step that removes the infection-incidence terms from the full nonlinear positive-cycle determinant.

## Limitations
The determinant being smaller than one does not imply asymptotic stability of a four-dimensional periodic solution: some multipliers may still have modulus greater than one. The result gives no existence, uniqueness, or bifurcation theorem beyond the source's own existence result. It also does not cover trajectories that hit \(T=0\) or \(D=0\), because the logarithmic reduction is then unavailable.

The web and indexed-literature checks did not locate this exact source-specific determinant identity, but search cannot prove absolute novelty. A residual risk is that an unindexed treatment of the same model may contain an equivalent Floquet-product calculation.

## References
1. T. Keyoumu, W. Ma, K. Guo, “Existence of positive periodic solutions for a class of in-host MERS-CoV infection model with periodic coefficients,” *AIMS Mathematics* 7 (2022), 3083–3096, DOI `10.3934/math.2022171`. Public source date: 2021-11-24.
2. S. Tang, W. Ma, P. Bai, “A Novel Dynamic Model Describing the Spread of the MERS-CoV and the Expression of Dipeptidyl Peptidase 4,” *Computational and Mathematical Methods in Medicine* (2017), Article 5285810, DOI `10.1155/2017/5285810`.
3. T. Keyoumu, K. Guo, W. Ma, “Periodic oscillation for a class of in-host MERS-CoV infection model with CTL immune response,” *Mathematical Biosciences and Engineering* 19 (2022), 12247–12259, DOI `10.3934/mbe.2022570`.
4. C. J. Browne, S. S. Pilyugin, “Periodic multidrug therapy in a within-host virus model,” *Bulletin of Mathematical Biology* 74 (2012), 562–589, DOI `10.1007/s11538-011-9677-x`.
