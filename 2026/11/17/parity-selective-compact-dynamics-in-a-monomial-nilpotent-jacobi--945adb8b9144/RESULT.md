# Parity-selective compact dynamics in a monomial nilpotent-Jacobian flow

## Finding

For **each integer** \(m\ge 2\), consider the real polynomial vector field on \(\mathbb R^3\)
\[
\dot x=(y+x^2)^m,\qquad
\dot y=z-2x(y+x^2)^m,\qquad
\dot z=(y+x^2)^{2m}-1. \tag{1}
\]
Its Jacobian is nilpotent at every point. The bounded forward dynamics undergo an **exact parity dichotomy**:

* For every **even** \(m\ge2\), there is no bounded forward trajectory, no nonempty compact forward-invariant set, and no compactly supported invariant probability measure.
* For every **odd** \(m\ge3\), a finite nonzero number of mutually disjoint energy cylinders are each completely foliated by periodic trajectories of identical physical-time period. Every bounded forward trajectory is one of those periodic trajectories; no others exist.

These assertions reduce to a scalar analytic displacement function. Set
\[
V_m(v)=v-\frac{v^{2m+1}}{2m+1},\quad
E_-=-\frac{2m}{2m+1},\quad E_+=\frac{2m}{2m+1}.
\]
For each \(E\in(E_-,E_+)\), let \(a_m(E)<-1<b_m(E)<1\) be the two turning points satisfying \(V_m(a_m(E))=V_m(b_m(E))=E\). Define the exact original-time period and axial displacement
\[
T_m(E)=\sqrt2\int_{a_m(E)}^{b_m(E)}\frac{dv}{\sqrt{E-V_m(v)}},\qquad
D_m(E)=\sqrt2\int_{a_m(E)}^{b_m(E)}\frac{v^m\,dv}{\sqrt{E-V_m(v)}}. \tag{2}
\]
Precisely the zeros of \(D_m\) are the energies of the periodic cylinders. If \(m\) is odd, each such zero lies in the strict interval \((0,E_+)\); the set of zeros is finite and nonempty. If \(m\) is even, \(D_m(E)>0\) throughout the annulus.

There are also sharp separatrix timing and axial-drift laws, for every integer \(m\ge2\):
\[
T_m(E)=\frac{1}{\sqrt{2m}}\log\!\frac1{E_+-E}+O(1),
\qquad \lim_{E\uparrow E_+}\frac{D_m(E)}{T_m(E)}=1. \tag{3}
\]
In fact,
\[
\lim_{E\uparrow E_+}\big(D_m(E)-T_m(E)\big)
=J_m:=\sqrt2\int_{a_m(E_+)}^1\frac{v^m-1}{\sqrt{E_+-V_m(v)}}\,dv, \tag{4}
\]
where \(a_m(E_+)\) denotes the unique root of \(V_m(v)=E_+\) strictly less than \(-1\); the improper integral is finite. For odd \(m\), \(J_m<0\). Formula (4) is not used to assert uniqueness of an odd-degree zero.

## Assumptions and scope

The system is the continuous-time flow of the **real** polynomial field (1), not iteration of that polynomial as a discrete map. All statements are quantified over every integer \(m\ge2\) and all real initial states for which a forward solution exists. A bounded forward trajectory means a solution defined for all \(t\ge0\) whose spatial image has bounded closure. A periodic cylinder means the full inverse image, under \((x,y,z)\mapsto(v,w)=(y+x^2,z)\), of a regular closed planar energy oval. It is a noncompact surface topologically \(\mathbb R\times S^1\), foliated by compact periodic orbits. No claim of an isolated limit cycle or attraction is made.

The primary literature first released on 2022-09-15 treats this nilpotent polynomial class and the linear defining-polynomial case \(m=1\); the present statement deliberately concerns the unclassified higher-degree monomials \(m\ge2\).

## Proof

**1. Nilpotence and exact coordinates.** Put \(v=y+x^2\), \(u=x\), \(w=z\). This polynomial automorphism has polynomial inverse \((x,y,z)=(u,v-u^2,w)\) and changes (1), without changing time, into
\[
\dot u=v^m,\qquad \dot v=w,\qquad \dot w=v^{2m}-1. \tag{5}
\]
For completeness, write \(f=v^m\), \(a=m v^{m-1}\). Direct differentiation of (1) yields
\[
J=\begin{pmatrix}2xa&a&0\\-2f-4x^2a&-2xa&1\\4xfa&2fa&0\end{pmatrix},
\qquad
J^2=\begin{pmatrix}-2af&0&a\\4afx&0&-2ax\\-4af^2&0&2af\end{pmatrix}.
\]
Multiplication gives \(J^3=0\) identically for all real states and every permitted degree; this is an exact polynomial identity, not a finite sample.

**2. Hamiltonian phase portrait.** The planar subsystem \((v,w)\) has conserved energy
\[
H(v,w)=\frac{w^2}{2}+V_m(v),\quad V'_m(v)=1-v^{2m}.
\]
The potential decreases on \(( -\infty,-1)\), increases on \((-1,1)\), and decreases on \((1,\infty)\). Its nondegenerate minimum at \(-1\) is \(E_-\); its nondegenerate maximum at \(+1\) is \(E_+\). Thus each \(E\in(E_-,E_+)\) has exactly one bounded oval component, with turning points stated above. The other energy components are unbounded; at the critical energies there are planar equilibria and a saddle separatrix. The planar ovals are regular and have exact time period \(T_m(E)\) in (2). Integrating the first equation of (5) for one complete planar circuit gives the *same* axial increment \(D_m(E)\) for every initial axial coordinate and every phase. Therefore a lift closes after one planar circuit precisely if \(D_m(E)=0\), and if it closes, its minimal period is \(T_m(E)\). Nonzero drift gives \(u(t+nT_m)=u(t)+nD_m\), hence unbounded forward motion.

**3. Parity and existence.** If \(m\) is even, \(v^m\ge0\) and it is positive on a set of positive time-measure on every regular oval, so \(D_m(E)>0\). If \(m\) is odd and \(E\le0\) lies in the oval interval, its right turning point is nonpositive (because \(V_m(0)=0\) and \(V_m\) increases on \((-1,1)\)), so \(D_m(E)<0\). Near the central oval, continuity also gives
\[
\lim_{E\downarrow E_-}T_m(E)=\frac{2\pi}{\sqrt{2m}},\qquad
\lim_{E\downarrow E_-}D_m(E)=\frac{(-1)^m2\pi}{\sqrt{2m}}. \tag{6}
\]

As \(E\uparrow E_+\), the right turning point tends to the saddle \(v=1\). Taylor expansion gives \(E_+-V_m(v)=m(v-1)^2+O((v-1)^3)\). Splitting the quadrature at a fixed point slightly left of the saddle and using the inner turning-point distance \(1-b_m(E)\sim\sqrt{(E_+-E)/m}\) gives the logarithmic coefficient in (3). On this long saddle passage, \(v^m\to1\). More precisely the integral for \(D_m-T_m\) has the finite limit (4): near \(v=1\), its numerator cancels one order of the double zero of \(E_+-V_m\), and near the left turning point the remaining square-root singularity is integrable. Consequently \(D_m(E)=T_m(E)+O(1)\to+\infty\). For odd \(m\), the negative drift near \(E_-\) and positive drift near \(E_+\) force an interior zero by continuity, and the previous sign argument places every zero in \((0,E_+)\). For odd \(m\), the integrand defining \(J_m\) is negative on \((a_m(E_+),1)\), yielding \(J_m<0\).

**4. Finiteness.** On regular analytic Hamiltonian ovals, both integrals in (2) vary real-analytically with \(E\). This also follows directly by factoring the simple turning-point zeros and substituting \(v=a_m(E)+(b_m(E)-a_m(E))\sin^2\theta\). The nonzero endpoint signs exclude zeros in neighborhoods of both endpoints, and an analytic function not identically zero has only finitely many zeros on the remaining compact energy interval. Thus the number of periodic cylinders is finite for each odd \(m\).

**5. Exhaustion of bounded forward dynamics.** A bounded forward solution of (5) has a bounded forward planar projection. By the elementary one-degree-of-freedom Hamiltonian phase portrait, its projection must be an oval, a planar equilibrium, or a branch approaching the saddle along the separatrix. On either planar equilibrium the axial velocity is \(v^m=\pm1\), hence \(u\) grows linearly. On any saddle-approaching branch \(v(t)\to1\), so \(\dot u(t)\to1\), again giving unbounded forward motion. On any oval with nonzero displacement \(D_m\), the axial motion is unbounded by step 2. Only zero-drift ovals remain, and every lifted orbit on them is periodic. This proves the complete bounded-forward classification. The compact-invariant and compact-invariant-probability consequences follow immediately: any compact forward-invariant set supplies a bounded forward trajectory, and a compactly supported invariant probability has compact forward-invariant support.

## Verification

The standalone \(\texttt{check.py}\) script uses only the Python standard library. It exactly evaluates \(J^3\) on rational test points for several degrees, verifies signs of (2) on sampled energies, and performs endpoint-regularized Simpson quadrature followed by bisection for the first three odd degrees. It prints approximate zero energies \(0.66314059645\) (\(m=1\), previously studied), \(0.85388528600\) (\(m=3\)), and \(0.90641236344\) (\(m=5\)). Its checks are supplementary: all-degree nilpotence, exact parity, the existence and finiteness of zeros, and the logarithmic law are proved above without extrapolating finite experiments. Run with \(\texttt{python3 check.py}\); it requires no external data files.

## Relationship to prior work

Castañeda and Rebollo-Perdomo introduced the full nilpotent-Jacobian class in their 2022 public preprint and prove a complete periodic-surface result when both defining polynomials are linear (their Proposition 1.3). Their concluding section explicitly asks how many periodic surfaces are possible when the first defining polynomial has higher degree. The conjugation to a one-degree-of-freedom Hamiltonian skew flow is also in their work. Neither that general conjugation nor the linear-degree periodic-surface theorem itself implies the higher-degree parity dichotomy, finite nonzero odd-degree census, all bounded-forward classification, or equations (3)–(4). The present result concerns the special but natural monomial subfamily and does **not** claim to settle the count for every polynomial or for each odd monomial exactly.

A separate known result for an even-power kinetic skew system has periodic cylinders and a different degenerate-period law. Its vector field has a different planar restoring term and axial drift; its period asymptotics do not cover the monomial nilpotent-Jacobian flow here. A 2026 Hurwitz-vector-field construction studies isolated hyperbolic cycles in a different parameter family, whereas (1) has pointwise nilpotent Jacobian and nonisolated periodic cylinders.

## Limitations

The exact *number* of zero-drift cylinders for a given odd \(m\ge3\) is not determined; the proof establishes that this number is a positive finite integer, not that it is one. The paper does not classify finite-time escape for unbounded trajectories or perturbative persistence of the nonisolated cycles. The late-2024 journal version of the motivating 2022 preprint was accessible as a publisher abstract/preview rather than as a separate full-text manuscript; the fully inspected 2022 preprint is the principal textual basis for the comparison, and any later unindexed additions remain a publication-priority risk.

## References

1. Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1 (first posted 2022-09-15), https://arxiv.org/abs/2209.06986 ; journal version, *Archiv der Mathematik* 124 (2025), 415–434, https://doi.org/10.1007/s00013-024-02085-8.
2. Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in R3 having non-constant periodic orbits*, arXiv:2610.09176 (2026-10-06), https://arxiv.org/abs/2610.09176 (a distinct Hurwitz construction).
