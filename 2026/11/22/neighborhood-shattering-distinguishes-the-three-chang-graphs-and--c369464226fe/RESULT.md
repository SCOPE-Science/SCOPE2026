# Neighborhood shattering distinguishes the three Chang graphs and detects nonpure facets

## Finding
Let \(G\) be a strongly regular graph with parameters \((28,12,6,4)\). For \(\star\in\{\circ,\bullet\}\), define its **neighborhood shattering polynomial**
\[
\Phi_G^\star(z)=\sum_{k\ge0}s_k^\star(G)z^k,
\]
where \(s_k^\circ(G)\) counts the \(k\)-element vertex supports shattered by the twenty-eight open-neighborhood concepts \(\{N_G(v):v\in V(G)\}\), and \(s_k^\bullet(G)\) is defined using the closed neighborhoods \(\{N_G[v]:v\in V(G)\}\). The complete coefficient vectors, ordered by \(k=0,1,2,3,4\), are:

| Graph | \((s_0^\circ,s_1^\circ,s_2^\circ,s_3^\circ,s_4^\circ)\) | \((s_0^\bullet,s_1^\bullet,s_2^\bullet,s_3^\bullet,s_4^\bullet)\) | Maximal open shattered triples |
|---|---|---|---:|
| Triangular \(T(8)\) | \((1,28,378,2800,9520)\) | \((1,28,378,1960,2520)\) | \(0\) |
| Chang, matching switch | \((1,28,378,2936,2736)\) | \((1,28,378,1968,984)\) | \(1328\) |
| Chang, eight-cycle switch | \((1,28,378,2968,1152)\) | \((1,28,378,1968,576)\) | \(1624\) |
| Chang, triangle-plus-pentagon switch | \((1,28,378,2986,810)\) | \((1,28,378,1980,450)\) | \(1786\) |

Every coefficient of degree at least five is zero. Hence all four graph types have open- and closed-neighborhood VC dimension exactly \(4\), but **both complete polynomials distinguish all four isomorphism classes**. The open-neighborhood shattered-support complex of \(T(8)\) is pure of dimension \(3\), while each Chang graph has inclusion-maximal shattered triples as well as quadruples, and is therefore nonpure. The displayed triangular-graph polynomial rows were known previously; the new finite classification is the three Chang rows and their facet comparison.

## Assumptions and scope
All graphs are simple and undirected. A support \(S\subseteq V(G)\) is shattered by a concept family \(\mathcal H\) when \(\{H\cap S:H\in\mathcal H\}=2^S\); concepts are indexed by actual graph vertices, and no empty or universal concept is added. By Chang's classification, the specified strongly regular parameter set has exactly four isomorphism classes.

For reproducible representatives, identify the vertices of the triangular graph with the twenty-eight unordered two-subsets of \(\{0,1,\ldots,7\}\), adjacent when they meet in one element. Write \(ij\) for the vertex \(\{i,j\}\). For a switching set \(B\), Seidel switching toggles an adjacency exactly when one vertex belongs to \(B\) and the other does not. Use:

\[
\begin{aligned}
B_M&=\{01,23,45,67\},\\
B_8&=\{01,12,23,34,45,56,67,07\},\\
B_{3+5}&=\{01,02,12,34,45,56,67,37\}.
\end{aligned}
\]

The resulting graphs are respectively the matching-, eight-cycle-, and disjoint triangle/pentagon-switched Chang graphs. No assumption about extra symmetries or a particular Chang numbering convention is needed.

## Proof
**(1) Exhaustive representatives.** The twenty-eight vertex labels and the preceding switching rule determine each adjacency entry uniquely. Both supplied programs reconstruct these four graphs without external graph datasets. For every graph, they verify that every vertex has degree \(12\), every pair of adjacent vertices has \(6\) common neighbors, and every nonadjacent pair has \(4\) common neighbors. The switching-set classification in Brouwer and Van Maldeghem, Section 10.11, establishes that these are precisely all four isomorphism classes of the indicated parameter set.

**(2) Finite and complete trace test.** For each of the \(\binom{28}{k}\) supports \(S=(v_0,\ldots,v_{k-1})\), with \(0\le k\le4\), form for every possible center \(c\) the trace code
\[
T_{c,S}=\sum_{i=0}^{k-1}2^i\mathbf 1_{\{cv_i\in E(G)\}}.
\]
For the closed family replace the indicator by \(\mathbf 1_{\{c=v_i\ \mathrm{or}\ cv_i\in E(G)\}}\). The support is shattered **exactly when** the collection of these twenty-eight integer codes equals \(\{0,\ldots,2^k-1\}\). This test is an immediate equivalence of the definitions, not a heuristic sampling rule. The two programs implement it independently: one enumerates explicit adjacency matrices and tuple traces, the other constructs integer bitsets and tests the trace masks. For each of four graphs and each neighborhood convention, all \(1+28+378+3276+20475=24158\) supports through size four are checked. Their exact counts agree and yield each coefficient in the table.

**(3) Exclusion of larger supports.** A shattered support of size five would require at least \(2^5=32\) distinct concepts, because different Boolean traces require different concept vertices. The class has only twenty-eight centers, so no five-element support can be shattered. Shattering is hereditary under taking subsets; hence no larger support is shattered. Thus the programs' four-layer census is a proof of the **complete** polynomial, not a truncated approximation.

**(4) Facets and purity.** For every shattered triple \(S\), the first program checks all \(25\) possible fourth vertices and records whether \(S\cup\{v\}\) is shattered. The bitset program independently constructs the union of the three-subsets of **all** shattered quadruples and subtracts it from the shattered triples. Both procedures give maximal-triple counts \(0,1328,1624,1786\) in the displayed graph order. Both also verify that every shattered pair extends to some shattered triple. All shattered quadruples are maximal by the preceding size-five exclusion. Thus the triangular case has only four-element facets, whereas each Chang case has facets of sizes three and four. Pairwise distinction of the open and closed coefficient vectors is immediate from the table.

## Verification
Using Python 3 and no third-party libraries, run `python3 verify_matrix.py` and `python3 verify_bitsets.py` in the same directory as the supplied files. Both reconstruct all graphs from their switching sets and enumerate every support through size four; the first tests \(193264\) support/family instances and checks extension maximality, while the second independently re-creates and matches the coefficients and facet counts. Their concluding messages are respectively `CHANG_SHATTER_MATRIX_PASS` and `CHANG_SHATTER_BITSETS_PASS`. The actual replay output is included in `verification_output.txt`. No random sampling, numerical approximation, or inferred higher-degree coefficient is involved.

## Relationship to prior work
Benediktsson, Macpherson and Adler prove the open-neighborhood VC-dimension upper bound of four for Johnson graphs, including the triangular graph as a case; their result does not cover the three non-Johnson Chang graphs or the full shattering coefficients. Earlier exact open- and closed-neighborhood shattering polynomials of triangular graphs already yield the **triangular row above**, which is therefore used only as a comparator. The classical Chang classification supplies the four representatives and their common strongly regular parameters, not these trace counts.

Previously published mod-two homology calculations enumerate the faces of the Lovász open-neighborhood complexes for the four parameter graphs. That simplicial complex consists of sets with a **single** center adjacent to every queried vertex; it is distinct from the present shattering complex, which requires centers realizing **every** labeling on a support. The prior neighborhood-complex face counts, such as \(2960\) triangles for the matching-switched graph compared with \(2936\) shattered triples here, demonstrate the difference. Its homology already distinguishes the four graphs; no claim of being the first distinguishing invariant is made. The new statement is the complete two-convention trace census and the purity boundary. A previously recorded four-round first-order distinction between the three Chang graphs is likewise about another invariant.

## Limitations
The result concerns only the four graphs of the stated strongly regular parameters; it does not give a formula for arbitrary strongly regular graphs or a general rule for Seidel switching. The proof is a complete finite exhaustive certificate rather than a symbolic all-order family argument. The literature inspection was substantial but cannot exclude an unindexed historical equivalent.

## References
1. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, first publicly posted 2020-07-31; particularly Theorems 3.6–3.7. https://arxiv.org/pdf/2007.16042.
2. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, Cambridge University Press (online 2022-01-06), Section 10.11, pp. 257–258 of the freely accessible author preprint. DOI:10.1017/9781009057226. https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
3. *Exact open-neighborhood shattering polynomial of triangular graphs*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-open-neighborhood-shattering-polynomial-of-triangular-grap--ea869538b5c1/RESULT.md.
4. *Complete closed-neighborhood shattering polynomial of triangular Johnson graphs*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-closed-neighborhood-shattering-polynomial-of-triangular--08634914be96/RESULT.md.
5. *Neighborhood homology distinguishes all four strongly regular (28,12,6,4) graphs*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-neighborhood-homology-distinguishes-all-four-strongly-regular-28--2d1512d0c583/RESULT.md.
6. *Four distinct rank-four theories of the Chang parameter graphs*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-four-distinct-rank-four-theories-of-the-chang-parameter-graphs--293323715435/RESULT.md.
