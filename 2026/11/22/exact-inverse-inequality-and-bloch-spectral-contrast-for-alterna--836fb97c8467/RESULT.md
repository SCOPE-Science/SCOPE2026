# Exact inverse inequality and Bloch spectral contrast for alternating periodic linear splines

## Finding
Let \(m\ge2\) be an integer and let \(a,b>0\). Subdivide the circle of circumference \(m(a+b)\) into \(2m\) intervals with lengths \(a,b,a,b,\ldots,a,b\). Denote by \(S_m(a,b)\) the real continuous periodic functions that are affine on each interval. For every \(s\in S_m(a,b)\),
\[
\boxed{\int |s'|^2\,dx\le\frac{12}{ab}\int |s|^2\,dx.}
\]
The constant is best possible at **every** finite \(m\), and equality for a nonzero \(s\) holds exactly when its successive nodal values alternate between \(c\) and \(-c\), for some nonzero real \(c\). Thus the optimal inverse-inequality constant is \(\sqrt{12/(ab)}\), not merely the generic minimum-cell estimate \(\sqrt{12}/\min(a,b)\).

The entire generalized eigenvalue spectrum of the derivative-energy form relative to the \(L^2\) form consists, with multiplicity, of the two nonnegative roots \(\lambda_\pm(\theta_j)\), at each \(\theta_j=2\pi j/m\) for \(j=0,\ldots,m-1\), of
\[
\left(\frac1a+\frac1b-\frac{a+b}{3}\lambda\right)^2
=\left(\frac1a+\frac a6\lambda\right)^2+
\left(\frac1b+\frac b6\lambda\right)^2
+2\left(\frac1a+\frac a6\lambda\right)
\left(\frac1b+\frac b6\lambda\right)\cos\theta_j.
\]
The lower branch increases and the upper branch decreases as \(\theta\) runs from \(0\) to \(\pi\). The two continuous Bloch bands (the union over \(0\le\theta\le\pi\)) are
\[
\left[0,\frac{12}{\max\{b(3a+b),\,a(a+3b)\}}\right]
\quad\text{and}\quad
\left[\frac{12}{\min\{b(3a+b),\,a(a+3b)\}},\frac{12}{ab}\right].
\]
Their intervening open gap has exact width
\[
\boxed{\Delta=\frac{12|a^2-b^2|}{ab(3a+b)(a+3b)}.}
\]
It is nonempty exactly when \(a\ne b\). For even \(m\), both inner band edges occur in the finite spectrum. If \(\delta=|a-b|/(a+b)\), its width normalized by the top eigenvalue obeys
\[
\boxed{\frac{\Delta}{12/(ab)}=\frac{\delta}{4-\delta^2},}
\]
a strictly increasing function of \(\delta\in[0,1)\). Hence the normalized spectral gap identifies the alternating mesh contrast up to exchange of \(a,b\).

## Assumptions and scope
All integrals use physical arclength on the circle; no normalization of total length is imposed. Periodicity identifies the last and first nodes. The \(L^2\) inner product and derivative seminorm are unweighted. The stated continuous Bloch bands are symbolic dispersion ranges; for finite \(m\), only the \(m\) listed Bloch phases occur. If \(m\) is odd, the inner band-edge phases \(\theta=\pi\) are absent from the discrete phase set. The result holds over complex scalars as well by inserting absolute-value squares, although the classification above specifies the real equality cases.

## Proof
Write the successive nodal values as \(u_0,\ldots,u_{2m-1}\), with cyclic indices, and let \(h_i=a\) for even \(i\), \(h_i=b\) for odd \(i\). Exact affine-element integration gives
\[
\int|s'|^2\,dx=\sum_i\frac{|u_{i+1}-u_i|^2}{h_i},\qquad
\int|s|^2\,dx=\sum_i\frac{h_i}{3}
\left(|u_i|^2+\operatorname{Re}(u_i\overline{u_{i+1}})+|u_{i+1}|^2\right).
\]
Because each node is adjacent to one \(a\)-interval and one \(b\)-interval, coefficient comparison yields the **exact positive sum-of-squares identity**
\[
\frac{12}{ab}\int|s|^2\,dx-\int|s'|^2\,dx
=\sum_i\left(\frac1{h_i}+\frac{2h_i}{ab}\right)|u_i+u_{i+1}|^2.
\]
Every weight is positive. Equality requires \(u_{i+1}=-u_i\) on all edges, which is consistent on the even cycle and proves the sharp inequality and all extremizers. In particular the top generalized eigenvalue is \(12/(ab)\); the constant vector has eigenvalue zero.

For the complete spectrum, arrange nodes as \((u_{2r},u_{2r+1})\), \(r\) modulo \(m\), and Fourier-transform across these two-node cells. For Bloch phase \(\theta\), the exact stiffness and mass blocks are
\[
K(\theta)=\begin{pmatrix}
\frac1a+\frac1b&-\frac1a-\frac{e^{-i\theta}}b\\
-\frac1a-\frac{e^{i\theta}}b&\frac1a+\frac1b
\end{pmatrix},\qquad
M(\theta)=\begin{pmatrix}
\frac{a+b}{3}&\frac{a+be^{-i\theta}}6\\
\frac{a+be^{i\theta}}6&\frac{a+b}{3}
\end{pmatrix}.
\]
Each mass block is positive definite: it is the Fourier compression of the strictly positive continuous spline mass form. The determinant equation \(\det(K(\theta)-\lambda M(\theta))=0\) gives precisely the displayed quadratic dispersion identity. At \(\theta=0\), it factors into roots \(0\) and \(12/(ab)\). At \(\theta=\pi\), the two eigenvectors \((1,1)\) and \((1,-1)\) give the unordered eigenvalues
\[
\frac{12}{b(3a+b)},\qquad\frac{12}{a(a+3b)}.
\]
To establish both band ranges rather than just their endpoints, let \(c=\cos\theta\). For any \(\lambda\ge0\) the determinant polynomial \(F(\lambda,c)\) has \(\partial F/\partial c=-2(1/a+a\lambda/6)(1/b+b\lambda/6)<0\). Its leading coefficient is \(\det M(\theta)>0\). At a pair of distinct generalized eigenvalues the derivative in \(\lambda\) is negative at the lower root and positive at the upper root, so implicit differentiation shows that the lower root strictly decreases and the upper root strictly increases with \(c\). Continuity extends this conclusion to the possible double-root endpoint \(a=b,\theta=\pi\). Thus the extrema occur at \(0\) and \(\pi\), proving the exact bands. Subtracting the two \(\pi\)-edge values gives the gap width. Since
\((3a+b)(a+3b)=(a+b)^2(4-\delta^2)\),
normalization yields the contrast formula. Its derivative \((4+\delta^2)/(4-\delta^2)^2\) is strictly positive, proving contrast identifiability.

## Verification
The accompanying `checker.py`, executable with Python 3 standard library only, exactly assembles mass and stiffness forms using rational arithmetic for many positive rational length pairs and finite cycle lengths; it tests the sum-of-squares identity, sharp extremizing eigenvector, and Bloch determinant and edge formulas. These finite checks are consistency tests, not a substitute for the preceding proof. The identities above directly determine all required infinite families and equality cases.

## Relationship to prior work
Takacs and Takacs, *Approximation error estimates and inverse inequalities for B-splines of maximum smoothness* (first arXiv posting 2015-02-12), prove general uniform-grid inverse estimates and in Remark 3 allow a nonuniform minimum-cell bound; that bound does not give this sharp alternating geometric-mean constant or the complete two-band spectrum. Dahmen, Faermann, Graham, Hackbusch and Sauter, *Inverse inequalities on non-quasiuniform meshes and application to the Mortar element method* (MiS Preprint 24/2001), provide a broader framework of weighted mesh inequalities; their accessible abstract does not settle the exact alternating-periodic spectral comparison, and its full preprint was not accessible for this comparison. Contemporary results on two-periodic linear spline **orthogonal-projection supremum norms** concern a different operator and do not imply the present derivative-energy generalized spectrum. The algebraic Fourier-block method is classical; no novelty is claimed for block diagonalization itself.

## Limitations
The theorem is specific to continuous degree-one periodic splines with exactly alternating positive cell lengths and consistent, unweighted continuous \(L^2\) mass. It does not characterize arbitrary meshes, higher-degree splines, or mass-lumped versions. The inner gap endpoints belong to the actual finite spectrum only when \(m\) is even. The literature comparison does not exclude a previously unindexed equivalent exact band formula, and independent mathematical review remains outstanding.

## References
1. S. Takacs and T. Takacs, *Approximation error estimates and inverse inequalities for B-splines of maximum smoothness*, arXiv:1502.03733, initial posting 2015-02-12. https://arxiv.org/abs/1502.03733
2. W. Dahmen, B. Faermann, I. G. Graham, W. Hackbusch, and S. A. Sauter, *Inverse inequalities on non-quasiuniform meshes and application to the Mortar element method*, MiS Preprint 24/2001, posted 2001-05-19. https://www.mis.mpg.de/de/publications/preprint-repository/article/2001/issue-24
3. W. Dahmen et al., *Inverse inequalities on non-quasi-uniform meshes and application to the mortar element method*, Math. Comp. 73 (2004), 1107–1138. https://doi.org/10.1090/S0025-5718-03-01583-7
