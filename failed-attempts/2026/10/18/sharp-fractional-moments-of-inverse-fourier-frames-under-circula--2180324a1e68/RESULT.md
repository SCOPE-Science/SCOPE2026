# Sharp fractional moments of inverse Fourier frames under circular repulsion

## Finding
Fix an integer \(N\ge2\) and \(\beta>0\). Write \(z_j=e^{i\theta_j}\) and give the ordered points \((z_1,\ldots,z_N)\) the probability density
\[
\frac{G(z_1,\ldots,z_N)}{Z_{N,\beta,G}}\prod_{1\le i<j\le N}|z_i-z_j|^{\beta}
\]
relative to \(d\theta_1/(2\pi)\cdots d\theta_N/(2\pi)\), where \(G\) is measurable and \(0<c\le G\le C<\infty\) almost everywhere. Let \(A_{jk}=z_j^{k}\), for row indices \(1\le j\le N\) and column indices \(0\le k<N\), and define the inverse-gram trace \(T=\operatorname{tr}((A^*A)^{-1})\). Then \(A\) is invertible almost surely, and, **for every real \(p>0\)**,
\[
\boxed{\quad\mathbb E[T^p]<\infty\ \Longleftrightarrow\ 2p<\beta+1.\quad}
\]
At \(2p=\beta+1\), the defining integral diverges already on neighborhoods of a single pair collision. This is an all-orders, exact, dimension-independent threshold; no asymptotic limit in \(N\) is taken. Translating the whole consecutive frequency band by an integer does not change the singular values or the statement.

If independent observation noise \(\xi\) has law \(\mathcal N_{\mathbb C}(0,\tau^2 I_N)\), with \(\tau>0\), and the coefficient error is \(e=A^{-1}\xi\), then, for all \(p>0\),
\[
\boxed{\quad\mathbb E\|e\|_2^{2p}<\infty\ \Longleftrightarrow\ 2p<\beta+1.\quad}
\]
In particular, the squared-error mean is finite exactly for \(\beta>1\), whereas its second moment is finite exactly for \(\beta>3\). Thus unitary repulsion, \(\beta=2\), makes mean-squared coefficient error finite but does not give the error a finite variance.

For the unmodified circular unitary ensemble (\(G\equiv1\), \(\beta=2\)), the projection-determinantal cofactor identity, already implicit in general volume-sampling theory [3,4], gives the exact normalization
\[
\mathbb E[(A^*A)^{-1}]=I_N,\qquad\mathbb E T=N.
\]
For noise covariance \(\varepsilon^2 I_N/N\), the mean squared coefficient error is consequently \(\varepsilon^2\), versus \(\varepsilon^2/N\) at equally spaced noiselessly conditioned nodes. This identity provides a benchmark rather than a separately asserted originality claim.

## Assumptions and scope
All matrix norms are unnormalized Euclidean/Frobenius norms, angular base measure is probability-normalized Haar measure, and the Fourier matrix entries have modulus one (there is no \(N^{-1/2}\) factor). The model samples exactly \(N\) points for \(N\) consecutive Fourier coefficients. The repulsion exponent \(\beta\) is any fixed positive real, not the aspect-ratio parameter with the same conventional letter in random-matrix asymptotics. There is no independence requirement on the points or permutation symmetry requirement on \(G\), only a uniform strictly positive lower bound and finite upper bound. The strict positivity condition on \(G\) is essential for the divergent-side conclusion: a density vanishing near collisions can change the threshold.

## Proof
**1. An upper comparison by one-point Lagrange denominators.** Pairwise collisions have zero probability. For distinct nodes, the \(j\)-th Lagrange cardinal polynomial is
\[
L_j(x)=\frac{\prod_{m\ne j}(x-z_m)}{\prod_{m\ne j}(z_j-z_m)}.
\]
Its coefficient vector is precisely column \(j\) of \(A^{-1}\). Since \(|z_m|=1\), the absolute value of its coefficient of degree \(k\) is at most \(\binom{N-1}{k}\prod_{m\ne j}|z_j-z_m|^{-1}\). Vandermonde's binomial identity gives
\[
T=\|A^{-1}\|_F^2\le \binom{2N-2}{N-1}\sum_{j=1}^{N}\prod_{m\ne j}|z_j-z_m|^{-2}.
\]
For any \(p>0\), the finite-sum power inequality
\( (\sum_j b_j)^p\le N^{\max\{p-1,0\}}\sum_j b_j^p\)
shows that it suffices to integrate one term \(\prod_{m\ne j}|z_j-z_m|^{-2p}\). Multiplying by the sampling density, bound \(G\le C\) and all factors between pairs not incident to \(j\) by \(2^\beta\). The remaining product of factors \(\prod_{m\ne j}|z_j-z_m|^{\beta-2p}\) is integrable in \(N-1\) independent angular variables precisely when \(\beta-2p>-1\), since a circle chord is comparable to the angular gap near coincidence. This proves finiteness for all \(2p<\beta+1\) without excluding simultaneous multi-point collisions by fiat; those configurations were included in the integral bound.

**2. The sharp collision obstruction.** Restrict the nodes so that \(z_1,z_2\) lie in one small arc, and the remaining \(N-2\) nodes lie in mutually separated arcs, each away from the first one. The joint density on this positive-measure region is at least a fixed positive multiple of \(|z_1-z_2|^\beta\). With the unit left test vector \(v=(1,-1,0,\ldots,0)/\sqrt2\),
\[
\lambda_{\min}(AA^*)\le v^*AA^*v=\frac12\sum_{k=0}^{N-1}|z_1^k-z_2^k|^2\le\frac12\Bigl(\sum_{k=1}^{N-1}k^2\Bigr)|z_1-z_2|^2,
\]
where \(|z_1^k-z_2^k|\le k|z_1-z_2|\) on the unit circle. Since \(T=\operatorname{tr}((AA^*)^{-1})\ge1/\lambda_{\min}(AA^*)\), we have \(T^p\ge c_{N,p}|z_1-z_2|^{-2p}\) there. The remaining gap integral contains \(\int_0^\delta t^{\beta-2p}\,dt\) and diverges if \(2p\ge\beta+1\). This includes the exact endpoint and proves necessity for every \(N\ge2\).

**3. Actual Gaussian coefficient noise.** Conditional on \(A\), write the eigenvalues of \((A^*A)^{-1}\) as \(b_1,\ldots,b_N>0\), with \(T=\sum b_j\). For independent standard circular complex Gaussian coordinates \(g_j\), \(\|A^{-1}\xi\|_2^2\) has conditional law \(\tau^2\sum b_j|g_j|^2\). Since \(\max_j b_j\ge T/N\) and \(\sum b_j|g_j|^2\le T\sum |g_j|^2\), for every \(p>0\) its conditional \(p\)-moment lies between \(\tau^{2p}N^{-p}\Gamma(p+1)T^p\) and \(\tau^{2p}\mathbb E[(\sum_j |g_j|^2)^p]T^p\). The Gaussian factors are positive and finite, so the same sharp threshold follows by integration over the nodes.

**4. The exact unitary mean, as context.** Under \(G\equiv1\) and \(\beta=2\), the joint density is \(|\det A|^2/N!\), using orthonormality of the circle characters. Write \(C_{jk}\) for the cofactor of entry \((j,k)\). The inverse Gram entry \(((A^*A)^{-1})_{k\ell}\) becomes \(\sum_jC_{jk}\overline{C_{j\ell}}/|\det A|^2\). The determinant factors cancel against the density. Integration of products of minors against the \(N-1\) retained Haar angles gives \((N-1)!\delta_{k\ell}\) by permutation expansion and Fourier orthogonality. Sum over the \(N\) choices of deleted row, divide by \(N!\), and obtain \(\mathbb E[(A^*A)^{-1}]=I_N\). This familiar projection-DPP identity is included to normalize the comparison, not claimed as a new theorem.

**5. Exact two-point check.** For \(N=2\), \(T=\csc^2((\theta_1-\theta_2)/2)\), and direct beta-function integration gives, for \(2p<\beta+1\),
\[
\mathbb E T^p=\frac{\Gamma((\beta-2p+1)/2)\Gamma((\beta+2)/2)}{\Gamma((\beta-2p+2)/2)\Gamma((\beta+1)/2)}.
\]
This special case yields \(\mathbb E T=\beta/(\beta-1)\) when \(\beta>1\), and exhibits the same sharp endpoint. It is a normalization test rather than the basis for extrapolating the universal statement.

## Verification
The companion `verify.py` executes exact rational two-node trigonometric beta-moment comparisons, exact Haar-character orthogonality of the cofactor minors for matrix sizes \(2\le N\le5\), and independent numerical Lagrange-inverse-versus-Gram-inverse comparisons for matrix sizes \(2\le N\le7\). All reported comparisons completed successfully. They corroborate selected algebraic steps; the proof in Steps 1–4 establishes all sizes, exponents and angular densities without a finite-enumeration inference. Reproduce with `python3 verify.py` (Python standard library only).

## Relationship to prior work
Xu and Shen [1] identify inverse singular-value moments as the reconstruction-risk mechanism and prove divergence of expected risk for independent uniform Fourier nodes; they also study equally spaced and jittered designs, not circular repulsive point ensembles. Tucci and Whiting [2, Theorem 3.3] already prove divergence of integer-order inverse spectral moments for independent phases, using an inverse Vandermonde formula. The independent case is not asserted as novel here.

Projection determinantal sampling and volume sampling are studied by Belhadji, Bardenet and Chainais [3] and Nouy and Michel [4]; the latter's Lemma 4.9 covers the first inverse-Gram mean at exactly interpolating design size. Consequently the \(\beta=2\) exact first-moment identity is **credited as established**. Neither inspected work supplies the all-\(p\) sharp threshold \(2p=\beta+1\) under circular \(\beta\)-repulsion, the controlled density perturbation, or the corresponding variance boundary for actual Gaussian noise. Ryan and Debbah [5] study asymptotic moments for independent-phase Vandermonde matrices, not the present repulsive finite-size negative-moment classification. The circular-ensemble density itself is classical [6]. The claim of novelty is limited to the complete robust fractional-moment transition and its noise consequence.

## Limitations
The result concerns a square consecutive-frequency Fourier matrix with a finite number of nodes; it does not characterize oversampled or general sparse-frequency matrices, nor does it supply quantitative prefactors for moments at arbitrary \(N\). The assumption \(c\le G\le C\) cannot be discarded for the divergent half of the theorem. No exact tail asymptotic, best constant or independence assertion is made. The first-moment CUE identity is not original; it is expressly credited to projection-volume sampling. Historical priority of the full repulsive fractional-moment threshold requires additional independent bibliographic review. This manuscript has not received independent mathematical validation.

## References
[1] Hang Xu and Yi Shen, *Non-asymptotic Analysis of Expected Reconstruction Risk for Trigonometric Polynomial Models*, first submitted 24 September 2026, https://arxiv.org/abs/2609.29286.

[2] Gabriel H. Tucci and Philip A. Whiting, *Asymptotic Behavior of the Maximum and Minimum Singular Value of Random Vandermonde Matrices*, first submitted 15 February 2012, Theorems 3.1 and 3.3, https://arxiv.org/html/1202.3184v2.

[3] Ayoub Belhadji, Rémi Bardenet and Pierre Chainais, *Signal reconstruction using determinantal sampling*, first submitted 13 October 2023, Section 2.3, https://arxiv.org/html/2310.09437v2.

[4] Anthony Nouy and Bertrand Michel, *Weighted least-squares approximation with determinantal point processes and generalized volume sampling*, first submitted 21 December 2023, Section 4 and Lemma 4.9, https://arxiv.org/pdf/2312.14057.

[5] Øyvind Ryan and Merouane Debbah, *Asymptotic Behaviour of Random Vandermonde Matrices with Entries on the Unit Circle*, first submitted 25 February 2008, https://arxiv.org/abs/0802.3570.

[6] Rowan Killip and Irina Nenciu, *Matrix models for circular ensembles*, International Mathematics Research Notices (2004), https://doi.org/10.1155/S1073792804141597.
