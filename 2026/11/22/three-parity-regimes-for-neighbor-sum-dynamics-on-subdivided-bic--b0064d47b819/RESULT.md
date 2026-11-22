# Three parity regimes for neighbor-sum dynamics on subdivided bicliques

## Finding

Let \(m,n\ge2\), let \(S(K_{m,n})\) be the ordinary subdivision of every edge of the complete bipartite graph, and let \(F\) simultaneously replace each vertex state by the sum of its open neighbors' states over any finite field \(\mathbb F_q\), where \(q=2^f\) and \(f\ge1\). There are \(d=mn+m+n\) state coordinates. The complete Jordan form is determined by the parity of the two shore sizes, as follows. Here \(J_j(\lambda)\) means one Jordan block of size \(j\) with eigenvalue \(\lambda\); multiplicity zero means no block.

| Shore parity | Eigenvalue-zero blocks | Eigenvalue-one blocks | Maximum first periodic-entry time | Possible least periods |
|---|---|---|---|---|
| Both even | \(J_4(0)^{\oplus2}\), \(J_3(0)^{\oplus(m+n-4)}\), \(J_1(0)^{\oplus(m-2)(n-2)}\) | None | 4 | 1 |
| Both odd | \(J_3(0)\), \(J_1(0)^{\oplus(m-1)(n-1)}\) | \(J_2(1)^{\oplus(m+n-2)}\) | 3 | 1, 2 |
| Mixed parity, \(e\) even and \(o\) odd | \(J_3(0)^{\oplus(o-1)}\), \(J_1(0)^{\oplus((e-2)(o-1)+1)}\) | \(J_4(1)\), \(J_2(1)^{\oplus(e-2)}\) | 3 | 1, 2, 4 |

Every listed maximum is attained. In particular, both even shores cause universal extinction after *exactly four* updates in the worst case; one even and one odd shore produce genuine four-cycles; both odd shores produce only fixed states and two-cycles. All statements hold for every permitted size and every characteristic-two finite field.

Write \(P_j\) for the number of states having least temporal period \(j\). Then the complete primitive cycle census is:

- Both even: \(P_1=1\) and every other \(P_j=0\).
- Both odd: \(P_1=q^{m+n-2}\) and \(P_2=q^{2(m+n-2)}-q^{m+n-2}\).
- Mixed parity: \(P_1=q^{e-1}\), \(P_2=q^{2e-2}-q^{e-1}\), and \(P_4=q^{2e}-q^{2e-2}\).

The number of *primitive orbits* of length \(j\) is \(P_j/j\). The nilpotent dimension \(b\), respectively, is \(d\), \((m-1)(n-1)+3\), or \(eo-e+o\). Every periodic state has exactly \(q^b\) configurations in its eventual projection fiber, so **every individual** primitive orbit of period \(j\) has an attraction basin of exactly \(j q^b\) initial configurations.

There is also a complete entry-time census. Let \(H_t\) denote the number of states already periodic after at most \(t\) updates, and let \(d=mn+m+n\). The sequence of exponents \(\log_q H_t\) for the listed consecutive times is

\[
\begin{array}{ll}
\text{both even},\ t=0,1,2,3,4:&(0,\ d-2(m+n-1),\ mn,\ d-2,\ d),\\
\text{both odd},\ t=0,1,2,3:&(2(m+n-2),\ 2(m+n-2)+(m-1)(n-1)+1,\\
&\quad 2(m+n-2)+(m-1)(n-1)+2,\ d),\\
\text{mixed},\ t=0,1,2,3:&(2e,\ 2e+(e-1)(o-1)+1,\\
&\quad 2e+e(o-1)+1,\ d).
\end{array}
\]

Each exact first-entry population is \(H_t-H_{t-1}\), with \(H_{-1}=0\), and \(H_t=q^d\) after the final listed time. These numbers also give all period-resolved entry counts: multiply each exact-entry population by \(P_j/\sum_iP_i\), because all periodic points have identical nilpotent fibers. The fraction is exact, not asymptotic.

## Assumptions and scope

A subdivision vertex corresponds to every ordered edge label \((i,j)\) with \(1\le i\le m\), \(1\le j\le n\). Only the two incidence edges between it and its endpoints remain; the original biclique edges are removed. The state is a triple \((x,y,z)\in\mathbb F_q^m\oplus\mathbb F_q^n\oplus\mathbb F_q^{mn}\). There are no self-loops or weighted coefficients. Write \(R_i=\sum_jz_{ij}\), \(C_j=\sum_iz_{ij}\), \(X=\sum_ix_i\), \(Y=\sum_jy_j\), and \(T=\sum_iR_i=\sum_jC_j\). Then

\[
F(x,y,z)=\bigl((R_i)_i,(C_j)_j,(x_i+y_j)_{ij}\bigr).
\]

The temporal period is the least positive \(p\) with \(F^p(s)=s\), applicable only to periodic states. The first periodic-entry time is the least nonnegative \(t\) for which \(F^t(s)\) is periodic. No result is claimed for odd characteristic, nonuniform edge weights, or asynchronous updating.

## Proof

**1. Incidence decomposition.** Let \(B\) be the \((m+n)\)-by-\(mn\) unsigned incidence matrix of the base biclique. Then

\[
F=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad
F^2=\operatorname{diag}(Q,L),\quad Q=BB^{\mathsf T},\quad L=B^{\mathsf T}B.
\]

With \(\alpha=n\bmod2\), \(\beta=m\bmod2\), the formulas become

\[
Q(x,y)=((\alpha x_i+Y)_i,(\beta y_j+X)_j),\qquad
(Lz)_{ij}=R_i+C_j,
\]

and

\[
(L^2z)_{ij}=\alpha R_i+\beta C_j.
\]

Because the base biclique is connected, \(\operatorname{rank}B=m+n-1\). Its image is precisely the zero-total-sum subspace \(W\) of the original-coordinate space, and \(\ker B^{\mathsf T}\) consists of the global constants. In particular, \(\operatorname{rank}F=2(m+n-1)\).

**2. Power ranks.** The rank of \(L\) equals the rank of \(B^{\mathsf T}|_W\), hence is \(m+n-2\) when \(m+n\) is even, otherwise \(m+n-1\). Directly from the displayed formula for \(Q\), its ranks in the both-even, both-odd, and mixed cases are respectively \(2\), \(m+n-1\), and \(e\). This proves the second-power ranks below. For the third power, use

\[
\operatorname{rank}F^3=\operatorname{rank}(Q B)+\operatorname{rank}(B^{\mathsf T}Q).
\]

The first summand is the rank of \(Q|_W\). The second is the rank of \(Q\) after quotienting its image by any intersection with the global constants. Their values are \((1,1)\), \((m+n-2,m+n-2)\), and \((e,e)\) in the three cases. Iterating the same formulas shows the ranks stabilize after the third power except when both parts are even, when \(F^4=0\). Thus

\[
\begin{array}{c|ccccc}
&\operatorname{rank}F^0&\operatorname{rank}F^1&\operatorname{rank}F^2&\operatorname{rank}F^3&\operatorname{rank}F^4\\
\text{even/even}&d&2(m+n-1)&m+n&2&0\\
\text{odd/odd}&d&2(m+n-1)&2(m+n)-3&2(m+n-2)&2(m+n-2)\\
\text{mixed}&d&2(e+o-1)&2e+o-1&2e&2e.
\end{array}
\]

The same explicit \(Q\) and \(L\) identities give \(F^4=0\) in the even/even case, \(F^5=F^3\) in the odd/odd case, and \(F^7=F^3\) in the mixed case (check the two off-diagonal blocks separately). These identities verify the claimed recurrent periods, rather than merely inferring them from rank stabilization. These ranks hold over every characteristic-two extension, because all row operations involve the prime subfield.

**3. Characteristic polynomial and unit blocks.** As \(mn\ge m+n\), the block determinant identity gives

\[
\chi_F(t)=t^{mn-m-n}\det(t^2I_{m+n}-Q).
\]

The explicit \(Q\) formula yields eigenvalue-one multiplicity zero, \(m+n-2\), or \(e\) on \(Q\), respectively, in the three parity regimes, and all other eigenvalues are zero. Thus the generalized eigenvalue-one space of \(F\) has dimension \(0\), \(2(m+n-2)\), or \(2e\). The rank stabilization in Step 2 identifies it with \(\operatorname{im}F^4\), and the complementary generalized zero-eigenspace is killed within four updates.

Solving \(F(x,y,z)=(x,y,z)\) reduces to \(Q(x,y)=(x,y)\) and \(z=B^{\mathsf T}(x,y)\). This gives fixed-space dimensions \(m+n-2\) in the odd/odd case and \(e-1\) in the mixed case. Solving \(F^2(s)=s\) similarly gives dimensions \(2(m+n-2)\) and \(2e-2\). For the latter calculation, \(Q(x,y)=(x,y)\) has dimension \(e-1\), and \(Lz=z\) has dimension \(e-1\): indeed, when \(e\) is even and \(o\) odd, it forces \(z_{ij}=R_i\) with \(\sum_iR_i=0\).

For both odd, the generalized unit space has only blocks of size two (as its total dimension is twice its fixed-space dimension and \(F^2\) is the identity there). For mixed parity, the unit space has period dividing four. Its total, fixed, and two-step fixed dimensions show that there are no unit blocks of size one and that either one block of size four or two blocks of size three occur. To distinguish them, choose a basis vector supported at one vertex of the even shore and let \(w=F^3(v)\), which is periodic. Direct substitution gives

\[
(F+I)^3w=(\mathbf1_e,\mathbf0_o,\mathbf1_{eo})\ne0.
\]

Therefore a size-four unit block occurs, and it must be unique; the remaining \(e-2\) unit blocks have size two.

**4. Zero blocks and exact counts.** The nonzero-eigenvalue blocks are now determined. Subtracting their rank contributions from the power-rank table and taking successive rank differences determines the zero blocks, giving exactly the three Jordan decompositions in the Finding. The largest zero block has size four (both even) or three (other cases), proving all sharp entry bounds. In characteristic two, \((I+N)^{2^a}=I+N^{2^a}\) for nilpotent \(N\), so the unit blocks of size two and four have order exactly two and four, respectively. Their fixed spaces under the first, second, and fourth powers yield the stated \(P_j\) by subtraction. Since the zero/unit generalized-eigenspace splitting is canonical and \(F\) acts invertibly on the unit space, the first periodic entry of a vector is precisely the first extinction of its zero component. Consequently \(H_t=q^{r+\dim\ker N^t}\), where \(r\) is the unit-space dimension. Summing \(\min(t,j)\) over the explicit zero-block sizes gives every exponent displayed above. A periodic vector has exactly \(q^b\) preimages under the canonical projection onto the unit space, independently of its period or coordinates. This proves all individual orbit-basin and period-resolved entry formulas.

## Verification

Two standalone Python 3 programs reproduce independent finite checks. `verify_ranks.py` constructs the full zero-diagonal adjacency matrix and computes binary ranks of its first four powers by integer-bitset Gaussian elimination, comparing all 49 ordered size pairs \(2\le m,n\le8\) against the theorem and checking the predicted fixed dimensions. `verify_states.py` constructs neighbor masks directly and exhaustively traces every initial binary configuration for the eight pairs \((2,2),(2,3),(3,2),(2,4),(3,3),(2,5),(3,4),(4,3)\), totaling 1,233,152 states. It checks primitive orbit populations and every exact first-entry population without invoking the matrix-rank algorithm. Both print `RANK_CHECK_OK` and `STATE_CHECK_OK` respectively. These tests support correctness but are not proofs for unbounded sizes or larger finite fields; the preceding algebraic argument establishes those claims.

## Relationship to prior work

Moreno, Bollman and Aviño-Díaz [1] develop the finite-field linear-dynamical viewpoint but do not calculate this graph family's orbit structure. Barrett and collaborators [2] study *minimum rank among matrices with an allowed graph pattern* for subdivisions; their optimized, diagonal-unrestricted rank invariant does not determine the powers or Jordan structure of the one fixed adjacency matrix here. Pasqualetti, Borra and Bullo [3] give general finite-field consensus and nilpotent Jordan criteria, but not the explicit three-parity biclique-subdivision census.

The related published work [4] treats the exact adjacency update on subdivided **cliques** and characterizes when a connected base graph gives extinction within three steps; this rules out three-step extinction for our biclique bases but does not imply four-step extinction, the mixed-shore four-cycles, or the present Jordan and basin counts. The related [5] treats the **edge-state** line graph of an all-even multipartite base, whose update is \(B^{\mathsf T}B\). Its two-step nilpotence for even-even bicliques is a proper operator factor inside \(F^2\), not a classification of the alternating original-vertex/edge-state dynamics; it does not cover odd shores. The formulas above explicitly resolve the resulting parity regimes. Priority over unindexed equivalent results is not claimed.

## Limitations

This theorem concerns ordinary once-subdivided bicliques, not arbitrary subdivisions or weighted incidence graphs. It is specific to characteristic two and synchronous zero-diagonal open-neighbor summation. All formal implications are algebraic; the numerical checks are finite corroboration only. Although the cited relevant literature and research records were compared by their mathematical implications, other unindexed or inaccessible treatments could contain an equivalent family-specific Jordan calculation; independent historical and mathematical review has not been performed.

## References

[1] O. Moreno, D. Bollman and M. A. Aviño-Díaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1, first public release 2006-04-25, https://arxiv.org/abs/math/0604534.

[2] W. Barrett, R. Bowcutt, M. Cutler, S. Gibelyou and K. Owens, *Minimum rank of edge subdivisions of graphs*, Electronic Journal of Linear Algebra 18 (2009), 530–563, https://doi.org/10.13001/1081-3810.1330.

[3] F. Pasqualetti, D. Borra and F. Bullo, *Consensus Networks over Finite Fields*, arXiv:1301.4587v1, first public release 2013-01-19, https://arxiv.org/abs/1301.4587.

[4] *Three-step extinction rigidity and parity-swapped cycles on subdivided cliques*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-three-step-extinction-rigidity-and-parity-swapped-cycles-on-subd--88cbaceccac4/RESULT.md.

[5] *Three-step edge-parity extinction and a part-count Jordan law for even multipartite graphs*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-three-step-edge-parity-extinction-and-a-part-count-jordan-law-fo--2fda8d5e0d01/RESULT.md.
