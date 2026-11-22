# Twenty-seven minimum-code exchange components in the complementary nine-cycle prism

## Finding
Let \(G\) be the complementary prism of the cycle \(C_9\), with the labelled vertices and edges specified below. A closed-neighborhood identifying code is a vertex set \(S\) for which the eighteen sets \(N_G[v]\cap S\), one for each vertex \(v\), are all nonempty and pairwise different.

**Theorem.** The identifying-code number of \(G\) is \(7\), and exactly \(90\) labelled seven-vertex codes attain it. Let \(\mathcal X\) have these \(90\) codes as vertices; two are adjacent if one selected graph vertex is replaced by one unselected vertex, leaving an identifying code. Then
\[
\mathcal X\cong 9\bigl(K_1\vee(2K_2)\bigr)\;\sqcup\;9P_3\;\sqcup\;9K_2.
\]
Here \(K_1\vee(2K_2)\) is the five-vertex *bowtie*, consisting of two triangles sharing exactly one vertex. Thus the exchange graph has exactly \(27\) components and \(81\) edges. Under the natural dihedral action of order \(18\) on the cycle positions, the optimal codes form exactly six orbits of sizes \(18,18,9,18,18,9\).

## Assumptions and scope
All objects are finite, undirected, simple and labelled. Let \(i\in\mathbb Z/9\mathbb Z\), and use vertices \(x_i\) in the cycle layer and \(y_i\) in the complement layer. Edges are precisely
\[
 x_ix_{i+1},\qquad x_iy_i,\qquad y_iy_j\ \text{for}\ i\ne j\ \text{and}\ j-i\not\equiv\pm1\pmod9.
\]
Indices are modulo \(9\), and every edge is undirected. In an identifying code \(S\), closed neighborhoods include their center vertices. Every code is a *set* with no repeated selections. An exchange changes exactly one selected and one unselected vertex, with no intermediate step. There is no requirement that the exchange be along an edge of \(G\).

The statement concerns only this eighteen-vertex complementary prism; it does not assert an infinite-period classification or a token-sliding result. The dihedral action rotates or reflects indices \(i\) while preserving both layers, without swapping the layers.

## Proof
For each \(v\in V(G)\), let \(B_v=N_G[v]\). For any \(S\subseteq V(G)\), the elementary identity
\[
 (B_u\cap S)\mathbin\triangle(B_v\cap S)=(B_u\mathbin\triangle B_v)\cap S
\]
shows that \(S\) is an identifying code **if and only if** it intersects each of the \(18\) masks \(B_v\) and each of the \(\binom{18}{2}=153\) masks \(B_u\triangle B_v\). This equivalence covers domination, every pairwise separation and all boundaries, with no unstated graph assumptions.

A finite exhaustive proof now has only \(2^{18}=262144\) subsets to consider. The attached `exact_hitting_census.cpp` constructs all closed neighborhoods directly from the displayed edge definition, tests all \(171\) masks on every subset, and reports zero identifying codes of sizes \(0,1,\ldots,6\) and exactly \(90\) of size \(7\). It also verifies that the seven-code set
\[
\{x_0,x_1,x_2,y_4,y_5,y_6,y_7\}
\]
is admissible (it is among the enumerated minima). Therefore the minimum is exactly \(7\).

A second, independently organized enumeration, `direct_trace_census.py`, examines exactly
\[
\sum_{k=0}^7\binom{18}{k}=63004
\]
candidates, constructs all eighteen restricted closed-neighborhood traces directly from their chosen landmark lists, and checks nonemptiness and pairwise inequality without using the symmetric-difference hitting masks. Both verifiers find the same \(90\) labelled minima.

To classify them more transparently, write a code as two binary strings of length nine, ordered \(x_0,\ldots,x_8\) and \(y_0,\ldots,y_8\). The six orbit representatives obtained by the exhaustive test are:

| Orbit size | Cycle layer | Complement layer | Exchange-component type | Degree |
|---:|---|---|---|---:|
| 18 | `100011100` | `111000000` | bowtie | 2 |
| 18 | `010001110` | `110100000` | bowtie | 2 |
| 9 | `000001110` | `111100000` | bowtie | 4 |
| 18 | `101001100` | `101001000` | edge | 1 |
| 18 | `100011010` | `101001000` | three-vertex path | 1 |
| 9 | `100001010` | `101101000` | three-vertex path | 2 |

The dihedral action maps admissible codes and legal exchanges to admissible codes and legal exchanges. The verifier checks that these are six disjoint orbits with total cardinality \(90\). Each pair of codes is joined exactly when \(|S\triangle T|=2\). Enumerating those pairs produces \(81\) edges and the component census
\[
9\times(5\text{ vertices},6\text{ edges},\text{ degrees }2,2,2,2,4),
\quad9\times(3,2,\text{ degrees }1,1,2),
\quad9\times(2,1,\text{ degrees }1,1).
\]
A five-vertex graph with one degree-four vertex and four degree-two vertices is a bowtie when it has six edges: removing the universal vertex leaves four degree-one vertices, hence two independent edges. The three- and two-vertex components are respectively \(P_3\) and \(K_2\). This proves the asserted disjoint union. The Python verifier additionally checks explicitly that all eighteen dihedral maps preserve the entire exchange adjacency relation.

## Verification
From the directory containing the embedded source files, execute:

```sh
g++ -O2 -std=c++17 exact_hitting_census.cpp -o exact_hitting_census
./exact_hitting_census
python3 direct_trace_census.py
```

The first program exhausts all \(262144\) bitmasks and includes assertions on the exact minimum, optimum count, edge count and every component motif. The second program tests all \(63004\) possible candidate sets of cardinality at most seven by direct traces, checks exchange pairs, enumerates the six symmetry orbits and checks all dihedral transformations. Both were executed successfully on their actual embedded source contents. The enumeration is a finite **exhaustive proof of the specified finite graph statement**, not an experiment extrapolated to infinitely many cycles.

## Relationship to prior work
Cappelle, Coelho, Coelho, Penso and Rautenbach [1] studied identifying codes in complementary prisms of cycles, gave a nine-column construction using seven selected vertices and proved a \(7n/9+\Theta(1)\) size estimate. In particular their Lemma 3 supplies an admissible seven-vertex construction at \(n=9\). Their complete accessible preprint, including the main theorem, does not state this exact cardinality classification, six dihedral orbits or the optimum-code exchange graph. The existence of one seven-code does not imply that there are no six-codes or classify how all optimal codes interchange.

Felix and Cappelle [2] obtained general complementary-prism inequalities and exact minimum sizes for complete bipartite and complete split host graphs. Their general lower bound at nine host vertices is six, not seven, and they do not give an optimum-code exchange graph for a cycle host. Other related work on ordinary cycles, ordinary circular-ladder prisms, and Kneser graphs has different host graphs or invariants, so its exchanges do not imply these statements.

## Limitations
Historical priority is assessed from accessible primary literature, indexed record searches and recoverable earlier mathematical claims; unindexed or inaccessible equivalent classifications remain possible. A 2009 study on locating-domination in complementary prisms uses a different identification requirement and was identified via the later bibliography, but its complete original text was not inspected. The web rendering of the 2023 article permitted inspection of all its mathematical statements, although an attempted page-image inspection was denied. No independent scholarly audit was performed. The computation says nothing about \(n\ne9\), robustness to sensor deletion or token sliding.

## References
1. M. R. Cappelle, E. M. M. Coelho, H. Coelho, L. D. Penso, D. Rautenbach, *Identifying Codes in the Complementary Prism of Cycles*, arXiv:1507.05083v1, first public July 17, 2015; later *Electronic Notes in Theoretical Computer Science* 346 (2019), 241–251. https://arxiv.org/abs/1507.05083 . Accessible complete text: https://www.researchgate.net/publication/280220967_Identifying_Codes_in_the_Complementary_Prism_of_Cycles .
2. J. Felix, M. Cappelle, *On Identifying Codes in Complementary Prisms*, *Matemática Contemporânea* 55 (2023), 142–151, doi:10.21711/231766362023/rmc5516. https://mc.sbm.org.br/wp-content/uploads/sites/9/sites/9/2023/12/Article-15.pdf .
3. T. W. Haynes, K. R. S. Holmes, D. R. Koessler, L. Sewell, *Locating-domination in complementary prisms of paths and cycles*, *Congressus Numerantium* 199 (2009), 45–55 (bibliographic comparison only).
