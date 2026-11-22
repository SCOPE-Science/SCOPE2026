# Exact intrinsic inballs and a mod-four center-locus transition for cycle edge-midpoint polytopes

## Finding
Let \(n\ge3\). For standard coordinate vectors \(e_0,\ldots,e_{n-1}\) and the all-one vector \(\mathbf1\), form the regular simplex of circumradius one with vertices
\[
u_i=\sqrt{\frac n{n-1}}\left(e_i-\frac1n\mathbf1\right)\quad(i\in\mathbb Z/n\mathbb Z).
\]
Retain only the midpoints of the \(n\) edges of a fixed Hamiltonian cycle:
\[
v_i=\tfrac12(u_i+u_{i+1}),\qquad P_n=\operatorname{conv}\{v_0,\ldots,v_{n-1}\}.
\]
All balls, facet distances, and dimensions below are intrinsic to the affine span of \(P_n\). The centroid \(0\) is always a maximum-radius inscribed-ball center. Its radius is
\[
\boxed{r_n=\begin{cases}
\displaystyle\frac{1}{(n-1)\sqrt{n+1}},&n\text{ odd},\\[5pt]
\displaystyle\frac1{\sqrt{(n-1)(m^2-1-\delta_m)}},&n=2m,\quad
\delta_m=\begin{cases}1,&m\text{ even},\\0,&m\text{ odd}.
\end{cases}
\end{cases}}
\]
For odd \(n\), all \(n\) facets are tangent to this ball and \(0\) is the **unique** maximal-ball center.

For even \(n=2m\), there are exactly \(m^2\) facets. Each facet omits one even-index and one odd-index midpoint. If those indices have minimum cyclic separation \(d\) (necessarily odd), its supporting plane is at distance
\[
\boxed{D_{n,d}=\frac1{\sqrt{(n-1)[d(n-d)-1]}}.}
\]
For every odd \(d<n/2\), this shell contains \(2m\) facets; if \(m\) is odd, the middle shell at \(d=m\) contains \(m\) facets. Thus the centered maximal ball contacts exactly \(n\) facets when \(4\mid n\), but exactly \(n/2\) facets when \(n\equiv2\pmod4\). **The complete set of maximum-radius centers is a singleton when \(4\mid n\), and has affine dimension \(n/2-1\) when \(n\equiv2\pmod4\).**

The latter set also admits an explicit difference-inequality description. When \(n=2m\) with \(m\ge3\) odd, put \(i_a=2a\) for \(a=0,\ldots,m-1\), and let \(d_{ab}\) be the minimum cyclic distance between \(2a\) and \(2b+m\), reduced modulo \(2m\). Then all maximum-ball centers, without repetition, are
\[
c(t)=\sum_{a=0}^{m-1}t_a(v_{2a}-v_{2a+m}),\qquad \sum_at_a=0,
\]
where for every ordered pair \(a,b\),
\[
\boxed{t_b-t_a\le\frac1m\left(1-\sqrt{\frac{d_{ab}(2m-d_{ab})-1}{m^2-1}}\right).}
\]
For \(a=b\), the inequality is equality; for \(a\ne b\), it is strict at the origin of parameter space, so the center set really has dimension \(m-1\). In particular, near-equality does not force centers toward the centroid in the \(n\equiv2\pmod4\) family. The inradii have the contrasting asymptotics \(r_n\sim n^{-3/2}\) along odd orders and \(r_n\sim2n^{-3/2}\) along even orders.

## Assumptions and scope
The metric is the ordinary Euclidean metric restricted to \(E_n=\operatorname{aff}(P_n)\), with the unit-circumradius simplex normalization above; it is *not* a combinatorial, lattice, or arbitrary affine-normalization inradius. For odd \(n\), \(E_n=\mathbf1^\perp\) has dimension \(n-1\). For even \(n\), \(E_n=\mathbf1^\perp\cap\eta^\perp\), with \(\eta_k=(-1)^k\), and has dimension \(n-2\). All indices are cyclic. A facet supporting hyperplane has a unique normal in \(E_n\) with the prescribed nonzero support level \(1\). For a full-dimensional convex polytope in \(E_n\), a radius-\(r\) ball centered at \(c\) is contained in the polytope exactly when the oriented facet inequalities \(\langle w,c\rangle+r\|w\|\le1\) hold for every normalized facet normal \(w\).

## Proof
**1. Faces and affine dimension.** Define the incidence matrix \(B=I+S\), where \((Sx)_k=x_{k+1}\) with cyclic indices. The midpoint columns differ by a constant translation and a positive scalar from the graph-edge incidence vectors of the cycle \(C_n\). If \(n\) is odd, \(B\) is invertible and its \(n\) columns are affinely independent: \(P_n\) is an \((n-1)\)-simplex. If \(n=2m\), the kernel of \(B\) is spanned by \(\eta\), and both even- and odd-index midpoint families are affinely independent simplices whose only affine dependence is \(\sum_{k\text{ even}}v_k=\sum_{k\text{ odd}}v_k=0\). Thus \(P_n\) is the free sum of two \((m-1)\)-simplices; every facet consists of all but one vertex from each parity class. The affine dimensions and combinatorial types are also stated in Tran--Ziegler (2014, Example 3); they are not claimed as new.

**2. Facet-normal equations.** Write \(\alpha=\sqrt{n/(n-1)}\). For \(w\in E_n\), the identity
\[
\langle w,v_k\rangle=\frac\alpha2(w_k+w_{k+1})
\]
reduces normalized facet normals to cyclic recurrences. Set \(z=(\alpha/2)w\), so \((I+S)z=s\), and \(\|w\|^2=4(n-1)\|z\|^2/n\). For odd \(n\), the facet omitting index \(i\) has \(s_i=1-n\) and \(s_k=1\) otherwise. Solving the alternating recurrence gives \((n+1)/2\) entries in \(z\) equal to \(-(n-1)/2\) and \((n-1)/2\) entries equal to \((n+1)/2\). Therefore
\[
\|z\|^2=\frac{n(n^2-1)}4,\qquad \|w\|^2=(n-1)^2(n+1).
\]
All odd-order facet planes are equidistant from \(0\), giving the first radius formula.

**3. Even-order facet distance spectrum.** Let \(n=2m\). For the facet omitting the even index \(i\) and odd index \(j\), the required support values are \(1\) elsewhere and \(1-m\) at each omitted index. With \(D=\operatorname{diag}((-1)^k)\), this is \(s=\mathbf1-m(e_i+e_j)\), so \(Ds=\eta-m(e_i-e_j)\). Conjugating the cyclic recurrence by \(D\) reduces it to \((I-S)Dz=Ds\). The unique \(z\in E_n\) has
\[
\|z\|^2=(Ds)^\mathsf TL^+(Ds),\quad L=(I-S)(I-S)^\mathsf T=2I-S-S^{-1},
\]
with \(L^+\) the inverse on the zero-sum subspace. Directly, \(L\eta=4\eta\), \(\eta^\mathsf TL^+\eta=n/4\), and \((e_i-e_j)^\mathsf TL^+\eta=1/2\). Also
\[
(e_i-e_j)^\mathsf TL^+(e_i-e_j)=\frac{d(n-d)}n.
\]
For completeness, solve the discrete cycle-Laplacian equation \(L\phi=e_i-e_j\): its increments along the two arcs of lengths \(d\) and \(n-d\) are constant and opposite, with magnitudes \((n-d)/n\) and \(d/n\). The potential drop from \(i\) to \(j\) is therefore \(d(n-d)/n\); no unverified electrical-network formula is required. Combining these identities gives
\[
\|z\|^2=\frac n4-m+\frac{m^2d(n-d)}n,
\qquad \|w\|^2=(n-1)[d(n-d)-1].
\]
This proves the displayed distances and shell multiplicities by counting opposite-parity pairs. The largest normal norm occurs at the odd distance(s) closest to \(m\). If \(m\) is odd, only distance \(m\) is closest and there are \(m\) tangent facets; if \(m\) is even, distances \(m-1,m+1\) are tied and there are \(2m=n\) tangent facets. This yields the two even-order radius branches.

**4. Global inradius.** Every cyclic vertex rotation induces an intrinsic orthogonal symmetry of \(P_n\). If \(c\) is a center of an inscribed radius-\(r\) ball, averaging its images under all \(n\) rotations gives the origin, and the averaged center remains feasible because every fixed-radius center-feasibility region is convex. Thus \(0\) supports a ball of largest possible radius, and the minimum centered facet distance computed above equals the *global* inradius.

**5. Every optimal center.** Let \(T\) denote the set of centered tangent facets and let \(w_F\) be their outward normals. Since \(T\) is rotation-invariant and \(E_n\) has no nonzero vector fixed by all cyclic shifts, \(\sum_{F\in T}w_F=0\). For any center \(c\) of a ball of the optimal radius, every tangent inequality is \(\langle w_F,c\rangle\le0\). Their sum vanishes, so each is necessarily an equality. When \(n\) is odd, the normals of the \(n\) simplex facets span \(E_n\); hence \(c=0\).

When \(n=2m\), express an arbitrary \(c\in E_n\) as \(c=\sum_ka_kv_k\) with \(\sum_ka_k=0\), noting that this representation is unique modulo \(a_k\mapsto a_k+t(-1)^k\). For a facet omitting even \(i\) and odd \(j\), the normal equation gives
\[
\langle w_{ij},c\rangle=-m(a_i+a_j).
\]
Thus tangent equalities form the bipartite graph of missing-index pairs. If \(m\) is odd, this graph is the perfect matching \(j=i+m\), producing an \((m-1)\)-dimensional solution space modulo the alternating kernel. If \(m\) is even, it is the connected even cycle \(j=i+m\pm1\), forcing all even coefficients equal and all odd coefficients their negatives; this is exactly the coefficient kernel, so \(c=0\). Finally, non-tangent inequalities have strict slack at \(c=0\). Hence the local dimension of the feasible center set is exactly the tangent solution dimension; no further equalities arise. Substituting \(a_{2a}=t_a\), \(a_{2a+m}=-t_a\) in every facet inequality and imposing the gauge \(\sum_at_a=0\) yields the displayed *exact global center-locus polytope* for odd \(m\).

## Verification
The standalone file `verify.py` computes all facet-normal squared norms exactly over \(\mathbb Q\) using the cyclic recurrence and checks their closed formulas for every \(3\le n\le26\). It also checks the full list of tangent facets, the largest norm, and the rational ranks of the tangent equalities; 1,022 exact checks pass. In particular it independently tests both congruence classes of even orders and the small cases \(n=3,4,6,8,10\). This finite test is a consistency check; the five all-order proof steps above establish the infinite family and the exact center description. Run with `python3 verify.py` (standard library only).

## Relationship to prior work
Hyunjun Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421 (first posted 2026-11-02), highlights the complete midpoint set of a regular simplex as an extremal Euclidean configuration; its main theorems concern large isosceles sets, not cycle-selected midpoint hulls or intrinsic inscribed balls. T. Tran and G. M. Ziegler, *Extremal Edge Polytopes* (2014), Example 3, already describe precisely the odd-cycle simplex and even-cycle two-simplex free-sum combinatorial types. Those combinatorial facts are used here without novelty claims. A publicly available study titled *Exact Euclidean chord-distance shells of cycle edge polytopes inside the second hypersimplex* computes distances of complete-hypersimplex vertices to the ordinary cycle edge polytope; its full RESULT.md was inspected, and it does not supply intrinsic facet-distance or incenter statements. Prior work on Euclidean inballs of wheel-graph ordinary edge polytopes and cycle symmetric-edge/root polytopes concerns different vertex configurations, and does not imply the metric formula here through abstract affine equivalence. The distinctive assertion is the intrinsic Euclidean facet-distance spectrum, exact global inradius, and congruence-dependent dimension and difference-polytope description of *all* inball centers.

## Limitations
The scale depends on unit *circumradius*, not unit edge length, and the inradius is intrinsic to the lower-dimensional even-order affine hull. Combinatorial affine equivalence alone cannot transport the Euclidean formulas. The result is for Hamiltonian-cycle midpoint selections, not for arbitrary graph selections of simplex-edge midpoints. Primary-literature and searchable-record comparisons cannot exclude every unindexed equivalent theorem; historical priority remains provisional. No independent mathematical validation has been performed.

## References
1. H. Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421v2 (2026), https://arxiv.org/html/2611.05421v2. First version 2026-11-02.
2. T. Tran and G. M. Ziegler, *Extremal Edge Polytopes*, Electronic Journal of Combinatorics 21(2) (2014), P2.57, https://arxiv.org/abs/1307.6708; Example 3.
3. *Exact Euclidean chord-distance shells of cycle edge polytopes inside the second hypersimplex*, published 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-euclidean-chord-distance-shells-of-cycle-edge-polytopes-in--13ab26bd16cc.
4. H. Ohsugi and T. Hibi, *Normal Polytopes Arising from Finite Graphs*, Journal of Algebra 207 (1998), 409–426, https://page.mi.fu-berlin.de/lapinou/lehre/ohsugiHibiGraphs.pdf (general graph-edge-polytope background).
