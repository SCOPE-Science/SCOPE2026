# The \(\langle2,7\rangle\) cusp, rational normalization, and projective \(C_3\) symmetry of the Klein quartic modulo seven

## Finding
Let \(k\) be any algebraically closed field of characteristic \(7\), and let \(C\subset\mathbf P^2_k\) be the plane curve
\[
F(X,Y,Z)=X^3Y+Y^3Z+Z^3X=0.
\]
Then \(C\) is geometrically integral and rational. Its **only** singular point is \(P=[2:4:1]\); this is a geometrically unibranch cusp with value semigroup \(\langle 2,7\rangle\), delta invariant \(3\), and normalization conductor exponent \(6\).

An explicit normalization \(\nu:\mathbf P^1_k\to C\), with homogeneous source coordinates \([S:T]\), is
\[
\begin{split}
X&=2S^4+S^2T^2-2ST^3+2T^4,\\
Y&=4S^4+S^2T^2+3ST^3+T^4,\\
Z&=S^4+S^2T^2-ST^3+4T^4.
\end{split}
\]
The cusp has the single preimage \([1:0]\). The full group of **projective linear** automorphisms of this embedded singular quartic is precisely \(C_3\). In normalization coordinate \(u=S/T\), its elements act as \(u\mapsto au\), where \(a^3=1\). The visible cyclic permutation \([X:Y:Z]\mapsto[Y:Z:X]\) corresponds to \(u\mapsto4u\). No statement is made that the abstract automorphism group of the normalization has order three.

## Assumptions and scope
All identities take place in characteristic exactly \(7\). The automorphism group is \(\{g\in\operatorname{PGL}_3(k):g(C)=C\}\), not the full automorphism group of \(\mathbf P^1\) or an integral model with stable reduction. This theorem concerns the naive integral plane equation reduced modulo \(7\), not a regular or stable model of the generic Klein quartic over a discrete valuation ring.

## Proof
**1. Singular support.** On \(Z=1\), set \(f(x,y)=x^3y+y^3+x\). The affine Jacobian ideal \((f,f_x,f_y)\) has the reduced lexicographic Groebner basis (over \(\mathbf F_7\))
\[
(x-2y^3,\;y^7+3).
\]
Since \(y^7+3=(y-4)^7\) in characteristic seven, its geometric support is \((x,y)=(2,4)\). On \(Z=0\), the only curve points are \([1:0:0]\) and \([0:1:0]\); the partial derivative with respect to \(Y\), respectively \(Z\), is nonzero there. Thus \(P\) is the sole singular point. This re-establishes a previously recognized characteristic-seven exceptional point; novelty is not claimed for the mere Jacobian test.

**2. The normalization map.** Denote the three quartic binary forms displayed above by \(A,B,D\). Direct polynomial expansion gives \(A^3B+B^3D+D^3A=0\) in \(\mathbf F_7[S,T]\). In the affine coordinate \(u=S/T\), their span is exactly
\[
W=\langle 1,u^2,u^4+6u\rangle\subset H^0(\mathbf P^1,\mathcal O(4)).
\]
In particular the three forms have no common projective zero: if the section \(T^4\) and the section \(S^2T^2\) both vanish, then \(T=0\), whereas \(S^4+6ST^3\ne0\) there. Therefore they define a morphism \(\nu\). The six products \(A^2,AB,AD,B^2,BD,D^2\) are linearly independent as binary octics (the supplied exact coefficient-matrix computation has rank \(6\)); hence the image satisfies no quadratic equation. It is also not a line, because \(A,B,D\) are linearly independent. The degree of the image times the generic degree of \(\nu\) is \(4\), so the image has degree \(4\), and \(\nu\) is birational. It equals \(V(F)\), since that hypersurface has degree \(4\); hence \(F\) is geometrically irreducible. Since \(\mathbf P^1\) is normal and \(\nu\) is a finite birational map of projective integral curves, it is the normalization.

**3. Exact cusp type.** Near \([S:T]=[1:0]\), put \(q=T/S\) and work in the chart \(Z\ne0\). Write \(v=y-4\), \(w=(x-2)-5v\), and
\[
h=w-3v^2-2v^3.
\]
The parametrization gives, with coefficients understood in \(k[[q]]\),
\[
 v=4q^2+O(q^4),\quad w=6q^4+O(q^6),\quad h=q^7+O(q^9).
\]
Thus the branch has multiplicity \(2\) and first characteristic exponent \(7\). Its value semigroup contains the numerical semigroup \(\langle2,7\rangle\), whose colength is \(3\). The cusp has no other normalization preimage: the finite-coordinate equations \(A(u)-2D(u)=0\) and \(B(u)-4D(u)=0\) have greatest common divisor \(1\) in \(\mathbf F_7[u]\); the unique remaining preimage is \([1:0]\). Since the whole degree-four curve has arithmetic genus \(3\) and rational normalization, the delta invariant of this one branch is exactly \(3\), proving that its value semigroup is exactly \(\langle2,7\rangle\). No assertion of formal analytic equivalence to the characteristic-zero \(A_6\) normal form is needed or made (in characteristic \(7\), such equivalence cannot be inferred from the semigroup alone). All remaining points are smooth by Step 1. The conductor in \(k[[q]]\) is \(q^6k[[q]]\).

**4. Exact projective stabilizer.** Every \(g\in\operatorname{PGL}_3(k)\) with \(g(C)=C\) fixes its unique cusp and hence induces an automorphism of the normalization fixing \([1:0]\). Consequently it has the form \(u\mapsto au+b\), with \(a\in k^\times\). Since \(g\) acts linearly on ambient hyperplane sections, its induced pullback stabilizes the three-space \(W\). The coefficient of \(u^3\) in \((au+b)^4+6(au+b)\) is \(4a^3b\). But every element of \(W\) has vanishing cubic coefficient, so \(b=0\). Now the pullback of \(u^4+6u\) is \(a^4u^4+6au\), which lies in \(W\) precisely when \(a^4=a\), or \(a^3=1\). Conversely each such scaling preserves \(W\) and induces a projective automorphism of its image. Since \(k\) contains exactly three cube roots of unity, the group is \(C_3\). Finally direct substitution shows
\[
[A(4u):B(4u):D(4u)]=[B(u):D(u):A(u)],
\]
identifying the cyclic coordinate permutation with one of the two nontrivial elements.

## Verification
Execute `python verify_exact.py` with SymPy. It checks the complete polynomial identity, lack of degree-one and degree-two image relations, affine singular Groebner basis, the two smooth points at infinity, valuations \(2,4,7\) with leading coefficients, the section subspace, and the cyclic symmetry. The exact program prints `KLEIN_CHAR7_NORMALIZATION_A6_PROJECTIVE_C3_CERTIFIED`. The proof above explains the deductions valid over every algebraically closed field of characteristic seven; the computation is a finite polynomial-identity check, not a sample enumeration. The affine linear reparametrization argument determines geometric projective automorphisms, not merely those defined over \(\mathbf F_7\).

## Relationship to prior work
Dolgachev and Martin (arXiv:2303.16170, first posted 2023-03-28, §4.2) identify the Klein quartic and its smooth characteristic behavior, including the exclusion of characteristic seven from the smooth symmetric quartic classification. The exceptional singular point was also explicitly identified in a public 2018 mathematical discussion. These earlier facts are acknowledged. The theorem here adds an explicit quartic normalization, the precise local value semigroup and conductor, and the full projective stabilizer of the **singular** reduction. These statements do not follow directly from a smooth-quartic automorphism classification or from detecting a singular point alone. Bouw et al., *Conductor and discriminant of Picard curves* (2020), discuss special Picard curves and discriminants in related residue characteristics, not this singular embedded normalization or its stabilizer in the inspected relevant sections.

## Limitations
This is a statement about the reduction of one particular plane equation, not the stable reduction of the genus-three curve, and does not classify all integral models, reduction types, or the full automorphism group of the abstract normalization. Literature-search coverage is incomplete; an unindexed earlier normalization or projective-stabilizer computation could affect priority. No independent mathematical audit has been performed.

## References
1. Igor Dolgachev and Gebhard Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170 (initially 2023-03-28), §4.2; journal DOI 10.1112/jlms.12905 (2024). https://arxiv.org/abs/2303.16170
2. Irene I. Bouw et al., *Conductor and discriminant of Picard curves*, Journal of the London Mathematical Society (2020), DOI 10.1112/jlms.12323. https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12323
3. Jyrki Lahtonen, answer to *Klein quartic smooth in Char different from 7* (2018-03-30), identifying the characteristic-seven singular point. https://math.stackexchange.com/questions/2714407/klein-quartic-smooth-in-char-different-from-7
4. *TauCeti: Klein Quartic*, public proof documentation for smoothness away from characteristic seven, https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/PlaneCurve/KleinQuartic.html (accessed 2026-10-27).
