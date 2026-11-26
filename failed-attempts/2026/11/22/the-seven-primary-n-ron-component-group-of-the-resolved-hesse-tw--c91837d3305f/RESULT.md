# The seven-primary Néron component group of the resolved Hesse twelve-line boundary

## Finding

Let \(\mathcal H\subset\mathbb P^2_{\mathbb C}\) be the reduced union of the twelve inflection lines of the classical Hesse pencil. Blow up its nine quadruple points, and let \(D\) be the reduced union of the twelve strict line transforms and the nine exceptional curves. Then \(D\) is a connected stable nodal curve with 21 rational components, 48 nodes and arithmetic genus 28. Its dual graph \(\Gamma\) has integral Laplacian characteristic polynomial

\[
\det(tI-L_\Gamma)=t(t-3)^{11}(t-7)^9.
\]

Its **complete integral graph critical group** is

\[
K(\Gamma)\cong(\mathbb Z/3\mathbb Z)^2\oplus(\mathbb Z/21\mathbb Z)^8.
\]

Equivalently, its 3-primary part is \((\mathbb Z/3\mathbb Z)^{10}\), its 7-primary part is \((\mathbb Z/7\mathbb Z)^8\), its exponent is 21, and it has precisely \(3^{10}7^8=340405734249\) elements. For a proper regular split semistable one-parameter smoothing over a strictly Henselian discrete valuation ring of characteristic-zero residue field, with this special fiber and all node thicknesses one, the geometric component group of the Néron model of the generic Jacobian is isomorphic to this group.

## Assumptions and scope

The Hesse arrangement is considered over \(\mathbb C\); all nine fourfold points are blown up once, and the twelve remaining ordinary double points are **not** blown up. The resulting reduced divisor \(D\) consists of the strict transforms and exceptional curves, not just the original twelve strict transforms. Its abstract stable curve has only ordinary nodes. For the conditional Néron statement, assume a proper, regular, split semistable family with all edges of thickness one; no claim concerns a nonregular model or arbitrary edge lengths.

Identify the nine quadruple points with the affine plane \(\mathbb F_3^2\). The twelve inflection lines are the four parallel classes of three affine lines each. Each affine line contains three distinguished points; every distinguished point lies on four lines; distinct lines in different classes meet at exactly one distinguished point; and the three projective lines belonging to one class form a triangle with three additional ordinary nodes. The latter provide twelve ordinary nodes in total. Blowing up a fourfold point produces one exceptional component meeting its four line transforms at four distinct nodes. Consequently, the strict transforms have five nodes apiece (three exceptional intersections and two ordinary intersections), while each exceptional component has four. All components are rational and carry at least three special points, so the curve is stable. The graph is connected, with \(12+9=21\) vertices and \(9\cdot4+12=48\) edges, hence \(p_a(D)=48-21+1=28\).

Define \(K(\Gamma)\) to be the torsion subgroup of \(\operatorname{coker}(L_\Gamma:\mathbb Z^{21}\to\mathbb Z^{21})\), equivalently the cokernel of any 20-by-20 principal reduced graph Laplacian.

## Proof

**1. Integral dual graph.** Order the twelve line vertices by their four parallel classes, and order the nine exceptional vertices by points of \(\mathbb F_3^2\). Let \(B\) be the \(12\)-by-\(9\) integer point–line incidence matrix: \(B_{\ell,P}=1\) when the point \(P\) lies on the line \(\ell\), zero otherwise. Let \(C\) be the adjacency matrix of four disjoint triangles on the twelve line vertices; thus \(C=\operatorname{diag}(J_3-I_3,J_3-I_3,J_3-I_3,J_3-I_3)\). The geometric node description gives the **integer** matrix

\[
L=\begin{pmatrix}5I_{12}-C&-B\\-B^{\mathsf T}&4I_9\end{pmatrix}.
\]

Every pair of distinct points lies on one affine line and each point lies on four lines, so \(B^{\mathsf T}B=3I_9+J_9\). Every line has three points, distinct nonparallel lines share one point, and distinct parallel lines share none, giving

\[
BB^{\mathsf T}=2I_{12}+J_{12}-C.
\]

These two identities are integral equalities, independent of spectral approximations.

**2. Laplacian spectrum.** On the 3-dimensional subspace of line vectors constant within each parallel class and with sum of class constants zero, \(B^{\mathsf T}=0\) and \(C=2I\), so \(L\) has eigenvalue 3. Let \(U\) be the 8-dimensional subspace of line vectors whose sums within each class vanish, and let \(V\) be the 8-dimensional zero-sum point subspace. The incidence matrix restricts to a scaled isometry \(V\to U\), because \(B^{\mathsf T}B=3I\) on \(V\). On each of eight paired two-dimensional summands the Laplacian is orthogonally equivalent to

\[
\begin{pmatrix}6&-\sqrt3\\-\sqrt3&4\end{pmatrix},
\]

which has eigenvalues 3 and 7. The final two-dimensional subspace of vectors constant on all twelve line vertices and on all nine point vertices carries \(\bigl(\begin{smallmatrix}3&-3\\-4&4\end{smallmatrix}\bigr)\), with eigenvalues 0 and 7. Therefore the full spectrum is \(0^1,3^{11},7^9\), proving the displayed characteristic polynomial and connectivity. The matrix–tree theorem gives

\[
|K(\Gamma)|=\frac{3^{11}7^9}{21}=3^{10}7^8.
\]

**3. Exact prime-local ranks.** Let \(H=\operatorname{diag}(J_3,J_3,J_3,J_3)\), so \(C=H-I_{12}\). Over either \(\mathbb F_3\) or \(\mathbb F_7\), the lower right block \(4I_9\) is invertible. Taking its Schur complement, multiplication by the unit 4 leaves the rank controlled by

\[
4(5I_{12}-C)-BB^{\mathsf T}=18I_{12}-3C-J_{12}=21I_{12}-3H-J_{12}.
\]

Modulo 3 this is \(-J_{12}\), of rank 1. Hence \(\operatorname{rank}_{\mathbb F_3} L=9+1=10\). Modulo 7 it is \(-3H-J_{12}\). It factors through the four surjective class-sum functionals, and the induced four-by-four matrix of output class constants is \(-3I_4-J_4\). Its eigenvalues are \(-3\) with multiplicity 3 and \(-7=0\) with multiplicity 1 over \(\mathbb F_7\), hence it has rank 3. Therefore \(\operatorname{rank}_{\mathbb F_7} L=9+3=12\).

The integral Laplacian has one zero Smith entry. Thus exactly \(21-10-1=10\) of its nonzero entries are divisible by 3, and exactly \(21-12-1=8\) are divisible by 7. Since its critical-group order has valuations exactly 10 and 8 at these primes, each corresponding primary Smith factor has valuation one. All other primes are absent. Thus the primary decomposition is \((\mathbb Z/3)^{10}\oplus(\mathbb Z/7)^8\), and combining coprime cyclic factors gives the asserted invariant factors \((\mathbb Z/3)^2\oplus(\mathbb Z/21)^8\).

**4. Jacobian component group.** For a proper regular split semistable curve over a strictly Henselian discrete valuation ring, Raynaud's graph description identifies the geometric component group of the Néron model of its generic Jacobian with the discriminant of the graph-cycle intersection pairing. When every node has thickness one, this discriminant is exactly the graph critical group calculated by the integral reduced Laplacian above. The asserted Néron conclusion follows subject to the stated smoothing hypotheses; it does not assert existence of a particular embedded smoothing inside the blown-up plane.

## Verification

The attached `verify_hesse_boundary.py` is a standalone exact-arithmetic checker (Python 3 and SymPy). It independently forms twelve Hesse line equations in \(\mathbb Z[\omega]\) with \(\omega^2+\omega+1=0\), enumerates all 66 line pairs, and groups projectively equal intersections exactly. It obtains nine quadruple points and twelve nodes, reconstructs the 21-vertex graph, computes an integer Laplacian and its characteristic polynomial and 20-by-20 Smith normal form, then reconstructs the same Smith factors from an independent affine-plane incidence model and verifies the ranks modulo 3 and 7. Run `python verify_hesse_boundary.py`; success prints `HESSE_RESOLVED_NERON_COMPONENT_GROUP_OK`. The mathematical proof above is independent of trusting a finite enumeration.

## Relationship to prior work

Artebani–Dolgachev's *The Hesse pencil of plane cubic curves* (first arXiv posting 2006-11-19, arXiv:math/0611590) provides the classical four-triangle, nine-flex incidence structure. Innamorati's *Quasi-Configurations Derived by Special Arrangements of Lines* (2024, DOI 10.3390/axioms13050321, §3) explicitly lists the twelve lines and the twelve ordinary triangle vertices. These supply the geometric starting point, not the integral Laplacian spectrum and 3/7-primary critical-group calculation.

An earlier calculation for the **Levi incidence graph alone** uses the same twelve lines and nine points but has only 36 edges and yields a pure 3-primary critical group; the present graph additionally retains all twelve ordinary line intersections after resolving the quadruple points. Other arithmetic work on the reduced twelve-line divisor determines Picard-torus and zeta information, not the monodromy pairing of this resolved dual graph. General graph/Néron correspondence and matrix-tree formulas are prior theory, used here rather than claimed as new. The distinctive claim is the exact integral invariant factors of this specific natural stable boundary, together with their direct spectral and prime-local explanation.

## Limitations

No classification is asserted for arbitrary Hesse-arrangement modifications, non-unit thicknesses, singular models, or non-split component actions. The group is an invariant of this specified **resolved** dual graph; it differs from the graph obtained by replacing all intersections with incidence-only edges. Historical priority is provisional: mathematical search and comparison cannot exclude an unindexed equivalent computation. Independent validation has not been performed.

## References

- M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (initial posting 2006-11-19), https://arxiv.org/abs/math/0611590.
- S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024), 321, https://doi.org/10.3390/axioms13050321, §3.
- M. Papikian, *Graph Laplacians, component groups and Drinfeld modular curves*, arXiv:1505.06860 (2015), https://arxiv.org/abs/1505.06860 (background on graph Laplacians and component groups; different family).
