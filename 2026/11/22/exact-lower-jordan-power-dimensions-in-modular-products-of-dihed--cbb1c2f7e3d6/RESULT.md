# Exact lower Jordan-power dimensions in modular products of dihedral and quaternion groups

## Finding

Let \(k\) be any field of characteristic two, let \(r\geq1\), let \(H_i\in\{D_8,Q_8\}\) for \(1\leq i\leq r\), and let \(A\) be any finite abelian group. Put \(G=A\times\prod_{i=1}^rH_i\), \(R=kG\), and equip the associative group algebra with the Jordan product \(x\circ y=xy+yx\). Define *vector subspaces*, without closing under associative multiplication, by \(L_1=R\) and \(L_{n+1}=\operatorname{span}_k\{x\circ y:x\in L_n,y\in R\}\).

Then, for every integer \(n\geq2\),
\[
\boxed{\dim_k L_n=|A|\sum_{j=n-1}^{r}\binom rj\left(4^r-4^{r-j}\right),}
\]
with an empty sum equal to zero. In particular, \(\dim_k L_1=|A|8^r\), \(\dim_k L_2=|A|(8^r-5^r)\), \(\dim_k L_{r+1}=|A|(4^r-1)\), \(L_{r+1}\ne0\), and \(L_{r+2}=0\). Thus the Jordan nilpotency index is exactly \(r+2\), while *every intermediate Jordan-power dimension* is independent of the choices between \(D_8\) and \(Q_8\).

The theorem concerns the **raw left-normed Jordan-product subspaces**, which in characteristic two equal the ordinary Lie lower central subspaces. They are not the associative ideals conventionally called lower Lie powers.

## Assumptions and scope

Here \(D_8\) is the nonabelian dihedral group of order eight, \(Q_8\) is the quaternion group of order eight, \(A\) may have even order, and the field \(k\) may be finite or infinite. All dimensions are vector-space dimensions over \(k\). The convention \(L_{n+1}=L_n\circ R\) uses left-normed products; no inversion of two is assumed.

## Proof

First take \(A=1\). For each factor \(H_i\), let \(z_i\) be its unique nontrivial central commutator. The center of \(H=\prod_iH_i\) is \(Z=\langle z_1,\ldots,z_r\rangle\cong C_2^r\). Write \(V=H/Z=\bigoplus_iV_i\), where \(V_i\cong\mathbb F_2^2\), and let \(B_i\) be the nondegenerate alternating commutator form on \(V_i\). Thus, for lifts of \(u,v\in V\), their group commutator is \(\prod_i z_i^{B_i(u_i,v_i)}\).

The central coefficient algebra has squarefree coordinates
\[
K=kZ\cong k[t_1,\ldots,t_r]/(t_1^2,\ldots,t_r^2),\qquad t_i=1+z_i.
\]
Choose one group lift \(h_v\) of every \(v\in V\), so \(kH=\bigoplus_{v\in V}Kh_v\). A bracket of elements in homogeneous cosets \(Kh_u\) and \(Kh_w\) lands in \(Kh_{u+w}\). Consequently each \(L_n\) splits over these cosets. It is also stable under multiplication by \(K\): any central coefficient can be transferred to the first input of a left-normed product.

For \(v\in V\), set \(S(v)=\{i:v_i\ne0\}\), let \(I=(t_1,\ldots,t_r)\subseteq K\), and let \(I_S=(t_i:i\in S)\), with \(I_{\varnothing}=0\). We establish, for each \(n\geq2\), the **stronger, componentwise identity**
\[
\boxed{L_n\cap Kh_v=I_{S(v)}I^{n-2}h_v.}\tag{1}
\]

For \(n=2\), the bracket \(h_u\circ h_{v-u}\) equals a central unit times
\[
\left(1+\prod_i z_i^{B_i(u_i,v_i)}\right)h_v.
\]
As \(u\) varies, the commutator vectors \((B_i(u_i,v_i))_i\) range over exactly the coordinate subspace supported on \(S(v)\). In particular, each \(t_i\) with \(i\in S(v)\) occurs; every remaining bracket coefficient lies in their ideal. Hence (1) holds for \(n=2\).

Assume (1) holds at \(n\geq2\). For any product reaching coset \(v\) from coset \(u\), the new bracket coefficient belongs to \(I_{S(v)}\cap I\), since its commutator vector is \(B(u,v)\), supported on \(S(v)\). The induction hypothesis therefore gives the inclusion \(L_{n+1}\cap Kh_v\subseteq I_{S(v)}I^{n-1}h_v\).

For the reverse inclusion it suffices to obtain any squarefree monomial \(t_T=\prod_{j\in T}t_j\) with \(|T|\geq n\) and \(T\cap S(v)\ne\varnothing\). Choose \(i\in T\cap S(v)\), and choose \(j\in T\setminus\{i\}\), which is possible because \(|T|\geq n\geq2\). Pick \(u\in V\) with \(B_i(u_i,v_i)=1\), \(B_\ell(u_\ell,v_\ell)=0\) for \(\ell\ne i\), and \(u_j\ne0\). This is possible coordinatewise: nondegeneracy supplies \(u_i\); at \(j\), take \(u_j=v_j\) if \(v_j\ne0\), otherwise any nonzero vector. The induction hypothesis supplies \(t_{T\setminus\{i\}}h_u\in L_n\). Bracketing it with \(h_{v-u}\) multiplies its central coefficient by \(t_i\), up to a central group unit. As the summand is stable under \(K\), it contains \(t_Th_v\). Thus the reverse inclusion holds and (1) follows by induction for all \(n\).

The squarefree monomials \(t_T\), \(T\subseteq\{1,\ldots,r\}\), form a basis of \(K\). Formula (1) says that the monomial \(t_T h_v\) occurs at stage \(n\geq2\) precisely when \(|T|\geq n-1\) and \(T\cap S(v)\ne\varnothing\). Fixing \(|T|=j\), there are \(\binom rj\) choices for \(T\). Of the \(4^r\) quotient vectors \(v\), exactly \(4^{r-j}\) vanish on every coordinate of \(T\). Summing gives the stated formula with \(A=1\). For \(n=r+1\) the only monomial is \(t_1\cdots t_r\), occurring in precisely \(4^r-1\) nonzero quotient cosets, and the next level vanishes.

Finally, \(k[H\times A]\cong kH\otimes_k kA\). Since \(A\) is abelian, a left-normed bracket of pure tensors equals the corresponding bracket in \(kH\) tensored with the product of their \(kA\) components. Taking spans shows \(L_n(k[H\times A])=L_n(kH)\otimes_k kA\) for all \(n\). Since \(\dim_k kA=|A|\), this proves the entire theorem.

## Verification

The self-contained `CHECK.py` uses exact binary arithmetic. It independently builds multiplication tables of \(D_8\), \(Q_8\), and their mixed direct products, computes actual left-normed Jordan subspaces by Gaussian elimination, and checks the theorem for ranks one and two. A separate central-polynomial recurrence checks each homogeneous component, not just total dimensions, through rank three. Expected dimension vectors (including \(L_1\) and the first zero term) are \((8,3,0)\), \((64,39,15,0)\), and \((512,387,243,63,0)\). This finite checking is supporting evidence only; the induction above proves the infinite family.

Run the checker with `python CHECK.py` using Python 3 and no third-party packages.

## Relationship to prior work

Cristo, Cornelissen Hoyos, and Rodrigues (arXiv:2611.06587v1, November 4, 2026) characterize Jordan nilpotency of group rings and give classifications by nilpotency **index**. Their characteristic-two results reduce Jordan products to Lie commutators. The dimension formula here refines an index determination by resolving every intermediate raw product subspace for a natural infinite direct-product family, including the independence of dihedral versus quaternion factors.

Bhandari and Passi's study of Lie nilpotency indices and the standard computational definitions of *lower Lie powers* concern **associative ideals generated by commutators**. Those objects do not supply (1): for \(r=1\), the raw second product space has dimension three, while the associative ideal it generates has dimension four. Gildea's 2026 work on equality of lower and upper Lie nilpotency indices is relevant to indices but the accessible summary does not establish the componentwise intermediate dimensions proved here.

## Limitations

The componentwise formula requires the commutator pairing to split into independent rank-two planes valued in independent central involutions. It does not claim the same graded dimensions for arbitrary class-two groups, odd characteristics, or Jordan powers taken as two-sided associative ideals. The similarity of the \(D_8\) and \(Q_8\) filtrations is a vector-space statement, not an assertion that their group algebras are isomorphic. Historical priority may be affected by unindexed or inaccessible specialized literature.

## References

1. O. B. Cristo, M. G. Cornelissen Hoyos, R. L. Rodrigues, *On Jordan nilpotency of index n in group rings*, arXiv:2611.06587v1 (first posted 2026-11-04), https://arxiv.org/html/2611.06587v1.
2. J. Gildea, *Lower and Upper Lie Nilpotency Indices of Modular Group Algebras*, arXiv:2610.10915v1 (first posted 2026-10-07), https://arxiv.org/abs/2610.10915.
3. A. K. Bhandari and I. B. S. Passi, *Lie-Nilpotency Indices of Group Algebras*, Bull. London Math. Soc. 24 (1992), 68–70, https://doi.org/10.1112/blms/24.1.68.
4. GAP LAGUNA manual, sections on `LieUpperNilpotencyIndex` and `LieLowerNilpotencyIndex`, https://fossies.org/linux/gap/pkg/laguna/doc/chap4_mj.html.
