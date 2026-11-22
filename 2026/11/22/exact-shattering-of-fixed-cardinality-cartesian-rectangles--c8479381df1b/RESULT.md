# Exact shattering of fixed-cardinality Cartesian rectangles

## Finding
Let \(1\le r\le m\) and \(1\le s\le n\). The hypothesis family on the cell domain \([m]\times[n]\) consists of exactly the Cartesian products \(A\times B\) with \(|A|=r\) and \(|B|=s\). There is an exact finite criterion for every shattered query support using its bipartite star components and a two-variable quota-inventory polynomial; it applies even when the grid is too small to provide spare rows or columns.

Write \(S\) for the queried cells, \(G_S\) for their bipartite incidence graph, \(\ell\) for the number of incident rows, and \(t\) for the number of incident columns. If \(G_S\) contains a three-edge simple path, \(S\) is not shattered. Otherwise its nontrivial connected components are stars. Give each single-edge component a left center by convention. Let the stars have orientations \(\epsilon_i\in\{L,R\}\) and degrees \(d_i\ge1\), with the right-center convention used only for degree at least two. Define
\[
F_{L,d,h}(x,y)=\begin{cases}(1+y)^d+x,&h=0,\\xy^h,&1\le h\le d,\end{cases}
\quad
F_{R,d,h}(x,y)=\begin{cases}(1+x)^d+y,&h=0,\\x^hy,&1\le h\le d.\end{cases}
\]
Then \(S\) is shattered **if and only if** \(G_S\) is a star forest and, for every integer vector \(0\le h_i\le d_i\),
\[
[x^r y^s](1+x)^{m-\ell}(1+y)^{n-t}\prod_i F_{\epsilon_i,d_i,h_i}(x,y)>0.
\tag{1}
\]
In particular, the criterion compares possible row and column quota inventories, not merely the number of available hypotheses.

For the whole parameter range \(m\ge2r\), \(n\ge2s\), criterion (1) simplifies: \(S\) is shattered exactly when \(G_S\) is a star forest with at most \(r\) incident rows and at most \(s\) incident columns. In this range, the complete shattered-support polynomial is
\[
\Phi_{m,n}^{r,s}(z)=\sum_{\ell=0}^r\sum_{t=0}^s
\binom m\ell\binom nt\,\ell!t!\,[u^\ell v^t]
\exp\left(uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)\right).
\tag{2}
\]
Its exact VC dimension is
\[
\operatorname{VCdim}=\begin{cases}
\max\{r,s\},&\min\{r,s\}=1,\\
r+s-2,&r,s\ge2.
\end{cases}
\tag{3}
\]
For \(r,s\ge3\), every maximum shattered support consists of two disjoint stars, one centered in each sort, occupying exactly \(r\) rows and \(s\) columns. The exact number of maximum supports is
\[
rs\binom mr\binom ns.\tag{4}
\]
For example, with \((m,n,r,s)=(6,6,3,3)\), the complete polynomial is \(1+36z+630z^2+6240z^3+3600z^4\).

## Assumptions and scope
The two coordinate sets are labeled finite sets, not ordered geometric intervals. Both factor cardinalities are **exact**, not upper bounds. Different \(A\times B\) are distinct for nonzero \(r,s\). Every queried cell receives one bit indicating membership in the product; all patterns must be realized to shatter a support. A star is a connected graph with at most one vertex of degree greater than one. Isolated unused rows and columns are outside the incident-vertex set and are accounted for separately. Equation (1) covers all finite valid \((m,n,r,s)\). Equations (2)--(4) require \(m\ge2r\), \(n\ge2s\); no optimality of this sufficient padding threshold is asserted.

## Proof
**1. Path obstruction and star components.** If the query graph contains the path with successive edges \((i,j)\), \((i',j)\), \((i',j')\), prescribe positive labels on its first and third edges and a negative label on its middle edge. Any product containing the positive endpoints necessarily contains the middle edge, a contradiction. Every finite bipartite graph with no three-edge simple path has each nontrivial component a star: a nonstar tree has a path of length three, and a cycle in a bipartite graph has length at least four and supplies such a path.

**2. The exact inventory test.** Fix a star component centered on the left with \(d\) incident queried cells, and a prescribed labeling with exactly \(h\) positive cells. If \(h>0\), its center and the \(h\) positively incident right leaves must be included in \(A\) and \(B\), and all other leaves excluded; the selected-coordinate inventory is the monomial \(xy^h\). If \(h=0\), either its center is excluded and any subset of its \(d\) right leaves is selected, giving \((1+y)^d\), or its center is included and no leaf is selected, giving \(x\). This proves the left-star formula; interchange sorts for a right-star. The single-edge convention avoids double counting components, while the two alternatives within each component are disjoint. For unused rows and columns, independent selection contributes \((1+x)^{m-\ell}(1+y)^{n-t}\). Because the star components have disjoint vertex sets, multiplying the inventory polynomials counts all permitted selections by their total row and column sizes. The coefficient in (1) is positive precisely when there is a rectangle realizing the labeling with \(h_i\) positives in component \(i\). Within a star, leaf permutations show that any two labelings with the same \(h_i\) have equivalent feasibility. Thus testing all degree-bounded \(h_i\) vectors is both necessary and sufficient. For \(S=\varnothing\), the product is empty and the coefficient is positive under the standing size hypotheses.

**3. The padded-range simplification.** If a support is shattered, its all-positive labeling requires every incident row and every incident column to lie in the chosen factors, hence \(\ell\le r\) and \(t\le s\); the preceding path obstruction also applies. Conversely assume those bounds and a star forest, with \(m\ge2r\), \(n\ge2s\). For any prescribed positive subset \(P\subseteq S\), select its incident rows and columns. Because each queried edge of a star forest has at least one degree-one endpoint, this product meets \(S\) **exactly** in \(P\): any negative edge cannot have both endpoints incident to positive edges. There are at least \(m-\ell\ge r\) completely unused rows and \(n-t\ge s\) completely unused columns, so complete these selected factors to cardinalities \(r,s\) using only unused vertices. These fillers create no new positive queried cell. This realizes every pattern, including the all-negative one.

**4. Enumeration and dimension.** A star forest on its incident vertices decomposes into single edges and stars of degree at least two, centered on either sort. The two-sort labeled exponential component series, with one variable for each incident vertex and \(z\) for each edge, is \(uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)\). Exponentiation produces precisely all such forests, with no isolated incident vertices. Choosing which \(\ell\) of \(m\) rows and which \(t\) of \(n\) columns are used yields equation (2). If the forest has \(c\ge1\) nontrivial components, it has exactly \(\ell+t-c\) edges. When \(r,s\ge2\), a one-component star has at most \(\max\{r,s\}\le r+s-2\) edges; at least two components imply at most \(r+s-2\) edges. The disjoint union of a star from one left center to \(s-1\) right leaves and a star from one right center to \(r-1\) left leaves attains this bound. If one quota equals one, a single star centered on the opposite sort achieves \(\max\{r,s\}\), and no support can be larger. This proves (3). For \(r,s\ge3\), equality in the two-component bound forces \(\ell=r\), \(t=s\), \(c=2\); both stars must have opposite-side centers, and choosing the center in each of the two sorts uniquely determines the support. There are \(rs\) choices on fixed active vertices, proving (4).

## Verification
The standard-library Python program `verify_inventory.py` implements the exact component-inventory criterion and independently compares it with brute-force product traces on all supports of sizes through four on the indicated small grids. It separately reconstructs the padded polynomial by exhaustive labeled star-forest enumeration on active vertices, rather than by applying the inventory rule. Compile `verify_uniform.cpp` using `g++ -O3 -std=c++17 verify_uniform.cpp -o verify_uniform` and run `./verify_uniform` to enumerate fixed-cardinality rectangles directly and check every support through the listed finite cutoffs. The outputs are in `verify_inventory_output.txt` and `verify_uniform_output.txt`.

The C++ program returns for quotas \((2,3)\) on a \(4\times6\) grid the coefficients \((1,24,276,800)\), and for quotas \((3,3)\) on a \(6\times6\) grid \((1,36,630,6240,3600)\). The independent Python active-vertex enumeration reproduces both. Finite replay confirms these examples, not the universal statements: the latter follow from the proof above.

## Relationship to prior work
The previously available unrestricted-rectangle theorem, *Shattered edge supports of combinatorial rectangles are star forests* (published-finding corpus, 2026), proves the path obstruction and exact shattering for arbitrary factor subsets and provides an unrestricted exponential enumerator. That premise is acknowledged and reused here. It does not assert shattering under **both exact nonzero factor-size quotas**, nor the all-parameter feasibility inventory (1), padded fixed-quota coefficient formula (2), or maximum-support count (4).

The published *Sharp static and online shattering thresholds for four-point Cartesian rectangles* (published-finding corpus, 2026) handles the special quota \((r,s)=(2,2)\) for all grids. That special-case learning-dimension conclusion is not claimed as new. The present result applies to all positive quota pairs, including quota pairs at least three in both coordinates, and resolves individual support feasibility in the small-grid regime as well as stable enumeration.

Block and collaborators' 2020 preprint and 2021 paper *P4-free Partition and Cover Numbers & Applications* motivate bipartite matrix rectangles and study edge partitions and covers by induced-\(P_4\)-free graphs. Their objects allow a four-cycle as one biclique component, whereas a support shattered by rectangular membership cannot even contain a not-necessarily-induced three-edge path. Their partition/cover bounds do not imply these membership-trace quota tests. Manurangsi (2023) relates general VC-dimension approximation to bicliques but is not asserted here to settle any uniform rectangle support classification.

## Limitations
The sufficiency padding region \(m\ge2r,n\ge2s\) is not asserted to be the sharp threshold. Equation (1) gives an exact finite criterion, not a closed elementary polynomial for arbitrary unpadded grids. Adaptive Littlestone dimensions and higher-dimensional products are outside the claim. Nontrivial prior-work coverage under alternative terminology remains possible; comparison is based on the identified primary and published material, not an exhaustive uniqueness guarantee. Independent mathematical audit has not been performed.

## References
1. A. R. Block, S. Brânzei, H. K. Maji, H. Mehta, T. Mukherjee, H. H. Nguyen, *P4-free Partition and Cover Numbers*, Cryptology ePrint 2020/1605 (2020); *P4-free Partition and Cover Numbers & Applications*, ITC 2021, DOI:10.4230/LIPIcs.ITC.2021.16.
2. *Shattered edge supports of combinatorial rectangles are star forests*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shattered-edge-supports-of-combinatorial-rectangles-are-star-for--41f165ae6da1.
3. *Sharp static and online shattering thresholds for four-point Cartesian rectangles*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-static-and-online-shattering-thresholds-for-four-point-car--83f66320ef8a.
4. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone’s Dimension via (Unbalanced) Biclique*, ITCS 2023, DOI:10.4230/LIPIcs.ITCS.2023.85.
