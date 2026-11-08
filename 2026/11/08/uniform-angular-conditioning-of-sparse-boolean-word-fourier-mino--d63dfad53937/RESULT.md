# Uniform angular conditioning of sparse Boolean-word Fourier minors

## Finding
Let \(r\ge 1\) be fixed, let \(n\ge r\) and \(m\ge3\) be integers, and set \(\omega=\exp(2\pi i/m)\) and \(\delta=|\omega-1|=2\sin(\pi/m)\). On the Boolean support ball
\[
\mathcal B_{n,r}=\{A\subseteq[n]:|A|\le r\},
\]
consider the square, **unnormalized** Fourier submatrix of \((\mathbb Z/m\mathbb Z)^n\),
\[
F_{n,r,m}(A,B)=\omega^{|A\cap B|}\quad(A,B\in\mathcal B_{n,r}),
\]
where a set is identified with its coordinatewise zero-one word. Every such matrix is invertible. Its spectral norm, inverse spectral norm and ordinary two-norm condition number obey, as \(n\to\infty\),
\[
\begin{aligned}
\|F_{n,r,m}\|_2&=\frac{n^r}{r!}\bigl(1+O_r(n^{-1/2})\bigr),\\
\|F_{n,r,m}^{-1}\|_2&=\frac{n^r}{r!\delta^r}\bigl(1+O_r(n^{-1/2})\bigr),\\
\kappa_2(F_{n,r,m})&=\frac{n^{2r}}{(r!)^2[2\sin(\pi/m)]^r}\bigl(1+O_r(n^{-1/2})\bigr).
\end{aligned}
\]
**All implied constants depend only on \(r\), not on \(m\)**. Consequently for any integers \(m_n\to\infty\), with no restriction on their rate of growth relative to \(n\),
\[
\frac{\kappa_2(F_{n,r,m_n})}{n^{2r}m_n^r}\longrightarrow\frac{1}{(2\pi)^r(r!)^2}.
\]
The leading left and right singular vectors for \(F_{n,r,m}\) approach the normalized constant vector, while the leading left and right singular vectors for its inverse approach the point mass at the empty set, in each case up to complex phase and with \(O_r(n^{-1/2})\) Euclidean error uniformly in \(m\). The latter statement identifies the asymptotic least-singular directions of the original matrix.

## Assumptions and scope
The ambient group is \((\mathbb Z/m\mathbb Z)^n\), equipped with the standard multiplicative character pairing \((x,y)\mapsto\exp(2\pi i\sum_jx_jy_j/m)\). Only the coordinates \(0\) and \(1\) are used in the selected rows and columns. They are not the entire nonzero-coordinate Hamming ball of the ambient group when \(m>2\). All norms are Euclidean operator norms and no \(m^{-n/2}\) Fourier normalization is used. The finite inverse formula below holds for every \(n\ge r\ge0\) and \(m\ge2\); the new uniform asymptotic statement concerns fixed \(r\ge1\) and arbitrary varying \(m\ge3\). Uniformity includes regimes where the phase separation tends to zero much faster than any power of \(n\).

## Proof
**1. Exact meet factorization.** Put \(a=\omega-1\). Index the matrix \(Z\) by \(\mathcal B_{n,r}\), with \(Z(A,C)=\mathbf1_{C\subseteq A}\). Order indices by cardinality. Then \(Z\) is lower unitriangular and the binomial identity gives
\[
\omega^{|A\cap B|}=(1+a)^{|A\cap B|}=\sum_{C\subseteq A\cap B}a^{|C|}.
\]
Hence \(F=ZDZ^{\mathsf T}\), where \(D(C,C)=a^{|C|}\). Because \(a\ne0\), this proves invertibility and the exact determinant
\[
\det F=a^{\sum_{j=0}^rj\binom nj}
=a^{n\sum_{j=0}^{r-1}\binom{n-1}j}.
\]
Boolean-lattice Möbius inversion gives \(Z^{-1}(A,C)=(-1)^{|A\setminus C|}\mathbf1_{C\subseteq A}\), so for \(U=A\cup B\) and \(u=|U|\),
\[
F^{-1}(A,B)=\begin{cases}
(-1)^{|A|+|B|}\displaystyle\sum_{k=u}^{r}\binom{n-u}{k-u}a^{-k},&u\le r,\\
0,&u>r.
\end{cases}
\tag{1}
\]
This determinant/inverse factorization is an instance of classical meet-matrix theory; neither its generic existence nor its special-case inversion is asserted to be independently novel.

**2. Forward rank-one approximation.** Let \(N=|\mathcal B_{n,r}|=\sum_{j=0}^r\binom nj\) and let \(J\) be the \(N\times N\) all-ones matrix. The difference \(F-J\) vanishes whenever \(A\cap B=\varnothing\) and its other entries have absolute value at most \(2\). Write \(b_{n,r}=\sum_{j=0}^{r-1}\binom{n-1}j\). There are at most \(n b_{n,r}^2\) ordered pairs with nonempty intersection, by selecting one shared coordinate. Therefore
\[
\|F-J\|_2\le\|F-J\|_F\le2\sqrt n\,b_{n,r}=O_r(n^{r-1/2}),
\]
with no dependence on \(m\). Since \(\|J\|_2=N=n^r/r!+O_r(n^{r-1})\), the claimed top norm follows.

**3. Inverse rank-one approximation.** Denote by \(e\) the coordinate vector at the empty set and set \(h=F^{-1}(\varnothing,\varnothing)\). Formula (1) yields
\[
h=a^{-r}\sum_{j=0}^r\binom n{r-j}a^j
=a^{-r}\left(\frac{n^r}{r!}+O_r(n^{r-1})\right),
\tag{2}
\]
uniformly over all \(m\), since \(|a|\le2\). For \(u=|A\cup B|\ge1\), the same formula bounds the entry by \(C_r|a|^{-r}n^{r-u}\), where \(C_r\) depends only on \(r\). For a fixed \(u\)-element union \(U\), at most \(3^u\) ordered pairs \((A,B)\) have \(A\cup B=U\). Consequently
\[
\begin{aligned}
\|F^{-1}-h ee^{\mathsf T}\|_F^2
&\le C_r^2|a|^{-2r}\sum_{u=1}^r3^u\binom nu n^{2r-2u}\\
&=O_r(|a|^{-2r}n^{2r-1}).
\end{aligned}
\]
Combining this with (2) gives
\[
\|F^{-1}\|_2=\frac{n^r}{r!|a|^r}\bigl(1+O_r(n^{-1/2})\bigr)
\]
uniformly in \(m\). Multiplication of the two norm estimates proves the asserted \(\kappa_2\) law. Finally, \(2\sin(\pi/m)\sim2\pi/m\) for any \(m\to\infty\), establishing the unrestricted joint limit. The singular-vector assertions follow from the rank-one gaps in Steps 2 and 3 and the standard elementary singular-vector perturbation estimate; the perturbation-to-gap ratios are \(O_r(n^{-1/2})\), uniformly in \(m\).

## Verification
The standalone script `checks/verify.py` constructs the Fourier minor directly from its character formula and a *separately implemented* entrywise inverse from (1). It checks both inverse products and the predicted determinant for 90 parameter triples with \(0\le r\le2\), various dimensions, and cyclic moduli \(2,3,4,5,11\). It also computes sample spectral condition-number ratios for \(m\in\{3,5,17,257\}\) in three radius/dimension settings. Execution produced `FINITE_PHASE_BALL_CHECKS_PASS cases=90`, maximum inverse residual approximately \(1.46\times10^{-14}\), and maximum relative determinant error approximately \(1.09\times10^{-14}\). The exact all-dimensional result is proved above; finite numerical tests are corroboration only.

## Relationship to prior work
Meet-matrix determinant and inverse formulae of Haukkanen and of Altinisik–Tuglu–Haukkanen, as summarized and compared by Mattila–Haukkanen, are **broader than** the algebraic factorization and invertibility in Step 1. Thus these algebraic formulas are background, not the originality claim. Osgood–Siripuram–Wu analyze discrete sampling and interpolation on cyclic groups, including a determinant-based **lower bound** on the condition number of particular one-dimensional sampling matrices in Appendix A; that bound neither describes the present Boolean-word Fourier minors nor determines their two-parameter sharp constant. Bass–Gröchenig address randomly chosen multivariate trigonometric sampling points and probabilistic condition estimates, rather than this deterministic family and its uniform joint limit. Earlier binary Boolean-ball inversion and conditioning cover \(m=2\), whereas the present main statement treats \(m\ge3\) with a genuinely variable character angle and a sharp modulus-uniform error estimate. No claim that a search establishes historical uniqueness is made.

## Limitations
The parameter \(r\) is fixed as \(n\to\infty\); no estimate uniform in growing \(r\) is proved. The complete finite-dimensional singular-value spectrum and optimal finite-\(n\) error constants are not computed. The spectral condition law is specific to the principal **Boolean-word** subset of the ambient Fourier matrix. A potentially relevant wider meet-matrix spectral theorem may exist; the originality assessment is bounded by the inspected sources. Independent validation is not available.

## References
1. E. Altinisik, N. Tuglu, P. Haukkanen, *Determinant and Inverse of Meet and Join Matrices*, Int. J. Math. Math. Sci. (2007), DOI:10.1155/2007/37580 (first published 2007-05-21).
2. M. Mattila, P. Haukkanen, *Determinant and inverse of join matrices on two sets*, arXiv:1110.4953 (first posted 2011-10-22); introduction discusses earlier meet-matrix inverse results.
3. B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992 (first posted 2012-04-04), especially Appendix A.
4. R. F. Bass, K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, SIAM J. Math. Anal. 36 (2004/05), DOI:10.1137/S0036141003432316.
