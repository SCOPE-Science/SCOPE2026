# Cubic extinction, a sign-changing second term, and a logarithmic resonance in a harvested predator–prey map

## Finding
For the positive discrete predator–prey map
\[
\begin{aligned}
x_{n+1}&=x_n+\delta x_n(1-x_n-y_n),\\
y_{n+1}&=y_n+\delta y_n\left(m-\frac{\beta y_n}{x_n}-\frac{\alpha}{\gamma+y_n}\right),
\end{aligned}
\]
at the **coincident invasion and equilibrium-fold threshold** \(\alpha=m\gamma\), \(\beta=m/\gamma\), there is an open wedge of strictly positive states attracted to \((1,0)\) at a cubic, rather than quadratic, critical rate. Let
\[
A=\frac{\delta m(\gamma+1)}{\gamma^2},\qquad \kappa=\frac{m(\gamma+1)}{\gamma^2}.
\]
Every orbit in the wedge satisfies
\[
\boxed{\ y_n=\frac{1}{\sqrt{2An}}-\frac{\gamma(\gamma-1)}{2\delta m(\gamma+1)}\frac1n+O\!\left(\frac{\log n}{n^{3/2}}\right),\qquad
\lim_{n\to\infty}\frac{1-x_n-y_n}{y_n^3}=\kappa.\ }
\]
The \(n^{-1}\) coefficient is negative for \(\gamma>1\), positive for \(\gamma<1\), and zero at \(\gamma=1\). At this exact cancellation point there is a finite \(L=L(x_0,y_0)\) such that
\[
\boxed{\ y_n^{-2}=4\delta m n+(1+m+3\delta m)\log n+L+o(1).\ }
\]
The logarithmic coefficient depends on the discrete step size, even though the continuous vector field has the same cubic cusp leading term.

## Assumptions and scope
Fix arbitrary \(m>0\), \(\gamma>0\), \(0<\delta<2\), and put \(\alpha=m\gamma\), \(\beta=m/\gamma\). Choose any fixed
\[
0<\eta<\min\left\{\frac14,\frac{\gamma+1}{4\gamma}\right\}.
\]
There exists \(\varepsilon=\varepsilon(m,\gamma,\delta,\eta)>0\) such that the theorem holds for **all** initial states
\[
0<y_0<\varepsilon,\qquad |x_0+y_0-1|<\eta y_0.
\]
The wedge is open and nonempty; taking \(\varepsilon\) smaller ensures \(x_0>0\), and the iterations remain well-defined and strictly positive. Estimates and error constants may depend on the fixed parameters and orbit. Claims do not include the stable boundary \(y=0\) or all positive initial conditions.

## Proof
Write \(v=y\) and \(w=x+y-1\), so \(x=1-v+w\). Algebra at the stated double threshold gives the **exact** recurrences
\[
\begin{aligned}
V:=v_{n+1}&=v+\frac{\delta m v^2(\gamma w-(\gamma+1)v)}{\gamma(\gamma+v)(1-v+w)},\\
W:=w_{n+1}&=[1-\delta(1-v+w)]w+(V-v).
\end{aligned}
\tag{1}
\]
Set \(r=|1-\delta|<1\). For \(|w|<\eta v\), \(v>0\) small, the first recurrence has \(0<V<v\) and \(|V-v|\le C v^3\). The second gives \(|W|\le(r+C v)|w|+C v^3\). Uniformly decreasing \(\varepsilon\) makes \(|W|<\eta V\), because \(V/v\ge1-Cv^2\) and \(r<1\). Thus the wedge is forward invariant, and all trajectories stay positive. The monotone sequence \(v_n\) has a limit; if positive, the strict negative increment on the wedge would be bounded away from zero, a contradiction, so \(v_n\to0\).

Dividing the second recurrence by \(V\) yields \(w_{n+1}/v_{n+1}=(1-\delta+o(1))w_n/v_n+O(v_n^2)\), and contraction implies \(w_n/v_n\to0\). Therefore \(v_{n+1}=v_n-A v_n^3+o(v_n^3)\), with \(A>0\). The reciprocal-square increments satisfy \(v_{n+1}^{-2}-v_n^{-2}\to2A\), so Stolz–Cesàro (or averaging increments) gives \(n v_n^2\to1/(2A)\).

Next, \(q_n=w_n/v_n^3\) obeys \(q_{n+1}=(1-\delta+o(1))q_n-A+o(1)\). The coefficient is eventually uniformly contractive, hence \(q_n\to-A/\delta=-\kappa\). More precisely, putting \(e_n=w_n+\kappa v_n^3\) into (1) and expanding gives \(e_{n+1}=(1-\delta+O(v_n))e_n+O(v_n^4)\). The already established slow ratio \(v_{n+1}/v_n\to1\) and geometric contraction give \(e_n=O(v_n^4)\), i.e.
\[
w_n=-\kappa v_n^3+O(v_n^4).
\tag{2}
\]
This proves the locking limit. Substituting (2) into (1), using Taylor series with controlled remainders in the invariant wedge, yields
\[
v_{n+1}=v_n-A v_n^3-B v_n^4-C v_n^5+O(v_n^6),
\tag{3}
\]
where
\[
B=A\frac{\gamma-1}{\gamma},\qquad
C=A\left(1-\frac1\gamma+\frac1{\gamma^2}+\frac m\gamma\right).
\]
Consequently, writing \(z_n=v_n^{-2}\),
\[
z_{n+1}-z_n=2A+2Bv_n+(2C+3A^2)v_n^2+O(v_n^3).
\tag{4}
\]
Since \(v_n\sim(2An)^{-1/2}\), (4) first implies \(z_n=2An+O(\sqrt n)\), then \(v_n=(2An)^{-1/2}+O(n^{-1})\). Summing (4) once more gives
\[
z_n=2An+\frac{4B}{\sqrt{2A}}\sqrt n+O(\log n).
\]
Taking inverse square roots proves the two-term assertion, since the coefficient of \(n^{-1}\) is \(-B/(2A^2)=-\gamma(\gamma-1)/(2\delta m(\gamma+1))\).

If \(\gamma=1\), then \(B=0\), \(A=2\delta m\), and \(C=A(1+m)\). Now (4) gives \(z_n=2An+O(\log n)\), and hence \(v_n^2=(2An)^{-1}+O(\log n/n^2)\). Both \(\sum v_n^3\) and \(\sum |v_n^2-(2An)^{-1}|\) converge. Subtracting from (4) the harmonic term \(((2C+3A^2)/(2A))n^{-1}\), summing, and using \(\sum_{j=1}^{n}j^{-1}=\log n+\text{constant}+o(1)\), shows that \(z_n-2An-[(2C+3A^2)/(2A)]\log n\) has a finite limit. Finally \((2C+3A^2)/(2A)=1+m+3\delta m\). All limits are in the original discrete clock \(n\).

## Verification
A standalone `check.py` independently differentiates the exact rational recurrence symbolically, substitutes the rigorously obtained third-order locking curve, and checks the coefficients \(A,B,C\) and the logarithmic constant by algebraic identities. It also iterates three nonidentical positive parameter combinations and compares first- and second-order finite-time diagnostics. Run with `python check.py`; it requires Python and SymPy. These finite trajectories are diagnostics, not the proof of the infinite limits. The derivation above supplies that proof.

## Relationship to prior work
Liu, Ma and Hu (2024) analyze the Euler map's equilibria and codimension-one/two local bifurcations. Their transcritical theorem at \(\alpha=m\gamma\) **explicitly excludes** \(\alpha=\beta\gamma^2\), precisely the degenerate slice \(\beta=m/\gamma\). Du, Hu, Zheng, Cheng and Liu (2024) establish a cubic cusp normal form for the corresponding **continuous-time** predator–prey vector field. That result establishes the existence and sign of the continuous cusp; neither the existence of that cusp nor the general cubic-slowing mechanism is claimed as new here. The new assertion is the explicit open-wedge, two-term **discrete** extinction asymptotic, the third-order prey locking, and a finite renormalized inverse-square clock with step-dependent logarithmic coefficient at \(\gamma=1\). Related indexed laws for other ecological maps are not the same model and do not imply these constants.

## Limitations
Only the stated open local wedge and positive parameters are covered; no global extinction, basin boundary, attraction for negative populations, or behavior at \(\delta=2\) is claimed. A continuous-time cusp result is a materially close predecessor. It does not itself determine the Euler trajectory's subleading coefficient or logarithmic constant. The literature search was not exhaustive and publication priority is not independently certified. No independently conducted audit is asserted.

## References
1. M. Liu, L. Ma, D. Hu, *Some Bifurcations of Codimensions 1 and 2 in a Discrete Predator–Prey Model with Non-Linear Harvesting*, Mathematics **12** (2024), 2872. Published 2024-09-14. https://doi.org/10.3390/math12182872 (full HTML, equations (3), (7)–(10), Theorem 4, and conclusions inspected).
2. R. Du, D. Hu, Z. Zheng, L. Cheng, M. Liu, *High codimension bifurcations analysis in a predator-prey system with Michaelis-Menten type predator harvesting*, Discrete and Continuous Dynamical Systems - B **29** (2024), 3775–3801; early access 2024-02-28. https://doi.org/10.3934/dcdsb.2024023 (author-posted full textual rendering inspected, especially section 3, Theorem 3.1 and cubic normal form).
