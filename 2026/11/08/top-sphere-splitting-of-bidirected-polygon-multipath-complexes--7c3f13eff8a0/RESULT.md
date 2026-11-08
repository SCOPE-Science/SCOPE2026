# Top-sphere splitting of bidirected polygon multipath complexes

## Finding

Let \(n\ge 6\). Let \(\mathrm{BP}_n\) be the digraph on \(\mathbb Z/(n+1)\mathbb Z\) with both directed arcs along every edge of the underlying cycle, and let \(X_n\) be its multipath simplicial complex: a set of arrows is a face if its spanning directed subgraph is a disjoint union of simple directed paths and isolated vertices. Define
\[
q_n=\left\lfloor\frac{n-1}{2}\right\rfloor+\begin{cases}1,&n\equiv0\pmod4,\\0,&\text{otherwise},\end{cases}
\qquad
r_n=\begin{cases}3,&n\equiv3\pmod4,\\1,&\text{otherwise}.\end{cases}
\]
Then there is an **integral homotopy equivalence**
\[
\boxed{\ |X_n|\simeq \left(\bigvee^{r_n}S^{q_n}\right)\vee S^{n-1}\vee S^{n-1}.\ }
\]
The two top-dimensional summands may be chosen as the inclusions of the actual subcomplexes consisting of proper subsets of all clockwise arcs, respectively all counterclockwise arcs. For example, the first three new lengths give \(|X_6|\simeq S^2\vee 2S^5\), \(|X_7|\simeq 3S^3\vee 2S^6\), and \(|X_8|\simeq S^4\vee 2S^7\). This result upgrades a published connectivity and integral-homology calculation to a complete infinite-family homotopy classification.

## Assumptions and scope

All complexes are finite, and homology is integral unless a coefficient field is displayed. A multipath includes isolated vertices; in particular, on a directed graph with \(n+1\) vertices it has at most \(n\) arrows. The cyclic underlying graph is simple since \(n+1\ge7\), and a pair of opposite arrows is forbidden because it makes a directed two-cycle. We use the published connectivity and integral-homology theorems for \(X(\mathrm{BP}_n)\) from Caputi–Collari–Smith (2026), Theorems 2.8 and 2.10, as stated mathematical inputs. We prove the additional spherical-generator assertion and the homotopy splitting independently of that paper.

## Proof

**1. Every top simplex is coherently directed.** A face with \(n\) arrows has an underlying undirected graph with \(n\) distinct edges: opposite arrows on one edge cannot both occur in a multipath. The underlying graph is a forest on \(n+1\) vertices because the only undirected cycle in the underlying polygon is its full cycle, which has \(n+1\) edges. Therefore the forest has exactly one connected component and is the polygon with one edge removed. The indegree and outdegree bound of a directed path forces all its arrows to point consistently along this spanning path. Thus its arrow set is precisely all clockwise arrows except one, or all counterclockwise arrows except one. These are the **only** \(n\)-arrow faces.

**2. Two embedded top spheres form an integral basis.** Write \(F\) and \(B\) for the sets of \(n+1\) clockwise and counterclockwise arcs. Every proper subset of \(F\) or \(B\) is a multipath. Thus the induced subcomplex on each of \(F\) and \(B\) is the boundary of an abstract \(n\)-simplex, an embedded \(S^{n-1}\). Its signed fundamental chain \(z_F\), respectively \(z_B\), is the alternating sum of its \(n+1\) top facets. These chains have disjoint arrow-support; in addition, any codimension-one face of a top facet is entirely in one of the two arrow orientations. Consequently the top boundary map splits into the two boundary maps of simplex boundaries. The top kernel of each is generated integrally by its alternating fundamental chain. There are no simplices of dimension \(n\). Hence
\[
H_{n-1}(X_n;\mathbb Z)=\mathbb Z[z_F]\oplus\mathbb Z[z_B],
\]
with **primitive**, geometrically spherical generators. This integer assertion does not follow merely from the rank of top homology.

**3. The bottom homology is spherical.** By the cited Theorem 2.8, \(X_n\) is \(\nu_n\)-connected where \(\nu_n=\lfloor(n-1)/2\rfloor-1\). By the cited Theorem 2.10, its only nonzero reduced homology groups are
\[
\widetilde H_{q_n}(X_n;\mathbb Z)\cong\mathbb Z^{r_n},\qquad
\widetilde H_{n-1}(X_n;\mathbb Z)\cong\mathbb Z^2.
\]
For \(n\not\equiv0\pmod4\), \(q_n=\nu_n+1\), so \(X_n\) is already \((q_n-1)\)-connected. For \(n\equiv0\pmod4\), \(q_n=\nu_n+2\). Here \(n\ge8\), hence \(\nu_n\ge2\). Since \(\widetilde H_{\nu_n+1}(X_n;\mathbb Z)=0\), the Hurewicz isomorphism in degree \(\nu_n+1\) gives \(\pi_{\nu_n+1}(X_n)=0\). Therefore \(X_n\) is again \((q_n-1)\)-connected. In every case \(q_n\ge2\), so the Hurewicz map \(\pi_{q_n}(X_n)\to H_{q_n}(X_n;\mathbb Z)\) is an isomorphism. We can choose \(r_n\) based maps of \(q_n\)-spheres representing an integral basis of bottom homology.

**4. A homology equivalence is a homotopy equivalence.** Wedge those \(r_n\) sphere maps with the two actual inclusions \(S^{n-1}\hookrightarrow X_n\) constructed in Step 2. This gives a based map
\[
f:\left(\bigvee^{r_n}S^{q_n}\right)\vee S^{n-1}\vee S^{n-1}\longrightarrow X_n.
\]
The source and target are simply connected CW complexes. By Steps 2–3 and the cited vanishing of all other reduced integral homology groups, \(f\) is an isomorphism on every integral homology group. The homological Whitehead theorem for simply connected CW complexes makes \(f\) a homotopy equivalence. This proves the claim for **every** \(n\ge6\), without extrapolating finite computations. \(\square\)

## Verification

The standalone `verify_bidirected_wedge.py` reconstructs faces directly from directed adjacency, confirms the exact two-family classification of maximal simplices, and independently computes reduced homology over \(\mathbb F_2\) for all underlying cycle sizes from four through nine. In particular its tests at seven, eight and nine vertices exercise all three lower-degree patterns occurring in the claimed range. A full Hasse-diagram acyclicity check for the five-vertex case provides an additional independent consistency check. Run `python3 verify_bidirected_wedge.py` with Python 3; the expected output is supplied in `verification_output.txt`. All these tests passed. They corroborate but do **not** prove the unrestricted integral statement, which is proved above from the cited theorems and the explicit top-sphere basis.

## Relationship to prior work

Caputi, Collari and Smith (2026) prove connectivity (Theorem 2.8) and the full integral homology groups (Theorem 2.10) for these complexes, but explicitly leave their wedge-of-spheres homotopy type as an open question in Section 3. This note uses those results without claiming them as new. The additional step is to identify a *primitive spherical basis* in top homology and to combine it with the first nonzero Hurewicz group and the homological Whitehead theorem. Neither the published homology ranks by themselves nor the previously studied oriented-cycle formula supplies this specific comparison map. Caputi, Collari, Di Trani and Smith (2024) treat polygonal graphs with a single orientation on each edge, explicitly excluding bidirected polygons in their Section 4.2.

## Limitations

The theorem assumes a simple bidirected cycle with at least seven underlying vertices, and it relies on the two cited published theorems rather than independently re-proving their general connectivity or homology formulas. No splitting is claimed to be equivariant for dihedral symmetries, no compatibility under polygon inclusions is asserted, and no classification of other digraphs is obtained. The finite verifier only evaluates small cases and mod-two homology; the integral infinite-family proof is the mathematical argument above.

## References

1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first submitted 2026-01-09, especially Theorems 2.8, 2.10, and Section 3. https://arxiv.org/html/2601.05670v1
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, *Mathematika* 70 (2024), e12235, especially Section 4.2. https://doi.org/10.1112/mtk.12235
3. Standard homological Hurewicz and homological Whitehead theorems for simply connected CW complexes, as used in Steps 3–4.
