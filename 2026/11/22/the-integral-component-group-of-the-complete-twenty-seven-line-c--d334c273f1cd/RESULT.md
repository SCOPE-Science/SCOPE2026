# The integral component group of the complete twenty-seven-line cubic-surface boundary

## Finding

Let \(S\) be a smooth complex cubic surface without Eckardt points, and let \(D\subset S\) be the reduced sum of all its twenty-seven lines. Let \(\Gamma\) be the dual graph of \(D\), with one vertex per line and one edge per ordinary double point. Then \(D\) has twenty-seven smooth rational components, exactly 135 distinct ordinary nodes and arithmetic genus 109. Its graph critical group has the complete integral decomposition

\[
K(\Gamma)\cong (\mathbb Z/9\mathbb Z)^{13}\oplus\mathbb Z/45\mathbb Z\oplus(\mathbb Z/135\mathbb Z)^5.
\]

Its order, which is the number of spanning trees of \(\Gamma\), is \(3^{43}5^6=5129015115539641837921875\), and its exponent is 135. The rational Laplacian spectrum is \(0^1,9^{20},15^6\), so the integral invariant factors contain information not specified by the spectrum and order alone.

Moreover, \(D\sim -9K_S\). For a general section defining a smooth member of \(|-9K_S|\) that is nonvanishing at every node of \(D\), the pencil through \(D\) gives a proper regular split semistable smoothing (formally over \(\mathbb C[[t]]\)) with thickness one at all nodes. Its geometric Néron component group of the Jacobian is the displayed graph critical group.

## Assumptions and scope

The ground field is \(\mathbb C\). The cubic surface is smooth and **Eckardt-free**: no three of its twenty-seven lines are concurrent. This ensures that the reduced union has ordinary double points only. The asserted group is that of the dual graph, or equivalently the geometric component group for the indicated regular split semistable smoothing with unit node thicknesses. No claim is made for an Eckardt surface, another special fiber, unequal thicknesses, or the ambient surface's Picard group.

Write \(H\) for the pullback of a projective-plane line and \(E_1,\ldots,E_6\) for the six exceptional divisor classes of a blow-up of six points in general position. Represent \(dH-\sum_{i=1}^6m_iE_i\) by \((d;m_1,\ldots,m_6)\); in this encoding an exceptional curve \(E_i\) has \(m_i=-1\).

## Proof

**1. Canonical graph and genus.** The twenty-seven negative-one curves have classes

\[
E_i\ (1\le i\le6),\qquad H-E_i-E_j\ (1\le i<j\le6),\qquad 2H-\sum_{j\ne i}E_j\ (1\le i\le6).
\]

The intersection pairing in the stated coordinates is \((d;m)\cdot(d';m')=dd'-\sum_i m_im_i'\). For distinct members of this list it takes only values zero and one. Each curve meets exactly ten other curves, yielding \(27\cdot10/2=135\) edges. Eckardt-freeness makes these edges geometrically distinct nodes. The curve \(D\) is connected. Its arithmetic genus is \(135-27+1=109\), since all normalizations have genus zero. Summing the classes gives \(D=27H-9\sum_iE_i=-9K_S\), consistent with adjunction \(p_a(D)=1+(D^2+D\cdot K_S)/2=109\).

**2. Laplacian and spanning trees.** Let \(A\) be the adjacency matrix of the 27-vertex graph, defined by distinct-line intersection numbers. A direct calculation from the three families of classes verifies the strongly regular parameters \((27,10,1,5)\): every adjacent pair has one common neighbor and every nonadjacent pair has five. Equivalently,

\[
A^2=5I-4A+5J.
\]

Since the all-ones vector has eigenvalue ten, this identity yields the other adjacency eigenvalues one (multiplicity twenty) and minus five (multiplicity six). Therefore \(L=10I-A\) has spectrum \(0^1,9^{20},15^6\). Kirchhoff's matrix-tree theorem gives

\[
\tau(\Gamma)=\frac{9^{20}15^6}{27}=3^{43}5^6.
\]

**3. The integral step.** Fix any vertex and delete its row and column from \(L\), giving the integral \(26\times26\) reduced Laplacian \(B\). The Smith invariant factors of \(B\) determine \(K(\Gamma)\). For each prime \(p\in\{3,5\}\), work over \(\mathbb Z/p^5\mathbb Z\). At each step choose an entry of smallest \(p\)-adic valuation in the remaining submatrix, swap its row and column into the next pivot position, and clear the pivot's row and column by elementary invertible operations using the inverse of its unit part. This is legitimate because every remaining entry is divisible by the pivot's \(p\)-power. The procedure is exact over the local ring: its pivot valuations are the valuations of the Smith invariant factors.

The explicit coordinate matrices and executable, finite integer algorithm are in `VERIFY.py`. For each of three independently rooted matrices (vertices 0, 18, and 26), all 26 pivots are resolved below precision five and yield the following valuation multisets:

\[
\begin{array}{c|ccc}
p=3&v_3=0:7&v_3=2:14&v_3=3:5\\
p=5&v_5=0:20&v_5=1:6&
\end{array}
\]

There are no other prime divisors, because \(\det B=\tau(\Gamma)=3^{43}5^6\). To form the ordered integral Smith factors, sort the valuations independently for each prime, align them at the same indices, and multiply the prime powers. This gives seven unit factors, thirteen factors of nine, one of 45, and five of 135. These form a divisibility chain and have product \(3^{43}5^6\), proving the claimed complete critical group. The included verifier uses independent exact fraction-free determinants of three reduced matrices as a separate check of the spanning-tree count.

**4. Geometric component-group interpretation.** Each of the twenty-seven lines has self-intersection \(-1\), anticanonical degree one, and ten transverse intersection points. The reduced divisor \(D\in|-9K_S|\). The system \(|-9K_S|\) is basepoint free; a general member \(G\) is smooth and misses the finite set of nodes. In a local regular coordinate ring at each node of \(D\), the pencil equation becomes \(xy+t\,u=0\), where \(u\) is a unit, hence its total space is regular and its special fiber reduced nodal with thickness one. Away from the nodes, a general choice makes the total space smooth; the family is proper. The usual intersection-graph description of the Néron component group for a regular split semistable curve identifies it with \(K(\Gamma)\). This application is conditional on precisely these hypotheses.

## Verification

The standalone Python 3 standard-library script `VERIFY.py` reconstructs all 27 divisor classes, checks every pairwise intersection and all \(27^2\) strongly regular graph equations, and computes reduced Laplacians. Its integer Bareiss determinants at deleted vertices 0, 18 and 26 agree with \(3^{43}5^6\). A separate exact local pivot implementation over \(\mathbb Z/3^5\mathbb Z\) and \(\mathbb Z/5^5\mathbb Z\) returns the two valuation multisets and the listed integral factors for each sink. The script terminates with `SCHLAEFLI_27_LINE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK`. These calculations are reproducible without external packages; they verify a finite, fully specified matrix, not a sample of cubic surfaces.

## Relationship to prior work

The twenty-seven-line configuration and its incidence numbers are classical; Hunt [1] records the 135 meeting pairs. The Schläfli complement is the collinearity graph of \(\mathrm{GQ}(2,4)\), with strongly regular parameters recorded by Saniga et al. [2] and Brouwer–Van Maldeghem [3]. Özçelebi [4, §6.3.1] determines Smith factors of the **adjacency matrix of the 16-regular nonintersection graph**; that is not the Smith form of the reduced Laplacian \(10I-A\) for the 10-regular intersection graph. Brouwer–Van Maldeghem [3, §9.4] discuss critical groups, Smith forms and graph families generally, but their inspected Schläfli section does not give these 26 integral Laplacian factors. Busonero–Melo–Stoppino [5] discuss the general component-group machinery; their results do not compute this specific matrix. The contribution here is the complete exact integral group for the canonical 27-line nodal boundary and its regular smoothing, not any novelty claim for the classical graph itself.

## Limitations

This is a fully finite integral calculation attached to a classical configuration. It does not prove its priority over every unindexed historical graph computation, and an equivalent sandpile-group decomposition under generalized-quadrangle terminology remains a possible prior-art risk. It is not a classification of all cubic-surface reductions or arbitrary Néron models. For surfaces with Eckardt points the intersection curve has triple points and the nodal-graph argument does not apply unchanged. General semistable models with unequal edge thicknesses can have different component groups. No independent mathematical audit has been performed.

## References

1. Bruce Hunt, *A Gem of the Modular Universe*, early arXiv version dated 27 March 1995, `alg-geom/9503018`; accessible preprint: https://www.mathcurve.com/surfaces.gb/clebsch/hunt%202.pdf. See the 27-line incidence table.
2. Metod Saniga et al., *The Veldkamp Space of GQ(2,4)*, 2009, https://arxiv.org/abs/0903.0715.
3. Andries E. Brouwer and Hendrik Van Maldeghem, *Strongly Regular Graphs*, 2021, §§9.4, 10.10, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
4. Çiçek Güven Özçelebi, *Buildings and Kneser Graphs*, 2012, §6.3.1, https://pure.tue.nl/ws/files/3689733/721532.pdf, DOI:10.6100/IR721532.
5. Luisa Busonero, Margarida Melo and Lidia Stoppino, *On the complexity group of stable curves*, 2008, https://arxiv.org/abs/0808.1529.
