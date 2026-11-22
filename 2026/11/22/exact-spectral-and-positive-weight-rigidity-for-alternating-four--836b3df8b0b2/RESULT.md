# Exact spectral and positive-weight rigidity for alternating Fourier sampling

## Finding

Let \(N=2m\ge 2\) be even and let \(-\pi/N<\delta<\pi/N\). At the \(N\) distinct points
\[
\theta_j=\frac{2\pi j}{N}+(-1)^j\delta\pmod {2\pi},\qquad 0\le j<N,
\]
consider the \(N\) consecutive Fourier characters \(e^{ik\theta}\), \(0\le k<N\). For any strictly positive normalized sampling weights \(w_j\) with \(\sum_jw_j=1\), set
\[
G(w)_{k\ell}=\sum_{j=0}^{N-1}w_j e^{i(k-\ell)\theta_j},\qquad s=\left|\sin\left(\frac{N\delta}{2}\right)\right|<1.
\]
The uniform weights \(w_j=1/N\) have the **complete** Gram spectrum
\[
\operatorname{spec}G(1/N)=\{1-s\;(m\text{ times}),\;1+s\;(m\text{ times})\}.
\]
Among **all** positive normalized weights, not merely weights constant on each subgrid, they simultaneously attain the largest possible lower eigenvalue, the smallest possible upper eigenvalue, the least spectral condition number, the least Frobenius Gram defect, and the greatest Gram determinant. In precise terms,
\[
\lambda_{\min}(G(w))\le 1-s,\quad
\lambda_{\max}(G(w))\ge 1+s,\quad
\frac{\lambda_{\max}(G(w))}{\lambda_{\min}(G(w))}\ge\frac{1+s}{1-s},
\]
\[
\|G(w)-I\|_F^2\ge Ns^2,\qquad \det G(w)\le (1-s^2)^{N/2}=\cos^N\left(\frac{N\delta}{2}\right).
\]
Equality in either the Frobenius or determinant bound holds **only** for uniform weights. The uniform weights attain equality in both individual eigenvalue bounds and the condition-number bound.

If normalization is dropped and arbitrary positive weights are permitted, the unique best scalar shrinkage is \(w_j=[N(1+s^2)]^{-1}\). Its exact globally minimum Frobenius defect is
\[
\min_{w_j>0}\|G(w)-I\|_F^2=\frac{Ns^2}{1+s^2}.
\]
At the collision boundary \(|\delta|=\pi/N\), the nodes pair up and the sampling matrix has rank \(N/2\), so no positive reweighting can recover a full frame.

## Assumptions and scope

The trigonometric-polynomial space has **exactly** \(N\) consecutive integer frequencies. All \(N\) sample nodes are retained; only their positive weights are variable. The Gram matrix has no hidden normalization factor: its diagonal entries equal \(\sum_jw_j\). The statements about eigenvalue and determinant optima require unit total weight, while the last Frobenius formula explicitly allows varying total weight. No assertion is made about arbitrary nonperiodic jitter, oversampled frequency sets, or quadrature for higher-frequency integrands.

With a fixed jitter fraction \(\alpha\) of the original node spacing, write \(\delta=2\pi\alpha/N\), \(|\alpha|<1/2\). Then \(s=|\sin(\pi\alpha)|\); the optimal frame condition is independent of \(N\), even for \(1/4<|\alpha|<1/2\). As \(|\alpha|\uparrow1/2\), the optimal squared-analysis condition number grows as \(4/[\pi^2(1/2-|\alpha|)^2]\).

## Proof

**1. Exact spectrum.** Write \(N=2m\) and form the normalized Fourier evaluation matrix \(U_{kj}=N^{-1/2}e^{ik\theta_j}\). Permute the even and odd sampling columns into separate blocks. Apply an \(m\)-point unitary Fourier transform in the even and odd sample indices, and pair Fourier rows \(r\) and \(r+m\), \(0\le r<m\). Up to diagonal unitary factors, the resulting \(m\) independent matrices have the form
\[
Q_r=\frac{1}{\sqrt2}\begin{pmatrix}
e^{ir\delta}&e^{i(r+m)\delta}\\
e^{ir(\pi/m-\delta)}&-e^{ir(\pi/m-\delta)}e^{-im\delta}
\end{pmatrix}.
\]
Each \(Q_r\) has squared Frobenius norm \(2\) and determinant modulus \(|\cos(m\delta)|\), so the eigenvalues of \(Q_r^*Q_r\) are exactly \(1\pm|\sin(m\delta)|\). These are the eigenvalues of \(G(1/N)=UU^*\), proving the spectrum, determinant, and invertibility for the stated open range.

**2. Finite dihedral symmetrization.** Regard the node set as two interlaced regular \(m\)-gons on the circle. It is invariant under a rotation by \(2\pi/m\) and under the reflection \(\theta\mapsto 2\pi/N-\theta\), which exchanges the two orbits. These maps generate a transitive action on all \(N\) nodes. Rotating the nodes multiplies each Fourier row by a unimodular scalar and hence unitarily conjugates the Gram matrix. Reflecting nodes maps a Fourier column to its entrywise conjugate, multiplied by frequency-dependent phases; thus it takes \(G\) to a diagonal-unitary conjugate of \(\overline G\). Both operations preserve eigenvalues, determinants, and the Frobenius distance to \(I\).

Average any positive normalized weight vector over this finite transitive action. The resulting vector is uniform. If \(a=\lambda_{\min}(G(w))\), \(b=\lambda_{\max}(G(w))\), every matrix along the orbit satisfies \(aI\preccurlyeq G\preccurlyeq bI\); so does their average, \(G(1/N)\). The exact spectrum from step 1 yields \(a\le1-s\) and \(b\ge1+s\), and thus the sharp ratio inequality. Convexity of the squared Frobenius norm gives the bound \(\|G(w)-I\|_F^2\ge\|G(1/N)-I\|_F^2=Ns^2\).

**3. Equality and determinant.** The map \(w\mapsto G(w)\) is injective for the distinct nodes: its matrix entries \(G_{k0}\), \(0\le k<N\), are the first \(N\) Vandermonde moments of \(w\), and the matrix \((e^{ik\theta_j})_{k,j}\) is invertible. Therefore \(w\mapsto\|G(w)-I\|_F^2\) is strictly convex; equality in its symmetrization inequality forces the uniform vector. If \(A_{kj}=e^{ik\theta_j}\), then \(G(w)=A\operatorname{diag}(w)A^*\), so \(\det G(w)=|\det A|^2\prod_jw_j\). The arithmetic-geometric mean inequality gives \(\prod_jw_j\le N^{-N}\), with equality only at uniform weights; step 1 supplies the displayed sharp determinant.

**4. Unnormalized optimization.** Fix \(t=\sum_jw_j>0\). The same transitive averaging and strict convexity show that uniform weights \(w_j=t/N\) uniquely minimize the Frobenius defect for this total mass. Their Gram eigenvalues are \(t(1\pm s)\), so
\[
\|G(t/N)-I\|_F^2=N\{(t-1)^2+t^2s^2\}.
\]
This strictly convex scalar quadratic has unique minimum at \(t=(1+s^2)^{-1}\), with minimum \(Ns^2/(1+s^2)\).

**5. Collision and asymptotics.** At \(|\delta|=\pi/N\), each neighboring pair of nodes coincides, leaving exactly \(N/2\) distinct sites and rank \(N/2\). For \(\alpha=1/2-\varepsilon\), \(s=\cos(\pi\varepsilon)=1-\pi^2\varepsilon^2/2+O(\varepsilon^4)\); inserting this into the exact eigenvalue ratio proves the quadratic divergence. The negative endpoint follows by reflection.

## Verification

The standalone `CHECK.py` recomputes complex Fourier Gram matrices directly, verifies their quadratic spectral identity, determinant and exact normalized and unnormalized Frobenius formulas for even orders \(2\) through \(32\), and checks the global normalized bound for seeded random positive weight vectors. The saved checker reports 846 successful supplementary assertions. These finite calculations corroborate but are not substitutes for the proof for all even orders and all positive weights.

## Relationship to prior work

Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling* (arXiv:2611.02379, first posted 2026-11-02), proves first-order alias-covariance and weight-orthogonality statements at critically sampled Fourier grids. Its introduction and Section 9 explicitly separate the local first-order program from optimization of weights at fixed imperfect nodes and spectral objectives. The present result instead solves a particular periodic-jitter design **nonperturbatively**, with exact spectral extrema and global positive-weight optimization.

Austin and Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points* (arXiv:1612.04018; *SIAM J. Numer. Anal.* 2017), study interpolation and convergence at general perturbed grids with odd numbers of nodes, giving bounds rather than this all-even, two-coset sharp spectrum. Yu and Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature* (arXiv:2202.04722, 2022), develop universal perturbation bounds and examples of negative exact quadrature weights, again without the stated global normalized Gram optimization. Standard finite Fourier decomposition and the \(2\)-coset polyphase viewpoint are established tools, not claimed as novel.

## Limitations

The theorem concerns alternating periodic jitter and one critically sampled consecutive-frequency block. The exact algebra is elementary after symmetry reduction; priority may be affected by older polyphase or periodically nonuniform sampling references not located here. Neither an arbitrary-jitter stability result nor an assertion about unique minimizers of the spectral condition-number objective is established. No independent mathematical validation is claimed.

## References

1. E. Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling*, arXiv:2611.02379 (2026). https://arxiv.org/abs/2611.02379
2. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, SIAM J. Numer. Anal. 55 (2017), 2113–2122. https://doi.org/10.1137/16M1107760
3. A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (2022). https://arxiv.org/abs/2202.04722
4. R. Ghosh, S. Mulleti, and C. S. Seelamantula, *Multichannel Sampling and Reconstruction in Multidimensional Shift-Invariant Spaces*, arXiv:2610.36142 (2026). https://arxiv.org/abs/2610.36142
