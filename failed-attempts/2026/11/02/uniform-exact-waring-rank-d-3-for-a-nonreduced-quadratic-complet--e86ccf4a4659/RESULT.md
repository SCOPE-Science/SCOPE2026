# Uniform exact Waring rank \(d+3\) for a nonreduced quadratic complete-intersection family
## Finding
For every integer \(d\ge5\), define \(I_d=(Y^2-Z^2,XY,X^d-Z^d)\subset T=\mathbb C[X,Y,Z]\). The homogeneous inverse system of \(T/I_d\) is the degree-\(d+1\) ternary form
\[
F_d=(d+1)x^d z+\frac{(y+z)^{d+1}+(-1)^{d+1}(y-z)^{d+1}}2.
\]
Its complex symmetric Waring rank is exactly
\[\operatorname{Rk}_{\mathbb C}(F_d)=d+3.\]
For \(d=5\), the previously known value \(8\) is recovered; the result asserts the whole infinite range, without a reduced-intersection hypothesis on the two quadrics.
## Assumptions and scope
Work over \(\mathbb C\), with ordinary characteristic-zero differential apolarity. The variables \(X,Y,Z\) act by differentiation on \(x,y,z\). Rank is the minimum number of nonzero scalar multiples of powers of linear forms summing to \(F_d\); equivalently, by the apolarity lemma, the minimum cardinality of a reduced finite projective subscheme with homogeneous ideal inside \(\operatorname{Ann}(F_d)\). All claims are for integers \(d\ge5\).
## Proof
**Inverse system.** Set \(q=Y^2-Z^2\), \(p=XY\), and \(h=X^d-Z^d\). Their first two equations define a length-four projective scheme \(B\) supported at \(P_0=[1:0:0]\) (a double point) and \(P_\pm=[0:1:\pm1]\) (simple points). As \(h\) is nonzero at all three support points, the three forms are a regular sequence, and \(T/I_d\) is an Artinian Gorenstein complete intersection with socle degree \(d+1\). Direct differentiation shows \(q\circ F_d=p\circ F_d=h\circ F_d=0\). The uniqueness of its top-degree inverse system implies \(\operatorname{Ann}(F_d)=I_d\).

**Upper bound.** The degree-\(d+1\) polynomial \(G=X^{d+1}+Z^{d-1}(Y^2-Z^2)\) lies in \(I_d\) by the identity
\[
G=Xh+(XY)(YZ^{d-2})+q(Z^{d-1}-XZ^{d-2}).
\]
Consider \(K=(XY,Y(Y^2-Z^2),G)\subset I_d\). These are the maximal minors, up to sign, of
\[
\begin{pmatrix}q&-X^d\\-X&-Z^{d-1}\\0&Y\end{pmatrix}.
\]
Its projective zero locus consists of the \(d+1\) distinct points \([\zeta:0:1]\) with \(\zeta^{d+1}=1\), together with \([0:1:1]\) and \([0:-1:1]\). There are no points on \(Z=0\). Each point is reduced in the chart \(Z=1\), as the local equations are transverse there; the ideal has height two, hence the Hilbert–Burch theorem identifies \(K\) as a saturated perfect ideal. Thus \(K\) is precisely the radical homogeneous ideal of these \(d+3\) points, providing the upper bound by apolarity.

**A separator lemma.** Let \(S\subset\mathbb P^2\) be a reduced set of at most \(d+2\) points and assume no line contains \(d\) of them. For each \(P\in S\), group the other at most \(d+1\) points by the distinct lines through \(P\). Each group has at most \(d-2\) members. Pair points from different groups as far as possible, then cover the remaining points by singletons. This requires at most \(\max\{d-2,\lceil(d+1)/2\rceil\}=d-2\) lines avoiding \(P\). Their product, padded to degree \(d-2\), separates \(P\) from all other points. Therefore evaluation of degree-\(d-2\) forms onto functions on \(S\) is surjective, and the saturated ideal \(I(S)\) is generated in degrees at most \(d-1\) (the standard separator/regularity lemma for reduced points).

**Lower bound, first reduction.** Suppose \(I(S)\subset I_d\) for a reduced set with \(|S|\le d+2\). Since \((I_d)_1=0\), the set is not collinear. If no line contains \(d\) points, the separator lemma implies \(I(S)\) is generated below degree \(d\), where \((I_d)_j=(q,p)_j\). Thus \(I(S)\subset(q,p)\), which would embed the nonreduced double point of \(B\) into a reduced finite set, impossible. Hence some line \(L\) contains at least \(d\) points of \(S\). If there is only one off-line point, the entire pencil \(I(S)_2\) consists of reducible conics sharing \(L\), contradicting \((I_d)_2=\langle q,p\rangle\), which has no common factor. If there are no off-line points, \(I(S)_1\ne0\). Consequently \(|S|=d+2\), with exactly \(d\) points \(U\) on \(L\) and two points \(V\) off it.

**Lower bound, conic-pencil obstruction.** The unique conic through \(S\) is \(LM\), where \(M\) is the line through the two points \(V\). Because \(LM\in\langle q,p\rangle\), the fact that the only reducible conics in this pencil are \(q=(Y-Z)(Y+Z)\) and \(p=XY\) forces \(LM\in\{q,p\}\) up to scalar. Write \(q'\) for the other quadric. Choose a quadratic \(H_2\) vanishing at both points of \(V\), not divisible by \(M\). Since \(LH_2\in I(S)_3=(I(S)_3\cap(q,p)_3)\), it has an expression \(LH_2=LM A+q'B\) with linear forms \(A,B\). Coprimality of \(L\) and \(q'\) forces \(B=cL\). As \(H_2\) is not divisible by \(M\), \(c\ne0\); on \(M\), the points \(V\) must therefore be the two zeros of \(q'|_M\), counted without multiplicity.

Choose a degree-\(d\) form \(H_d\in I(S)_d\) whose restriction to \(L\) has precisely the simple zeros \(U\). Such a form is obtained by lifting the degree-\(d\) product on \(L\) and correcting values at \(V\) with a multiple of \(L\). Since \((I_d)_d=(q,p)_d+\mathbb C h\), write \(H_d=J_d+ch\). Both \(H_d\) and \(J_d\) vanish at \(V\subset B\), where \(h\) does not vanish, so \(c=0\). Hence \(H_d\in(q,p)_d\), and restricting to \(L\) implies that the degree-\(d\) divisor \(U\) contains the zero divisor of \(q'|_L\).

For \(LM=p=XY\), either \(L=X=0\), so \(q'|_M=-Z^2\) has a double zero and cannot cut out two distinct points \(V\), or \(L=Y=0\), so \(q'|_L=-Z^2\) has a double zero and cannot divide a reduced divisor \(U\). For \(LM=q=(Y-Z)(Y+Z)\), the complementary quadratic \(q'=XY\) vanishes at the intersection \(P_0=L\cap M\), forcing \(P_0\) into both the off-line set \(V\) and the on-line set \(U\), a contradiction. All alternatives fail. Thus no apolar reduced set of length at most \(d+2\) exists, and the upper bound is sharp.
## Verification
The accompanying `verify.py` performs exact symbolic checks (using SymPy) for degrees \(d=5,6,7,8,9,12\): the apolar differential identities, the expression for \(G\) in the ideal, the root distinctness, and the reducible-conic pencil determinant. Running `python verify.py` returned `VERIFY_OK`. These finite checks support, but do not replace, the arguments proving the result uniformly for every \(d\ge5\).
## Relationship to prior work
Bhat–Carlini–Masuti–Sebastian analyze Waring rank of inverse systems of complete intersections and in Example 6.1 consider precisely \(I_5\), exhibiting a reduced apolar set of eight points and a lower bound of five; their stated general sufficient criteria impose conditions on the intersection of the low-degree generators that fail for this nonreduced quadratic base. A previous calculation gave the exact value eight at degree six for this single instance. The present result supplies the uniform exact formula in every degree \(d\ge5\), via a new point-separator and quadratic-pencil argument. Related studies of special ternary Waring decompositions treat different families; pairwise-coprime monomial rank formulas do not apply to these forms.
## Limitations
The result is confined to this explicit family over characteristic zero; it is not a classification of all complete intersections of multidegree \((2,2,d)\). The computed examples do not certify the infinite family independently of the proof. An implicit equivalent statement in additional literature remains possible. No independent mathematical audit has been performed.
## References
1. Bhat, Carlini, Masuti and Sebastian, *Waring rank of certain complete intersection forms*, arXiv:2610.18346v1 (2026), especially Example 6.1 and Theorems 3.4 and 3.6.
2. Angelini, Chiantini and Oneto, *Waring decompositions of special ternary forms with different Hilbert functions*, arXiv:2303.06780v1 (2023).
3. Carlini, Catalisano and Geramita, *The solution to the Waring problem for monomials and the sum of coprime monomials*, arXiv:1112.3474v1.
