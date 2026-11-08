# Exact all-length count of sparse nonbinary universal cycles

## Finding

Fix an integer alphabet size \(q\ge3\) and a window length \(n\ge3\). The alphabet is \(\Sigma_q=\{0,1,\ldots,q-1\}\) with a distinguished zero symbol; symbols other than zero remain individually labeled. Let \(\mathcal W_{q,n}\) be the length-\(n\) words of **Hamming weight at most two**, i.e. having at most two nonzero positions. A sparse universal cycle is a cyclic sequence whose length-\(n\) windows contain every element of \(\mathcal W_{q,n}\) exactly once. Rotation identifies cycles, but neither alphabet relabeling nor reversal does.

**Theorem.** The number of sparse universal cycles is

\[
U_{q,n}=((q-1)!)^{\,1+(n-1)(q-1)}q^{\,(n-1)(q-2)+\lfloor(n-1)/2\rfloor}.
\]

Their common period is \(1+n(q-1)+\binom{n}{2}(q-1)^2\). For example, \(U_{3,3}=864\), \(U_{3,4}=10368\). The displayed theorem is an all-length count, not a finite census.

## Assumptions and scope

The window is cyclic and ordered. A nonzero symbol can take any of the \(q-1\) distinct labels; Hamming weight counts **nonzero positions**, not the arithmetic sum of symbol labels. A cycle has precisely \(|\mathcal W_{q,n}|\) positions, and the word \(0^n\) occurs exactly once, giving a canonical starting window. The proof also works when \(q=2\) or \(n=2\); those endpoints are used as consistency tests rather than new priority claims.

## Proof

Put \(m=n-1\) and \(r=q-1\). Form the directed de Bruijn graph with vertices all length-\(m\) words of Hamming weight at most two and directed edges all length-\(n\) such words, from their length-\(m\) prefix to their length-\(m\) suffix. Each vertex is balanced: the incoming and outgoing degrees are \(q\) for weight zero or one and one for weight two. Appending zeros reaches the root \(o=0^m\) from any vertex; starting at \(o\), appending the desired symbols reaches any vertex. Thus the graph is strongly connected and Eulerian.

The directed BEST theorem, with the edge \(0^n\) designated as the first edge and with the root \(o\), counts cyclic Euler tours as \(t_o\prod_v(d_v-1)!\), where \(t_o\) is the number of in-arborescences directed to \(o\). There are exactly \(1+mr\) vertices with degree \(q\), and all other vertices have degree one. Hence the factorial product is \(((q-1)!)^{1+mr}\). It remains to prove

\[
t_o=q^{m(r-1)+\lfloor m/2\rfloor}.
\]

Every weight-two vertex has exactly one outgoing edge, which appends zero, so that edge must lie in every in-arborescence. Such forced edges have no directed cycles: repeatedly appending zeros eventually reaches the root or a weight-one vertex. We may therefore contract each of these forced paths without changing the number of arborescences. Label a weight-one vertex by \((a,j)\), where \(a\in\{1,\ldots,r\}\) is its nonzero symbol and \(j\in\{0,\ldots,m-1\}\) counts its position from the right. Appending zero sends \((a,j)\) to \((a,j+1)\) if \(j<m-1\), otherwise to \(o\). Appending a nonzero symbol \(b\) and then following the forced zero edges sends it to \((b,m-1-j)\). Thus the reduced rooted directed Laplacian on the \(mr\) weight-one states is

\[
L=qI-S\otimes I_r-R\otimes J_r,
\]

where \(S\) is the \(m\)-by-\(m\) matrix with ones on its superdiagonal, \(R\) is the reversing permutation matrix of order \(m\), and \(J_r\) is the all-ones matrix. The directed Matrix–Tree Theorem identifies \(t_o=\det L\); loops are correctly handled by the diagonal-minus-adjacency convention. Decompose the color space into the one-dimensional constant subspace and its \((r-1)\)-dimensional sum-zero subspace. Since \(J_r\) acts as \(r\) and zero respectively,

\[
t_o=\det\big(qI_m-S-rR\big)\,\det(qI_m-S)^{r-1}
=q^{m(r-1)}\det\big(qI_m-S-(q-1)R\big).
\]

**Determinant lemma.** For every integer \(m\ge1\) and scalar \(q\),
\[
\det\big(qI_m-S-(q-1)R\big)=q^{\lfloor m/2\rfloor}.
\]

Indeed set \(A=qI_m-S-(q-1)R\) and let \(T\) be the upper-triangular matrix \(T_{jk}=1\) when \(k\ge j\), zero otherwise, with zero-based indices. It has determinant one. The final column of \(AT\) is the final coordinate vector, because \(A\mathbf1=e_{m-1}\). Consequently \(\det A\) equals the determinant of the \((m-1)\)-square matrix \(C\), indexed by \(j,k\in\{0,\ldots,m-2\}\), with
\[
C_{jk}=q\mathbf1_{j=k}+(q-1)\big(\mathbf1_{k\ge j+1}-\mathbf1_{k\ge m-1-j}\big).
\]

Order these indices by distance to the nearer endpoint of \(\{0,\ldots,m-2\}\), breaking ties by putting the smaller index first: \(0,m-2,1,m-3,\ldots\). In this simultaneous row-and-column order, \(C\) is upper triangular. To check this without an unstated lemma, if \(j\) is on the left half, every nonzero off-diagonal entry has \(j<k\le m-2-j\), which is more central or at the tied right endpoint; if \(j\) is on the right half, every such entry has \(m-1-j\le k<j\), strictly closer to the center. Its diagonal entries are \(q\) at exactly the \(\lfloor m/2\rfloor\) left-side/central positions and one elsewhere. The determinant is therefore \(q^{\lfloor m/2\rfloor}\). The case \(m=1\) is immediate. This proves the lemma, the arborescence formula, and the theorem by BEST.

## Verification

The standalone `check_sparse_cycles.py` recomputes two logically separate finite checks using Python's standard library. First it forms the reduced directed Laplacian on colored weight-one states and evaluates its determinant by exact Bareiss integer elimination, verifying the tree count for \(2\le q\le5\) and \(2\le n\le9\). Second it exhaustively enumerates local outgoing-edge orders, with the all-zero edge fixed first, and checks that every successful tour has precisely the required **distinct cyclic windows**. This verifies \(2\le n\le11\) at \(q=2\), \(n=2,3,4\) at \(q=3\), and \(n=2\) at \(q=4\). All assertions pass with `VERIFY_OK`. These are finite checks; the all-parameter theorem depends on the displayed algebraic proof.

## Relationship to prior work

The March 12, 2026 work of Gabrić, Imam, Janik-Jones, and Sawada [1] identifies enumerating universal cycles as a fundamental question and develops decoding for bounded **symbol-sum** weight de Bruijn sequences. The q-ary successor construction of Gabrić, Sawada, Williams, and Wong [2] also uses numerical symbol-sum weight; a Hamming-weight restriction with multiple independently labeled nonzero symbols is distinct for \(q\ge3\). Neither inspected account gives the stated universal-cycle count. Sawada and Gabrić [3] study uniform generation through spanning in-trees, not an exact closed count for this sparse multicolor model. The earlier study by Li, Jiang, and Lin [4] concerns *binary* vectors of weight at most \(k\); it motivates close priority caution for the \(q=2\) specialization, which is excluded from the new claim. Mitchell and Wild [5] treat weight-constrained cycle existence rather than this multicolor Hamming-weight-two enumeration. General BEST and Matrix–Tree results supply the proof machinery but not the explicitly factored sparse determinant.

## Limitations

No formula is claimed for windows with more than two nonzero symbols, unequal symbol restrictions, forbidden local transitions, or noisy reconstruction. The count distinguishes symbol labels and does not quotient by alphabet permutation or reversal. The alphabet size is fixed independently of whether \(q\) is a prime power. An independent audit and definitive historical-priority confirmation, especially against unindexed nonbinary enumerations, remain outstanding.

## References

1. D. Gabrić, W. Imam, L. Janik-Jones, and J. Sawada, *Decoding universal cycles for t-subsets and t-multisets by decoding bounded-weight de Bruijn sequences*, first arXiv version March 12, 2026, https://arxiv.org/abs/2603.11934.
2. D. Gabrić, J. Sawada, A. Williams, and D. Wong, *A successor rule framework for constructing k-ary de Bruijn sequences and universal cycles*, IEEE Trans. Inf. Theory 66 (2020), 679–687, https://doi.org/10.1109/TIT.2019.2928292; author text https://www.socs.uoguelph.ca/~sawada/papers/kary-successor.pdf.
3. J. Sawada and D. Gabrić, *Random generation of universal cycles and de Bruijn sequences*, first arXiv version October 18, 2025, https://arxiv.org/abs/2510.16545.
4. M. Li, Y. Jiang, and D. Lin, *Properties of the cycles that contain all vectors of weight at most k*, Designs, Codes and Cryptography 91 (2023), 221–239, published online September 6, 2022, https://doi.org/10.1007/s10623-022-01100-9.
5. C. J. Mitchell and P. R. Wild, *Weight-constrained cut-down de Bruijn sequences*, first arXiv version July 24, 2026, https://arxiv.org/abs/2607.22350.
