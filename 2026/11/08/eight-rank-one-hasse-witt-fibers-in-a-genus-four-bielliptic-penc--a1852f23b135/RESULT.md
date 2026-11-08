# Eight rank-one Hasse–Witt fibers in a genus-four bielliptic pencil over \(\overline{\mathbb F}_{19}\)

## Finding
Let \(k=\overline{\mathbb F}_{19}\). For \(t\in k\), consider the projective complete intersection
\[
C_t:\quad y^2z-x^3+xz^2=0,\qquad w^2-xy-tz^2=0\quad\subset\mathbb P^3_k.
\]
It is smooth of genus four exactly when \(t\ne0\) and \(t^4\ne12\). On this smooth locus, writing \(f_t\) for the geometric \(19\)-rank of the Jacobian and \(a_t\) for its Cartier \(a\)-number, the complete classification is
\[
(f_t,a_t)=\begin{cases}(1,3),&t^4=6\text{ or }t^4=7,\\(2,2),&t^4\notin\{6,7\}.\end{cases}
\]
There are exactly eight exceptional geometric coefficient parameters; all are smooth. They form two four-element orbits under \(t\mapsto it\), where \(i^2=-1\). In particular no smooth member has \(19\)-rank zero or is superspecial. These are coefficient counts, not a classification of geometric isomorphism classes.

## Assumptions and scope
All equations and integers in finite-field identities are reduced modulo \(19\); geometric invariants are computed over \(k\), not merely \(\mathbb F_{19}\). The fixed elliptic quotient is \(E:y^2z=x^3-xz^2\), which is supersingular because the coefficient of \(x^{18}\) in \((x^3-x)^9\) vanishes. The conics \(xy+tz^2=0\) form a simple equivariant pencil on this fixed quotient, containing its point at infinity \(O=[0:1:0]\) and having five further moving branch points. Smoothness, the parameter locus and both Jacobian invariants are asserted for every geometric parameter satisfying the displayed exclusions.

## Proof
### Smoothness and genus
The projection \((x:y:z:w)\mapsto(x:y:z)\) is a degree-two cover of the smooth elliptic cubic \(E\). It branches at its intersection with \(xy+tz^2=0\). At \(O\), use \(y=1\) as a local chart: the elliptic equation gives \(z=x^3-xz^2\), and the conic equation becomes \(x+tz^2\), which vanishes simply at \(O\). If \(t\ne0\), the five affine branch points have \(z=1\), \(x\ne0\), \(y=-t/x\), and their \(x\)-coordinates are the roots of
\[
F_t(x)=x^5-x^3-t^2.
\]
Since \(F'_t(x)=x^2(5x^2-3)\), its nonzero roots are distinct precisely when \(3125t^4-108\ne0\). In characteristic \(19\), this is \(t^4\ne12\). When \(t=0\), the branch divisor has a multiple point at \((x,y)=(0,0)\). Thus the double cover is smooth precisely under the stated exclusions. Six simple branch points give \(2g(C_t)-2=6\) by Riemann–Hurwitz, hence \(g(C_t)=4\).

### Exact Hasse–Witt matrix
For the ordered exponent vectors
\[
e_1=(1,1,1,2),\quad e_2=(1,1,2,1),\quad e_3=(1,2,0,1),\quad e_4=(2,1,1,1),
\]
apply the complete-intersection coefficient formula of Ogasawara–Ohashi–Sakata–Harashita (Lemma 2.10): the \((i,j)\) Hasse–Witt entry is the coefficient of the monomial with exponents \(19e_i-e_j\) in \((PQ)^{18}\), where \(P=y^2z-x^3+xz^2\) and \(Q=w^2-xy-tz^2\). Exact multinomial expansion yields
\[
M(t)=\begin{pmatrix}
0&0&0&0\\
0&-7t^3(t^4+7)&0&7t^5(t^4+8)\\
0&0&0&0\\
0&-7t(t^4-1)&0&7t^3
\end{pmatrix}.
\]
Its potentially nonzero \(2\)-by-\(2\) block is
\[
B(t)=7t\begin{pmatrix}-t^2(t^4+7)&t^4(t^4+8)\\-(t^4-1)&t^2\end{pmatrix},
\]
with exact determinant
\[
\det B(t)=-8t^6(t^8+6t^4+4)=-8t^6(t^4-6)(t^4-7).
\]
Since the lower-right entry of \(B\) is \(7t^3\ne0\) on the smooth locus, \(M\) has rank two away from the two displayed quartic equations and rank one on them. By definition \(a_t=4-\operatorname{rank}M(t)\), giving the asserted \(a\)-numbers. Each of \(t^4-6\) and \(t^4-7\) has four simple roots, and neither overlaps the smoothness exclusions \(t=0\) or \(t^4=12\).

### Stable Frobenius rank
The geometric \(19\)-rank equals the stable rank of the \(19\)-semilinear Hasse–Witt operator. Outside the determinant-zero set, \(B(t)\) is invertible, so the stable rank is two. For the two exceptional fourth-power values choose representatives \(t=9\) (with \(9^4=6\)) and \(t=7\) (with \(7^4=7\)) in \(\mathbb F_{19}\). Their nonzero blocks are
\[
B(9)=\begin{pmatrix}9&10\\8&11\end{pmatrix},\qquad
B(7)=\begin{pmatrix}16&15\\10&7\end{pmatrix}.
\]
Both have determinant zero and nonzero traces, respectively \(1\) and \(4\). Their matrix powers therefore maintain rank one; because these representatives lie in the prime field, Frobenius twists leave their entries fixed. For every fourth root of \(6\) (respectively \(7\)), the ratio to \(9\) (respectively \(7\)) is a fourth root of unity. The transformation
\[
(x,y,z,w,t)\longmapsto(-x,iy,z,\eta w,-it),\qquad i^2=-1,\quad \eta^2=-i,
\]
gives an isomorphism \(C_t\simeq C_{-it}\) over \(k\). Consequently all four roots in each orbit have the same stable rank one. No other smooth geometric parameters occur, so the \(19\)-rank classification is complete.

## Verification
The standalone scripts `verify_expand.py` and `verify_strata.py` use only the Python standard library and can be run by `python3 verify_expand.py` and `python3 verify_strata.py`. The first directly expands both defining forms to the eighteenth power, multiplies the resulting sparse polynomials, and extracts all sixteen Hasse–Witt coefficients. The second derives those coefficients independently using multinomial sums, then verifies the determinant factorization, squarefreeness, disjointness from the singular-parameter divisor, and representative stable-rank checks. Both scripts returned `VERIFY_OK`. The proof of the all-geometric-parameter statement is the symbolic determinant and orbit argument above; finite enumerations alone are not taken as exhaustive geometric proofs.

## Relationship to prior work
Ogasawara, Ohashi, Sakata and Harashita (arXiv:2403.08139, first public 2024-03-12), establish the general genus-four double-elliptic-cover model, smoothness principle and Hasse–Witt coefficient extraction, and classify *superspecial* examples in small characteristics. These methods and their superspecial enumeration are prior work, not new assertions here. Chang, Dragutinović, Groen, Lin, Pacheco-Tallaj and Singhal (arXiv:2502.09540, 2025), prove general dimensions and nonemptiness properties of \(p\)-rank strata of elliptic double-cover moduli. Neither inspected treatment provides the present explicit pencil's eight-point rank-one locus or its complete \((19\text{-rank},a)\) classification. No claim is made to classify all genus-four elliptic double covers.

## Limitations
The eight points are coefficient parameters in this specified pencil; the two four-element orbits are proven, but no assertion of distinct geometric isomorphism classes between the two orbits is made. Newton polygons, additional automorphisms and the complete ambient moduli stratification are not determined. Historical priority against unindexed equivalent specializations remains uncertain. The verification is an exact reproducible same-work calculation, not independent mathematical certification.

## References
- T. Ogasawara, R. Ohashi, K. Sakata and S. Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139 (first submitted 2024-03-12), Sections 2.2, 2.4, 4. https://arxiv.org/abs/2403.08139
- K. Chang, D. Dragutinović, S. R. Groen, Y. Lin, N. Pacheco-Tallaj and D. Singhal, *The p-rank stratification of the moduli space of double covers of a fixed elliptic curve*, arXiv:2502.09540 (2025), Theorem 1.1 and Section 4. https://arxiv.org/abs/2502.09540
