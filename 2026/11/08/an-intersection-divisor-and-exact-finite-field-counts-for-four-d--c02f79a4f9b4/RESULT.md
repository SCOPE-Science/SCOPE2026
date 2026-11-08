# An intersection divisor and exact finite-field counts for four-dimensional exterior-algebra modules

## Finding

Let \(k\) be any field, and let \(\Lambda=k\langle u,v\rangle/(u^2,v^2,uv+vu)\), the four-dimensional exterior algebra (in characteristic two this is also \(k[u,v]/(u^2,v^2)\)). Define the reduced variety \(\mathcal E_4\) of four-dimensional left \(\Lambda\)-modules by pairs \((X,Y)\) of \(4\times4\) matrices such that \(X^2=Y^2=XY+YX=0\).

The reduced variety has exactly two geometrically irreducible components \(C_0\) and \(C_1\), each of dimension \(12\). The first is the locus \(XY=0\); the second is the closure of the single \(\mathrm{GL}_4\)-orbit where \(XY\ne0\). These components intersect in dimension exactly \(11\). On the dense rank-two first-matrix stratum of \(C_0\), write \(X=\begin{psmallmatrix}0&I_2\\0&0\end{psmallmatrix}\) and \(Y=\begin{psmallmatrix}0&B\\0&0\end{psmallmatrix}\); membership in \(C_0\cap C_1\) is **equivalent**, over an algebraic closure, to the repeated-eigenvalue condition
\[
(\operatorname{tr}B)^2-4\det B=0.
\]
In characteristic two, the reduced equation of this divisor is \(\operatorname{tr}B=0\). Thus the intersection is a divisor whose dense rank-two chart is controlled by the discriminant of a binary quadratic characteristic polynomial.

Over every finite field \(\mathbb F_q\), including even characteristic, the total number of ordered pairs is
\[
\boxed{\#\mathcal E_4(\mathbb F_q)=q^6(2q^6+q^5+q^4-q^2-q-1).}
\]
Exactly
\[
\boxed{\frac{|\operatorname{GL}_4(\mathbb F_q)|}{q^3(q-1)}}
\]
ordered pairs have \(XY\ne0\); all such pairs afford the regular four-dimensional \(\Lambda\)-module. The remaining pairs belong to \(C_0\). These assertions are compatible with, but not identical to, the previously established characteristic-two component census.

## Assumptions and scope

A field has no characteristic restriction. All component and dimension statements are about the reduced underlying affine variety after base change to an algebraic closure, not about nilpotent structure in the defining ideal. Finite-field counts concern ordered labeled matrix pairs, not conjugacy classes. The matrices act on a four-dimensional vector space; \(\Lambda\) has basis \(1,u,v,uv\) in every characteristic. The intersection criterion uses the rank-two locus for the first matrix and is not asserted as a global defining equation.

## Proof

**1. The nonzero-product orbit.** Suppose \(XY\ne0\). There is \(z\in k^4\) with \(XYz\ne0\). The four vectors \(z,Xz,Yz,XYz\) are independent: apply \(XY\), then \(X\), then \(Y\) to a putative relation, using \(X^2=Y^2=XY+YX=0\). They therefore form a basis, exhibiting the regular module \(\Lambda\). Conversely left multiplication by \(u,v\) on \(\Lambda\) satisfies the relations and has nonzero product. Thus the open set \(O=\{XY\ne0\}\) is one orbit. Its stabilizer is \(\Lambda^{\mathrm{op},\times}\), of algebraic dimension \(4\), so \(\dim O=16-4=12\). Write \(C_1=\overline O\); it is geometrically irreducible of dimension \(12\).

**2. The zero-product component.** If \(X^2=Y^2=XY=YX=0\), then \(\operatorname{im}X+\operatorname{im}Y\subseteq\ker X\cap\ker Y\). A two-dimensional subspace \(U\) can be chosen between these subspaces. Indeed, if either matrix has rank two, its image and kernel coincide and the mutual-annihilation relations force the other image into that plane; otherwise both images have joint dimension at most two and the two kernels intersect in dimension at least two. The incidence space
\[
\{(U,X,Y):U\in\operatorname{Gr}(2,4),\ \operatorname{im}X,\operatorname{im}Y\subseteq U\subseteq\ker X\cap\ker Y\}
\]
is a rank-eight vector bundle over \(\operatorname{Gr}(2,4)\), hence irreducible of dimension \(4+8=12\). Its image is exactly \(C_0=\{X^2=Y^2=XY=YX=0\}\). The incidence projection is closed because the Grassmannian is proper, so \(C_0\) is irreducible. It has dimension exactly \(12\): the rank-two \(X\)-orbit has dimension eight and each such \(X\) admits a four-dimensional affine family of mutually annihilating \(Y\)'s. Since \(\mathcal E_4=C_0\cup O\), the two distinct twelve-dimensional irreducible closed sets \(C_0,C_1\) are exactly the components.

**3. Intersection divisor.** Fix \(X\) of rank two and choose a basis giving \(X=\begin{psmallmatrix}0&I_2\\0&0\end{psmallmatrix}\). A general anti-commuting matrix has the unique form
\[
Y=\begin{pmatrix}A&B\\0&-A\end{pmatrix},\quad A,B\in M_2(k),
\]
with \(Y^2=0\) precisely when \(A^2=0\) and \([A,B]=0\). Here \(XY\ne0\) exactly when \(A\ne0\). If \(A\ne0\), it is a rank-one nilpotent and its centralizer in \(M_2\) is \(kI_2+kA\); therefore \(B\) has a repeated eigenvalue. The repeated-root condition is algebraically closed and remains necessary on the closure. Conversely over an algebraic closure a repeated-eigenvalue \(B\) has the form \(\lambda I_2+N\) for \(N^2=0\). Take \(A_0=N\) if \(N\ne0\), or any fixed nonzero square-zero matrix if \(N=0\). Then \(Y_t=\begin{psmallmatrix}tA_0&B\\0&-tA_0\end{psmallmatrix}\) lies in \(O\) for \(t\ne0\) and tends to the given \(Y_0\in C_0\). Local triviality of the rank-two conjugacy orbit of \(X\) identifies the fiberwise closure with the full closure on this rank-two chart. Hence the intersection there is exactly the discriminant-zero locus of \(B\). The discriminant-zero locus in \(M_2\) is irreducible of dimension three, also in characteristic two after reduction. The rank-two \(X\)-orbit has dimension eight, so this gives an eleven-dimensional subset of \(C_0\cap C_1\). The intersection is a proper closed subset of irreducible \(C_0\) of dimension twelve, so it has dimension at most eleven. Equality follows. No global irreducibility assertion for the intersection is made.

**4. Ordered pairs over finite fields.** Let \(s_1=(q^3+q^2+q+1)(q^3-1)\) be the number of rank-one square-zero matrices in \(M_4(\mathbb F_q)\), and let \(s_2=(q^2+1)(q^2+q+1)(q^2-1)(q^2-q)\) be the number of rank-two square-zero matrices. These follow by choosing image/kernel and an isomorphism from the quotient to the image. There is also the zero matrix.

For fixed \(X=0\), the number of admissible \(Y\) is \(1+s_1+s_2\). For fixed rank-two \(X\), the preceding block form gives
\[
q^4+(q^2-1)q^2=2q^4-q^2
\]
choices: \(A=0\) allows arbitrary \(B\), while each of the \(q^2-1\) nonzero square-zero \(A\)'s has a \(q^2\)-element centralizer. Exactly \(q^2(q^2-1)\) of these have \(XY\ne0\).

For fixed rank-one \(X=E_{14}\), anti-commutation and \(Y^2=0\) force
\[
Y=\begin{pmatrix}0&b&c\\0&D&e\\0&0&0\end{pmatrix}
\]
relative to block sizes \(1,2,1\), with \(D^2=bD=De=be=0\). If \(D=0\), there are \(q^4+q^3-q^2\) possibilities: \(b,e\in\mathbb F_q^2\) satisfy the scalar condition \(be=0\), and \(c\) is arbitrary. If \(D\ne0\), there are \(q^2-1\) choices of rank-one square-zero \(D\); both \(b\) and \(e\) range over one-dimensional spaces and \(be=0\) automatically, giving \(q^3\) choices per \(D\). Altogether the rank-one fiber has size \(q^5+q^4-q^2\).

Summing the three \(X\)-rank strata gives
\[
1+s_1+s_2+s_1(q^5+q^4-q^2)+s_2(2q^4-q^2)
=q^6(2q^6+q^5+q^4-q^2-q-1).
\]
The nonzero-product count \(s_2q^2(q^2-1)\) equals \(|\operatorname{GL}_4(\mathbb F_q)|/(q^3(q-1))\) because the unit group of the four-dimensional local algebra \(\Lambda\) has cardinality \((q-1)q^3\). This independently agrees with the regular-orbit argument.

## Verification

The standalone programs `check_pairs.py` and `check_representatives.py` use only Python's standard library. Run `python3 check_pairs.py` and `python3 check_representatives.py`. The first enumerates all square-zero \(4\times4\) matrices over \(\mathbb F_2\), then all admissible ordered pairs, and separately checks the symbolic orbit-stabilizer identities at \(q=2,3,4,5,7\). Its direct result is \(10{,}816\) pairs, including \(2{,}520\) with nonzero product. The second enumerates concrete canonical rank-one and rank-two fibers over \(\mathbb F_2\) and \(\mathbb F_3\) and checks matrix squares and anti-commutators, including the \(XY\ne0\) subfiber. The exact printed outputs are included in `CHECK_RESULTS.txt`. These finite checks do not prove the statements for all fields; the algebraic arguments above do.

## Relationship to prior work

Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first public 2002-11-19), classifies the \(XY=YX=0\) representation varieties, providing substantial prior coverage of \(C_0\). Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180 (first public 2006-09-06), already proves the **two twelve-dimensional component census in characteristic two**; this aspect is not advanced as historically new. Chen–Wang, *Anti-commuting varieties*, arXiv:1805.00378 (first public 2018-05-01), treats the unrestricted complex anti-commuting variety and its semi-nilpotent variant, not the simultaneous square-zero subvariety. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first public 2021-10-29), counts annihilating matrix pairs in broader families, not the nonzero-product exterior-algebra locus. The potentially additional contribution claimed here is the all-characteristic finite-field point-count polynomial together with the **explicit rank-two intersection discriminant and the dimension-eleven incidence statement**; a broader representation-variety theorem could still imply them.

## Limitations

The component claims concern the reduced variety, not the scheme structure or multiplicities of the original quadratic ideal. The displayed discriminant describes only the rank-two first-matrix chart, not a global defining equation of the intersection; no assertion that the intersection is irreducible is made. The exact finite-field formula is for dimension four only and does not enumerate module isomorphism types beyond the nonzero-product orbit. This work has not received independent external mathematical review or comprehensive historical-priority certification.

## References

- J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (2002), https://arxiv.org/abs/math/0211293.
- P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180 (2006), https://arxiv.org/abs/math/0609180.
- X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378 (2018), https://arxiv.org/abs/1805.00378.
- Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (2021), https://arxiv.org/abs/2110.15566.
