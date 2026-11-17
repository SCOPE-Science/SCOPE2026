# Three conditioning regimes for first-band Fourier sampling on nonbinary Hamming balls

## Finding
Let \(A\) be any finite abelian group of fixed order \(q\ge3\). For \(n\ge2\) and \(1\le r\le n\), let \(B_{n,r}\subset A^n\) consist of all words with at most \(r\) nonzero coordinates. Form the rectangular Fourier matrix \(F_{n,r}\) with rows indexed by \(B_{n,r}\) and columns indexed by the trivial character and all characters nontrivial at exactly one coordinate. Then \(F_{n,r}\) has full column rank. Its spectral condition number is independent of whether the finite abelian alphabet is cyclic or a product of cyclic groups.

Write \(p=(q-1)/q\). For each fixed density \(0<\alpha<p\), and any integer radii with \(r_n/n\to\alpha\), the *sharp* subcritical condition-number law is
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{\kappa_2(F_{n,r_n})}{n^{3/2}}
 =\frac{(q-1-q\alpha)^3}{q(q-1)\sqrt{\alpha(1-\alpha)}}.}
\]
The power \(3/2\) and the coefficient both refer to singular values of the actual rectangular sampling matrix; no normalization of all entries changes their ratio.

There is a universal, alphabet-independent crossover throughout the central-limit window. For a fixed real \(s\), if
\[
\frac{r_n-np}{\sqrt{np(1-p)}}\longrightarrow s,
\]
put \(h_s=\varphi(s)/\Phi(s)\), where \(\varphi(s)=(2\pi)^{-1/2}e^{-s^2/2}\) and \(\Phi(s)=\int_{-\infty}^{s}\varphi(u)\,du\), and let \(\Lambda_+(s)\ge\Lambda_-(s)>0\) be the eigenvalues of
\[
\begin{pmatrix}1&h_s\\h_s&1-sh_s\end{pmatrix}.
\]
Then
\[
\boxed{\displaystyle
\kappa_2(F_{n,r_n})\longrightarrow
\sqrt{\Lambda_+(s)/\Lambda_-(s)}.}
\]
At \(s=0\), the limit equals \(\sqrt{(1+\sqrt{2/\pi})/(1-\sqrt{2/\pi})}\). In contrast, if \(r_n/n\to\alpha>p\), then \(\kappa_2(F_{n,r_n})\to1\). Together these are a sharp three-regime stability law for a natural nonbinary deterministic Fourier sampling family.

## Assumptions and scope
All groups are finite abelian with fixed order \(q\ge3\), and the dimension tends to infinity while \(q\) stays fixed. The Fourier columns are all \(1+n(q-1)\) characters of support size at most one. The sample rows are **every** word in the indicated ball, not random points. A word's weight is the number of nonidentity coordinates. Throughout, \(\kappa_2(F)\) means the ratio of the largest to smallest nonzero singular value of \(F\). The finding also covers the case \(q=2\) algebraically, but no originality is asserted there: the new quantitative claims are restricted to \(q\ge3\). The exact finite-dimensional Gram decomposition below is used as an auxiliary calculation and is not by itself asserted to be a new independent theorem.

## Proof
**1. Exact Gram decomposition.** Let \(X\) be uniformly distributed on \(B_{n,r}\), and let \(W\) be its Hamming weight. Relative to the ball-normalized inner product, the Gram matrix of the Fourier columns is \(G=F_{n,r}^{*}F_{n,r}/|B_{n,r}|\). Put
\[
a=\frac{\mathbb E W}{n},\qquad
b=\frac{\mathbb E[W(W-1)]}{n(n-1)},\qquad
\nu=1-\frac{qa}{q-1},\qquad
\tau=1-\frac{2qa}{q-1}+\frac{q^2b}{(q-1)^2}.
\]
Character orthogonality among the \(q-1\) nonidentity symbols gives a Gram diagonal entry \(1\) for every Fourier column, cross entry \(\nu\) between the constant and a nontrivial one-coordinate character, cross entry \(\nu\) between distinct nontrivial characters on the *same* coordinate, and cross entry \(\tau\) between characters on *different* coordinates. These identities use only the order of \(A\), not its internal structure.

Decompose the \(q-1\) nontrivial characters at each coordinate into the direction constant across labels and its \((q-2)\)-dimensional orthogonal complement. Next split the coordinate-constant-label directions into their global sum and the \((n-1)\)-dimensional sum-zero space. The exact eigenvalues of \(G\), with multiplicities, are
\[
\begin{array}{ll}
\displaystyle L_{\rm label}=\frac{qa}{q-1}, & n(q-2),\\[3pt]
\displaystyle L_{\rm site}=\frac{q^2(a-b)}{q-1}, & n-1,
\end{array}
\]
and the two eigenvalues of
\[
R_{n,r}=\begin{pmatrix}1&m\\m&m^2+v\end{pmatrix},\qquad
m=\frac{n(q-1)-q\mathbb EW}{\sqrt{n(q-1)}},\quad
v=\frac{q^2\operatorname{Var}(W)}{n(q-1)}.
\]
The radial second basis vector is \((n(q-1))^{-1/2}\sum_{i,\chi\ne1}\chi(X_i)\), which equals \((n(q-1)-qW)/\sqrt{n(q-1)}\) pointwise. This proves the matrix \(R_{n,r}\), including its normalization. Since \(r\ge1\), \(W\) takes both zero and one with positive probability, so \(v>0\). Also \(a>0\) and \(a-b=\mathbb E[W(n-W)]/[n(n-1)]>0\) for \(n\ge2\) and \(r\ge1\). Thus all the eigenvalues are positive. The rank and group-independence assertions follow.

**2. Exact computable moments.** Write
\[
N=\sum_{j=0}^{r}\binom nj(q-1)^j.
\]
Then
\[
\mathbb EW=\frac{\sum_{j=0}^{r}j\binom nj(q-1)^j}{N},\qquad
\mathbb E[W(W-1)]=\frac{\sum_{j=0}^{r}j(j-1)\binom nj(q-1)^j}{N}.
\]
These rational sums determine the entire spectrum just derived, and furnish a direct independent numerical replay path. Under the unrestricted uniform distribution on \(A^n\), \(W\sim\operatorname{Bin}(n,p)\); under the ball-uniform distribution it has precisely this binomial distribution conditioned on \(W\le r\).

**3. Subcritical geometric boundary layer.** Fix \(0<\alpha<p\), let \(r_n/n\to\alpha\), and put \(J=r_n-W\). For each fixed nonnegative integer \(j\), the ratio of the unnormalized binomial masses at \(r_n-j\) and at \(r_n\) converges to \(\rho^j\), where
\[
\rho=\frac{\alpha}{(q-1)(1-\alpha)}<1.
\]
The successive ratios as one moves toward smaller weights are decreasing, and for all sufficiently large \(n\) are uniformly bounded above by some \(\rho_*<1\). Dominated convergence therefore applies also to the second moments of \(J\): \(J\) converges in its first two moments to a geometric random variable with \(\operatorname{Var}(J)=\rho/(1-\rho)^2\). Consequently \(\mathbb EW/n\to\alpha\) and \(\operatorname{Var}(W)\to V=\rho/(1-\rho)^2\).

Put \(C=q-1-q\alpha>0\). The larger eigenvalue of \(R_{n,r_n}\) satisfies \(\lambda_+\sim nC^2/(q-1)\). Since \(\det R_{n,r_n}=v\), its smaller eigenvalue satisfies
\[
\lambda_-\sim\frac{q^2V}{n^2C^2}.
\]
The two other spectral sectors converge to the strictly positive constants \(q\alpha/(q-1)\) and \(q^2\alpha(1-\alpha)/(q-1)\). Thus \(\lambda_+\) and \(\lambda_-\) are respectively the largest and smallest Gram eigenvalues for all sufficiently large \(n\). Their square-root ratio gives
\[
\frac{\kappa_2(F_{n,r_n})}{n^{3/2}}
\longrightarrow\frac{C^2}{q\sqrt{(q-1)V}}
=\frac{C^3}{q(q-1)\sqrt{\alpha(1-\alpha)}}.
\]
The last equality uses the explicit \(\rho\) and involves no unproved interchange of asymptotic limits.

**4. Central-limit window.** With \(p=(q-1)/q\), the radial Fourier character sum above is *exactly* the negative of the binomial standardized weight:
\[
\frac{n(q-1)-qW}{\sqrt{n(q-1)}}
=-\frac{W-np}{\sqrt{np(1-p)}}.
\]
If the threshold converges to a finite standardized \(s\), the binomial central limit theorem gives convergence of this variable conditional on \(W\le r_n\) to \(-Z\) conditioned on \(Z\le s\), for standard normal \(Z\). The conditional first and second moments converge because the unconditioned standardized binomial fourth moments are bounded and \(\Pr\{W\le r_n\}\to\Phi(s)>0\). Gaussian integration gives \(\mathbb E[-Z\mid Z\le s]=h_s\) and \(\mathbb E[Z^2\mid Z\le s]=1-sh_s\). Hence \(R_{n,r_n}\) converges to the displayed positive definite Gaussian block. The label and site eigenvalues both tend to \(1\), while the two eigenvalues of the limiting block lie strictly on opposite sides of \(1\) because its off-diagonal entry is positive. Continuity of matrix eigenvalues proves the sharp window condition-number limit.

**5. Supercritical completeness.** If \(r_n/n\to\alpha>p\), the complementary binomial upper-tail probability decreases exponentially. The moments of every fixed set of coordinate characters conditioned on \(W\le r_n\) converge to their unrestricted orthogonality values exponentially fast. Since there are only \(1+n(q-1)\) Fourier columns, the full Gram matrix converges in operator norm to the identity. Therefore both extreme singular values become asymptotically equal and \(\kappa_2\to1\).

## Verification
The standalone `verify.py` constructs the actual Fourier sampling matrix for alphabets \(\mathbb Z_3\), \(\mathbb Z_4\), \(\mathbb Z_2\times\mathbb Z_2\), and \(\mathbb Z_5\), every \(2\le n\le4\), and every \(1\le r\le n\). It compares all eigenvalues with independently computed moment-sector predictions, in 36 complete finite cases. It also checks the sharp subcritical normalization numerically for several densities and the central-window limit for finite positive and negative standardized thresholds. Execute `python verify.py` from the extracted package directory, with Python 3 and NumPy installed. The expected marker is `HAMMING_BALL_FIRST_BAND_CHECKS_PASS finite_cases=36`. These finite calculations independently test normalizations and computations; the infinite-dimensional statements rest on the proofs above.

## Relationship to prior work
The Fourier/spatial concentration formalism is standard (Tsitsvero–Barbarossa–Di Lorenzo), and multivariate Krawtchouk orthogonality was established independently of this calculation (Mizukawa). Cheraghchi–Guruswami–Velingker connect finite Fourier sampling with coding and restricted isometry, but do not derive deterministic low-band Hamming-ball conditioning constants.

Closest relevant previously published computations are the exact first Walsh band on **binary** Hamming balls and the first Fourier band on one **nonbinary fixed-weight shell**. The former already supplies the Boolean central Gaussian limit, and the latter supplies an exact one-shell Gram spectrum and its kernel; neither explicitly states the sharp \(q\ge3\) subcritical \(n^{3/2}\) coefficient or the nonbinary full central-window crossover. The exact **finite** ball Gram decomposition can also be recovered by summing the fixed-weight-shell Gram operators and is *not* asserted as an independent novelty. A separate all-degree result for nonbinary single spheres likewise treats a fixed weight rather than a ball. The novelty claimed here is limited to the complete sharp nonbinary **asymptotic conditioning trichotomy**, including the explicit low-density leading coefficient. The known binary case and the fixed-shell formulas materially reduce the work needed; this is explicitly acknowledged.

## Limitations
All asymptotics fix the alphabet order \(q\). The subcritical law assumes an interior limiting density; it does not claim a uniform estimate as that density tends to zero or to the binomial mean. The central-window formula fixes a finite standardized threshold and does not assert an error estimate uniform in the threshold. Neither a joint growing-alphabet limit nor higher Fourier bands are covered. Although the comparison to the closest published source statements did not uncover the exact asserted asymptotic trichotomy, its ingredients are close to existing exact shell spectra, so an implicit-priority or routinely-derived-corollary risk remains. There is no independent mathematical audit.

## References
1. Hiroshi Mizukawa, *Orthogonality Relations for Multivariate Krawtchouk Polynomials*, arXiv:1009.1203v1, first publicly posted 2010-09-07, https://arxiv.org/abs/1009.1203.
2. Mahdi Cheraghchi, Venkatesan Guruswami, and Ameya Velingker, *Restricted Isometry of Fourier Matrices and List Decodability of Random Linear Codes*, arXiv:1207.1140v1, publicly posted 2012-07-04, https://arxiv.org/abs/1207.1140.
3. Mikhail Tsitsvero, Sergio Barbarossa, and Paolo Di Lorenzo, *Signals on Graphs: Uncertainty Principle and Sampling*, arXiv:1507.08822v1, first publicly posted 2015-07-31, https://arxiv.org/abs/1507.08822.
4. *Exact first-Walsh-band concentration spectra on Boolean Hamming balls*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f.
5. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594.
6. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
