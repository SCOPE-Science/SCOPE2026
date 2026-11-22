# Error-detecting identifying codes of the thirteen-vertex Paley graph

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), with edges between residues differing by a nonzero square. A *closed-neighborhood error-detecting identifying code* (DET:IC) is a set of detector vertices satisfying the asymmetric two-witness criterion in the next section. The cardinality polynomial of *all* such codes, with the graph vertices fixed and no quotient by symmetry, is
\[
E_{P_{13}}(z)=364z^9+286z^{10}+78z^{11}+13z^{12}+z^{13}.
\]
Consequently the minimum detector count is exactly \(9\), attained by exactly \(364\) subsets. An example is \(S=\{0,1,2,3,4,5,6,7,9\}\). These \(364\) minimum codes form precisely seven orbits under the \(78\) affine automorphisms \(x\mapsto ax+b\), where \(a\) is a nonzero square and \(b\in\mathbb Z/13\mathbb Z\); their orbit sizes are \(26,26,39,39,78,78,78\).

The structural obstruction is also exact. Among the \(715\) four-vertex omitted sets \(U\), precisely \(351\) violate DET:IC, each for a unique adjacent pair of vertices. Every five-vertex omitted set contains at least one of those forbidden tetrads. Thus **four** is the largest possible number of omissions, and exactly \(364\) four-omission patterns are permitted.

## Assumptions and scope
All graphs are finite, undirected, simple. The Paley adjacency is defined explicitly by \(R=\{1,3,4,9,10,12\}\) in \(\mathbb Z/13\mathbb Z\): vertices \(u\ne v\) are adjacent iff \(u-v\in R\). Write \(N[u]\) for the *closed* neighborhood, with seven vertices. For a candidate detector set \(S\), the DET:IC requirements are, for every \(u\), \(|N[u]\cap S|\ge2\), and for every \(u\ne v\),
\[
\max\bigl(|S\cap(N[u]\setminus N[v])|,|S\cap(N[v]\setminus N[u])|\bigr)\ge2.
\]
This is the **error-detecting**, not the ordinary identifying-code or redundant one-erasure criterion. The asymmetric criterion is Theorem 2.1 of Jean--Seo (2022), following Seo--Slater. A selected code is an ordinary labeled subset of the thirteen fixed vertices; only the optional orbit statement quotients by a specified automorphism subgroup.

## Proof
**1. Neighborhood sizes.** Every vertex has six neighbors, so its closed neighborhood has seven vertices. A direct residue calculation gives \(|R\cap(1+R)|=2\) and \(|R\cap(2+R)|=3\). Multiplication by a nonzero square takes any nonzero square difference to \(1\), and any nonsquare difference to \(2\). Thus adjacent pairs have two common open neighbors and nonadjacent pairs three. The two directed closed-neighborhood differences \(A_{uv}=N[u]\setminus N[v]\) and \(B_{uv}=N[v]\setminus N[u]\) are disjoint, each of cardinality \(3\) if \(uv\) is an edge and \(4\) otherwise.

**2. Exact four-omission obstruction.** Put \(U=V\setminus S\). If \(|U|\le4\), the seven-element closed neighborhoods retain at least three selected vertices, so the two-domination requirement is automatic. To violate the directed pair condition, \(U\) must contain at least \(2\) elements of each directed three-set (adjacent pair), or at least \(3\) of each directed four-set (nonadjacent pair). Since these differences are disjoint, no \(|U|\le3\) can violate any pair condition; when \(|U|=4\) only an adjacent pair can fail. For such an adjacent pair, the forbidden omission is exactly a union of a two-subset of \(A_{uv}\) and a two-subset of \(B_{uv}\). Every edge consequently gives \(\binom32^2=9\) candidate forbidden tetrads. There are \(39\) edges.

**3. No duplicated tetrads, and no five-omission set survives.** The finite calculation is reduced to affine orbits by the verified automorphisms \(x\mapsto ax+b\) (\(a\in R\), \(b\in\mathbb Z/13\mathbb Z\)). Exhaustively constructing all four-element subsets gives thirteen orbits with orbit size and forbidden-witness count as follows (\(c\) is the number of adjacent pairs witnessing the failure of the representative):

| Representative \(U\) | Orbit size | \(c\) |
|---|---:|---:|
| \(\{0,1,2,3\}\) | 39 | 1 |
| \(\{0,1,2,4\}\) | 78 | 0 |
| \(\{0,1,3,4\}\) | 39 | 1 |
| \(\{0,1,2,5\}\) | 78 | 1 |
| \(\{0,1,3,5\}\) | 78 | 1 |
| \(\{0,2,3,5\}\) | 39 | 0 |
| \(\{0,1,2,6\}\) | 78 | 0 |
| \(\{0,1,4,6\}\) | 26 | 0 |
| \(\{0,2,4,6\}\) | 39 | 0 |
| \(\{0,1,2,7\}\) | 78 | 0 |
| \(\{0,2,3,7\}\) | 26 | 0 |
| \(\{0,2,4,7\}\) | 78 | 1 |
| \(\{0,2,5,7\}\) | 39 | 1 |

The orbit sizes sum to \(715\). Their six forbidden orbits total \(351\) elements, and all their witness counts equal one. Their seven permitted orbits total \(364\) elements. By construction every one of the \(39\cdot9=351\) adjacent-pair candidates is counted exactly once.

For five omissions, each orbit representative can be checked against its five constituent tetrads; all nineteen orbits have a positive count of forbidden tetrads. The full certificate is printed by `check_orbits.cpp` and recorded in `output_orbits.txt`. The resulting exact number of five-subsets containing respectively one, two, three or four forbidden tetrads is \(273,312,546,156\); their sum is \(\binom{13}{5}=1287\). Hence no five-omission set is permitted. By monotonicity of the detector requirements under *adding* sensors, no omitted set with at least five elements is permitted.

**4. Polynomial and minimum.** All omissions of size zero, one, two and three work; precisely \(364\) of the four-subsets work; larger omissions fail. Complementation gives \(\binom{13}{0}z^{13}+\binom{13}{1}z^{12}+\binom{13}{2}z^{11}+\binom{13}{3}z^{10}+364z^9\), as claimed. The group of \(78\) affine maps partitions the seven good tetrad orbits into sizes \(26,26,39,39,78,78,78\), giving the stated orbit count.

All finite counts above are proven by explicit exhaustive integer loops in the attached standalone source programs, without a timeout assumption or a heuristic extrapolation.

## Verification
Execute `python3 check_direct.py` to test all \(2^{13}=8192\) possible detector sets directly from the two-defining-inequalities. Execute `g++ -std=c++17 -O2 check_orbits.cpp -o check_orbits && ./check_orbits` for an independent certificate that constructs the \(351\) forbidden tetrads from pairs of directed differences, tests every five-subset for obstruction coverage, and enumerates the affine orbit decompositions. Output from these commands is preserved in `output_direct.txt` and `output_orbits.txt`. Both independently produce the cardinality polynomial above.

## Relationship to prior work
Jean and Seo's 2022 *Optimal Error-detection system for Identifying Codes* (arXiv:2208.06052v1) supplies the exact criterion for this fault model, discusses complexity, hypercubes, cubic graphs and grids, and does not calculate the Paley-13 polynomial. Jean and Seo's 2021 *Fault-tolerant Identifying Codes in Special Classes of Graphs* (arXiv:2112.01685) concerns redundant codes under a single detector outage; its symmetric two-witness separation criterion is not the directed error-detection criterion. Gravier, Parreau, Rottey, Storme and Vandomme (2015) investigate ordinary identifying codes in vertex-transitive and strongly regular graphs, including Paley graphs, but not these error-detecting all-set multiplicities. Elsawy and Almohammadi (2025) explicitly draw the same Paley-13 graph, but study edge-graceful labelings, not identifying sensors. Related recorded computations for projective-plane incidence graphs and for standard identifying codes of other small strongly regular graphs concern different graphs and requirements. No searched source implied this polynomial or its obstruction census.

## Limitations
The classification is finite and specific to \(P_{13}\); it does not provide a formula for all Paley graphs. Affine orbit sizes refer to the stated order-78 subgroup, not an unverified enumeration of the full graph automorphism group. Finite computation is exhaustive for the defined thirteen-vertex graph, but it is not a proof for graphs of other orders. Scholarly priority is subject to literature not identified in the searches, and an independent mathematical audit has not been performed.

## References
1. Devin C. Jean and Suk J. Seo, *Optimal Error-detection system for Identifying Codes*, arXiv:2208.06052v1, first posted 11 August 2022. https://arxiv.org/abs/2208.06052
2. Devin C. Jean and Suk J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685v1, 2021. https://arxiv.org/abs/2112.01685
3. Sylvain Gravier, Aline Parreau, Sara Rottey, Leo Storme and Élise Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, Electronic Journal of Combinatorics 22(4) (2015), P4.6. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p6/pdf/0
4. Ahmed N. Elsawy and Reyoud Nasser Almohammadi, *Paley, Cubic Paley, Quadruple Paley, and Generalized Paley Graphs with an Edge Graceful Labeling*, European Journal of Pure and Applied Mathematics 18(4) (2025), 6600. https://www.ejpam.com/ejpam/article/download/6600/2596
