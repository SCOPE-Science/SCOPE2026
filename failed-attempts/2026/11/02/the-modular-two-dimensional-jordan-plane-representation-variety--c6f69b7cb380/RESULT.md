# The modular two-dimensional Jordan-plane representation variety

## Finding

Let \(k\) be any field and let \(R_k=k\langle x,y\rangle/(xy-yx-y^2)\). Its reduced variety of two-dimensional representations is
\[
\mathcal V_k=\{(X,Y)\in M_2(k)^2:XY-YX=Y^2\}_{\mathrm{red}},
\]
where the equation is interpreted geometrically after arbitrary field extension. There are exactly two geometrically irreducible components, both defined over \(k\), in every characteristic. One is always \(C_0=\{Y=0\}\cong\mathbb A^4_k\). The other has dimension four if \(\operatorname{char}k\ne2\), but dimension five if \(\operatorname{char}k=2\). Thus \(\mathcal V_k\) is equidimensional exactly when \(\operatorname{char}k\ne2\).

If \(\operatorname{char}k\ne2\), the second component is the closure \(C_1\) of the locus \(Y\ne0\), \(Y^2=0\), \([X,Y]=0\). Its intersection with \(C_0\) consists exactly of pairs \((X,0)\) for which \(X\) has repeated characteristic root, equivalently \((\operatorname{tr}X)^2=4\det X\). This intersection is irreducible of dimension three.

If \(\operatorname{char}k=2\), write
\[
X=\begin{pmatrix}s&t\\r&u\end{pmatrix},\quad
Y=\begin{pmatrix}a&b\\c&a\end{pmatrix}.
\]
The second component is the explicitly defined irreducible hypersurface
\[
C_1=\{s=u,\quad a^2+bc+br+ct=0\}\subset\mathbb A^6_k
\]
(with coordinates \(s,t,r,a,b,c\)). It intersects \(C_0\) in \(\{Y=0,\operatorname{tr}X=0\}\cong\mathbb A^3_k\). Its intrinsic singular locus is the affine line \(\{X=sI_2,Y=0\}\). Its dense open subset contains matrices \(Y\) of nonzero determinant, so the positive-characteristic component is not a nilpotent-matrix stratum.

For every finite field \(\mathbb F_q\), the exact number of ordered pairs is
\[
\#\mathcal V_{\mathbb F_q}(\mathbb F_q)=
\begin{cases}
2q^4-q^2,&q\text{ odd},\\
q^5+q^4-q^3,&q\text{ even}.
\end{cases}
\]
With \(\mathbb L=[\mathbb A^1_k]\), the corresponding reduced-variety classes in the Grothendieck ring are \(2\mathbb L^4-\mathbb L^2\) in characteristic different from two and \(\mathbb L^5+\mathbb L^4-\mathbb L^3\) in characteristic two.

## Assumptions and scope

No algebraic closure, finiteness or perfection assumption on \(k\) is needed for the geometric claims. Geometric irreducibility means irreducibility after extending \(k\) to an algebraic closure. The variety is reduced by definition; the scheme cut out before taking radicals is not claimed to be reduced. Matrix representations are labeled: there is no quotient by simultaneous similarity. The finite-field count is for labeled pairs, not isomorphism classes. The one-dimensional representation variety is always \(\mathbb A^1_k\), because the scalar image of \(y\) must square to zero; hence dimension two is the smallest representation dimension where the modular change can appear.

## Proof

**1. Characteristic different from two.** It suffices to prove nilpotence of \(Y\) over an algebraic closure. Suppose it has a nonzero eigenvalue \(\lambda\). Let \(W\) be its generalized eigenspace and let \(P\) be the spectral projector, which commutes with \(Y\). Compressing the defining identity gives \([PXP,Y|_W]=(Y|_W)^2\). The trace of the left side is zero. Since \(\dim W\in\{1,2\}\) and \(Y|_W=\lambda I+N\) with \(N\) nilpotent of size at most two, \(\operatorname{tr}((Y|_W)^2)=(\dim W)\lambda^2\ne0\) in characteristic different from two, a contradiction. Therefore \(Y\) is nilpotent, and \(Y^2=0\) for a two-by-two matrix. The defining relation becomes \([X,Y]=0\).

For \(Y\ne0\), its Jordan type is a single length-two block, so its centralizer in \(M_2\) is the two-dimensional space \(kI+kY\). The nonzero nilpotent cone of two-by-two matrices is geometrically irreducible of dimension two: a nonzero \(Y\) is specified by its kernel/image line \(\ell\in\mathbb P^1\) and a nonzero element of \(\operatorname{Hom}(k^2/\ell,\ell)\). The locus \(Y\ne0\) of solutions is consequently a rank-two vector bundle over this cone and is irreducible of dimension four. Denote its closure by \(C_1\).

Every point of the open stratum satisfies \((\operatorname{tr}X)^2=4\det X\), since \(X=\alpha I+\beta Y\). Hence \(C_1\cap C_0\) lies in this discriminant-zero hypersurface. Conversely, every matrix on that hypersurface can be written \(X=\alpha I+N\) with \(N^2=0\). If \(N\ne0\), the family \((X,tN)\) for \(t\ne0\) lies in the open stratum and approaches \((X,0)\). If \(N=0\), use any fixed nonzero square-zero matrix in place of \(N\). Thus the intersection is exactly the discriminant-zero hypersurface, irreducible of dimension three. Finally, \(C_0\not\subset C_1\), as \(\operatorname{diag}(0,1)\) has distinct eigenvalues, while \(C_1\not\subset C_0\) because it has points with \(Y\ne0\). Since every solution belongs to \(C_0\cup C_1\), these are precisely the two components, both of dimension four.

**2. Characteristic two.** Taking traces in \([X,Y]=Y^2\) yields \(0=\operatorname{tr}(Y^2)=(\operatorname{tr}Y)^2\), so \(\operatorname{tr}Y=0\). Use the coordinates in the statement. Direct matrix multiplication gives exactly
\[
b(s+u)=0,\qquad c(s+u)=0,\qquad br+ct=a^2+bc.
\]
If \(b=c=0\), the last equation implies \(a=0\), hence \(Y=0\). Otherwise \(s=u\), so the point lies in \(C_1\). The converse follows by direct substitution. This proves equality of the underlying geometric point sets \(\mathcal V_k=C_0\cup C_1\).

The polynomial \(f=a^2+bc+br+ct\) is absolutely irreducible: as a polynomial of degree one in \(r\) over the UFD \(\bar k[a,b,c,t]\), its leading coefficient \(b\) is coprime to its constant coefficient \(a^2+bc+ct\). The primitive linear polynomial is irreducible by Gauss's lemma. The additional coordinate \(s\) is free. Hence \(C_1\) is geometrically irreducible of dimension five. Both components are proper and neither contains the other: \(C_0\) has points of nonzero \(\operatorname{tr}X\), while \(C_1\) has points with \(Y\ne0\). Their intersection is exactly the three-dimensional affine space stated. For the singular locus of \(C_1\), the partial derivatives of \(f\) with respect to \(a,b,c,r,t\) are \(0,c+r,b+t,b,c\); together with \(f=0\) they force \(a=b=c=r=t=0\), leaving \(s\) free. This proves the singular-line assertion. Since the open set \(b\ne0\) allows \(a^2+bc\ne0\), invertible \(Y\) occur on the dense component.

**3. Arithmetic and motivic counts.** In odd characteristic, the zero matrix \(Y\) permits \(q^4\) choices of \(X\). There are \(q^2-1\) nonzero nilpotent \(Y\), each with a two-dimensional commuting space of \(X\), giving \(2q^4-q^2\) solutions. For the motivic statement, the nonzero nilpotent cone is a punctured line bundle over \(\mathbb P^1\), of class \((\mathbb L+1)(\mathbb L-1)=\mathbb L^2-1\), and its commuting \(X\)-fibers are locally trivial affine two-spaces.

In characteristic two, \(Y=0\) contributes \(q^4\) choices of \(X\). There are \(q^3-q\) nonscalar trace-zero \(Y\) (all trace-zero matrices minus the \(q\) scalar matrices), and each admits exactly \(q^2\) solutions of the two independent linear conditions \(s=u\) and \(br+ct=a^2+bc\). The result is \(q^5+q^4-q^3\). Over the nonscalar trace-zero base \(\mathbb A^3\setminus\mathbb A^1\), the solutions of \(X\) form a Zariski-locally trivial affine-two-space bundle, by solving for \(r\) on \(b\ne0\) and for \(t\) on \(c\ne0\). This yields the indicated motivic class. All computations hold over finite extensions as well, after replacing \(q\) by the extension-field cardinality.

## Verification

The standalone program `verify_jordan_plane.py` uses the original four matrix equations, not the component parametrizations, to construct the linear map \(X\mapsto XY-YX\) for every \(Y\) over seven fields. Independent Gaussian elimination determines its rank and tests whether \(Y^2\) is in its image. The resulting counts agree with both formulas over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_4,\mathbb F_8,\mathbb F_9\). Complete brute-force enumeration of all \((X,Y)\) was also performed over \(\mathbb F_2\) and \(\mathbb F_3\). The exact output is in `verification_output.txt`. These are finite checks, not proof of a general field claim.

## Relationship to prior work

Iyudu's study of the Jordan plane (arXiv:0802.1545, originally February 12, 2008) explicitly works over an algebraically closed field of characteristic zero and notes that nonnilpotent images of \(y\) can occur in positive characteristic. Iyudu's later complete description of its representation varieties (arXiv:1209.0746, September 4, 2012, §13, Theorem 13.1) establishes equidimensionality and partition-indexed irreducible components in characteristic zero. In contrast, the present theorem determines the smallest modular-dimensional exception, proves the failure of equidimensionality in characteristic two, identifies both components and their intersection and singular locus, and counts every labeled representation over finite fields. It does not challenge or reproclaim the characteristic-zero theorem. Bourgeois's paper on the exact equation \(AX-XA=X^2\) (arXiv:1406.0199, Introduction and §2) assumes characteristic zero or characteristic exceeding the matrix size for its main theorems, and §2 expressly excludes characteristic two. Thus it addresses the same matrix relation but does not imply the modular fivefold, its component count or its finite-field census. Work on restricted or super Jordan planes studies different algebras or excludes characteristic two and does not immediately imply this statement.

## Limitations

These assertions concern two-dimensional labeled representations and their *reduced* varieties, not the possibly nonreduced defining schemes. They do not classify higher-dimensional modular representations or similarity orbits and do not determine intersection multiplicities. The originality comparison is a documented best-knowledge literature comparison, not proof of historical uniqueness. Independent review has not been performed.

## References

1. N. K. Iyudu, *The representation theory of the Jordanian algebra*, arXiv:0802.1545v1, first publicly submitted 2008-02-12, https://arxiv.org/abs/0802.1545.
2. N. K. Iyudu, *Representation spaces of the Jordan plane*, arXiv:1209.0746v1, first publicly submitted 2012-09-04; see §2 and §13, https://arxiv.org/abs/1209.0746.
3. N. Andruskiewitsch and H. Peña Pollastri, *On the restricted Jordan plane in odd characteristic*, arXiv:2002.02514, 2020; a distinct positive-characteristic construction, https://arxiv.org/abs/2002.02514.
4. G. Bourgeois, *The matrix equation AX-XA = X^α g(X) over fields or rings*, arXiv:1406.0199, 2014; Introduction and §2 assume characteristic zero or greater than matrix size (or exclude characteristic two), https://arxiv.org/abs/1406.0199.
