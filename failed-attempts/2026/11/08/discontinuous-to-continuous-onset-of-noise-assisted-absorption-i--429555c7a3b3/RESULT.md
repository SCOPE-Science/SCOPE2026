# Discontinuous-to-continuous onset of noise-assisted absorption in a selectively dephased quantum trimer

## Finding
For a lossy three-site quantum chain with dephasing restricted to its detuned middle site, the global optimum of mean absorption time switches from zero dephasing to a positive value along an exact phase boundary. The optimum jumps discontinuously for weak enough terminal loss, but emerges continuously above a sharp loss threshold. Let \(z=\Delta^2\), \(K_0=32^{1/4}\), and define
\[
Q_\kappa(\gamma)=\kappa\gamma^2+(\kappa^2+8)\gamma+4\kappa.
\]
For every \(\kappa>0\) and \(\gamma\ge0\), the mean absorption time is
\[
T(\gamma)=\frac3\kappa+\frac{3\gamma+2\kappa}{4}
+\frac{z\kappa(3\gamma+\kappa)}{Q_\kappa(\gamma)}.
\]
Write \(z_c(\kappa)\) for the sharp global threshold. It is
\[
z_c(\kappa)=
\begin{cases}
\dfrac{48-3\kappa^2+12\sqrt{12-2\kappa^2}}{\kappa^2}, &0<\kappa<K_0,\\
\dfrac{12}{\kappa^2-4}, &\kappa\ge K_0.
\end{cases}
\]
If \(z<z_c\), the unique global minimizer of \(T\) on \([0,\infty)\) is \(\gamma=0\). If \(z>z_c\), there is a unique strictly positive global minimizer. At \(z=z_c\), the unique optimum is zero when \(\kappa\ge K_0\), while for \(0<\kappa<K_0\) there are exactly two global minimizers:
\[
\gamma=0,\qquad \gamma=\gamma_c(\kappa)=\frac{4-\kappa^2+\sqrt{8(6-\kappa^2)}}{\kappa}>0.
\]
Thus the optimal rate jumps from zero to a finite positive value for \(\kappa<K_0\), but is continuous across the boundary for \(\kappa\ge K_0\). The term “transition” describes this optimizer bifurcation, not a thermodynamic singularity.

## Assumptions and scope
Take \(\hbar=1\), hopping amplitude exactly one as the time unit, and the one-excitation orthonormal basis \(\{|1\rangle,|2\rangle,|3\rangle\}\). Set
\[
H=\begin{pmatrix}0&1&0\\1&\Delta&1\\0&1&0\end{pmatrix},
\quad P_j=|j\rangle\langle j|,
\quad\rho(0)=P_1,
\quad\kappa>0,\ \Delta\in\mathbb R,\ \gamma\ge0.
\]
The unnormalized transient density matrix evolves by
\[
\dot\rho=-i[H,\rho]-\frac\kappa2\{P_3,\rho\}
+\gamma\big(P_2\rho P_2-\tfrac12\{P_2,\rho\}\big).
\]
The environment is Markovian, the sink is absorbing, no additional loss/reinjection is present, and there is no dephasing on sites 1 or 3. The absorption-time survival function is \(S(t)=\operatorname{Tr}\rho(t)\); \(T(\gamma)=\int_0^\infty S(t)\,dt\). This theorem concerns mean absorption time, not stationary current in a reservoir-driven chain or arbitrary spatial dephasing profiles.

## Proof
**Finite absorption.** The transient semigroup is completely positive and trace-nonincreasing, with \(\dot S=-\kappa\rho_{33}\le0\). A nonzero positive stationary survivor would have \(\rho_{33}=0\). Positivity forces all coherences involving site 3 to vanish. The stationarity equation for the \((2,3)\) entry then forces \(\rho_{22}=0\); positivity and the \((1,2)\) equation force \(\rho_{11}=0\), a contradiction. Compactness of trace-one positive states and the Cesàro-average argument exclude a nonzero surviving asymptotic mass. Finite dimensionality therefore gives exponential decay of the transient semigroup, and its integral exists.

**Exact resolvent.** Put \(F=\int_0^\infty\rho(t)\,dt\); then \(\mathcal LF=-P_1\). The three population balance equations yield \(F_{33}=1/\kappa\) and \(\operatorname{Im}F_{12}=\operatorname{Im}F_{23}=1/2\). Writing \(F_{12}=A+i/2\), \(F_{23}=B+i/2\), \(F_{13}=iE\), the remaining coherence equations reduce to
\[
E=-\frac\Delta2-\frac\gamma2A,\qquad
E+\frac\Delta2=\frac{\gamma+\kappa}{2}B,\qquad
E=\frac{2(A-B)}\kappa.
\]
Their unique solution is
\[
A=-\frac{\Delta\kappa(\gamma+\kappa)}{Q_\kappa(\gamma)},\quad
B=\frac{\Delta\kappa\gamma}{Q_\kappa(\gamma)},\quad
E=-\frac{2\Delta(2\gamma+\kappa)}{Q_\kappa(\gamma)}.
\]
The remaining real diagonal equations give \(F_{22}=1/\kappa+\Delta B+(\gamma+\kappa)/4\) and \(F_{11}=F_{22}-\Delta A+\gamma/4\). Summing the three diagonal entries proves the displayed formula for \(T=\operatorname{Tr}F\).

**Global threshold.** The exact improvement relative to a coherent chain is
\[
T(\gamma)-T(0)=\frac{\gamma}{4Q_\kappa(\gamma)}
\left[3\kappa\gamma^2+(3\kappa^2+24-z\kappa^2)\gamma
+\kappa\big(12+z(4-\kappa^2)\big)\right].
\]
Since \(Q_\kappa(\gamma)>0\), an improvement for positive \(\gamma\) is possible only where \(h_\kappa(\gamma)=\kappa^2\gamma+\kappa(\kappa^2-4)>0\), and exactly when
\[
z>R_\kappa(\gamma):=
\frac{3\kappa\gamma^2+(3\kappa^2+24)\gamma+12\kappa}{\kappa^2\gamma+\kappa(\kappa^2-4)}.
\]
The numerator is positive; \(R\) diverges at any positive left endpoint where \(h=0\), and diverges as \(\gamma\to\infty\). Differentiation gives
\[
R_\kappa'(\gamma)=
\frac{3\big(\kappa^2\gamma^2+2\kappa(\kappa^2-4)\gamma+\kappa^4-32\big)}{\kappa\big(\kappa\gamma+\kappa^2-4\big)^2}.
\]
For \(0<\kappa<K_0\), the derivative numerator has exactly one positive zero, equal to \(\gamma_c\) above, and the minimum of \(R\) is \(z_c=R(\gamma_c)\). For \(\kappa\ge K_0\), it is nonnegative on \([0,\infty)\), so the infimum is attained at the zero boundary and equals \(R(0)=12/(\kappa^2-4)\); there is no positive improvement at equality. These observations prove the threshold and all equality claims.

**Uniqueness and continuity.** Differentiating the exact mean twice yields
\[
T''(\gamma)=\frac{2z\kappa^2}{Q_\kappa(\gamma)^3}
\left[3\kappa\gamma^3+3\kappa^2\gamma^2
+3\kappa(\kappa^2-4)\gamma+\kappa^4-32\right].
\]
For \(\kappa\ge K_0\), this is positive for \(\gamma>0\) if \(z>0\), so \(T\) has at most one interior minimum; for \(z=0\), \(T\) increases linearly. For \(z>0\) and \(0<\kappa<K_0\), the cubic factor has exactly one positive root by its coefficient signs (one sign change in descending order), so \(T'\) first decreases then increases. There can consequently be at most one interior local minimum, and any strict improvement over \(T(0)\) must occur at that minimum. Coercivity \(T(\gamma)\to\infty\) as \(\gamma\to\infty\) proves existence. In the continuous regime \(\kappa\ge K_0\), strict convexity and continuity of \(T'\) force the unique positive optimum to tend to zero as \(z\downarrow z_c\). In the discontinuous regime, the two competing minima tie exactly at the positive rate \(\gamma_c\), so the positive minimizer tends to \(\gamma_c\) as \(z\downarrow z_c\).

## Verification
The accompanying standalone `verify.py` uses Python's exact rational `fractions.Fraction` arithmetic, builds the full nine-variable real Hermitian Lindblad generator independently of the derived resolvent, and solves its integrated linear equations by exact Gaussian elimination. Running `python verify.py` checks 294 combinations of loss, detuning, and dephasing, including signed detunings and the zero-noise boundary, and matches the exact mean and improvement formulas. It also verifies exact signs in multiple parameter regimes. Finite checks supplement, but do not replace, the global algebraic proof.

For an exact transition witness, \(\kappa=2\) gives \(z_c=15\) and \(\gamma_c=2\); at this parameter \(T(2)=T(0)\), while choosing \(\Delta=4\) yields \(T(2)-T(0)=-1/10\). For \(\kappa=3\), the boundary is \(z_c=12/5\) and the positive optimum emerges continuously.

## Relationship to prior work
Jacob et al. (arXiv:2407.21715, first version July 31, 2024) study dephasing-assisted steady-state current in a **boundary-driven chain with a linear potential and bulk dephasing**; their exact three-site specialization has a different potential profile, boundary drive, noise geometry and observable. Contreras-Pulido et al. (arXiv:1407.0924) solve current and fluctuations in a **linear triple quantum dot with equal dephasing on all dots**, and identify a current-enhancement threshold; even after the renewal relation between current and residence time is considered, their homogeneous noise generator does not reduce to the middle-only dephasing generator here. Coates et al. (arXiv:2106.12567) and Lawrence, Wang and Segal (arXiv:2604.23005) study broader noise-assisted transport and spatially nonuniform noise, but do not state this exact global zero-vs-positive mean-first-absorption optimum and its jump-to-continuous boundary in the present model. These differences are statements about inspected material, not a claim that no equivalent treatment could exist elsewhere.

## Limitations
The result is exact for a single excitation, a three-site open chain with unit equal hopping, a detuned middle site, site-2-only pure dephasing, and a single irreversible sink. It does not classify general chains, collective environments, non-Markovian noise, distinct hopping strengths or additional loss channels. At extremely large \(\gamma\), the idealized Markovian dephasing model can cease to be appropriate for a microscopic implementation. General resolvent methods in the literature could implicitly produce the pointwise formula; the stated global optimizer phase boundary requires the additional sign analysis. Independent external scientific validation has not been performed.

## References
1. S. L. Jacob et al., “Dephasing-assisted transport in a tight-binding chain with a linear potential,” arXiv:2407.21715v1 (2024-07-31), https://arxiv.org/abs/2407.21715.
2. L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga and M. B. Plenio, “Dephasing-assisted transport in linear triple quantum dots,” arXiv:1407.0924v1 (2014-07-03), https://arxiv.org/abs/1407.0924.
3. C. Coates, B. W. Lovett and E. M. Gauger, “Localisation determines the optimal noise rate for quantum transport,” arXiv:2106.12567v1 (2021-06-23), https://arxiv.org/abs/2106.12567.
4. J. Lawrence, Y. Wang and D. Segal, “Design Principles for Enhanced Quantum Transport with Site-Dependent Noise,” arXiv:2604.23005v1 (2026-04-24), https://arxiv.org/abs/2604.23005.
