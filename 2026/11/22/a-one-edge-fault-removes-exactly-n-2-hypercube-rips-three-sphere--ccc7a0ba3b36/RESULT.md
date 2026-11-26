# A one-edge fault removes exactly \(n-2\) hypercube Rips three-spheres

## Finding

Let \(Q_n\) be the graph of binary words of length \(n\), with edges at Hamming distance one, and let \(G_n=Q_n-e\) with the **recomputed unweighted shortest-path metric**. For each integer \(n\ge3\), put
\[
c_n=\sum_{0\le j<i<n}(j+1)(2^{n-2}-2^{i-1}).
\]
In the inclusive Vietoris–Rips filtration,
\[
\operatorname{VR}(G_n;2)\simeq\bigvee^{c_n-(n-2)}S^3.
\]
The zero-summand wedge is a point, so the faulted three-cube is contractible at radius two. At radius one, the faulted complex is a wedge of \((n-2)2^{n-1}\) circles, one fewer than for the intact cube. The two filtrations are literally identical at every radius at least three.

**Persistence comparison.** Over any field the barcode differs by exactly one fewer degree-one interval \([1,2)\) and exactly \(n-2\) fewer degree-three intervals \([2,3)\); all other intervals agree. Over \(\mathbb Z\), the same statement holds for the multiplicities of the free interval-module summands at these two intervals, with a common integral persistence module for the remaining stages. It does not require all the integral groups at higher scales to be free.

## Assumptions and scope

A finite vertex set belongs to \(\operatorname{VR}(G;r)\) when all of its pairwise shortest-path distances in \(G\) are at most \(r\). The inclusion is at the lower endpoint of every half-open interval. The fault does not remove vertices. All homology groups in the proof have integer coefficients except where another coefficient ring is indicated. For a coefficient ring \(R\), \(I_R[a,b)\) denotes the persistence module with a copy of \(R\) on \([a,b)\), with identity maps inside the interval, and zero elsewhere.

## Proof

**1. Exactly one distance changes.** By cube symmetry we may delete \(e=\{0,e_1\}\), where \(e_i\) has one nonzero coordinate in position \(i\). The endpoints now have distance three: there is a three-edge detour along a square and the bipartition rules out a two-edge path. Between words of Hamming distance at least two, flip the differing coordinates in any order and in its reverse order. These geodesics have disjoint interiors: at each intermediate level their flipped coordinate sets are distinct (a proper prefix and suffix of the same size). In particular, at least one avoids the deleted edge. Every other adjacency is unchanged. Thus with \(X=\operatorname{VR}(Q_n;2)\) and \(Y=\operatorname{VR}(G_n;2)\), \(Y\) consists of precisely those faces of \(X\) not containing both endpoints of \(e\).

**2. Link and relative homology.** The vertex set of \(L=\operatorname{lk}_X(e)\) consists of \(a_i=e_i\) and \(b_i=e_1+e_i\) for \(2\le i\le n\), by the distance-two conditions from both endpoints. The \(a\)'s form one simplex, the \(b\)'s another, and the only cross-edges are \(a_i b_i\). Collapsing both contractible simplices in the quotient gives a graph of two vertices with \(n-1\) parallel edges. In particular \(L\) is connected, has the homotopy type of a wedge of \(n-2\) circles, and the squares \(a_2 a_i b_i b_2 a_2\), \(3\le i\le n\), give an integral basis of \(H_1(L)\) by taking differences from the rung with index two.

The union \(X=Y\cup(e*L)\) has intersection \((\partial e)*L\). The relative simplicial chains have exactly the simplices containing \(e\) as generators; orienting the two vertices of \(e\) first identifies this complex with the augmented chains of \(L\) shifted by two, since the boundary terms deleting an endpoint vanish relatively. Thus \(H_k(X,Y)=\widetilde H_{k-2}(L)\), with just \(H_3(X,Y)\cong\mathbb Z^{n-2}\) nonzero.

**3. An integral surjection.** For each \(3\le i\le n\), the eight vertices in the subcube on coordinates \(\{1,2,i\}\) give a radius-two complex that is the boundary of a four-dimensional cross-polytope (only antipodal pairs are forbidden). Its oriented fundamental cycle maps to the corresponding link square under the map \(H_3(X)\to H_3(X,Y)\): the tetrahedra containing \(e\) leave the four oriented link edges on deleting its endpoints. Each has coefficient \(1\) or \(-1\) and they form a cycle, so the image is the indicated square with one of its two orientations. The images form the integral basis above, and hence the map is onto over \(\mathbb Z\).

**4. Homotopy type.** The intact theorem [1, Theorem 1] gives \(X\simeq\bigvee^{c_n}S^3\). The relative sequence and the surjection give \(\widetilde H_3(Y)=\mathbb Z^{c_n-(n-2)}\) and no other reduced homology. The complex \(Y\) is connected because it contains the connected graph \(G_n\). The intersection \((\partial e)*L\) is the suspension of a connected complex, hence simply connected. The star \(e*L\) is contractible, so van Kampen for this union of subcomplexes gives \(\pi_1(Y)\cong\pi_1(X)=0\). The vanishing of \(H_2(Y)\) gives \(\pi_2(Y)=0\) by Hurewicz. Based maps from three-spheres representing an integral homology basis then induce an integral homology equivalence from their wedge to \(Y\), and the simply connected homology Whitehead theorem gives the desired homotopy equivalence, also in the zero-rank case.

**5. Radius one and persistence.** At radius one the faulted complex is the connected triangle-free graph \(G_n\), on \(2^n\) vertices and \(n2^{n-1}-1\) edges, so its cycle rank is \((n-2)2^{n-1}\). At radius three and above, both metrics admit exactly the same pairs, so the complexes and all subsequent inclusions agree. Both filtrations have the same degree-zero persistence, as the vertices are the same and each graph is connected at radius one. In positive degrees the only groups below radius three are degree one on \([1,2)\) and degree three on \([2,3)\), and they are free over \(\mathbb Z\) or vector spaces of the same ranks over any given field. The degree-one maps across radius two are zero by the degree-one homology vanishing there. The faulty radius-two-to-three inclusion factors through \(X\hookrightarrow\operatorname{VR}(Q_n;3)\), which is nullhomotopic by [2, Proposition 3.3]; the intact map is the same nullhomotopic inclusion. Thus there are no connecting positive-degree maps from either early interval into the remaining stages. For either coefficient choice, both modules split as their common part (degree zero and the common positive-degree tail, extended by zero below radius three) plus the indicated \(I_R[1,2)\) and \(I_R[2,3)\) summands in degrees one and three. The rank differences are one and \(n-2\), respectively. Over a field the common part has the usual interval decomposition, so this gives the full barcode comparison. Over \(\mathbb Z\) the displayed splitting makes the comparison without any decomposition assumption on the common part.

## Verification

The companion standard-library code `verify_hypercube_fault.py` checks the distances, radius-two faces, Betti numbers over \(\mathbb F_2\) and the link structure for \(n=3,4,5,6\); see `verification_output.txt` for its recorded results. The intact/faulted third Betti numbers in those dimensions are \((1,0),(9,7),(49,46),(209,205)\). This finite check is corroboration only. The arbitrary-dimensional integral homotopy argument and the coefficient-specific persistence statements follow from the proof, not from a field calculation or a higher-scale homology census.

## Relationship to prior work and limitations

The intact-cube sphere count and the nullhomotopy of intact successive scale inclusions are established inputs [1,2]. The cross-polytopal spheres in intact coordinate subcubes are also known [2]; the new step is the integral comparison with the specific lost edge, via their images in its link cycle lattice. This is different from puncturing the vertex set of the Hamming metric or determining a homotopy type of an intact higher-scale cube. Only one missing graph edge is treated. No torsion-freeness or new individual homotopy classification of the common stages at radii at least three is asserted. Priority is provisional.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, Theorem 1. https://arxiv.org/abs/2103.01040
2. H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222, Proposition 3.3 and Section 4. https://arxiv.org/abs/2309.06222
3. S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs*, arXiv:2202.02756. https://arxiv.org/abs/2202.02756
