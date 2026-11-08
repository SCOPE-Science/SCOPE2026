# Embedded nilpotent layers in commuting square-zero Heisenberg centralizer schemes

## Finding

Let \(k\) be an arbitrary field, \(m\ge1\), and let \(e=E_{12}\in M_3(k)\). The nilpotent elements of the matrix centralizer of \(e\) form the linear three-space
\[
H=\{Z(a,b,c)=aE_{12}+bE_{13}+cE_{32}:a,b,c\in k\}.
\]
This is also a nilpotent associative algebra with \(E_{13}E_{32}=E_{12}\) and all other products of basis matrix units equal to zero. Define the **equation scheme** \(\mathscr S_m\subset H^m\) by the matrix-entry equations \(Z_i^2=0\) and \(Z_iZ_j=Z_jZ_i\) for all \(i,j\). We do **not** replace the defining ideal by its radical.

The scheme admits a characteristic-free decomposition
\[
\mathscr S_m\simeq \mathbb A^m\times\operatorname{Spec}R_m,
\qquad R_m=\frac{k[b_1,\ldots,b_m,c_1,\ldots,c_m]}{(b_ic_i,\ b_ic_j-b_jc_i\ (i<j))}.
\]
Write \(N_m=\sqrt{0}\subset R_m\). Its entire graded vector-space structure and the dimensions of all its powers are
\[
\dim_k(N_m)_d=\begin{cases}(d-1)\binom md,&2\le d\le m,\\0,&\text{otherwise},\end{cases}
\qquad \dim_kN_m^s=\sum_{d=2s}^{m}(d-2s+1)\binom md\quad(s\ge1).
\]
Consequently
\[
\dim_kN_m=(m-2)2^{m-1}+1,
\qquad N_m^{\lfloor m/2\rfloor+1}=0,
\qquad N_m^{\lfloor m/2\rfloor}\ne0\text{ when }m\ge2.
\]
At \(m=1\) the length expression equals zero, and \(N_1=0\). The full nilradical is \(k[a_1,\ldots,a_m]\otimes_k N_m\), free of that stated rank over the central parameter space. For \(m\ge2\), the central \(m\)-plane is an **embedded associated component**. The underlying reduced scheme is a union of two affine \(2m\)-spaces meeting on that central plane, and the nonreduced structure first appears for \(m=2\). The reduced geometry alone does not determine these embedded nilpotent layers.

The complete Hilbert series in the \(b,c\) grading is
\[
H_{R_m}(t)=\frac{2}{(1-t)^m}-1+\sum_{d=2}^m(d-1)\binom md t^d.
\]
The Hilbert series of \(\mathscr S_m\), grading all \(a,b,c\) coordinates by degree one, is \(H_{R_m}(t)/(1-t)^m\).

## Assumptions and scope

The base \(k\) is any field, with no characteristic restriction, and \(m\) is any positive integer. Only the nilpotent linear subspace \(H\) of the centralizer of a *fixed* rank-one nilpotent \(e\) is used. The result does not assert this precise scheme structure for the unconstrained full-matrix commuting-square-zero scheme or for the scheme of all matrices in the centralizer before imposing nilpotence. The word “length” refers to the finite-dimensional transverse nilradical \(N_m\), not the positive-dimensional support over the free \(a\)-coordinates.

## Proof

**1. Centralizer coordinates and defining equations.** A matrix commutes with \(E_{12}\) exactly when it has shape
\[
\begin{pmatrix}\lambda&a&b\\0&\lambda&0\\0&c&\mu\end{pmatrix}.
\]
It is nilpotent exactly when \(\lambda=\mu=0\), over every field. This proves the displayed form for \(H\). Direct multiplication yields
\[
Z_iZ_j=b_ic_j E_{12},\qquad Z_i^2=b_ic_iE_{12},\qquad [Z_i,Z_j]=(b_ic_j-b_jc_i)E_{12}.
\]
No other matrix-entry equations survive, so the coordinate ring is exactly \(k[a_1,\ldots,a_m]\otimes R_m\), not only set-theoretically isomorphic to it.

**2. A normal-form basis.** Work in \(R_m\). A monomial involving both some \(b\) and some \(c\) vanishes whenever an index is repeated anywhere in it. If an index appears in both types, it contains \(b_ic_i\). If it appears twice as \(b_i\) and another \(c_j\) occurs, use \(b_ic_j=b_jc_i\) on one copy to obtain a factor \(b_ic_i\); the case of a repeated \(c_i\) is symmetric. Thus every surviving mixed monomial is squarefree in the combined index set. For a fixed squarefree support \(S\) of cardinality \(d\) and a fixed number \(u\) of \(b\)-letters, with \(1\le u\le d-1\), all \(b/c\) assignments of that support are equal: elementary swaps \(b_ic_j=b_jc_i\) connect every two assignments.

These relations do not mix the combined-index multidegree nor the number of \(b\)-letters. Each such mixed equivalence class is nonzero: the polynomial ideal is generated solely by monomial zero relations and differences of monomials, so its quotient has a basis indexed by equivalence classes avoiding the monomial zero relations. This gives **exactly one** basis vector for each triple \((S,u,d)\) with \(d=|S|\), \(2\le d\le m\), and \(1\le u\le d-1\), and yields \((d-1)\binom md\) independent mixed basis vectors in total degree \(d\). Pure \(b\)-monomials and pure \(c\)-monomials remain unrestricted, with shared constant. Their Hilbert series contributes \(2/(1-t)^m-1\), proving the full Hilbert-series formula.

**3. The nilradical and its support.** Let \(J=(b_ic_j:1\le i,j\le m)\) in the ambient polynomial ring, so \(J/I\subset R_m\) is the span of all mixed classes. The quotient by this ideal is the reduced ring \(k[b,c]/J\), the fiber product of two polynomial rings over \(k\). Every mixed class has degree at most \(m\), hence the mixed ideal is nilpotent and equals the nilradical \(N_m\). Since its homogeneous pieces vanish above degree \(m\), this is a finite-length module supported at \((b_1,\ldots,b_m,c_1,\ldots,c_m)\). Summing degrees gives
\[
\sum_{d=2}^m(d-1)\binom md=m2^{m-1}-(2^m-1)=(m-2)2^{m-1}+1.
\]
At \(m=1\) the sum is empty and the right side equals zero.

**4. Every nilpotent power.** A product of \(s\) mixed classes is nonzero exactly when their index supports are disjoint. A squarefree mixed class of degree \(d\), with \(u\) \(b\)-letters and \(d-u\) \(c\)-letters, belongs to \(N_m^s\) precisely when \(u\ge s\) and \(d-u\ge s\). Necessity follows from each of the \(s\) factors having both types; sufficiency follows by splitting off \(s\) disjoint \(b/c\) pairs and distributing remaining letters. Thus for every support of size \(d\), the available \(u\)'s number \(d-2s+1\), provided \(d\ge2s\). This proves the power-dimension formula. The highest nonzero power is \(s=\lfloor m/2\rfloor\) when \(m\ge2\), giving the asserted nilpotency index.

**5. Minimal and embedded components.** The two minimal primes of \(R_m\) are the images of \((b_1,\ldots,b_m)\) and \((c_1,\ldots,c_m)\). Hence the reduced variety consists of two affine \(m\)-spaces meeting at the origin in \(\operatorname{Spec}R_m\), and after restoring the \(a\)-parameters, two affine \(2m\)-spaces meeting along \(\mathbb A^m\). For \(m\ge2\), a degree-\(m\) mixed class with \(b\)-count one is nonzero but annihilated by every \(b_i,c_i\). Its annihilator is the maximal homogeneous ideal, which is therefore an embedded associated prime. No other embedded primes occur because the nilradical is supported only at that maximal ideal; away from it the scheme is reduced and the two remaining branches are smooth. Tensoring with \(k[a_1,\ldots,a_m]\) preserves all these conclusions. \(\square\)

## Verification

Two standalone standard-library Python programs are provided. `verify_heisenberg_nilradical.py` independently constructs the quotient by monomial-zero and binomial-swap relations using equivalence classes of actual monomials (not the claimed closed formulas) and checks every graded dimension through degree \(m+2\) for \(1\le m\le5\). It also checks the finite nilradical length. `verify_transverse_slice.py` constructs and multiplies the actual \(3\times3\) matrices in prime characteristics \(2,3,5\), checking square-zero, commutation and the reduced union in multiple tuple lengths. Recorded outputs are included. These finite checks are not proofs of all-degree or all-characteristic assertions; the preceding algebraic argument supplies those proofs.

## Relationship to prior work

Levy, *Varieties of Modules for Z/2Z x Z/2Z* (first preprint September 6, 2006), considers characteristic-two restricted nilpotent commuting varieties and centralizers, with the focus on equidimensionality and irreducible components. Ngo, *Commuting varieties of r-tuples over Lie algebras* (first preprint September 7, 2012), explicitly obtains a **reduced**, two-branch description of the commuting tuples over the subregular orbit closure in \(\mathfrak{sl}_3\); the present two-branch reduced support follows that framework and is **not** claimed as new. The added statement computes the **equation ideal's nilradical as a module**, including its graded Hilbert series, exponentially growing transverse length, every nilradical-power dimension, and an embedded associated prime. None of those statements follows from a set-theoretic decomposition alone. Jelisiejew--Šivic, *Components and singularities of Quot schemes and varieties of commuting matrices* (2021 preprint), investigates broader unrestricted commuting-matrix moduli, and its introduction and main component theorem do not supply these scheme-theoretic restricted-centralizer invariants.

## Limitations

The result is only for the nilpotent centralizer \(H\) of a fixed \(3\times3\) rank-one nilpotent matrix, not arbitrary nilpotent centralizers, matrix sizes or the full original commuting-square-zero scheme. The closed Hilbert-series formula depends on this precise three-dimensional nilpotent associative algebra. Literature priority, particularly possible implications from unlocated work on nonreduced commuting schemes, remains subject to independent verification. No independent audit was performed.

## References

1. P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180, first public September 6, 2006, https://arxiv.org/abs/math/0609180.
2. N. V. Ngo, *Commuting varieties of r-tuples over Lie algebras*, arXiv:1209.1659, first public September 7, 2012, https://arxiv.org/abs/1209.1659, especially Section 7.2 and Lemma 7.2.2.
3. J. Jelisiejew and K. Šivic, *Components and singularities of Quot schemes and varieties of commuting matrices*, arXiv:2106.13137, first public June 24, 2021, https://arxiv.org/abs/2106.13137.
