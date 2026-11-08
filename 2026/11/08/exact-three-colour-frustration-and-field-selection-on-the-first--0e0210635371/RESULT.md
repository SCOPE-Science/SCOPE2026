# Exact three-colour frustration and field selection on the first four-chromatic Kneser graph

## Finding
Let \(G=\mathrm{KG}(6,2)\), the fifteen-vertex graph whose vertices are the two-element subsets of \([6]\), with two vertices adjacent precisely when the subsets are disjoint. For a labeled three-colour Potts spin configuration \(\sigma:V(G)\to\{0,1,2\}\), consider
\[
H_{J,h}(\sigma)=J\sum_{\{S,T\}\in E(G)}\mathbf1_{\sigma(S)=\sigma(T)}-h\sum_{S\in V(G)}\mathbf1_{\sigma(S)=0},\qquad J>0,\ h\in\mathbb R.
\]
Writing \(x=h/J\), the **exact ground-state energy for every real field** is
\[
\frac{E_0(h)}J=\min\{15,\ 3-4x,\ 3-6x,\ 15-10x,\ 45-15x\}.
\]
The only transition fields are \(x=-3,0,3,6\). In the five open intervals determined by them, the number of sites in color 0 is respectively \(0,4,6,10,15\), and the numbers of labeled ground states are respectively \(882,60,60,192,1\). At the four transition fields, the total ground-state degeneracies are \(5862,180,2652,1583\), respectively.

At zero field the minimum number of monochromatic edges is exactly **three**, attained by exactly **180** labeled configurations. Every minimizer has colour-class sizes \(4,5,6\) (in some order) and belongs to one explicit family: select two distinct points \(a,b\in[6]\), colour the edges of the original complete graph \(K_6\) incident to \(b\) (including \(ab\)) with one colour, the four remaining edges incident to \(a\) with another colour, and the six edges on the other four vertices with the third colour. Permuting the three labels yields the complete family of \(6\cdot5\cdot6=180\) configurations. The only frustrated pairs are the three unordered disjoint edge pairs within this monochromatic \(K_4\).

## Assumptions and scope
All vertices and colours are labeled; no quotient by graph automorphisms or colour permutations is used in the energy or degeneracy counts. Every graph edge is counted once. The coupling is strictly antiferromagnetic \(J>0\). The field \(h\) is an arbitrary real number, including negative values and equality at every transition. The result concerns one finite graph, not a thermodynamic limit. This is the first member of the two-subset Kneser family with chromatic number four; the classical chromatic-number formula alone guarantees a nonzero three-colour penalty but does not determine its amount or multiplicity.

## Proof
Identify vertices \(S=\{i,j\}\) with the fifteen edges of the complete graph on six points. Then a Potts conflict in \(G\) is exactly a monochromatic pair of *disjoint* edges in this three-edge-colouring of \(K_6\). There are \(\binom{6}{2}=15\) sites and \(45\) conflict edges.

For each \(n\in\{0,\ldots,15\}\), define \(m_n\) as the least number of monochromatic conflict edges among all configurations with precisely \(n\) sites of colour 0, and \(g_n\) as the number attaining this sector minimum. The complete exact census is:

| \(n\) | \(m_n\) | \(g_n\) |
|---:|---:|---:|
| 0 | 15 | 882 |
| 1 | 12 | 2400 |
| 2 | 9 | 1920 |
| 3 | 6 | 600 |
| 4 | 3 | 60 |
| 5 | 3 | 60 |
| 6 | 3 | 60 |
| 7 | 6 | 600 |
| 8 | 9 | 1200 |
| 9 | 12 | 600 |
| 10 | 15 | 192 |
| 11 | 21 | 480 |
| 12 | 27 | 640 |
| 13 | 33 | 240 |
| 14 | 39 | 30 |
| 15 | 45 | 1 |

A complete finite enumeration supplies these integers with two independent implementations. The first assigns all fifteen spins recursively; when a spin is assigned it adds exactly the same-colour edges to earlier vertices. Every leaf corresponds to one and only one of the \(3^{15}=14348907\) labeled configurations. The second first computes, for each subset \(A\) of vertices, its induced-edge count \(c(A)\) using the exact recurrence
\[
c(A)=c(A\setminus\{v\})+|N(v)\cap(A\setminus\{v\})|,
\]
and then enumerates all ordered three-part partitions \((A,B,C)\), charging \(c(A)+c(B)+c(C)\). Thus every one of the \(3^{15}\) configurations is covered exactly once by another decomposition of the calculation. Both produce the identical table, including all sector minima and counts. Source files and a reproducible comparison program are supplied alongside this document.

For the zero-field structural classification, the second enumeration separately constructs the proposed family by choosing the ordered pair \((a,b)\) and permuting all three colours; it compares the resulting set of \(180\) encodings with the **entire** enumerated minimum-energy set and finds equality, not merely matching cardinalities. Each constructed assignment has exactly three frustrated pairs, contributed by the three perfect matchings of the residual \(K_4\).

At field \(x\), the sector energy is \(m_n-nx\). Pairwise exact rational comparisons of all sixteen affine functions give just five lower-envelope branches, corresponding to \(n=0,4,6,10,15\), and the four stated crossings. Sectors that lie on a crossing but are not branches in an open interval are included exactly at that crossing: \(n=0,1,2,3,4\) at \(-3\); \(4,5,6\) at \(0\); \(6,7,8,9,10\) at \(3\); and \(10,11,12,13,14,15\) at \(6\). Summing the corresponding \(g_n\) yields respectively \(5862,180,2652,1583\). Rational half-space intersections prove that no omitted sector is minimal on any other interval or point.

## Verification
Run `python3 verify.py` in the directory containing `recursion.cpp` and `subsets.cpp`. A C++17 compiler (`g++`) is needed. The program compiles and executes both independent complete enumerators, checks all sixteen sector minima and multiplicities, verifies the exact star-star-core characterization, and checks the rational lower envelope and transition degeneracies. All integer counts fit within signed 64-bit integers. The full configuration space is exhausted; no random sampling, numerical tolerance, or extrapolation is used.

## Relationship to prior work
Kneser graph chromatic-number theory proves \(\chi(\mathrm{KG}(6,2))=4\), but does not yield the precise least conflict penalty, its structural minimizers, or the field-dependent degeneracy envelope [1]. General Potts external-field polynomial and forest expansions permit a formal partition function for any finite graph [2,3], but the examined source results do not evaluate this specific fifteen-site graph, its complete zero-field defect classification, or the four threshold multiplicities. Three-colour Ramsey multiplicity results for monochromatic triangles [4] concern the graph \(K_3\) as the monochromatic pattern, not the disjoint-edge pattern \(2K_2\), so do not imply these counts. The earlier general combinatorial identities and chromatic-number theorem are not claimed as new.

## Limitations
This is an exact finite-graph result, not a theorem for all Kneser graphs or a finite-temperature thermodynamic phase transition. The uniqueness of the 180 extremal configurations is established by transparent exhaustive finite enumeration rather than by a separate noncomputational classification proof. The surveyed literature and matching-record searches cannot rule out every unindexed historical table or equivalent enumeration; an earlier exact \(2K_2\) multiplicity computation would affect priority.

## References
[1] J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072 (first public arXiv version, 2002-08-09). https://arxiv.org/abs/math/0208072

[2] R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182 (2010-09-07). https://arxiv.org/abs/1009.1182

[3] L. M. McDonald and I. Moffatt, *On the Potts model partition function in an external field*, arXiv:1107.2363 (2011-07-12). https://arxiv.org/abs/1107.2363

[4] J. Cummings, D. Král', F. Pfender, K. Sperfeld, A. Treglown, and M. Young, *Monochromatic triangles in three-coloured graphs*, arXiv:1206.1987 (2012-06-10). https://arxiv.org/abs/1206.1987
