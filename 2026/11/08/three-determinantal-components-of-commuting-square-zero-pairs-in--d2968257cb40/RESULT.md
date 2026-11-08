# Three determinantal components of commuting square-zero pairs in the four-by-four nilradical

## Finding
Let \(k\) be any field and \(\mathfrak n_4(k)\) the associative algebra of strictly upper-triangular \(4\times4\) matrices. The **reduced** affine variety
\[
\mathcal X=\{(X,Y)\in\mathfrak n_4(k)^2:X^2=Y^2=0,\ XY=YX\}_{\mathrm{red}}
\]
has **exactly three geometrically irreducible components**, of respective dimensions \(8,7,7\), in every characteristic. The first is affine eight-space. Each of the other two is the product of affine two-space and a rank-at-most-one determinantal cone of matrices of size \(4\times2\) (equivalently \(2\times4\)). In particular, \(\mathcal X\) is not equidimensional.

There are explicit intrinsic coordinate models for all three components, with incidence dimensions \(6,5,6\) for the three pairwise intersections in the order given below. Over every finite field \(\mathbb F_q\), the number of ordered points is
\[
\#\mathcal X(\mathbb F_q)=q^8+2q^7-2q^5.
\]
The finite-field total is included as a consistency check; the previously known exact prescribed-product counts in this algebra already imply this total. The principal finding is the **complete reduced geometric component and incidence description**.

## Assumptions and scope
All schemes and varieties are over \(k\), with \(\mathcal X\) denoting the reduced closed subscheme cut out set-theoretically by the displayed equations. Geometric irreducibility means irreducibility after any extension to an algebraic closure; dimensions refer to geometric Krull dimensions. The statement is valid without restrictions on the characteristic.

Write the independent entries in the order
\[
X=\begin{pmatrix}0&a&b&c\\0&0&d&e\\0&0&0&f\\0&0&0&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&A&B&C\\0&0&D&E\\0&0&0&F\\0&0&0&0\end{pmatrix}.
\]
When \(d=D=0\), set
\[
M=\begin{pmatrix}a&b\\-f&e\end{pmatrix},\quad
N=\begin{pmatrix}A&B\\-F&E\end{pmatrix},\quad
S=\operatorname{diag}(1,-1).
\]
The sign convention is meaningful and valid even in characteristic two, when \(S\) is the identity.

Define the following closed reduced subvarieties:
\[
\begin{aligned}
\mathcal E&=\{a=f=A=F=0\},\\
\mathcal R&=\{d=D=0,\ \operatorname{rank}\begin{pmatrix}M\\N\end{pmatrix}\le1\},\\
\mathcal T&=\{d=D=0,\ \operatorname{rank}\begin{pmatrix}M&SN\end{pmatrix}\le1\}.
\end{aligned}
\]
Every unmentioned coordinate, including \(c,C\), is free subject to the displayed conditions.

## Proof
**1. Exhaustion of the outer stratum.** The square-zero equations are
\[
ad=df=ae+bf=0,\qquad AD=DF=AE+BF=0.
\]
The commutator equations are
\[
aD-Ad=0,\qquad dF-Df=0,\qquad aE+bF-Ae-Bf=0.
\]
If either \(d\ne0\) or \(D\ne0\), these equations force \(a=f=A=F=0\). Conversely, every point of \(\mathcal E\) satisfies all equations, including when \(d=D=0\). Thus all solutions lie in \(\mathcal E\) or in the closed slice \(d=D=0\).

**2. Determinantal factorization of the slice.** On \(d=D=0\), the square-zero equations say exactly \(\det M=\det N=0\). For nonzero rank-one \(M,N\), choose column and row factorizations
\[
M=p\ell^{\mathsf T},\qquad N=qm^{\mathsf T},\qquad p,q,\ell,m\in k^2.
\]
The final commutator coordinate then factors as
\[
aE+bF-Ae-Bf=(p_1q_2+p_2q_1)(\ell_1m_2-\ell_2m_1).
\]
The second factor vanishes precisely when \(M,N\) have a common right factor, equivalently their vertical stack has rank at most one. The first factor vanishes precisely when \(p,Sq\) are dependent, equivalently the horizontal concatenation \((M\mid SN)\) has rank at most one. If either \(M\) or \(N\) is zero, both determinantal rank conditions are automatically satisfied. Hence the slice is exactly \(\mathcal R\cup\mathcal T\) over every field, including characteristic two. The full reduced variety is therefore \(\mathcal E\cup\mathcal R\cup\mathcal T\).

**3. Irreducible components and dimensions.** The first component \(\mathcal E\cong\mathbb A^8\). The vertical stack in \(\mathcal R\) ranges over all \(4\times2\) matrices of rank at most one, with \(c,C\) free. The horizontal matrix in \(\mathcal T\) ranges over all \(2\times4\) matrices of rank at most one, again with \(c,C\) free. A rank-one determinantal cone of format \(u\times v\) is the closure of outer products of two vectors and is geometrically irreducible of dimension \(u+v-1\); this follows directly from its dominant outer-product parametrization with a one-dimensional generic scaling fiber. Therefore \(\dim\mathcal R=\dim\mathcal T=7\). The components are distinct: \(\mathcal E\) contains points with \(d\ne0\); \(\mathcal R\) contains the commuting pair \((E_{12},E_{34})\) not in \(\mathcal T\); and \(\mathcal T\) contains \((E_{12},E_{13})\) not in \(\mathcal R\). Since none is contained in another, they are exactly the three irreducible components.

**4. Incidence dimensions.** Intersecting with \(\mathcal E\) imposes \(d=D=a=f=A=F=0\). Every such point lies in \(\mathcal R\), so \(\mathcal E\cap\mathcal R\cong\mathbb A^6\). It lies in \(\mathcal T\) exactly when \(bE+eB=0\), giving \(\mathcal E\cap\mathcal T\cong\mathbb A^2\times V(bE+eB)\) of dimension five; this is also the triple intersection. Finally, \(\mathcal R\cap\mathcal T\) is the image of
\[
\{(p,q,\ell):p_1q_2+p_2q_1=0\}\subset\mathbb A^6
\]
under \((p,q,\ell)\mapsto(p\ell^{\mathsf T},q\ell^{\mathsf T})\), with \(c,C\) free. The source quadric is geometrically irreducible, and the generic scaling fiber is one-dimensional. Its image is the whole intersection, including the zero-matrix boundaries, so the intersection is geometrically irreducible of dimension \(6\).

**5. Finite-field check.** The number of rank-at-most-one matrices of size \(2\times2\) is \(R=q^3+q^2-q\). For each nonzero \(M\) of rank one, the two commuting partner conditions are two distinct two-dimensional linear subspaces of the four-dimensional space of \(N\), meeting in a line; their union has \(2q^2-q\) elements. At \(M=0\), all \(R\) rank-at-most-one partners are allowed. Thus the slice \(d=D=0\) has \(R+(R-1)(2q^2-q)=2q^5+q^4-2q^3\) pairs of \(M,N\); multiplying by \(q^2\) accounts for \(c,C\). Since \(\#\mathcal E=q^8\) and \(\#(\mathcal E\cap(\mathcal R\cup\mathcal T))=q^6\), inclusion-exclusion yields \(q^8+2q^7-2q^5\).

## Verification
The standalone `verify.py` exhaustively generates every square-zero strictly upper-triangular matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), checks the literal matrix commutator equations, tests membership in each determinantal component, and compares the exact point totals and subcomponent intersection counts with the formulas. The \(\mathbb F_4\) arithmetic uses the irreducible polynomial \(z^2+z+1\). Execute `python3 verify.py`; expected output is embedded in `verify_output.txt`. Finite enumeration does not establish the all-fields result; the determinant-factorization and dimension arguments above do.

## Relationship to prior work
Premet's 2003 work concerns the full commuting variety of nilpotent elements in a reductive Lie algebra. Melnikov's 2007 work classifies orbits and closures for **one** strictly upper-triangular square-zero matrix. Basili's 2008 paper addresses the unrestricted commuting variety of upper-triangular and strictly upper-triangular pairs. Their objects and theorems do not directly specify the three components of the **doubly square-zero** commuting slice described here.

Prior work on prescribed nonzero products in the same strict triangular algebra already establishes the nonzero-product stratum and a finite-field zero-product count; those counts imply the total stated above. This note does not claim those arithmetic totals, or the determinantal rank-one parametrization in isolation, as new. The distinction investigated here is the complete reduced pair variety, including two different determinantal boundary components, a larger affine component and their intersections.

## Limitations
Only the reduced variety and its irreducible components and indicated intersections are classified. Nothing is asserted about the nonreduced defining ideal, embedded components, generic multiplicities or a complete singular-locus classification. The four-by-four size is fixed; no claim about higher ranks is made. The originality comparison is based on the inspected works and accessible research records, not an independent global priority certification.

## References
- A. Premet, *Nilpotent commuting varieties of reductive Lie algebras*, arXiv:math/0302204v1, first publicly posted 2003-02-18. https://arxiv.org/html/math/0302204v1
- A. Melnikov, *B-orbits of nilpotent order 2 and link patterns*, arXiv:math/0703371v1, first publicly posted 2007-03-13. https://arxiv.org/html/math/0703371v2
- R. Basili, *Some remarks on varieties of pairs of commuting upper triangular matrices and an interpretation of commuting varieties*, arXiv:0803.0722v1, first publicly posted 2008-03-05. https://arxiv.org/abs/0803.0722
