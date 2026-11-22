# An integral component-group coincidence for stable degenerations from order-four plane three-nets

## Finding

Let \(\mathcal N\) be any \((3,4)\)-net of complex projective lines, with twelve lines in three labelled classes of four and sixteen distinguished intersections. The marked-incidence graph \(\Gamma(\mathcal N)\) has one vertex per line or distinguished point and one edge per containment. Its graph Jacobian, equivalently the component group of a regular semistable genus-\(21\) smoothing of the stable curve below, is always

\[
K(\Gamma)\cong \mathbb Z/2\mathbb Z\oplus(\mathbb Z/8\mathbb Z)^2\oplus(\mathbb Z/24\mathbb Z)^4\oplus(\mathbb Z/96\mathbb Z)^2.
\]

Its order is \(2^{29}3^6\), and the rooted Laplacian has eighteen unit Smith entries. The two nonisomorphic order-four net Latin-square types have the *same complete integral* group.

## Assumptions and scope

Work over \(\mathbb C\). A \((3,4)\)-net is a triple of line classes \(A,B,C\) of size four and a set of sixteen marked points, with each cross-class pair meeting at one marked point and exactly one line from each class through each marked point. No restrictions are imposed on intersections *within* a class. Only the marked cross-class incidences enter \(\Gamma\); it is not the dual graph of the original plane divisor.

For its stable-curve interpretation, attach one copy of \(\mathbb P^1\) to each of the 28 vertices and glue ordinary nodes at distinct smooth points for every edge. The choice of attachment points does not affect the dual graph. Every component has respectively valence four or three, so this is a stable nodal curve of arithmetic genus \(48-28+1=21\). Its node thicknesses are assumed one in the regular semistable smoothing. Such smoothings exist by unobstructed deformation of stable nodal curves over characteristic zero. These conditions are essential for the Néron component-group identification.

## Proof

Identify the first and second four-line classes with row labels \(i,j\in\{0,1,2,3\}\). Their crosspoints are \(P_{ij}\), and the unique third-class line through \(P_{ij}\) is \(C_{s(i,j)}\) for a Latin square \(s\) of order four. Thus the graph has vertices \(A_i,B_j,C_k,P_{ij}\), with precisely the 48 edges \(P_{ij}A_i,P_{ij}B_j,P_{ij}C_{s(i,j)}\). In particular it is connected: two first-class line vertices are joined via any second-class line, and every third-class line has four point neighbors.

Independent permutations of the three line classes induce graph isomorphisms. Normalize any Latin square so the first row and first column are \((0,1,2,3)\). Exhausting row permutations then produces exactly four reduced squares, reproduced by the standalone certificate. They yield two isotopy types, distinguished by their 2-by-2 intercalate counts: three of the reduced squares have four, and the remaining one has twelve. This also proves that a single particular Fermat pencil does not suffice to establish the claim for all nets.

For each reduced square, form its 28-by-28 degree-minus-adjacency Laplacian and delete the last row and column. The exact Bareiss elimination in `verify.py` yields determinant \(2^{29}3^6\), and exact modular Smith elimination yields respective invariant-factor valuation lists

\[
(v_2(d_i))_i=(0^{[18]},1,3^{[6]},5^{[2]}),\qquad
(v_3(d_i))_i=(0^{[21]},1^{[6]}).
\]

Since the determinant has no other prime factors, these local elementary divisor data determine the globally ordered Smith factors, namely eighteen units followed by \(2,8,8,24,24,24,24,96,96\). For each prime the program performs elementary invertible row and column operations over \(\mathbb Z/p^{14}\mathbb Z\), pivoting at a coefficient of minimum valuation; all pivot valuations are below 14, and the exact determinant independently controls omitted higher powers. This is an exhaustive four-case integer certificate, not sampling.

Finally, for a regular semistable curve over a discrete valuation ring with reduced split special fiber and every node of thickness one, the standard degree-class-group/Raynaud identification gives the Néron component group of the Jacobian as the cokernel of a reduced intersection (graph Laplacian) matrix. The stable curve built from \(\Gamma\) satisfies these hypotheses, so its component group is precisely the computed critical group.

## Verification

Run `python3 verify.py` using only Python's standard library. It enumerates exactly the four reduced Latin squares, checks their different intercalate types, constructs each 27-by-27 rooted Laplacian, computes each exact Bareiss determinant, and independently computes the complete 2-adic and 3-adic Smith valuations using invertible modular row-column operations. Its printed success marker is recorded in `verification_output.txt`. The proof requires the cited standard identification of component groups of strictly semistable Jacobians, beyond the finite integer calculation.

## Relationship to prior work

Yuzvinsky (2003) introduced and developed the realization of finite Abelian groups by complex plane three-nets, including elliptic-cubic realizations and the Latin-square correspondence. Its Theorem 4.4 realizes both groups of order four, while its paper does not determine a degree-class group of the 28-vertex marked-incidence stable curve. Korchmáros–Nagy–Pace (2011) classify realizable groups more generally; their group-realization results do not imply a specific integral Smith decomposition. Related published calculations of sandpile groups for 18-vertex \((9_3)\) graphs concern different incidence objects. A determination of the rational spectrum or spanning-tree number alone would not imply the complete integral group or its coincidence across both net isotopy classes.

## Limitations

The claim is for the 28-vertex *marked cross-incidence* graph, not the full singularity-incidence graph of all twelve actual lines, and not the generalized Jacobian of their reduced union. The Néron interpretation assumes a *regular*, unit-thickness semistable smoothing; weighted dual graphs can have other groups. No classification of the other moduli of the smoothing curve, nor independence of nonunit thickness, is claimed. Historical priority remains open to literature not accessible through the checked sources; independent mathematical audit has not been performed.

## References

1. S. Yuzvinsky, *Realization of finite Abelian groups by nets in \(\mathbb P^2\)*, arXiv:math/0305242 (first posted 2003-05-16), *Compositio Mathematica* 140 (2004), 1614–1624, doi:10.1112/S0010437X04000600.
2. G. Korchmáros, G. P. Nagy and N. Pace, *3-nets realizing a group in a projective plane*, arXiv:1104.4439 (2011).
3. Standard Raynaud degree-class-group description of the component group of the Néron model of a semistable Jacobian (used only in the regular, unit-thickness split case).
