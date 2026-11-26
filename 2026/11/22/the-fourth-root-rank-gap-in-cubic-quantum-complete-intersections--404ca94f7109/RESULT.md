# The fourth-root rank gap in cubic quantum complete intersections

## Finding
Let \(q\) be any prime power and \(\lambda\in\mathbb F_q^\times\). For the nine-dimensional algebra
\[
A_{\lambda}=\mathbb F_q\langle x,y\rangle/(x^3,y^3,yx-\lambda xy),
\]
write \(C_r(\lambda)=\#\{a\in A_\lambda:\operatorname{rank}_{\mathbb F_q}([a,-])=r\}\). Here \([a,b]=ab-ba\) is the associative commutator. All \(C_r\) for \(0\le r\le4\) are given by this exact, characteristic-uniform table; the entries in every row total \(q^9\):

| Parameter stratum | \(C_0\) | \(C_1\) | \(C_2\) | \(C_3\) | \(C_4\) |
|---|---|---|---|---|---|
| \(\lambda=1\) | \(q^9\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \(\lambda=-1\ne1\) | \(q^6\) | \(0\) | \(q^9-q^6\) | \(0\) | \(0\) |
| \(\lambda\) of multiplicative order four | \(q^2\) | \(q^2(q+1)(q^2-1)\) | \(q^2(q^5-q^3-q^2+q)\) | \(0\) | \(q^7(q^2-1)\) |
| All remaining twists | \(q^2\) | \(q^2(q^2-1)\) | \(q^4(q^2+q-2)\) | \(q^4(q-1)(q^2-1)\) | \(q^7(q^2-1)\) |

The parameter cases are disjoint and exhaustive. The third row is equivalently \(\lambda^2=-1\) in odd characteristic; in characteristic two that equation forces \(\lambda=1\), which belongs to the first row. In particular, away from the commutative and exterior-type degenerations, **adjoint rank three disappears precisely when \(\lambda\) is a primitive fourth root**, although ranks one, two, and four still occur. At ordinary twists all five ranks occur. This is a sharp cyclotomic rank-gap transition and a complete all-parameter centralizer census. Each element of rank \(r\) has precisely \(q^{9-r}\) commuting partners, so the table also gives the commuting-pair count \(\sum_{r=0}^4 C_r(\lambda)q^{9-r}\) and the commuting probability \(q^{-9}\sum_{r=0}^4 C_r(\lambda)q^{-r}\).

The generic specialization for a primitive cube root of unity was already established separately and is **not asserted to be new**. The all-twist classification and, in particular, the primitive-fourth-root rank-three disappearance are the proposed contribution.

## Assumptions and scope
The algebra is associative, unital, and defined over the displayed finite field. The ordered PBW monomials \(x^iy^j\), \(0\le i,j\le2\), form its nine-element vector-space basis. The center is the set of \(a\) for which \(\operatorname{ad}_a=0\), so the number of central elements is \(C_0\). Thus the center has dimension nine at \(\lambda=1\), six at \(\lambda=-1\ne1\), and two otherwise. Rank means rank of the linear map \(b\mapsto[a,b]\), not the rank of left multiplication, the nilpotency index, or the size of the unit-group orbit. The theorem covers characteristic two and all finite-field extensions. It treats exactly the two-generator exponent-three family, not arbitrary quantum complete intersections.

## Proof
**Normal form.** The relation \(yx=\lambda xy\) gives the multiplication rule
\[
(x^iy^j)(x^ky^\ell)=\begin{cases}
\lambda^{jk}x^{i+k}y^{j+\ell},&i+k\le2,\ j+\ell\le2,\\
0,&\text{otherwise}.
\end{cases}
\]
The usual skew-polynomial normal form proves linear independence of the nine displayed basis monomials. Write a general element as
\[
a=\alpha+u x+v y+A x^2+B xy+C y^2+D x^2y+E xy^2+F x^2y^2.
\]
The coefficients \(\alpha,F\) contribute no commutator, providing a free factor \(q^2\) to all seven-coordinate counts. Every commutator lies in the four-dimensional space spanned by \(xy,x^2y,xy^2,x^2y^2\), so rank never exceeds four.

**Commutator matrix.** Suppose first \(\lambda\ne1\). Set \(h=1+\lambda\) and \(k=1+\lambda^2\). Relative to input columns \(x,y,x^2,xy,y^2,x^2y,xy^2\) and output rows \(xy,x^2y,xy^2,x^2y^2\), direct use of the product rule gives \(\operatorname{ad}_a=(\lambda-1)M\), where
\[
M=\begin{pmatrix}
v&-u&0&0&0&0&0\\
B&-Ah&vh&-u&0&0&0\\
Ch&-B&0&v&-uh&0&0\\
Eh&-Dh&Chk&0&-Ahk&vh&-uh
\end{pmatrix}.
\]
Because \(\lambda-1\ne0\), the desired rank is \(\operatorname{rank}M\).

**Nonzero linear part.** If \(h\ne0\) and \((u,v)\ne(0,0)\), the first three rows are independent: when \(v\ne0\) use the distinct pivot in column \(x^2\), and when \(u\ne0\) use that in column \(y^2\), together with the first row. The final row has a nonzero entry in one of the last two columns (\(vh,-uh\)), where all first three rows vanish. Thus rank is four, for exactly \((q^2-1)q^5\) active-coordinate choices, and after restoring \(\alpha,F\) its multiplicity is \(q^7(q^2-1)\). If \(h=0\), the next case applies instead.

**Zero linear part with \(h\ne0\).** Now take \(u=v=0\). The only possibly nonzero rows are the last three; the middle two rows have first-two-column matrix
\[
R=\begin{pmatrix}B&-Ah\\ Ch&-B\end{pmatrix},
\qquad \det R=h^2AC-B^2.
\]
As \(h\ne0\), the equation \(\det R=0\) has exactly \(q^2\) solutions in \((A,B,C)\): for \(A\ne0\) choose \(A,B\) and solve uniquely for \(C\), or for \(A=0\) impose \(B=0\) and freely choose \(C\). Only the zero triple makes \(R=0\); hence the counts for ranks zero, one, and two of \(R\) are \(1,q^2-1,q^3-q^2\).

If \(k\ne0\), the final row has additional coordinates \((Chk,-Ahk)\) in columns \(x^2,y^2\). When \((A,C)\ne(0,0)\), those coordinates raise the rank by one. If \(A=C=0\) but \(B\ne0\), then \(R\) already has rank two and the final row lies in its row space; there are \(q-1\) such triples. For \(A=B=C=0\), the remaining final row is \((Eh,-Dh)\), which has rank one for \(q^2-1\) pairs \((D,E)\). Summing the cases gives the **seven-coordinate** counts
\[
(c_0,c_1,c_2,c_3,c_4)=
\bigl(1,q^2-1,q^2(q^2+q-2),q^2(q-1)(q^2-1),(q^2-1)q^5\bigr).
\]
Multiplying all entries by \(q^2\) proves the last table row.

If \(k=0\), the last row lies wholly in the same two-column space as \(R\), so rank at most two whenever \(u=v=0\). For \(R=0\), the \(q^2\) possibilities for \((D,E)\) contribute one rank-zero and \(q^2-1\) rank-one matrices. Each of the \(q^2-1\) rank-one choices of \(R\) has exactly \(q\) final-row values in its row-space and \(q^2-q\) outside it. Each of the \(q^3-q^2\) rank-two matrices stays rank two for all \(q^2\) final rows. Therefore the seven-coordinate counts are
\[
(c_0,c_1,c_2,c_3,c_4)=
\bigl(1,(q+1)(q^2-1),q^5-q^3-q^2+q,0,(q^2-1)q^5\bigr).
\]
Again multiplication by \(q^2\) proves the primitive-fourth-root row. Here \(k=0\) and \(h\ne0\) imply \(\lambda\) has multiplicative order four, because in a field of characteristic two \(-1=1\), so \(\lambda^2=-1\) would force \(\lambda=1\).

**Exterior-type twist and commutative twist.** If \(h=0\) with \(\lambda\ne1\), then \(\lambda=-1\) in odd characteristic. The last matrix row vanishes and the first three have rank two whenever \((u,v,B)\ne(0,0)\), otherwise rank zero. Of the seven active coordinates exactly \(q^4\) give rank zero; multiplying by \(q^2\) recovers \(C_0=q^6\). Every other element has rank two. Finally \(\lambda=1\) makes the algebra commutative, so every rank is zero. This exhausts all fields, twists and elements.

## Verification
The accompanying standalone `checker.py` builds the multiplication table directly from the defining skew relation, forms every element's commutator matrix by subtracting its two ordered products, and computes finite-field ranks by Gaussian elimination, without implementing the above reduced four-by-seven proof matrix. Run `python3 checker.py` from the extracted package. The recorded `checker-output.txt` gives nine exhaustive field-and-twist tests over the prime fields of orders two, three and five and the extension field of order four; all four strata have an exhaustive representative. Five further field-and-twist pairs were sampled, checking only whether the observed ranks are allowed. Exactly \(q^2\) scalar/socle choices lift every checked active-coordinate vector to a distinct full algebra element. The exhaustive checks establish the displayed formulas for those finite instances only; the algebraic count proves them for all prime powers.

## Relationship to prior work
Bergh–Oppermann (2007) gives the quantum-complete-intersection algebra and a foundational representation-theoretic analysis, not an elementwise commutator-rank distribution. The known centralizer-spectrum theorem for exponent pattern \((2,m)\), “Cyclotomic resonance in the centralizer spectra of two-generator quantum complete intersections,” has a different monomial quotient and does not cover the \((3,3)\) algebra. The existing computation “Exact element adjoint-rank and conjugacy-class census for a primitive cubic quantum complete intersection” (a prior mathematical record in this algebra family) gives precisely the **generic** row of the table at primitive third roots, and that row in that specialization is fully credited as covered. The all-radical elementwise nilpotency-index distribution for the \((3,3)\) algebra detects other cyclotomic effects, but cannot determine the kernel dimensions of the commutator operator. A separate study of left-multiplication Jordan types and principal right ideals covers the primitive-cube parameter, but neither gives the all-parameter centralizer phase diagram nor the order-four gap. In particular, neither previous specified-root computation covers the order-four locus \(\lambda^2=-1\).

## Limitations
The classification does not apply to exponent patterns other than \((3,3)\) or to more than two quantum generators. This is a census of centralizer **dimensions**, not a classification of their subalgebra isomorphism types, conjugacy orbits, or centralizer scheme structures. Primitive fourth roots exist only when \(4\mid(q-1)\); when absent the corresponding row describes no points in that field. Independent external validation and exhaustive historical priority checking have not been performed. Existing generic primitive-cube formulas are not claimed as original, and unindexed earlier calculations with general parameters could reduce the novelty of the full classification.

## References
1. P. A. Bergh and S. Oppermann, “The representation dimension of quantum complete intersections,” arXiv:0710.2606, first public posting 2007-10-13, https://arxiv.org/abs/0710.2606.
2. D. J. Benson, K. Erdmann and M. Holloway, “Rank varieties for a class of finite-dimensional local algebras,” *J. Pure Appl. Algebra* 211 (2007), 497–510, DOI 10.1016/j.jpaa.2007.02.006; first public online date 2007-03-25.
3. “Cyclotomic resonance in the centralizer spectra of two-generator quantum complete intersections,” published mathematical record 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-cyclotomic-resonance-in-the-centralizer-spectra-of-two-generator--56b11792d0e8.
4. “Cyclotomic gaps in the nilpotency-index spectrum of nine-dimensional quantum complete intersections,” published mathematical record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cyclotomic-gaps-in-the-nilpotency-index-spectrum-of-nine-dimensi--34b3aa08e8c0.
5. “A six-stratum Jordan census and principal right-ideal count for the cubic quantum complete intersection,” published mathematical record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-six-stratum-jordan-census-and-principal-right-ideal-count-for--7f6201de1b8d.
