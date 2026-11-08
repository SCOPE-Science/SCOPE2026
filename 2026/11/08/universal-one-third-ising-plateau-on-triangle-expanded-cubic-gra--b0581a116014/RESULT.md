# Universal one-third Ising plateau on triangle-expanded cubic graphs and the truncated tetrahedral critical census

## Finding
Let \(G=(V,E)\) be a finite simple cubic graph with a perfect matching and \(|V|=n\) (necessarily even). Its **triangle expansion** \(T(G)\) has a spin \(s_{u,v}\in\{\pm1\}\) for each directed incidence \((u,v)\) of an undirected edge \(uv\in E\). For each \(u\), the three incidence spins form a triangle; each \(uv\in E\) adds the edge between \(s_{u,v}\) and \(s_{v,u}\). The Hamiltonian is
\[
H(s)=J\sum_{u\in V}\sum_{\{v,w\}\subset N(u)}s_{u,v}s_{u,w}
+K\sum_{uv\in E}s_{u,v}s_{v,u}-h\sum_{(u,v)}s_{u,v},
\]
with \(J,K>0\), \(h\in\mathbb R\). The exact ground energy is
\[
E_0(h)=\begin{cases}
-nJ-\frac{3n}{2}K,&0\le |h|\le K,\\
-nJ-\frac n2K-n|h|,&K\le|h|\le K+2J,\\
3nJ+\frac{3n}{2}K-3n|h|,&|h|\ge K+2J.
\end{cases}
\]
For positive field strictly between the two transitions, all ground states have magnetization \(M=n\), i.e. exactly one third of the saturation value \(3n\). The three open positive-field regimes have respectively magnetizations \(0,n,3n\). Negative fields follow by global spin reversal.

**Complete structural classification.** For \(h=0\) and for \(0<h<K\), ground configurations correspond bijectively to orientations of the edges of \(G\) in which every vertex has both positive indegree and positive outdegree: assign \(s_{u,v}=-1\) precisely when edge \(uv\) points outward from \(u\). For \(K<h<K+2J\), ground configurations correspond bijectively to choices of one incident edge at every vertex, with no edge chosen by both ends; set precisely those chosen incidence spins negative. At \(h=K\), a configuration minimizes the energy exactly when every expanded triangle is nonmonochromatic and no opposite pair \((s_{u,v},s_{v,u})\) consists of two negative spins. At \(h=K+2J\), a configuration is a minimizer exactly when its set of negative incidence spins is independent in \(T(G)\). For \(h>K+2J\), the only minimizer is the all-positive configuration.

For the truncated tetrahedron \(T(K_4)\) (12 spins, 12 triangle bonds and six external bonds), its full ground-state counts at nonnegative field are

| Field range | Ground magnetization(s) | Number of states |
|---|---|---:|
| \(0\le h<K\) | \(0\) | 24 |
| \(h=K\) | \(0,2,4\) | 114 |
| \(K<h<K+2J\) | \(4\) | 30 |
| \(h=K+2J\) | \(4,6,8,10,12\) | 163 |
| \(h>K+2J\) | \(12\) | 1 |

At \(h=K\), the multiplicities of magnetizations \(0,2,4\) are \(24,60,30\). At \(h=K+2J\), the polynomial counting negative spins is \(1+12z+48z^2+72z^3+30z^4\). Under one-spin flips that remain within the ground manifold, each critical-state graph is connected: the lower-field graph has 114 vertices and 216 edges; the upper-field graph has 163 vertices and 444 edges.

## Assumptions and scope
Every assertion concerns **classical** Ising spins \(\pm1\), a finite simple 3-regular base graph possessing a perfect matching, positive triangle and external-edge antiferromagnetic couplings \(J,K\), and a real homogeneous longitudinal field \(h\). Edges of the base graph are not spin sites; its directed incidences are. The graph need not be planar, connected, or bipartite. The theorem makes no claim for noncubic or matchingless bases, nonuniform couplings within an edge orbit, transverse fields, or finite-temperature effects. All magnetizations are sums of the \(3n\) spins, not spin-half units. At zero or critical field, ground-state multiplicities are part of the statement, not obtained by taking either one-sided limit.

## Proof
**Step 1: an attained zero-field lower bound.** On a triangle of three signs, the pair-product sum is at least \(-1\), with equality precisely when the signs are not all identical. Across an external edge, the sign product is at least \(-1\). There are \(n\) triangles and \(3n/2\) external edges, so at \(h=0\)
\[
H(s)\ge -nJ-\frac{3n}{2}K.
\]
To attain both local bounds, remove a perfect matching from \(G\); the remaining spanning 2-regular subgraph is a disjoint union of cycles. Orient every cycle cyclically, then orient the matching edges arbitrarily. At each vertex there is at least one incoming and one outgoing edge. Set \(s_{u,v}=-1\) for an outward edge and \(+1\) for an inward one. Every triangle is nonmonochromatic, and the two incidence spins across every original edge are opposite, proving attainment. Conversely, equality in each positively weighted local term forces precisely those two conditions. In particular each original edge contributes one negative spin, giving total magnetization zero. This proves the claimed orientation classification.

**Step 2: a sharp lower bound at \(h=K\).** Split the field contribution among the external links, using one field unit \(K\) per incidence spin. For signs \(a,b\in\{\pm1\}\),
\[
 ab-a-b=\begin{cases}-1,&(a,b)\ne(-1,-1),\\3,&(a,b)=(-1,-1).\end{cases}
\]
Therefore the contribution of each external link \(K(ab-a-b)\) is at least \(-K\), while each triangle term is at least \(-J\). Hence \(H_K\ge-nJ-3nK/2\), attained by the zero-field states. Equality holds exactly when each triangle is nonmonochromatic and no external edge has both ends negative. This proves the critical-state classification at \(h=K\).

**Step 3: a sharp lower bound at \(h=K+2J\).** Allocate a field term \(-K(a+b)\) to each external edge and \(-2J(a+b+c)\) to each triangle. For a triangle with \(q\) negative spins, its rescaled local energy is
\[
(ab+bc+ca)-2(a+b+c)=\begin{cases}-3,&q=0,1,\\1,&q=2,\\9,&q=3.\end{cases}
\]
The corresponding external edge reaches its lower bound \(-K\) exactly unless both its spins are negative. Thus the total at \(K+2J\) is at least \(-3nJ-3nK/2\), attained by the all-positive state, with equality **exactly** when the negatives form an independent set in \(T(G)\). In particular this establishes all upper-critical configurations, including the empty independent set.

**Step 4: interpolate without losing equality conditions.** Each of \(H_h\) and the three displayed lower bounds is affine in \(h\ge0\). For \(0<h<K\), \(H_h\) is a strict convex combination of \(H_0\) and \(H_K\); equality requires simultaneous equality at both endpoints. All zero-field minimizers already satisfy the \(K\)-endpoint conditions, so exactly the source/sink-free orientations survive. For \(K<h<K+2J\), strict convexity likewise requires satisfying both boundary classifications. One negative spin per triangle is the only possibility: the lower boundary demands one or two negatives, and the upper demands at most one, with no opposite external double-negatives. Such configurations exist by orienting the cycles in the complement of a perfect matching and choosing, at each vertex, its outgoing cycle incidence as the unique negative. There can be no doubly chosen original edge. Their magnetization is \(n\). For \(h>K+2J\), moving away from the unique maximally magnetized all-positive state increases the energy by a strictly positive field cost per negative spin, whereas the boundary inequality already gives its optimality. Thus it remains the unique ground state. The formula for the three intervals follows by substituting their magnetizations. Spin inversion proves the case \(h<0\).

**Step 5: exact truncated-tetrahedral census.** Let \(G=K_4\). At \(h=0\), a source/sink-free orientation of \(K_4\) is a tournament where each vertex has outdegree one or two. There are 24 such labelled tournaments. At \(h=K\), the negative-port count \(q\) can be \(4,5,6\), with exact counts \(30,60,24\). For \(q=4\), the one-outgoing-port choices have \(3^4=81\) possibilities; inclusion-exclusion removes the reciprocal choices on each of six edges (nine completions per edge) and restores the three pairs of disjoint reciprocal edges, giving \(81-6\cdot9+3=30\). For \(q=5\), exactly one triangle has two negative ports; choose its vertex in four ways and its unique positive port in three ways. Of the 27 assignments choosing one negative port on each of the remaining three triangles, exactly five obey the no-double-negative constraint, giving \(4\cdot3\cdot5=60\). For \(q=6\), every external edge is oppositely signed, and each triangle has one or two negatives, recovering the 24 tournaments. The upper-critical counts for \(q=0,1,2,3,4\) are \(1,12,48,72,30\), obtained by the independent-set condition and verified by the exhaustive exact enumerator described below. The \(30\) top-degree independent sets are precisely the strict-plateau choices. These counts establish all claimed multiplicities for the finite example.

## Verification
The accompanying `verify.py` is a standalone Python-standard-library exact checker. It constructs the directed-incidence expansion for three distinct cubic bases (\(K_4\), \(K_{3,3}\), and the triangular prism), enumerates all \(2^{3n}\) configurations by Gray-code spin flips, and compares the exact integer Hamiltonian minimum to the theorem at several independent positive coupling pairs and each boundary and interior phase. It separately reconstructs a 12-site adjacency labeling of the truncated tetrahedron, locates its triangles from three-cycles, and exhaustively checks all 4096 spin assignments and both critical one-spin-flip transition graphs. The checks return `UNIVERSAL_EXAMPLE_OK` for all three bases, `TETRAHEDRON_EXACT_OK`, and `ALL_EXACT_CHECKS_OK`. Finite enumeration corroborates, but does **not** substitute for, Steps 1–4 proving the theorem for all permitted base graphs. No finite numerical tolerance or unverified external calculation is needed.

## Relationship to prior work
Coffey and Trugman (1992) study the **same truncated-tetrahedral geometry and inequivalent triangle/intertriangle bonds** but principally classical vector spins and the quantum \(S=1/2\) Heisenberg model; their field behavior is not this discrete Ising, all-base exact classification. Yu (2015) studies the zero-field Ising antiferromagnet on the 11 infinite Archimedean lattices, including the star (triangle-dodecagon) lattice, and establishes previously known frustrated ground-state phenomena. The **zero-field geometric frustration and local triangle constraint are not claimed as novel**. The new claim is the universal finite-cubic perfect-matching field theorem, including simultaneous exact endpoints and ground-state descriptions, together with the explicitly enumerated two critical-state layers of the truncated tetrahedron. The 2015 regular-Ising-polyhedra study by Strečka and collaborators addresses Platonic solids, not this particular truncated polyhedron or the universal triangle-expanded cubic family. In the examined material no prior implication of the complete claim was identified; an unindexed equivalent graph-theoretic or statistical-mechanics treatment remains possible.

## Limitations
A successful self-review is **not an independent audit or proof of historical priority**. Published formulations may use Fisher decoration, the triangle-dodecagon/star lattice, frustrated-edge budgets, tournament orientations, or graph independence polynomials rather than the present terminology; these equivalences were explicitly considered when searching. The finite census uses labelled spins and no symmetry quotient, so its multiplicities are not counts of geometric or spin-flip equivalence classes. The theorem does not determine finite-temperature partition functions or dynamics. The infinite-family claim is proved analytically, while the critical one-spin-flip connectivity claim is specific to the 12-spin truncated tetrahedron and is checked by finite exhaustive computation.

## References
1. D. Coffey and S. A. Trugman, *Correlations for the S=1/2 Antiferromagnet on a Truncated Tetrahedron* (1992), first public 1992-06-26, https://arxiv.org/abs/cond-mat/9206011 .
2. U. Yu, *Ising antiferromagnet on the Archimedean lattices*, Physical Review E **91**, 062121 (published 2015-06-17), https://doi.org/10.1103/PhysRevE.91.062121 ; open manuscript https://arxiv.org/pdf/1606.08191 .
3. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra* (first public 2015-02-16), https://arxiv.org/abs/1502.04449 .
