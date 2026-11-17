# Integral cohomology ring of two-plane odd biisotropic Grassmannians

## Finding
For every integer \(n\geq2\), let \(X_n=\operatorname{S_2Gr}(2,2n+1)\) be the variety of two-dimensional subspaces simultaneously isotropic for a general pencil of alternating forms on \(\mathbb C^{2n+1}\). Put
\[
A_n=\mathbb Z[a,b]/(s_{2n},s_{2n+1}),\qquad
s_0=1,\quad s_1=a,\quad s_j=a s_{j-1}-b s_{j-2}\quad(j\ge2),
\]
where \(a\) has cohomological degree two and \(b\) degree four. Define the **explicit annihilator ideal**
\[
J_n=\{f\in A_n: a^2 f=0\text{ in }A_n\}.
\]
Then restriction of the tautological Chern classes induces an **integral graded-ring isomorphism**
\[
\boxed{H^*(X_n,\mathbb Z)\ \cong\ A_n/J_n.}
\]
The right-hand side is computable from a finite two-generator polynomial presentation using ordinary Grassmannian Schubert multiplication. No rationalization or torsion quotient is involved.

More explicitly, put \(m=2n-2\) and let \(\sigma_{(m-i,i)}\), \(0\le i<n\), be the Schubert classes on \(\operatorname{Gr}(2,2n+1)\). Their restrictions form an integral basis of the middle cohomology \(H^{4n-4}(X_n,\mathbb Z)\), with intersection matrix
\[
\boxed{B_n=\begin{pmatrix}
2&1&0&\cdots&0\\
1&2&1&\ddots&\vdots\\
0&1&\ddots&\ddots&0\\
\vdots&\ddots&\ddots&2&1\\
0&\cdots&0&1&1
\end{pmatrix},\qquad\det B_n=1.}
\]
For \(n=2\), this means \(B_2=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\).
The top power of the primitive Plücker class is
\[
\int_{X_n}a^{4n-4}=\frac{1}{2n}\binom{4n-2}{2n-1},
\]
which differs from the Plücker degree \(\frac1{2n-1}\binom{4n-4}{2n-2}\) of \(\operatorname{Gr}(2,2n)\). Thus their graded integral cohomology rings are not isomorphic, despite having isomorphic graded cohomology groups.

## Assumptions and scope
All varieties are smooth complex projective varieties. The two alternating forms span a **general** pencil; smoothness of \(X_n\), its dimension \(4n-4\), cellularity, and the additive cohomology identity with \(\operatorname{Gr}(2,2n)\) are established in Fonarev--Kuznetsov, arXiv:2610.03309, Theorem 1.1 and Section 2. For \(k=2\), each isotropy condition is a Plücker hyperplane, so \(X_n\) is a smooth codimension-two linear section of \(G_n=\operatorname{Gr}(2,2n+1)\).

The symbols \(a=c_1(\mathcal U^*)\) and \(b=c_2(\mathcal U^*)\) denote restrictions from the tautological rank-two bundle \(\mathcal U\) on \(G_n\). The \(s_j\) are complete symmetric polynomials in its two formal Chern roots. The ring \(A_n\) is the standard integral Schubert presentation of \(H^*(G_n,\mathbb Z)\). Its annihilator \(J_n\) is taken **inside that explicitly presented ring**, not inside the unknown cohomology of \(X_n\).

## Proof
Set \(M=2n-1\), \(d=2M-2=4n-4\) and \(m=M-1\), so \(\dim_{\mathbb C}(G_n)=2M\) and \(\dim_{\mathbb C}(X_n)=d\). Write \(i:X_n\hookrightarrow G_n\). Two Plücker hyperplanes cut out \(X_n\) transversely; therefore \(i_*[X_n]=a^2\cap[G_n]\), and for classes of complementary degree
\[
\int_{X_n} i^*v\,i^*w=\int_{G_n}v w a^2.
\]

**Below the middle degree.** The integral weak Lefschetz hyperplane theorem applied twice gives an isomorphism \(i^*:H^{2j}(G_n,\mathbb Z)\to H^{2j}(X_n,\mathbb Z)\) for \(j<m\). Both groups are torsion-free, and odd groups on \(X_n\) vanish by its cellular decomposition. The additive theorem identifies the rank in codimension \(j\) with the number of partitions of \(j\) in a two-row rectangle of width \(M-1\).

**At the middle.** The classes \(\sigma_{(m-i,i)}\), \(0\le i<n\), form a basis of \(H^{2m}(G_n,\mathbb Z)\) and their images are independent. The Schubert dual of \(\sigma_{(u,v)}\) in the rectangle of width \(M\) is \(\sigma_{(M-v,M-u)}\). Since \(a^2=\sigma_{(2)}+\sigma_{(1,1)}\), the horizontal- and vertical-strip Pieri rules yield precisely the matrix \(B_n\) displayed above: adjacent entries equal one, diagonal entries equal two except the last, which equals one, and other entries vanish. Expanding the determinant successively from the first row, or using the continuant recurrence with terminal diagonal one, gives \(\det B_n=1\). The additive theorem says the middle cohomology of \(X_n\) has rank \(n\). Poincaré duality makes its full middle integral intersection lattice unimodular; hence a rank-\(n\) sublattice whose pairing has determinant one must have index one. Therefore the restricted Schubert classes form its integral basis.

**Above the middle.** Fix a codimension \(j>m\), and put \(r=d-j<m\) and \(s=\lfloor r/2\rfloor\). The classes \(\beta_c=\sigma_{(r-c,c)}\), \(0\le c\le s\), restrict to an integral basis in codimension \(r\). Consider in codimension \(j\) the valid ambient Schubert classes
\[
\alpha_t=\sigma_{(M-t,\,M-2-r+t)},\qquad 0\le t\le s.
\]
Their Poincaré-dual partitions in \(G_n\) are \((r+2-t,t)\). In the Pieri expansion of \(\beta_c a^2\), the coefficient of \(\sigma_{(r+2-t,t)}\) vanishes for \(t<c\), while it is exactly one for \(t=c\) (two boxes added to the first row). Thus the integral matrix \((\int_{X_n}i^*\alpha_t\,i^*\beta_c)_{0\le t,c\le s}\) is lower triangular with diagonal entries one. Poincaré duality implies that \(i^*\alpha_t\) form an integral basis in codimension \(j\). This proves **surjectivity of the restriction map in every cohomological degree**.

**Kernel and ring.** If \(v\in H^*(G_n,\mathbb Z)\) restricts to zero, the projection formula gives \(v a^2=0\) by Poincaré duality on \(G_n\). Conversely, if \(v a^2=0\), then \(i^*v\) pairs to zero with all restricted classes; surjectivity and Poincaré duality on \(X_n\) force \(i^*v=0\). Thus \(\ker i^*=\operatorname{Ann}_{A_n}(a^2)=J_n\), proving the ring presentation.

Finally, \(a\) generates \(H^2(X_n,\mathbb Z)\) by integral weak Lefschetz. As \(X_n\) is a codimension-two Plücker linear section, its Plücker degree is that of \(\operatorname{Gr}(2,2n+1)\), namely the Catalan number \(\frac{1}{2n}\binom{4n-2}{2n-1}\). The ordinary Grassmannian \(\operatorname{Gr}(2,2n)\) has the smaller Catalan Plücker degree \(\frac{1}{2n-1}\binom{4n-4}{2n-2}\). Any isomorphism of graded rings would carry the primitive generator of degree two to its positive or negative and preserve the absolute top intersection, which is impossible.

## Verification
The included standalone `verify.py` independently multiplies two-variable Schur polynomials with \((x+y)^2\), extracts the top integration coefficient for \(\operatorname{Gr}(2,2n+1)\), evaluates the middle pairing, and verifies the lower-triangular unit-diagonal pairings in every upper codimension for \(2\le n\le12\). All integers are exact; a fraction-free determinant algorithm checks the determinant. It prints `ALL_EXACT_SCHUR_PAIRING_CHECKS_OK` upon success. This finite calculation is a consistency test of the all-\(n\) symbolic Pieri proof, not a replacement for that proof.

To run: `python3 verify.py` (standard library only). No input files are needed.

## Relationship to prior work
Fonarev and Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (first submitted 2026-10-02), prove a uniform **graded-group** isomorphism with ordinary Grassmannian cohomology. Their Remark 1.2 explicitly separates the ring-structure question, which this result answers for \(k=2\) and every \(n\ge2\). The ambient integral Schubert presentation, weak Lefschetz theorem and Pieri rules are classical inputs and are not claimed as new. The special two-plane case is a codimension-two Plücker linear section; the new integral step is the unimodularity computation in the middle and in every higher degree, giving a surjective restriction and explicit kernel. General Schubert-calculus results and specialized work on linear sections may contain related statements; no identical all-parameter ring presentation was located in the sources checked.

## Limitations
This result covers only the two-plane case \(k=2\) for general pencils of skew forms over \(\mathbb C\); it does **not** determine the rings for \(k\ge3\), equivariant or quantum cohomology, integral cohomology in other characteristics, or special/singular pencils. It gives an annihilator presentation which is finite and algorithmic but does not assert a minimal two-relation presentation of \(J_n\). Priority against all older literature on linear sections has not been independently certified.

## References
- A. Fonarev and A. Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (submitted 2026-10-02), especially Theorem 1.1 and Remark 1.2, https://arxiv.org/html/2610.03309v1 .
- W. Fulton, *Young Tableaux*, Cambridge University Press (1997), classical Schubert basis, Giambelli and Pieri formulas.
- S. L. Kleiman, *The transversality of a general translate*, Compositio Math. 28 (1974), background on transversality of general intersections; smoothness for the present variety is taken from the motivating source.
