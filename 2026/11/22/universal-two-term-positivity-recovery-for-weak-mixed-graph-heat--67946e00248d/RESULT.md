# Universal two-term positivity recovery for weak mixed graph heat on diameter-two networks

## Finding
Let \(G=(V,E,w)\) be any finite, connected, undirected graph with strictly positive symmetric edge conductances and support-graph diameter exactly two. Let \(L=D-W\) be its unnormalized weighted combinatorial Laplacian and
\[
S_\varepsilon(t)=\exp\bigl(-t(L+\varepsilon L^2)\bigr),\qquad t\ge0,\quad\varepsilon>0.
\]
There exists \(\varepsilon_G>0\) such that, for every \(0<\varepsilon<\varepsilon_G\), each nonedge \(\{i,j\}\) has exactly one positive transition-kernel zero \(t_{ij}(\varepsilon)\). Its matrix entry is negative for \(0<t<t_{ij}(\varepsilon)\), vanishes at that root, and is positive afterward. All diagonal and adjacent-vertex entries are strictly positive for every \(t>0\).

Write \(B_{ij}=(L^2)_{ij}\) and \(C_{ij}=(L^3)_{ij}\). Every nonedge satisfies \(B_{ij}=\sum_{k:\,i\sim k\sim j}w_{ik}w_{kj}>0\). Uniformly over the finitely many nonedges,
\[
\boxed{t_{ij}(\varepsilon)=2\varepsilon-\frac83\frac{C_{ij}}{B_{ij}}\varepsilon^2+O_G(\varepsilon^3).}
\]
Consequently, defining \(T_G(\varepsilon)=\max_{\{i,j\}\notin E}t_{ij}(\varepsilon)\), the **entire** entrywise-nonnegative time set and the sharp recovery law are
\[
\boxed{\{t\ge0:S_\varepsilon(t)\ge0\text{ entrywise}\}
=\{0\}\cup[T_G(\varepsilon),\infty),}
\]
\[
\boxed{T_G(\varepsilon)=2\varepsilon-\frac83\varepsilon^2
\min_{\{i,j\}\notin E}\frac{(L^3)_{ij}}{(L^2)_{ij}}+O_G(\varepsilon^3).}
\]
The leading recovery factor \(2\) is universal across all such weighted graphs, whereas the first graph-dependent correction is a local three-step Laplacian invariant. In particular, the nonedges having the smallest ratio in the displayed minimum determine the latest-recovery class to second order.

## Assumptions and scope
The graph is finite, undirected, loopless and connected. A positive conductance \(w_{ij}=w_{ji}\) exists precisely on an edge, and \(L_{ij}=-w_{ij}\) for distinct adjacent vertices. The **unweighted support graph** has diameter exactly two, so at least one nonedge exists and every nonedge has a common neighbor. Counting measure and the unnormalized graph Laplacian are used. The matrix exponential has its usual real symmetric spectral meaning, and \(\varepsilon_G\) depends on the *fixed graph and conductances*. No uniform-in-size or uniform-in-weight assertion is made. The time \(t=0\) is nonnegative because the exponential is the identity, but its nonedge entries vanish and are immediately negative at positive times.

## Proof
**1. The nonedge's critical scale.** Fix a nonedge \(i,j\), so \(L_{ij}=0\). Since all length-two routes use positive conductances,
\[
B_{ij}=(L^2)_{ij}=\sum_{k\in V}L_{ik}L_{kj}
=\sum_{k:\,i\sim k\sim j}w_{ik}w_{kj}>0.
\]
The exponential is jointly analytic near \((t,\varepsilon)=(0,0)\). Put \(t=\varepsilon u\). Its nonedge entry has the factorization
\[
S_\varepsilon(\varepsilon u)_{ij}
=\varepsilon^2u\left[B_{ij}\left(\frac u2-1\right)
+\varepsilon C_{ij}\left(u-\frac{u^2}{6}\right)
+\varepsilon^2R_{ij}(u,\varepsilon)\right],\tag{1}
\]
where \(R_{ij}\) and its first \(u\)-derivative are bounded uniformly for \(0\le u\le3\) and sufficiently small \(\varepsilon\). To confirm the coefficient, expand the exponential in powers of \(t\): the terms containing \(L^2\) are \(-\varepsilon tL^2+t^2L^2/2\); those containing \(L^3\) are \(\varepsilon t^2L^3-t^3L^3/6\). Terms omitted from (1) contain an additional power of \(\varepsilon\) after dividing by \(\varepsilon^2u\). The factorization extends analytically through \(u=0\).

The bracket in (1) converges in \(C^1([0,3])\) to \(B_{ij}(u/2-1)\). Its derivative is therefore strictly positive throughout \([0,3]\) for sufficiently small positive \(\varepsilon\); its values at \(u=0\) and \(u=3\) have opposite signs. It has exactly one root \(u_{ij}(\varepsilon)\) in \((0,3)\), with the indicated negative-to-positive sign change. By the analytic implicit-function theorem, \(u_{ij}(0)=2\), and differentiating (1)'s bracket gives
\[
\frac{B_{ij}}2u_{ij}'(0)
+ C_{ij}\left(2-\frac46\right)=0,
\qquad u_{ij}'(0)=-\frac{8C_{ij}}{3B_{ij}}.
\]
Thus the claimed two-term expansion holds for \(t_{ij}(\varepsilon)=\varepsilon u_{ij}(\varepsilon)\).

**2. No second sign crossing at intermediate times.** For some graph-dependent \(t_0>0\), uniformly for sufficiently small \(0<\varepsilon\le1\) and \(0<t\le t_0\), Taylor's formula gives
\[
S_\varepsilon(t)_{ij}=B_{ij}\left(\frac{t^2}{2}-\varepsilon t\right)
+O_G(t^3+\varepsilon t^2+\varepsilon^2t).\tag{2}
\]
For \(3\varepsilon\le t\le t_0\), the displayed leading term is at least \(B_{ij}t^2/6\). The remainder is bounded by a graph-dependent constant times \(t^2(t_0+\varepsilon+\varepsilon^2/t)\). Because \(\varepsilon\le t/3\), it is at most a fixed multiple of \(t^2(t_0+\varepsilon)\). Take \(t_0\) and then \(\varepsilon\) sufficiently small to make its absolute value less than \(B_{ij}t^2/12\). Hence the nonedge entry stays strictly positive throughout this intermediate region.

**3. Positivity for all later times.** The ordinary weighted graph heat matrix \(P(t)=e^{-tL}\) is strictly positive entrywise for every \(t>0\): the Metzler generator \(-L\) is irreducible, or this follows directly from the positive-weight walk expansion after adding a sufficiently large scalar multiple of the identity. Since the graph is finite and \(P(t)\to|V|^{-1}J\) as \(t\to\infty\),
\[
\inf_{t\ge t_0}\min_{i,j}P(t)_{ij}>0.
\]
On each positive Laplacian eigenspace, the mixed and ordinary multipliers differ by
\[
\left|e^{-t(\lambda+\varepsilon\lambda^2)}-e^{-t\lambda}\right|
\le\varepsilon t\lambda^2e^{-t\lambda}
\le\frac{\varepsilon\lambda}{e}\qquad(t\ge0).
\]
The zero eigenvalue multipliers coincide. Because the spectrum is finite, this bounds \(\sup_{t\ge0}\|S_\varepsilon(t)-P(t)\|\) by \(O_G(\varepsilon)\) in any matrix norm. Taking \(\varepsilon\) sufficiently small therefore makes all entries of \(S_\varepsilon(t)\) strictly positive for all \(t\ge t_0\).

**4. The remaining entry types and the global endpoint.** For distinct adjacent vertices, \(-L_{ij}=w_{ij}>0\), and
\[
S_\varepsilon(t)_{ij}=t w_{ij}+O_G(t^2+\varepsilon t)
\]
uniformly at small positive \(t\), so these entries are positive for \(0<t\le t_0\) after decreasing \(t_0\) and \(\varepsilon_G\), and Step 3 covers later times. Every diagonal entry is strictly positive at all finite \(t\ge0\), since \(S_\varepsilon(t)\) is a real symmetric positive-definite matrix. Finiteness of the edge and nonedge sets permits a single \(\varepsilon_G>0\) for all these assertions.

Every nonedge is negative for positive times below its root, and positive above. Thus all entries are nonnegative exactly at \(t=0\) and from the largest nonedge root onward. Finally, the maximum of finitely many expansions
\(2\varepsilon-\frac83\varepsilon^2(C_{ij}/B_{ij})+O_G(\varepsilon^3)\)
is the expansion with the smallest ratio, proving the last formula. No uniqueness of the *winning nonedge* is required or asserted.

**5. A nontrivial local-selection example.** For the unweighted six-vertex graph with edges \(01,04,05,12,23,34,35\) (each digit denotes a vertex), every nonedge has a common neighbor. Directly multiplying its exact integer Laplacian gives the ratios \((L^3)_{ij}/(L^2)_{ij}\), ordered by nonedge \(02,03,13,14,15,24,25,45\), as
\[
5,\quad\frac{15}{2},\quad5,\quad6,\quad6,\quad6,\quad6,\quad7.
\]
Thus the two nonedges \(02\) and \(13\), not the other six, control the first graph-dependent recovery correction, and
\[
T_G(\varepsilon)=2\varepsilon-\frac{40}{3}\varepsilon^2+O_G(\varepsilon^3).
\]
This graph is not complete multipartite, so this example is not a parameter substitution in the known exact complete-multipartite formulas.

## Verification
The companion `artifacts/check_diameter2.py` draws a fixed-seed collection of **112** diameter-two weighted graph examples, constructs their full conductance Laplacians, and computes \(\exp[-t(L+\varepsilon L^2)]\) independently with a matrix-exponential routine. It probes nonedge root signs, the two-term expansion, edgewise row sums and sign samples. Execution passed **336** graph–parameter cases and **1,584** nonedge root comparisons, plus star-graph spot checks. Dependencies: Python 3, NumPy and SciPy; reproduce with `python artifacts/check_diameter2.py`. Numerical checks test finite samples only. All quantified, all-time and all-graph statements are supplied by the analytic proof above, not inferred from finite sampling.

## Relationship to prior work
Daners, Glück and Kennedy [1] give general spectral and order-theoretic frameworks for eventual positivity, not the universal weak-coupling recovery constant and three-step correction here. Gregorio and Mugnolo [2] analyze *pure* discrete bi-Laplacian heat and eventual positivity; this theorem instead treats a positive first-order generator perturbed by a small fourth-order term, for arbitrary positive edge conductances on support-diameter-two graphs. Published exact formulas [3,4] for the pure \(e^{-tL^2}\) kernel on complete multipartite and unbalanced bipartite graphs do not calculate this perturbative threshold. A published general fractional-power phase diagram [5] handles \(e^{-tL^\alpha}\) on complete multipartite graphs, not the mixed generator. These distinctions concern the statements' actual implications, not just their titles. The classical star and four-site path mixed-generator special cases are not claimed anew here. A historical exact calculation with a different graph-matrix formulation could still contain the same second-order law.

## Limitations
The result is **perturbative for each fixed finite weighted graph**. It does not provide an exact finite-\(\varepsilon\) global recovery formula, a uniform \(\varepsilon_G\) over graph families, or a general statement for support diameter three or larger (where higher-distance kernel terms compete). When several nonedges tie in the second-order invariant, no claim is made about which one dominates at third order. Independent mathematical audit and comprehensive historical-priority certification are not asserted.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first posted 2015-11-17, https://arxiv.org/abs/1511.05294 .

[2] G. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, first posted 2017-12-20, https://arxiv.org/abs/1712.07370 .

[3] *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f/RESULT.md .

[4] *Two timescales of transient amplification and positivity recovery on unbalanced bipartite graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-two-timescales-of-transient-amplification-and-positivity-recover--61512629ac2e/RESULT.md .

[5] *A sharp positivity transition for fractional graph heat on complete multipartite networks*, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1/RESULT.md .
