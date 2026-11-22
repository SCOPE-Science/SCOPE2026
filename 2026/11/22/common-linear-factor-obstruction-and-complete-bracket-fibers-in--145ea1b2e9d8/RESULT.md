# Common-linear-factor obstruction and complete bracket fibers in a free class-four Lie algebra

## Finding

Let \(K=\mathbb F_q\) be a finite field, with \(q\) an arbitrary prime power. Let \(L\) be the free nilpotent Lie algebra of class four on two generators. For a prescribed \(T\in[L,L]\), the number \(N_q(T)\) of **ordered** pairs \((r,s)\in L^2\) with \([r,s]=T\) is calculated below, with no characteristic restriction.

Choose the Hall basis \(x,y,z,u,v,a,b,c\) with
\[
z=[x,y],\quad u=[x,z],\quad v=[y,z],\quad a=[x,u],\quad b=[x,v]=[y,u],\quad c=[y,v].
\]
For \(T=wz+U_1u+U_2v+V_1a+V_2b+V_3c\), write \(U=U_1X+U_2Y\) and \(V=V_1X^2+V_2XY+V_3Y^2\). Put \(h(U,V)\) equal to the number of distinct \(K\)-rational projective linear factors common to \(U\) and \(V\), allowing every line to divide the zero polynomial. Thus \(h(0,0)=q+1\). Then
\[
N_q(T)=\begin{cases}
q^8(q^2-1),&w\neq0,\\
q^9(q^2-1)h(U,V),&w=0,\ (U,V)\neq(0,0),\\
q^{12}+(q+1)q^9(q^2-1),&T=0.
\end{cases}
\]
Consequently a nonzero target with \(w=0\) is a single bracket precisely when its linear and quadratic components have a common \(K\)-rational projective factor. Every derived element is a sum of at most two brackets, and the minimum uniform bound is two. The number of distinct single brackets is
\[
(q-1)q^5+(q^2-1)q^2+\frac{(q^2-1)(q+2)}2+1.
\]
In particular the fraction of commuting ordered pairs is
\[q^{-4}+(q+1)(q^2-1)q^{-7}.\]

## Assumptions and scope

All statements concern the eight-dimensional **ordinary free Lie algebra quotient** on two generators by brackets of length at least five. Its dimensions by bracket degree are \(2,1,2,3\); the degree-four component is central. This is an algebra over every finite field, including characteristic two. In characteristic two the bracket is alternating, so skew-symmetry must be interpreted in the alternating sense. No characteristic-zero extension result is assumed as a proof of the finite-field statement.

The polynomial symbol \(X,Y\) is auxiliary and commutative; it encodes the degree-three and degree-four coordinates, not an additional algebra operation. A projective linear factor is a one-dimensional subspace of the degree-one binary-form space; repeated factors count once. The source-pair count is over all \(q^{16}\) ordered pairs, without quotienting by automorphisms.

## Proof

Write
\[
r=\alpha x+\beta y+\gamma z+\delta u+\epsilon v+r_4,\qquad
s=\alpha' x+\beta' y+\gamma' z+\delta' u+\epsilon' v+s_4,
\]
with arbitrary central \(r_4,s_4\) (six independent field coordinates). Set the binary linear forms \(f=\alpha X+\beta Y\), \(g=\alpha'X+\beta'Y\), \(d=\delta X+\epsilon Y\), \(e=\delta'X+\epsilon'Y\). The Hall brackets and Jacobi identity give exactly
\[
[w,U,V]=[\det(f,g),\ f\gamma'-g\gamma,\ fe-gd],
\]
where the middle two entries are respectively a linear and a quadratic binary form. Explicitly, the three degree-four coordinates are \(\alpha\delta'-\alpha'\delta\), \(\alpha\epsilon'+\beta\delta'-\alpha'\epsilon-\beta'\delta\), and \(\beta\epsilon'-\beta'\epsilon\). This establishes the coordinate normalizations even in characteristic two.

If \(w\neq0\), the ordered pair \((f,g)\) has prescribed nonzero determinant and has \(|\mathrm{SL}_2(K)|=q(q^2-1)\) possibilities. For each, the linear map \((\gamma,\gamma')\mapsto U\) is bijective, while \((d,e)\mapsto V\) is surjective with a one-dimensional kernel: the products \(fX,fY,gX,gY\) span the three-dimensional binary-quadratic space. Thus each prescribed \((U,V)\) has \(q\) lifts in \((d,e)\), and the central coordinates contribute \(q^6\). Multiplication gives \(q(q^2-1)q q^6=q^8(q^2-1)\).

Suppose \(w=0\) and \((f,g)\neq(0,0)\). Such a dependent pair is uniquely \((f,g)=(s\ell,t\ell)\) for one projective line \([\ell]\) and a nonzero ordered scalar pair \((s,t)\); there are \(q^2-1\) choices of the latter per line. Both \(U=(s\gamma'-t\gamma)\ell\) and \(V=(se-td)\ell\) are divisible by \(\ell\). Conversely, for each common projective factor \(\ell\), the prescribed \(U\) has exactly \(q\) preimages \((\gamma,\gamma')\) and the prescribed \(V\) exactly \(q^2\) preimages \((d,e)\), because multiplication by a fixed nonzero form \(\ell\) is injective on linear forms. The six central coordinates give \(q^6\). Thus each common factor contributes \((q^2-1)q^{1+2+6}=q^9(q^2-1)\) source pairs. If \(f=g=0\), the bracket is zero irrespective of the other twelve source coordinates, contributing \(q^{12}\) only to \(T=0\). This proves every fiber formula.

For the image cardinality, targets with \(w\neq0\) contribute \((q-1)q^5\). With \(w=0,U\neq0\), the line \([U]\) is forced and \(V\) ranges over its \(q^2\)-element multiple subspace, contributing \((q^2-1)q^2\). With \(w=U=0,V\neq0\), attainable \(V\) are precisely the nonzero split or square binary quadratics, represented by unordered pairs with repetition of the \(q+1\) projective linear factors, times \(q-1\) nonzero scalars: \((q-1)(q+1)(q+2)/2\). Include the zero target. Finally any \(T\) with \(w=0\) is the sum of two brackets with respective nonzero \(z\)-coordinates \(1\) and \(-1\), because the nonzero-\(w\) case admits all other coordinates. There exist excluded single brackets (take nonzero \(U\) and \(V\) not divisible by it), so the exact width is two. Taking the zero fiber and dividing by \(q^{16}\) proves the commuting probability.

## Verification

The accompanying script `verification/bracket_fibers.py` enumerates all \(2^{16}=65536\) ordered pairs over \(\mathbb F_2\) and checks all 64 target fibers, including the absent ones. For \(\mathbb F_3\) it independently computes the rank and consistency of the map \(s\mapsto[r,s]\) for each of 6,561 possible first arguments and verifies the formula for 20 prescribed targets, including attainable and unattainable cases. Recorded output is `verification/bracket_fibers_output.txt`. Finite experiments corroborate the all-field proof but are not substitutes for it.

## Relationship to prior work

Benito and de-la-Concepción (2013), especially their section on free nilpotent algebras of type two, provides the rank-two graded class-four context and Hall commutator structure; its subject is extensions and derivations of complex Lie algebras, not these finite-field prescribed-target fibers. Del Barco (2011) studies symplectic structures of free nilpotent Lie algebras, not the finite-field bracket counting problem. A separate exact adjoint-rank/centralizer census on one-dimensional central quotients of this same eight-dimensional free algebra may imply the **zero-target** count, which is therefore not asserted as a new standalone invariant. The claim assessed here is the full prescribed nonzero-target law, its common-factor obstruction and image/width consequences.

## Limitations

The statement is for the free rank-two class-four algebra, not its arbitrary central quotients or arbitrary higher-class free Lie algebras. The literature search cannot establish historical uniqueness; a previously published equivalent commutator-map enumeration, particularly in older Lie-algebra or word-map literature, could subsume this theorem. A related public central-quotient study could not be inspected in full, and its exact nonzero-fiber coverage remains a residual comparison risk. No independent external mathematical review has been performed.

## References

- P. Benito and D. de-la-Concepción, *A note on extensions of nilpotent Lie algebras of type 2*, arXiv:1307.8419v1, first public 2013-07-31, https://arxiv.org/html/1307.8419v1.
- V. del Barco, *Symplectic Structures on Free Nilpotent Lie algebras*, arXiv:1111.3280v1, first public 2011-11-14, https://arxiv.org/html/1111.3280v1.
