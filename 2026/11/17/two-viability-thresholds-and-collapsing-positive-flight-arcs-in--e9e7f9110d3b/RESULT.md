# Two viability thresholds and collapsing positive-flight arcs in a geometric-mean predator–prey flow

## Finding
For the square-root predator–prey flow on the nonnegative quadrant, the oscillator first integral supports a complete classification of **maximal strictly positive trajectories**, not just the unrestricted harmonic oscillator. There are two changes in the number of biologically admissible angular arcs, and one short trajectory family disappears with a sharp linear duration law. The nonnegative boundary is not forward-unique.

## Assumptions and scope
Fix \(r>0\) and normalized physical time \(t\). Consider nonnegative classical solutions of
\[
\dot X=\sqrt X(\sqrt Y-1),\qquad \dot Y=\sqrt Y(r-\sqrt X).
\]
For a strictly positive initial state set \(u=\sqrt X>0\), \(v=\sqrt Y>0\), and
\[
\rho=\sqrt{(u-r)^2+(v-1)^2},\quad m=\min\{r,1\},\quad M=\max\{r,1\},\quad R=\sqrt{r^2+1}.
\]
At \(\rho=0\) the positive coexistence equilibrium is \((X,Y)=(r^2,1)\). For \(\rho>0\), let
\[
\alpha(\rho)=\begin{cases}0&\rho\le r,\\\arccos(r/\rho)&\rho>r,\end{cases}\qquad
\beta(\rho)=\begin{cases}0&\rho\le 1,\\\arccos(1/\rho)&\rho>1.\end{cases}
\]
A maximal strictly positive segment is an orbit restricted to one connected component of \(\{\phi\bmod 2\pi:r+\rho\cos\phi>0,\ 1+\rho\sin\phi>0\}\); duration means the full time-length of that component (independent of which interior point parametrizes it). Endpoints are excluded by strict positivity.

**Exact phase portrait.** Every nonstationary positive solution is complete and periodic with period \(4\pi\) if and only if \(0<\rho<m\). For \(m\le\rho<M\), there is one maximal positive component of duration
\[
\tau_{\rm one}=4\pi-4[\alpha(\rho)+\beta(\rho)].
\]
For \(M\le\rho<R\), there are two components with durations
\[
\tau_{\rm long}=3\pi-2[\alpha(\rho)+\beta(\rho)],\qquad
\tau_{\rm short}=\pi-2[\alpha(\rho)+\beta(\rho)].
\]
For \(\rho\ge R\), only the long component remains, of duration \(\tau_{\rm long}\). If \(r=1\), then \(m=M=1\), the intermediate one-component interval is empty, and the two components appear together at \(\rho=1\). At \(\rho=m\), a strictly positive complete periodic orbit no longer exists, because a nonnegative coordinate vanishes at one or two phases.

The short component disappears at the critical radius \(R\), with
\[
\tau_{\rm short}(\rho)=\frac{2R}{r}(R-\rho)+O_r((R-\rho)^2),\qquad \rho\uparrow R.
\]
The fraction of an unrestricted oscillator phase circle lying inside the strictly positive quadrant is \(1-[\alpha(\rho)+\beta(\rho)]/\pi\) up to \(\rho\le R\), and \([3\pi/2-\alpha(\rho)-\beta(\rho)]/(2\pi)\) for \(\rho>R\). This is a geometric fraction, not a physical occupation measure beyond the first boundary hit.

**Boundary branching.** Every point \((X,Y)=(0,v_0^2)\) with \(v_0\ge0\) has distinct forward nonnegative classical continuations. It can remain on the predator-free axis \(X=0\), where \(\sqrt{Y(t)}=v_0+rt/2\), or after any delay \(s\) with \(v_0+rs/2>1\) it can depart along an interior harmonic arc. Thus the periodic square-coordinate formula, when allowed to run through negative square roots, is not a solution of the original nonnegative ODE in general.

## Proof
On \(X,Y>0\), the principal square roots satisfy exactly
\[
\dot u=(v-1)/2,\qquad \dot v=(r-u)/2.
\]
It follows that \(\rho\) is constant. For \(\rho>0\), every interior orbit has the unique lift
\[
u=r+\rho\cos\phi,\qquad v=1+\rho\sin\phi,\qquad \dot\phi=-1/2.
\]
Conversely, on any open phase interval for which both displayed variables are positive, their squares solve the original equations. This converse is restricted to the positive lift: if \(u\) or \(v\) changes sign, squaring can reverse the sign of the relevant velocity, so the unrestricted oscillator does not globally conjugate the physical flow.

For \(\rho>r\), the prohibited phases \(u\le0\) form the closed interval centered at \(\pi\) of half-width \(\alpha\); otherwise it is empty (or a singleton at equality). For \(\rho>1\), the prohibited phases \(v\le0\) form the closed interval centered at \(3\pi/2\) of half-width \(\beta\); otherwise it is empty (or a singleton at equality). If exactly one nonempty prohibited interval is present, its complementary positive arc has angular length \(2\pi-2(\alpha+\beta)\). At a single tangent threshold, the prohibited singleton likewise removes that phase. With two prohibited intervals present, their centers differ by \(\pi/2\). Before they overlap, the two positive complements have angular lengths \(3\pi/2-\alpha-\beta\) and \(\pi/2-\alpha-\beta\).

The overlap threshold is \(\alpha+\beta=\pi/2\). For \(\rho>\max(r,1)\), the identity
\[
\cos(\alpha+\beta)=\frac{r-\sqrt{(\rho^2-r^2)(\rho^2-1)}}{\rho^2}
\]
shows the threshold is exactly \(\rho^2=r^2+1\); on and beyond it, only the long complement survives. Multiplying angular lengths by \(2\), since \(|\dot\phi|=1/2\), proves all displayed durations. For the collapse, differentiate:
\[
(\alpha+\beta)'(\rho)=\frac{r}{\rho\sqrt{\rho^2-r^2}}+\frac{1}{\rho\sqrt{\rho^2-1}},
\]
whose value at \(\rho=R\) is \(R/r\). Taylor expansion of \(\pi-2(\alpha+\beta)\) yields \(2R(R-\rho)/r+O_r((R-\rho)^2)\).

Finally fix \((0,v_0^2)\) and a delay \(s\ge0\) with \(v_s=v_0+rs/2>1\). Follow \(X=0,\sqrt Y=v_0+rt/2\) for \(0\le t\le s\), then for \(t>s\) set \(u(s)=0,v(s)=v_s\), evolve the preceding harmonic system on its first strictly positive time interval, and put \(X=u^2,Y=v^2\). The right derivative at the join equals \((0,rv_s)\), identical to the derivative along the axis, because \(2u\dot u=0\) there and \(2v\dot v=rv_s\). This yields a nonnegative \(C^1\) solution locally past \(s\), distinct from the axis-only trajectory. Multiple choices of \(s\) prove nonuniqueness without assuming any continuation through later boundary hits.

## Verification
The derivation is algebraic; no numerical sampling is used as proof of the global arc count. The included `verify.py` independently samples phase circles at multiple noncritical radii and compares their strictly positive angular-component lengths to the formulas; it also checks the claimed derivative and matching boundary tangents. Reproduce with `python3 verify.py` using only the Python standard library. The numerical component is illustrative only; all infinite and exact statements are proved above.

## Relationship to prior work
Kaniadakis (2022) introduced the square-root predator–prey equations, Hamiltonian first integral and explicit harmonic canonical flow (his Sec. IV). Da Silva, Carbone and Kaniadakis (2023) supplied the normalized equations, oscillator-circle interpretation and exact squared waveforms (their Sec. II, Eqs. (8), (13)–(20)), and discussed finite-time stopping when prey disappears (Sec. III). The present classification does not claim the oscillator reduction or its period as new: it identifies the full positive-domain orbit-component topology at the two biologically natural radii, a sharp collapse rate of a positive flight, and concrete nonuniqueness of forward nonnegative continuations. The squared harmonic formula alone is not a globally valid continuation through sign-changing lifted square roots.

## Limitations
The formula concerns normalized physical time, deterministic initial states and maximal intervals of **strict positivity**. At a non-Lipschitz boundary the model does not prescribe a unique continuation; no selection mechanism or stochastic extinction law is asserted. The geometric phase fraction is not a long-time physical occupation fraction for a boundary-hitting trajectory. While the two primary source texts were inspected, potential equivalent presentations in less-indexed literature remain a priority risk. The new features are elementary consequences of the known oscillator structure; their value lies in a complete positivity-constrained classification, not in discovering a new invariant.

## References
1. G. Kaniadakis, *Novel predator-prey model admitting exact analytical solution* (2022), arXiv:2208.02457; https://arxiv.org/abs/2208.02457 .
2. S. L. da Silva, A. Carbone and G. Kaniadakis, *Quantifying population dynamics via a geometric mean predator–prey model*, *Chaos* **33** (2023), DOI:10.1063/5.0158723; https://doi.org/10.1063/5.0158723 .
