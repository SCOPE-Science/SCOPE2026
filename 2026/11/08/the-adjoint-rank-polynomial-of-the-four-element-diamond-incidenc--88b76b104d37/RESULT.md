# The adjoint-rank polynomial of the four-element diamond incidence algebra

## Finding
Let \(P\) be the four-element diamond poset with relations \(0<1<3\), \(0<2<3\), and no relation between \(1\) and \(2\). For every prime power \(q\), let \(A=I(P,\mathbb F_q)\), the nine-dimensional associative incidence algebra, and let \(\operatorname{ad}_x(y)=xy-yx\). Then the exact rank-generating polynomial of the **element-indexed** inner derivations is
\[
\begin{aligned}
R_q(T):=\sum_{x\in A}T^{\operatorname{rank}\operatorname{ad}_x}
={}&q+q(q-1)T+2q^2(q-1)(q+2)T^2\\
&+2q^2(q-1)(3q^2+2q-3)T^3\\
&+q^2(q-1)(5q^4+4q^3-11q^2-5q+3)T^4\\
&+q^4(q-1)(q^4+q^3-4q^2-3q+6)T^5.
\end{aligned}
\]
Every rank from \(0\) through \(5\) occurs, in every characteristic. The center is \(\mathbb F_q1\), so each distinct inner derivation occurs as \(\operatorname{ad}_x\) for exactly \(q\) different elements; its enumerator is \(R_q(T)/q\). Thus the commuting probability of two uniformly sampled elements is exactly \(q^{-9}R_q(q^{-1})\).

In the first field \(\mathbb F_2\), the element-indexed rank multiplicities are \((2,2,32,104,244,128)\); in \(\mathbb F_3\) they are \((3,6,180,1080,7236,11178)\). The diamond is the smallest connected poset with two incomparable interior elements connecting a bottom to a top: it has a nonzero radical square, unlike height-two incidence algebras. The fifth possible rank and its exact multiplicity measure this extra two-step interval interaction.

## Assumptions and scope
The field is exactly \(k=\mathbb F_q\), for any prime power \(q\ge2\); no characteristic exclusion is used. The poset has precisely the four specified vertices. In the ordered basis of matrix units
\[
(e_{00},e_{11},e_{22},e_{33},e_{01},e_{02},e_{13},e_{23},e_{03}),
\]
write \(x\in A\) using diagonal coordinates \(d_0,d_1,d_2,d_3\), edge coordinates \(a,b,c,d\), and long-interval coordinate \(e\). The rank is the rank over \(k\) of the nine-by-nine linear map \(\operatorname{ad}_x\). The count is over all \(q^9\) elements, **not** over conjugacy classes or only over distinct maps.

## Proof
For a second element \(y\), write its diagonal coordinates \(v_0,v_1,v_2,v_3\) and its five interval coordinates \(u_{01},u_{02},u_{13},u_{23},u_{03}\). The diagonal commutator entries vanish. In the five interval coordinates the commutator \([x,y]\) has rows
\[
\begin{aligned}
&\alpha u_{01}+a(v_1-v_0),\\
&\beta u_{02}+b(v_2-v_0),\\
&\gamma u_{13}+c(v_3-v_1),\\
&\delta u_{23}+d(v_3-v_2),\\
&\eta u_{03}+e(v_3-v_0)+a u_{13}+b u_{23}-c u_{01}-d u_{02},
\end{aligned}
\]
where \(\alpha=d_0-d_1\), \(\beta=d_0-d_2\), \(\gamma=d_1-d_3\), \(\delta=d_2-d_3\), and \(\eta=d_0-d_3=\alpha+\gamma=\beta+\delta\). This identity follows directly from \(e_{ij}e_{jk}=e_{ik}\), in particular the two products \(e_{01}e_{13}=e_{03}\) and \(e_{02}e_{23}=e_{03}\). All later rank claims concern this explicit five-row matrix.

We first condition on \(d_0\ne d_3\). Then \(\eta\ne0\), so the last row has a private pivot in the \(u_{03}\) column. The first four rows split into the two length-two chains. For either chain, when the middle diagonal value equals one endpoint there is one unequal edge and one equal edge; its row-rank polynomial, after summing over its two arrow coefficients, is \(qT(1+(q-1)T)\). There are two endpoint choices. For each of the remaining \(q-2\) middle diagonal values, both edges have unequal diagonals, giving \(q^2T^2\). Thus define
\[
F_q(T)=2qT(1+(q-1)T)+(q-2)q^2T^2.
\]
The two chains use separate pivot columns, and the equal-edge rows are independent because they form a forest. The coordinate \(e\) is arbitrary, so the entire contribution from \(d_0\ne d_3\) is \(q^2(q-1)T F_q(T)^2\).

Now suppose \(d_0=d_3\). For each of the two middle vertices, say a chain is *active* when its diagonal differs from \(d_0\). Let \(k\in\{0,1,2\}\) be the number of active chains. Each condition depends only on equality, not on the numerical values of the nonzero diagonal differences.

For \(k=2\), the first four rows have four private pivots. Elimination leaves the final row a scalar multiple of \(v_3-v_0\), with scalar \(e+ac/\alpha+bd/\beta\). Every choice of the four short-arrow coefficients yields exactly one \(e\) making this scalar zero. Hence the rank polynomial over the five interval coefficients is
\[
P_2(T)=q^4(T^4+(q-1)T^5).
\]

For \(k=1\), assume without loss that the chain through vertex \(1\) is active. Its first and third rows give two pivots. The other two rows are multiples of the independent diagonal forms \(v_2-v_0\) and \(v_3-v_2\), controlled by \(b,d\). If at least one of \(b,d\) is nonzero, the final row has a private pivot in the corresponding arrow input column; it raises rank by one. If both vanish, it raises rank precisely when \(e+ac/\alpha\ne0\). Counting the cases of zero, one, or two nonzero values among \(b,d\) yields
\[
P_1(T)=q^2T^2+q^2(q-1)T^3+2(q-1)q^3T^4+(q-1)^2q^3T^5.
\]

For \(k=0\), all four diagonals coincide. The first four commutator rows are the weighted incidence rows of the four-cycle on \(0,1,3,2\), supported where \(a,b,c,d\) are nonzero. For a nonempty support, its graphic rank is the number of edges unless all four are present, in which case it is three. The final row then has a private nonzero short-arrow coefficient and is independent. If all four coefficients vanish, the final row has rank one precisely when \(e\ne0\). Consequently
\[
P_0(T)=1+(q-1)T+4q(q-1)T^2+6q(q-1)^2T^3+q\bigl(4(q-1)^3+(q-1)^4\bigr)T^4.
\]

There are respectively \(q\), \(2q(q-1)\), and \(q(q-1)^2\) diagonal assignments for \(k=0,1,2\). Putting together disjoint cases yields the unexpanded exact identity
\[
R_q(T)=qP_0(T)+2q(q-1)P_1(T)+q(q-1)^2P_2(T)+q^2(q-1)T F_q(T)^2.
\]
Expanding gives precisely the polynomial stated under Finding. Setting \(T=1\) gives \(q^9\), as required by the number of elements of \(A\). The rank-zero condition forces all four diagonal values equal and all five interval coefficients zero, proving \(Z(A)=k1\). Since the rank-five coefficient is strictly positive for \(q\ge2\) (also clear from the \(\eta\ne0\) contribution), and all other coefficients are visibly positive in the factored counting expression, every rank occurs. Counting centralizer elements \(q^{9-\operatorname{rank}\operatorname{ad}_x}\) for each \(x\) gives the commuting-probability formula. No step uses division by the field characteristic: the only divisions are by explicitly nonzero diagonal differences.

## Verification
The standalone `verify.py` directly constructs the five commutator rows from nine coordinates, uses modular Gaussian elimination, and exhaustively enumerates all \(2^9\) inputs over \(\mathbb F_2\) and all \(3^9\) inputs over \(\mathbb F_3\). It compares full rank-count dictionaries with the independent symbolic four-case formula and checks the normalization \(R_q(1)=q^9\) for \(q=2,3,4,5,7,11\). The exact run returned `VERIFY_OK`. The universal theorem is proved by the case analysis above, not inferred from these finite experiments.

## Relationship to prior work
Krylov and Tuganbaev (arXiv:2305.02984, first public 4 May 2023) give structural descriptions of derivations and automorphisms of general incidence algebras. Their Sections 14–19, including Theorem 19.2, describe derivation modules and dimensions, not the elementwise rank enumerator of the inner adjoint on the diamond. Previously obtained graphic-matroid rank formulas for height-two (radical-square-zero) poset incidence algebras do not cover this height-three diamond: its nonzero products between radical basis elements create the fifth commutator row. Earlier counts for other poset or quiver families, and general structure theorems that imply possible derivation dimensions, do not specify these six exact fiber multiplicities. The remaining publication-priority risk is an unlocated broader centralizer-enumerator or commuting-probability theorem that would specialize to this nine-dimensional algebra.

## Limitations
This is a complete exact calculation for one canonical four-point poset, not a classification for all height-three posets. It does not determine conjugacy classes of elements or the distributions of arbitrary outer derivations. The mathematical value is a reproducible non-radical-square-zero boundary case for extending the known graphic-matroid methods; a general height-three formula remains open to further work. Priority remains provisional pending independent literature review. This proof and its verification are self-reviewed only; no independent audit has been performed.

## References
1. P. Krylov and A. Tuganbaev, *Incidence Rings: Automorphisms and Derivations*, arXiv:2305.02984v1 (4 May 2023), https://arxiv.org/abs/2305.02984 ; especially §§14–19.
2. P. Krylov and A. Tuganbaev, *Derivations of Incidence Algebras*, Mathematics 12 (2024), 999, https://doi.org/10.3390/math12070999.
3. The exact matrix-unit multiplication \(e_{ij}e_{kl}=\delta_{jk}e_{il}\) and the explicit checker `verify.py` constitute the self-contained computational specification.
