# Centroidal sensing polynomials and exact optimal exchanges distinguish the Shrikhande and rook graphs

## Finding

Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Both are strongly regular with parameters \((16,6,2,2)\). Define the **centroidal sensing polynomial** of a finite connected graph by
\[
F_G(z)=\sum_{B\subseteq V(G):\ B\text{ centroidal locating}}z^{|B|}.
\]
A detector set \(B\) is centroidal locating when the ordered partitions of \(B\) obtained by sorting detector distances (with ties retained, and absolute distances forgotten) are distinct at all graph vertices, including the detector vertices themselves.

The complete polynomials for this exceptional strongly regular pair obey
\[
\begin{aligned}
F_S(z)={}&1728z^5+6736z^6+11152z^7+12846z^8+11440z^9\\
&+8008z^{10}+4368z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16},\\
F_R(z)={}&F_S(z)+12z^5(z+4)(z^2+4z+8).
\end{aligned}
\]
In particular, \(\operatorname{CD}(S)=\operatorname{CD}(R)=5\), with respectively \(1728\) and \(2112\) minimum centroidal bases. Every nine-element detector set works on either graph, whereas exactly \(24\) eight-element sets fail for \(S\) and \(12\) fail for \(R\). The latter twelve are precisely the unions of two full rows or two full columns of the four-by-four board.

If detectors are placed independently at each vertex with probability \(p\), then for every \(0<p<1\), the rook graph has strictly greater probability of centroidal identification. The exact difference, \(\Pr_R-\Pr_S\), equals
\[
12p^5(1-p)^8[p+4(1-p)]\,[p^2+4p(1-p)+8(1-p)^2]>0.
\]

Let \(\mathcal E(G)\) join minimum centroidal bases when one detector is replaced by a previously unselected detector. Both exchange graphs are connected and every vertex has eccentricity five. They have respectively \(1728\) vertices and \(22176\) edges for \(S\), and \(2112\) vertices and \(30624\) edges for \(R\). Thus both have radius and diameter five, despite different exact optimizer counts and exchange edge counts.

## Assumptions and scope

All graphs are finite, simple, undirected, loopless and unweighted. Write \(V=\{(i,j):i,j\in\mathbb Z/4\mathbb Z\}\), with the vertex code \(4i+j\). In \(R\), distinct pairs are adjacent when they share a row or column. In \(S\), two vertices are adjacent exactly when their coordinate difference lies in
\[
\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
Both have 16 vertices, degree six and exactly two common neighbors for every two distinct vertices, and therefore diameter two. Set \(d_G(x,b)\) to the ordinary graph distance. The rank signature \(\rho_B(x)\) is the ordered list of nonempty level sets
\[
\bigl(\{b\in B:d_G(x,b)=r\}:r=0,1,2\bigr),
\]
with empty levels removed. The ordering is retained, but the numerical labels \(r\) are not part of the signature. A centroidal set is one for which the 16 signatures are pairwise distinct. Polynomial coefficients count *unlabelled detector subsets on the fixed labelled graph*, not colourings or graph-isomorphism types. The exchange graph permits replacement by any unoccupied vertex; adjacency in the underlying graph is not required.

## Proof

**Graph model and rank signatures.** The explicit adjacency rules give row sums six. Directly evaluating every pair of distinct vertices yields two common neighbors, whether adjacent or not. Hence all nonadjacent vertices have distance two. For any detector set \(B\), the ordered partition \(\rho_B(x)\) defined above is precisely the relative-distance observation in the foundational definition. Equivalently, for each pair of selected sensors \(b,c\), record one of three outcomes \(d_G(x,b)<d_G(x,c)\), equality, or \(>\). The collection of pairwise outcomes determines exactly the same ordered partition, and conversely. This equivalence is immediate by recovering ties and the induced total ordering of tied classes. Crucially, distinguishing sensor vertices as well as exterior vertices is required.

**Exhaustive certificate for all coefficients.** For each of the two explicit graphs, enumerate the integer masks \(m\) from \(0\) through \(2^{16}-1\). Bit \(j\) indicates whether detector \(j\) belongs to \(B_m\). Construct all sixteen rank signatures from the graph-distance matrix, insert them into a set, and accept \(m\) exactly when the set has sixteen elements. Increment the coefficient indexed by the bit count of \(m\). The complete source `check_cpp.cpp` implements this enumeration directly using ordered partitions and breadth-first graph distances. The independent `check_python.py` instead constructs the same graphs from coordinate adjacency formulas, uses the diameter-two adjacency/nonadjacency distinction, and builds all pairwise comparison-sign vectors without forming distance partitions or using the C++ path computation. Both independently enumerate every one of the \(65536\) possible subsets for each graph; the resulting coefficients are:

| Cardinality \(k\) | \(F_S[z^k]\) | \(F_R[z^k]\) |
|---:|---:|---:|
| 0–4 | 0 | 0 |
| 5 | 1728 | 2112 |
| 6 | 6736 | 7024 |
| 7 | 11152 | 11248 |
| 8 | 12846 | 12858 |
| 9 | 11440 | 11440 |
| 10 | 8008 | 8008 |
| 11 | 4368 | 4368 |
| 12 | 1820 | 1820 |
| 13 | 560 | 560 |
| 14 | 120 | 120 |
| 15 | 16 | 16 |
| 16 | 1 | 1 |

No detector sets of size less than five pass, and some of size five pass, establishing the common centroidal dimension. Subtracting the coefficient arrays and factoring gives the displayed polynomial identity. For each \(k\ge9\), the count is \(\binom{16}{k}\), so all such subsets pass. Among the \(\binom{16}{8}=12870\) eight-element subsets exactly \(24\) and \(12\) fail, respectively. In the rook graph, the twelve unions of two full rows or of two full columns fail because two vertices in a common unselected column or row have the same relative-distance partition; the complete enumeration shows no other failures of size eight. This establishes the sharp universal sensor budget nine, without claiming it is sharp for other graph families.

**Minimal obstructions.** A failing set is inclusion-maximal when adding any one absent detector makes it work. Testing all failing masks and all their immediate supersets gives the following complete obstruction-size distributions: for \(S\), \(48\) of size four, \(24\) of size six, \(96\) of size seven, and \(24\) of size eight; for \(R\), \(144\), \(72\), \(96\), and \(12\) respectively. The monotonicity of centroidal detection under adding detectors follows directly by restricting the more detailed relative-distance comparisons to the old detector subset. Therefore testing immediate additions suffices to characterize inclusion-maximal failures.

**Exact exchange structure.** Retain precisely the accepted masks of bit count five. For each such mask enumerate all replacements of a selected bit with an unselected bit and retain the replacements belonging to the same accepted family. Each undirected edge is counted twice among outgoing choices. The complete graph has \(22176\) edges in the Shrikhande case and \(30624\) in the rook case. A component search shows one component in each case. Breadth-first distance searches from *every* accepted five-mask show eccentricity five for every vertex, proving both radius and diameter are five. The independently implemented Python verifier reconstructs this entire exchange graph and confirms the same connectedness, edge counts and eccentricity census.

**Reliability comparison.** A sensor subset \(B\) is selected with probability \(p^{|B|}(1-p)^{16-|B|}\), whence the successful-placement probability equals \((1-p)^{16}F_G(p/(1-p))\) for \(0\le p<1\). Substitute the exact polynomial difference and clear powers of \(1-p\). This yields the displayed factored, strictly positive expression for every \(0<p<1\). At \(p=0\) or \(p=1\), both graph models have equal success probability.

## Verification

The package contains complete independent source files `check_cpp.cpp` and `check_python.py`. Run with a standard compiler and Python 3:

```
c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp
./check_cpp
python3 check_python.py
```

The C++ checker constructs all-pairs distances with sixteen breadth-first searches per graph and uses ordered partitions. The Python checker computes all pairwise detector rankings from the adjacency relation instead; neither program reads cached tables or data from the other. Both assert the full 17-coefficient arrays, all inclusion-maximal failure sizes, both exchange edge totals, connectedness, and eccentricity five of every optimal set. Each verifies degree six and exactly two common neighbors for all distinct vertex pairs. The complete finite proof derives from the explicit exhaustive search space and checked Boolean predicates, not from a sample or asymptotic extrapolation.

## Relationship to prior work

Foucaud, Klasing and Slater introduced centroidal bases and the definition by relative rankings, proved general comparison bounds with metric and locating-domination dimensions, and examined diameter-two bounds. This foundation is explicitly credited; it does not assert either exact polynomial or the present pair's exchange structure. Gravier, Parreau, Rottey, Storme and Vandomme study identifying codes of vertex-transitive and strongly regular graphs, defined by distinct closed-neighborhood intersections, a different observational model. A published classification of minimum *global locating-dominating* codes for the same Shrikhande–rook pair counts \(1488\) versus \(1872\) minimum codewords; those codes require nonempty, nonfull, and pairwise distinct exterior open-neighborhood traces. Their minimal-code counts and exchange graphs do not determine the centroidal signatures or these all-cardinality polynomials. The comparison involves mathematical predicates, not merely differing names. No previously checked statement was found that implies the present exact centroidal classification.

## Limitations

All enumerative and reconfiguration results concern exactly these two sixteen-vertex graphs, not all strongly regular graphs. The graph-specific enumeration is exhaustive and independently checked by two implementations, but no external independent mathematical audit has been performed. Historical novelty is not established by a failed search: obscure earlier computations, private theses and unindexed sources might contain equivalent counts. The graph classification does not claim any sharp asymptotic sensor threshold for larger graph families. The value of nine is a *worst-case* deterministic budget, not the minimum number of detectors needed in one carefully chosen placement.

## References

1. F. Foucaud, R. Klasing and P. J. Slater, *Centroidal bases in graphs*, arXiv:1406.7490v1 (first public 2014-06-29), later *Networks* 64(2) (2014), 96–108. https://arxiv.org/abs/1406.7490
2. S. Gravier, A. Parreau, S. Rottey, L. Storme and E. Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, arXiv:1411.5275 (first version 2014), *Electronic Journal of Combinatorics* 22(4) (2015), P4.6. https://arxiv.org/abs/1411.5275
3. *Minimum global locating-dominating codes distinguish the Shrikhande and four-by-four rook graphs*, public mathematical-result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-minimum-global-locating-dominating-codes-distinguish-the-shrikha--b1d04ec503f1
