# Cyclotomic gaps in the nilpotency-index spectrum of nine-dimensional quantum complete intersections

## Finding
Let \(k=\mathbb F_q\) be a finite field and \(\lambda\in k^\times\). Define the nine-dimensional quantum complete intersection
\[
A_\lambda=k\langle x,y\rangle/(x^3,y^3,yx-\lambda xy),
\qquad J=(x,y).
\]
For \(w\in J\), let \(\nu(w)\) be the least positive integer \(r\) with \(w^r=0\); thus \(\nu(0)=1\). Define \(N_r=|\{w\in J:\nu(w)=r\}|\). Put
\[
s=1+\lambda+\lambda^2,\qquad
 t=1-\lambda+\lambda^2,\qquad u=1+\lambda^2.
\]
The complete nilpotency-index distribution over **every** finite field is obtained from
\[
C_2=q^5,\qquad
C_3=\begin{cases}
 q^8,&s=0,\\
 (2q-1)q^6,&s\ne0,\ t=0,\\
 q^5(3q-2),&s\ne0,\ t\ne0,
\end{cases}
\]
\[
C_4=\begin{cases}
 q^8,&su=0,\\
 (2q-1)q^6,&su\ne0,
\end{cases}
\qquad C_5=q^8,
\]
by taking
\[
\boxed{N_1=1,\quad N_2=C_2-1,\quad
N_3=C_3-C_2,\quad N_4=C_4-C_3,\quad N_5=C_5-C_4.}
\]
Every element of \(J\) has fifth power zero. These formulas therefore specify the full distribution, not a lower bound or an experimental pattern.

There are two sharp consequences. **An element of nilpotency index four exists exactly when \(st\ne0\)**, whereas **an element of nilpotency index five exists exactly when \(su\ne0\)**. In particular, if \(t=0\) and \(s\ne0\), then no element has index four although exactly \(q^6(q-1)^2\) elements have index five. If \(s=0\), every element of \(J\) has cube zero although \(J^4\ne0\). In the generic case \(su\ne0\), a proportion \((1-q^{-1})^2\) of the radical has index five.

## Assumptions and scope
The parameter \(\lambda\) may be any nonzero field element, including \(1\), and the field may have characteristic two or three. Products are in the associative, unital algebra \(A_\lambda\), and the index is the **elementwise** nilpotency index, not the ideal nilpotency class. The ordered monomials \(x^iy^j\), \(0\le i,j\le2\), form a basis by the skew-polynomial normal form. The Jacobson radical \(J\) consists exactly of the eight-dimensional zero-constant-term subspace. The algebras for \(\lambda\) and \(\lambda^{-1}\) are isomorphic on interchanging \(x\) and \(y\), and each of \(s,t,u\) has a vanishing condition invariant under that inversion.

## Proof
For basis monomials one has the normal-form product
\[
(x^iy^j)(x^ry^v)=\begin{cases}
\lambda^{jr}x^{i+r}y^{j+v},&i+r\le2,\ j+v\le2,\\
0,&\text{otherwise}.
\end{cases}
\]
Write any \(w\in J\) uniquely as
\[
w=ax+by+cx^2+dxy+ey^2+fx^2y+gxy^2+hx^2y^2.
\]
The degree-two part of \(w^2\) is \(a^2x^2+(1+\lambda)abxy+b^2y^2\). Thus \(w^2=0\) forces \(a=b=0\). Conversely, with these two coefficients zero, the entire square reduces to
\[
w^2=\bigl(\lambda d^2+(1+\lambda^4)ce\bigr)x^2y^2.
\]
If \(1+\lambda^4=0\), the displayed equation is equivalent to \(d=0\), leaving exactly \(q^2\) choices of \((c,d,e)\). Otherwise, for \(d=0\) there are \(2q-1\) choices with \(ce=0\), while for \(d\ne0\) there are \((q-1)^2\) choices with \(ce=-\lambda d^2/(1+\lambda^4)\). This again totals \(q^2\). The free \((f,g,h)\) give \(C_2=q^5\).

A direct expansion in the same normal form yields the universal identity
\[
\begin{aligned}
w^3=s\big[&a^2b\,x^2y+ab^2\,xy^2\\
&+\big(t(a^2e+b^2c)+(1+\lambda)abd\big)x^2y^2\big].
\end{aligned}
\]
If \(s=0\), every cube vanishes. Otherwise, the independent degree-three monomials force \(ab=0\). For \(a=b=0\), all remaining six coefficients are free, giving \(q^6\) solutions. If \(a\ne0,b=0\), the final equation becomes \(te=0\). This contributes \((q-1)q^6\) choices when \(t=0\) or \((q-1)q^5\) choices otherwise. The case \(a=0,b\ne0\) is symmetric, with \(c\) in place of \(e\). These three disjoint cases give \(C_3\).

One further multiplication gives
\[
w^4=su\,a^2b^2x^2y^2,\qquad w^5=0.
\]
If \(su=0\), all fourth powers vanish. Otherwise, \(w^4=0\) is equivalent to \(ab=0\), giving \((2q-1)q^6\) elements. This gives \(C_4,C_5\). Subtracting nested power-zero sets gives the claimed \(N_r\).

For the two existence statements, \(t=0\) implies \(u=\lambda\ne0\), and if also \(s\ne0\) then \(C_3=C_4\), hence \(N_4=0\) while \(N_5=q^6(q-1)^2>0\). When \(s,t\ne0\) and \(u\ne0\), \(N_4=2q^5(q-1)^2>0\); when \(s,t\ne0\) and \(u=0\), \(N_4=q^5(q^3-3q+2)=q^5(q-1)^2(q+2)>0\). When \(s=0\), \(N_4=0\) by cube-zero. Thus \(N_4>0\iff st\ne0\). The formula for \(N_5\) gives \(N_5>0\iff su\ne0\). Finally \(x^2y^2\ne0\) lies in \(J^4\), even at \(s=0\), proving the strict distinction between elementwise cube-zero and ideal cube-zero.

## Verification
The standalone `verify.py` constructs the complete nine-dimensional multiplication table and directly enumerates all \(q^8\) radical elements for \((q,\lambda)=(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)\). Its finite fields of order four use the irreducible polynomial \(X^2+X+1\). For every enumerated element, successive powers are multiplied in the algebra to obtain its index independently of the derived counting formulas. The program compares full five-entry histograms to the formulas. It also directly enumerates all five lower-degree coefficients at selected parameters over fields of orders five and seven, using the proved degree-filtration independence to account for the remaining three coefficients. It prints `VERIFY_OK_QCI_NILPOTENCE` on success.

The separate `verify_symbolic.py` expands the products in the PBW basis over the integral coefficient polynomial ring using integer-polynomial arithmetic and verifies all critical identities for \(w^2,w^3,w^4,w^5\). It prints `VERIFY_OK_QCI_SYMBOLIC` on success. Both programs were executed successfully. The proof covers all finite fields; the finite tests are supplementary and do not claim exhaustive checking outside the enumerated cases.

For orientation, the distributions \((N_1,N_2,N_3,N_4,N_5)\) over \(\mathbb F_3\) are \((1,242,6318,0,0)\) for \(\lambda=1\) and \((1,242,3402,0,2916)\) for \(\lambda=-1\). Over \(\mathbb F_4\), the parameter \(\lambda=1\) gives \((1,1023,9216,55296,0)\), while the two nonidentity parameters each give \((1,1023,64512,0,0)\).

## Relationship to prior work
Bergh, Erdmann and Jorgensen (arXiv:1910.06714, posted 2019-10-15) work with quantum complete intersections with a specially chosen root-of-unity parameter and prove, using an earlier lemma, that all nonzero linear combinations of the generators have the prescribed nilpotency index. Their paper investigates Jordan types of modules and Auslander–Reiten components, not the all-radical, all-parameter elementwise nilpotency distribution above. In the root-of-unity case their generator statement is consistent with the cube-zero branch; that branch is not presented as new by itself.

Erdmann and Hellstrøm-Finnsen (arXiv:1703.05962, posted 2017-03-17) investigate Hochschild cohomology for the same two-generator quantum complete intersection presentation, primarily with the skew parameter a primitive root of unity. Their main results concern cohomology groups and nilpotent classes in the **cohomology ring**, not nilpotency indices of all elements of the algebra itself. Jin and Zhang (arXiv:2208.05687, first posted 2022-08-11) study compatible bi-Frobenius and Hopf structures on quantum complete intersections; their structural restrictions do not provide the stated counting distribution. The nilpotence-spectrum calculation concerns a different invariant from all three works.

The full finite-field phase diagram and the missing-index-four phenomenon are the proposed contribution. No claim of publication priority or independent certification is made. A more general unpublished polynomial-identity or finite-algebra enumeration theorem could imply the result.

## Limitations
The result treats the natural first two-generator exponent-three family, not arbitrary exponents or numbers of quantum generators. The count is of elements in the radical, not isomorphism classes, ideals, or cyclic modules. It does not determine Jordan types of left multiplication by every element. The arithmetic branches may coincide in some small fields, and the distribution does not classify parameters up to algebra isomorphism. Exhaustive checks are limited to the listed fields; publication-priority assessment is provisional.

## References
1. P. A. Bergh, K. Erdmann, D. A. Jorgensen, *Modules of constant Jordan type over quantum complete intersections*, arXiv:1910.06714, first posted 2019-10-15, https://arxiv.org/abs/1910.06714.
2. K. Erdmann, M. Hellstrøm-Finnsen, *Hochschild cohomology of some quantum complete intersections*, arXiv:1703.05962, first posted 2017-03-17, https://arxiv.org/abs/1703.05962.
3. H. Jin, P. Zhang, *Bi-Frobenius algebra structure on quantum complete intersections*, arXiv:2208.05687, first posted 2022-08-11, https://arxiv.org/abs/2208.05687.
