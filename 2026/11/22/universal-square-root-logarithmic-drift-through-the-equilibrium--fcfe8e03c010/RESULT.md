# Universal square-root-logarithmic drift through an equilibrium-line degeneracy

## Finding
For the quadratic differential equation
\[
\dot x=yz,\qquad \dot y=x^2-y,\qquad \dot z=-4x,
\]
the equilibrium line \(\{(0,0,z):z\in\mathbb R\}\) coexists with a nonempty open set of forward-global solutions that escape to \(z=-\infty\) at a universal square-root-logarithmic speed, even though \(x\) and \(y\) both tend to zero. This is the zero-forcing \(a=b=0\) member of the Algaba–Domínguez-Moreno–Merino–Rodríguez-Luis two-parameter quadratic flow studied also by Qu and Yang.

For every initial point with
\[
x_0>0,\quad w_0=-z_0\ge3,\quad
\frac12\le\frac{y_0}{x_0^2}\le2,\quad 0<w_0x_0\le\frac1{10},
\]
the exact universal asymptotic constants are
\[
\lim_{t\to\infty}t\,x(t)(-z(t))=1,\qquad
\lim_{t\to\infty}\frac{z(t)^2}{8\log t}=1,\qquad
\lim_{t\to\infty}\frac{y(t)}{x(t)^2}=1.
\]
Consequently,
\[
z(t)\sim-\sqrt{8\log t},\quad
x(t)\sim\frac1{t\sqrt{8\log t}},\quad
y(t)\sim\frac1{8t^2\log t}.
\]

## Assumptions and scope
The solution is a classical maximal real solution of the displayed polynomial vector field, with time \(t\ge0\), and \(\sim\) means ratio tending to one (the signed expression for \(z\) is interpreted with its negative sign). The initial inequalities describe an invariant region and contain an open subset of \(\mathbb R^3\); for instance \(x_0=1/100\), \(y_0=1/10000\), \(z_0=-3\) is admitted. The constant values \(3\) and \(1/10\) are sufficient convenient trapping bounds, not claimed sharp. The theorem is not a complete classification of initial conditions and is restricted to \(a=b=0\).

## Proof
Put \(w=-z>0\), \(r=y/x^2\), and \(h=wx\) whenever \(x>0\). Direct differentiation, with no approximation, gives
\[
\dot x=-wrx^2,\qquad\dot w=4x,\qquad
\dot r=1-r+2hr^2,\qquad
\dot h=h^2\left(\frac4{w^2}-r\right).
\]
At \(r=1/2\), \(\dot r=1/2+h/2>0\); at \(r=2\), \(\dot r=-1+8h\le-1/5<0\). Since \(w\ge3\) and \(r\ge1/2\), the last equation gives
\[
\dot h\le\left(\frac49-\frac12\right)h^2=-\frac1{18}h^2<0.
\]
Also \(\dot w=4x>0\). Thus the closed constraints \(w\ge3\), \(1/2\le r\le2\), and \(0<h\le1/10\) are forward invariant, as long as the solution exists with \(x>0\). On each finite time interval, \(0<x(t)\le x_0\) and \(w(t)\le w_0+4x_0t\); since \(\dot x=-wrx^2\), \(x\) cannot reach zero in finite time. Moreover \(y=rx^2\) stays bounded. The polynomial solution therefore exists for all \(t\ge0\), and the invariant-region argument is global.

Since \(h\) is positive and \(\dot h\le-h^2/18\), we have \(h(t)\to0\). If \(w\) had a finite upper bound \(W\), then \(\dot x\ge-2W x^2\), so \(x(t)\ge[x_0^{-1}+2Wt]^{-1}\). Its integral over \([0,\infty)\) diverges, contradicting \(w(t)=w_0+4\int_0^t x(s)ds\le W\). Hence \(w(t)\to+\infty\).

The exact equation \(\dot r+(r-1)=2hr^2\) has forcing bounded between zero and \(8h(t)\to0\). Variation of constants proves \(r(t)\to1\). Using the exact reciprocal identity
\[
\frac d{dt}\left(\frac1h\right)=r-\frac4{w^2}\longrightarrow1,
\]
we obtain \(1/h(t)\sim t\) and therefore \(t h(t)\to1\). Finally, \(\frac d{dt}(w^2)=8wx=8h\), hence
\[
w(t)^2=w_0^2+8\int_0^t h(s)ds\sim8\log t.
\]
Since \(w=-z\), \(x=h/w\), and \(y=rx^2\), all three stated asymptotic equivalents follow. In particular, \(w\to\infty\) proves genuine escape, not convergence to a finite point on the equilibrium line.

## Verification
The accompanying standalone `check.py` verifies both transformed derivative identities symbolically using SymPy, checks the signs at all trapping boundaries exactly, and integrates three interior initial values using SciPy through time \(100000\). It checks preservation of the invariant bounds on observation times and reports the convergence diagnostics \(r\), \(twx\), and \(w^2/(8\log t)\). Numeric calculations are supporting consistency checks only: the infinite-time limits and invariance are proved above analytically. Execute `python check.py` with SymPy and SciPy installed.

## Relationship to prior work
Algaba and coauthors introduced this two-parameter flow to study homoclinic-flip bifurcations. Qu and Yang gave a classification of its equilibria, identifying the nonisolated line exactly when \(a=b=0\), and analyzed local bifurcations at isolated equilibria and Poincaré dynamics at infinity. Giraldo, Krauskopf and Osinga investigated connecting orbits to infinity for homoclinic-flip phenomena. The proved theorem here instead isolates an explicit forward-invariant physical-time channel in the degenerate equilibrium-line regime and calculates the leading asymptotic constants for coordinatewise drift. These formulas do not follow from the cited qualitative bifurcation or compactification statements. The accessible Algaba author upload exposes only limited searchable full-text material; that access limit leaves residual priority uncertainty.

## Limitations
No global portrait for arbitrary starting points or for \(a\ne0\) or \(b\ne0\) is asserted. The trapping constants are sufficient rather than optimal; the logarithmic laws are first-order equivalents, not uniform-in-parameters expansions. The asymptotic class is a nonempty open sector, not necessarily the whole escaping basin. Independent external mathematical validation has not occurred.

## References
1. Algaba, A., Domínguez-Moreno, M. C., Merino, M., and Rodríguez-Luis, A. J., Study of a simple 3D quadratic system with homoclinic flip bifurcations of inward twist case C_in, Communications in Nonlinear Science and Numerical Simulation 77 (2019), 324–337, doi:10.1016/j.cnsns.2019.05.005. Author full text publicly uploaded 2019-05-16: https://www.researchgate.net/publication/332988091_Study_of_a_simple_3D_quadratic_system_with_homoclinic_flip_bifurcations_of_inward_twist_case_C
2. Qu, J., and Yang, S., New Insights on Non-integrability and Dynamics in a Simple Quadratic Differential System, Journal of Nonlinear Mathematical Physics 31 (2024), article 10, published 2024-02-21, https://doi.org/10.1007/s44198-024-00174-4
3. Giraldo, A., Krauskopf, B., and Osinga, H. M., Computing connecting orbits to infinity associated with a homoclinic flip bifurcation, Journal of Computational Dynamics 7 (2020), 489–510, https://doi.org/10.3934/jcd.2020020
