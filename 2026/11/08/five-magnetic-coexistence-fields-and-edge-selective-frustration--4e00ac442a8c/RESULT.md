# Five magnetic coexistence fields and edge-selective frustration in the Chvátal Potts antiferromagnet

## Finding
On the twelve-vertex Chvátal graph, the three-state antiferromagnetic Potts ground-state energy in a uniform field favoring one labeled color is exactly
\[
\frac{E_0(h)}{J}=\min\{4,\ 1-3x,\ 1-5x,\ 2-6x,\ 8-8x,\ 24-12x\},\qquad x=\frac hJ.
\]
There are precisely five coexistence fields \(x=-1,0,1,3,4\), separating six intervals whose favored-color occupancies are \(0,3,5,6,8,12\) and labeled degeneracies are respectively \(4,96,96,64,320,1\). The coexistence degeneracies, in increasing field order, are \(256,504,160,832,929\).

At zero field the minimum is one monochromatic edge, achieved by exactly \(504\) labeled three-color assignments. In the explicit vertex labeling below, four edges can **never** be the unique monochromatic edge of such a minimum-energy assignment: \((2,3),(6,11),(7,8),(9,10)\). The other twenty edges support unique frustration with counts given in `EDGE_DEFECT_COUNTS.csv`. Thus one bond of frustration is unavoidable but cannot be located arbitrarily, despite the graph being regular.

## Assumptions and scope
The graph has vertices \(\{0,1,\ldots,11\}\) and the following twenty-four undirected edges:

`(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3) (2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10) (5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)`.

This is a standard labeling of the Chvátal graph, the smallest triangle-free, four-regular, four-chromatic graph. The spins \(\sigma_v\) take one of three labeled values \(\{0,1,2\}\); coupling \(J>0\) is uniform, and the longitudinal field \(h\in\mathbb R\) is arbitrary. The energy is
\[
H_{J,h}(\sigma)=J\sum_{\{u,v\}\in E}\mathbf1_{\sigma_u=\sigma_v}
-h\sum_{v\in V}\mathbf1_{\sigma_v=0}.
\]
All degeneracies count distinct labeled spin assignments. This is a finite graph at zero temperature; it is not a thermodynamic-limit phase transition.

## Proof
For \(k\in\{0,\ldots,12\}\), let \(e_k\) be the minimum number of monochromatic edges among all assignments with precisely \(k\) vertices of color zero, and let \(c_k\) be the number of assignments attaining that minimum. The exact complete census is:

| \(k\) | \(e_k\) | \(c_k\) |
|---:|---:|---:|
| 0 | 4 | 4 |
| 1 | 3 | 32 |
| 2 | 2 | 124 |
| 3 | 1 | 96 |
| 4 | 1 | 312 |
| 5 | 1 | 96 |
| 6 | 2 | 64 |
| 7 | 5 | 448 |
| 8 | 8 | 320 |
| 9 | 12 | 416 |
| 10 | 16 | 168 |
| 11 | 20 | 24 |
| 12 | 24 | 1 |

This is a finite exhaustive mathematical proof: `verify.py` enumerates each of the \(3^{12}=531441\) assignments once in two distinct bijective representations. The first enumerates all ternary spin words and directly sums edge conflicts. The second chooses the subset \(S\) of color-zero vertices and independently enumerates binary colorings of \(V\setminus S\). In the second representation, bonds internal to \(S\) are automatically conflicted, and bonds crossing from \(S\) to its complement never are. Each algorithm computes the minimum and attaining multiplicity for every \(k\), and each independently counts every possible unique frustrated edge. Their exact-integer results agree with the displayed table and both standalone CSV outputs.

Because each spin assignment belongs to exactly one \(k\)-sector, minimizing over all spins is equivalent to minimizing \(e_k-kx\) over thirteen integer sector minima. The successive differences of the displayed \(e_k\) are
\[
(-1,-1,-1,0,0,1,3,3,4,4,4,4).
\]
They are nondecreasing. Hence the lower convex envelope has vertices \(k=0,3,5,6,8,12\), and all intermediate sectors lie exactly on its line segments. Its slopes are \(-1,0,1,3,4\), giving exactly the five stated coexistence fields and the six strict-energy branches. At each coexistence field all sectors lying on the corresponding hull segment tie, and summing their \(c_k\) values gives the five stated degeneracies. For example, at \(x=4\), occupancies \(8,9,10,11,12\) tie, with total \(320+416+168+24+1=929\).

At \(x=0\), the global minimum is \(1\) and it occurs in exactly the sectors \(k=3,4,5\). Consequently the zero-field degeneracy is \(96+312+96=504\). The same exhaustive enumerations count the number of assignments with exactly one monochromatic edge at each specified bond. The four zero entries in `EDGE_DEFECT_COUNTS.csv` prove the edge-selective obstruction. Since every assignment contributes its unique conflicted bond exactly once, the twenty-four bond counts sum to \(504\).

## Verification
Run `python3 verify.py` from a directory containing the delivered standalone source file. Python's standard library suffices. It checks the graph size, regularity and triangle-free property; enumerates all \(531441\) states twice using different encodings; compares all thirteen sector minima, all multiplicities, and twenty-four individual defect-edge counts against the independently supplied exact tables; and uses `fractions.Fraction` to test all field crossings, strict regimes, and degeneracies without floating-point comparisons. Reproducing the two CSV files is described in their headers.

## Relationship to prior work
Chvátal's 1970 construction provides the natural smallest triangle-free four-regular four-chromatic host graph; its graph structure and chromatic number are also described in MathWorld and the NetworkX graph reference. Shrock and Xu (arXiv:1009.1182, initial version 2010-09-07) give a general field-dependent Potts partition-function framework. Their inspected full text treats families such as trees, lattice strips and wheels, but does not tabulate the Chvátal three-color frustrated field sectors or one-bond location counts. Its proper-coloring specialization vanishes here because the Chvátal graph is four-chromatic; the positive one-bond frustrated sector requires the finite-temperature expansion or direct enumeration. Björklund and coauthors (arXiv:0711.2585, initial version 2007-11-16) give general graph Tutte-polynomial algorithms and concrete graph computations; their inspected full text does not provide the present single-color field envelope or localized frustration census. General finite-graph partition-function identities provide computational methods, not the evaluated Chvátal benchmark shown here. Exact field calculations on other four-chromatic graphs, including the eleven-vertex Grötzsch graph, do not imply these twelve-vertex counts.

## Limitations
The result concerns only the specified finite Chvátal graph, precisely three colors, uniform positive antiferromagnetic bond penalty, and a field favoring one color. No finite-temperature or infinite-graph statement is made. Exact enumeration is sufficient for these finite quantified claims but does not by itself establish the historical novelty of the evaluated values. Earlier graph-coloring work already implies four-chromaticity and may record individual edge-deletion obstructions; an overlooked exact field enumeration or complete edge-criticality table remains possible. The 1970 original graph article's complete text could not be inspected; only its verified bibliographic attribution and later graph accounts were available. Independent scientific review has not been performed.

## References
- V. Chvátal, “The smallest triangle-free 4-chromatic 4-regular graph,” *Journal of Combinatorial Theory* 9 (1970), 93–94. DOI: 10.1016/S0021-9800(70)80057-6.
- R. Shrock and Y. Xu, “Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings,” arXiv:1009.1182 (first version 2010-09-07), https://arxiv.org/abs/1009.1182.
- A. Björklund, T. Husfeldt, P. Kaski, and M. Koivisto, “Computing the Tutte polynomial in vertex-exponential time,” arXiv:0711.2585 (first version 2007-11-16), https://arxiv.org/html/0711.2585v4.
- E. W. Weisstein, “Chvátal Graph,” MathWorld, https://mathworld.wolfram.com/ChvatalGraph.html.
- NetworkX, `chvatal_graph` documentation, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.chvatal_graph.html.
