# Singular components and transverse nodes of the second-hypersimplex discriminant

## Finding
For every integer \(n\ge5\), put \(N=\binom n2\). Let \(M=(m_{ij})_{1\le i,j\le n}\) be the symmetric matrix with \(m_{ii}=0\) and independent off-diagonal projective coordinates \(m_{ij}=m_{ji}=x_{ij}\) for \(i<j\). Let \(H_n=V(\det M)\subset\mathbb P^{N-1}_{\mathbb C}\), the \(A\)-discriminant of the second hypersimplex.

Define \(D_n=\{[M]:\operatorname{rank}M\le n-2\}\) and \(L_i=\{[M]:m_{ij}=0\text{ for all }j\ne i\}\). Then the **entire reduced singular locus** is
\[
\operatorname{Sing}(H_n)_{\mathrm{red}}=D_n\cup\bigcup_{i=1}^{n}L_i.
\]
These are exactly its \(n+1\) irreducible components. The determinantal component \(D_n\) has dimension \(N-4\) and ambient projective codimension \(3\). Each \(L_i\) is a linear \(\mathbb P^{N-n}\), of ambient codimension \(n-1\). The hypersurface \(H_n\) is irreducible and normal.

At every closed point in a nonempty Zariski-open subset of \(D_n\), the complete local ring is
\[
\mathbb C[[s_1,\ldots,s_{N-4},a,b,c]]/(ac-b^2).
\]
At every closed point in the open subset of \(L_i\) where the remaining \((n-1)\)-by-\((n-1)\) principal block is invertible, it is
\[
\mathbb C[[t_1,\ldots,t_{N-n},z_1,\ldots,z_{n-1}]]/\left(\sum_{j=1}^{n-1}z_j^2\right).
\]
In particular, all these generic transverse singularities are nondegenerate ordinary quadratic cones with Hilbert–Samuel multiplicity \(2\), but the two component types have different transverse dimensions.

## Assumptions and scope
Everything is over \(\mathbb C\), with \(n\ge5\). Only the *reduced* singular support and completed local rings on specified dense open strata are asserted; no global radicality of the Jacobian ideal is claimed. Local product statements concern closed complex points and completed local rings. The exceptional \(n=4\) hypersurface is not included: its corank-two locus splits into multiple components.

## Proof
**Jacobian and support.** The derivative with respect to the off-diagonal coordinate \(x_{ij}\), \(i<j\), is \(2\operatorname{adj}(M)_{ij}\), since the variable occurs in both symmetric positions. If \(\operatorname{rank}M\le n-2\), the entire adjugate vanishes. For a matrix of rank \(n-1\), its symmetric adjugate has rank one and is \(\lambda uu^{\mathsf T}\), where \(\lambda\ne0\) and \(u\) spans the kernel. All off-diagonal derivatives vanish if and only if \(u_i u_j=0\) for every \(i\ne j\), which means \(u\) is proportional to a coordinate vector. Equivalently, an entire row and column of \(M\) vanish. The projective Jacobian criterion therefore gives exactly the displayed set-theoretic equality of singular loci; the stated reduced equality follows.

**Irreducibility and dimension of the corank-two component.** Set \(r=n-2\ge3\). Every complex symmetric matrix of rank at most \(r\) can be factored as \(WW^{\mathsf T}\) with \(W\) having \(r\) columns (zero padding is allowed). The zero-diagonal condition says that every one of the \(n\) row vectors of \(W\) lies on the isotropic quadric \(Q_r=\{v\in\mathbb A^r:\sum_{k=1}^r v_k^2=0\}\). This quadric is irreducible of dimension \(r-1\) because \(r\ge3\). Hence \(D_n\)'s affine cone is the surjective Gram image of the irreducible variety \(Q_r^n\), and is irreducible. Full-column-rank matrices form a nonempty open subset. Two such Gram factorizations give the same symmetric matrix exactly when they differ by the right action of \(O(r,\mathbb C)\), whose dimension is \(r(r-1)/2\). Thus the affine dimension is \(n(r-1)-r(r-1)/2=N-3\), and \(\dim D_n=N-4\) after projectivization. Each \(L_i\) is plainly a projective linear subspace of dimension \(\binom{n-1}{2}-1=N-n\). It is not contained in \(D_n\): on \(L_i\) choose the remaining block to be the zero-diagonal all-ones-off-diagonal matrix, with determinant \((-1)^{n-2}(n-2)\ne0\), giving rank \(n-1\). The irreducible \(D_n\) is not contained in any \(L_i\), since general Gram products of nonzero isotropic vectors have no zero row. Therefore all \(n+1\) displayed components are distinct and exhaustive.

**Normality.** The displayed singular components all have ambient codimension at least \(3\), so the singular locus has ambient codimension at least \(3\). A reducible homogeneous determinant would have two hypersurface factors whose codimension-two intersection lies in its singular locus; a repeated factor would make an entire hypersurface singular. Both contradict the support calculation. Thus \(\det M\) is irreducible and reduced. As an irreducible hypersurface, \(H_n\) is Cohen–Macaulay and satisfies Serre's \(S_2\). Its singular locus has codimension at least \(2\) inside \(H_n\), so it satisfies \(R_1\). Serre's criterion gives normality.

**Normal form along \(L_i\).** Reorder indices and write \(M=\begin{pmatrix}0&v^{\mathsf T}\\v&B\end{pmatrix}\), where \(B\) is hollow symmetric of order \(n-1\). Over \(\det B\ne0\), the exact Schur-complement identity is
\[
\det M=-\det(B)\,v^{\mathsf T}B^{-1}v.
\]
At each closed point of \(L_i\) in this chart, the quadratic form in the \(n-1\) coordinates \(v\) is nondegenerate, and the coefficient \(\det B\) is a unit. Over the completed regular local ring of the smooth base, an invertible formal change of normal coordinates diagonalizes this quadratic form to \(\sum z_j^2\). The other \(N-n\) projective-chart parameters supply a smooth factor. This is an actual completed-local-ring isomorphism, not merely an identification of tangent cones.

**Normal form along \(D_n\).** Around a rank-\(r=n-2\) point with an invertible principal \(r\)-by-\(r\) minor, a symmetric block Schur complement writes the determinant as a unit times \(ac-b^2\), where \(\begin{pmatrix}a&b\\b&c\end{pmatrix}\) is the residual symmetric \(2\)-by-\(2\) block. To verify that \(a,b,c\) are independent local normal parameters at a nonempty open subset of \(D_n\), construct an explicit point. In \(\mathbb C^r\) take the independent isotropic vectors \(w_1=e_1+ie_2\), \(w_2=e_1-ie_2\), and \(w_j=e_1+ie_j\) for \(3\le j\le r\). Append \(w_{r+1}=w_1\) and \(w_{r+2}=w_3\), and set \(M_0=WW^{\mathsf T}\). The first \(r\) rows of \(W\) form an invertible matrix; hence \(M_0\) has rank \(r\) and an invertible leading principal \(r\)-minor. A basis of its kernel is \(u=e_{r+1}-e_1\), \(v=e_{r+2}-e_3\). The first-order map from symmetric zero-diagonal perturbations \(E\) to \((u^{\mathsf T}Eu,u^{\mathsf T}Ev,v^{\mathsf T}Ev)\) is surjective: perturbations of the three entries \(x_{1,r+1}\), \(x_{3,r+2}\), and \(x_{r+1,r+2}\) yield linearly independent triples. Thus the restricted Schur-complement map has differential of rank \(3\) at \(M_0\). Since \(D_n\) is irreducible, this rank condition defines a nonempty dense open subset. On that subset the formal implicit-function theorem makes the three Schur entries part of a regular parameter system, and \(\det M\) has the asserted ordinary quadratic normal form with \(N-4\) smooth parameters.

## Verification
The supplementary standalone checker `check_hollow.py` uses exact symbolic arithmetic and no external data. Run `python check_hollow.py` with Python 3 and SymPy. It verifies the derivative–cofactor identity for \(36\) fixed-seed specializations in matrix sizes \(5,6,7,8\); four exact Schur-complement identities; four full-rank isotropic Gram examples; and four independent conormal calculations. Expected recorded output is `check_output.txt`. These finite checks are consistency tests; the proofs of irreducibility, the component count, and the generic local descriptions work for every integer \(n\ge5\) by the arguments above.

## Relationship to prior work
Helmer–Sturmfels explicitly identify this determinant with the \(A\)-discriminant of the second hypersimplex; their calculation concerns polar degrees and Euclidean distance degrees, rather than the full singular-component and transverse-local classification. El Maazouz–Sturmfels–Sverrisdóttir establish that the hollow symmetric rank-bounded locus \(\operatorname{rank}\le r\) is irreducible for \(r\ge3\), a result consistent with and stronger than the irreducibility sublemma for \(D_n\). Their paper also classifies the special rank-two locus and treats singularities for a different block-hollow family. The four-by-four case has a distinct previously recorded eleven-component singular support. These facts are not claimed as new. The present claim concerns precisely the all-size \(n\ge5\) singular decomposition and generic transverse types. The complete historical literature may contain an equivalent specialization, so an independent novelty audit remains appropriate.

## Limitations
No scheme-theoretic primary decomposition or global radicality statement is asserted for the full Jacobian ideal, nor are special local germs at component intersections classified. Formal normal forms are proved on nonempty dense open subsets only. The formulas do not extend unchanged to \(n=4\) or to positive characteristic.

## References
1. M. Helmer and B. Sturmfels, *Nearest Points on Toric Varieties*, arXiv:1603.06544 (first posted 21 March 2016), especially equation (35) in §4. https://arxiv.org/abs/1603.06544
2. Y. El Maazouz, B. Sturmfels and S. Sverrisdóttir, *Gram Matrices for Isotropic Vectors*, arXiv:2411.08624 (2024), Example 2.2 and Theorem 2.5. https://arxiv.org/abs/2411.08624
3. J. Huang, *Determinantal Hypersurface from a Geometric Perspective*, California Institute of Technology dissertation (2013). https://thesis.caltech.edu/7656/
4. *Eleven singular surfaces on the smallest squared Grassmannian*, publicly indexed mathematical note (2026), concerning the distinct \(n=4\) case. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-eleven-singular-surfaces-on-the-smallest-squared-grassmannian--6ce60a96126e
