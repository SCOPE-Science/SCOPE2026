# The hexagon components of the eight-cycle Petersen Hom complex are rings of triangles

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph. In the ordinary polyhedral complex \(\operatorname{Hom}(C_8,P)\), fix an oriented simple hexagon of \(P\), taken modulo cyclic shifts but not reversal. Consider the homomorphisms whose cyclic eight-step walk reduces to that hexagon by deleting a two-step backtrack. They form **two whole components**. Each component is isomorphic as a cell complex to a ring of 24 filled triangles: consecutive triangles share one vertex, the preceding and following intersections are distinct vertices, and no other identifications occur. Each triangle has one vertex private to it. In particular, each component has 48 vertices and 72 edges, and it collapses to an embedded 24-cycle joining the shared vertices. There are 20 oriented hexagons, hence 40 components with this description.

## Assumptions and scope

The graphs are simple and undirected. Source vertices are labelled by \(\mathbb Z/8\). A cell is a tuple of nonempty sets of target vertices, with every possible edge present between sets at adjacent source sites; its polytope is the product of the corresponding simplices. A two-step backtrack is a subwalk \(A,X,A\), erased by retaining a single occurrence of \(A\). The theorem identifies the actual cell structure of the hexagon components, not just their homotopy type. It does not claim a new census of homotopy types or an all-length cell model.

## Proof

Write the oriented hexagon as \((v_j)_{j\in\mathbb Z/6}\), with edges in the direction \(v_j\) to \(v_{j+1}\). For \((i,j)\in\mathbb Z/8\times\mathbb Z/6\), define \(T_{i,j}\) by setting source site \(i+1\) to the three-element set \(N_P(v_j)\) and site \(i+2+k\) to the singleton \(\{v_{j+k}\}\) for \(0\le k\le6\), with the indices read cyclically. This is a triangle, since the neighbors of site \(i+1\) are both mapped to \(v_j\). Its vertices are exactly the three insertions of the spur at this position and core vertex. Every map in the claim occurs in a triangle of this form. The triangles are distinct: the varying site specifies \(i\), and the fixed sites and their order specify \(j\) and the oriented hexagon.

An alternative color is possible at a site only when its two neighbors have the same color, since distinct Petersen vertices have at most one common neighbor. At a vertex of \(T_{i,j}\), the site \(i+1\) is always such a site. Simplicity of the hexagon rules out all other sites except \(i\) and \(i+2\). Site \(i\) has equal-color neighbors precisely when the chosen spur color is \(v_{j-1}\); this map is shared with \(T_{i-1,j-1}\). Site \(i+2\) has equal-color neighbors precisely when the spur color is \(v_{j+1}\), giving the intersection with \(T_{i+1,j+1}\). The two exceptional spur colors are distinct. The third spur color gives no intersection. Indeed, a different triangle containing a map must vary at a different available site and has the same oriented reduced hexagon by the two explicit deletions just described. Two triangles with different varying sites share at most one map, since each fixes all the coordinates that the other can vary.

All incident edges therefore lie within this collection. There are no extra incident two-cells or higher cells: at any ordinary map vertex of such a cell each nonsingleton coordinate must be an available alternative-color site. If there are two such sites they are adjacent, and adjacent nonsingleton coordinates would give a \(K_{2,2}\) in the square-free target. A cell varying at just one site is already a face of the indicated triangle. Since connected components of a polyhedral complex are determined by its one-skeleton, the triangle unions found this way are whole components.

The triangle-intersection graph on the index pairs has steps \((1,1)\) and \((-1,-1)\). Translation by \((1,1)\) has order \(\operatorname{lcm}(8,6)=24\) on 48 index pairs, so it gives two 24-cycles. Distinct shared vertices occur at the two ends of each triangle along this cycle; there is one further private vertex. Every edge of a triangle belongs to no other triangle. Deleting one private-vertex edge with its triangle and then deleting the remaining private vertex and its edge yields the embedded cycle of shared vertices. This proves the claimed model and collapse.

The Petersen graph has ten unoriented hexagons, also checked by `verify_hexagon_triangles.py`: there are 120 injective rooted directed six-walks that close, and each unoriented hexagon has twelve such parametrizations. Accounting for two orientations gives the stated total.

## Verification

`python3 verify_hexagon_triangles.py` enumerates the injective rooted hexagons from the Kneser definition and checks the 24-triangle incidence models directly with site recolorings. The proof above establishes the cell restrictions and the absence of incident higher cells, not merely equality of face counts.

## Relationship to prior work and limitations

Fujii–Kimura–Nozaki (arXiv:2412.19039) and Matsushita (arXiv:2412.19144) give general square-free-target Hom homotopy results. The all-length Petersen primitive-period formula gives component counts from reduced-walk necklaces. Neither a homotopy classification nor a count by necklaces is offered here as a new result; the conclusion instead specifies which filled triangles meet and at which vertices, with an explicit surviving cycle. The labelled incidence proof is for the single-spur hexagon case at source length eight and does not give cell structures of arbitrary even-length Petersen cycle-Hom components.

## References

1. S. Fujii, K. Kimura, and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, https://arxiv.org/abs/2412.19039.
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, https://arxiv.org/abs/2412.19144.
3. *A primitive-period formula for all Petersen cycle-Hom complexes*, Resultary record `2026/11/22/SCOPE-a-primitive-period-formula-for-all-petersen-cycle-hom-complexes--172d5b46cff5`.
4. A. E. Brouwer, *Petersen graph*, https://aeb.win.tue.nl/drg/graphs/Petersen.html.
