# Logarithmic period walls and a critical crossover in an invariant-square quartic center

## Finding
For the quartic polynomial center
\[
\dot x=-(1-x^2)(1+px)y,\qquad \dot y=(1-y^2)(1+qy)x,
\]
with \(p,q\in[-1,1]\), every noncentral point in the open invariant square \((-1,1)^2\) has a periodic orbit. Its original-physical-time minimal period, indexed by the normalized first integral \(H=E\), has a **sharp boundary multiplicity law**. Define
\[
J(z)=\frac{\log2-\log(1+z)}{1-z}\quad(-1<z<1),\qquad J(1)=\frac12,
\]
and \(m=\mathbf1_{\{|p|=1\}}+\mathbf1_{\{|q|=1\}}\). With the sum taken over those coefficients \(h\in\{p,q\}\) satisfying \(|h|<1\), counting multiplicities, the fixed-parameter formula is
\[
\boxed{T_{p,q}(E)=4E+m\log E+2\left[\sum_{|h|<1}\bigl(J(h)+J(-h)\bigr)+m\left(\log2+\frac12\right)\right]+o(1).}
\]
Thus the logarithmic coefficient is exactly \(0,1,2\), according to the number of degenerate opposite-edge factors; it does not depend on the sign of either boundary coefficient.

The transition is resolved on the **critical scale** \(p_E=1-\kappa/E\), while \(q\in(-1,1)\) is fixed. For every fixed \(\kappa\ge0\),
\[
\boxed{T_{p_E,q}(E)=4E+\log E+1+2[J(q)+J(-q)]+\Psi(\kappa)+o(1),}
\]
where the continuous crossover function is
\[
\Psi(\kappa)=\log\!\left[\frac{2(1-e^{-2\kappa})}{\kappa}\right]\ (\kappa>0),\qquad \Psi(0)=\log4.
\]
The remainder in this critical-scale formula is uniform for \(\kappa\) in any fixed compact interval of \([0,\infty)\). By reflection, the same formula holds for \(p_E=-1+\kappa/E\).

## Assumptions and scope
The parameters \(p,q\) belong to \([-1,1]\); all trajectories and the periods are strictly **inside** the square. The first integral and its energy normalization are
\[
H(x,y)=F_p(x)+G_q(y),\quad F_p(x)=\int_0^x\frac{s\,ds}{(1-s^2)(1+ps)},\quad G_q(y)=\int_0^y\frac{s\,ds}{(1-s^2)(1+qs)},\quad H(0,0)=0.
\]
The two coordinate potentials grow to infinity at both edges even when one boundary factor is double. Here \(E>0\) denotes this exact energy; shifting or rescaling it would change the stated constants. Parameters \(p_E\) in the crossover assertion vary between **different ODEs** as \(E\) varies. No uniformity for unrestricted approaches to the parameter boundary is claimed.

## Proof
**1. Global center and exact quadrant clock.** Write \(A_p(x)=(1-x^2)(1+px)\), \(B_q(y)=(1-y^2)(1+qy)\). They are strictly positive inside the square for \(|p|,|q|\le1\), and
\[
\dot H=\frac{x}{A_p(x)}(-A_p(x)y)+\frac{y}{B_q(y)}(B_q(y)x)=0.
\]
Each coordinate potential is strictly monotone outward from zero, quadratic near zero, and diverges at either edge; therefore each positive energy level is a compact regular simple closed curve with four axis crossings, and its nonvanishing vector field produces a periodic orbit.

For signs \(\sigma,\tau\in\{-1,1\}\), set
\[
U_{\sigma,p}(r)=\int_0^r\frac{s\,ds}{(1-s^2)(1+\sigma p s)},\quad R_{\sigma,p}=U_{\sigma,p}^{-1},\quad f_{\sigma,p}(u)=\frac1{R_{\sigma,p}(u)}-1.
\]
Here \(0<r<1\), \(u>0\). Along the quadrant with coordinate signs \((\sigma,\tau)\), use \(u=F_p(x)\), so \(G_q(y)=E-u\) and **in original time** \(\dot u=-xy\). Its duration is exactly
\[
T_{\sigma\tau}(E)=\int_0^E [1+f_{\sigma,p}(u)][1+f_{\tau,q}(E-u)]\,du.
\]
The endpoint singularities are integrable, since \(R_{\sigma,p}(u)\sim\sqrt{2u}\) at zero. Expanding the product gives \(E+L_{\sigma,p}(E)+L_{\tau,q}(E)+C_{\sigma\tau}(E)\), with \(L_{\sigma,p}(E)=\int_0^Ef_{\sigma,p}(u)du\) and \(C_{\sigma\tau}(E)=\int_0^Ef_{\sigma,p}(u)f_{\tau,q}(E-u)du\).

**2. Exact finite defect and the critical edge.** Changing from \(u\) to \(r=R_{\sigma,p}(u)\) gives the *exact* truncated defect identity
\[
L_{\sigma,p}(E)=\int_0^{R_{\sigma,p}(E)}\frac{dr}{(1+r)(1+\sigma p r)}.
\]
For \(-1<\sigma p\le1\) the limit is \(J(\sigma p)\). At \(\sigma p=-1\), this integral is \(\operatorname{artanh} R_{\sigma,p}(E)\). The critical potential satisfies, with \(r=R_{\sigma,p}(E)\),
\[
E=\frac1{2(1-r)}-\frac12+\frac14\log\frac{1-r}{1+r}.
\]
Consequently \(1-r\sim(2E)^{-1}\) and
\[
L_{\sigma,p}(E)=\frac12\log E+\log2+o(1)\quad\text{if }\sigma p=-1.
\]
Its defect obeys \(f_{\sigma,p}(u)=O((1+u)^{-1})\) at infinity. For any strict branch \(\sigma p>-1\), it is integrable and decays exponentially at infinity. Across all \(|p|\le1\), reflection/comparison with the critical branch gives the uniform envelope \(0\le f_{\sigma,p}(u)\le f_{-1}(u)\), where \(f_{-1}(u)=O(1/u)\) for large \(u\) and \(O(u^{-1/2})\) at zero.

**3. Vanishing convolution and fixed-boundary formula.** Split the convolution at \(E/2\). On the first half, bound one factor by its nonincreasing value at \(E/2\), and similarly on the second half. In the worst case both defects are critical, the bound is \(O((\log E)/E)\), hence \(C_{\sigma\tau}(E)=o(1)\). Each noncritical coefficient contributes two finite quadrant defects \(J(h)+J(-h)\), each counted twice in the period sum. Each critical coefficient contributes twice \(\frac12\log E+\log2\) and twice the other-sign finite defect \(J(1)=1/2\). Summing four quadrants proves the first boxed expression, including the constants and all sign choices.

**4. The moving critical layer.** Put \(p=1-\varepsilon\), \(\varepsilon=\kappa/E\) and let \(\delta_E=1-R_{-,p}(E)\). The singular side's exact potential, expressed with \(w=1-r\), has derivative integrand
\[
\frac{1-w}{w(2-w)[\varepsilon+(1-\varepsilon)w]}.
\]
For \(\kappa\) in a fixed compact interval, comparison on the region \(w=O(E^{-1})\) to \([2w(w+\varepsilon)]^{-1}\), and an \(O(\log E)\) bound on the integrated difference, yield
\[
\varepsilon E=\frac12\log\!\left(1+\frac\varepsilon{\delta_E}\right)+o(1).
\]
Thus, uniformly for compact \(\kappa\)-ranges,
\[
E\delta_E\longrightarrow \frac\kappa{e^{2\kappa}-1},\qquad \left.\frac\kappa{e^{2\kappa}-1}\right|_{\kappa=0}:=\frac12.
\]
The exact elementary defect identity becomes
\[
L_{-,p}(E)=\frac1{2-\varepsilon}\log\!\frac{2-\delta_E}{\varepsilon+(1-\varepsilon)\delta_E},
\]
so
\[
2L_{-,p}(E)=\log E+\Psi(\kappa)+o(1).
\]
The regular side contributes \(L_{+,p}(E)=1/2+o(1)\), and the two \(q\)-sides contribute \(J(q)+J(-q)+o(1)\), uniformly as asserted. The convolution tends to zero uniformly by the critical envelope and the exponential tail of the fixed \(q\)-branches. Summing the four quadrant clocks gives the second boxed expression. Reflection \(x\mapsto-x\), \(t\mapsto-t\) handles the negative parameter wall.

## Verification
The standalone `verify_period_wall.py` checks the invariant-energy identity and critical potential antiderivative algebraically, checks elementary finite-defect integrals exactly, and probes the critical-scale endpoint equation using numerical quadrature. The numerical tests only check finite instances; the asymptotic and uniformity assertions follow from the estimates in the proof. The exact critical coefficient \(\log E\) is one per degenerate parameter, not per singular quadrant.

## Relationship to prior work
Grau and Szántó (2024, Theorem 2 and proof case (v)) introduce the invariant-square quartic family, identify its center locus and inverse integrating factor. They do not give this boundary period analysis. The previously published result *Universal two-term period growth in an invariant-square quartic center* gives \(T(E)=4E+2\sum J+o(1)\) **only when both coefficients are strictly between -1 and 1**; its proof provides the quadrant-clock representation, but its finite constants diverge as a coefficient approaches a critical edge. The new result determines actual dynamics at the excluded singular parameters and gives a uniform parameter–energy scaling window; neither is a corollary obtained by inserting a boundary value in that fixed-parameter result. General work of Villadelprat and Zhang on canonical separable Hamiltonian period functions does not automatically imply the original-time constants here, since the planar flow has a state-dependent conformal Hamiltonian factor.

## Limitations
Only the full-square center stratum and coefficients in the closed square \([-1,1]^2\) are treated. The law does not classify other center strata or exterior trajectories. The critical-layer uniformity holds for bounded nonnegative \(\kappa\), not all approaches to the boundary, and is proved for a single moving wall with the other coefficient fixed strictly interior. There is no claim of independent validation or of uniqueness in all literature. A potentially relevant separable-Hamiltonian period-function article was available as bibliographic abstract rather than inspected full text; its coverage is a residual priority risk.

## References
1. M. Grau and I. Szántó, “A Polynomial System of Degree Four with an Invariant Square Containing At Least Five Limit Cycles,” *Qualitative Theory of Dynamical Systems* 23 (2024), article 247. First publicly available July 26, 2024. https://doi.org/10.1007/s12346-024-01106-9.
2. “Universal two-term period growth in an invariant-square quartic center,” published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-two-term-period-growth-in-an-invariant-square-quartic--73607523fe89; inspected full `RESULT.md`.
3. J. Villadelprat and X. Zhang, “The Period Function of Hamiltonian Systems with Separable Variables,” *Journal of Dynamics and Differential Equations* 32 (2020), 741–767, https://doi.org/10.1007/s10884-019-09759-w.
