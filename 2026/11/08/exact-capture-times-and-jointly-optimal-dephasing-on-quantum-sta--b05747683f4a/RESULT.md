# Exact capture times and jointly optimal dephasing on quantum stars

## Finding

For every integer \(m\ge2\), consider a single tight-binding excitation on the star \(K_{1,m}\), initially localized at one leaf, with uniform coherent edge hopping \(J\ne0\), uniform site-basis pure dephasing rate \(\gamma>0\), and one irreversible trap of population-loss rate \(\kappa>0\) at the central vertex. Write \(T_{m}^{\mathrm{leaf}}\) for the **unconditional expected time to absorption**, namely the integral over all time of the surviving excitation probability. Absorption occurs with probability one and

\[
T_m^{\mathrm{leaf}}(\gamma,\kappa)=\frac{m+1}{\kappa}+\frac{m-1}{\gamma}+\frac{\gamma+\kappa/2}{2J^2}.
\]

The positive rates have the **unique joint minimizer**

\[
\gamma_*=|J|\sqrt{2(m-1)},\qquad \kappa_*=2|J|\sqrt{m+1},
\quad \min_{\gamma,\kappa>0}T_m^{\mathrm{leaf}}=
\frac{\sqrt{m+1}+\sqrt{2(m-1)}}{|J|}.
\]

Thus the optimal mean grows as \((1+\sqrt2)\sqrt m/|J|\). For the same dynamics initially at the central vertex instead, the exact mean is \(T_m^{\mathrm{hub}}=(m+1)/\kappa\), independently of the positive dephasing strength and the hopping strength. At **zero** dephasing, the hub-initial capture mean becomes \(2/\kappa\), while a localized leaf has an uncaptured dark-state fraction \((m-1)/m\); hence the leaf-initial unconditional mean is infinite at \(\gamma=0\). All statements are for finite \(m\) and do not require an asymptotic limit.

## Assumptions and scope

The single-excitation Hilbert space has orthonormal basis \(|0\rangle,|1\rangle,\ldots,|m\rangle\), where \(0\) is the trapped hub. Units have \(\hbar=1\). Let

\[
H=J\sum_{j=1}^{m}\bigl(|0\rangle\langle j|+|j\rangle\langle0|\bigr),\qquad P_0=|0\rangle\langle0|,\qquad P_j=|j\rangle\langle j|.
\]

For \(J\in\mathbb R\setminus\{0\}\), \(\gamma>0\) and \(\kappa>0\), the unnormalized, trace-decreasing density matrix satisfies

\[
\dot\rho=-i[H,\rho]-\frac\kappa2\{P_0,\rho\}
+\gamma\sum_{v=0}^{m}\left(P_v\rho P_v-\frac12\{P_v,\rho\}\right).
\]

This normalization gives \(\dot\rho_{uv}\supset-\gamma\rho_{uv}\) for distinct sites \(u\ne v\), and \(\frac{d}{dt}\operatorname{tr}\rho=-\kappa\rho_{00}\). The initial conditions are \(\rho(0)=|1\rangle\langle1|\) for the leaf finding and \(\rho(0)=|0\rangle\langle0|\) for the companion hub formula. The survival function is \(S(t)=\operatorname{tr}\rho(t)\), and the unconditioned first-capture mean is \(T=\int_0^\infty S(t)\,dt\). There is no nontrapping recombination, site disorder, direct leaf-leaf coupling, or coherent preparation over leaves. The result does not concern the median absorption time or conditional capture time at zero dephasing.

## Proof

**1. Complete capture for positive dephasing.** Embed the trace-decreasing dynamics in the one-excitation space, and use the Hilbert–Schmidt norm. For a Hermitian solution,

\[
\frac d{dt}\operatorname{tr}(\rho^2)
=-2\kappa\sum_{v=0}^m|\rho_{0v}|^2
-2\gamma\sum_{u\ne v}|\rho_{uv}|^2\le0.
\]

The only invariant state inside the set where this derivative vanishes has all hub entries and all off-diagonal entries zero. For such a diagonal leaf state, the coherent commutator yields \(\dot\rho_{0j}=-iJ(\rho_{jj}-\rho_{00})=-iJ\rho_{jj}\), which can remain zero for all \(j\) only when the entire state is zero. Finite-dimensional invariance therefore forces every initial positive state to converge to zero (or equivalently, all eigenmodes of this dissipative generator decay). In particular \(S(t)\to0\), and the integrated resolvent exists; there is unit eventual capture probability.

**2. Symmetric reduction without changing the observable.** The mean \(T\) is a linear functional of the initial density matrix, and the dynamics and trap are invariant under every permutation of the leaves. Consequently, the mean for \(|1\rangle\langle1|\) equals that for the uniform *incoherent* mixture \(m^{-1}\sum_{j=1}^m|j\rangle\langle j|\). The hub-initial density matrix is already symmetric. For either symmetric initial condition write \(p=\rho_{00}\), \(a=\rho_{jj}\), \(b=\rho_{ij}\) for distinct leaves \(i\ne j\), and \(\rho_{0j}=iy\). The off-diagonal leaf variable \(b\) is real, and \(y\) is real because these properties hold initially and are invariant. Directly taking matrix elements gives

\[
\begin{aligned}
\dot p&=-\kappa p-2mJy,&\dot a&=2Jy,\\
\dot b&=2Jy-\gamma b,&\dot y&=J[p-a-(m-1)b]-(\gamma+\kappa/2)y.
\end{aligned}
\]

**3. Exact time integrals.** Denote the time integrals by capital letters \(P,A,B,Y\). For the uniform leaf mixture the starting values are \((p,a,b,y)=(0,1/m,0,0)\). Integrating all four differential equations over \([0,\infty)\) and using their zero terminal values gives

\[
P=\frac1\kappa,\quad Y=-\frac1{2mJ},\quad B=-\frac1{m\gamma},\quad
A=\frac1\kappa+\frac{m-1}{m\gamma}
+\frac{\gamma+\kappa/2}{2mJ^2}.
\]

The survival integral \(P+mA\) is exactly the asserted expression. For the hub initial data \((1,0,0,0)\), integration instead yields \(Y=B=0\), \(P=A=1/\kappa\), and thus \(T_m^{\mathrm{hub}}=(m+1)/\kappa\).

**4. Unique optimum and boundaries.** Rewrite the leaf expression as

\[
T_m^{\mathrm{leaf}}=
\left(\frac{m-1}{\gamma}+\frac\gamma{2J^2}\right)
+\left(\frac{m+1}{\kappa}+\frac\kappa{4J^2}\right).
\]

Both brackets have strictly positive second derivative on their positive domains for \(m\ge2\), and diverge at both endpoints. Differentiation gives the unique \(\gamma_*\), \(\kappa_*\), and stated minimum. The small-dephasing divergence is \((m-1)/\gamma\); the large-dephasing divergence is \(\gamma/(2J^2)\). For \(\gamma=0\), the normalized symmetric leaf vector \(m^{-1/2}\sum_j|j\rangle\) is the only leaf combination coupled to the hub. A localized leaf has bright weight \(1/m\) and permanent dark weight \((m-1)/m\); the unconditional mean is therefore infinite. For hub initial data, the dynamics reduces to the bright two-state subspace, whose integrated trapping mean is \(2/\kappa\) (integrating the two-level population and coherence equations). This proves the noncommuting zero-dephasing limit.

## Verification

Two independent computational implementations accompany this result. `verify_reduced_exact.py` uses fractions and exact Gaussian elimination on the four-dimensional integrated equation, checking 108 parameter and initial-state cases. `verify_full_lindblad.py` independently builds the unrestricted complex Lindblad matrix on all \((m+1)^2\) density-matrix coordinates and solves its resolvent at 30 additional cases. Every tested case agrees with the displayed exact formula, including negative real hopping and both initial positions. These finite checks are corroborations; the all-size proof is the invariant-system reduction and exact integration above. Execute with `python verify_reduced_exact.py` and `python verify_full_lindblad.py` (the latter requires NumPy and SciPy).

## Relationship to prior work

Rebentrost et al. (arXiv:0807.0929, 2008) and Kassal–Aspuru-Guzik (arXiv:1201.5202, 2012) establish fundamental environment-assisted transport mechanisms, including dephasing and absorbing traps, but analyze different networks and efficiency observables. Pepe–Pouthier–Yalouz (arXiv:2308.15857, 2023) study star networks under the same off-diagonal decay convention and use symmetry reductions, yet their initial state is a **coherent uniform peripheral superposition**, their reported absorption time is a **50-percent capture quantile**, and their principal optimization concerns **energy defects**, not the unconditional quantum mean for a single localized leaf optimized jointly over trap and dephasing rates. Its Appendix C does derive a mean first-passage estimate for an effective **classical directed chain** at intermediate/strong dephasing; this neither gives the exact all-rate quantum star formula nor the two-rate optimum. Alterman–Berman–Strauch (arXiv:2309.00164, 2023) treat complete graph hopping, not hub-only star coupling. Classical site-dephasing and trap models are established prior tools; the asserted contribution is the star-localized initial-state lifetime identity and its sharp joint optimizer and singular boundary comparison, not a new master equation or generic noise-assisted transport principle.

## Limitations

The theorem uses exactly symmetric hopping, independent *uniform* pure dephasing of all sites, one hub trap and one excitation. Neither the formula nor its optimizer is claimed for site disorder, correlated baths, extra losses, thermal relaxation, or interacting excitations. The zero-dephasing leaf survival is nonzero and must not be mistaken for eventual full capture. Earlier Gaab–Bardeen (2004), DOI 10.1063/1.1786922, concerns closely related Haken–Strobl connectivity/trapping optimization, but only abstract-level material was accessible for the present comparison; an unrecognized same-family analytical specialization remains a historical-priority risk. The result has not received independent scientific review.

## References

1. P. Rebentrost, M. Mohseni, I. Kassal, S. Lloyd and A. Aspuru-Guzik, *Environment-Assisted Quantum Transport*, arXiv:0807.0929 (first posted July 7, 2008). https://arxiv.org/abs/0807.0929
2. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (first posted January 25, 2012). https://arxiv.org/abs/1201.5202
3. L. Pepe, V. Pouthier and S. Yalouz, *Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing*, arXiv:2308.15857 (first posted August 30, 2023). https://arxiv.org/html/2308.15857v2
4. R. Alterman, G. P. Berman and F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on Fully Connected Networks*, arXiv:2309.00164 (2023). https://arxiv.org/abs/2309.00164
5. K. M. Gaab and C. J. Bardeen, *The effects of connectivity, coherence, and trapping on energy transfer in simple light-harvesting systems studied using the Haken–Strobl model with diagonal disorder*, J. Chem. Phys. 121 (2004), 7813–7820. https://doi.org/10.1063/1.1786922
