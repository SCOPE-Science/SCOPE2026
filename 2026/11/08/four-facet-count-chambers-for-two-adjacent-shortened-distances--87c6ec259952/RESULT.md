# Four facet-count chambers for two adjacent shortened distances

## Finding
Let \(N\ge4\) and let \(M=\{a,b,c,z_1,\ldots,z_{N-3}\}\). Give \(M\) the metric with \(d(a,b)=r\), \(d(b,c)=s\), and all other distinct-point distances equal to \(1\), where \(0<r,s<1\) and \(r+s\ge1\). Let \(\mathcal F(M)\) be the real Lipschitz-free space over this finite metric, equipped with its Kantorovich--Rubinstein norm. The exact number of facets of its unit ball is

\[
F_N(r,s)=\begin{cases}
2^{N+1}-12,&r\ne s,\ r+s>1,\\
7\cdot2^{N-2}-10,&r=s>1/2,\\
7\cdot2^{N-2}-12,&r\ne s,\ r+s=1,\\
3\cdot2^{N-1}-10,&r=s=1/2.
\end{cases}
\]

These are all possible parameter cases in the stated open-square metric domain. Thus exact equality of the two shortened lengths and exact saturation of the triangle inequality are two distinct, intersecting facet-loss loci. In particular, for \(N=5\) the four counts are respectively \(52,46,44,38\), while the unmodified equilateral metric has \(30\) facets. The answer is independent of the numerical values within each of the four chambers.

## Assumptions and scope
The triangle inequality for \(a,b,c\) is precisely \(r+s\ge1\). The remaining inequalities hold automatically since \(0<r,s<1\) and all other distances equal \(1\). The dual unit ball is the Lipschitz polytope
\[
L(M)=\{f:M\to\mathbb R:f(z_1)=0,\ \lvert f(x)-f(y)\rvert\le d(x,y)\ \text{for all }x,y\in M\}.
\]
Its vertices correspond bijectively by polarity to facets of the unit ball of \(\mathcal F(M)\). Every count is of distinct geometric facets, without identifying opposites.

## Proof
**1. Tight-graph criterion.** At any \(f\in L(M)\), form the undirected graph on \(M\) whose edge \(xy\) is present exactly when \(\lvert f(x)-f(y)\rvert=d(x,y)\). A point \(f\) is a vertex modulo constants if and only if this tight graph is connected. Indeed, connectivity determines all potential differences and hence yields a singleton affine solution. If the graph is disconnected, the potential can be perturbed by independent sufficiently small constants on its components while retaining all strict cross-component inequalities, so the point is not extreme. This argument remains valid when a triangle inequality is an equality.

**2. Outsiders are binary.** Each \(z_j\) is incident only to edges of length \(1\). At a vertex it must have an incident tight edge, since the tight graph is connected. Since every metric distance is at most \(1\), a tight length-\(1\) edge realizes the global minimum and maximum of \(f\). Subtracting the minimum normalizes the entire potential into \([0,1]\), and each outsider must have potential \(0\) or \(1\). If all outsiders equal \(0\), at least one distinguished point must equal \(1\); otherwise no outsider has a tight edge. The case of outsiders all equal \(1\) is symmetric.

**3. Exhaustive distinguished triples away from the two walls.** Assume first \(r>s\) and \(r+s>1\); the case \(r<s\) is obtained by interchanging \(a,c\) and \(r,s\). If outsiders of both binary values occur, their unit tight edges form a connected core. Every distinguished point with value \(0\) or \(1\) connects to that core by a unit edge. Any distinguished point with intermediate value can join only through the two short edges \(ab,bc\). Hence a connected tight graph has either zero, one or two short tight edges. Conversely, every feasible triple of these types with the intermediate points attached to the binary core has connected tight graph.

The complete list of \((f(a),f(b),f(c))\) is as follows. The two configurations with no short tight edge are \((0,0,0)\) and \((1,1,1)\). Those with exactly one short tight edge are
\[
\begin{gathered}
(0,0,s),\ (0,1-s,1),\ (0,s,0),\ (0,r,1),\ (1-r,1,1),\\
(r,0,0),\ (1,1-r,0),\ (1,1-s,1),\ (1,s,0),\ (1,1,1-s).
\end{gathered}
\]
Those with both short edges tight are
\[
(0,r,r-s),\quad(1-r,1,1-s),\quad(r,0,s),\quad(1,1-r,1-r+s).
\]
All \(16\) satisfy the metric inequalities, and the tight edges connect them to the mixed outsider core. Completeness follows by the endpoint-attachment argument above: in the zero-edge case all three distinguished values must be binary; with one edge, the remaining point is binary; with both edges, the three-vertex path must have a binary anchor, and \(r>s\), \(r+s>1\) exclude all other sign choices. This explicitly exhausts the two signs of each short edge and the two available binary anchors. Exactly \(10\) of these triples contain a \(1\), and exactly \(10\) contain a \(0\). The respective subsets are precisely those whose tight graph stays connected when all outsiders are \(0\), or when all are \(1\). Consequently the all-zero outsider assignment contributes \(10\) vertices, the all-one assignment contributes \(10\), and each of the remaining \(2^{N-3}-2\) assignments contributes \(16\). The total is \(20+16(2^{N-3}-2)=2^{N+1}-12\).

**4. Exact counts on the walls.** The admissible polytopes depend continuously on \((r,s)\) because their inequality normals are fixed, the distances remain positive, and their interiors contain the zero potential. Every vertex of a wall polytope is a limit of vertices from adjacent open chambers: maximize any linear functional exposing that vertex uniquely and pass to maximizing vertices under a converging sequence of parameters. Therefore the specialized \(16\)-triple list remains exhaustive, although some configurations coincide, and the connected-tight-graph test determines which specialized candidates remain vertices.

At \(r=s>1/2\), the two distinct pairs \((0,s,0)=(0,r,r-s)\) and \((1,1-r,1-r+s)=(1,1-s,1)\) coalesce. The mixed-outside, all-zero, all-one contributions become \(14,9,9\). Hence \(18+14(2^{N-3}-2)=7\cdot2^{N-2}-10\).

At \(r\ne s\), \(r+s=1\), the coalescing pairs are \((0,1-s,1)=(0,r,1)\) and \((1,1-r,0)=(1,s,0)\). The contributions become \(14,8,8\), giving \(16+14(2^{N-3}-2)=7\cdot2^{N-2}-12\).

At the intersection \(r=s=1/2\) all four pair identifications apply and are independent. The contributions become \(12,7,7\), giving \(14+12(2^{N-3}-2)=3\cdot2^{N-1}-10\). This proves every case.

## Verification
The standalone standard-library Python program `check_facets.py` performs rational tight-graph enumeration for \(9\) length pairs and outsider counts \(1\) through \(6\), covering all four chambers and both asymmetry directions (\(54\) exact tests). Separately, it enumerates all rank-three active halfspace intersections of the four-point Lipschitz polytopes using exact Cramer's-rule determinants, without using the proposed triple templates, and matches the theorem in every tested length regime. A second independent standard-library program, `check5_extra.py`, exhaustively enumerates all rank-four active-constraint intersections for four representative five-point metrics and obtains the four distinct counts \(52,46,44,38\). The first program exits with `ALL_ADJACENT_SHORTENING_FACET_CHECKS_PASSED` on success. These finite calculations are supplementary; the all-\(N\), all-parameter assertion is proved by the classification and wall argument.

## Relationship to prior work
Vershik introduced the fundamental-polytope viewpoint and motivated classification of finite metrics by polytope face structure. Gordon and Petrov give the tight-graph/face framework and an \(f\)-vector formula for generic metrics. The present metrics are highly nongeneric because all but two distances coincide; their theorem does not supply these facet counts. Delucchi, Kühne, and Mühlherr analyze the Wasserstein arrangement and provide low-dimensional enumerations, but do not state this all-dimensional two-parameter facet formula.

A separately established count for independently shortened **disjoint** pairs is inapplicable: the two short edges here meet at \(b\), so the matching hypothesis fails. Another result treats two incident **elongated equal** lengths; its interior count coincides numerically with the equal-shortening stratum, but it does not imply the distinct asymmetric chamber or the triangle-equality boundary. No claim of general priority beyond the checked sources is made.

## Limitations
The result counts facets, not the entire face vector or the complete face lattice. It assumes exactly two adjacent short edges, all remaining distances equal to one, real scalar Lipschitz-free spaces, and at least one outsider point. The parameter faces \(r=1\) or \(s=1\), and metrics with three or more modified distances, are not included. A theoretically equivalent result in literature not indexed by the searches remains possible.

## References
1. A. M. Vershik, *Classification of finite metric spaces and combinatorics of convex polytopes*, arXiv:1504.03601, first publicly posted 2015-04-14.
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, first publicly posted 2016-08-24.
3. E. Delucchi, L. Kühne and L. Mühlherr, *Combinatorial invariants of finite metric spaces and the Wasserstein arrangement*, arXiv:2408.15584, first publicly posted 2024-08-28.
