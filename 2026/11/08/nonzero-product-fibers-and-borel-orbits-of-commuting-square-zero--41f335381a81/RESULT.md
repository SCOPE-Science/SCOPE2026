# Nonzero product fibers and Borel orbits of commuting square-zero triangular pairs

## Finding
Let \(k\) be **any field**, let \(J_4(k)\) be the associative algebra of strictly upper-triangular \(4\times4\) matrices, and put
\[
\mathcal Z(k)=\{(X,Y)\in J_4(k)^2:X^2=Y^2=0,\ XY=YX\}.
\]
Write \(E_{ij}\) for a matrix unit. For every \(t\in k^\times\), the prescribed-product fiber
\[
\mathcal R_t=\{(X,Y)\in\mathcal Z(k):XY=tE_{14}\}
\]
is, as an affine \(k\)-variety, **isomorphic to** \(\operatorname{GL}_2\times\mathbb A^2\); the union \(\mathcal R_{\ne0}\) of these fibers is isomorphic to \(\operatorname{GL}_2\times\mathbb G_m\times\mathbb A^2\). All other nonzero prescribed-product fibers in \(J_4(k)\) are empty.

For finite \(k=\mathbb F_q\), every nonzero \(t\) has exactly
\[
\boxed{q^3(q-1)(q^2-1)}
\]
ordered preimages. Under simultaneous conjugation by the invertible upper-triangular group \(B_4(\mathbb F_q)\), the nonzero-product locus consists of **exactly \(q+1\) orbits**, naturally indexed by \(\mathbb P^1(\mathbb F_q)\); **each orbit has size \(q^3(q-1)^3\)**. Over an algebraic closure the orbit parameter space is the projective line, rather than a finite orbit set.

For completeness, the full prescribed-product distribution over \(\mathbb F_q\) is
\[
\#\{(X,Y)\in\mathcal Z(\mathbb F_q):XY=C\}=\begin{cases}
q^8+2q^7-2q^5-q^3(q-1)^2(q^2-1),&C=0,\\
q^3(q-1)(q^2-1),&C=tE_{14},\ t\ne0,\\
0,&\text{otherwise}.
\end{cases}
\]
The aggregate count \(q^8+2q^7-2q^5\) has appeared in earlier work for commuting square-zero pairs in characteristic two; the contribution assessed here is the **nonzero-product geometric fiber and Borel-orbit classification valid in every characteristic**, with its sharp nonzero-product support and exact multiplicities. The aggregate identity is also independently derived below, including odd characteristic.

## Assumptions and scope
Every field is allowed, without any characteristic hypothesis, for the geometric isomorphisms and orbit descriptions over rational points. For counting and orbit sizes assume \(k=\mathbb F_q\), any prime power. Matrices are labeled and ordered; orbits refer specifically to simultaneous conjugation by \(B_4(k)\), not all of \(\operatorname{GL}_4(k)\). The matrix equation \(XY=YX\) is ordinary associative commutation. Algebraic-variety isomorphisms concern the locally closed nonzero-product loci, not a claim about the full nonreduced square-zero commuting scheme.

## Proof
**1. Coordinate reduction.** Write
\[
X=\begin{pmatrix}0&a&d&f\\0&0&b&e\\0&0&0&c\\0&0&0&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&A&D&F\\0&0&B&E\\0&0&0&C\\0&0&0&0\end{pmatrix}.
\]
The equations \(X^2=Y^2=0\) are
\[
ab=bc=ae+dc=0,\qquad AB=BC=AE+DC=0.
\]
Commutation gives \(aB-Ab=bC-Bc=aE+dC-Ae-Dc=0\). If either \(b\) or \(B\) is nonzero, these equations force \(a=c=A=C=0\), hence \(XY=0\). If \(b=B=0\), all entries of \(XY\) except possibly the \((1,4)\)-entry vanish. Thus any nonzero product must be \(tE_{14}\) with \(t\ne0\).

**2. Exact nonzero fibers.** Assume \(b=B=0\). Introduce the factorization
\[
P=\begin{pmatrix}a&d\\A&D\end{pmatrix},\qquad
Q=\begin{pmatrix}e&E\\c&C\end{pmatrix},\qquad
PQ=\begin{pmatrix}ae+dc&aE+dC\\Ae+Dc&AE+DC\end{pmatrix}.
\]
The three square-zero/commuting equations are equivalent to
\[
PQ=t\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
If \(t\ne0\), then \(P\) is invertible and \(Q=tP^{-1}\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) uniquely. Conversely every such \(P,Q\), together with arbitrary \(f,F\in k\), gives a pair in \(\mathcal R_t\). This correspondence and its inverse are regular on \(\det P\ne0\). It proves \(\mathcal R_t\cong\operatorname{GL}_2\times\mathbb A^2\), and allowing \(t\ne0\) gives \(\mathcal R_{\ne0}\cong\operatorname{GL}_2\times\mathbb G_m\times\mathbb A^2\). In particular all these loci are smooth, irreducible, and of dimensions \(6\) and \(7\), respectively.

**3. Complete-flag and orbit interpretation.** Let \(X,Y\) commute, square to zero and have \(XY\ne0\) on a four-dimensional vector space \(V\). Choose \(v\) with \(XYv\ne0\). The four vectors \(v,Xv,Yv,XYv\) are linearly independent: apply \(XY\), then \(X\), then \(Y\) to a putative relation. They form a basis, so \(V\) is the regular module for \(H=k[s,t]/(s^2,t^2)\), with \(s\) acting as \(X\), \(t\) as \(Y\). This also proves that dimension four is the least dimension supporting a nonzero product of commuting square-zero operators.

A complete \(H\)-stable flag in the regular module is a chain of ideals. Its one-dimensional term is necessarily \(\operatorname{soc}(H)=k(st)\), and its three-dimensional term is necessarily \(\mathfrak m=(s,t)\). Its two-dimensional term is one of the planes between \(k(st)\) and \(\mathfrak m\), parametrized by \(\mathbb P^1(k)\). The centralizer in \(\operatorname{GL}(V)\) of the ordered pair is \(H^\times\); since \(H\) is commutative, multiplication by a unit preserves **every** ideal, so acts trivially on these flags.

A pair belongs to \(J_4(k)^2\) precisely when it preserves the standard complete flag and acts trivially on its successive quotients. Hence simultaneous conjugation by \(B_4(k)\) identifies pairs exactly when the corresponding regular-module stable flags are the same up to the centralizer action. There is one \(B_4(k)\)-orbit per point of \(\mathbb P^1(k)\). Every stabilizer is \(H^\times\), contained in \(B_4(k)\), so for \(k=\mathbb F_q\) its size is \((q-1)q^3\). Since \(|B_4(\mathbb F_q)|=(q-1)^4q^6\), every orbit has size \(q^3(q-1)^3\). This gives \((q+1)q^3(q-1)^3=q^3(q-1)^2(q^2-1)\) pairs with nonzero product, independently of the direct fiber count.

**4. Zero fiber and normalization.** For completeness, the aggregate count is obtained from the same coordinate equations. If \((b,B)\ne(0,0)\), both first and last superdiagonal coordinates vanish and the remaining \(d,e,f,D,E,F\) are arbitrary, contributing \((q^2-1)q^6\). If \(b=B=0\), fix \((a,c,A,C)\). The three linear equations on \((d,e,D,E)\) have rank zero for the all-zero quadruple, rank two for \((q^2-1)(q+1)\) quadruples, and rank three for \((q^2-1)(q^2-q)\) quadruples. The rank-two criterion when both \((a,c)\) and \((A,C)\) are nonzero is \(aC-cA=0\); when exactly one is nonzero the rank is also two. Thus this case contributes
\[
q^2\bigl[q^4+(q^2-1)(q+1)q^2+(q^2-1)(q^2-q)q\bigr]
=2q^7+q^6-2q^5.
\]
Summing gives \(q^8+2q^7-2q^5\); subtract the \((q-1)\) identical nonzero fibers to obtain the zero-fiber formula. No finite extrapolation is used.

## Verification
Run `python3 verify_borel_product.py` with Python 3 standard library only. The checker independently enumerates all square-zero elements and ordered commuting pairs using literal finite-field arithmetic over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), verifies **every product fiber**, and generates the complete upper-triangular conjugation orbits for orders \(2,3,4\). The \(\mathbb F_4\) arithmetic uses the irreducible polynomial \(z^2+z+1\). Recorded output is in `checks.txt`. Exhaustive finite instances corroborate, but do not replace, the proof for all fields. The matrix \(P,Q\) factorization and ideal-flag proof are separate noncomputational arguments.

## Relationship to prior work
Basili's 2008 paper (arXiv:0803.0722), especially its Example A for \(4\times4\) commuting strictly triangular pairs, describes the **unrestricted** commuting variety and its components; it neither imposes both square-zero equations nor determines prescribed nonzero products or their upper-triangular conjugacy orbits. Ngo (arXiv:1209.1659) treats commuting varieties in lower-rank Lie algebras and the \(3\times3\) nilradical; Ngo--Šivic (arXiv:1308.4438) treat commuting nilpotent matrix-tuple geometry up to full similarity, not these upper-triangular restricted fibers. Boos (arXiv:1504.05367) classifies orbits for **single** square-zero nilpotents under parabolics; the present object is a commuting **ordered pair**, and the product restriction is essential. Hua (arXiv:2303.15862) classifies full-similarity forms of commuting nilpotent \(4\times4\) pairs, but not the fixed-flag conjugacy splitting or finite-field product fibers. The regular-module uniqueness up to full similarity is classical and is not claimed as new.

Previously available counts for commuting square-zero pairs in characteristic two, and broader nilpotent-pair orbit/annihilation results, provide important context. A total pair count is not a prescribed-product distribution, and classification under full \(\operatorname{GL}_4\) does not classify the \(B_4\)-orbits of a fixed regular pair. The specific novelty claim is restricted to the combined **nonzero-product fiber isomorphism, exact all-field-size multiplicities, and projective-line Borel-orbit splitting**. Historical priority remains provisional.

## Limitations
This theorem concerns the first possible nonzero-product case, dimension four, for **ordered** commuting square-zero matrices inside a fixed strictly upper-triangular algebra. It does not classify the complete zero-product fiber geometrically, higher-dimensional triangular algebras, larger tuples, nonreduced scheme structures, or group-conjugacy classes outside the specified upper-triangular group. The orbit-count statement over finite fields is exact; over infinite fields the orbit parameter has infinitely many points. No independent mathematical audit or exhaustive priority certification has been performed.

## References
1. R. Basili, *Some remarks on varieties of pairs of commuting upper triangular matrices and an interpretation of commuting varieties*, arXiv:0803.0722, public preprint dated 2008-03-05, https://arxiv.org/abs/0803.0722.
2. N. V. Ngo, *Commuting varieties of \(r\)-tuples over Lie algebras*, arXiv:1209.1659, dated 2012-09-07, https://arxiv.org/abs/1209.1659.
3. N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438, dated 2013-08-20, https://arxiv.org/abs/1308.4438.
4. M. Boos, *Finite parabolic conjugation on varieties of nilpotent matrices*, arXiv:1504.05367, dated 2015-04-21, https://arxiv.org/abs/1504.05367.
5. M. Boos and M. Bulois, *Parabolic conjugation and commuting varieties*, arXiv:1606.08840, dated 2016-06-28, https://arxiv.org/abs/1606.08840.
6. J. Hua, *Canonical forms for pairs of commuting nilpotent \(4\times4\) matrices under simultaneous similarity*, arXiv:2303.15862, dated 2023-03-28, https://arxiv.org/abs/2303.15862.
