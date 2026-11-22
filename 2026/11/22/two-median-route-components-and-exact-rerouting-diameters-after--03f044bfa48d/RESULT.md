# Two median route components and exact rerouting diameters after one rectangular-mesh vertex failure

## Finding

Let \(a,b\ge2\), let \(G\) be the rectangular unit grid with vertices \(\{0,\ldots,a\}\times\{0,\ldots,b\}\), and delete exactly one **strictly interior** vertex \(v=(i,j)\), where \(1\le i<a\) and \(1\le j<b\). Consider the shortest paths from \(s=(0,0)\) to \(t=(a,b)\) in \(G-v\). A reconfiguration step replaces exactly one intermediate path vertex, with both routes remaining shortest.

Their reconfiguration graph has **exactly two nonempty connected components**, denoted \(U\) (routes above the failed vertex) and \(L\) (routes below it). Each is a median graph, isometrically embeddable in a Boolean cube. For every pair of routes in the same component, the exact number of rerouting steps is the \(\ell_1\) distance of the north-step profiles defined below.

The component diameters, which also equal their minimum isometric hypercube dimensions, are
\[
\operatorname{diam}(U)=a(b-j-1)+(i-1)(j+1),\qquad
\operatorname{diam}(L)=ab-(i+1)(b-j+1).
\]
The respective numbers of routes are
\[
|U|=\sum_{x=0}^{i-1}\binom{x+j}{j}\binom{a-x+b-j-1}{a-x},
\]
\[
|L|=\sum_{y=0}^{j-1}\binom{i+y}{i}\binom{a-i-1+b-y}{b-y}.
\]
In particular,
\[
|U|+|L|=\binom{a+b}{a}-\binom{i+j}{i}\binom{a+b-i-j}{a-i}.
\]
This is an exact all-size, all-interior-failure classification; it includes singleton components.

## Assumptions and scope

Coordinates and grid edges are indexed, horizontal (east) and vertical (north) steps have unit length, and the source/target are opposite corners. A shortest path still has length \(a+b\) after deletion because the all-east-then-north and all-north-then-east paths avoid every strictly interior vertex. Such paths consist only of east and north steps. Vertex-changing adjacency is the conventional shortest-path rerouting rule, *not* token sliding or simultaneous changes of several vertices.

For a route \(P\), define \(h_r(P)\) as the number of east steps preceding its \(r\)-th north step, for \(1\le r\le b\). Then
\[
0\le h_1(P)\le\cdots\le h_b(P)\le a.
\]
The vector \(h(P)\) reconstructs \(P\) uniquely. Write \(P\preceq Q\) if \(h_r(P)\le h_r(Q)\) for every \(r\). Call a path **above** when \(h_{j+1}\le i-1\), and **below** when \(h_j\ge i+1\); these are the only two possibilities for a path avoiding \(v\).

## Proof

**1. Separation and path poset.** Every monotone path visits exactly one vertex of level \(i+j\), where the level of \((x,y)\) is \(x+y\). That vertex equals the failed vertex precisely when \(h_j\le i\le h_{j+1}\). Consequently a path avoids \(v\) exactly when \(h_{j+1}\le i-1\) or \(h_j\ge i+1\). The alternatives are exclusive and nonempty. A vertex-changing reconfiguration replaces a consecutive east–north pair with north–east, or conversely, and therefore increments or decrements one profile coordinate by one. A reconfiguration cannot cross between the two alternatives without passing through a profile with \(h_j\le i\le h_{j+1}\), which is forbidden.

**2. Each side is a lattice interval.** Coordinatewise minimum and maximum preserve nondecreasing integral profiles. The upper region is exactly the interval from
\[
P_{U,\min}=N^bE^a
\quad\text{to}\quad
P_{U,\max}=E^{i-1}N^{j+1}E^{a-i+1}N^{b-j-1}.
\]
The lower region is exactly the interval from
\[
P_{L,\min}=N^{j-1}E^{i+1}N^{b-j+1}E^{a-i-1}
\quad\text{to}\quad
P_{L,\max}=E^aN^b.
\]
Here \(E,N\) denote the respective steps; exponents indicate repeated steps. Equivalently, a profile encodes the subset of cells \((x,r)\) with \(1\le x\le h_r\), an order ideal of the product of two chains with the row order reversed. The two regions are intervals of this distributive lattice. Every nonterminal ideal has an addable or removable boundary cell, so each interval is connected by single-cell additions/removals. Hence exactly the two stated components occur.

**3. Exact distances, medianity and minimal cube dimension.** Each allowed square flip toggles one unit cell. Thus any sequence between \(P\) and \(Q\) has length at least
\[
d(P,Q)\ge\sum_{r=1}^{b}|h_r(P)-h_r(Q)|.
\]
Within a lattice interval, first remove cells in \(P\setminus Q\) to reach \(P\wedge Q\), and then add cells in \(Q\setminus P\). Each operation is a valid square flip and stays in the interval, attaining this lower bound. The component embeds isometrically into the cube whose coordinates are the cells between its minimum and maximum ideals. For three routes, the coordinatewise median of their profiles is nondecreasing and belongs to the same interval; the cellwise majority ideal is their unique metric median. Therefore each component is median. Each movable cell appears on an edge and gives a distinct convex halfspace split, so none of these coordinates can be identified in an isometric cube embedding. The minimal isometric cube dimension is precisely the number of movable cells, equal to the rank difference of the interval's endpoints.

**4. Diameters.** The minimum and maximum of any interval attain its largest distance, since every pair's differing cell set lies between those extremes. The rank of a path is \(\sum_r h_r\). The upper maximal profile has \(j+1\) entries equal to \(i-1\), followed by \(b-j-1\) entries equal to \(a\), while the lower minimal profile has \(j-1\) zeros followed by \(b-j+1\) entries equal to \(i+1\). Subtracting these ranks from \(0\) and \(ab\), respectively, yields the two displayed diameters and cube dimensions.

**5. Counts.** Each upper route has a unique position \(x\in\{0,\ldots,i-1\}\) for its \((j+1)\)-st north step. The prefix and suffix are counted by the two binomial factors in \(|U|\). Similarly every lower route has a unique position \(y\in\{0,\ldots,j-1\}\) for its \((i+1)\)-st east step, yielding \(|L|\). Alternatively exactly \(\binom{i+j}{i}\binom{a+b-i-j}{a-i}\) of the \(\binom{a+b}{a}\) original shortest routes pass through \(v\). Removing them gives the total-count identity.

## Verification

The standalone standard-library script `VERIFY.py` enumerates routes as east/north strings, reconstructs their geometric vertex sets, and independently reconstructs adjacency from changed intermediate vertices. It checks both exact component sizes, connectivity, separation, diameters and every pairwise rerouting distance by breadth-first search for \(2\le a,b\le5\) at every interior failure location. It also checks a larger finite range with direct \(\ell_1\) diameter enumeration. Its execution produced `PASS 208 punctured rectangular meshes; 519072 ordered pair BFS distance comparisons`. Additional small cases check the unique coordinatewise median property. This finite testing corroborates but does not replace the preceding general proof. Run `python3 VERIFY.py` from the extracted package directory.

## Relationship to prior work

Asplund et al., *Reconfiguration graphs of shortest paths*, characterize the shortest-path graph of an **intact** rectangular grid as a staircase lattice graph (their Section 6, Theorem 23 and Corollary 24); the present analysis uses that exact standard model but deletes an interior grid vertex and determines the resulting components, metrics, dimensions, and size formulas. Bonsma's planar shortest-path rerouting theory supplies more general reachability/topological obstructions, so the existence of separated routing sectors is not claimed to be new in isolation. It does not supply the present all-position median intervals, exact diameters, minimal hypercube dimensions or finite-size formulas. Bousquet et al. study parameterized complexity of shortest-path reconfiguration; Gajjar et al. characterize several graph families including the unpunctured hypercube. These are complementary in object or outcome. An equivalent deduction or an unindexed direct fault-analysis result may nonetheless exist; no priority or independence from all possible prior research is claimed.

## Limitations

This theorem covers one strictly interior failed vertex of a two-dimensional rectangular grid with opposite-corner terminals. Boundary failures, multiple faults, other terminals, other graph types, and non-shortest admissible paths are outside its scope. The general proof does not rely on finite verification. No external independent validation is claimed.

## References

1. N. Bousquet, K. Gajjar, A. Lahiri, A. E. Mouawad, *Parameterized Shortest Path Reconfiguration*, arXiv:2406.12717, first public 2024-06-18, https://arxiv.org/abs/2406.12717.
2. J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick, B. Werner, *Reconfiguration graphs of shortest paths*, arXiv:1705.09385, first public 2017-05-25, https://arxiv.org/abs/1705.09385.
3. P. S. Bonsma, *Rerouting shortest paths in planar graphs*, arXiv:1204.5613, first public 2012-04-25, https://arxiv.org/abs/1204.5613.
4. K. Gajjar, A. V. Jha, M. Kumar, A. Lahiri, *Reconfiguring Shortest Paths in Graphs*, Algorithmica 86 (2024), 3309–3338, https://doi.org/10.1007/s00453-024-01263-y.
