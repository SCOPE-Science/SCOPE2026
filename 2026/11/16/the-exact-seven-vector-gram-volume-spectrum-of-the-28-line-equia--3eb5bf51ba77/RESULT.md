# The exact seven-vector Gram-volume spectrum of the \(28\)-line equiangular tight frame

## Finding
Consider the canonical real equiangular tight frame of \(28\) unit vectors in dimension seven, indexed by the edges of \(K_8\). Among the \(\binom{28}{7}=1{,}184{,}040\) seven-vector selections, their Gram determinants and precise multiplicities are

| Gram determinant | Number of selections |
|---|---:|
| \(0\) | \(662{,}760\) |
| \(64/2187\) | \(508{,}896\) |
| \(256/2187\) | \(12{,}096\) |
| \(64/243\) | \(288\) |

There are exactly \(521{,}280\) bases. The largest squared parallelotope volume is \(64/243\), attained at precisely \(288\) edge sets: the \(8\) spanning stars and \(280\) disjoint unions of a triangle with a star on the complementary five vertices. These are all determinant-maximizing seven-point selections.

More generally, let \(H=(V,S)\) be the graph with the eight labeled vertices and the seven chosen edges. The determinant is positive if and only if every component is a tree or an odd unicyclic component, there is exactly one tree component, and the tree's two bipartite color classes have different cardinalities. If that tree has color-class sizes \(a,b\) and \(u\) other components are odd-unicyclic, then

\[\det G_S=\frac{16}{2187}\,4^u(a-b)^2.\]

An isolated vertex is regarded as a tree with color-class sizes \(1,0\); all components include isolated vertices when relevant.

## Assumptions and scope
Let \(e_i\) be the standard basis of \(\mathbb R^8\) and \(\mathbf1=(1,\ldots,1)\). For every unordered pair \(\{i,j\}\) of distinct indices between \(1\) and \(8\), put

\[ f_{ij}=\frac{4(e_i+e_j)-\mathbf1}{\sqrt{24}}\in\mathbf1^\perp.\]

Each vector has norm one, and the inner product of distinct vectors equals \(1/3\) when their edges meet and \(-1/3\) when their edges are disjoint. Symmetry or direct summation shows the frame operator on \(\mathbf1^\perp\) is \(4I\). We treat indexed seven-element subsets \(S\) without replacement, with Gram matrix \(G_S=(\langle f_e,f_{e'}\rangle)_{e,e'\in S}\). The Gram determinant is the square of the seven-dimensional parallelotope volume, not a smallest-eigenvalue or noisy-reconstruction constant.

## Proof
**1. Exact determinant reduction.** Write \(B_S\) for the \(8\times7\) unsigned incidence matrix of \(H\), namely the column for edge \(\{i,j\}\) is \(e_i+e_j\). Set \(P=I-\mathbf1\mathbf1^{\mathsf T}/8\) and \(W_S=[B_S\ \mathbf1]\), an \(8\times8\) integral matrix. Since \(4P(e_i+e_j)=4(e_i+e_j)-\mathbf1\), we have \(G_S=(2/3)B_S^{\mathsf T}PB_S\). Orthogonal decomposition into \(\mathbf1^\perp\) and the unit vector \(\mathbf1/\sqrt8\) gives

\[\det(W_S)^2=8\det(B_S^{\mathsf T}PB_S),\qquad \det G_S=\frac{16}{2187}\det(W_S)^2.\]

**2. Graph component criterion.** For a connected graph on \(v\) vertices, its unsigned incidence matrix has left kernel spanned by the vector taking values \(+1,-1\) on a bipartition if the graph is bipartite, and has zero left kernel if it is not bipartite. Consequently a connected component with \(e\) edges can contribute independent columns only if it is a tree (\(e=v-1\)) or is an odd unicyclic component (\(e=v\)). Since the whole graph has seven edges and eight vertices, there is exactly one tree component if all seven incidence columns are independent. Expansion of \(\det W_S\) along its last column then gives

\[|\det W_S|=2^u|a-b|.\]

For clarity, deleting one vertex row of a tree's unsigned incidence matrix has determinant of magnitude one; an odd-unicyclic component's square incidence determinant has magnitude two (remove attached leaves and reduce to its odd cycle). Summing signed tree-row cofactors against the appended constant column contributes the difference \(a-b\). In particular, a balanced tree component makes \(W_S\) singular, and any other component arrangement is also singular. This proves the graph criterion and the determinant formula, including every boundary case.

**3. Exhaustive symbolic graph counts.** A labeled tree on a specified \(t\)-vertex set with color classes of sizes \(a,b\), where \(a+b=t\), is a spanning tree of \(K_{a,b}\). The number for a specified bipartition is \(a^{b-1}b^{a-1}\); divide by two only when unordered equal-sized classes would double count. Thus, on all eight vertices, spanning trees with color difference \(6,4,2,0\) have respective counts \(8,5376,113400,143360\).

The counts \(U_k\) of connected labeled odd-unicyclic graphs on \(k=3,4,5,6,7\) vertices are respectively \(1,12,162,2520,45195\). This follows by choosing an odd cycle of length \(\ell\), arranging it in \((\ell-1)!/2\) undirected cycles, and attaching a forest rooted at the cycle vertices; the number of attachments is \(\ell k^{k-\ell-1}\) for \(\ell<k\), and one when \(\ell=k\).

With exactly one odd-unicyclic component (and exactly one tree component), the counts grouped by \(|\det W_S|\) are \(280\) at \(6\), \(3360\) at \(4\), \(395496\) at \(2\), and \(80640\) at zero. Concretely: \(k=3\) contributes \(280\) at \(6\) and \(6720\) at \(2\); \(k=4\) contributes \(3360\) at \(4\) and \(10080\) at zero; \(k=5\) contributes \(27216\) at \(2\); \(k=6\) contributes \(70560\) at zero; \(k=7\) contributes \(361560\) at \(2\). With two odd-unicyclic components, necessarily there are \((3,3,2)\) or \((3,4,1)\) component-size triples, yielding \(280\) at zero and \(3360\) at \(4\), respectively. Three odd-unicyclic components would need at least nine vertices.

Therefore the counts at nonzero magnitudes \(|\det W_S|=2,4,6\) are respectively \(508896,12096,288\). The complement to \(\binom{28}{7}=1184040\) is \(662760\) at zero. This yields the Gram determinant spectrum and its frequencies exactly, without statistical sampling. The maximal magnitude \(6\) comes only from a spanning tree with color sizes \(1,7\) or from one triangle and a five-vertex star with color sizes \(1,4\); these give respectively \(8\) and \(\binom83\cdot5=280\) configurations. There are no other maxima.

## Verification
Two standalone checks accompany this result. `verify_28frame.cpp` enumerates all \(1{,}184{,}040\) seven-edge subsets and computes the exact integer determinant of a seven-row coordinate submatrix by fraction-free elimination, asserting the four counts. For each selected edge column, the first seven coordinates of the unnormalized \(4(e_i+e_j)-\mathbf1\) vector have determinant of magnitude \(2048|\det W_S|\), by expanding \([4PB_S,\mathbf1]\) along the constant column and using its zero-sum property. `verify_graph_count.py` independently enumerates the same finite sample domain but computes graph components, odd cycles and bipartition imbalances, asserting the corresponding four integer magnitudes. Each returns a success marker and a nonzero process status on disagreement. The closed combinatorial enumeration and determinant reduction above are the mathematical proof; the complete-code repetitions provide error detection, not a replacement for infinite-case reasoning.

Reproduce with `g++ -std=c++17 -O2 verify_28frame.cpp -o verify_28frame && ./verify_28frame` and `python3 verify_graph_count.py`.

## Relationship to prior work
The canonical \((7,28)\) equiangular tight frame is classical. Böttcher–Fukshansky–Garcia–Maharaj–Needell (2016) examine its associated lattice, geometric realization, and specific bases, not the complete seven-subframe determinant distribution. Fickus–Lake (first public February 17, 2023) study binders (minimum dependent regular-simplex configurations) of doubly transitive equiangular tight frames and calculate the associated \((7,28)\)-frame binder with \(315\) size-four subsets. This identifies many small dependencies but does not classify all seven-subframe determinants, volumes or determinant-maximizing sets. Equiangular-frame constructions via rank-three graphs and Seidel matrices give the frame equivalence, not the new seven-edge census. The present theorem is a complete fixed-instance D-optimal design and basis-volume classification, not a new construction of equiangular lines.

## Limitations
The result concerns this fixed labeled \((7,28)\) real equiangular tight frame and seven-vector subsets, rather than arbitrary dimensions, unordered design equivalence classes, smallest eigenvalues or noise amplification. Claims of historical originality are subject to specialized or unindexed tables not available in the inspected literature. Exact combinatorial proof and finite verifiers establish the mathematical statement independently of those priority uncertainties.

## References
1. M. Fickus and E. C. Lake, *Doubly transitive equiangular tight frames that contain regular simplices*, arXiv:2302.08879v1, first posted 2023-02-17, https://arxiv.org/abs/2302.08879v1 ; full later-version text at https://arxiv.org/html/2302.08879v2 .
2. A. Böttcher, L. Fukshansky, S. R. Garcia, H. Maharaj and D. Needell, *Lattices from tight equiangular frames*, arXiv:1607.05350, 2016, https://arxiv.org/abs/1607.05350 .
3. Eiichi Bannai, Etsuko Bannai, Chin-Yen Lee, Hajime Tanaka and Wei-Hsuan Yu, *The real equiangular tight frames obtained from rank 3 graphs*, arXiv:2202.09858, 2022, https://arxiv.org/abs/2202.09858 .
