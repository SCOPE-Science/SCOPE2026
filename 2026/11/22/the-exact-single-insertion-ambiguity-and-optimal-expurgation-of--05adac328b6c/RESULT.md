# The exact single-insertion ambiguity and optimal expurgation of doubled-block words

## Finding

Let \(\Sigma\) be an alphabet with \(q\ge2\) distinct symbols and let \(m\ge1\). Consider the *doubled-block* family
\[
\mathcal C_{q,m}=\{UU:U=u_1\cdots u_m\in\Sigma^m\}\subseteq\Sigma^{2m}.
\]
This is repetition of a whole block, **not** symbol-by-symbol repetition. For \(W\in\Sigma^{2m+1}\), let \(L(W)\) be the number of distinct members of \(\mathcal C_{q,m}\) obtainable by deleting exactly one position of \(W\). Let \(N_j\) count the received words with \(L(W)=j\). Then the complete distribution is
\[
\begin{aligned}
N_2&=q^m-q,\\
N_1&=q^m\big((2m+1)q-2m\big)-2(q^m-q),\\
N_0&=q^{2m+1}-q^m(2m+1)(q-1)-q,
\end{aligned}
\]
with \(N_j=0\) for every \(j\ge3\). The \(N_2\) words are **exactly** \(UUu_1\) for nonconstant roots \(U=u_1\cdots u_m\). Each such word has the parents \(UU\) and \(\rho(U)\rho(U)\), where \(\rho(U)=u_2\cdots u_m u_1\). Every nonconstant root supplies a distinct ambiguous word.

Consequently, two different members \(UU\), \(VV\) have a common one-insertion output if and only if their roots are adjacent under cyclic rotation, i.e. \(V=\rho(U)\) or \(U=\rho(V)\). The confusability graph consists of one isolated vertex per constant root, one edge per rotation orbit of size two, and a simple cycle per orbit of size at least three.

Write
\[
P_q(d)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}
\]
for the number of primitive rotation classes of length \(d\), and put \(\alpha_d=2\) for even \(d\ge2\), \(\alpha_d=d\) for odd \(d\ge3\). The maximum cardinality of a one-insertion-correcting subcode of \(\mathcal C_{q,m}\) and the number of such maximum labeled subcodes are, respectively,
\[
\boxed{K_q(m)=q+\sum_{\substack{d\mid m\\d\ge2}}P_q(d)\lfloor d/2\rfloor},
\qquad
\boxed{A_q(m)=\prod_{\substack{d\mid m\\d\ge2}}\alpha_d^{P_q(d)}}.
\]
The empty sum and product have their usual values, giving \(K_q(1)=q\) and \(A_q(1)=1\). In particular, for every fixed \(q\ge2\), \(K_q(m)/q^m\to1/2\) as \(m\to\infty\).

## Assumptions and scope

Symbols are labeled, and words are linear, not identified up to reversal or rotation. A single insertion means insertion of exactly one freely chosen symbol into any of the \(2m+1\) gaps of a codeword; distinct resulting words are counted once, regardless of insertion history. A correcting subcode requires disjoint sets of one-insertion outputs for its distinct codewords. No primality or algebraic structure is assumed for the alphabet size.

## Proof

**At most two possible parents.** Fix any \(W=AcB\), with \(|A|=|B|=m\) and \(c\in\Sigma\). A deletion at or to the left of the center position leaves the last \(m\) symbols \(B\) intact, so a resulting doubled word must be \(BB\). A deletion at or to the right of the center leaves the first \(m\) symbols \(A\) intact, so it must be \(AA\). Thus \(L(W)\le2\). If \(A=B\), the potential parents coincide.

**Rigidity of two parents.** Suppose both parents exist and \(A\ne B\). Deleting a symbol in \(Ac\) must yield \(B\), and deleting a symbol in \(cB\) must yield \(A\). The first deletion cannot delete the last \(c\), nor can the second delete the leading \(c\), because either operation would imply \(A=B\). Let \(r\) be the first index with \(A_r\ne B_r\). For a deletion from \(Ac\) yielding \(B\), one may place the deleted position at \(r\): any earlier deletion crosses only an initial run of equal letters, so shifting it to \(r\) does not change the result. Therefore
\[
B_t=A_{t+1}\quad(r\le t\le m),\qquad A_{m+1}:=c.
\]
For the deletion from \(cB\) yielding \(A\), write the deleted position as \(j+1\) with \(1\le j\le m\). It cannot have \(j<r\), since then \(A_r=B_r\) would follow from the unchanged suffix. Thus \(j\ge r\), and the leading alignment gives
\[
A_1=c,\qquad A_t=B_{t-1}\quad(2\le t\le r).
\]
Because \(A_t=B_t\) for \(t<r\), induction gives \(A_1=\cdots=A_r=c\) and \(B_1=\cdots=B_{r-1}=c\). The displayed suffix equation then extends to all \(t\), giving \(B=A_2\cdots A_m c=\rho(A)\), with \(c=A_1\). Hence \(W=AAa_1\), where \(a_1\) is the first letter of \(A\). Conversely, if \(W=UUu_1\), deleting the final or initial position yields \(UU\) and \(\rho(U)\rho(U)\). These are distinct exactly when \(U\) is nonconstant. The first \(m\) letters recover \(U\), so there are exactly \(q^m-q\) different two-parent outputs.

**Complete spectrum.** For any fixed \(2m\)-letter word, the number of distinct length-\((2m+1)\) one-insertion outputs is \(q(2m+1)-2m\): insertions in separate gaps can coincide only when inserting the same symbol within its existing run; a run of length \(r\) contributes exactly \(r\) redundant placements, summing to \(2m\). Summing across the \(q^m\) codewords counts every received word \(L(W)\) times. Therefore \(N_1+2N_2=q^m[q(2m+1)-2m]\). Substitution of \(N_2=q^m-q\) gives \(N_1\), and subtraction from the universe \(q^{2m+1}\) gives \(N_0\).

**Graph and optimal subcodes.** The rigidity argument identifies every edge of the confusability graph as an unordered pair \(\{U,\rho(U)\}\), with \(U\) nonconstant. Each root has a unique least rotation period \(d\mid m\), and its orbit has \(d\) vertices. There are precisely \(P_q(d)\) such orbits, by standard Möbius inversion. An orbit with \(d=1\) is isolated; with \(d=2\) it is an edge; with \(d\ge3\) it is a cycle. A largest independent set has size \(1\) when \(d=1\) and \(\lfloor d/2\rfloor\) otherwise. For \(d\ge2\), the number of maximum independent sets is \(2\) for even \(d\) and \(d\) for odd \(d\). Independent choices across the orbit components give the two stated formulas. Finally, non-full-period roots number at most \(\sum_{d\mid m,\,d<m}q^d=O_q(q^{m/2})\), while full-period root orbits contribute fraction \(\lfloor m/2\rfloor/m\to1/2\). Therefore \(K_q(m)/q^m\to1/2\).

## Verification

The standalone `checker.py` constructs every distinct one-insertion word independently from every doubled-block parent; records its complete inverse list; compares the \(0\)-, \(1\)-, and \(2\)-parent populations with the formulas; and compares the computed confusability graph with root-rotation adjacency. It enumerates every maximum independent set inside each actual rotation orbit and compares the aggregate exact cardinality and number of optimal subcodes against the Möbius formula. It passes for all \(1\le m\le9\) at \(q=2\), all \(1\le m\le6\) at \(q=3\), and all \(1\le m\le4\) at \(q=4\). These computations are finite checks only; the proof above establishes the all-length claims.

## Relationship to prior work

Sala, Gabrys, Schoeny and Dolecek [1] study general intersections of insertion balls and reconstruction from synchronization codes. Their arXiv manuscript first appeared on April 11, 2016. The relevant theorem bounds maximum common supersequence populations for unconstrained sequence pairs; it does not furnish the doubled-block inverse-list distribution or the rotation-orbit maximum-subcode classification. Cheng, Guruswami, Haeupler and Li [2] discuss symbolwise two-fold repetition in the context of linear insertion/deletion codes, which is different from the whole-block map \(U\mapsto UU\). Published 2026 results on one-deletion confusability for palindromic codewords and on scattered square subsequences of cyclic permutation powers involve different code families and observations. The originality assessment is conditional on the accessible indexed literature; unpublished or unindexed equivalent classifications may exist.

## Limitations

The result addresses exactly one inserted symbol and a full doubled-block parent family over a fixed alphabet. It does not address two or more insertions, insertion/deletion mixtures, stochastic insertion-position weights, or optimal codes outside the doubled-block family. Exhaustive checks do not certify the infinite theorem independently. The literature search is not a proof of priority.

## References

[1] F. Sala, R. Gabrys, C. Schoeny and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, arXiv:1604.03000, first public version April 11, 2016, https://arxiv.org/abs/1604.03000.

[2] K. Cheng, V. Guruswami, B. Haeupler and X. Li, *Efficient Linear and Affine Codes for Correcting Insertions/Deletions*, arXiv:2007.09075, first public version July 17, 2020, https://arxiv.org/abs/2007.09075.
