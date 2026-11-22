# Infinitely many fold-to-flip sink windows in a three-dimensional symmetric sine map

## Finding
The real map introduced by Almatroud and collaborators is
\[
F_{p,q,g}(x,y,z)=\bigl(y,\sin z,\,px+qy-g\sin z\bigr),\qquad (p,q,g)\in\mathbb R^3.
\]
Put \(k=p+q-g\). For all \(k>0\), its entire **real fixed-point census** is determined by a strictly increasing sequence of thresholds. Define \(K_0=1\), and for every integer \(m\ge1\) let \(\zeta_m\) be the unique solution of
\[
\tan\zeta_m=\zeta_m,\qquad 2m\pi<\zeta_m<(2m+\tfrac12)\pi,
\qquad K_m=\sqrt{1+\zeta_m^2}.
\]
Then the number of distinct real equilibria is exactly
\[
N(k)=1+2\mathbf1_{k>1}
+4\#\{m\ge1:K_m<k\}
+2\#\{m\ge1:K_m=k\},\qquad k>0,
\]
where all sets counted are finite. In particular, \(N(k)=2k/\pi+O(1)\) as \(k\to+\infty\). New symmetric pairs of equilibria arise at every \(K_m\), with a unique positive root already present for \(k>1\).

A stronger **stability staircase** holds on the natural pure-sine-feedback limit \((p,q,g)=(0,0,-k)\). Put \(\eta_0\) equal to the unique solution of \(\tan\eta=-\eta\) in \((\pi/2,\pi)\), and for \(m\ge1\) let \(\eta_m\) be its unique solution in \(((2m+\tfrac12)\pi,(2m+1)\pi)\). Define \(H_m=\sqrt{1+\eta_m^2}\). There are exactly two attracting nonzero fixed points, related by central symmetry, **if and only if**
\[
\boxed{k\in\bigcup_{m\ge0}(K_m,H_m).}
\]
The intervals are mutually disjoint. At each lower endpoint \(K_m\), the corresponding fixed-point derivative has a multiplier \(+1\); at each upper endpoint \(H_m\), the newly created stable branch has a multiplier \(-1\). In every interior window the two nonzero fixed points are exponentially attracting in the full three-dimensional state space; no nonzero fixed point is attracting outside these windows. The origin is attracting precisely for \(0<k<1\) on the pure-feedback limit. The high-index window widths obey the sharp law
\[
\boxed{H_m-K_m=\frac{2}{(2m+1/2)\pi}+O(m^{-3}),\qquad m\to\infty.}
\]
For **each** such gain window there are also open neighborhoods of three-parameter systems with \(p,q\ne0\) and two attracting symmetric nonzero fixed points. Thus the staircase is not merely a collection of attracting states confined to a singular one-parameter surface.

## Assumptions and scope
The map is studied exactly as defined above, on all of \(\mathbb R^3\), with real parameters. The effective gain \(k=p+q-g\) is assumed positive for the global equilibrium census. The pure-feedback stability classification is restricted to \(p=q=0,g=-k\), with \(k>0\); full three-parameter persistence is asserted only locally near each strictly stable member of that family. A fixed point is called *attracting* when all three Jacobian eigenvalues have modulus strictly less than one; this implies a locally exponentially attracting fixed point. Counts refer to distinct points, with the origin counted once.

For \(k>0\), every equilibrium is precisely \((\sin z,\sin z,z)\) for a real solution \(z=k\sin z\). For a positive \(z\), the sine must be positive. Write \(I_m=(2m\pi,(2m+1)\pi)\), \(m\ge0\), and \(A_m=(2m+\tfrac12)\pi\).

## Proof
**1. Complete fixed-point count.** At a stationary state the first two coordinates must satisfy \(x=y=\sin z\), and the third must satisfy \(z=k\sin z\). The converse is immediate. The equation is odd, so nonzero roots come in opposite pairs. For \(k>0\), every positive root lies in one of the intervals \(I_m\), where \(\sin z>0\), and has \(z\le k\), so only finitely many intervals can contribute.

On \((0,\pi)\) the function \(h(z)=z/\sin z\) rises strictly from \(1\) to infinity, because \(\sin z-z\cos z\) has derivative \(z\sin z>0\) and tends to zero at the origin. Thus the first lobe has precisely one positive root for \(k>1\), none for \(0<k\le1\). On each \(I_m\) with \(m\ge1\), the numerator \(v(z)=\sin z-z\cos z\) of \(h'(z)\) increases strictly from \(-2m\pi\) to \((2m+1)\pi\). Its unique zero \(\zeta_m\) lies before \(A_m\) and satisfies \(\tan\zeta_m=\zeta_m\). Since \(h\to+\infty\) at both ends and has exactly this one minimum, the lobe has 0, 1, or 2 positive roots as \(k<K_m\), \(k=K_m\), or \(k>K_m\). At the minimum, \(h(\zeta_m)=1/\cos\zeta_m=\sqrt{1+\zeta_m^2}\). Distinct lobes have strictly ordered fold values because their critical locations lie in ordered intervals and \(\sqrt{1+z^2}\) increases for \(z>0\). Combining the positive roots, symmetry and the origin gives the exact formula for \(N(k)\).

The relation \(2m\pi<\zeta_m<(2m+1/2)\pi\) yields \(K_m=2m\pi+O(1)\). Consequently the number of fully opened higher positive lobes is \(k/(2\pi)+O(1)\). Each contributes four real nonzero equilibria, so \(N(k)=2k/\pi+O(1)\), including at fold parameters.

**2. Exact stability on the pure-feedback limit.** If \(p=q=0,g=-k\), the Jacobian at the stationary point corresponding to \(z\) is
\[
J_z=\begin{pmatrix}0&1&0\\0&0&\cos z\\0&0&k\cos z\end{pmatrix},\qquad
\operatorname{spec}(J_z)=\{0,0,k\cos z\}.
\]
Thus the fixed point is attracting exactly if \(\lvert k\cos z\rvert<1\). On an equilibrium branch, \(k\cos z=z\cot z=:w(z)\). In every interval \(I_m\) the function \(w\) decreases strictly because
\[
w'(z)=\frac{\sin z\cos z-z}{\sin^2z}<0;
\]
the numerator is negative for \(z>0\), since \(z-\sin z\cos z\) has derivative \(2\sin^2z\) and vanishes at zero.

For the first lobe, \(w\) decreases from \(1\) to \(-\infty\), crossing \(-1\) once at \(\eta_0\in(\pi/2,\pi)\) with \(\tan\eta_0=-\eta_0\). The positive fixed point (and its negative) is attracting precisely for \(1<k<h(\eta_0)=H_0\).

For every higher lobe, the smaller root lies to the left of \(\zeta_m\), where \(w>1\), hence is never attracting. The larger root lies to its right; along this branch \(w\) falls from \(1\) to \(-\infty\) as \(k\) increases. It crosses \(-1\) exactly once at \(\eta_m\in(A_m,(2m+1)\pi)\), so its symmetric pair is attracting precisely for \(K_m<k<H_m\). The relation \(\tan\eta_m=-\eta_m\), with negative cosine, gives \(H_m=-1/\cos\eta_m=\sqrt{1+\eta_m^2}\). On the origin the only nonzero eigenvalue is \(k\), so it is attracting exactly for \(0<k<1\). This exhausts *all* fixed points, not merely sampled orbits.

The intervals of attraction are disjoint. Indeed, for every \(m\ge0\), \(\eta_m<(2m+1)\pi<(2m+2)\pi<\zeta_{m+1}\); since \(z\mapsto\sqrt{1+z^2}\) increases, \(H_m<K_{m+1}\). At the gain boundaries the stated \(+1\) and \(-1\) Jacobian multipliers are exact; nonlinear stability at these neutral points is not asserted.

**3. Sharp shrinking windows.** Let \(A=A_m=(2m+1/2)\pi\). The two defining transcendental equations become \(\cot\varepsilon=A-\varepsilon\) with \(\zeta_m=A-\varepsilon\) and \(\cot\delta=A+\delta\) with \(\eta_m=A+\delta\), where \(0<\varepsilon,\delta<\pi/2\). Since \(\cot t=1/t-t/3+O(t^3)\) as \(t\downarrow0\), monotonicity and substitution yield \(\varepsilon=A^{-1}+O(A^{-3})\) and \(\delta=A^{-1}+O(A^{-3})\). Taylor expansion of \(\sqrt{1+z^2}\) at \(A\) gives
\[
K_m=A-\frac1{2A}+O(A^{-3}),\qquad
H_m=A+\frac3{2A}+O(A^{-3}),
\]
so their difference is exactly \(2/A+O(A^{-3})\) at the stated order.

**4. Genuine three-parameter persistence.** Fix any \(m\ge0\) and any \(k\in(K_m,H_m)\). Each of the two opposite nonzero equilibria at \((p,q,g)=(0,0,-k)\) has all multipliers strictly in the unit disc. Thus \(I-DF\) is invertible at each; the implicit-function theorem gives nearby fixed points for nearby parameters, and continuous eigenvalues preserve strict attraction on an open three-parameter neighborhood. Because the map is odd, these two equilibria remain symmetry-related and distinct. The neighborhood contains coefficient triples with \(p,q\ne0\); hence this produces two attracting equilibria in full-dimensional parameter regions for infinitely many unbounded net gains.

## Verification
The standalone Python checker `verify.py` computes the fold and flip roots by bisection, verifies the sign changes, checks the strict stability multipliers of reconstructed equilibria, and tests the claimed asymptotic width against increasing lobe indices. Run `python3 verify.py` for `VERIFY_OK`. These finite diagnostics are not an infinite-count proof; that is supplied by the monotonicity and asymptotic arguments above.

For the published numerical parameter triple \((p,q,g)=(1.7,1.9,0.5)\), the effective gain is \(k=3.1\). Since \(1<3.1<K_1\), the global census identifies exactly three fixed points (the origin and two nonzero symmetry partners), even though the source's local stability analysis concentrates on the origin.

## Relationship to prior work
The originating 2024 paper [1] gives the exact 3D map and notes its stationary equation \(z=(p+q-g)\sin z\). It studies linear stability at the origin and numerical multistability, but does not enumerate the nonzero stationary states across all net gains, give the infinite exact fold sequence, or quantify the fold-to-flip attraction intervals and their inverse-index width. The theorem neither asserts that the original authors claimed uniqueness of the origin nor treats their numerical chaotic-attractor evidence as an analytic proof. The results use the full published equations, not only a generic one-dimensional sine-map analogy.

A later discussion by Wilczak, Serrano and Barrio [2] also treats recurring saddle-node creation in a scalar sine-map example; that qualitative mechanism is acknowledged, not asserted to be new here. Only an indexed passage, not its complete text, was available for comparison. The standard one-dimensional sine iteration and scalar tangency conditions are classical background. The new claim is the integrated full three-dimensional equilibrium census plus the exact repeated attraction-window geometry, its sharp width coefficient, and its nondegenerate open-parameter persistence for the published 3D family. Prior indexed periodic-orbit analyses of this or related 3D sine-delay systems concern primitive period-two cycles, different parameter surfaces, or added linear feedback and do not provide this full fixed-point staircase. Unindexed equivalent analyses remain a publication-priority risk.

## Limitations
The complete equilibrium count is for the positive net-gain half-space \(k>0\). Exact stability-window boundaries are proven on the pure-feedback coefficient line; elsewhere only local persistence is claimed, not global optimality of the full three-parameter stability region. We make no assertion about primitive two-cycles, invariant measures, chaotic attractors, global basins, or nonlinear stability at neutral endpoints. The asymptotics are at fixed model structure as \(m\to\infty\). No independent mathematical validation has been performed.

## References
[1] O. A. Almatroud, M. Abu Hammad, A. Dababneh, L. Diabi, A. Ouannas, A. A. Khennaoui and S. Alshammari, *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry **16** (2024), 1093, first published 2024-08-22. https://doi.org/10.3390/sym16081093 (full open-access HTML, especially §2, equations (1)–(5), and §3).

[2] D. Wilczak, S. Serrano and R. Barrio, *A mechanism for growth of topological entropy and global changes of the shape of chaotic attractors*, arXiv:2504.04887 (2025), https://arxiv.org/abs/2504.04887 (related scalar-sine qualitative background; full text not inspected).
