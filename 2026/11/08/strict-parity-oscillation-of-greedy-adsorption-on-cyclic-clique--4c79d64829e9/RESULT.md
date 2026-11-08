# Strict parity oscillation of greedy adsorption on cyclic clique chains

## Finding
For integers \(m,r\ge3\), form \(G_{m,r}\) from the cycle with vertices \(v_0,\ldots,v_{m-1}\) by attaching \(r-2\) distinct private vertices to each edge \(\{v_i,v_{i+1}\}\), making those \(r\) vertices a clique. Let \(\rho_{m,r}\) be the expected fraction of vertices retained by the random-order greedy maximal independent-set algorithm on this \(m(r-1)\)-vertex graph. Put \(\lambda=r-1\), and for integers \(k\ge1\), define
\[
J_k(\lambda)=\int_0^\infty\exp\!\left[-(\lambda k-1)t-\frac2\lambda(1-e^{-\lambda t})\right]dt,
\qquad \rho_r=\frac{1-J_2(\lambda)}\lambda.
\]
Then the exact finite-size law is
\[
\boxed{\rho_{m,r}-\rho_r=\frac{(-1)^{m-1}2^{m-2}}{\lambda\prod_{j=2}^{m-1}(\lambda j-1)}\left(\frac1{\lambda m}-J_m(\lambda)\right).}
\]
The expression in parentheses is **strictly positive**. Consequently \(\rho_{m,r}>\rho_r\) for every odd \(m\ge3\), while \(\rho_{m,r}<\rho_r\) for every even \(m\ge4\). For fixed \(r\), the correction is factorially small, with
\[
\left|\rho_{m,r}-\rho_r\right|\sim\frac{2^{m-2}}{\lambda^3m^2\prod_{j=2}^{m-1}(\lambda j-1)}
\qquad (m\to\infty).
\]
In particular, for triangular blocks \(r=3\),
\[
\rho_3=\frac14+\frac{\sqrt\pi}{8e}\operatorname{erfi}(1)=0.3845198767\ldots,
\]
and the finite-ring expectations strictly alternate above and below this value.

## Assumptions and scope
All graphs are finite, simple and undirected. Indices on the \(m\)-cycle are modulo \(m\). The random-order greedy independent set scans all vertices in a uniformly random permutation and retains a vertex if none of its previously retained neighbours is adjacent. The parameter \(r\) is an integer at least three, and the number \(m\) of cliques is at least three. The infinite-reference constant \(\rho_r\) is defined by the displayed integral, not by a presumed thermodynamic-limit theorem; the exact identity itself proves convergence to it. The limit in the last display fixes \(r\) while \(m\to\infty\).

## Proof
Assign independent rate-one exponential arrival clocks to the vertices. Their ordering is uniform, hence they reproduce the greedy algorithm. Call each \(r\)-clique a site, and index sites by \(i\in\mathbb Z/m\mathbb Z\). A private vertex belongs to one clique, while the backbone vertex \(v_i\) belongs to two consecutive cliques. An accepted private vertex occupies one site, and an accepted backbone vertex occupies two. Two candidate vertices conflict exactly when their site sets overlap. Thus this is random sequential adsorption of monomers at total rate \(a=r-2=\lambda-1\) per site and dimers at rate one per adjacent pair. At the end, every site is occupied: a vacant site would admit its private vertex. If \(D\) is the number of accepted dimers, then \(|I|=m-D\). In particular
\[
\rho_{m,r}=\frac{1-d_m}{\lambda},\qquad d_m=\frac{\mathbb ED}{m}.
\]

For each \(1\le k\le m\), let \(E_k^{(m)}(t)\) be the probability that a specified cyclic interval of \(k\) sites remains empty at time \(t\). Translation invariance gives \(E_k^{(m)}(0)=1\). For \(1\le k<m\), the interval can first lose emptiness due to \(k\) monomer clocks, \(k-1\) internal dimer clocks or either of its two boundary-crossing dimer clocks. This yields
\[
(E_k^{(m)})'=-(\lambda k-1)E_k^{(m)}-2E_{k+1}^{(m)}.
\]
For \(k=m\), all \(m\) monomer groups and all \(m\) dimer clocks must be untouched; hence \(E_m^{(m)}(t)=e^{-\lambda mt}\). All quantities vanish as \(t\to\infty\).

The infinite hierarchy with the same differential equations admits the explicit solution
\[
E_k^\infty(t)=\exp\!\left[-(\lambda k-1)t-\frac2\lambda(1-e^{-\lambda t})\right],\quad k\ge1.
\]
Indeed \(E_k^\infty(0)=1\), \(E_{k+1}^\infty/E_k^\infty=e^{-\lambda t}\), and differentiation checks the equations exactly. Write \(J_k=\int_0^\infty E_k^\infty(t)dt\). Integrating the differential equations gives \(1=(\lambda k-1)J_k+2J_{k+1}\).

Set \(\Delta_k=\int_0^\infty(E_k^{(m)}-E_k^\infty)dt\), for \(1\le k\le m\). The terminal value is \(\Delta_m=(\lambda m)^{-1}-J_m\), and integration of the two matching differential hierarchies yields \((\lambda k-1)\Delta_k+2\Delta_{k+1}=0\), for \(1\le k<m\). In particular
\[
\Delta_2=\frac{(-2)^{m-2}}{\prod_{j=2}^{m-1}(\lambda j-1)}\left(\frac1{\lambda m}-J_m\right).
\]
An individual dimer is accepted precisely when its arrival clock rings while its two sites are empty, so the compensator identity gives \(d_m=\int_0^\infty E_2^{(m)}(t)dt=J_2+\Delta_2\). Substitution into \(\rho_{m,r}=(1-d_m)/\lambda\) proves the exact formula.

To prove the strict sign, differentiate the infinite-hierarchy expression: its instantaneous hazard at index \(m+1\) is \(\lambda(m+1)-1+2e^{-\lambda t}\le\lambda(m+1)+1\). Thus \(J_{m+1}\ge(\lambda(m+1)+1)^{-1}\). For \(\lambda\ge2,m\ge3\), \(\lambda(m-1)>1\), giving \(J_{m+1}>1/(2\lambda m)\). Now \(1=(\lambda m-1)J_m+2J_{m+1}\) implies \(J_m<1/(\lambda m)\). Hence the difference changes sign strictly with the parity of \(m\).

Finally, as \(m\to\infty\) with \(\lambda\) fixed,
\[
\frac1{\lambda m}-J_m=\int_0^\infty e^{-\lambda mt}\left[1-\exp\!\left(t-\frac2\lambda(1-e^{-\lambda t})\right)\right]dt.
\]
The bracket is \(t+O(t^2)\) at zero. The integral's tail beyond any fixed small positive time is exponentially negligible, while standard Laplace localization or dominated convergence after \(u=mt\) yields \((\lambda^2m^2)^{-1}(1+o(1))\). This proves the stated asymptotic. For \(\lambda=2\), substitute \(u=e^{-t}\) to obtain \(J_2=e^{-1}\int_0^1u^2e^{u^2}du=\frac12-\frac{\sqrt\pi}{4e}\operatorname{erfi}(1)\), yielding the triangular case.

## Verification
The accompanying standalone Python script `verify.py` independently reconstructs exact random-order greedy expectations by the first-selected-vertex recurrence on residual graphs. For \(m\in\{3,4,5,6\}\), \(r\in\{3,4,5\}\) with at most 24 vertices, it compares the exact rational expectations against the analytic formula calculated from the absolutely convergent series
\[
J_k(\lambda)=e^{-2/\lambda}\sum_{j\ge0}\frac{(2/\lambda)^j}{j!\,[\lambda(k+j)-1]}.
\]
It also checks the parity signs over additional finite parameter pairs. These finite checks support the implementation; all-size correctness comes from the exact hierarchy and proof, not extrapolation.

## Relationship to prior work
Krivelevich, Mészáros, Michaeli and Shikhelman (first public version, 2019) study limiting random greedy independent-set densities through local limits; this supplies motivation and the common model but does not give this finite-ring parity formula. Pippenger (1989) develops random sequential adsorption on graphs, including locally cyclic models, and Fan and Percus (1991) address asymptotic coverage for lattices and cactuses. The empty-interval technique and infinite-volume density are related to classical adsorption calculations. The claim here is specifically the exact finite cyclic clique-chain correction, its strict alternating sign for every block count, and its factorial asymptotic. Earlier graph-level adsorption formulas could potentially subsume this case; see limitations.

## Limitations
No assertion is made that the general empty-interval method or infinite-line adsorption density is new. The first-order arrival model, identical complete-clique blocks, uniform random order and finite cyclic geometry are essential to the stated exact formula. The asymptotic assumes fixed \(r\). Full-text access to Pippenger (1989) was unavailable for comparison, so historical priority is qualified; the displayed identity has not been independently audited.

## References
1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216v1 (public 2019-07-16), https://arxiv.org/abs/1907.07216.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034.
3. Y. Fan and J. K. Percus, *Asymptotic coverage in random sequential adsorption on a lattice*, Phys. Rev. A 44 (1991), 5099, https://doi.org/10.1103/PhysRevA.44.5099.
