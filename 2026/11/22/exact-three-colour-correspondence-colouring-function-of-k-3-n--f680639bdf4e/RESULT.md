# Exact three-colour correspondence-colouring function of \(K_{3,n}\)

## Finding
For every integer \(n\ge1\), define \(P_{DP}(K_{3,n},3)\) as the minimum number of independent transversals among all three-fold correspondence (DP) covers of \(K_{3,n}\). The exact values are
\[
P_{DP}(K_{3,n},3)=\begin{cases}
24&n=1,\\
18&n=2,\\
14&n=3,\\
6&n=4,\\
5&n=5,\\
0&n\ge6.
\end{cases}
\]
The first five positive values refine the previously known sharp non-colourability threshold at six right vertices. The six-vertex threshold itself is not a new claim.

## Assumptions and scope
The graphs \(K_{3,n}\) are finite, simple, and complete bipartite, with one part of size three and the other of size \(n\ge1\). A three-fold DP cover gives three available representatives at each vertex; for every edge a matching joins incompatible representatives. A DP colouring is an independent transversal selecting exactly one representative at each graph vertex. The DP colour function takes the minimum over every such cover, including covers with partial matchings. Each matching can be completed to a perfect matching, which cannot increase the number of independent transversals. Thus it suffices to minimize over full, permutation-labelled covers.

## Proof
Label the three left vertices \(u_0,u_1,u_2\), and every three-element fibre by \(\{0,1,2\}\). In a full cover, the matching between \(u_0\) and each right vertex is normalized to the identity by relabelling that right fibre. The remaining matchings at right vertex \(v_i\) are permutations \((p_i,q_i)\in S_3\times S_3\). Relabel the fibres of \(u_1\) and \(u_2\) so that \((p_1,q_1)=(\mathrm{id},\mathrm{id})\). As right vertices are exchangeable, the other \(n-1\) pairs may be sorted lexicographically. No full cover is omitted by this normalization.

For a left-fibre assignment \((a,b,c)\in\{0,1,2\}^3\), exactly
\[
F_{p,q}(a,b,c)=3-\left|\{a,p(b),q(c)\}\right|
\]
right-fibre representatives remain available at a vertex of type \((p,q)\). Choices on distinct right vertices are independent; consequently the total number of DP colourings of a normalized cover is
\[
N(p_2,q_2;\ldots;p_n,q_n)
=\sum_{a,b,c=0}^{2}F_{\mathrm{id},\mathrm{id}}(a,b,c)
\prod_{i=2}^{n}F_{p_i,q_i}(a,b,c).
\]
This exact 27-term integer formula is valid for every full cover.

Enumerate the six permutations in lexicographic order \(012,021,102,120,201,210\). Give a pair \((p,q)\) type index \(6j+k\) when \(p\) and \(q\) are permutations at indices \(j\) and \(k\). The verified standalone exhaustive programs `verify.cpp` and `verify.py` enumerate all weakly increasing \(n-1\) type-index tuples from \(\{0,\ldots,35\}\), evaluate the 27-term sum exactly, and minimize. There are precisely \(\binom{n+33}{n-1}\) normalized cases. For \(n=1,2,3,4,5,6\) the numbers of tested cases are respectively \(1,36,666,8436,82251,658008\), and the computed minima are \(24,18,14,6,5,0\). The independently implemented programs agree. Here enumeration is an exhaustive finite certificate, not an inference from experimental samples: the normalization covers all possible full covers and every normalized case is explicitly evaluated. One attaining tuple of type indices for each successive \(n\) is

| \(n\) | Complete tuple of normalized type indices | Number of DP colourings |
|---|---|---:|
| 1 | `0` | 24 |
| 2 | `0,22` | 18 |
| 3 | `0,8,29` | 14 |
| 4 | `0,8,29,33` | 6 |
| 5 | `0,1,8,16,24` | 5 |
| 6 | `0,3,4,18,21,22` | 0 |

For a separate symbolic obstruction valid at every \(n\ge6\), use the six right-vertex types \((p,q)=(s_u,s_v)\) with \(u\in\{0,1\}\), \(v\in\{0,1,2\}\), where \(s_j(z)=z+j\pmod3\). Given any left assignment \((a,b,c)\), select \(u\in\{0,1\}\) such that \(b+u\not\equiv a\pmod3\), and then select \(v\in\{0,1,2\}\) so that \(c+v\) is the unique third residue. This right vertex forbids all three representatives, so no independent transversal exists. Adding any further right vertices preserves the obstruction. This proves the zero case for all integers \(n\ge6\), not just the computationally checked instance.

## Verification
Compile and execute `verify.cpp` with `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. The exact integer program enumerates every normalized full cover through \(n=6\), checks the expected minima and number of minimizing type multisets, tests explicit witnesses by independent direct enumeration, and tests the analytic six-type obstruction on every possible triple of left colours. Independently run `python3 verify.py` to enumerate the same finite normal forms using a separately written program. Both programs end in `VERIFY_OK` when all checks pass. The C++ minimizer counts for \(n=1,\ldots,6\) are \(1,2,18,6,180,60\). These are counts of normalized minimizer multisets, **not** counts of inequivalent labelled DP covers.

## Relationship to prior work
Kaul, Mudrock, Sharma, and Ullyot, *The DP Color Function of Bipartite Graphs* (first public August 3, 2026), develop general bipartite DP-colour-function methods and an exact calculation on the two-vertex shore. Their results do not state this three-vertex-shore three-colour census. Mudrock's *A Note on the DP-Chromatic Number of Complete Bipartite Graphs* establishes non-colourability thresholds, including the known three-colour six-right-vertex obstruction. Further covering-family work in 2026 also notes this threshold. The threshold is credited, and the claimed contribution is the complete set of exact worst-cover counts, especially the positive pre-threshold values. Prior searches have not located an equivalent published table, although coverage of the literature cannot be guaranteed.

## Limitations
The claim concerns only three-element fibres of \(K_{3,n}\). It does not give the DP colour function for four or more colours, arbitrary bipartite graphs, or a classification of all distinct minimizing covers. The finite integer certificate relies on exhaustive normalization as explicitly explained, not on an unprovided external solver. An earlier unindexed equivalent table remains a priority risk. Independent mathematical audit has not been performed.

## References
- H. Kaul, J. A. Mudrock, G. Sharma, and A. Ullyot, *The DP Color Function of Bipartite Graphs*, arXiv:2608.02335 (first public 2026-08-03), https://arxiv.org/abs/2608.02335.
- H. Kaul et al., *Covering Families for DP-Coloring of Cartesian Products with Complete Bipartite Graphs*, arXiv:2609.33966 (2026), https://arxiv.org/abs/2609.33966.
- J. A. Mudrock, *A Note on the DP-Chromatic Number of Complete Bipartite Graphs*, arXiv:1803.09141 (first public 2018-03-24), https://arxiv.org/abs/1803.09141.
