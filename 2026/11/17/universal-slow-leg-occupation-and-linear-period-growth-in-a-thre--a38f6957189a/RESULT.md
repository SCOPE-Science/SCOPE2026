# Universal slow-leg occupation and linear period growth in a three-species Lotka–Volterra flow

## Finding

Fix any \(a,d,K>0\) and consider the positive three-species differential system
\[
\dot B=B(-a+C+D),\qquad
\dot C=C(d-a-B+D),\qquad
\dot D=D(d-B-C).
\]
The quantity \(K=BD/C\) is invariant. On each surface \(BD/C=K\) there is exactly one positive equilibrium; all other positive trajectories on that surface are simple periodic orbits.

Define the energy and its minimum by
\[
E=H_K(B,D)=B+D+\frac{BD}{K}-d\log B-a\log D,
\qquad E_*(K)=\min_{B,D>0}H_K(B,D).
\]
For every \(E>E_*(K)\), let \(T_K(E)\) be the *minimal original-time period* of the corresponding periodic trajectory. With \(a,d,K\) held fixed,
\[
\boxed{\lim_{E\to\infty}\frac{T_K(E)}E=\frac1{ad}.}
\]
The leading coefficient does not depend on the conserved leaf parameter \(K\).

Let \((B_E(t),C_E(t),D_E(t))\) traverse this orbit once in original physical time. For every bounded continuous function \(f:\mathbb R^3\to\mathbb R\),
\[
\lim_{E\to\infty}\frac1{T_K(E)}\int_0^{T_K(E)}
 f\left(-\frac{\log B_E(t)}E,-\frac{\log C_E(t)}E,-\frac{\log D_E(t)}E\right)\,dt
=\int_0^1 f\left(\frac{s}{d},\frac{s}{d}+\frac{1-s}{a},\frac{1-s}{a}\right)\,ds.
\]
Thus the time-sampled logarithmic abundance vector converges weakly to the **uniform arclength distribution on an explicit line segment**. The entire limit is independent of \(K\). Equivalently, \((-d\log B/E,-a\log D/E)\) converges to \((U,1-U)\) with \(U\) uniform on \([0,1]\). These two assertions constitute one theorem about the asymptotic periodic dynamics of the specified flow.

## Assumptions and scope

All three species are strictly positive, the coefficients \(a,d\) and invariant \(K\) are fixed positive constants, and only energy \(E\) tends to positive infinity. The system is the three-block case \((k,l,m)=(1,1,1)\), with the parameters \(b=-a\), \(c=d-a\), of the integrable Lotka–Volterra family described by van der Kamp, McLaren and Quispel (2024). The conservation law and reduction are not asserted to be new. No uniformity in varying parameters or leaf number is claimed.

## Proof

**1. Canonical leaf reduction and global periodicity.** Differentiate \(\log(BD/C)\) using the three differential equations: its derivative is
\[
(-a+C+D)+(d-B-C)-(d-a-B+D)=0.
\]
On \(BD/C=K\), set \(p=\log B\) and \(q=\log D\), so that \(C=e^{p+q}/K\). The equations reduce exactly to
\[
\dot p=\partial_q F_K(p,q),\qquad
\dot q=-\partial_p F_K(p,q),
\quad F_K=e^p+e^q+K^{-1}e^{p+q}-dp-aq.
\]
The Hessian of \(F_K\) is
\[
\begin{pmatrix}e^p+u&u\\u&e^q+u\end{pmatrix},\qquad u=K^{-1}e^{p+q}>0,
\]
whose leading principal minor and determinant \(e^{p+q}+u(e^p+e^q)\) are positive. Moreover \(F_K\) is proper: \(F_K\ge(e^p-dp)+(e^q-aq)\), and each summand tends to infinity at both ends of its argument. Hence \(F_K\) has a unique nondegenerate global minimum, and every level above it is a smooth strictly convex closed curve. Canonical Hamiltonian motion runs around that curve with nonzero velocity, so it is a single minimal periodic orbit. This proves completeness and the positive-leaf classification.

**2. Area-to-period identity.** Let \(\Omega_E=\{(p,q):F_K(p,q)\le E\}\), \(A_K(E)=\operatorname{area}(\Omega_E)\), and \(g_K(E)=\sqrt{A_K(E)}\), for \(E>E_*(K)\). The coarea formula and the canonical velocity identity \(\lvert(\dot p,\dot q)\rvert=\lvert\nabla F_K\rvert\) give
\[
A_K'(E)=\oint_{F_K=E}\frac{ds}{\lvert\nabla F_K\rvert}=T_K(E).
\]
By convexity, \((1-\theta)\Omega_{E_1}+\theta\Omega_{E_2}\subseteq\Omega_{(1-\theta)E_1+\theta E_2}\). The two-dimensional Brunn–Minkowski inequality implies that \(g_K(E)\) is concave in \(E\). It is nondecreasing and continuously differentiable for \(E>E_*(K)\).

**3. Exact leading area.** In scaled coordinates \((u,v)=(p/E,q/E)\), the indicators of \(E^{-1}\Omega_E\) converge almost everywhere to the indicator of the triangle
\[
\mathcal T=\{(u,v):u\le0,\ v\le0,\ -du-av\le1\}.
\]
Indeed if \(u>0\) or \(v>0\), at least one positive exponential dominates \(F_K(Eu,Ev)/E\) and the point is eventually outside. If \(u<0,v<0\), all exponentials tend to zero, giving \(F_K(Eu,Ev)/E\to-du-av\). Boundary cases have planar Lebesgue measure zero. The scaled sublevel sets lie in one fixed bounded rectangle for all sufficiently large \(E\): this follows from \(F_K\ge(e^p-dp)+(e^q-aq)\) and the finite minima of the two separate summands, giving \(p\ge-E/d-O(1)\), \(q\ge-E/a-O(1)\) and \(p,q\le O(\log E)\). Dominated convergence therefore gives
\[
\lim_{E\to\infty}\frac{A_K(E)}{E^2}=\operatorname{area}(\mathcal T)=\frac1{2ad}.
\]
It follows that \(g_K(E)/E\to1/\sqrt{2ad}\). For a nondecreasing differentiable concave function with an asymptotic slope, its decreasing derivative tends to the same slope (by the secant-slope bounds). Thus \(g_K'(E)\to1/\sqrt{2ad}\). Combining with \(T_K(E)=2g_K(E)g_K'(E)\) proves \(T_K(E)/E\to1/(ad)\). This step does not infer a derivative asymptotic from area growth without the required concavity argument.

**4. The time-sampled limit.** Fix \(0<\delta<1/2\). For every \(p\) in
\[
-\frac{(1-\delta)E}{d}\le p\le-\frac{\delta E}{d},
\]
the energy level has a unique lower branch \(q=q_E(p)<0\). Its equation and the strict negativity of the logarithmic coordinates imply, uniformly over this interval,
\[
q_E(p)=-\frac{E+dp}{a}+o(1),\qquad
\dot p=-a+o(1).
\]
For clarity, the first statement follows by evaluating \(F_K\) at \(q_0=-(E+dp)/a\), where the discrepancy from \(E\) is exponentially small, and using \(\partial_qF_K=-a+o(1)\) in a fixed neighborhood of \(q_0\). Thus the lower branch traverses this \(p\)-interval exactly once, in time
\[
\frac{(1-2\delta)E}{ad}+o(E).
\]
Parametrize this traversal by \(s=-dp/E\in[\delta,1-\delta]\). Along it,
\[
\left(-\frac{\log B}{E},-\frac{\log C}{E},-\frac{\log D}{E}\right)
=\left(\frac{s}{d},\frac{s}{d}+\frac{1-s}{a},\frac{1-s}{a}\right)+o(1)
\]
uniformly, because \(\log C=p+q-\log K\). Further, \(dt/T_K(E)=(1+o(1))\,ds\), uniformly on the traversal. Its normalized duration approaches \(1-2\delta\). Since the whole orbit has normalized duration one, the remaining part has limiting time mass at most \(2\delta\). For each bounded continuous \(f\), integrate on the lower branch, bound the complementary contribution by its mass times \(\lVert f\rVert_\infty\), then let \(\delta\downarrow0\). This proves the asserted weak convergence and its independence of the initial phase.

## Verification

The standalone script `check.py` symbolically verifies the conserved leaf and exact canonical reduction, computes two independent finite-energy area derivatives by nested one-dimensional quadrature, and reports their approach to the proven period slope \(1/(ad)\) for two parameter triples. Numerical quadrature does not prove the infinite-energy limit; the analytic area, concavity and traversal arguments above do.

Run `python check.py` with Python 3, NumPy, SciPy and SymPy. The script uses no external data, random seeds or hidden files.

## Relationship to prior work

Van der Kamp, McLaren and Quispel identify the three-block system, its Poisson and Darboux integrals, and Lambert-W solvability. Those tools give integrability, but the relevant inspected full text does not state the linear high-energy physical-period slope or the time-uniform logarithmic population law. The 2019 skew-interaction classification of Kobayashi, Suzuki and Yamada covers periodicity in broader families; periodicity itself is therefore only a prerequisite here. Classical Waldvogel and later period-energy work treat two-species or separable Hamiltonians; the present canonical Hamiltonian includes the mixed term \(e^{p+q}/K\) and the three-species time-sampling conclusion. Published results on skew Lotka–Volterra metapopulations focus on migration-driven convergence, not on this high-energy statement in the inspected introductory and model sections.

## Limitations

The result concerns fixed strictly positive \(a,d,K\) and the indicated three-species family, not arbitrary three-block parameters or all skew-symmetric Lotka–Volterra systems. The time limit is weak convergence for bounded continuous tests, not total-variation convergence. No numerical rate, next-order period constant, finite-sample confidence interval, or optimal uniform remainder is proved. A more general pre-existing tropical/convex-Hamiltonian asymptotic theorem could imply the result without matching the model's wording; no universal novelty claim is made. Some older broad periodic-orbit and period-asymptotic papers were inspected only through accessible abstracts or excerpts; see the review for priority limitations.

## References

1. P. H. van der Kamp, D. I. McLaren, and G. R. W. Quispel, *On a quadratic Poisson algebra and integrable Lotka–Volterra systems with solutions in terms of Lambert's W function*, arXiv:2408.14720v1 (first submitted 2024-08-27); later v2, 2024-10-29. https://arxiv.org/html/2408.14720v2
2. M. Kobayashi, T. Suzuki, and Y. Yamada, *Lotka–Volterra Systems with Periodic Orbits*, Funkcialaj Ekvacioj 62 (2019), 129–155. DOI: 10.1619/fesi.62.129.
3. J. Waldvogel, *The Period in the Volterra–Lotka Predator-Prey Model*, SIAM J. Numer. Anal. 20 (1983), 1264–1272. DOI: 10.1137/0720098.
4. S. Foschi, G. Mingari Scarpello, and D. Ritelli, *Higher Order Approximation of the Period-energy Function for Single Degree of Freedom Hamiltonian Systems* (2003); accessible abstract and excerpt, method concerns separated variables.
5. *On the Dynamics of Lotka–Volterra Equations Having an Invariant Hyperplane*, SIAM J. Appl. Math. (1998). DOI: 10.1137/S0036139997319463.
6. A. S. Anish, B. De Baets, and S. Rao, *Metapopulation models with anti-symmetric Lotka–Volterra systems*, Journal of Biological Dynamics 18 (2024), article 2397404. DOI: 10.1080/17513758.2024.2397404.
