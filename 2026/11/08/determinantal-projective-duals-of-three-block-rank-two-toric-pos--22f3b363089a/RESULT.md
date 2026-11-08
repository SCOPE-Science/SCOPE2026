# Determinantal projective duals of three-block rank-two toric positroids

## Finding

For integers \(2\le a\le b\), let \(A,B,C\) be three consecutive nonempty parallel classes of sizes \(a,b,1\). Let \(X_{a,b}\) be the corresponding rank-two positroid variety in its Plücker linear span \(\mathbb P^{ab+a+b-1}_{\mathbb C}\). Rescale the signs of the Plücker coordinates so that its dense torus is parametrized by
\[
[u_1v_1:\cdots:u_av_b:u_1w:\cdots:u_aw:v_1w:\cdots:v_bw],
\qquad u_iv_jw\ne0.
\]
Write a hyperplane in the coefficient coordinates as a triple \((M,\alpha,\beta)\), where \(M\) is an \(a\times b\) matrix, \(\alpha\) is a column of length \(a\), and \(\beta\) is a column of length \(b\). Form the \((a+1)\times(b+1)\) augmented matrix
\[
T(M,\alpha,\beta)=\begin{pmatrix}M&\alpha\\\beta^{\mathsf T}&0\end{pmatrix}.
\]
The **reduced projective dual** is exactly the irreducible determinantal variety
\[
X_{a,b}^{\vee}=\{[M:\alpha:\beta]:\operatorname{rank}T(M,\alpha,\beta)\le a\}.
\]
Its codimension in the dual projective space is \(b-a+1\), its degree is \(\binom{b+1}{a}\), and its projective dual defect is \(b-a\). The contact locus in the dense torus of a general tangent hyperplane has closure a projective linear space \(\mathbb P^{b-a}\). Consequently, the dual is a hypersurface if and only if \(a=b=m\); in that case its irreducible equation is
\[
\det\begin{pmatrix}M&\alpha\\\beta^{\mathsf T}&0\end{pmatrix}
=-\alpha^{\mathsf T}\operatorname{adj}(M)^{\mathsf T}\beta=0,
\]
of degree \(m+1\).

## Assumptions and scope

The ground field is \(\mathbb C\), and all ranks and projective duals are taken over this field. Both non-singleton parallel classes have at least two elements, and \(2\le a\le b\) fixes their order; exchanging the classes treats the opposite order. The dual is formed in the Plücker **linear span** consisting of coordinates indexed by bases; its ambient dimension is \(ab+a+b-1\), not the larger full Plücker ambient space. The asserted equality is equality of reduced closed subvarieties, not a claim about equality of scheme structures of different ideal presentations.

The rank-two matroid with these three parallel classes is represented by three distinct real directions in the plane, with signs chosen to give all nonzero maximal minors positive. It is regular: its simplification is the three-point rank-two matroid, which is graphic, and parallel extensions preserve regularity. By the standard definition of positroid variety, its nonzero Plücker coordinates on the dense stratum are precisely the pairwise cross-products above. The parametrization is injective on that torus, since any nonzero \(u_i/w\) and \(v_j/w\) are recovered as quotients of cross-product coordinates.

## Proof

**1. Tangency equations.** The coefficient triple gives the quadratic pullback
\[
F(u,v,w)=u^{\mathsf T}Mv+w\alpha^{\mathsf T}u+w\beta^{\mathsf T}v.
\]
On the dense smooth torus of \(X_{a,b}\), a hyperplane is tangent exactly when the differential of \(F\) vanishes at some projective representative with every parameter nonzero. Because \(F\) is homogeneous quadratic and the torus map is an immersion, this is equivalent to
\[
Mv+w\alpha=0,\qquad M^{\mathsf T}u+w\beta=0,\qquad
\alpha^{\mathsf T}u+\beta^{\mathsf T}v=0.
\]

**2. Elimination on a dense coefficient open set.** Suppose \(\operatorname{rank}M=a\). If such tangency occurs, the second equation forces a unique \(\lambda\in\mathbb C^a\) satisfying \(\beta=M^{\mathsf T}\lambda\), and then \(u=-w\lambda\). The first equation says \(Mv=-w\alpha\). Substitution into the third gives \(-2w\lambda^{\mathsf T}\alpha=0\), hence \(\lambda^{\mathsf T}\alpha=0\), since \(w\ne0\) and the characteristic is zero. Conversely, for generic full-row-rank \(M\) with \(\beta=M^{\mathsf T}\lambda\), \(\lambda^{\mathsf T}\alpha=0\), and all \(\lambda_i\ne0\), the affine system \(Mv=-\alpha\) has solutions with all \(v_j\ne0\); taking \(w=1\) and \(u=-\lambda\) yields a smooth-torus tangency. These genericity requirements define a nonempty open set, as shown by explicit witnesses in the accompanying exact checker.

The same pair of constraints is equivalent to \(\operatorname{rank}T\le a\) when \(M\) has full row rank: the last row of \(T\) is a linear combination of its first \(a\) rows, with coefficients \(\lambda\), precisely when \(\beta=M^{\mathsf T}\lambda\) and \(\lambda^{\mathsf T}\alpha=0\).

**3. Irreducibility and boundary.** Let \(Y\) be the projective rank locus \(\{\operatorname{rank}T\le a\}\) in the hyperplane of the full matrix space where the southeast entry vanishes. Any matrix in the affine cone over \(Y\) has a factorization \(PQ\), where \(P\) has size \((a+1)\times a\) and \(Q\) has size \(a\times(b+1)\). The southeast-zero condition on \(PQ\) is the scalar equation \(\sum_{i=1}^{a} P_{a+1,i}Q_{i,b+1}=0\). For \(a\ge2\) this is an irreducible bilinear quadratic polynomial in independent variables, so its zero set is irreducible. The multiplication map \((P,Q)\mapsto PQ\) surjects onto the affine cone over \(Y\); therefore \(Y\) is irreducible. It contains points with \(\operatorname{rank}M=a\), and this stratum is dense. As the generic points of this stratum arise from genuine smooth-torus tangencies in step 2, the closure of tangent hyperplanes is all of \(Y\), with no extra boundary component.

**4. Dimension, degree, contact.** On the open set \(\operatorname{rank}M=a\), the coefficient locus is parametrized by \(M\), \(\lambda\), and \(\alpha\), with the one independent equation \(\lambda^{\mathsf T}\alpha=0\), and \(\beta=M^{\mathsf T}\lambda\). Its affine dimension is \(ab+2a-1\). The affine coefficient space has dimension \(ab+a+b\), giving codimension \(b-a+1\). The standard maximal-minor determinantal variety of \((a+1)\times(b+1)\) matrices of rank at most \(a\) has degree \(\binom{b+1}{a}\), for example by the top degeneracy-class computation \([H^{b-a+1}](1-H)^{-(a+1)}\). The fixed southeast-zero condition is a proper hyperplane section of that projective determinantal variety, so it preserves its degree. Thus \(\deg Y=\binom{b+1}{a}\). The dual defect is \(\operatorname{codim}Y-1=b-a\).

For general \(M,\alpha,\lambda\) on this locus, normalized \(w=1\), \(u=-\lambda\) is fixed, and the set of \(v\) solving \(Mv=-\alpha\) is a \((b-a)\)-dimensional affine translate of \(\ker M\). Its image under the Plücker parametrization is affine-linear in \(v\); its projective closure is a linear \(\mathbb P^{b-a}\). No greater general contact dimension is possible because the dual defect was calculated above.

**5. Balanced case.** If \(a=b=m\), the augmented matrix is square; the block determinant identity gives \(\det T=-\alpha^{\mathsf T}\operatorname{adj}(M)^{\mathsf T}\beta\). Irreducibility from step 3 shows that this degree-\((m+1)\) polynomial is the single reduced dual equation, not merely a factor of a quadratic-form discriminant.

## Verification

Run \(\texttt{python verify_dual.py}\) with Python 3 and SymPy. The supplementary exact script checks nonzero smooth-torus witnesses, every tangency equation, exact augmented-matrix rank and nullity, and the predicted defect and degree for six pairs \((a,b)\). It also checks the adjugate determinant identity for the balanced cases \(a=2,3\) and an extraneous-factor identity for the full quadratic Hessian at \(a=2\). All those tests pass. The script does not prove the general theorem; the parameter-independent steps above supply that proof.

## Relationship to prior work

McNeill, *There are no unexpected toric positroid varieties* (arXiv:2610.35914, first public 2026-10-07), classifies when a positroid variety is toric, not its projective duals. Gonzales–Le–Lowen (arXiv:2609.30257) provides a parallel toricity result as well as cohomological study. Furukawa–Ito (arXiv:1605.05801, §§1 and 6) develops general dual-defect theory for toric embeddings and does not give this three-block determinantal equation, its degree, and the full contact description in the inspected material. The maximal-minor degree and adjugate identities are classical tools and not claimed as new. Earlier results describing singular strata of three-parallel-class positroid varieties concern primal singularities, not their projective duals.

## Limitations

The statement concerns only three parallel classes with the third a singleton and \(a,b\ge2\), over \(\mathbb C\), in the Plücker linear span. It does not classify duals of arbitrary regular positroids, nor the singular scheme of the dual, nor the exceptional boundary contact loci. Literature priority remains provisional because an equivalent graph-theoretic \(A\)-discriminant presentation under another name may exist; independent mathematical review has not been performed.

## References

1. A. McNeill, *There are no unexpected toric positroid varieties*, arXiv:2610.35914 (2026), https://arxiv.org/abs/2610.35914.
2. T. Gonzales, T. Le and C. Lowen, *A quasisymmetric analog of Grassmannian Schubert varieties*, arXiv:2609.30257 (2026), https://arxiv.org/abs/2609.30257.
3. K. Furukawa and A. Ito, *A combinatorial description of dual defects of toric varieties*, arXiv:1605.05801, https://arxiv.org/abs/1605.05801.
4. S. Billey and J. Weaver, *A pattern avoidance characterization for smoothness of positroid varieties* (2022), https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/57.pdf.
