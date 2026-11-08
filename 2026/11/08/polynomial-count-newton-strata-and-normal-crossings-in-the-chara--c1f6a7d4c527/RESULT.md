# Polynomial-count Newton strata and normal crossings in the characteristic-three Ciani family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\), and put
\[
F_{a,b,c}=X^4+Y^4+Z^4+aX^2Y^2+bY^2Z^2+cZ^2X^2.
\]
The smooth Ciani coefficient space is the open set \(U\subset\mathbb A_k^3\) defined by
\[
(a^2-1)(b^2-1)(c^2-1)\Delta\ne0,\qquad
\Delta=a^2+b^2+c^2-abc-1.
\]
Set \(h_X=b+ac\), \(h_Y=c+ab\), \(h_Z=a+bc\). At every geometric point of \(U\), the \(3\)-rank of \(J(C_{a,b,c})\) is the number \(f\) of nonzero entries among \(h_X,h_Y,h_Z\). Its \(a\)-number is \(3-f\), and its Newton slopes are \(f\) copies of \(0\), \(2(3-f)\) copies of \(1/2\), and \(f\) copies of \(1\).

The reduced nonordinary divisor \(D=V(h_Xh_Yh_Z)\cap U\) is a *strict simple normal crossings* divisor with three smooth irreducible components. The three pairwise intersections are the three coordinate axes, restricted to \(U\); the unique triple point is the Fermat coefficient triple \((0,0,0)\), with \(3\)-rank zero and superspecial Jacobian.

For every integer \(n\ge1\), writing \(q=3^n\), the exact counts of coefficient triples \((a,b,c)\in U(\mathbb F_q)\) by \(3\)-rank are
\[
\begin{array}{c|c}
f&N_f(q)\\\hline
0&1\\
1&3(q-3)\\
2&3(q-3)(q-5)\\
3&(q-3)(q^2-7q+18).
\end{array}
\]
In particular, \(\#U(\mathbb F_q)=(q-2)^3-(q-3)^2\). The counts are for parameterized quartic equations, *not* isomorphism classes of curves.

## Assumptions and scope
The base field is algebraically closed of characteristic three for the geometric assertions. The rational-point counts use the literal coefficient space over \(\mathbb F_{3^n}\) and the same smoothness discriminant. No quotient by diagonal changes of coordinates, permutations, or the full isomorphism group is taken. The primary object is the three-dimensional natural family of smooth genus-three Ciani curves; the defining equation is its standard marked form.

## Proof
**1. Smoothness.** In characteristic three,
\[
F_X=X(X^2-aY^2-cZ^2),\quad F_Y=Y(Y^2-aX^2-bZ^2),\quad F_Z=Z(Z^2-bY^2-cX^2).
\]
If exactly one coordinate vanishes at a singular point, the complementary two-by-two matrix in its squared coordinates is singular, so one among \(a^2,b^2,c^2\) equals \(1\); the converse follows by choosing the corresponding two nonzero squared coordinates over \(k\). If all coordinates are nonzero, their squares lie in the nullspace of
\[
M=\begin{pmatrix}1&-a&-c\\-a&1&-b\\-c&-b&1\end{pmatrix},\qquad\det M=-\Delta.
\]
Provided none of \(a^2,b^2,c^2\) equals \(1\), every nonzero nullvector of \(M\) has all three coordinates nonzero (each complementary principal two-by-two minor is invertible); square roots yield a singular point. Hence the displayed open set is precisely the smooth locus. A smooth plane quartic has genus three.

**2. Hasse–Witt matrix.** The connecting isomorphism from \(0\to\mathcal O_{\mathbb P^2}(-4)\to\mathcal O_{\mathbb P^2}\to\mathcal O_C\to0\) identifies \(H^1(C,\mathcal O_C)\) with the three Čech classes represented by \(X^{-2}Y^{-1}Z^{-1}\), \(X^{-1}Y^{-2}Z^{-1}\), and \(X^{-1}Y^{-1}Z^{-2}\). Frobenius is computed by raising these monomials to their third powers, multiplying by \(F_{a,b,c}^2\), then retaining the three cohomological classes. All exponents in \(F^2\) are even; the cross entries vanish, and coefficient extraction gives
\[
H=\operatorname{diag}(2(b+ac),\,2(c+ab),\,2(a+bc)).
\]
This diagonal matrix represents a semilinear map. Every iterate has the same nonzero diagonal positions, so its stable rank is \(f=\#\{h_i\ne0\}\), while its first-kernel dimension (the \(a\)-number) is \(3-f\).

**3. Newton slopes.** The three sign involutions (two independent modulo projective scalar) yield elliptic quotient curves \(E_X,E_Y,E_Z\); the total quotient by the Klein four group is a conic. The three nontrivial characters give the three elliptic factors of the Jacobian up to a power-of-two isogeny. In fact the corresponding degree-eight isogeny is explicit in Ohashi, Section 3 [2]. Because the characteristic is three, it preserves the associated rational Dieudonné isocrystal and Newton polygons. Completing the square in the quotient \(E_X\) yields a genus-one equation \(V^2=A Y^4+B Y^2Z^2+C Z^4\), with \(B\) a nonzero scalar multiple of \(h_X=b+ac\); analogous formulas hold cyclically. In characteristic three the Hasse invariant of such a quartic model is its middle coefficient \(B\), so precisely the \(h_i=0\) elliptic factors have slopes \((1/2,1/2)\), while the others have slopes \((0,1)\). This proves the Newton-slope assertion.

**4. Crossing geometry.** The components are graphs
\[
D_X:\ b=-ac,\qquad D_Y:\ c=-ab,\qquad D_Z:\ a=-bc,
\]
intersected with \(U\); each is a nonempty smooth irreducible open subset of an affine plane. On \(D_X\cap D_Y\), the identity \((1-a^2)c=0\), together with the unit \(1-a^2\) on \(U\), gives \(b=c=0\), so the intersection is the \(a\)-axis inside \(U\). Cyclically the other intersections are the other axes. At a point \((a,0,0)\), the gradients of \(h_X,h_Y\) restricted to the \((b,c)\) coordinates have determinant \(1-a^2\), a unit; thus the intersection is transverse. At the unique triple point \((0,0,0)\), the three gradients form a basis. Each component occurs with multiplicity one in \(V(h_Xh_Yh_Z)\). Therefore \(D\) is a reduced strict simple normal crossings divisor.

**5. The smooth coefficient count.** Write \(S=\mathbb F_q\setminus\{1,-1\}\), with \(\#S=q-2\). At fixed \(a,b\in S\), the singular-discriminant equation is
\[
c^2-ab c+(a^2+b^2-1)=0,
\]
whose discriminant is \((a^2-1)(b^2-1)\). Let \(\chi\) be the quadratic character extended by \(\chi(0)=0\). Since \(\sum_{t\in\mathbb F_q}\chi(t^2-1)=-1\), the number of solutions with \(a,b\in S\) and unrestricted \(c\) is
\[
(q-2)^2+\left(\sum_{a\in S}\chi(a^2-1)\right)^2=(q-2)^2+1.
\]
One can verify the character sum by counting solutions of \((t-u)(t+u)=1\), a bijection with nonzero values of \(t-u\). At \(c=1\) the discriminant equation becomes \((a+b)^2=0\), and at \(c=-1\) it becomes \((a-b)^2=0\); each excluded value of \(c\) contributes \(q-2\) pairs. The number of singular triples in \(S^3\) is therefore \((q-3)^2\), proving \(\#U(\mathbb F_q)=(q-2)^3-(q-3)^2\).

**6. Counts for each rank.** On \(D_X\), put \(b=-ac\). A direct substitution gives \(\Delta=-(a^2-1)(c^2-1)\), so \(D_X(\mathbb F_q)\) is precisely the set of pairs \((a,c)\) satisfying \(a,c\ne\pm1\) and \(ac\ne\pm1\). For \(a=0\), there are \(q-2\) choices of \(c\); for each of the \(q-3\) values \(a\in\mathbb F_q^\times\setminus\{\pm1\}\), four distinct choices of \(c\) are forbidden. Thus
\[
\#D_X(\mathbb F_q)=(q-2)+(q-3)(q-4)=q^2-6q+10.
\]
Each pairwise intersection axis contains \(q-2\) rational points, and the triple intersection one. The rank-zero count is one; rank one occurs on exactly two components and has count \(3(q-3)\). Rank two occurs on exactly one and has count \(3[(q^2-6q+10)-2(q-2)+1]=3(q-3)(q-5)\). Subtracting all nonordinary counts from the total in Step 5 yields \((q-3)(q^2-7q+18)\) rank-three triples. All formulas are valid for every \(n\ge1\), including \(q=3\), when the two last nonordinary strata are empty.

## Verification
Run `python3 verify.py` from this package directory. It uses only the Python standard library and independently checks: all nine Hasse–Witt coefficient extractions in the generic squared quartic; the polynomial substitution identities for the discriminant; irreducibility of the displayed finite-field presentations; and exhaustive counts in \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). The actual output is included as `VERIFY_OUTPUT.txt`. These finite enumerations are reproducibility cross-checks, not an infinite proof; Steps 1–6 above prove the universal statements.

## Relationship to prior work
The Ciani family is classical; Basson–Lercier–Ritzenthaler–Sijsling [1] study coefficient invariants on its complex locus. Ohashi [2] gives the smoothness criterion and explicit prime-to-three elliptic decomposition, which already controls the abstract Newton polygon through the elliptic quotients. Ohashi–Kudo–Harashita [3] explicitly distinguish the Ciani cases from their cyclic-automorphism families. This result **does not claim** the Ciani family, its elliptic splitting, or the superspeciality criterion as new. Its specific contribution is the scheme-theoretic normal-crossing description of the nonordinary coefficient divisor together with the all-extension polynomial point counts of each exact Newton stratum. The latter requires the discriminant character-sum calculation and the component intersection arithmetic, not just the existence of an elliptic isogeny. No equivalent complete parameter-space count or SNC claim was identified in the accessible inspected sources; historical priority remains open to further specialist checks.

## Limitations
This theorem concerns the smooth marked coefficient space; changing coefficients may produce isomorphic curves, so the displayed counts are **not** counts of isomorphism classes or moduli-stack masses. The normal-crossing conclusion holds inside \(U\), not at removed singular quartics. It does not classify the principal polarization, or finer isomorphism types of the \(3\)-torsion group scheme. The prime-to-three elliptic decomposition is used as known published input; the symbolic checker does not independently rederive that isogeny. The source-comparison search is best-knowledge and cannot prove historical novelty.

## References
[1] R. Basson, R. Lercier, C. Ritzenthaler, J. Sijsling, *An explicit expression of the Lüroth invariant*, arXiv:1211.1327v1 (first posted 2012-11-06), Section 3, https://arxiv.org/abs/1211.1327.

[2] R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1 (2022), Lemma 2.1 and Section 3, https://arxiv.org/html/2201.12996v1.

[3] R. Ohashi, M. Kudo, S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (2021/2024), https://arxiv.org/abs/2111.09777.
