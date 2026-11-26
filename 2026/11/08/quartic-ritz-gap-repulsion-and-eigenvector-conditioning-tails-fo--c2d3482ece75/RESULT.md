# Quartic Ritz-gap repulsion and eigenvector-conditioning tails for equilateral unitary compressions

## Finding

Let \(\omega=e^{2\pi i/3}\), \(A=\operatorname{diag}(1,\omega,\omega^2)\), and let \(Q\) be any orthonormal basis of a Haar two-plane in \(\mathbb F^3\), for \(\mathbb F=\mathbb C\) or \(\mathbb R\). The matrix \(A\) is complex even when the trial plane is real. Set \(B=Q^*AQ\) and \(D=|\lambda_1(B)-\lambda_2(B)|\). When the eigenvalues are distinct, let \(\kappa_{\mathrm{eig}}\) be the spectral condition number of the matrix whose two columns are right eigenvectors of unit Euclidean norm. Both quantities are independent of the chosen orthonormal basis, and of phases and ordering of the eigenvectors. The leading tail constants are
\[
\begin{array}{c|cc}
\mathbb F & \lim_{\varepsilon\downarrow0}\varepsilon^{-4}\Pr(D\le\varepsilon)&
\lim_{R\to\infty}R^4\Pr(\kappa_{\mathrm{eig}}>R)\\ \hline
\mathbb C & \pi/(12\sqrt3) & 4\pi/(3\sqrt3)\\
\mathbb R & 1/16 & 1
\end{array}
\]
Hence for real \(p>0\), \(\mathbb E\kappa_{\mathrm{eig}}^p<\infty\) exactly when \(p<4\).

The defective planes are precisely those with a unit normal \(v\) satisfying \(|v_1|^2=|v_2|^2=|v_3|^2=1/3\). They comprise a two-torus of planes in the complex ensemble and four planes in the real ensemble. They belong to the Haar support but form a null set in both ensembles. Their compressions represent a **single unitary similarity class**, not a single trial plane.

## Proof

**Discriminant and defective set.** Write \(w_j=|v_j|^2\) and \(u=w_1+\omega w_2+\omega^2w_3\), so \(u\) is in the closed spectral triangle \(T=\operatorname{conv}\{1,\omega,\omega^2\}\). Completing \(Q\) with \(v\) to an orthonormal basis and taking the cofactor of its last row and column yields, with \((\alpha_1,\alpha_2,\alpha_3)=(1,\omega,\omega^2)\),
\[
\det(zI-B)=v^*\operatorname{adj}(zI-A)v
=\sum_j w_j\prod_{k\ne j}(z-\alpha_k)=z^2+uz+\bar u.
\]
Consequently \(D^2=|u^2-4\bar u|\). A nonzero discriminant root would have modulus 4, whereas \(|u|\le1\) on \(T\), so only \(u=0\) is possible. Since barycentric coordinates are unique, this means balanced weights. The complex normal lines of balanced weight are represented uniquely by \((1,e^{i\theta},e^{i\phi})/\sqrt3\); the real normal lines are represented by \((1,\pm1,\pm1)/\sqrt3\). The map from these lines to their orthogonal planes is bijective. Diagonal unitary phase changes (diagonal signs in the real case) commute with \(A\), identifying all balanced-weight compressions up to unitary similarity. The densities computed below give zero probability to the single weight-space point, and the Haar measure has full plane support.

**Condition number.** For \(P=QQ^*=I-vv^*\), unitarity of \(A\) gives
\[
\|B\|_F^2=\operatorname{tr}(A^*PAP)=1+|v^*Av|^2=1+|u|^2.
\]
By Schur triangularization, the squared modulus \(\nu^2\) of the upper off-diagonal entry is \(\|B\|_F^2-\sum_i|\lambda_i(B)|^2=1+(|u|^2-D^2)/2\), where the sum of squared moduli is \((|u|^2+D^2)/2\). At \(u=0\) the compression is a nonzero nilpotent (its two eigenvalues are zero, but its Frobenius norm is one); hence every repeated-eigenvalue compression here is defective. For \(D>0\), the two unit eigenvectors in the Schur basis have overlap of modulus \(\gamma=\nu/\sqrt{\nu^2+D^2}\): one is the first coordinate vector and the other has coordinate-modulus ratio \(\nu:D\). The Gram matrix has eigenvalues \(1\pm\gamma\), giving
\[
\kappa_{\mathrm{eig}}=\sqrt{\frac{1+\gamma}{1-\gamma}}
=\frac{\sqrt{\nu^2+D^2}+\nu}{D}.
\]
Since \(u^2-4\bar u=-4\bar u(1+O(|u|))\) near zero and \(\nu\to1\),
\[
D=2|u|^{1/2}(1+O(|u|)),\qquad
\kappa_{\mathrm{eig}}=|u|^{-1/2}(1+o(1)).
\]

**Planar density and limits.** Normalizing an isotropic Gaussian vector gives a Haar normal. Squared coordinate moduli before normalization are independent Gamma variables with common scale and shape \(1\) (complex) or \(1/2\) (real). Thus on the simplex the density in \((w_1,w_2)\) is \(2\) (complex) or \(1/(2\pi\sqrt{w_1w_2w_3})\) (real). The absolute Jacobian for the affine map \((w_1,w_2)\mapsto(\Re u,\Im u)\) is \(3\sqrt3/2\). At the barycenter the planar densities are respectively \(f_{\mathbb C}(0)=4/(3\sqrt3)\) and \(f_{\mathbb R}(0)=1/\pi\), both positive and continuous there. Therefore a disk of small radius \(r\) has probability \(\pi f_{\mathbb F}(0)r^2+o(r^2)\).

Away from any neighborhood of zero, compactness gives a positive lower bound on \(D\) and a finite upper bound on \(\kappa_{\mathrm{eig}}\). In that neighborhood the local expansions sandwich the events between disks with asymptotic radii \(\varepsilon^2/4\) for \(D\le\varepsilon\) and \(R^{-2}\) for \(\kappa_{\mathrm{eig}}>R\): for each fixed relative error the expansions give both inclusions eventually. A point omitted from the latter disk or assigned infinite condition has mass zero. The disk probabilities give the four constants. Finally, for \(p>0\) the layer-cake integral \(p\int_0^\infty R^{p-1}\Pr(\kappa_{\mathrm{eig}}>R)\,dR\) is finite exactly for \(p<4\) by the positive leading tail coefficient.

## Verification, context and limits

One can test the determinant, Frobenius and conditioning formulas by generating real or complex unit normals, building their orthogonal complements and comparing with direct two-by-two algebra. Explicit normals \((1,1,1)/\sqrt3\) and \((1,1,-1)/\sqrt3\) already illustrate distinct defective planes. Finite tests of identities do not establish the limits, which follow from the proof.

The numerical shadow \(u=v^*Av\) is a known distributional tool: see [*Numerical shadows: measures and densities on the numerical range*, Lemma 4.1](https://arxiv.org/abs/1010.4189) and [*Real numerical shadow and generalized B-splines*, §§2 and 4](https://arxiv.org/abs/1409.4941). Deterministic compression geometry is treated by [Malamud, Theorem 3.7](https://arxiv.org/abs/math/0304158) and by [Carden–Hansen](https://doi.org/10.1016/j.laa.2012.12.030). [Shah's random-compression pseudospectrum paper](https://arxiv.org/abs/2501.01418) gives different probabilistic area bounds whose main corollary's dimension hypothesis does not hold here. The stated result is an exact evaluation of gap and eigenvector-condition tails in this equilateral model, not a new numerical-shadow formula, deterministic geometry theorem or general pseudospectrum bound. It does not cover arbitrary spectra, finite-precision eigensolvers or non-Haar subspaces. The exact tails require unit-normalized eigenvector columns. The accessible comparisons do not establish historical priority.
