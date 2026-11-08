# Scientific review: nilpotent-base corona wave census

## Correctness — PASS

For a nilpotent base adjacency with Jordan lengths \(s_i\), the corona block \(\begin{psmallmatrix}B&I\\I&0\end{psmallmatrix}\) has a unique Jordan block of length \(2s_i\) at eigenvalue one for each old nilpotent block; the characteristic polynomial and eigenspace dimension independently establish this. Its second reversible lift has two blocks of length \(2s_i\) at the distinct primitive cubic roots. Consequently its exact order is \(3\cdot2^{\lceil\log_2(2s_{\max})\rceil}\) and its fixed-space dimensions are \(2\sum_i\min(2s_i,2^{\nu_2(k)})\) when \(3\mid k\). The two companion identities prove the converse. Matching-parity and cube/path corollaries follow from independently justified adjacency identities. Two distinct standard-library programs checked all 278 eligible base graphs among 1,099 small labelled graphs and all 69,648 states in three low-order cases; the symbolic proof, not finite trials, supports the universal quantifiers.

## Originality — PASS with explicit priority limits

Relevant primary sources were compared at the level of statements and implications. Macfarlane (2004) supplies reversible second-order matrix methods, and Steeb–Hardy (2007) supplies a construction and a concrete wave rule; neither accessible statement gives the all-base-graph corona criterion. Barik–Pati–Sarma (2007) gives the corona adjacency block and real spectral transfer (full text, Lemma 2.1 and Theorem 3.1), not the needed characteristic-two Jordan chains or a period census. A separately obtained dyadic-sunlet instance is covered by the new theorem, but does not imply it. Published indexing searches and comparison with accessible prior claims yielded no dominating or equivalent universal statement. The full Macfarlane article remained inaccessible; its actual reviewed material was limited to its publisher abstract, and an unindexed equivalent remains possible. Thus the originality conclusion is evidence-based and qualified, not a claim of certified priority.

## Mathematical value — PASS

The result characterizes a natural global dynamical property through a base graph invariant, and gives every recurrent population for **all** nilpotent-adjacency base graphs, including disconnected ones. It also interprets the condition combinatorially through matching parities on trees and separates two unbounded families with radically different temporal clocks: path coronas with growing period and even-cube coronas with constant period. The converse and family contrast make this substantially broader than a graph-by-graph matrix diagonalization or isolated finite computation.

## Limits of review

All arithmetic assumes characteristic two and simple graph coronas with exactly one private leaf at each vertex. The inaccessible Macfarlane full text and potential equivalences under different terminology remain priority uncertainties. Program outputs are supporting checks, not external verification or proof of infinite statements.

Self-review: passed. Independent audit: not yet performed.
