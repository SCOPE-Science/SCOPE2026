# An exact omission law for entanglement on odd-order projective-plane graph states

## Finding

**Theorem (all-matchings entropy law).** Let \(\Pi\) be any finite projective plane of **odd order** \(q\ge3\), not necessarily Desarguesian. Write \(n=q^2+q+1\), and let \(B\in\mathbb F_2^{n\times n}\) denote its point-by-line incidence matrix. Prepare the pure qubit graph state of its bipartite incidence graph with ideal controlled-\(Z\) gates on all incidences. Choose **any** matching of omitted incidence gates
\[
F=\{(p_i,\ell_i):1\le i\le k\},\qquad 0\le k\le n,
\]
with all point endpoints distinct and all line endpoints distinct. Set \(D\in\mathbb F_2^{k\times k}\) by \(D_{ij}=B_{p_j,\ell_i}+\delta_{ij}\) modulo two, and define
\[
K_F=\begin{pmatrix}D&\mathbf1_k\\ \mathbf1_k^{\mathsf T}&0\end{pmatrix}\in\mathbb F_2^{(k+1)\times(k+1)}.
\]
For \(k=0\), interpret \(K_F\) as the one-by-one zero matrix. The **complete nonzero Schmidt spectrum** across the full point-versus-line bipartition is uniform on exactly \(2^{S(F)}\) coefficients, where
\[
\boxed{S(F)=n-\dim_{\mathbb F_2}\ker K_F\quad\text{bits}.}
\]
In particular every positive-order Rényi entropy equals the von Neumann entropy \(S(F)\).

The pristine graph state has \(S(\varnothing)=n-1\), while omitting **any one gate** gives the maximum possible \(S(F)=n\). If \(F\ne\varnothing\) is an *induced matching* (no selected point is incident to any selected line except its own matched line), then
\[
\boxed{S(F)=n-k+1.}
\]
Thus any two distinct omitted incidence gates on mutually nonincident cross-endpoints restore the original entropy \(n-1\), and each further omission preserving the induced-matching property reduces entropy by one bit. For two disjoint omitted gates the alternative is sharp: one cross-incidence gives maximum entropy \(n\), while zero cross-incidences give \(n-1\); both cross-incidences are impossible in a projective plane.

For every odd prime power \(q\), the Desarguesian plane \(\mathrm{PG}(2,q)\) has a conic with \(q+1\) distinct tangents that form an induced matching. Removing this set of gates has entropy \(n-q\), a loss of \(q-1\) bits relative to the pristine state, despite the one-omission increase. No such conic assertion is made for arbitrary non-Desarguesian planes.

## Assumptions and scope

A finite plane of order \(q\) has \(n=q^2+q+1\) points and lines, \(q+1\) incidences at each point and line, and exactly one common line through any two distinct points. Only the parity of \(q\) enters the all-matching rank theorem. \(\mathbb F_2\) arithmetic means bitwise addition. An omitted gate must be an actual incidence, and omissions are restricted to a matching; no other gate weights, noise, measurements, or alterations occur. The entropy concerns the full point-register versus full line-register cut, not a general subset bipartition.

## Proof

**1. Reduce graph-state entropy to binary incidence rank.** For a pure graph state, standard stabilizer bipartition theory (Hein, Eisert, Briegel [1]) gives a flat Schmidt spectrum of rank \(2^{\operatorname{rank}_{\mathbb F_2}A}\) when \(A\) is the adjacency submatrix crossing the partition. Omitting the matched gates changes the crossing block from \(B\) to \(B+UV^{\mathsf T}\), with \(U=(e_{p_1},\ldots,e_{p_k})\) and \(V=(e_{\ell_1},\ldots,e_{\ell_k})\). Therefore the entropy equals \(\operatorname{rank}_{\mathbb F_2}(B+UV^{\mathsf T})\).

**2. Prove the odd-order incidence inverse-on-even-vectors identity.** Because \(q+1\) is even, \(B\mathbf1=0\) and \(\mathbf1^{\mathsf T}B=0\) in characteristic two. Counting common lines of points gives the *integer* identity \(BB^{\mathsf T}=qI+J\), where \(J=\mathbf1\mathbf1^{\mathsf T}\). Reducing modulo two and using odd \(q\) gives
\[
BB^{\mathsf T}=I+J.
\]
Since \(n=q^2+q+1\) is odd, \(I+J\) has kernel exactly \(\langle\mathbf1\rangle\) and rank \(n-1\). Therefore \(\operatorname{rank}B=n-1\), both right and left kernels of \(B\) are spanned by \(\mathbf1\), and for every even-parity vector \(y\) (i.e. \(\mathbf1^{\mathsf T}y=0\)) one has \(BB^{\mathsf T}y=y\). This proves the pristine entropy \(n-1\) directly.

**3. Solve the faulted kernel exactly.** Let \(x\in\mathbb F_2^n\) satisfy \((B+UV^{\mathsf T})x=0\), and set \(z=V^{\mathsf T}x\in\mathbb F_2^k\). Then \(Bx=Uz\). Multiplication by \(\mathbf1^{\mathsf T}\) and the pairwise distinct point endpoints imply \(\mathbf1_k^{\mathsf T}z=0\). The identity from Step 2 gives the complete solution family
\[
x=B^{\mathsf T}Uz+c\mathbf1,\qquad c\in\mathbb F_2.
\]
Substituting \(z=V^{\mathsf T}x\) gives
\[
(I_k+V^{\mathsf T}B^{\mathsf T}U)z+c\mathbf1_k=0,\qquad\mathbf1_k^{\mathsf T}z=0,
\]
which is precisely \(K_F(z,c)^{\mathsf T}=0\), since the \((i,j)\) entry of \(V^{\mathsf T}B^{\mathsf T}U\) is \(B_{p_j,\ell_i}\). Conversely, every \((z,c)\in\ker K_F\) constructs a solution \(x\) by the displayed formula and satisfies \(V^{\mathsf T}x=z\). The correspondence is injective: if \(x=0\), then \(z=0\) and hence \(c=0\). Thus \(\ker(B+UV^{\mathsf T})\cong\ker K_F\) and the announced rank, entropy, and flat Schmidt spectrum follow. The same proof includes \(k=0\) when \(K_F=(0)\).

**4. Induced-matching and two-gate consequences.** For any matching, all diagonal entries of \(D\) vanish because each selected pair is incident. If the matching is induced, its cross-incidence matrix is \(I_k\), so \(D=0\). For \(k\ge1\), \(K_F(z,c)=0\) then forces \(c=0\) and \(\sum_i z_i=0\), a solution space of dimension \(k-1\). For \(k=1\), the same formula yields zero nullity and maximal entropy. For \(k=2\), two cross-incidences would place two distinct points on two distinct lines, contradicting the unique-line axiom. Therefore \(D\) is either zero or has exactly one off-diagonal one; direct elimination of the displayed three-by-three \(K_F\) gives nullity one or zero respectively.

**5. Conic tangent construction for all odd prime powers.** In \(\operatorname{PG}(2,q)\) with \(q\) odd, for each \(t\in\mathbb F_q\) take the point \(P_t=[t^2:t:1]\) and tangent \(\ell_t=[1:-2t:t^2]\), and append \(P_\infty=[1:0:0]\) and \(\ell_\infty=[0:0:1]\). Their incidence evaluation is \(\ell_t(P_s)=(s-t)^2\), so \(P_s\) belongs to \(\ell_t\) only when \(s=t\); no finite point lies on \(\ell_\infty\) and \(P_\infty\) lies on no finite \(\ell_t\). The \(q+1\) flags are distinct and form an induced matching. Step 4 gives \(S=n-(q+1)+1=n-q\). The construction needs odd characteristic so that \(\ell_t\) is the usual conic tangent; its incidence conclusion follows directly from the displayed dot products.

## Verification

The accompanying complete standard-library `VERIFY.py` independently constructs normalized point and line coordinates of \(\operatorname{PG}(2,p)\) for prime orders \(p=3,5,7,11\); computes binary ranks of the original and faulted incidence matrices by exact bitwise Gaussian elimination; and separately computes the smaller \(K_F\) ranks. It checks every single omitted incidence in each plane, all two-edge incidence matchings of the ternary plane, seeded finite samples of longer matchings, and each full conic-tangent matching. The four exact check totals are \(1723,937,1207,1947\), totaling \(5814\) cases. For those prime orders, the baseline ranks are respectively \(12,30,56,132\), and the conic-induced entropies are \(10,26,50,122\). The proof in Steps 1–5, not these finite tests, establishes the all-matching result for every finite odd-order plane and the conic construction for every odd prime power.

## Relationship to prior work

Hein, Eisert and Briegel [1] prove the general stabilizer cut-rank law used in Step 1 and give general edge-variation statements; these foundational tools are not new. Cautrès and coauthors [2] explicitly study the *same projective-plane incidence graphs* as graph-state resources (Section 4.2), but their results concern vertex-minor universality and pairability, not the entropy after omitting arbitrary incidence matchings. The published *even-order* projective-plane matching-omission theorem [3] has a complementary, genuinely different hypothesis and effect: it proves a positive one-bit-per-omission gain up to its threshold in even-order planes; its characteristic-two incidence-code argument does not apply to odd order. A separate published order-three incidence-graph induced-matching census [4] describes eligible fault patterns but not quantum entropies under their removal. The claimed contribution is the exact arbitrary-size compressed odd-order entropy law, including its structural induced-matching reversal and conic family. An unindexed preexisting equivalent binary-rank identity remains a historical-priority risk; no independent priority certification is asserted.

## Limitations

These are ideal pure qubit graph states with an exact point-versus-line partition and matchings of missing controlled-\(Z\) gates. There is no assertion about arbitrary nonmatching fault patterns, noisy or weighted gates, different partitions, fault probabilities, scalable preparation overhead, or experimental advantage. The all-plane formula needs odd order; the explicit conic lower-entropy example needs the Desarguesian construction. Finite exact calculations support but do not replace the general proof. Historical priority has not been independently established.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first publicly posted 18 July 2003, https://arxiv.org/abs/quant-ph/0307130 ; especially the bipartition stabilizer results.
2. M. Cautrès, N. Claudet, M. Mhalla, S. Perdrix, V. Savin and S. Thomassé, *Vertex-minor universal graphs for generating entangled quantum subsystems*, arXiv:2402.06260 (2024), Section 4.2, https://arxiv.org/html/2402.06260v3 .
3. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes*, published mathematical research record dated 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768 .
4. *Induced-matching and saturation spectra of the order-three projective-plane Levi graph*, published mathematical research record dated 13 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-induced-matching-and-saturation-spectra-of-the-order-three-proje--4180b85d8592 .
