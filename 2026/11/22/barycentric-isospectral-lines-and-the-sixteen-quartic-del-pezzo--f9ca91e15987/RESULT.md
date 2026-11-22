# Barycentric isospectral lines and the sixteen quartic-del-Pezzo directions

## Finding

**Theorem.** Let \(n\geq5\), let \(d_1,\ldots,d_n\in\mathbb C\) be pairwise distinct, put \(D=\operatorname{diag}(d_1,\ldots,d_n)\), and define \(P(z)=\prod_{i=1}^{n}(z-d_i)\). For each choice of nonzero square roots
\[
 u_i^2=\frac{1}{P'(d_i)},\qquad 1\leq i\leq n,
\]
define a complex symmetric matrix \(Q(u)\) by
\[
 Q(u)_{ii}=0,\qquad Q(u)_{ij}=(d_i-d_j)^2u_i u_j\quad(i\ne j).
\]
Then the following assertions hold simultaneously.

1. For every \(t\in\mathbb C\), the characteristic polynomial of \(D+tQ(u)\) equals that of \(D\). In particular \(Q(u)\ne0\) is an isospectral symmetric affine-line direction for **every**, not merely generic, simple-spectrum \(D\).
2. The \(2^n\) root choices give exactly \(2^{n-1}\) distinct projective directions \([Q(u)]\); simultaneous reversal of all signs is the sole duplication.
3. Every \(Q(u)\) has rank exactly \(3\). For \(n=5\), it has nilpotency index \(3\), ranks \(\operatorname{rank} Q=3\) and \(\operatorname{rank}Q^2=1\), and Jordan partition \((3,2)\). For every \(n\geq6\), it is square-zero and has Jordan partition \((2,2,2,1^{n-6})\).
4. When \(n=5\), the associated surface
\[
 X_D=\left\{[z_1:\cdots:z_5]\in\mathbb P^4:\ \sum_i z_i^2=\sum_i d_i z_i^2=0\right\}
\]
is a smooth intersection of two quadrics. Its sixteen geometric lines are precisely \(\mathbb P(\operatorname{span}(u,Du))\) for the sixteen sign classes above. The naturally induced Plücker-commutator embedding from its line scheme takes these sixteen lines to the sixteen directions \([Q(u)]\).

Only the distinguished directions and their line-scheme origin are classified here. In dimensions \(n\geq6\), additional isospectral directions may exist; no classification of the entire isospectral cone is asserted. In dimension five, no claim that all nonzero symmetric isospectral directions come from lines of \(X_D\) is made.

## Assumptions and scope

All geometry is over \(\mathbb C\), with characteristic zero. The spectrum is simple: \(d_i\ne d_j\) whenever \(i\ne j\). Complex square roots are allowed; the chosen \(u_i\) are never zero. The projective direction \([Q]\) identifies two nonzero matrices differing by any nonzero scalar. The term *isospectral affine line* means equality of characteristic polynomials as polynomials in both the characteristic indeterminate and \(t\), not merely equality at finitely many values of \(t\). Rank and Jordan form refer to the complex matrix \(Q\), not to \(D+tQ\).

The construction is invariant under simultaneous permutation of the eigenvalues and their associated coordinates. No order or algebraic independence of the \(d_i\) is required.

## Proof

**Step 1: exact interpolation moments.** For the weights \(w_i=P'(d_i)^{-1}\), the leading coefficient in the Lagrange interpolation identity for a polynomial of degree at most \(n-1\) gives
\[
 s_k:=\sum_{i=1}^n w_i d_i^k=0\ (0\leq k\leq n-2),\qquad s_{n-1}=1.
\]
Indeed, the Lagrange basis polynomial \(P(z)/((z-d_i)P'(d_i))\) has leading coefficient \(w_i\); the degree-\(n-1\) coefficient of \(z^k\) is zero for \(k<n-1\) and one for \(k=n-1\). In particular \(s_0=s_1=s_2=s_3=0\) since \(n\geq5\), while \(s_4=1\) for \(n=5\) and \(s_4=0\) for \(n\geq6\).

**Step 2: an orthogonal unipotent conjugation.** Regard \(u=(u_i)\) and \(v=Du\) as column vectors; use ordinary transpose rather than conjugate transpose. The moments imply
\[
 u^{\mathsf T}u=u^{\mathsf T}v=v^{\mathsf T}v=0,
\quad
 u^{\mathsf T}Du=u^{\mathsf T}Dv=v^{\mathsf T}Dv=0.
\]
Set \(N=uv^{\mathsf T}-vu^{\mathsf T}\). Thus \(N^{\mathsf T}=-N\), \(N^2=0\), and \(NDN=0\). Consequently the polynomial orthogonal matrix \(g(t)=I+tN\) has inverse \(I-tN\) and obeys
\[
 g(t)Dg(t)^{-1}
 =D+t(ND-DN)-t^2NDN=D+tQ(u).
\]
For \(i\ne j\), \(N_{ij}=(d_j-d_i)u_i u_j\), so \((ND-DN)_{ij}=(d_j-d_i)^2u_i u_j\), with zero diagonal, exactly as claimed. Similarity for every \(t\) proves the entire characteristic-polynomial identity.

**Step 3: exact rank and nilpotency.** Write \(U=\operatorname{diag}(u_i)\), \(W=U^2=\operatorname{diag}(w_i)\), and \(B_{ij}=(d_i-d_j)^2\), including \(B_{ii}=0\). Then \(Q=UBU\) and
\[
 B=VCV^{\mathsf T},\quad
 V=\begin{pmatrix}1&d_1&d_1^2\\ \vdots&\vdots&\vdots\\1&d_n&d_n^2\end{pmatrix},\quad
 C=\begin{pmatrix}0&0&1\\0&-2&0\\1&0&0\end{pmatrix}.
\]
The Vandermonde matrix \(V\) has column rank three, \(C\) is invertible, and \(U\) is invertible; hence \(\operatorname{rank}Q=3\). Expanding \(BWB\) entrywise gives
\[
 (BWB)_{ij}=\sum_{k=1}^n w_k(d_i-d_k)^2(d_k-d_j)^2=s_4
\]
where all lower moments \(s_0,s_1,s_2,s_3\) vanish. Thus
\[
 Q^2=s_4\,u u^{\mathsf T}.
\]
Further, \(Qu=UB(Uu)=UB(w_i)_{i=1}^n=0\), because \(\sum_i w_i(d_j-d_i)^2=s_2-2d_j s_1+d_j^2s_0=0\). Therefore \(Q^3=0\) always. When \(n=5\), \(s_4=1\) makes \(Q^2=uu^{\mathsf T}\ne0\) of rank one. The rank sequence \((5,3,1,0)\) determines Jordan blocks of sizes \(3\) and \(2\). When \(n\geq6\), \(s_4=0\) implies \(Q^2=0\); rank three then forces exactly three size-two blocks and \(n-6\) size-one blocks.

**Step 4: count the projective directions.** The weight \(w_i\ne0\) has exactly two square roots. All off-diagonal entries \(Q_{ij}\) are nonzero. If two sign assignments \(u_i'=\epsilon_i u_i\), \(\epsilon_i\in\{\pm1\}\), give proportional matrices, \(Q(u')=cQ(u)\), then \(\epsilon_i\epsilon_j=c\) for every \(i\ne j\). Since \(n\geq5\), comparing a triangle of indices forces all signs to coincide, with \(c=1\). Hence the sole duplication is simultaneous sign reversal; there are exactly \(2^{n-1}\) distinct projective directions.

**Step 5: the dimension-five line scheme.** For \(n=5\), the vectors \(u,Du\) are independent: an eigenvector of a simple diagonal matrix has only one nonzero coordinate, whereas every \(u_i\ne0\). The six pairings in Step 2 show that the projective line \(\ell_u=\mathbb P(\operatorname{span}(u,Du))\) lies on both quadrics defining \(X_D\). The surface is smooth: a singular point of the complete intersection would have \((a+bd_i)z_i=0\) for all \(i\) with \((a,b)\ne(0,0)\), and therefore at most one nonzero coordinate; this contradicts \(\sum_i z_i^2=0\). It is thus a smooth degree-four del Pezzo surface, and the classical classification gives exactly sixteen geometric lines (five exceptional curves, ten pairwise-point lines, and one conic transform in the plane-blowup model).

Every line \(\ell=\mathbb P(\operatorname{span}(a,b))\subset X_D\) defines a skew Plücker matrix \(N_\ell=ab^{\mathsf T}-ba^{\mathsf T}\), unique up to scale. The coordinatewise linear transformation
\[
 (N_\ell)_{ij}\longmapsto([N_\ell,D])_{ij}=(d_j-d_i)(N_\ell)_{ij}\quad(i<j)
\]
is invertible because all \(d_i\) are distinct. It therefore gives a projective embedding of the line scheme via its usual Plücker embedding. By Steps 2 and 4, the sixteen \(\ell_u\) have distinct images. They exhaust all sixteen lines, and their images are exactly the sixteen \([Q(u)]\), as stated.

## Verification

The standalone reproducibility file `verify.py` uses only Python standard-library exact rational arithmetic and modular arithmetic. It checks Lagrange moments and the identities \(BWB=\mathbf1\mathbf1^{\mathsf T}\) for \(n=5\), \(BWB=0\) for \(n\geq6\), and \(BWBWB=0\) for two unequal sets of diagonal entries at each \(5\leq n\leq10\). For explicit finite-field examples at \(n=5,6,7\), it checks \(N^2=NDN=0\), four distinct polynomial conjugation parameters, the rank and square/cube ranks, and the complete sign orbit. All supplied tests pass. These finite checks do **not** prove the universal theorem; the interpolation, matrix identities, and classical del Pezzo classification in the proof do.

## Relationship to prior work

Asokan, *Isospectral Deformations of Diagonal Matrices by Symmetric Matrices in Dimension Four* (2026, arXiv:2611.07150v1), proves generic rigidity for \(n\leq4\) and notes that nontrivial isospectral directions exist generically for \(n\geq5\), reserving explicit constructions for later work. Its published theorem does not give the displayed all-spectrum barycentric formula, the precise \(2^{n-1}\) orbit, the rank-three Jordan-type threshold, or its relation to the sixteen lines of a quartic del Pezzo surface. The existence statement alone is not claimed as new.

Hassett and Tschinkel, *Equivariant Geometry of Odd-Dimensional Complete Intersections of Two Quadrics* (2022), Section 8.1, records the classical sixteen-line classification and coordinate sign action on a diagonal quartic del Pezzo surface. The line count and diagonal automorphism group are prior results, not claimed as new. The additional isospectral commutator interpretation and its all-size spectral formula are the specific contribution examined here.

Buium and Vasiu, *Delta-Invariant Theory for Hecke Correspondences* (2026), addresses invariant theory of tuples of quadratic forms, but only its public overview was accessible; its full relevant text was not compared. The author's 2026 dissertation *Invariant Theory of Triplets of Quadratic Forms* is bibliographically verified but was not available as an inspectable full text. Those priority uncertainties remain explicit.

## Limitations

The theorem is restricted to algebraically closed characteristic-zero fields, and to matrices with pairwise distinct eigenvalues. It constructs a canonical finite sign family, not the entire scheme of isospectral perturbations in any size. The sixteen lines in the dimension-five del Pezzo case are exhaustive as lines on the specified surface, not proved exhaustive among all isospectral directions. No claim is made about arithmetic descent of individual square-root choices to the field generated by the \(d_i\). Independent mathematical validation has not been performed. The unavailable dissertation and book chapters leave an unresolved, nondecisive publication-priority risk for equivalent constructions.

## References

1. Hari Asokan, *Isospectral Deformations of Diagonal Matrices by Symmetric Matrices in Dimension Four*, arXiv:2611.07150v1, first publicly submitted 2026-11-04. https://arxiv.org/abs/2611.07150
2. Brendan Hassett and Yuri Tschinkel, *Equivariant Geometry of Odd-Dimensional Complete Intersections of Two Quadrics*, preprint dated 2022-02-21, Section 8.1. https://www.math.brown.edu/bhassett/papers/Equivariant_geometry_two_quadrics/EGodd2Q.pdf
3. Hari Asokan, *Invariant Theory of Triplets of Quadratic Forms*, Ph.D. dissertation, Binghamton University, 2026; bibliographic record only. https://matrix-math.mathmig.binghamton.edu/d/mysql/create_theses
4. Alexandru Buium and Adrian Vasiu, *Delta-Invariant Theory for Hecke Correspondences*, Lecture Notes in Mathematics 2396, Springer, 2026, DOI:10.1007/978-3-032-20571-1. Full text not inspected.
