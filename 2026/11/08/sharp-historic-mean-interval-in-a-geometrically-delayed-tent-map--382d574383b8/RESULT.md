# Sharp historic-mean interval in a geometrically delayed tent map

## Finding
Let \(k\ge2\) be an integer and \(z\in[0,1]\). For the symmetric tent map \(T(u)=2\min\{u,1-u\}\), let the delayed sequence satisfy \(x_0=z\) and
\[
x_{n+1}=T\!\left(x_{\lfloor n/k\rfloor}\right),\qquad n\ge0.
\]
Write its physical-time Cesàro mean as
\[
A_N(z)=\frac1N\sum_{n=0}^{N-1}x_n,\qquad N\ge1.
\]
The following two assertions hold simultaneously for every integer \(k\ge2\).

**Exact convergence classification.** The scalar sequence \(A_N(z)\) converges if and only if the ordinary tent orbit of \(z\) eventually reaches one of the fixed points \(0\) or \(2/3\). In this case its limit is that fixed point. Hence the set of initial points with a convergent delayed physical-time mean is countable.

**Exact typical oscillation interval.** For Lebesgue-almost every \(z\in[0,1]\), the set of all subsequential limits of \(A_N(z)\) is the full closed interval
\[
\boxed{\left[0,\frac{2k}{2k+1}\right].}
\]
Equivalently, the liminf is \(0\), the limsup is \(2k/(2k+1)\), and every intermediate number occurs as a subsequential limit. In contrast, for those same almost-everywhere initial points, the ordinary undelayed tent-orbit mean converges to \(1/2\).

## Assumptions and scope
All time indices are nonnegative integers. The delay uses the floor exactly as written; the delayed recurrence has no instantaneous term. The initial point is in the compact interval \([0,1]\), and the observable is the scalar state itself, not an arbitrary observable. All statements are exact and include dyadic/branch-boundary seeds. The almost-everywhere assertion uses Lebesgue measure on the initial point. The primary classification is ergodic-theoretic: convergence, failure of convergence, and the complete limit set of physical-time averages.

## Proof
**1. Exact plateaus and endpoint averages.** Put \(y_j=T^j(z)\) and
\[
B_{-1}=0,\quad B_m=\frac{k^{m+1}-1}{k-1}\quad(m\ge0),\quad B_m-B_{m-1}=k^m.
\]
Induction on \(m\), including the index shift in the recurrence, gives \(x_n=y_m\) whenever \(B_{m-1}\le n<B_m\). Thus for \(E_m=A_{B_m}\),
\[
B_m E_m=\sum_{j=0}^m k^j y_j,
\qquad
k^m y_m=B_m E_m-B_{m-1}E_{m-1}\quad(m\ge1).
\]
As \(m\to\infty\), \(B_m/k^m\to k/(k-1)\) and \(B_{m-1}/k^m\to1/(k-1)\). If \(A_N\to a\), then \(E_m\to a\) and the exact subtraction identity forces \(y_m\to a\). Conversely, if \(y_m\to a\), the plateau sequence \(x_n\to a\) and its Cesàro means converge to \(a\). Hence a physical-time mean exists exactly when the original orbit converges.

**2. Convergence of tent orbits.** By continuity, any possible limit of \(y_m\) is fixed by \(T\), so it must be \(0\) or \(2/3\). Near either fixed point the tent map is affine with slope of absolute value \(2\); if an orbit converged there without hitting it, its sufficiently small nonzero errors would eventually double at every step, a contradiction. Thus convergence is equivalent to eventual arrival at a fixed point. Each inverse fiber of \(T^j\) is finite, so the union of these two finite-preimage trees is countable.

**3. Typical tent orbits are dense.** Lebesgue measure is invariant under \(T\), as its two affine full branches each have inverse Jacobian \(1/2\). Moreover, it is ergodic: for any invariant measurable set \(D\) and each dyadic interval \(I\) of generation \(r\), the restriction of \(T^r\) maps \(I\) affinely onto \([0,1]\), so \(\mathrm{Leb}(D\cap I)/\mathrm{Leb}(I)=\mathrm{Leb}(D)\). Dyadic differentiation forces \(\mathrm{Leb}(D)\) to equal \(0\) or \(1\). The pointwise ergodic theorem applied to a countable base of nonempty open intervals shows that almost every forward orbit visits every such interval infinitely often and therefore is dense. It also gives \(r^{-1}\sum_{j<r}T^j(z)\to\int_0^1u\,du=1/2\) almost everywhere.

**4. The exact endpoint cluster set.** Fix a seed whose ordinary forward orbit is dense. Set \(\beta=1/k\). For any increasing subsequence of plateau indices, compactness and a diagonal extraction yield limits \(w_{-j}\in[0,1]\) of \(y_{m-j}\) for each fixed \(j\ge0\). Continuity forces \(T(w_{-j-1})=w_{-j}\), so \((w_0,w_{-1},\ldots)\) is a backward tent orbit. The geometric weights of the endpoint mean give
\[
\lim E_m=(1-\beta)\sum_{j=0}^\infty\beta^j w_{-j}
\]
along the extracted subsequence; finite-prefix convergence and a uniformly bounded geometric tail justify passage to the limit. Conversely, *every* backward orbit is attained as such an endpoint cluster limit: for each depth \(J\), use the infinitely recurrent dense forward orbit to choose arbitrarily large \(m\) with \(y_{m-J}\) as close as desired to \(w_{-J}\). Continuity of the finitely many iterates makes \(y_{m-j}\) close to \(w_{-j}\) for \(0\le j\le J\); a diagonal choice and the bounded tail complete the argument.

**5. A sharp universal upper bound.** The only inverse branches are \(u\mapsto u/2\) and \(u\mapsto1-u/2\). For every backward orbit,
\[
w_{-j}+\tfrac12 w_{-(j-1)}\le1\qquad(j\ge1).
\]
Writing \(S=\sum_{j\ge0}\beta^j w_{-j}\), multiply these inequalities by \(\beta^j\) and sum to obtain
\[
(1+\beta/2)S-w_0\le\frac{\beta}{1-\beta}.
\]
Because \(0\le w_0\le1\),
\[
0\le(1-\beta)S\le\frac{1}{1+\beta/2}=\frac{2k}{2k+1}.
\]
Both endpoints are sharp. For the lower endpoint use the constant-zero backward orbit. For the upper endpoint use \(w_0=1\) and recursively \(w_{-j}=1-w_{-(j-1)}/2\); then every preceding inequality is an equality. The density argument in Step 4 realizes both extrema as limits of the delayed endpoint averages.

**6. All physical times and the full interval.** On each plateau the state is constant. As the physical-time averaging endpoint varies from \(B_{m-1}\) to \(B_m\), its average lies between the two endpoint averages (it is a monotone fractional-linear function of the number of new observations). Therefore the entire sequence \(A_N\) has the same liminf and limsup as \((E_m)\), namely \(0\) and \(2k/(2k+1)\). Finally,
\[
|A_{N+1}-A_N|=\frac{|x_N-A_N|}{N+1}\le\frac1{N+1}\longrightarrow0.
\]
A bounded real sequence with successive differences tending to zero has every number between its liminf and limsup as a subsequential limit (apply consecutive-crossing indices). Hence the full cluster interval is exactly the stated one. This completes both assertions.

## Verification
The standalone `verify.py` uses exact rational arithmetic and tests the plateau/endpoint subtraction law across integer delays, the backward-inverse upper bound on every binary inverse word of length eight from 17 rational grid points for each tested delay, the extremizing backward construction, and an explicit primitive two-cycle. Execute `python3 verify.py` from the extracted directory. Expected final line: `VERIFY_OK exact_checks=27453 k_range=2..7 grid=17 inverse_depth=8`. These finite checks support arithmetic and indexing only; the infinite-time assertions depend on the proof above.

For illustration, the undelayed two-cycle \(\{2/5,4/5\}\) at \(k=2\) has ordinary mean \(3/5\), but the geometric plateau endpoint averages approach distinct values \(8/15\) and \(2/3\). This example is not used to infer the almost-everywhere statement.

## Relationship to prior work
Gade and Bhalekar introduced the homogeneous delayed tent/logistic construction, identified the exact geometrically increasing plateau endpoints, and noted qualitatively that physical-time averages need not agree with averages of the undelayed map (arXiv:2610.21635, §§2.3, 3). Those observations are prior work, not claimed here. The contribution is the all-seed convergence criterion and, for almost every seed of the tent map, the sharp complete physical-time Cesàro cluster interval with an explicit parameter-dependent upper endpoint. Classical historic-behavior literature, including Labouriau and Rodrigues (arXiv:1606.07017), concerns nonconvergent time averages for other dynamics, particularly heteroclinic flows, and does not in the inspected passages supply the present exact proportional-delay interval. The generic ergodicity of the full tent map and elementary facts about Cesàro averages are standard and not claimed as original.

## Limitations
This theorem concerns the homogeneous case and integer proportional-delay divisor \(k\ge2\). It does not cover the partially coupled nonhomogeneous recurrence, noninteger delay ratios, other maps, arbitrary observables, or stability under perturbations. The quantitative interval depends on the full-branch tent geometry. The supporting script is finite corroboration, not a certificate of the almost-everywhere theorem; broader historical priority beyond the named sources remains provisional.

## References
1. P. M. Gade and S. Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635v1, first public 2026-10-15. https://arxiv.org/abs/2610.21635
2. I. S. Labouriau and A. A. P. Rodrigues, *On Takens' Last Problem: tangencies and time averages near heteroclinic networks*, arXiv:1606.07017, first public 2016-06-22. https://arxiv.org/abs/1606.07017
3. D. Färm, *Nontypical Behaviour of Orbits and Birkhoff Averages for Expanding Maps*, Lund University doctoral thesis, 2011. https://www.lu.se/publikation/49527a5c-cbea-4bb1-b034-b0be1b91fc57
