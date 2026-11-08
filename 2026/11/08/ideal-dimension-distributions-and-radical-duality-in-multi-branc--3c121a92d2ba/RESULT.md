# Ideal-dimension distributions and radical duality in multi-branch Artinian fibre products

## Finding
For every field \(k\), integer \(r\ge2\), and integers \(n_1,\ldots,n_r\ge2\), let
\[
 A=k[x_1,\ldots,x_r]/(x_ix_j\ (i\ne j),\ x_i^{n_i}\ (1\le i\le r)),
 \qquad \mathfrak m=(x_1,\ldots,x_r),\quad N=\sum_{i=1}^r(n_i-1).
\]
Every proper ideal has a unique normal form described below by an integer vector \(b\) and a subspace with no coordinate axis. Over every finite field \(k=\mathbb F_q\), its full ideal-dimension polynomial \(Z_A(T)=\sum_{I\triangleleft A}T^{\dim_k I}\) is
\[
 Z_A(T)=T^{N+1}+
 \sum_{S\subseteq\{1,\ldots,r\}}H_{|S|}(T,q)
 \prod_{i\notin S}T^{n_i-1}
 \prod_{i\in S}(1+T+\cdots+T^{n_i-2}),
\]
where
\[
 H_s(T,q)=\sum_{d=0}^s h_{s,d}(q)T^d,\qquad
 h_{s,d}(q)=\sum_{j=0}^{\min(s,d)}(-1)^j\binom{s}{j}{s-j\brack d-j}_q.
\]
Here \({a\brack b}_q\) is the Gaussian binomial coefficient, zero unless \(0\le b\le a\). The part \(P_A(T)=Z_A(T)-T^{N+1}\) enumerating proper ideals is **self-reciprocal**:
\[
 T^N P_A(T^{-1})=P_A(T).
\]
Thus proper ideals of dimension \(d\) and \(N-d\) have exactly the same count, even though these local rings have socle dimension \(r\ge2\) and are not Gorenstein.

## Assumptions and scope
The field is arbitrary for the normal form and dimension-reversing duality, and finite only for the point-count formula. The rings are commutative and unital. An ideal means a \(k\)-linear ideal, including zero and the whole ring. All proper ideals lie in \(\mathfrak m\). Define \(U_i=x_i k[x_i]/(x_i^{n_i})\), so \(\mathfrak m=\bigoplus_i U_i\) as vector spaces, with cross-branch products zero.

Fix \(b=(b_1,\ldots,b_r)\) with \(1\le b_i\le n_i\), and put
\[
 K_b=\bigoplus_{i=1}^r x_i^{b_i}k[x_i]/(x_i^{n_i})\subseteq\mathfrak m,
 \quad S(b)=\{i:b_i\ge2\}.
\]
Write \(K_b^+=K_b+\operatorname{span}_k\{x_i^{b_i-1}:i\in S(b)\}\), and identify \(K_b^+/K_b\cong k^{S(b)}\) by these monomial classes. The normal form asserts that every proper ideal is uniquely \(I=\pi_b^{-1}(L)\), with inverse image inside \(K_b^+\), for a unique \(b\) and a unique subspace \(L\le k^{S(b)}\) satisfying \(L\cap ke_i=0\) for each \(i\in S(b)\). No condition excludes the zero subspace. Its dimension is
\[
 \dim_k I=\sum_i(n_i-b_i)+\dim_k L.
\]
For any fixed \(b\) and \(d\), the corresponding reduced parameter stratum is the open subset \(\{L\in\mathrm{Gr}(d,|S(b)|):e_i\notin L\text{ for all }i\}\) of a Grassmannian; this is a set-theoretic/reduced stratification, not a claim about nonreduced ideal-scheme structure.

## Proof
**Normal form.** Let \(I\subseteq\mathfrak m\) be an ideal. Each \(I\cap U_i\) is an ideal of the uniserial \(k[x_i]\)-module \(U_i\), so there is a unique exponent \(b_i\in\{1,\ldots,n_i\}\) such that \(I\cap U_i=x_i^{b_i}k[x_i]/(x_i^{n_i})\). In particular \(K_b\subseteq I\). Let \(v=\sum_i v_i\in I\), with \(v_i\in U_i\). Multiplication by \(x_i\) yields \(x_iv=x_iv_i\in I\cap U_i\), hence \(v_i\) lies in the preimage of \(\ker(x_i:U_i/(I\cap U_i)\to U_i/(I\cap U_i))\). For \(b_i\ge2\) this is precisely \(x_i^{b_i-1}k\) modulo \(I\cap U_i\), and for \(b_i=1\) it is zero. Therefore \(I\subseteq K_b^+\). The image \(L=I/K_b\subseteq k^{S(b)}\) cannot contain a coordinate axis, since then a pure \(x_i^{b_i-1}\) would belong to \(I\cap U_i\), contradicting minimality of \(b_i\). Conversely, any such \(L\) defines a \(k\)-subspace \(I\) containing \(K_b\); every \(x_i\) maps \(K_b^+\) into \(K_b\), so it is an ideal; the no-axis condition recovers exactly its indicated intersections. This proves necessity, sufficiency and uniqueness, including all boundary cases.

**Exact enumeration.** For \(s=|S|\), the set of all \(d\)-subspaces of \(k^s\) has size \({s\brack d}_q\). For any specified \(j\) coordinate axes, the number of \(d\)-subspaces containing them is \({s-j\brack d-j}_q\). Inclusion-exclusion over the \(s\) axes gives \(h_{s,d}(q)\). Grouping \(b_i=1\) for \(i\notin S\), contributing dimension \(n_i-1\), and \(b_i\in\{2,\ldots,n_i\}\) for \(i\in S\), contributing dimensions \(0,\ldots,n_i-2\), proves the displayed polynomial. The sole nonproper ideal is \(A\), of dimension \(N+1\).

**Duality and palindromicity.** Equip \(\mathfrak m\) with the nondegenerate symmetric bilinear form determined on its basis by
\[
 \langle x_i^a,x_j^b\rangle=\begin{cases}1&i=j\ \text{and }a+b=n_i,\\0&\text{otherwise},\end{cases}
 \qquad 1\le a<n_i,\ 1\le b<n_j.
\]
The pairing satisfies \(\langle xv,w\rangle=\langle v,xw\rangle\) for every \(x\in A\), by testing generators \(x_i\). Hence the orthogonal complement \(I^\perp\) of any ideal \(I\subseteq\mathfrak m\) is again an \(A\)-submodule of \(\mathfrak m\), thus a proper ideal. Orthogonal complementation is an involution and \(\dim I+\dim I^\perp=N\). This gives the self-reciprocity for any finite field and any branch lengths, without assuming \(A\) itself is Frobenius.

## Verification
The standalone `branch_ideals_checker.py` independently enumerates all reduced-row-echelon subspaces of \(\mathfrak m\) over prime fields, tests invariance under multiplication by each \(x_i\), and compares the resulting dimension histogram with the exact inclusion-exclusion formula. It exhaustively tested eight independent settings, including \((n_1,n_2,n_3)=(3,3,3)\) over \(\mathbb F_3\), where it inspected \(56{,}632\) radical subspaces and found \(164\) ideals including the unit ideal. The corresponding polynomial simplifies to
\[
 Z_A(T)=T^7+1+(q^2+q+1)(T+T^5)+(4q^2+q+1)(T^2+T^4)+(6q^2+1)T^3+T^6
\]
when all three lengths equal \(3\); hence the total is \(16q^2+4q+8\), giving \(80\) at \(q=2\) and \(164\) at \(q=3\). The checker also confirmed dimensions and totals for mixed lengths and four-branch square-zero radicals. See the embedded `branch_ideals_verification.log`. These finite checks corroborate but do not replace the proof for arbitrary fields and dimensions.

## Relationship to prior work
A 2023 mathematical discussion by Aitor Iribar Lopez establishes a two-branch ideal normal form for the untruncated nodal curve over the complex field; the corresponding two-branch classification is therefore prior knowledge, not independently claimed here. The present statement encompasses arbitrary numbers of branches, arbitrary coefficient fields, the full finite-field dimension-count polynomial and radical ideal duality. Moore's 2007 study of local fibre products develops resolutions and Ext-algebra structure for rings sharing their residue field, but does not give this ideal-dimension count. Conca and Römer (2007) analyze generic initial ideals of fibre products, a different ideal-theoretic problem. Kassel and Reutenauer (2015) count ideals of fixed codimension in Laurent polynomial algebras, using different ambient rings and Hilbert-scheme geometry. The classification here concerns *every ideal* of finite truncated multi-branch fibre products and a dimension-reversing duality internal to the maximal ideal. The standard Grassmannian count is used as a counting ingredient rather than asserted as independently new. A broader theorem on submodule lattices of finite direct sums of uniserial modules may imply or subsume the present result; no claim of exhaustive historical priority is made.

## Limitations
This is a classification for monomial fibre products of truncated one-variable local algebras, not general Artinian local rings or arbitrary fibre products. It counts embedded ideals and their dimensions, not ideal-isomorphism classes or all incidence numbers of the inclusion poset. The geometric statement concerns reduced parameter strata only, not possible nonreduced structure of the full ideal scheme. The result is not an independent historical-priority certification.

## References
1. W. Frank Moore, *Cohomology of Fiber Products of Local Rings*, first submitted 2007-04-26, arXiv:0704.3631v1, https://arxiv.org/html/0704.3631v1.
2. A. Conca and T. Römer, *Generic initial ideals and fibre products*, first submitted 2007-07-04, arXiv:0707.0678v1, https://arxiv.org/html/0707.0678v1.
3. C. Kassel and C. Reutenauer, *Counting the ideals of given codimension of the algebra of Laurent polynomials in two variables*, first submitted 2015-05-27, arXiv:1505.07229, https://arxiv.org/abs/1505.07229.
4. D. D. Anderson and J. Kintzinger, *Ideals in Direct Products of Commutative Rings*, Bulletin of the Australian Mathematical Society 77 (2008), 477–483, DOI:10.1017/S0004972708000415 (distinct direct-product setting).
5. Aitor Iribar Lopez, answer to *Determining all ideals of C[x,y]/(xy)*, Mathematics Stack Exchange, 2023-12-13, https://math.stackexchange.com/questions/4811969 (explicit two-branch nodal ideal classification).
