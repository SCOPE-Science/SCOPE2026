# Integral graph Jacobian of the Klein \(21_4\) quadruple-point configuration

## Finding

The canonical symmetric Klein \(21_4\) incidence configuration comprises 21 of the lines in the classical Klein arrangement and precisely their 21 ordinary quadruple intersections. Its connected bipartite Levi graph \(G\), with an edge for each line–point incidence, has 42 vertices, 84 edges and cycle rank 43. Its complete integral critical group is
\[
K(G)\simeq (\mathbb Z/2\mathbb Z)^{10}\oplus\mathbb Z/6\mathbb Z\oplus\mathbb Z/138\mathbb Z\oplus(\mathbb Z/966\mathbb Z)^4\oplus\mathbb Z/1932\mathbb Z.
\]
The number of spanning trees, equivalently the order of this group, is \(2^{18}3^7 7^5 23^6=1426415078790162284544\). In particular the group has exponent \(1932\), with 17 nontrivial invariant factors and 24 unit factors in a reduced 41-by-41 Laplacian.

## Assumptions and scope

Work over \(k=\mathbb Q(a)\subset\mathbb C\) with \(a^2+a+2=0\), or an algebraically closed field of characteristic zero. Number the 21 projective lines by the explicit triples given in Section 4.1 of Bauer--Di Rocco--Harbourne--Huizenga--Lundman--Pokora--Szemberg (2014). A triple \((u,v,w)\) specifies the line \(uX+vY+wZ=0\). Identify projective intersection points over \(k\) by equality of cross products modulo \(a^2+a+2\). Of the 49 intersection points, select exactly the 21 lying on four distinct lines. Do not retain the 28 triple points. Let \(B\) be the 21-by-21 zero–one incidence matrix with \(B_{ij}=1\) when the \(i\)th line contains the \(j\)th quadruple point, and let
\[
L=\begin{pmatrix}4I_{21}&-B\\-B^{\mathsf T}&4I_{21}\end{pmatrix}.
\]
The critical group is \(\operatorname{coker}L_{\mathrm{red}}\), for any deleted vertex. These specifications define a finite, completely reproducible mathematical object, independent of the choice of the two conjugate values of \(a\), of point numbering, and of sink vertex.

## Proof

**1. Exact incidence.** The 21 listed coefficient triples yield \(\binom{21}{2}=210\) pairs of lines. Compute each projective intersection using a three-coordinate cross product in \(\mathbb Z[a]/(a^2+a+2)\) and group points by projective equality. The resulting 49 point classes consist of 21 containing six pairs each (hence exactly four incident lines) and 28 containing three pairs each (exactly three incident lines); \(21\cdot6+28\cdot3=210\). A separate reconstruction evaluates all 21 *explicit quadruple-point coordinates* printed in the same source against the line coefficients; the resulting incidence matrix agrees with \(B\) up to column permutation. Each row and each column of \(B\) has four entries equal to one. Consequently the matrix above is the graph Laplacian of a 42-vertex 4-regular bipartite graph.

**2. Connectivity and spanning trees.** Exact integer characteristic-polynomial computation yields
\[
\det(tI_{42}-L)=t(t-8)(t-6)^8(t-2)^8(t^2-10t+23)^6(t^2-6t+7)^6.
\]
Since zero occurs once, \(G\) is connected. The matrix–tree theorem gives
\[
\tau(G)=\frac{8\cdot6^8\cdot2^8\cdot23^6\cdot7^6}{42}=2^{18}3^7 7^5 23^6.
\]
An independent exact determinant of a deleted 41-by-41 Laplacian gives the same integer.

**3. Integral Smith calculation.** The signed eigenvalues do not determine the critical group. An exact integer Smith form of a reduced Laplacian gives 24 unit diagonal entries and the nonunit factors
\[
2^{[10]},\quad 6,\quad138,\quad966^{[4]},\quad1932.
\]
Here the bracket multiplicities label *copies* of invariant factors, not exponentiation of group elements. These integers divide their successors: \(2\mid6\mid138\mid966\mid1932\). An independent prime-local elimination modulo \(p^e\), with \(e\) strictly larger than the largest Smith valuation, gives for each prime \(p\) the following counts of local diagonal valuations \(0,1,2\):

| Prime | Valuation 0 | Valuation 1 | Valuation 2 |
| --- | ---: | ---: | ---: |
| 2 | 24 | 16 | 1 |
| 3 | 34 | 7 | 0 |
| 7 | 36 | 5 | 0 |
| 23 | 35 | 6 | 0 |

All other primes are excluded by the independently computed determinant. The prime-local counts reconstruct precisely the invariant factors listed above. Repeating both calculations for deleted vertices 1, 22 and 42 yields identical factors; this is also a check of sink independence. The product of all nonunit factors equals \(\tau(G)\), completing the proof.

**4. Stable-curve interpretation.** Glue 42 projective lines according to \(G\), with four distinct smooth marked points on each component and one ordinary split node for each of its 84 edges. Every rational component has four special points, hence the curve is stable. Its arithmetic genus is \(84-42+1=43\). For a regular semistable unit-thickness smoothing, the usual graph-Laplacian description of the geometric Néron component group of the Jacobian identifies it with \(K(G)\). This is conditional on the stipulated smoothing and does not assert that simply blowing up the 21 quadruple points of the original plane arrangement yields the same nodal curve: its 28 other triple crossings remain.

## Verification

Run the standalone pure-Python/SymPy script `verify_klein_quadruple_graph.py`. It independently produces the quadruple-point incidence both from all 210 line-pair intersections and from the printed 21 quadruple coordinates, checks the Laplacian characteristic polynomial and determinant, then recomputes exact Smith factors and modular prime-local valuations for three different sink choices. Successful completion prints `KLEIN_21_4_QUADRUPLE_GRAPH_VERIFIED_OK`. The attached script supplies all input coefficients and can be executed without external input data. The input is a complete 21-line coefficient list; no data or log from another computation is required.

## Relationship to prior work

Bauer et al. (first public arXiv version, 10 July 2014) provide the 21 line equations, 49 points, complete incidence data and the \((21_4)\) subconfiguration. Those *geometric data and incidences* are prior work. Gévay and Pokora study the same Klein arrangement and its Grünbaum–Rigby realization, plus further derived configurations; their inspected full text does not give a reduced-Laplacian Smith form or a critical-group classification. Lorenzini provides general Laplacian and critical-group theory but not these 42-vertex invariants. A separately known graph using **all** 49 crossings and the same 21 lines has 70 vertices and a different critical group; that broader *vertex set* does not make this 42-vertex group a corollary of its stated invariant-factor decomposition. The new claim here is only the precise integral critical group of the canonical 21-line/21-quadruple-point graph, with its exact tree count and conditional genus-43 Jacobian-component application. Searches for equivalences and old tables remain non-exhaustive.

## Limitations

The result is in characteristic zero for the geometric Klein configuration. It does not classify bad reduction or rational Frobenius actions. Only the abstract rational nodal stable curve and appropriate regular thickness-one smoothings are addressed; no claim about the actual plane arrangement being already nodal after a partial blow-up is made. The exact published incidence array makes the computation feasible but does not itself publish the resulting integral critical group. Unpublished or unindexed historic tabulations remain possible.

## References

1. T. Bauer et al., *Bounded Negativity and Arrangements of Lines*, arXiv:1407.2966v1 (first public 10 July 2014), Section 4.1 and the explicit 21-line/49-point incidence table. https://arxiv.org/abs/1407.2966
2. G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309 (2022), Section 2; DOI:10.1007/s13366-023-00697-9. https://arxiv.org/abs/2211.15309
3. D. Lorenzini, *Smith normal form and Laplacians*, J. Combin. Theory Ser. B 98 (2008), 1271–1300. DOI:10.1016/j.jctb.2008.02.002.
