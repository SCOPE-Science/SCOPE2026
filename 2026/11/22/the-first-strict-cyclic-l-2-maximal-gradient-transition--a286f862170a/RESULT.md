# The first strict cyclic \(L^2\) maximal-gradient transition

## Finding
For \(n=3,4\), define the uncentered contiguous-arc maximal operator on \(C_n=\mathbb Z/n\mathbb Z\) by
\[
(\mathcal M_n f)(j)=\max_{1\leq\ell\leq n}\;\max_{0\leq r<\ell}\frac{1}{\ell}\sum_{k=0}^{\ell-1}|f(j-r+k\bmod n)|.
\]
Write \(V_2(f)^2=\sum_{j=0}^{n-1}|f(j+1\bmod n)-f(j)|^2\). For every nonconstant complex-valued \(f\) on \(C_n\), the *sharp* constants in \(V_2(\mathcal M_n f)\leq C_nV_2(f)\) are
\[
C_3=\frac12,\qquad C_4=\sqrt{\frac{7+\sqrt{13}}{36}}>\frac12.
\]
In particular, the first step from three to four cyclic sites creates a strict increase in the optimal second-variation ratio. At four sites an attaining signal is
\[
f=(1,t,0,t),\qquad t=\frac{5-\sqrt{13}}6.
\]

## Assumptions and scope
All arcs are contiguous in the cyclic order and contain the evaluation vertex. Their lengths range from one to the entire cycle, and averages are unweighted. The signal may be real or complex; the sharpness examples are real and nonnegative. The claim is restricted to \(n\in\{3,4\}\); it asserts neither a formula nor monotonicity for larger cycles. The constant-signal case is trivial and excluded only from the defining ratio.

## Proof
**Reduction.** The pointwise inequality \(|\,|z|-|w|\,|\leq|z-w|\) implies \(V_2(|f|)\leq V_2(f)\). Since \(\mathcal M_n f=\mathcal M_n|f|\), the supremum is attained within nonnegative real signals. For nonnegative signals \(h\) and constants \(c\geq0\), \(\mathcal M_n(h+c)=\mathcal M_nh+c\). Positive rescaling commutes with \(\mathcal M_n\). We may therefore normalize the minimum to zero and the maximum to one; rotations and reflections preserve the ratio.

**Three sites.** Sort the values cyclically as \((u+v,v,0)\), where \(u,v\geq0\). Because the three-cycle is a triangle, every cyclic permutation is equivalent. The maximal values are
\[
\left(u+v,\frac{u+2v}{2},\max\left\{\frac{u+v}{2},\frac{u+2v}{3}\right\}\right).
\]
The original energy is \(V_2(f)^2=2(u^2+uv+v^2)\). If \(u\geq v\), a direct expansion gives \(V_2(\mathcal M_3 f)^2=V_2(f)^2/4\). If \(v\geq u\), the exact deficit is
\[
\frac14V_2(f)^2-V_2(\mathcal M_3 f)^2=\frac{(v-u)(4u+5v)}{18}\geq0.
\]
A nonzero choice with \(u\geq v\) gives equality.

**Four sites and exact continuous certificate.** Normalize a maximizing vertex to index zero and a minimizing vertex to either index one (adjacent case) or index two (opposite case). Write the remaining entries as independent \(x,y\in[0,1]\). Each of the four maximal values is the maximum of finitely many rational affine expressions in \(x,y\), corresponding to all arcs through that vertex. Form the deficit
\[
D(x,y)=\frac{7+\sqrt{13}}{36}V_2(f)^2-V_2(\mathcal M_4f)^2.
\]
Intersecting the affine half-planes determining every active averaging expression partitions the two unit squares into six and seven positive-area convex rational polygons, respectively. Zero-area boundaries are covered by continuity. On each polygon, \(D\) is an explicit quadratic polynomial with coefficients in \(\mathbb Q(\sqrt{13})\). An exact minimum of a quadratic on a compact convex polygon must occur at a vertex, at an edge stationary point, or at an interior stationary point with positive-definite Hessian. The accompanying standalone program `cycle_interval_maximal_certificate.py` generates these half-planes, clips polygons using exact rational arithmetic, constructs each quadratic, and evaluates every such candidate in exact \(\mathbb Q(\sqrt{13})\), including exact sign comparisons. The rational polygon areas sum to one in each case, so no continuous inputs are omitted. The global exact minima of \(D\) are
\[
\min_{\mathrm{adjacent}}D=-\frac1{12}+\frac{5\sqrt{13}}{156}>0,
\qquad \min_{\mathrm{opposite}}D=0.
\]
Thus the claimed four-cycle inequality holds for all normalized values and hence for every signal, not merely for a finite sample.

**Sharpness at four sites.** For \(t=(5-\sqrt{13})/6\), consider \(f=(1,t,0,t)\). Direct evaluation of all permitted arcs gives
\[
\mathcal M_4f=\left(1,\frac{1+t}{2},\frac{1+t}{3},\frac{1+t}{2}\right).
\]
Consequently
\[
V_2(f)^2=2\big((1-t)^2+t^2\big),\qquad
V_2(\mathcal M_4f)^2=2\left(\frac{(1-t)^2}{4}+\frac{(1+t)^2}{36}\right),
\]
and their ratio is exactly \((7+\sqrt{13})/36\). This proves sharpness.

## Verification
From the supplied standalone file, run `python3 cycle_interval_maximal_certificate.py`. It requires only Python's standard library; no floating-point calculations, optimization packages, external files or network access are used. It verifies the exhaustive six/seven polygon counts, area conservation, exact algebraic minimum on each polygon, positivity, and the sharp witness. A separate integer-grid consistency test for the three-cycle is auxiliary; the analytic three-cycle argument above, rather than the grid, proves the infinite statement. The coefficient \(\sqrt{13}\) is treated as an exact quadratic algebraic number throughout.

## Relationship to prior work
Liao, Madrid and Palsson (2026) prove sharp derivative inequalities for the *real-line* uncentered maximal operator, not finite periodic cyclic-arc second variation [1]. González-Riquelme, Kovač and Madrid (2026) study a *centered graph-ball* operator, including the four-cycle only for *first variation*; its Section 3.1 is not the present uncentered second-variation optimization [2]. González-Riquelme and Madrid (2022) likewise treat the centered graph-ball definition [3]. Liao et al. (2026) treat discrete uncentered maximal derivatives on the infinite integer line, with sharp results for characteristic functions, not the present finite cyclic arbitrary-amplitude classification [4]. These distinctions are definitional and in exponent, not merely terminological.

## Limitations
No result is claimed for cycles with five or more vertices or for other exponents. The exact four-cycle upper bound is computer-assisted through a self-contained *exhaustive algebraic* certificate; its completeness relies on the specified polygon clipping and quadratic minimization rules, which are fully inspectable in the embedded source. Results in unindexed or inaccessible older literature could overlap; absence of a database match alone does not establish novelty. No independent mathematical audit is asserted.

## References
[1] S.-Y. Liao, J. Madrid, E. A. Palsson, *Sharp derivative inequalities for uncentered maximal functions*, arXiv:2610.39178v1 (first public 2026-10-29), https://arxiv.org/html/2610.39178v1.

[2] C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (2026), https://arxiv.org/html/2603.12462v1.

[3] C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, J. Math. Anal. Appl. 506 (2022), article 125647, https://doi.org/10.1016/j.jmaa.2021.125647.

[4] S.-Y. Liao, J. Madrid, E. A. Palsson, J. Weigt, *Sharp higher order regularity of discrete maximal functions*, arXiv:2607.10753 (2026), https://arxiv.org/abs/2607.10753.

