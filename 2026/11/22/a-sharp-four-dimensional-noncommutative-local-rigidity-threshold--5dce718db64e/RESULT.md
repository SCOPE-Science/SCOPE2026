# A sharp four-dimensional noncommutative local-rigidity threshold in characteristic two

## Finding

**Theorem.** Let \(K\) be any field of characteristic \(2\). Among finite-dimensional **noncommutative** Zinbiel \(K\)-algebras \(A\) with \(A^3=0\), the minimum dimension for which every linear local derivation is an ordinary derivation is **four**.

The lower bound holds without any assumption on the size or perfection of \(K\). It is attained by the indecomposable four-dimensional algebra \(A_4=Kx\oplus Ky\oplus Kz\oplus Kc\), whose only nonzero basis products are
\[
xy=xz=y^2=zx=c.
\]
Its two-sided annihilator and square both equal \(Kc\), and its complete derivation and linear-local-derivation spaces agree:
\[
\operatorname{LocDer}(A_4)=\operatorname{Der}(A_4)
=\left\{D:\begin{array}{l}
D(x)=\alpha x+\beta z+\lambda_xc,\\
D(y)=\alpha y+\lambda_yc,\\
D(z)=\alpha z+\lambda_zc,\\
D(c)=0
\end{array};\ \alpha,\beta,\lambda_x,\lambda_y,\lambda_z\in K\right\}.
\]
In particular, this space has dimension \(5\) over \(K\). The example admits nonadditive \(2\)-local derivations; this last assertion is an application of a previously established general interpolation criterion, not a separate novelty claim.

## Assumptions and scope

A Zinbiel algebra is a vector space with bilinear multiplication satisfying \((ab)c=a(bc+cb)\). Here \(A^2\) is the span of pairwise products and \(A^3=A(A^2)+(A^2)A\). A **linear local derivation** \(\Delta:A\to A\) is a linear map for which every \(a\in A\) admits an ordinary derivation \(D_a\) with \(\Delta(a)=D_a(a)\). A \(2\)-local derivation is not assumed linear and matches a derivation at each ordered pair of inputs.

All assertions hold over *every* characteristic-two field, finite or infinite, and apply to noncommutative two-step nilpotent Zinbiel algebras. The dimension bound does not assert a classification of all such algebras, nor a minimum over commutative examples or over algebras with nonvanishing third power.

## Proof

**1. The lower-dimensional obstruction.** Suppose \(\dim_K A\le3\), \(A^3=0\), and \(A\) is noncommutative. Because \(A^2\subseteq\operatorname{Ann}(A)\), multiplication factors through a bilinear map \((A/A^2)\times(A/A^2)\to A^2\). Noncommutativity requires \(\dim(A/A^2)\ge2\), while nonzero multiplication requires \(\dim A^2\ge1\). Thus \(\dim A=3\), \(\dim(A/A^2)=2\), and \(\dim A^2=1\).

Choose a complement spanned by \(u,v\), let \(A^2=Kw\), and write its multiplication as the matrix
\[
B=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
uw=wu=vw=wv=w^2=0.
\]
Noncommutativity is equivalent to \(e=b+c\ne0\) in characteristic two. Define
\[
P=\begin{pmatrix}0&d/e\\a/e&1\end{pmatrix}.
\]
Direct multiplication yields \(P^{\mathsf T}B+BP=B\). Hence the linear map \(D\) on \(A\) with \(D|_{Ku+Kv}=P\) and \(D(w)=w\) is an ordinary derivation: the displayed equation is exactly the derivation condition on products of complement elements, and all products with \(w\) vanish.

Let \(\pi:A\to Kw\) be the projection with kernel \(Ku+Kv\). It is a proper linear local derivation. Indeed, at any nonzero \(w\)-component alone, \(D\) witnesses \(\pi\); at any element \(v_0+tw\) with \(0\ne v_0\in Ku+Kv\), the map \(S(a)=\ell(a\bmod A^2)w\) for a functional satisfying \(\ell(v_0)=t\) is a derivation and witnesses \(\pi(v_0+tw)=tw\). Such central maps are derivations because they kill \(A^2\) and have annihilator-valued image. Finally, \(\pi(uv)=uv\ne0\) for some product, whereas \(\pi(u')=\pi(v')=0\) for every pair in the chosen complement, so \(\pi\) cannot satisfy the derivation identity. The claimed dimension lower bound follows.

**2. The four-dimensional example.** Every triple product in \(A_4\) is zero, so the Zinbiel identity holds. The multiplication matrix on \(V=Kx\oplus Ky\oplus Kz\) with values in \(Kc\) is
\[
B=\begin{pmatrix}0&1&1\\0&1&0\\1&0&0\end{pmatrix},\qquad \det B=1.
\]
The invertibility of \(B\) implies \(\operatorname{Ann}(A_4)=Kc=A_4^2\). This also proves indecomposability: if \(A_4=I\oplus J\) as a sum of ideals, then \(A_4^2=I^2\oplus J^2\) is one-dimensional, so one square vanishes; assume \(J^2=0\). Cross-products vanish between the two ideals, whence \(J\subseteq\operatorname{Ann}(A_4)=A_4^2\subseteq I\), forcing \(J=0\).

Any derivation preserves \(A_4^2=Kc\), so relative to \(V\oplus Kc\) it has block form
\[
D=\begin{pmatrix}P&0\\\lambda&s\end{pmatrix},
\]
where \(P\in M_3(K)\), \(\lambda\in\operatorname{Hom}(V,Kc)\), and \(s\in K\). The Leibniz rule is exactly
\[
P^{\mathsf T}B+BP=sB.
\]
Writing \(P=(p_{ij})\), comparison of the nine entries, in characteristic two, forces
\[
p_{12}=p_{21}=p_{23}=p_{32}=s=0,
\qquad p_{11}=p_{22}=p_{33}=\alpha,
\]
while \(p_{31}=\beta\) is arbitrary. Explicitly, the \((1,1)\) and \((2,1)\) equations force \(p_{21}=p_{32}=0\); the \((2,2)\), \((2,3)\), and \((3,2)\) equations give \(p_{12}=p_{23}=s\), \(p_{13}=0\); the \((1,3)\) and \((3,1)\) equations then force \(s=0\), and the remaining entries give equality of the diagonal entries. Conversely, each such \(P\), together with any \(\lambda\), satisfies the matrix equation. Thus all ordinary derivations have precisely the five parameters displayed in the finding.

**3. Pointwise rigidity.** Let \(\Delta\) be a linear local derivation. Every ordinary derivation kills \(c\), so \(\Delta(c)=0\). Modulo \(Kc\), the image of a vector \(v\in V\) under an ordinary derivation lies in
\[
\{\alpha v+\beta\,x^*(v)z:\alpha,\beta\in K\},
\]
where \(x^*\) is the linear functional selecting the \(x\)-coordinate. Applying pointwise locality to \(y\), \(z\), and \(y+z\) shows that the projected linear map has the same scalar \(\alpha\) on both \(y\) and \(z\). Applying it to \(x\) and \(x+y\) forces that same \(\alpha\) on \(x\), while permitting only an additional \(\beta z\) term in the image of \(x\). Consequently the induced map on \(V\) has precisely the form \(\alpha I+\beta E_{zx}\). The remaining \(Kc\)-valued components of \(\Delta(x),\Delta(y),\Delta(z)\) form an arbitrary linear functional, and all such functionals already appear among the ordinary derivations. Therefore \(\Delta\) is an ordinary derivation, proving \(\operatorname{LocDer}(A_4)=\operatorname{Der}(A_4)\).

**4. Known two-local phenomenon in the example.** Let \(\overline A=A_4/A_4^2\). Define a homogeneous but nonadditive map \(h:\overline A\to K\) by \(h(t(\bar x+\bar y))=t\) for \(t\in K\), and \(h(v)=0\) on every other projective line. Then \(\Phi(a)=h(\bar a)c\) is not additive, since \(\Phi(x)=\Phi(y)=0\) but \(\Phi(x+y)=c\). At any two quotient vectors, homogeneity ensures that their prescribed images extend to a linear functional; such a functional defines a central derivation into \(Kc\). Hence \(\Phi\) is \(2\)-local. This is a direct specialization of the existing arbitrary-field two-local interpolation theorem cited below and is **not** claimed as an independent new result.

## Verification

The independent-of-proof finite-field program `verify.py` constructs linear derivation equations from the multiplication tables and tests the pointwise-locality conditions on every vector over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). The computed dimensions for \(A_4\) are \(5\) for both ordinary and linear local derivations in every tested field. It additionally tests the displayed scaling derivation of the noncommutative three-dimensional case for **all** bilinear-form matrices over each field (respectively \(8\), \(192\), and \(3584\) noncommutative matrices). The program uses no external libraries. The exact field-independent proof above, rather than finite enumeration, establishes the universal theorem. Expected output is recorded in `verification_output.txt`.

## Relationship to prior work

Abdireymov, Sattarov, and Yusupov (arXiv:2611.07863v1; first posted November 5, 2026) prove a **characteristic-zero** minimal local-rigidity dimension of five and provide general machinery for two-step algebras. Their Theorem 1.1 and Theorem 4.2 do not cover characteristic two, and their general block description does not state this sharp noncommutative characteristic-two cutoff or the explicit four-dimensional derivation space. Their arbitrary-field theorem on nonlinear two-local derivations covers the final application, which is therefore not a novelty assertion.

Prior work already identified characteristic-two local rigidity of the two-dimensional one-generator square algebra. That **commutative** case is not included in the present novelty claim. Earlier finite-dimensional constructions of locally rigid Zinbiel algebras in dimensions five and six likewise do not determine the sharp **noncommutative** two-step threshold or the four-dimensional example here.

## Limitations

The minimality assertion is restricted to noncommutative Zinbiel algebras with zero third power in characteristic two. It does not classify all four-dimensional locally rigid algebras. The computational checks cover finite fields of orders two, four, and eight, whereas the proof covers arbitrary characteristic-two fields, including infinite and imperfect fields. Historical priority remains provisional pending wider examination of older characteristic-two nonassociative-algebra literature and unindexed classification tables. The work has not undergone independent mathematical audit.

## References

1. A. Abdireymov, A. Sattarov, B. Yusupov, *Local and 2-Local Derivations of Finite-Dimensional Zinbiel Algebras*, arXiv:2611.07863v1, November 5, 2026. https://arxiv.org/abs/2611.07863 (especially Theorems 1.1, 1.2, 3.5, 3.6 and 4.2).
2. K. Kaygorodov, K. Kudaybergenov, I. Yuldashev, *Local derivations of semisimple Leibniz algebras*, Communications in Mathematics **30** (2022), 1–12. https://doi.org/10.46298/cm.9274 (contrasting algebraic category).
