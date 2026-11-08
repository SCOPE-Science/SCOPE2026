# A three-halves clock law for reversible waves on nilpotent-base graph prisms

## Finding

Let \(H\) be any nonempty finite simple graph, let \(B\) be its adjacency matrix over \(\mathbb F_2\), and suppose \(B\) is nilpotent with Jordan-block lengths \(s_1,\ldots,s_b\). Construct its matched prism \(G=H\square K_2\), in which two copies of \(H\) are joined by a perfect matching. For every finite field \(\mathbb F_q\), \(q=2^f\), form the reversible graph wave
\[
T_G(u,v)=(A_Gu+v,u),\qquad (u,v)\in\mathbb F_q^{V(G)}\times\mathbb F_q^{V(G)}.
\]
Define the multiset \(\mathcal L\) by replacing each even \(s_i\) by \((s_i,s_i)\) and each odd \(s_i\) by \((s_i+1,s_i-1)\), omitting zero entries. Put
\[
R=\left\lceil\log_2\max\mathcal L\right\rceil,\qquad
E_j=2\sum_{\ell\in\mathcal L}\min(\ell,2^j)\quad(j\ge0).
\]
Then \(\operatorname{ord}(T_G)=3\cdot2^R\), and the exact fixed-point count of its \(t\)-th iterate is
\[
\#\operatorname{Fix}(T_G^t)=
\begin{cases}
1,&3\nmid t,\\
q^{E_{\nu_2(t)}},&3\mid t.
\end{cases}
\]
In particular, its only nonzero primitive-period populations are
\[
P_1=1,\quad P_3=q^{E_0}-1,\quad
P_{3\cdot2^j}=q^{E_j}-q^{E_{j-1}}\quad(1\le j\le R).
\]
All these populations are positive. The number of primitive temporal orbits of length \(p\) is \(P_p/p\).

For the same base \(H\), the two-level wave \(T_H(u,v)=(Bu+v,u)\) has order \(2^{1+\lceil\log_2 s\rceil}\), where \(s=\max_i s_i\). Consequently, matching each base vertex to a second copy **changes the entire clock from a power of two to a multiple of three**, and gives the sharp order ratio
\[
\frac{\operatorname{ord}(T_G)}{\operatorname{ord}(T_H)}=
\begin{cases}
3,&B=0,\\
\dfrac32,&B\ne0\text{ and nilpotent}.
\end{cases}
\]
The ratio is valid for disconnected as well as connected bases.

An explicit infinite connected family is \(H=P_{2^a-1}\), \(a\ge2\). Its adjacency has one nilpotent block of length \(n=2^a-1\); the open ladder \(P_n\square K_2\) has prism-block lengths \(n+1\) and \(n-1\), hence exact wave order \(3\cdot2^a\). Its fixed-point exponent when \(3\mid t\) is
\[
E_j=2\bigl(\min(2^a,2^j)+\min(2^a-2,2^j)\bigr),
\quad j=\nu_2(t),
\]
and the primitive-period formula above applies without any further enumeration.

## Assumptions and scope

All graphs are finite, undirected, simple, and labelled by their vertices; isolated vertices and disconnected bases are permitted. Nilpotence is over \(\mathbb F_2\), equivalently over any characteristic-two extension. The wave state is the ordered pair of consecutive vertex configurations; counting individual vertex configurations instead would not be this invariant. All periods are **least positive temporal periods**, every wave state is immediately periodic because the update is invertible, and \(\nu_2(t)\) denotes the exponent of two in a positive integer \(t\). The two copies of \(H\) are adjacent along the canonical perfect matching; this is the ordinary Cartesian graph product. The empty base graph is excluded.

## Proof

**1. Nilpotent Jordan blocks under a matched doubling.** On the vector space for \(G\), use a tensor factor for the two layers. In characteristic two, the adjacency of \(K_2\) has the form \(S=I+N\), where \(N^2=0\) and \(N\) is similar to a single size-two nilpotent Jordan block. Thus
\[
A_G=B\otimes I_2+I\otimes S
=I+M,\qquad M=B\otimes I_2+I\otimes N.
\]
For a size-\(s\) nilpotent Jordan block of \(B\), identify its contribution to \(M\) with multiplication by \(x+y\) on the \(2s\)-dimensional algebra
\[
\mathbb F_q[x,y]/(x^s,y^2).
\]
Its square is multiplication by \(x^2\), so its nilpotency index is \(s\) for even \(s\), \(s+1\) for odd \(s\). The number of Jordan blocks is the dimension of the quotient by \((x+y)\), namely \(\min(s,2)\). For \(s\ge2\) there are exactly two blocks. Their sum of lengths is \(2s\), so even \(s\) gives \((s,s)\), whereas odd \(s\ge3\) gives \((s+1,s-1)\). For \(s=1\) there is a single block of length two, agreeing with the claimed convention. This proves that the nilpotent Jordan multiset of \(M=A_G+I\) is exactly \(\mathcal L\), and that \(A_G\) is invertible.

**2. A general unipotent-adjacency wave identity.** On the doubled wave-state space write \(\widehat A=\operatorname{diag}(A_G,A_G)\) and \(\widehat M=\operatorname{diag}(M,M)\). Since the companion wave matrix satisfies \(T_G^2=\widehat A T_G+I\), with \(\widehat A\) commuting with \(T_G\), one obtains
\[
T_G^3+I=\widehat M^2T_G+\widehat M
=\widehat M(I+\widehat M T_G).
\]
The second factor is invertible because \(\widehat M T_G\) is nilpotent, and it commutes with \(\widehat M\). Consequently
\[
\dim\ker(T_G^3+I)^{2^j}
=\dim\ker\widehat M^{2^j}
=2\sum_{\ell\in\mathcal L}\min(\ell,2^j)=E_j.
\]
For an odd \(h\), the factorization of \((T_G^3)^h+I\) shows that the remaining factor after \(T_G^3+I\) is invertible (it equals \(I\) modulo the nilpotent \(T_G^3+I\)). Therefore \(\dim\ker(T_G^t+I)=E_{\nu_2(t)}\) whenever \(3\mid t\). Since \(A_G\) is invertible, \(T_G+I\) is invertible (eliminate the two wave-state components). The minimal polynomial of \(T_G\) hence divides a power of \(z^2+z+1\), and \(T_G^t+I\) is invertible whenever \(3\nmid t\). Over \(\mathbb F_q\), a kernel of dimension \(d\) contains exactly \(q^d\) states. This proves the fixed-point formula.

The nilpotency index of \(T_G^3+I\) is \(L=\max\mathcal L\), because its invertible factor preserves the nilpotency index of \(\widehat M\). Thus \(T_G^{3\cdot2^R}=I\) but \(T_G^{3\cdot2^{R-1}}\ne I\), and all eigenvalues are primitive cube roots of unity. Its exact order is \(3\cdot2^R\). Subtracting the nested sets of states fixed by the iterates of periods \(3\cdot2^j\) gives the displayed primitive populations. Strict positivity follows from a block of maximal length \(L>2^{R-1}\), as well as \(E_0>0\).

**3. Comparison with the base wave.** Its matrix satisfies \(T_H^2+I=\widehat B T_H\), where \(\widehat B=\operatorname{diag}(B,B)\) is nilpotent and commutes with \(T_H\). Hence \(T_H\) has exact order \(2^{1+\lceil\log_2 s\rceil}\). If \(s\ge2\), the parity transformation in step 1 has maximal length \(L\) satisfying \(2^{R-1}<L\le2^R\) for \(R=\lceil\log_2 s\rceil\); equivalently \(\lceil\log_2 L\rceil=\lceil\log_2 s\rceil\). If \(s=1\), necessarily \(B=0\), and \(L=2\). The asserted order ratios follow.

**4. Dyadic paths.** Let \(f_n(z)\) be the characteristic polynomial of path adjacency on \(n\) vertices, with \(f_0=1\), \(f_1=z\), and \(f_n=zf_{n-1}+f_{n-2}\) over \(\mathbb F_2\). Expanding the path determinant at its central vertex gives \(f_{2k+1}=z f_k^2\): the two off-center contributions agree and cancel in characteristic two. Induction then gives \(f_{2^a-1}(z)=z^{2^a-1}\). The first endpoint vector is cyclic for the path adjacency: its \(j\)-th image has a unique length-\(j\) route to vertex \(j+1\), so its Krylov vectors are independent for \(0\le j<n\). Thus the matrix is a single nilpotent Jordan block of length \(n\); the stated ladder census follows from steps 1–3.

## Verification

Both supplied standalone Python programs use only the standard library and exact bit-vector arithmetic over \(\mathbb F_2\). Run `python3 check_matrix.py` and `python3 check_states.py` in the directory containing the extracted files. Their recorded outputs are `check_matrix.out` and `check_states.out`.

The matrix checker examined all 1,099 labelled simple base graphs with at most five vertices. Exactly 278 had nilpotent binary adjacency and were tested against the predicted prism Jordan decomposition, exact order, and 4,170 independent time-fixed-space comparisons. It also verified the dyadic open ladders with lengths 3, 7 and 15 (orders 12, 24 and 48). The second checker directly enumerated all 4,096 ordered binary two-time-level states of the six-vertex open ladder and obtained primitive populations \(P_1=1\), \(P_3=15\), \(P_6=240\), and \(P_{12}=3840\). These are finite consistency checks; the arbitrary-graph theorem is proved algebraically above. For extension fields, the proof is valid by scalar extension and the same kernel dimensions, without exhaustive extension-field simulation.

## Relationship to prior work

The second-order reversible automaton mechanism and companion-matrix method are established in Macfarlane (2004), and the explicit general reversible construction is in Steeb and Hardy (2007), whose full article was inspected (especially its construction and one-dimensional wave example). Norman (2008) treats the general modular Kronecker-sum Jordan-form problem, which covers the algebraic Jordan-block subproblem; no novelty is asserted for that stand-alone subproblem. The present graph-theoretic statement combines the matched-prism operation with the two-time-level wave and derives its full arbitrary-graph orbit census and universal clock ratio. The available material did not identify a prior theorem that already states or entails this combined dynamical result without further prism-specific analysis.

Closely related graph-wave computations for paths, periodic ladders, Hamming products, and one-leaf-per-vertex coronas concern different graph operations or different dynamical maps. In particular, a corona adds leaves to the base and doubles nilpotent block lengths, whereas a matched prism replaces lengths by a parity-dependent pair; their clock-transfer ratios are different.

## Limitations

The theorem requires nilpotent binary adjacency; it does not classify arbitrary base graphs whose adjacency has nonzero eigenvalues. Source priority is qualified: the accessible Macfarlane and Norman materials did not include their full articles, so an equivalent differently formulated consequence in those texts or unindexed literature cannot be excluded. The generic Kronecker-sum Jordan computation is known and should not be attributed to this theorem. No independent audit has yet been performed; empirical replay cannot certify general correctness or historical uniqueness.

## References

1. A. J. Macfarlane, “Linear reversible second-order cellular automata and their first-order matrix equivalents,” *Journal of Physics A* **37** (2004), 10791–10814. DOI: `10.1088/0305-4470/37/45/006`. Publisher records publication on October 28, 2004.
2. W.-H. Steeb and Y. Hardy, “One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations,” *Zeitschrift für Naturforschung A* **62** (2007), 569–572. DOI: `10.1515/zna-2007-10-1103`. Full article available online.
3. C. W. Norman, “On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic,” *Linear and Multilinear Algebra* **56** (2008), 415–451. DOI: `10.1080/03081080701395640`.
