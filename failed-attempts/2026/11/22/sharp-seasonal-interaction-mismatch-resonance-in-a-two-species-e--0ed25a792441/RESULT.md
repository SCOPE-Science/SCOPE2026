# Sharp seasonal interaction-mismatch resonance in a two-species ecological feedback model

## Finding

In an ecologically sign-consistent two-species community-matrix model, seasonal changes to unequal reciprocal interaction strengths can destabilize an otherwise damped predator–prey feedback at a specific frequency. The full *leading-order* instability tongue, including the necessary mismatch of environmental responses, is explicit. This separates the effects of noncommutativity, environmental timescale and demographic damping, all while each frozen-time community matrix is strictly stable.

Fix \(b,c,p,q,\kappa>0\), a detuning \(\delta\in\mathbb R\), and a sufficiently small positive \(\varepsilon\). Let \(\Omega=\sqrt{bc}\), \(\omega_\varepsilon=2\Omega+\delta\varepsilon>0\), and
\[
\frac{dx}{dt}=A_\varepsilon(t)x,\qquad
A_\varepsilon(t)=-\kappa\varepsilon I+
\begin{pmatrix}0&b\\-c&0\end{pmatrix}+
\varepsilon\cos(\omega_\varepsilon t)
\begin{pmatrix}0&p\\-q&0\end{pmatrix}.
\]
Here \(x\in\mathbb R^2\) is a vector of *linear perturbations*, not raw species densities. Define the interaction-response mismatch
\[
D=\frac{pc-bq}{2\sqrt{bc}},
\]
and the maximal real Floquet exponent of the period-\(T_\varepsilon=2\pi/\omega_\varepsilon\) evolution by
\[
\Lambda_\varepsilon=\frac{1}{T_\varepsilon}\log\rho(M_\varepsilon),
\]
where \(M_\varepsilon\) is the fundamental matrix at the end of one period, initialized at the identity.

**Theorem (sharp first-order seasonal tongue).** For every fixed admissible \(b,c,p,q,\kappa,\delta\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Lambda_\varepsilon}{\varepsilon}=-\kappa+\frac12\sqrt{\max\{D^2-\delta^2,0\}}.}
\]
Consequently, if \(\delta^2+4\kappa^2<D^2\), the Floquet exponent is strictly positive for all sufficiently small positive \(\varepsilon\); if \(\delta^2+4\kappa^2>D^2\), it is strictly negative for all sufficiently small positive \(\varepsilon\). No assertion on the equality locus is implied by this first-order classification. For all \(0<\varepsilon<\min\{b/p,c/q\}\), *every* frozen matrix \(A_\varepsilon(t)\) has both eigenvalues with negative real part \(-\kappa\varepsilon\), including in the Floquet-unstable regime. At fixed \(\kappa\), the leading-order unstable detuning interval is nonempty exactly when \(|D|>2\kappa\), in which case it is \(|\delta|<\sqrt{D^2-4\kappa^2}\). The *resonant forcing coefficient* is zero exactly when the two interaction matrices commute, equivalently \(pc=bq\). In this commuting case the Floquet exponent is exactly \(-\kappa\varepsilon\) for every positive forcing frequency and amplitude (even without the smallness restriction).

**Exact comparison of two frequencies.** If \(b=c=1\), \(p=2\), \(q=1/2\), \(\kappa=1/4\), and \(\delta=0\), then \(D=3/4\). At \(\omega=2\),
\[
\Lambda_\varepsilon=\frac{\varepsilon}{8}+O(\varepsilon^2)>0.
\]
For the same parameters and every sufficiently small positive \(\varepsilon\), at fixed \(\omega=4\),
\[
\Lambda_\varepsilon=-\frac{\varepsilon}{4}<0.
\]
Thus seasonal timing alone reverses linear stability without changing either the frozen-time sign pattern or the environmental forcing amplitudes.

## Assumptions and scope

All coefficients \(b,c,p,q,\kappa\) are fixed and strictly positive as \(\varepsilon\downarrow0\); detuning \(\delta\) is fixed and may be positive, negative or zero. The baseline matrix is a two-species antagonistic feedback with reciprocal entries of opposite sign. The sinusoidal susceptibility matrix preserves this antagonistic sign structure. Self-regulation scales as \(\kappa\varepsilon\), the natural near-marginal regime where weak forcing can compete with damping. For sufficiently small \(\varepsilon\), both instantaneous reciprocal interaction entries retain their signs. Floquet stability means exponential decay or growth of the *linearized perturbations* over repeated seasons. No stationary positive population equilibrium, nonlinear extension or stochastic abundance model is assumed or established here.

## Proof

**1. Strict stability of all frozen environments.** At any phase \(u=\cos(\omega_\varepsilon t)\in[-1,1]\),
\[
A_\varepsilon(u)=\begin{pmatrix}-\kappa\varepsilon&b+\varepsilon p u\\-c-\varepsilon q u&-\kappa\varepsilon\end{pmatrix}.
\]
If \(0<\varepsilon<\min\{b/p,c/q\}\), both the upper-right and the negative lower-left entries are positive in magnitude. The frozen eigenvalues therefore are
\[
-\kappa\varepsilon\pm i\sqrt{(b+\varepsilon p u)(c+\varepsilon q u)},
\]
and both have strictly negative real part. In particular this also proves stability of the averaged matrix, since its spectrum is \(-\kappa\varepsilon\pm i\Omega\).

**2. Reduce to an unforced rotation and a single mismatch invariant.** Make the constant positive diagonal similarity \(x=Sz\), with \(S=\operatorname{diag}(\sqrt b,\sqrt c)\). Set
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
K=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\alpha=\frac{pc+bq}{2\Omega}.
\]
Direct matrix multiplication gives
\[
S^{-1}BS=\Omega J,\qquad S^{-1}HS=\alpha J+DK,
\]
so the transformed system is
\[
\dot z=-\kappa\varepsilon z+
\left[\Omega J+\varepsilon\cos(\omega_\varepsilon t)(\alpha J+DK)\right]z.
\]
Here \(J^2=-I\), \(K^2=I\), and \(JK+KJ=0\). The original commutator has the exact form
\[
[B,H]=(pc-bq)\begin{pmatrix}1&0\\0&-1\end{pmatrix};
\]
therefore it vanishes precisely when \(D=0\), i.e. when the two reciprocal environmental-response ratios agree.

**3. Rotating-frame, uniformly bounded one-period expansion.** Write \(R(t)=\exp[(\omega_\varepsilon t/2)J]\) and substitute \(z(t)=e^{-\kappa\varepsilon t}R(t)y(t)\). The factor \(R\) is bounded, invertible, and obeys \(R(T_\varepsilon)=-I\) since \(\omega_\varepsilon T_\varepsilon=2\pi\). A direct differentiation gives
\[
\dot y=\varepsilon Q_\varepsilon(t)y,\qquad
Q_\varepsilon(t)=-\frac\delta2 J+
\cos(\omega_\varepsilon t)
R(t)^{-1}(\alpha J+DK)R(t).
\]
Conjugation leaves \(J\) fixed and rotates \(K\) at angular frequency \(\omega_\varepsilon\); consequently its resonant cosine component has mean \(K/2\). More explicitly,
\[
\frac{1}{T_\varepsilon}\int_0^{T_\varepsilon}Q_\varepsilon(t)\,dt
=C:=\frac12(DK-\delta J).
\]
The matrix \(Q_\varepsilon\) and period \(T_\varepsilon\) stay uniformly bounded as \(\varepsilon\downarrow0\). The Peano–Baker expansion, with its uniformly bounded double-integral remainder, yields for the fundamental matrix of the \(y\)-system
\[
Y_\varepsilon(T_\varepsilon)=I+\varepsilon T_\varepsilon C+O(\varepsilon^2)
\]
in matrix norm. The original monodromy is similar to \(-e^{-\kappa\varepsilon T_\varepsilon}Y_\varepsilon(T_\varepsilon)\).

**4. Limiting Floquet exponent and both strict directions.** Since \(J^2=-I\), \(K^2=I\) and \(JK=-KJ\),
\[
C^2=\frac{D^2-\delta^2}{4}I.
\]
Thus the maximum real part among eigenvalues of \(C\) is \(\frac12\sqrt{\max\{D^2-\delta^2,0\}}\). The eigenvalues of \(\bigl(Y_\varepsilon(T_\varepsilon)-I\bigr)/(\varepsilon T_\varepsilon)\) converge as a multiset to those of \(C\), even when the limiting matrix is defective. Taking logarithms of the modulus of the monodromy eigenvalues gives
\[
\lim_{\varepsilon\downarrow0}\frac{\Lambda_\varepsilon}{\varepsilon}
=-\kappa+\frac12\sqrt{\max\{D^2-\delta^2,0\}}.
\]
The strict-sign assertions follow from positivity or negativity of this limit, respectively. No higher-order sign is inferred on the boundary \(\delta^2+4\kappa^2=D^2\).

**5. Exact commuting exception.** If \(D=0\), the entire time-varying matrix equals \(-\kappa\varepsilon I+[\Omega+\varepsilon\alpha\cos(\omega t)]J\) after similarity. These matrices commute for every pair of times. Over one period the cosine integrates to zero, so the undamped monodromy is \(\exp(\Omega JT)\), with spectral radius one; the damped Floquet exponent is exactly \(-\kappa\varepsilon\) for arbitrary positive frequency and amplitude. Conversely \([B,H]\ne0\) if \(D\ne0\), and choosing sufficiently weak \(\kappa\) and sufficiently small \(|\delta|\) makes the instability inequality feasible.

**6. Concrete nonresonant comparison.** The numerical values given above yield \(\Omega=1\) and \(D=3/4\). With \(\delta=0\), the averaged matrix \(C=(3/8)K\) has distinct real eigenvalues, and standard eigenvalue perturbation upgrades the limiting relation to \(\Lambda_\varepsilon=\varepsilon/8+O(\varepsilon^2)\). Now fix \(\omega=4\) with all other coefficients unchanged. Remove scalar damping and denote the determinant-one monodromy by \(N_\varepsilon\). At \(\varepsilon=0\), its period is \(\pi/2\), and \(N_0=\exp[(\pi/2)J]=J\) has trace zero. By continuous dependence of solutions, \(|\operatorname{tr}N_\varepsilon|<2\) for all sufficiently small \(\varepsilon\). Since its determinant is one (Liouville's formula), its two eigenvalues form a conjugate pair of modulus one. Reinstating scalar damping gives \(\Lambda_\varepsilon=-\varepsilon/4\) *exactly* in this small-amplitude range.

## Verification

Run \(\texttt{python checker.py}\) with NumPy, SciPy and SymPy installed. The standalone checker verifies the normalized commutator and discriminants symbolically, integrates the fundamental matrix over one period at several small amplitudes, compares the detuned Floquet exponent against the limiting formula and checks the exact damping identity both in the commuting and nonresonant examples. Its finite computations corroborate the algebra; they do not certify the limit, the universal parameter quantifiers or the proof, which follow from the matrix identities and uniform Peano–Baker bound above.

## Relationship to prior work

Nag Chowdhury (arXiv:2608.14081v1, first public 2026-08-14) introduced the broader periodically driven ecological community-matrix model and proved that completely shared environmental responses have no effect on the growth exponent. The paper develops adiabatic and high-frequency regimes for large ecological networks, but does not give the two-species near-resonant first-order instability tongue in terms of reciprocal interaction-response mismatch. Its commuting limit is acknowledged as known and used as a consistency check here, not claimed as new.

Swailem and Rucklidge (arXiv:2511.03521) investigated parametric resonance in a nonlinear predator–prey model with seasonally varying carrying capacity and a different linearized coefficient structure, including periodically varying diagonal terms. This establishes that seasonal predator–prey resonance itself is prior art. Classical Mathieu/Hill instability tongues and their perturbative derivation are also prior art. The claim here is narrower: an explicit, uniform weak-amplitude Floquet criterion for the specified antagonistic *community interaction matrix*, with a commutator-controlled response mismatch, negative frozen-time eigenvalues and an exact fixed-frequency stability reversal. A published alternating-season ecological feedback theorem also exhibits frozen-stable Floquet instability; its time dependence is piecewise constant, and the available abstract does not determine the continuous sinusoidal coefficient criterion above.

## Limitations

The result concerns infinitesimal perturbations and a near-marginal scaling where damping is proportional to forcing amplitude; for any fixed nonzero damping it does not assert instability under arbitrarily weak forcing. The sign test applies to fixed detuning in an \(O(\varepsilon)\) window around twice the unforced oscillation frequency, and to sufficiently small positive forcing only. It does not classify all finite-amplitude resonance tongues or the nonlinear fate of species near a seasonal instability. Strict stability on the equality boundary is unresolved at first order. General parametric resonance, Mathieu averaging and the perfectly commuting exception are established background; this calculation is an ecological sign-constrained specialization. Historical-priority risk remains for more general Hill-equation formulas and a related published alternating-season result whose full proof was not accessible.

## References

1. S. Nag Chowdhury, *Periodic Environmental Forcing Shapes the Stability of Complex Ecological Networks*, arXiv:2608.14081v1 (2026). https://arxiv.org/abs/2608.14081
2. M. Swailem and A. M. Rucklidge, *Parametric resonance, chaos and spatial structure in the Lotka–Volterra model*, arXiv:2511.03521v1 (2025). https://arxiv.org/abs/2511.03521
3. I. Kovačić, R. H. Rand and S. M. Sah, *Mathieu's Equation and Its Generalizations: Overview of Stability Charts and Their Features*, Applied Mechanics Reviews **70**, 020802 (2018). https://doi.org/10.1115/1.4039144
4. C. A. Klausmeier, *Floquet theory: a useful tool for understanding nonequilibrium dynamics*, Theoretical Ecology **1**, 153–161 (2008). https://doi.org/10.1007/s12080-008-0016-2
