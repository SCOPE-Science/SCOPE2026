# The matching complex of \(C_3\square C_4\): forty-four three-spheres and its full row-column character

## Finding
Let \(G=C_3\square C_4=K_3\square C_4\) be the Cartesian graph product of a triangle and a four-cycle, and let \(\mathcal M(G)\) be its ordinary matching complex. There is an integral homotopy equivalence
\[
|\mathcal M(G)|\simeq\bigvee^{44}S^3.
\]
In addition, the natural \(S_3\times D_4\) action on \(G\) induces the rational third-homology character in the table below, determining the entire forty-four-dimensional representation. The actual geometric quotient by this order-forty-eight group has \(\widetilde H_3(-;\mathbb Q)\cong\mathbb Q\), and the quotient by the order-twelve product of row and column rotation groups has \(\widetilde H_3(-;\mathbb Q)\cong\mathbb Q^4\). All other reduced rational homology of these quotients vanishes.

The row class \(e\), \(\rho\), or \(\tau\) means identity, nonidentity three-cycle, or transposition in \(S_3\). The column classes \(e\), \(r^2\), \(r^{\pm1}\), \(s_v\), and \(s_e\) mean identity, half-turn, quarter-turns, reflections through opposite vertices, and reflections through opposite edges of the four-cycle. Here \(r:j\mapsto j+1\), and \(s_v:j\mapsto-j\), with column indices modulo four.

| Row class | Column class | Class size | Trace on \(\widetilde H_3\) |
|:--|:--|--:|--:|
| \(e\) | \(e\) | 1 | 44 |
| \(e\) | \(r^2\) | 1 | 8 |
| \(e\) | \(r^{\pm1}\) | 2 | -2 |
| \(e\) | \(s_v\) | 2 | -8 |
| \(e\) | \(s_e\) | 2 | -4 |
| \(\rho\) | \(e\) | 2 | -1 |
| \(\rho\) | \(r^2\) | 2 | -1 |
| \(\rho\) | \(r^{\pm1}\) | 4 | 1 |
| \(\rho\) | \(s_v\) | 4 | 1 |
| \(\rho\) | \(s_e\) | 4 | -1 |
| \(\tau\) | \(e\) | 3 | -2 |
| \(\tau\) | \(r^2\) | 3 | 10 |
| \(\tau\) | \(r^{\pm1}\) | 6 | -4 |
| \(\tau\) | \(s_v\) | 6 | 2 |
| \(\tau\) | \(s_e\) | 6 | 2 |

Over \(\mathbb Q\), the irreducibles of \(S_3\) are \(\mathbf1,\varepsilon,V_2\), with dimensions \(1,1,2\). Those of \(D_4\) are the four lines \(L_{a,b}\), where \(r\) acts as \(a\in\{\pm1\}\) and \(s_v\) as \(b\in\{\pm1\}\), and the standard two-dimensional module \(E\). The multiplicity columns below are ordered \(L_{+,+},L_{+,-},L_{-,+},L_{-,-},E\):

| \(S_3\)-type | \(L_{+,+}\) | \(L_{+,-}\) | \(L_{-,+}\) | \(L_{-,-}\) | \(E\) |
|:--|--:|--:|--:|--:|--:|
| \(\mathbf1\) | 1 | 1 | 2 | 2 | 0 |
| \(\varepsilon\) | 0 | 2 | 0 | 0 | 3 |
| \(V_2\) | 1 | 3 | 2 | 3 | 3 |

## Assumptions and scope
The twelve graph vertices are pairs \((i,j)\) with \(i\in\mathbb Z/3\) and \(j\in\mathbb Z/4\). Two distinct vertices are joined when precisely one coordinate changes by an edge of the corresponding cycle. In particular, \(C_3\) is a triangle, not a three-vertex path, and both coordinates are periodic. The graph has twenty-four edges. A simplex of \(\mathcal M(G)\) is any set of graph edges with pairwise disjoint endpoints. All homotopy assertions are nonequivariant; character and quotient claims concern rational homology of the specified natural group action, not an asserted equivariant wedge model. The theorem concerns precisely this graph.

## Proof
Order the graph vertices lexicographically and order its twenty-four graph edges lexicographically by sorted endpoints. Encode a matching by the corresponding 24-bit integer; the accompanying standalone program recursively enumerates every matching by adding graph edges in strictly increasing edge order whenever its endpoints are still unused. Including the empty matching, the exact number is 2764. Counts by simplex dimension zero through five are respectively 24, 204, 748, 1149, 588, and 50.

The finite acyclic matching uses the ordered edge-index pivots
`[5,23,16,7,4,3,22,21,1,15,20,19,0,9,6,12,8,10,18,14,17,13,2,11]`.
At a pivot, pair each still-unpaired nonempty face not containing that edge with the face obtained by adding the edge, if both remain. This makes exactly 1358 disjoint pairs on the 2763 nonempty faces. Orient every codimension-one Hasse relation downwards, except matched relations, which point upwards. A complete topological sort visits all 2763 nodes along 10488 incidence relations; hence no directed cycle exists. The unmatched cells are one zero-cell, forty-five three-cells, and one four-cell, with no other cells.

For exact attaching degrees, orient each simplex by increasing edge indices, with the standard alternating signed deletion boundary. Eliminate each matched unit boundary incidence over the integers. Concretely, the projection of an unmatched cell is itself, the projection of a cell matched as the upper member is zero, and if a lower matched cell \(a\) is paired with an upper cell \(b\), solve the equality \(\partial b=[b:a]a+\sum_{c\ne a}[b:c]c\) for \(a\), then project the other terms recursively. Acyclicity proves that this recursion terminates. The unique critical four-cell has a Morse boundary consisting of **seven distinct critical three-cells with coefficients \(\pm1\)**. Their complete face masks and coefficients are:

| Critical three-face mask (hexadecimal) | Signed coefficient |
|:--|--:|
| `0x90102` | -1 |
| `0x94002` | 1 |
| `0x210500` | -1 |
| `0x404410` | -1 |
| `0x408401` | -1 |
| `0x40c010` | -1 |
| `0x480101` | 1 |

The Morse CW three-skeleton is a wedge of forty-five three-spheres, and the four-cell attaches by this primitive degree vector. Since \(\pi_3(\bigvee^{45}S^3)\cong\mathbb Z^{45}\), a unimodular change of three-sphere basis sends the attaching map to the inclusion of one wedge summand with degree one. The cell cancels, proving the wedge of forty-four three-spheres. In particular, integral homology is free and supported in degree three.

For the symmetry result, let \(g\in S_3\times D_4\). It acts by permuting graph edges and hence matching simplices. The simplicial Lefschetz number equals the alternating sum, over all nonempty setwise fixed simplices, of the sign of the permutation induced on their ordered vertices. Since the only nonzero rational homology is \(H_0\) and \(\widetilde H_3\), its value is \(1-\operatorname{tr}(g\mid\widetilde H_3)\). Evaluating this signed sum for every one of the forty-eight group elements yields the fifteen class values above.

There is a second exact derivation. Decompose the twenty-four graph edges into cycles under \(g\). Discard an orbit whose edges share an endpoint. Make a conflict graph on the remaining orbits, adjacent when their union cannot be a matching. An invariant matching is a union of mutually compatible edge orbits. Every included orbit contributes a factor of minus one to the signed, reduced Lefschetz sum, independent of its length; consequently the trace is the independence polynomial of this orbit-conflict graph evaluated at minus one. The recurrence \(I(H;-1)=I(H-v;-1)-I(H-N[v];-1)\), with \(I(\varnothing;-1)=1\), computes these traces independently. Both derivations agree on all forty-eight elements.

The two displayed character tables follow from rational character orthogonality for \(S_3\times D_4\). Averaging traces over all forty-eight group elements gives exactly one invariant homology class. Averaging over the twelve row/column rotations gives exactly four. For a finite simplicial group action, barycentric subdivision makes simplices stabilizer-fixed pointwise, so with rational coefficients the homology of the geometric orbit space identifies with invariant homology. This gives the asserted quotient homology groups.

## Verification
Run `python3 torus_match_verify.py` using Python 3.10+ and no external libraries. It checks total face counts, every matching pair, the complete oriented Hasse DAG, the exact seven-entry integer attaching vector, the original mod-two simplicial boundary ranks, and two independent symmetry-trace algorithms for every group element. The ranks of the original mod-two simplicial boundary maps from dimension one through five are respectively 23, 181, 567, 538, and 50; they yield reduced third Betti number 44. The program also carries out exact integer character inner products and checks nonnegative integral irreducible multiplicities. Its exact output is recorded in `torus_match_verification_output.txt`; the separate `symmetry_character.csv` provides machine-readable class traces.

## Relationship to prior work
Chauhan, Sharma and Shukla (first public version September 23, 2026) study \(P_3\square P_n\), explicitly defining both factors as **paths**, and establish connectivity and certain homology vanishing statements. Their Table 1 gives \(\widetilde H_3\cong\mathbb Z^9\) for the rectangular \(3\times4\) grid. The present graph is the different, 4-regular, periodic \(C_3\square C_4\), with 44 third-homology generators and a natural row-column symmetry character; neither the path-grid theorem nor its table implies this result. The earlier polygonal-line-tiling classifications concern chains of polygons and do not directly cover this toroidal product. A published computation of a *rectangular* grid's reflection quotient and studies of the *open neighborhood complex* of triangular cylinders also concern different simplicial complexes or underlying graphs.

## Limitations
The proof is an exhaustive finite computation for precisely twelve graph vertices; it does not classify \(C_m\square C_n\) for general parameters, nor assert a canonical equivariant wedge splitting, integral homology of the quotients, or uniqueness against all unpublished computations. Exact arithmetic and complete enumeration provide a self-contained certificate but not an independent mathematical audit. Jonsson's unpublished 2005 manuscript on grid matching complexes could not be inspected in full; an earlier implicit equivalent calculation cannot be categorically excluded. The quotient claims use rational coefficients only.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of 3 × n grid graphs*, arXiv:2609.27366v1, first publicly posted 2026-09-23, https://arxiv.org/pdf/2609.27366v1 . Especially Definitions 1.1 and the grid definition, Theorems 1.2–1.3, and Section 4/Table 1.
2. S. Goyal, S. Shukla, A. Singh, *Matching complexes of 3 × n grid graphs*, Electron. J. Combin. 28(4) (2021), #P4.16; withdrawn, with subsequent correction notice. https://doi.org/10.37236/10496 . Mentioned only as historical context, not as a proof premise.
3. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Math. 346 (2023), 113428. https://doi.org/10.1016/j.disc.2023.113428 .
4. J. Jonsson, *Matching complexes on grids*, unpublished manuscript (2005), cited in Chauhan–Sharma–Shukla; full scope unverified.
5. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (standard discrete-Morse reduction).
