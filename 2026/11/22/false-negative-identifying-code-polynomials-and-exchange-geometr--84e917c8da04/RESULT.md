# False-negative identifying codes and exchange geometry of the Shrikhande–rook pair

## Finding

Let \(R=K_4\square K_4\) be the sixteen-vertex rook graph, and let \(S\) be the Shrikhande graph. Both are strongly regular with parameters \((16,6,2,2)\), but are nonisomorphic. For a graph \(G\), let \(D_G(z)=\sum_C z^{|C|}\), where the sum ranges over **error-detecting identifying codes** \(C\) as defined in the next section (one false-negative detector report is permitted). Then

\[
\begin{aligned}
D_R(z)&=720z^{10}+1920z^{11}+1496z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16},\\
D_S(z)&=256z^{10}+1392z^{11}+1424z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]

Both minimum cardinalities equal \(10\); the respective numbers of optimum labeled sensor sets are \(720\) and \(256\). Under full graph automorphisms, the rook minima form three orbits of sizes \(144,288,288\), whereas Shrikhande minima form five orbits of sizes \(16,48,48,48,96\).

Form the **minimum-code exchange graph** by joining two optimum codes if exactly one chosen sensor is replaced by one previously unchosen vertex. The rook exchange graph is connected on \(720\) vertices, with \(3312\) edges, degree distribution \(144\) of degree \(6\) and \(576\) of degree \(10\), and diameter \(6\). The Shrikhande exchange graph has \(624\) edges and exactly \(23\) connected components: \(16\) isolates, six components of order \(16\) each isomorphic to \(K_4\square K_4\), and one component of order \(144\). Its degree distribution is \(16\) of degree \(0\), \(48\) of degree \(4\), \(96\) of degree \(5\), and \(96\) of degree \(6\).

## Assumptions and scope

Vertices of both graphs are indexed by \((r,c)\in\mathbb Z_4^2\), represented in certificates by \(i=4r+c\). Distinct rook vertices are adjacent when their first or second coordinates agree. Distinct Shrikhande vertices are adjacent when their difference belongs to
\[
T=\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\subseteq\mathbb Z_4^2.
\]

Write \(N_G[v]\) for the closed neighborhood of \(v\). A detector set \(C\subseteq V(G)\) is error-detecting identifying if, for every vertex \(v\),
\[|N_G[v]\cap C|\ge2,\]
and, for every distinct pair \(u,v\),
\[
\max\bigl(|(N_G[u]\setminus N_G[v])\cap C|,|(N_G[v]\setminus N_G[u])\cap C|\bigr)\ge2.
\]
This is the asymmetric \(2^{\#}\)-distinguishability requirement of Jean and Seo (2022), not the weaker one-erasure/redundant condition based on a symmetric difference. All subsets, graph vertices and sensor placements are labeled. No quotient is taken in the displayed polynomials.

## Proof

**Reduction to a finite forbidden-four-set hypergraph.** Both graphs have closed neighborhoods of size \(7\). For adjacent \(u,v\), the two disjoint directed differences \(A=N[u]\setminus N[v]\) and \(B=N[v]\setminus N[u]\) each have cardinality \(3\). For nonadjacent \(u,v\), they each have cardinality \(5\). Put \(O=V(G)\setminus C\). When \(|O|\le7\), a nonadjacent pair cannot violate asymmetric separation: it would require omitting at least four vertices in each of two disjoint five-element sets. An adjacent pair violates separation precisely when \(O\) contains two vertices of each of \(A,B\). Thus let
\[
\mathcal B_G=\bigcup_{uv\in E(G)}\{X\cup Y:X\in\tbinom{A}{2},\;Y\in\tbinom{B}{2}\},
\]
where the two differences correspond to the edge \(uv\). Then, for \(|O|\le7\), separation holds if and only if \(O\) contains no member of \(\mathcal B_G\). The two-dominating requirement holds if and only if \(|O\cap N[v]|\le5\) for every \(v\). These are exact equivalences, not approximate conditions.

**Exhaustive finite step.** For each graph, construct its sixteen closed-neighborhood masks directly from the adjacency rule, construct all \(48\) adjacent-pair contributions to \(\mathcal B_G\), remove duplicate four-sets, and iterate each of the \(\sum_{j=0}^{7}\binom{16}{j}\) omitted sets of size at most seven. The resulting counts of distinct forbidden four-sets are \(|\mathcal B_R|=324\) and \(|\mathcal B_S|=396\). Counts of admissible omitted sets in sizes \(0,1,2,3,4,5,6\) are, respectively,
\[
R:(1,16,120,560,1496,1920,720),\qquad
S:(1,16,120,560,1424,1392,256).
\]
No admissible seven-omission set exists. More precisely, in the rook graph the only sixteen seven-subsets avoiding the forbidden-four-set hypergraph are the sixteen closed neighborhoods; each fails two-domination. In the Shrikhande graph every seven-subset already contains a forbidden four-set. Since adding omissions cannot restore either condition, **no set omitting more than seven vertices is admissible**. This proves the minimum and both complete polynomials. The source `code/obstruction_exchange.py` performs precisely this finite step and checks its boundary assertions; the independently structured complete-enumeration sources `code/direct_checker.cpp` and `code/set_checker.py` verify the results by the original neighborhood conditions on all \(2^{16}\) detector masks. The finite range is exhaustive, and no claim about an unexamined infinite family is made.

**Automorphism orbits.** For the rook graph, any automorphism permutes the eight maximal four-cliques (four rows and four columns), giving the full group \((S_4\times S_4)\rtimes C_2\) of order \(1152\). For Shrikhande, its six neighbors of one vertex induce a six-cycle; the nine remaining vertices are distinguished by their two neighbors on this cycle. Thus the vertex stabilizer has order at most \(12\). Exactly twelve invertible \(\mathbb Z_4\)-linear maps preserve \(T\), and the sixteen translations are automorphisms; therefore these \(192\) affine maps constitute the full automorphism group. Applying the explicitly enumerated permutations to the admissible ten-vertex masks proves the orbit sizes above. Representatives encoded as sixteen-bit code masks are
\[
R:\ 0x177e\ (144),\quad 0x17ee\ (288),\quad 0x37cd\ (288);
\]
\[
S:\ 0x3a6f\ (16),\quad 0x07fe\ (48),\quad 0x0f3f\ (48),\quad 0x1f1f\ (48),\quad 0x07f7\ (96).
\]
The hexadecimal values in these two displays are literal machine labels, not algebraic variables.

**Exchange graph.** For every optimum mask, exchange neighbors are computed by deleting one set bit and setting one unset bit, retaining precisely the masks in the optimum family. Breadth-first components give the stated sizes, edges and degrees. In the Shrikhande case, an explicit adjacency-preserving sixteen-mask bijection from \(K_4\square K_4\) onto one size-sixteen exchange component is embedded in `code/obstruction_exchange.py`; applying the full automorphism group carries this component to the other five and proves all six isomorphisms. The rook exchange diameter is obtained by breadth-first distances from all its \(720\) vertices (the value is \(6\)); diameter is not needed for the Shrikhande component-count claim.

## Verification

All three standalone programs use only exact integer/set operations and no external graph data. The complete-enumeration programs independently generate the two graphs and test every detector subset. The obstruction program uses forbidden four-subsets, a different acceptance criterion justified above, and also checks the full automorphism lists, orbit representatives, exchange adjacency, component sizes, and the explicit rook-component isomorphism. In `census_certificate.json`, coefficients and finite structural counts are included in machine-readable form. To reproduce, run (from the extracted artifact directory):

```sh
g++ -O2 -std=c++17 code/direct_checker.cpp -o direct_checker
./direct_checker
python3 code/set_checker.py
python3 code/obstruction_exchange.py
```

The programs have all been executed and produced the exact asserted polynomial, forbidden-set, orbit and component counts. The two full-set enumerations agree independently with the complementary omission obstruction method.

## Relationship to prior work

Jean and Seo's work on error-detecting identifying codes, first publicly posted 2022-08-11, gives the necessary-and-sufficient two-domination and asymmetric-separation criterion, and general results for other graph classes; it does not tabulate these two graphs or their optimum exchange configurations. Gravier and collaborators (2015) treat ordinary identifying codes and fractional bounds in vertex-transitive and strongly regular graphs; their sections on Cartesian products of cliques concern the weaker ordinary notion. A separate published result on optimal ordinary identifying-code exchange geometry of the Shrikhande and rook graphs treats codes without false-negative tolerance, so its minima and exchange graphs are distinct from those above. Those works are credited as premises or comparators, not claimed as discoveries here.

## Limitations

This is an exact finite theorem for two specified sixteen-vertex graphs only; it does not assert that the strongly regular parameters determine these polynomials or that the same behavior extends to larger graph families. The orbital classification uses the full automorphism groups justified above, whereas exchange edges allow arbitrary one-for-one replacements (not necessarily graph-edge slides). Historical priority cannot be fully ruled out for unindexed data tables or inaccessible related notes. Independent external validation has not been performed.

## References

- D. C. Jean and S. J. Seo, *Optimal Error-detection System for Identifying Codes*, arXiv:2208.06052, initially posted 2022-08-11; Theorem 2.1 and Section 4. https://arxiv.org/abs/2208.06052
- S. Gravier, A. Parreau, S. Rottey, L. Storme, and E. Vandomme, *Identifying Codes in Vertex-Transitive Graphs and Strongly Regular Graphs*, Electronic Journal of Combinatorics 22(4), P4.6 (2015). https://doi.org/10.37236/5256
- D. C. Jean and S. J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685 (2021). https://arxiv.org/abs/2112.01685
