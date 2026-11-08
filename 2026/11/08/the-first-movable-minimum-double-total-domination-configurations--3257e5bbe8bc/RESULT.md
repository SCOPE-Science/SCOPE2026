# The first movable minimum double-total domination configurations in rook graphs

## Finding

For the rectangular rook graph \(R_{n,m}=K_n\square K_m\), let a *double-total dominating set* (2TDS) be a vertex subset \(S\) for which every vertex, whether selected or not, has at least two neighbours in \(S\). The one-exchange graph has as vertices the minimum-cardinality 2TDS sets, with an edge for replacing one selected square by one unselected square while preserving minimum 2TDS. *Token sliding* additionally requires the two squares to be adjacent in the rook graph; *token jumping* does not.

**Theorem.** On the \(4\times6\) rook board, the minimum size is \(8\), with exactly \(3189\) minimum 2TDS sets. Both token-jumping and token-sliding reconfiguration graphs coincide. Each consists of \(2109\) isolated vertices and \(20\) pairwise disjoint, mutually isomorphic connected components with \(54\) vertices and \(144\) edges each. Every nontrivial component has diameter \(5\), with \(36\) degree-six and \(18\) degree-four vertices. There are therefore exactly \(2880\) reconfiguration edges. The nontrivial components are naturally indexed by the \(\binom63=20\) choices of three occupied columns.

Among nondegenerate rectangular rook graphs \(R_{n,m}\), \(2\le n\le m\), with \(nm\le24\), the \(4\times6\) graph is the **only** one with any exchange between minimum double-total dominating sets. In particular, it is the first mobility instance when boards are ordered by their number of cells.

## Assumptions and scope

Every board square \((i,j)\), \(0\le i<n\), \(0\le j<m\), is a graph vertex. Two distinct squares are adjacent exactly when they have a common row or column. All configurations are *labeled*: rows and columns are fixed and distinct, and no quotient by symmetry is taken. Exchanges replace exactly one member of \(S\) by exactly one member of its complement. All assertions concern 2TDS sets of **minimum possible cardinality**, not arbitrary inclusion-minimal 2TDS sets.

Write \(x_{ij}\in\{0,1\}\) for selection, and \(r_i=\sum_j x_{ij}\), \(c_j=\sum_i x_{ij}\). A set is 2TDS if and only if
\[
 r_i+c_j-2x_{ij}\ge2 \quad\text{for every }(i,j).
\]
This is because the square sees every other square in its row or column, but not itself.

## Proof

**1. Minimum cardinality.** Two full columns give a feasible eight-square configuration. Suppose at most seven squares were selected. If some column were empty, the displayed inequality would force every one of the four rows to contain at least two selected squares, a contradiction. If no column is empty, the six positive column sums total at most seven, so every column sum is at most two and at least one is one. A row of sum zero violates the inequality in a singleton column. A row of sum one has its selected square in a column of sum at most two, so the inequality there is at most \(1+2-2=1\). Thus all four rows have sum at least two, again a contradiction. Therefore the minimum is eight.

**2. Classification and exact count.** If an eight-square configuration contains a zero column, all four row sums must be exactly two. Every occupied column must contain at least two squares, and these conditions are also sufficient. There are therefore two, three or four occupied columns:

* With two occupied columns they are both full: \(\binom62=15\) configurations.
* With three occupied columns, each row omits one of these columns. Every column must be omitted by at most two rows. The omitted-count partitions are \((2,2,0)\), with \(18\) assignments, and \((2,1,1)\), with \(36\), giving \(54\binom63=1080\) configurations.
* With four occupied columns, every active column has sum two. The corresponding bipartite graph on four row vertices and four column vertices is two-regular, so it is either one eight-cycle (\(72\) labeled structures) or two four-cycles (\(18\)). This gives \(90\binom64=1350\) configurations.

If no column is empty, six positive column sums totaling eight have profile \((2,2,1,1,1,1)\) or \((3,1,1,1,1,1)\). The first is impossible: a row of sum zero or one cannot occur, so every row has sum two, incompatible with a selected square in a singleton column. In the second profile, any row of sum one must occupy the unique triple column, a row of sum two is impossible, and all other rows have sum at least three. The only row profiles are \((5,1,1,1)\) or \((3,3,1,1)\). In the first there are \(4\cdot6=24\) configurations: choose the five-square row and the triple column, and place the other three selections in that column. In the second, choose the two three-square rows, the triple column, which of these high rows belongs to the triple column, and which two of the five singleton columns the same high row occupies. The count is \(\binom42\cdot6\cdot2\cdot\binom52=720\). Every described configuration satisfies the domination inequality. The five structural families (six degree-profile classes) contain
\[
15+1080+1350+24+720=3189
\]
configurations.

**3. Exchanges and frozen classes.** A single exchange changes at most two row sums, each by one. The classified no-zero-column row profiles \((5,1,1,1)\) and \((3,3,1,1)\) cannot be reached in a single exchange from \((2,2,2,2)\), or vice versa. Neither no-zero-column profile can be changed to another allowable no-zero-column profile by transferring between different rows. Consequently any legal exchange must stay in the same row. A within-row exchange from a no-zero-column configuration changes the column profile to one forbidden above, or creates a zero column without changing the requisite row profile, so these \(744\) configurations are frozen.

In zero-column configurations, the same-row condition preserves row sums. A move into an empty column creates a selected singleton column, violating the 2TDS inequality, so the set of occupied columns is invariant. In the two-column class there is no unselected square in an occupied column. In the four-column class removing a selected square reduces a column from two to one, violating the inequality. Both classes are frozen. For three occupied columns, each row selects exactly two of the three; changing the omitted column in one row is valid precisely if no column becomes omitted by more than two rows. These are all allowable exchanges, and because they stay in the same row **every jump is a rook-edge slide**.

**4. The universal \(54\)-vertex component.** Fix a triple of occupied columns and label them \(0,1,2\). Every state is uniquely a word \((a_1,a_2,a_3,a_4)\in\{0,1,2\}^4\) in which each symbol occurs at most twice; \(a_i\) is the column omitted by row \(i\). Two words are adjacent exactly when they differ in one coordinate and the resulting word still has all symbol multiplicities at most two. There are \(36\) words of multiplicity pattern \((2,1,1)\), each of degree six, and \(18\) of pattern \((2,2,0)\), each of degree four. Hence there are \((36\cdot6+18\cdot4)/2=144\) edges. The standalone `verify_structure.py` performs a complete breadth-first search of all \(54\) explicitly defined words and verifies that the graph is connected and has diameter five. In particular the pair \((0,0,1,1)\), \((1,1,0,0)\) has distance five. Since an exchange cannot change the occupied column triple, the \(\binom63=20\) copies are different components. There are \(15+1350+744=2109\) isolated configurations.

**5. Earliest board size.** The standalone `verify_direct.py` enumerates *all* candidate subsets by cardinality until it reaches the minimum, for every \(2\le n\le m\) with \(nm\le24\). It builds each exact one-exchange graph. The complete finite check finds zero exchanges in every such board except \((n,m)=(4,6)\). This last statement is a rigorously finite enumeration (not an infinite classification of all rook graphs).

## Verification

Both embedded programs use Python 3 standard-library modules only, and run independently using `python verify_direct.py` and `python verify_structure.py`. `verify_direct.py` tests the definition against all \(\binom{24}{8}=735471\) eight-element choices on the four-by-six board, reconstructs all exchanges, checks their slides, decomposes the graph and performs exhaustive all-source breadth-first searches in the nontrivial components. It also checks every nondegenerate rook board with at most 24 squares. `verify_structure.py` generates the five structural families without enumerating all eight-subsets, verifies the domination inequalities, and independently computes degrees, edges, connectivity and diameter of the 54-state omission-word graph. Captured outputs are supplied in `direct_output.txt` and `structure_output.txt`.

The computation establishes finite exact results. No claim is made about boards having more than 24 vertices except the explicitly analyzed \(4\times6\) graph, and no computer check is substituted for an infinite-family proof.

## Relationship to prior work

Henning and Kazemi introduced the general \(k\)-tuple total domination framework. Kazemi, Pahlavsay and Stones established exact minimum *cardinalities* for rook graphs in their preprint first submitted 28 September 2015; their Proposition 1 gives the value eight for \(K_4\square K_6\), and Table 2 gives sample minimum matrices. Their equation (3) is the row/column criterion used here. Their component switchings replace entire submatrices, not a single selected square. This result establishes a different, finer object: the complete labeled minimum-configuration classification, total count, and strict single-token reconfiguration metric for the smallest mobile rook board.

Ordinary domination, paired domination, and total \([1,2]\)-domination impose different neighbor constraints; none is automatically interchangeable with the lower-bound-two open-neighborhood condition here. Also, a more general result supplying only a minimum cardinality does not imply the count or exchange graph.

## Limitations

The exact historical priority of the configuration counts and mobility graph has not been independently certified. An unindexed enumeration or older treatment of identical token exchanges could overlap. The novelty comparison is based on inspected accessible primary material, targeted literature searches, mathematical-record searches, and accessible prior research claims. The stated minimal-area cutoff is restricted to \(2\le n\le m\) and \(nm\le24\). All computational verification uses exact integer arithmetic but remains a self-review; independent external validation has not been performed.

## References

1. A. P. Kazemi, B. Pahlavsay, R. J. Stones, *Cartesian product graphs and \(k\)-tuple total domination*, arXiv:1509.08208, first posted 2015-09-28, especially Section 3, Proposition 1, and Table 2. https://arxiv.org/abs/1509.08208
2. M. A. Henning, A. P. Kazemi, *\(k\)-tuple total domination in graphs*, Discrete Applied Mathematics 158 (2010), 1006–1011. https://doi.org/10.1016/j.dam.2010.01.009
