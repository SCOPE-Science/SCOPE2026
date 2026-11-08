# Sharp three-erasure robustness for three-frequency cyclic sampling

## Finding
For every integer \(N\ge6\), among all sets of exactly three erased samples of a three-frequency Fourier signal on the \(N\)-cycle, **the uniquely worst sets are the cyclically consecutive triples**. The exact smallest residual energy ratio and all equality signals are given below. In particular, no scattered three-site erasure causes equally large reconstruction loss.

Put \(\theta=2\pi/N\), \(d=1+2\cos\theta\), and \(e=1+2\cos(2\theta)\), and define
\[
L_N=3+\frac e2+\sqrt{\frac{e^2}{4}+2d^2}.
\]
Then for every three-site erasure set \(E\subset\mathbb Z/N\mathbb Z\) and every \(c\in\mathbb C^3\),
\[
\frac1N\sum_{j\notin E}\left|\sum_{k=0}^2c_ke^{2\pi i jk/N}\right|^2\ \ge\ \left(1-\frac{L_N}{N}\right)\sum_{k=0}^2|c_k|^2. \tag{1}
\]
The constant is positive, optimal uniformly over erasure masks, and attained precisely when \(E\) is a cyclic translate of \(\{-1,0,1\}\) and \(c\) lies on the corresponding one-dimensional top-concentration line. For \(E=\{-1,0,1\}\), that line is spanned by
\[
\left(r+2\cos\theta,\ r+2,\ r+2\cos\theta\right),\qquad r=\frac{2d}{L_N-3}.
\]
For other extremal masks, the coefficient vectors are its phase modulations. The sharp coefficient-recovery amplification, for unit-normalized full sampling, is \(\bigl(1-L_N/N\bigr)^{-1/2}\). In the minimally redundant case \(N=6\) the exact lower factor is \((3-2\sqrt2)/6\). As \(N\to\infty\), \(L_N=9-16\pi^2/N^2+O(N^{-4})\).

## Assumptions and scope
Let \(N\) be any integer at least six and \(\omega=e^{2\pi i/N}\). Equip \(\mathbb C^3\) and \(\mathbb C^N\) with their standard Euclidean norms, and let \(A:\mathbb C^3\to\mathbb C^N\) be the isometry \((Ac)_j=N^{-1/2}\sum_{k=0}^2c_k\omega^{jk}\). A mask \(E\) has exactly three distinct indices, with no weights or repeated samples. The retained operator is \(R_{E^c}A\), where \(R\) is coordinate restriction. Cyclically consecutive means \(E=\{t,t+1,t+2\}\) modulo \(N\); these are \(N\) distinct masks for \(N\ge6\). Complex coefficient vectors are allowed. All lower bounds concern squared norms; square roots give singular values.

## Proof
**1. Reduction to a three-dimensional concentration matrix.** Since the three characters are distinct, orthogonality of roots of unity gives \(A^*A=I_3\). Let \(V_E\) be the unnormalized matrix of the three erased rows, \((V_E)_{j,k}=\omega^{jk}\). Then
\[
(R_{E^c}A)^*(R_{E^c}A)=I_3-N^{-1}V_E^*V_E.
\]
The top eigenvalue of \(V_E^*V_E\) equals that of \(V_EV_E^*\). Multiplying row \(j\) by \(\omega^{-j}\) gives the real symmetric Gram kernel
\[
G_E(j,l)=g(j-l),\qquad g(s)=1+2\cos(2\pi s/N),\quad G_E(j,j)=3.
\]
Thus sharp residual stability is the maximum of \(\lambda_{\max}(G_E)\) over all three-site masks.

**2. Consecutive spectrum.** After translation and ordering, a consecutive mask gives
\[
G_{\rm con}=\begin{pmatrix}3&d&e\\d&3&d\\e&d&3\end{pmatrix},
\]
with spectrum \(3-e\) and \(3+e/2\pm\sqrt{e^2/4+2d^2}\). Since \(d>0\) and \(e\ge0\) for \(N\ge6\), the top eigenvalue \(L_N\) is simple. Its row-space eigenvector in the real gauge is \((1,r,1)\), with \(r=2d/(L_N-3)\). Undoing the row phase and applying \(V_E^*\) gives the stated frequency coefficient vector for the centered mask, and proves equality there.

**3. Every nonconsecutive mask loses strictly less energy when \(N\ge8\).** For \(N\ge8\), \(d>e\ge1\). If a pair of sites has cyclic distance at least two, its kernel entry satisfies \(|g(s)|\le e\): for angles from \(4\pi/N\) to \(\pi\), the real quantity \(1+2\cos\alpha\) lies in \([-1,e]\). Any three distinct sites which are not consecutive have **at most one** cyclicly adjacent pair. Permute their rows so that the absolute-value Gram matrix is entrywise dominated by \(G_{\rm con}\), with a strict inequality in at least one of the two positions where \(G_{\rm con}\) has off-diagonal value \(d\). For any Hermitian \(H\), \(\lambda_{\max}(H)\le\lambda_{\max}(|H|)\), because \(|z^*Hz|\le|z|^T|H||z|\). Strict Perron–Frobenius monotonicity for the irreducible positive symmetric matrix \(G_{\rm con}\) therefore yields \(\lambda_{\max}(G_E)<L_N\). This proves both optimality and strict mask uniqueness in these orders.

**4. The two smaller cyclic orders.** For \(N=6\) or \(7\), \(d\ge2\), \(e\ge0\), and every nonadjacent pair has \(|g(s)|\le1\), by direct cosine monotonicity on the available cyclic distances. Hence a nonconsecutive triple has an absolute Gram matrix entrywise bounded, after permutation, by
\[
H=\begin{pmatrix}3&d&1\\d&3&1\\1&1&3\end{pmatrix}.
\]
The Perron eigenvalue of \(H\) is \(3+\frac12(d+\sqrt{d^2+8})\). For \(d\ge2\),
\[
\frac12(d+\sqrt{d^2+8})<\sqrt2\,d\le\frac e2+\sqrt{\frac{e^2}{4}+2d^2}.
\]
The first inequality follows, on squaring positive quantities, from \(d^2>2+\sqrt2\), and the second from \(e\ge0\). Therefore all nonconsecutive masks again have strictly smaller top eigenvalue. For every \(N\ge6\), a consecutive mask has full-rank retained matrix: at least three retained distinct nodes give a nonsingular degree-two Vandermonde minor. Thus \(L_N<N\) and (1) has a strictly positive constant.

**5. Extremizers, endpoint, and asymptotic.** Simplicity of \(L_N\) shows that for a consecutive mask the only equality vectors are nonzero multiples of \(V_E^*u\), where \(u\) is the unique top erased-row eigenvector; the explicit centered expression above follows from Step 2. The strict inequalities in Steps 3–4 exclude every other mask. For \(N=6\), \(d=2\) and \(e=0\), so \(L_6=3+2\sqrt2\), giving the exact minimum \((3-2\sqrt2)/6\). Finally \(d=3-\theta^2+O(\theta^4)\) and \(e=3-4\theta^2+O(\theta^4)\) imply \(L_N=9-4\theta^2+O(\theta^4)=9-16\pi^2/N^2+O(N^{-4})\).

## Verification
The standalone `checker.py` evaluates the actual complex Fourier matrices, independently computes their Hermitian Gram eigenvalues, and exhaustively checks every three-erasure mask for all \(6\le N\le40\), including the full set of equality masks. It also checks the exact analytic contiguous spectrum, the elementary cosine comparison for additional orders, the six-node endpoint, and the large-order expansion. This finite computation corroborates Steps 1–5 and is not used as the proof of the uniform statement.

## Relationship to prior work
The classical discrete prolate literature studies time-frequency concentration and burst-erasure interpolation, notably Delsarte–Janssen–de Vries (1985). The exact arbitrary-mask minimax comparison (1) is stronger than merely solving the concentration problem on one consecutive burst. Zhu and collaborators (2017, entire accessible text, Sections II–III) provide nonasymptotic spectral-distribution estimates for a **fixed contiguous** time window, not an extremal comparison against arbitrary three-site masks. Dirckx, Huybrechs, and Ongenae (2022, entire accessible HTML, Sections 1–3) calculate singular systems for **contiguous** Fourier submatrices; their formula for the Dirichlet kernel is consistent with Step 1 but does not establish the competing-mask strict inequality.

A published exact three-node Riesz-conditioning result optimizes the ratio \(\lambda_{\max}/\lambda_{\min}\) over all three-node Fourier Vandermonde systems; its optimum is nearly equally spaced nodes. That is a different extremal functional and does not imply the sharp maximum of \(\lambda_{\max}\) here. A published two-character arbitrary-erasure result has only a two-dimensional frequency domain, and likewise does not cover the present three-frequency theorem. The closest 1984–1985 papers were not obtainable in complete text; the originality claim is qualified accordingly.

## Limitations
The result concerns exactly three consecutive frequencies, exactly three erased nodes, uniform cyclic sampling, and complex scalar coefficients. It does not determine the most harmful masks for four or more erasures, nonconsecutive frequency sets, nonuniform weights, or noncyclic groups. The historical interpolation and periodic prolate papers could not be read in full; an equivalent special theorem in those or unindexed older literature remains a residual originality risk. Independent validation has not been performed.

## References
1. K. Khare and N. George, *Sampling theory approach to prolate spheroidal wavefunctions*, Journal of Physics A 36 (2003), 10011–10021, DOI 10.1088/0305-4470/36/39/303. First publicly dated 2003-09-17.
2. Ph. Delsarte, A. J. E. M. Janssen, and L. B. Vries, *Discrete prolate spheroidal wave functions and interpolation*, SIAM Journal on Applied Mathematics 45 (1985), 641–650, DOI 10.1137/0145037.
3. W. Y. Xu and C. Chamzas, *On the periodic discrete prolate spheroidal sequences*, SIAM Journal on Applied Mathematics 44 (1984), 1210–1217, DOI 10.1137/0144086.
4. Z. Zhu et al., *The Eigenvalue Distribution of Discrete Periodic Time-Frequency Limiting Operators*, arXiv:1707.05344 (2017), Sections II–III.
5. S. Dirckx, D. Huybrechs, and R. Ongenae, *On the computation of the SVD of Fourier submatrices*, arXiv:2208.12583 (2022), Sections 1–3.
6. *Sharp Riesz conditioning for consecutive triples on finite cycles*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae .
7. *Exact adversarial erasure spectra for two-character cyclic harmonic frames*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0 .
