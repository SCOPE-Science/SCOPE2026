# A sharp fear-controlled trichotomy at a doubly neutral discrete predator–prey equilibrium

## Finding
Consider the Du–Han–Lei discrete predator–prey map, at simultaneous prey-flip and predator-invasion thresholds \(r=2\) and \(\alpha=d\):
\[
 u_{n+1}=u_n\exp\!\left[\frac{2(1-u_n/K)}{1+kv_n}-\frac{\beta v_n}{u_n+\gamma}\right],\qquad
 v_{n+1}=v_n\exp\!\left[-\frac{a v_n}{bu_n+c}\right].
\]
All seven coefficients \(K,k,\beta,\gamma,a,b,c\) are positive. Define
\[
 A=\frac{a}{bK+c},\quad B=\frac{\beta}{K+\gamma},\quad H=\frac K{K+\gamma},\quad
 L=2k+B(1+H),\quad p=\frac LA.
\]
Suppose \(0<p<1\), and choose any \(q\) with \(\max\{1/2,p\}<q<1\). There is a sufficiently small \(\delta>0\), depending only on these parameters and \(q\), such that every initial state satisfying
\[
0<v_0<\delta,\qquad v_0^q<s_0<\delta,\qquad s_0=\frac{u_0}{K}-1+\frac B2v_0
\]
has an orbit in the positive quadrant tending to \((K,0)\) and obeys \(\lim_{n\to\infty} n v_n=1/A\). Its sign-alternating prey coordinate satisfies exactly the following trichotomy:
\[
\begin{array}{ll}
0<p<1/2:&\displaystyle \lim_{n\to\infty}(-1)^n\sqrt n\,s_n=\frac{\sqrt{3(1-2p)}}2,\\[4pt]
p=1/2:&\displaystyle \lim_{n\to\infty}(-1)^n\sqrt{n\log n}\,s_n=\frac{\sqrt3}2,\\[4pt]
1/2<p<1:&\displaystyle \lim_{n\to\infty}(-1)^n n^p s_n=C(u_0,v_0)>0.
\end{array}
\]
Here \(s_n=u_n/K-1+Bv_n/2\). Consequently, varying the positive fear intensity \(k\) through \(k_*=A/4-B(1+H)/2\), when this lies in the permitted parameter interval, changes prey damping from a universal inverse-square-root amplitude to a logarithmically corrected amplitude and then to an initial-state-dependent inverse-power amplitude. The coefficient \(1/A\) of predator extinction is unchanged.

## Assumptions and scope
The theorem is **local and one-sided**: it concerns the explicit nonempty open wedge \(s_0>v_0^q\) with positive, small predator density. It does not assert a global basin theorem, nor the same asymptotics for the complementary thin sector. The restriction \(p<1\) is essential to this proof because it leaves a barrier exponent \(q<1\). The codimension-two boundary \(r=2,\alpha=d\) is not the interior flip bifurcation treated in the cited paper. There is no stochastic interpretation assumed here.

## Proof
Put \(x=u/K-1\), \(y=v\), \(J=bK/(bK+c)\), and \(s=x+By/2\). The exact map becomes
\[
 x'=(1+x)\exp\!\left[-\frac{2x}{1+ky}-\frac{By}{1+Hx}\right]-1,
 \qquad y'=y\exp\!\left[-\frac{Ay}{1+Jx}\right].
\]
It is analytic near \((0,0)\). Taylor expansion through cubic order gives \(s'=-s+(2/3)s^3+Lsy+O(s^4+s^2y+y^2)\) and \(y'=y-Ay^2+O(|s|y^2+y^3)\). Directly composing twice, using cancellation of the even pure fourth-order and quadratic-mixed terms at multiplier \(-1\), yields the **critical two-step normal form**
\[
 \boxed{s''=s-\frac43s^3-2Lsy+O(s^5+s^3y+sy^2+y^3),\quad
 y''=y-2Ay^2+O(|s|y^2+y^3).}\tag{1}
\]
Every error estimate in (1) is uniform on a sufficiently small neighborhood with \(y\ge0\). The cubic coefficient and \(sy\) coefficient can also be obtained by differentiating the exact two-fold map at the origin; `CHECK.py` reproduces their polynomial-jet identities.

Fix \(q\in(\max\{1/2,p\},1)\). In a sufficiently small rectangle \(0<y<\delta\), \(0<s<\delta\), the exact two-step map decreases \(y\) and decreases \(s\), preserving positivity. At the boundary \(s=y^q\), (1) gives
\[
 \frac{s''}{(y'')^q}=1+2(Aq-L)y-\frac43 y^{2q}+O(y^{\min\{2,\,3-q,\,q+1\}})=1+2A(q-p)y+o(y)>1.
\]
The boundary \(s=\delta\) points inward because of the strictly negative cubic drift. Thus \(y^q<s<\delta\) is forward invariant for the two-step map after choosing \(\delta\) sufficiently small. Both coordinates decrease to zero; the odd iterates stay near the origin and satisfy \(s_{2m+1}=-s_{2m}(1+o(1))\). All original prey and predator coordinates remain positive by smallness.

Since \(y_{n+1}=y_n\exp[-Ay_n/(1+Jx_n)]\) and \(x_n\to0\), the reciprocal differences obey \(1/y_{n+1}-1/y_n\to A\), so \(y_n\sim 1/(An)\). The cubic term in (1) gives \(s_{2m}=O(m^{-1/2})\); the odd iterates have the same absolute order. Hence summing the sharper reciprocal identity \(1/y_{n+1}-1/y_n=A+O(|x_n|+y_n)\) yields \(1/y_n=An+O(\sqrt n+\log n)\) and
\[
y_{2m}=\frac1{2Am}+O(m^{-3/2}).\tag{2}
\]

Write \(\sigma_m=s_{2m}\), \(\eta_m=y_{2m}\), \(R_m=\sigma_m^{-2}\). By (1) and the wedge lower bound \(\sigma_m>\eta_m^q\), the positive inverse square obeys
\[
 R_{m+1}=\left(1+\frac{2p}{m}+\epsilon_m\right)R_m+\frac83+o(1),\qquad
 \sum_m|\epsilon_m|<\infty.\tag{3}
\]
Indeed, the small relative errors are bounded by a constant times \(\sigma_m^4+\sigma_m^2\eta_m+\eta_m^2+\eta_m^3/\sigma_m\), whose sums converge by \(\sigma_m^2=O(m^{-1})\), \(\eta_m=O(m^{-1})\), and \(q<1\). Formula (2) makes the error in the leading coefficient \(2p/m\) summable. The residual contribution to the additive term is \(o(1)\): bounds \(\eta_m^2/\sigma_m^2\le\eta_m^{2-2q}\to0\) and \(\eta_m^3/\sigma_m^3\le\eta_m^{3-3q}\to0\) suffice.

A product variation-of-constants argument for (3) now gives three cases. If \(2p<1\), \(R_m\sim(8/3)m/(1-2p)\). If \(2p=1\), \(R_m\sim(8/3)m\log m\). If \(2p>1\), \(R_m/m^{2p}\to Q\in(0,\infty)\), because the homogeneous product is a positive multiple of \(m^{2p}\) and the inhomogeneous series \(\sum_m m^{-2p}\) converges. Translating \(n=2m\) gives the stated coefficients, with \(C=2^p/\sqrt Q\). Odd-step sign reversal completes the proof for all integers \(n\).

## Verification
Run `python CHECK.py` with Python 3 and SymPy installed. The checker constructs the exact normalized analytic map, calculates the two-step polynomial jet, verifies the coefficients \(-4/3\) and \(-2L\), checks cancellation of the degree-four pure-prey term, and runs numerical asymptotic diagnostics on three parameter choices straddling the threshold. These finite diagnostics do **not** establish the asymptotic theorem; (1)–(3) do. The exact proof covers arbitrary positive coefficients satisfying the stated inequalities and all initial data in the wedge.

## Relationship to prior work
Du, Han and Lei (2023) introduce exactly this discrete exponential fear model and record the eigenvalues \(1-r\) and \(e^{\alpha-d}\) at \((K,0)\) (their Proposition 3). Their subsequent bifurcation analysis treats positive equilibria. At the simultaneous boundary, the multipliers are \(-1\) and \(+1\), and neither the one-sided nonlinear convergence theorem nor the three fear-controlled amplitudes is supplied by that local eigenvalue classification. A published research record concerning the *same* map addresses the number of positive equilibria, not this double-neutral time-asymptotic problem; see the originality assessment in `AUDIT.json`. General flip and parabolic scaling theory supplies proof techniques but does not alone give the displayed parameter-dependent coefficient \(L\) or this model-specific invariant wedge.

## Limitations
The result applies to the stated local open wedge, not all positive populations or all initial phases. It does not classify exceptional trajectories lying outside the wedge, nor establish structural stability away from \(r=2,\alpha=d\). The published-source comparison is limited to accessible full text and indexed records; equivalence hidden in unindexed or inaccessible work cannot be excluded. Independent verification has not been performed.

## References
Du, X., Han, X., and Lei, C. (2023). “Dynamics of a nonlinear discrete predator-prey system with fear effect.” *AIMS Mathematics* 8(10), 23953–23973, https://doi.org/10.3934/math.20231221 (published 2023-08-07; especially equation (1.2), Proposition 3 and the bifurcation sections).
