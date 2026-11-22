# Component cuts and total metric resolution in rectangular rook graphs

## Finding

**Theorem.** Let \(m,n\geq2\) be integers, and let \(G=K_m\square K_n\). Identify a set of selected vertices \(S\subseteq V(G)=[m]\times[n]\) with the edge set of a spanning bipartite graph \(H_S\), whose row vertices are \(R_1,\ldots,R_m\), column vertices are \(C_1,\ldots,C_n\), and whose selected edges are \(R_iC_j\) for \((i,j)\in S\). Then \(S\) is a *total resolving set* (every pair of distinct vertices is distinguished by some selected vertex other than either endpoint) if and only if all three conditions hold:

1. For each row vertex \(R_i\), at most one column vertex \(C_j\) has \(N_{H_S}(C_j)\subseteq\{R_i\}\).
2. For each column vertex \(C_j\), at most one row vertex \(R_i\) has \(N_{H_S}(R_i)\subseteq\{C_j\}\).
3. No union of connected components of the *spanning* graph \(H_S\) (isolated root vertices included) contains exactly two row vertices and exactly two column vertices.

For the symmetric square case of order sixteen, \(G=K_4\square K_4\), the minimum size is \(\dim_t(G)=6\), and the **complete** polynomial enumerating total resolving sets by size is

\[
\begin{aligned}
T_G(z)={}&2016z^6+6912z^7+10872z^8+10960z^9\\
&+7960z^{10}+4368z^{11}+1820z^{12}\\
&+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]

Thus there are \(45{,}605\) total resolving sets, including \(2{,}016\) minimum ones. The latter form exactly five orbits under independent permutations of rows and columns, together with coordinate interchange; their sizes are \(96,192,576,576,576\). The set of all six-element subsets demonstrates that total resolution and weak \(2\)-resolution are not equivalent: precisely \(864\) satisfy both, \(1{,}152\) satisfy only total resolution, \(1{,}168\) satisfy only weak \(2\)-resolution, and \(4{,}824\) satisfy neither. Weak \(2\)-resolution here means the sum of absolute differences of distances to selected vertices is at least \(2\) for every pair, *including* possible endpoint contributions.

## Assumptions and scope

Graph distances are unweighted shortest-path distances in a finite, simple, undirected Cartesian product. A landmark may coincide with a queried endpoint for ordinary or weak resolving sets, but not for *total* resolving sets. The incidence graph \(H_S\) always retains all \(m+n\) row/column vertices, including isolates. All subsets and partitions in the square-board count are labelled; the five orbits are for the natural group \((S_4\times S_4)\rtimes C_2\) of order \(1{,}152\). The general characterization holds for all integers \(m,n\ge2\); the enumerative corollary is asserted only for the \(4\)-by-\(4\) board.

## Proof

For a cell \(x=(i,j)\) and \(w=(p,q)\),
\[
d_G(x,w)=[i\ne p]+[j\ne q].
\]
First compare two cells in the same row, \(x=(i,j)\) and \(y=(i,k)\) with \(j\ne k\). Their distances to \(w=(p,q)\) differ exactly when \(q\in\{j,k\}\). Excluding the two queried endpoints removes \((i,j)\) and \((i,k)\), so a permissible selected witness exists exactly when one of columns \(j,k\) contains a selected cell outside row \(i\). Requiring this for every two columns is equivalent to condition 1. Swapping row and column roles proves condition 2 for all same-column pairs.

Now let the queried cells \(x=(i,j)\), \(y=(k,\ell)\) differ in both coordinates. A selected third-party witness \((p,q)\) distinguishes them exactly in one of these two cases: \(p\in\{i,k\}\) and \(q\notin\{j,\ell\}\), or \(p\notin\{i,k\}\) and \(q\in\{j,\ell\}\). The cross-corners \((i,\ell)\), \((k,j)\) have equal distance to the targets; the diagonal corners are the forbidden endpoints. Consequently, a permissible witness is precisely an edge crossing the cut in \(H_S\) with shore \(U=\{R_i,R_k,C_j,C_\ell\}\). This cut is empty exactly when \(U\) is a union of complete connected components of \(H_S\). As \(i,k,j,\ell\) vary, these shores are exactly the subsets containing two row and two column roots, proving condition 3 and the all-parameter equivalence.

For \(4\)-by-\(4\), assume that a total resolving set has at most five cells. If a row is isolated in \(H_S\), condition 2 forces all other three rows to have degree at least two (a degree-one row would violate condition 2 along with the isolated row). Thus there are at least six selected edges, a contradiction; the analogous argument handles an isolated column. Otherwise all eight roots are nonisolated, and a graph with at most five edges has at least three connected components. A component with three vertices would be a two-edge star and would violate condition 1 or 2. A component with four vertices is either an offending two-row/two-column component or has three leaves on one side, violating condition 1 or 2. Every component therefore has either two or at least five vertices. At least three nontrivial components cannot include one of order five on only eight vertices. Hence all components are single edges; two of them unite to form a forbidden two-row/two-column shore. This proves \(\dim_t(G)\ge6\).

For sharpness, select the six cells \((1,1),(2,1),(2,2),(3,2),(3,3),(4,4)\). Its incidence graph consists of a six-vertex path and a disjoint edge. Its row and column leaves have distinct neighbors, and its only nontrivial component profiles are \((3,3)\) and \((1,1)\). The three conditions therefore hold, so \(\dim_t(G)=6\).

For the counting statements, `check_distance.py` builds every distance-pair witness mask and loops through each of the \(2^{16}=65{,}536\) vertex subsets. It also compares weak \(2\)-resolution with total resolution for all \(\binom{16}{6}=8{,}008\) six-sets. Row and column adjacent transpositions and coordinate interchange generate the full claimed symmetry group; breadth-first orbit enumeration gives the five orbit sizes. Independently, `check_components.py` implements the component-subset criterion and compares it against a separately written direct-distance test for *every* subset of boards of sizes \(2\times2\), \(2\times3\), \(3\times3\), \(3\times4\), and \(4\times4\). The complete verified cardinality counts are those in the displayed polynomial. These finite exhaustive verifications supply the numerically exact coefficients; the all-parameter characterization is established by the direct proof above, not by extrapolation from computation.

## Verification

Run `python3 check_distance.py` and `python3 check_components.py` with Python 3 and only its standard library. The expected terminal markers are `DIRECT_DISTANCE_CHECK_OK` and `COMPONENT_CHARACTERIZATION_CHECK_OK`. Both scripts assert exact coefficients; the distance program additionally asserts the weak-resolution contingency table and the five symmetry orbits. All source files and instructions required to reproduce the computation are included.

## Relationship to prior work

Hedetniemi, Laskar and Mulder (2020) introduced total metric resolution and treated Cartesian grids of *paths*, the three-cube and the Petersen graph, but not general products of two complete graphs. Cáceres and collaborators (2007) studied the *ordinary* metric dimension of Cartesian products, where queried endpoints are allowed as witnesses. Fernández and collaborators (2025) determined weak \(k\)-metric dimensions of square rook graphs; their weak criterion sums distance differences and permits endpoint contributions. The explicit overlap counts above show that their weak \(2\)-resolving family does not determine the total-resolving family, even at equal minimum cardinality. Related published enumerations of rook-graph domination and other incidence graph properties involve different constraints and do not imply the three-condition characterization. No claim of exhaustive bibliographic priority is made.

## Limitations

The structural equivalence applies to all two-factor complete-graph Cartesian products but does not itself give a closed minimization or generating-function formula for arbitrary \(m,n\). The exhaustive enumerator and orbit counts are only for the labelled \(4\)-by-\(4\) graph; the additional small-board checks validate the implementation but do not prove infinite statements. Publication priority and the finite computations have not received independent scholarly audit.

## References

1. S. T. Hedetniemi, R. C. Laskar and H. M. Mulder, *New resolvability parameters of graphs*, AKCE International Journal of Graphs and Combinatorics (published online May 4, 2020), https://doi.org/10.1016/j.akcej.2019.12.021 ; lawful full text https://repub.eur.nl/pub/126872/Repub_126872_O-A.pdf.
2. E. Fernández, S. Klavžar, D. Kuziak, M. Muñoz-Márquez and I. G. Yero, *On the weak \(k\)-metric dimension of Hamming graphs*, arXiv:2505.19642 (first version May 26, 2025), https://arxiv.org/abs/2505.19642.
3. J. Cáceres et al., *On the metric dimension of Cartesian products of graphs*, SIAM Journal on Discrete Mathematics 21 (2007), 423–441, https://doi.org/10.1137/050641867.
