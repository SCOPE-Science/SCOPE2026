# Exact enumeration of universal cycles of noninjective three-letter words

## Finding

Let \(q\ge 2\) be an integer, and let \(\Sigma\) be a fixed, labeled alphabet of size \(q\). Define
\[
\mathcal W_q=\{(a,b,c)\in\Sigma^3:\ a=b\text{ or }b=c\text{ or }a=c\}.
\]
A universal cycle for \(\mathcal W_q\) is a cyclic word whose cyclic length-three windows list **each** word of \(\mathcal W_q\) exactly once and list no other word. Two universal cycles are considered identical only when one is a cyclic rotation of the other; alphabet relabeling, reflection and reversal are not identified.

**Theorem.** The number of these cycles is exactly
\[
N_q=2^{q-1}\,3^{(q-1)(q-2)/2}\,q^{q-2}\,\bigl((q-1)!\bigr)^q,\qquad q\ge2.
\]
Their common length is \(3q^2-2q\). In particular,
\[
(N_2,N_3,N_4,N_5,N_6)
=(2,288,4478976,11609505792000,7312316880125952000000).
\]

## Assumptions and scope

The alphabet symbols are distinct and labeled. Every cyclic window is indexed by its starting position, and a cycle represents each allowed triple exactly once. The graph-theoretic proof uses the directed de Bruijn overlap graph, with self-loops permitted. Eulerian tours distinguish edges by their corresponding three-letter labels. For \(q=2\) all triples are allowable, so the familiar binary order-three de Bruijn count is recovered as a baseline, rather than claimed as novel.

## Proof

**1. Overlap graph and connectivity.** Create a directed graph \(G_q\) whose vertices are ordered pairs \((a,b)\in\Sigma^2\). Each admissible triple \((a,b,c)\in\mathcal W_q\) is a distinct directed edge \((a,b)\to(b,c)\). There are \(q^3-q(q-1)(q-2)=3q^2-2q\) edges. The diagonal vertices \(D_a=(a,a)\) have in- and outdegree \(q\), and the off-diagonal vertices \(O_{ab}=(a,b)\), \(a\ne b\), each have in- and outdegree \(2\).

All vertices belong to one strongly connected component: for distinct \(a,b\), the edges \(D_a\to O_{ab}\to D_b\) are labeled \(aab\) and \(abb\), respectively; every off-diagonal vertex reaches a diagonal vertex by \(O_{ab}\to D_b\). From any diagonal vertex one can reach any off-diagonal vertex through the appropriate diagonal vertex. Hence \(G_q\) is strongly connected and Eulerian. Reading successive edge labels identifies Euler tours with universal cycles.

**2. Normalize the cyclic starting point.** Every allowed triple occurs exactly once, including the loop \((0,0,0)\) after assigning the symbols names \(0,\dots,q-1\). Therefore each universal cycle has exactly one rotation with the edge \(000\) first. Counting Euler tours with this distinguished first edge counts rotational classes with no division factor.

Let \(T_q\) be the number of directed spanning arborescences toward \(D_0\). By the directed BEST theorem with the fixed initial edge \(000\),
\[
N_q=T_q\prod_{v\in V(G_q)}(\deg^+(v)-1)!=T_q\bigl((q-1)!\bigr)^q,
\]
since the factors at the off-diagonal vertices are \(1!\).

**3. Compute the arborescence determinant.** Form the outdegree Laplacian \(L\) of \(G_q\), including loops in both degree and adjacency so that they cancel on the diagonal. Order vertices first by the \(q\) diagonal vertices \(D_a\), then by the off-diagonal vertices \(O_{ab}\). Delete the row and column corresponding to the root \(D_0\). The off-diagonal principal block \(B\) decomposes over unordered symbol pairs \(\{a,b\}\): for each such pair the two states \(O_{ab},O_{ba}\) give the block
\[
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
Consequently \(\det B=3^{\binom q2}\), and each inverse block is
\[
\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
The diagonal-vertex block of the full Laplacian is \((q-1)I\). Vertex \(D_a\) has a single outgoing edge to \(O_{ab}\) for each \(b\ne a\); vertex \(O_{ab}\) has an outgoing edge to \(D_b\) and one to \(O_{ba}\). Eliminating all off-diagonal states by the Schur complement thus gives a diagonal entry \((q-1)-(q-1)/3=2(q-1)/3\) and an off-diagonal entry \(-2/3\) for every pair of distinct diagonal vertices. Equivalently, the resulting \(q\)-by-\(q\) Laplacian is
\[
S=\frac23\bigl(qI-J\bigr),
\]
where \(J\) denotes the all-ones matrix. Deleting its root row and column gives \(S_{\widehat0}\), whose determinant is
\[
\det S_{\widehat0}=\left(\frac23\right)^{q-1}q^{q-2}.
\]
The last equality follows from the eigenvalues of the complete-graph Laplacian minor (or the directed matrix-tree theorem for a complete digraph): the minor \(qI_{q-1}-J_{q-1}\) has eigenvalues \(1\) once and \(q\) with multiplicity \(q-2\). These identities remain valid at \(q=2\).

By the directed matrix-tree theorem and the determinant factorization,
\[
T_q=\det B\,\det S_{\widehat0}
=3^{q(q-1)/2}\left(\frac23\right)^{q-1}q^{q-2}
=2^{q-1}3^{(q-1)(q-2)/2}q^{q-2}.
\]
Inserting \(T_q\) into the BEST formula proves the theorem for every integer \(q\ge2\).

## Verification

Run the standalone standard-library Python checker using `python3 verify.py`. It computes the full integer Laplacian determinant by fraction-free Bareiss elimination, independently of the Schur calculation, for every \(2\le q\le6\); it checks the arborescence formula, the word count, and the Euler-tour count. It also exhaustively enumerates Euler tours starting with `000` at \(q=2,3\). Its success marker is `VERIFY_OK`.

For a separate enumeration implementation, compile `crosscheck.cpp` using `c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck` and execute `./crosscheck`. It builds the edge list and enumerates every edge-simple rooted Euler circuit by depth-first search at \(q=2,3\); it returns `CROSSCHECK_OK`. These are finite corroborations of the stated infinite-family proof, not replacements for it. The exact computed counts are

| \(q\) | Edges | Rooted arborescences | Universal cycles |
|---:|---:|---:|---:|
| 2 | 8 | 2 | 2 |
| 3 | 21 | 36 | 288 |
| 4 | 40 | 3456 | 4478976 |
| 5 | 65 | 1458000 | 11609505792000 |
| 6 | 96 | 2448880128 | 7312316880125952000000 |

## Relationship to prior work

Leitner and Godbole (first public preprint in August 2008; revised in 2009) prove universal-cycle existence for several restricted classes and explicitly observe in the remark after their Theorem 5 that universal cycles of non-bijections exist when word length and alphabet size coincide. This establishes existence for the ternary instance but does not evaluate its number. Champlin, Godbole and Tomlinson (first public preprint in March 2013), Theorem 5, prove existence for noninjective words of length at least four over general alphabets, and display a three-letter ternary example. Their result does not count all three-letter cycles. The graph description, the directed BEST theorem, and the directed matrix-tree theorem are established tools, not new ingredients.

The specific contribution here is the evaluated all-alphabet expression for the number of three-letter noninjective universal cycles, obtained by a complete determinant factorization that accounts for the off-diagonal pair states. The existence of these cycles and the familiar \(q=2\) de Bruijn case are explicitly prior. Search limitations and possible unindexed earlier numerical evaluations remain.

## Limitations

The theorem fixes word length to exactly three and the alphabet size to \(q\ge2\). It is not a closed counting formula for arbitrary word lengths or arbitrary forbidden-window classes. The count identifies rotations only: reversal, alphabet relabeling, and other group actions remain unquotiented. Computations are finite cross-checks through \(q=6\); the all-\(q\) assertion rests on the symbolic proof. No independent external verification or exhaustive historical-priority certification has been performed.

## References

1. Arielle Leitner and Anant Godbole, *Universal Cycles of Classes of Restricted Words*, arXiv:0808.1309, first posted 2008-08-08. https://arxiv.org/abs/0808.1309
2. Michelle Champlin, Anant Godbole, and Beverly Tomlinson, *Universal Cycles of Complementary Classes*, arXiv:1303.3323, first posted 2013-03-14. https://arxiv.org/abs/1303.3323
3. Directed BEST theorem and directed matrix-tree theorem, classical enumerative graph theory (used with fixed-edge Euler-tour normalization).
