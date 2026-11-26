# Exact enumeration of primitive-only order-four de Bruijn cycles

## Finding

For every integer \(q\ge2\), take an alphabet of \(q\) distinct labeled symbols. A length-four word is *primitive* when it is not the square of a length-two word; equivalently it is not of the form \(abab\), including the case \(a=b\). A *primitive-only de Bruijn cycle of order four* is a cyclic string in which the circular factors of length four are precisely all primitive length-four words, each occurring exactly once. Count cyclic rotations as the same string but do not identify symbol permutations or reversals.

There are exactly \(q^4-q^2\) required factors, and the number \(\mathcal U_4(q)\) of distinct cycles is

\[\mathcal U_4(q)=\frac{(q!)^{q^3}\big((q-1)^2+1\big)^{(q-1)(q-2)/2}}{q^{q^2-q+4}(q-1)^{q^2-2q+2}}.\]

In particular, \(\mathcal U_4(2)=4\) and \(\mathcal U_4(3)=2708265511157760\). This evaluates the complete cyclic enumeration, not just existence or the number of distinct primitive words.

## Assumptions and scope

All integers \(q\ge2\) are covered. Symbols are labeled. The cyclic string has length exactly \(q^4-q^2\); no factor may be repeated, and no imprimitive four-word is admitted. Loops in an auxiliary directed graph count as edges when calculating degrees, but cancel in its Laplacian. An Eulerian cycle is considered modulo cyclic rotation of its distinct labeled arcs.

## Proof

**1. The overlap graph.** Let \(V=\Sigma^3\), so \(|V|=q^3\). Start with the de Bruijn digraph \(H\) having one arc \(abcd\) from \(abc\) to \(bcd\) for every four-word. Delete precisely the \(q^2\) arcs \(abab\); call the remaining digraph \(P\). The arcs of \(P\) are in bijection with primitive four-words. Each vertex \(aba\) has in- and outdegree \(q-1\); all other vertices have in- and outdegree \(q\). These are all positive since \(q\ge2\). A traversal of each arc once yields exactly the required circular word, and the circular factors uniquely recover the traversal.

**2. The unrestricted arborescence determinant.** Let \(A\) be the adjacency matrix of \(H\), \(I\) the identity, and \(J\) the all-ones matrix, all indexed by \(V\). Because each triple of appended symbols gives one path between any two vertices, \(A^3=J\). The outdegree Laplacian is \(L_0=qI-A\). Its restriction to the \((q^3-1)\)-dimensional zero-sum space \(W\) has determinant \(q^{q^3-1}\), because \(A^3=0\) on \(W\). Since the graph is balanced, all directed in-arborescence cofactors are equal; their common value is

\[t_0=q^{q^3-4}.\]

Indeed the product of nonzero Laplacian eigenvalues equals \(q^3t_0\).

**3. The low-rank correction.** Deleting a loop \(aaaa\) leaves the Laplacian unchanged. For each unordered pair \(\{a,b\}\) of distinct symbols, deleting the opposite arcs \(abab\) and \(baba\) replaces \(L_0\) by \(L_0-f_{ab}f_{ab}^\top\), where \(f_{ab}=e_{aba}-e_{bab}\). Let \(F\) be the matrix of these \(\binom q2\) difference columns. Thus \(L=L_0-FF^\top\). All columns of \(F\) lie in \(W\). There the inverse of \(L_0\) is

\[G=\frac1q\left(I+\frac Aq+\frac{A^2}{q^2}\right),\]

as \((qI-A)G=I-A^3/q^3=I\) on \(W\). Hence the determinant lemma, restricted to \(W\), gives \(t_P/t_0=\det(I-F^\top GF)\).

For special vertices \(aba\) and \(cdc\), the adjacency entries are \(A_{aba,cdc}=[c=b,d=a]\), and the two-step entries are \((A^2)_{aba,cdc}=[a=c]\), with brackets denoting a truth indicator. Let \(B\) be an arbitrary oriented vertex-edge incidence matrix of the complete graph on the alphabet: its column indexed by \(a<b\) is \(e_a-e_b\). Direct substitution into the preceding inverse shows

\[F^\top GF=\frac{2(q-1)}{q^2}I+\frac1{q^3}B^\top B.\]

The nonzero eigenvalues of \(B^\top B\) are \(q\) with multiplicity \(q-1\); its remaining \((q-1)(q-2)/2\) eigenvalues are zero. Consequently

\[\frac{t_P}{t_0}=\left(\frac{(q-1)^2}{q^2}\right)^{q-1}\left(\frac{(q-1)^2+1}{q^2}\right)^{(q-1)(q-2)/2}.\]

This ratio is strictly positive. Thus there is an in-arborescence to the chosen root. Since \(P\) is balanced and has no isolated vertices, its condensation has no nontrivial source or sink, so \(P\) is strongly connected and Eulerian. In particular, the BEST theorem applies. This also supplies an independent existence proof.

**4. Counting Eulerian cycles.** The directed matrix-tree theorem gives \(t_P\) rooted in-arborescences. The BEST theorem says that the number of Euler cycles modulo rotation of the labeled arcs is

\[t_P\prod_{v\in V}(\deg^+(v)-1)!=t_P\big((q-2)!\big)^{q^2}\big((q-1)!\big)^{q^3-q^2}.\]

The factors of each resulting circular word are pairwise distinct, so this edge-cycle count equals the number of circular words, with no extra division by the word length. Substitute \(t_P=t_0(t_P/t_0)\), use \(q!=(q)(q-1)(q-2)!\), and simplify to the formula under **Finding**. This establishes it for every \(q\ge2\).

## Verification

Run `python3 verify.py` using a standard Python 3 interpreter. The verifier builds the unrestricted and primitive overlap Laplacians directly, computes their exact integer cofactors for \(q=2,3\) using fraction-free elimination, and checks their ratio and BEST counts against the formula. It independently evaluates the small incidence-matrix determinant for \(2\le q\le8\). It also exhaustively enumerates binary cyclic words of length \(12\) up to rotation and checks every length-four factor. The four binary cycles are `000111011001`, `000110111001`, `000100111011`, and `000100110111`. The successful output ends with `ALL_CHECKS_PASS`. Exact finite calculations corroborate but do not replace the general determinant proof.

## Relationship to prior work

Au (arXiv:0904.3997; public 25 April 2009, subsequently published in 2015) proves existence of primitive-word de Bruijn cycles for all lengths and alphabets, including a Lyndon concatenation construction, and explicitly sets up their directed overlap graphs (Sections 1–2, Theorem 9). The present statement enumerates *all* order-four cycles over arbitrary alphabet sizes, rather than selecting one construction. Sawada, Williams and Wong provide generalized greedy and necklace constructions, including the aperiodic language, but the inspected sections do not give the order-four enumeration. The classical unrestricted enumeration \((q!)^{q^3}/q^4\) follows from the BEST theorem, but does not itself yield the required deletion-corrected arborescence determinant. Moreno supplies existence criteria for arbitrary dictionary overlap graphs; no corresponding closed primitive-cycle count was established by the accessible abstract.

## Limitations

Only order-four primitive-factor cycles are enumerated; no analogous formula is claimed for other orders or for restrictions on word weights. The alphabet is labeled and reverse/complement symmetries are not quotiented. Bibliographic searches and inspections cannot rule out a previously unindexed equivalent enumeration.

## References

1. Y. H. Au, *Generalized de Bruijn words for Primitive words and Powers*, first arXiv version 25 April 2009, arXiv:0904.3997; author-hosted full text: https://au-gary.github.io/Au15a.pdf; published in *Discrete Mathematics* 338 (2015), doi:10.1016/j.disc.2015.05.025.
2. J. Sawada, A. Williams and D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, accessible full text: https://pdfs.semanticscholar.org/d856/7846f05e12b2a86a939c9bdae1e6f11e3251.pdf.
3. E. Moreno, *De Bruijn sequences and de Bruijn graphs for a general language*, *Information Processing Letters* 96 (2005), doi:10.1016/j.ipl.2005.05.028.
4. BEST theorem and the directed matrix-tree theorem; a modern reference for the former is https://mathworld.wolfram.com/BESTTheorem.html.
