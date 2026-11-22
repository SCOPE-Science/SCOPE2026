# Exact weak-damping inertia and an eventual half-negative law for powered geodesic circle kernels

## Finding
Fix a real exponent \(\alpha>1\), a damping parameter \(t>0\), and an even integer \(N\ge2\). Sample the unit circle at \(x_j=2\pi j/N\) and put
\[
G_{N,\alpha,t}(j,k)=\exp\!\left[-t\,d_{\mathbb S^1}(x_j,x_k)^\alpha\right],\qquad 0\le j,k<N,
\]
where \(d_{\mathbb S^1}\) is shortest angular arc distance in \([0,\pi]\). Write \(n_+,n_-,n_0\) for the positive, negative and zero eigenvalue counts, with multiplicity.

**Exact all-size signature at weak damping.** For every real \(\alpha>1\), every even \(N\ge2\), and
\[
0<t\le \frac{\alpha-1}{\alpha\pi^\alpha},
\]
the matrix is nonsingular and
\[
\boxed{\bigl(n_+(G_{N,\alpha,t}),n_-(G_{N,\alpha,t}),n_0(G_{N,\alpha,t})\bigr)
=\left(\frac N2+1,\frac N2-1,0\right).}
\]
More precisely, its cyclic Fourier modes \(k\ne0\) have strictly positive eigenvalue for odd \(k\) and strictly negative eigenvalue for even \(k\).

**Exact eventual signature at arbitrary fixed damping.** For \(m\ge0\), let
\[
b_m=\frac1\pi\int_0^\pi e^{-t\theta^\alpha}\cos(m\theta)\,d\theta.
\]
Define the integer
\[
J_{\alpha,t}=\#\{m\ge1:m\text{ odd},\ b_m<0\}
-\#\{m\ge2:m\text{ even},\ b_m>0\}.
\]
Both sets are finite. For every fixed \((\alpha,t)\) there exists an even-size cutoff \(N_0(\alpha,t)\) such that for **all even** \(N\ge N_0(\alpha,t)\), the sample matrix is nonsingular and
\[
\boxed{n_-(G_{N,\alpha,t})=\frac N2-1+2J_{\alpha,t}.}
\]
In particular, for every fixed \(\alpha>1,t>0\),
\[
\boxed{\lim_{\substack{N\to\infty\\2\mid N}}\frac{n_-(G_{N,\alpha,t})}{N}=\frac12.}
\]
Vanishing continuum coefficients \(b_m=0\) produce no correction in \(J_{\alpha,t}\): the finite-grid alias tail has the baseline parity sign for all sufficiently large even \(N\). The displayed weak-damping interval is a sufficient, explicitly quantified interval, not asserted to be the largest interval of the stated inertia law.

## Assumptions and scope
The circle has circumference \(2\pi\); the distance is intrinsic arc distance, **not** Euclidean chord length and **not** unnormalized graph distance. The exponent \(\alpha>1\) is an arbitrary fixed real number, not required to be integral. The sampling points are uniformly spaced and the grid size is even. Eigenvalue counts include real multiplicity; the complex discrete Fourier diagonalization gives the same real eigenvalues and multiplicities. At general fixed \((\alpha,t)\) the eventual-size cutoff is an existence result, not a uniform threshold in either parameter. No claim is made for odd grid orders.

## Proof
**1. Endpoint-driven alternating Fourier tail.** Put \(f(\theta)=e^{-t\theta^\alpha}\) for \(0\le\theta\le\pi\). For \(\alpha>1\), \(f'(0)=0\), and \(f'\) is absolutely continuous: near zero,
\[
f''(\theta)=t\alpha\theta^{\alpha-2}e^{-t\theta^\alpha}
\bigl[t\alpha\theta^\alpha-(\alpha-1)\bigr]
\]
is integrable because \(\alpha-2>-1\). Integration by parts twice, valid for every integer \(m\ge1\), gives
\[
b_m=\frac{(-1)^m f'(\pi)}{\pi m^2}
-\frac1{\pi m^2}\int_0^\pi f''(\theta)\cos(m\theta)\,d\theta.
\]
The Riemann--Lebesgue lemma and \(f'(\pi)=-t\alpha\pi^{\alpha-1}e^{-t\pi^\alpha}\) therefore yield
\[
\boxed{b_m=\frac{(-1)^{m+1}t\alpha\pi^{\alpha-2}e^{-t\pi^\alpha}}{m^2}
+o_{\alpha,t}(m^{-2}).}\tag{1}
\]
The coefficient of \(m^{-2}\) is strictly positive in magnitude. Hence there is a finite integer \(M=M(\alpha,t)\) such that each \(m\ge M\) has \(\operatorname{sign}b_m=(-1)^{m+1}\). Consequently the two exceptional sets defining \(J_{\alpha,t}\) are finite. The estimate also gives absolute Fourier summability \(\sum_{m\in\mathbb Z}|b_{|m|}|<\infty\).

**2. Aliasing on the even cycle.** The absolutely convergent Fourier series of the continuous periodic function \(\theta\mapsto f(d_{\mathbb S^1}(\theta,0))\) represents its sampled values. The circulant eigenvalue in frequency \(k\in\{0,\ldots,N-1\}\) is therefore exactly
\[
\Lambda_{N,k}=N\sum_{j\in\mathbb Z}b_{|k+jN|}.\tag{2}
\]
This is an absolutely convergent identity. When \(N\) is even, every integer \(k+jN\) has the same parity as \(k\). For \(M\le k\le N-M\), all indices on the right of (2) have magnitude at least \(M\), so **every summand has the strict sign** \((-1)^{k+1}\). The constant-frequency eigenvalue \(\Lambda_{N,0}\) is strictly positive because every matrix entry is strictly positive.

For each fixed \(1\le k<M\), absolute summability and the \(O(m^{-2})\) tail imply \(\Lambda_{N,k}/N=b_k+O_{\alpha,t}(N^{-2})\). If \(b_k\ne0\), its eigenvalue eventually has the sign of \(b_k\). If \(b_k=0\), every nonzero alias in (2) has magnitude at least \(N-k\); once \(N-k\ge M\), its sign is \((-1)^{k+1}\), so the sum is strictly of baseline sign. The mirror mode \(N-k\) has exactly the same eigenvalue. This exhausts every frequency and proves eventual nonsingularity.

The baseline parity signs assign negative eigenvalues to precisely the nonzero even frequencies, numbering \(N/2-1\). For each exceptional positive even coefficient, the two modes \(k,N-k\) replace two negatives by positives; for each exceptional negative odd coefficient, they replace two positives by negatives. This proves the exact eventual index formula with correction \(2J_{\alpha,t}\), and hence its half-negative limiting density.

**3. Exact signature for every even size under weak damping.** If
\[
0<t\le(\alpha-1)/(\alpha\pi^\alpha),
\]
then \(f''(\theta)\le0\) throughout \((0,\pi)\), and \(h(\theta)=-f''(\theta)>0\) except possibly at the endpoint. A second integrated identity is
\[
b_m=\frac1{\pi m^2}\int_0^\pi
h(\theta)\bigl[\cos(m\theta)-(-1)^m\bigr]d\theta.\tag{3}
\]
Indeed, integrate \(\int f\cos(m\theta)\) first by parts, then write \(-f'(\theta)=\int_0^\theta h(u)du\); the inner integral \(\int_u^\pi\sin(m\theta)d\theta\) equals \((\cos(mu)-(-1)^m)/m\). For odd \(m\), the bracket in (3) is \(1+\cos(m\theta)\ge0\) and not almost everywhere zero; for even \(m\), it is \(\cos(m\theta)-1\le0\) and not almost everywhere zero. Thus
\[
\operatorname{sign} b_m=(-1)^{m+1}\quad\text{for every }m\ge1.\tag{4}
\]
For every even \(N\) and each nonzero Fourier index \(k\), formula (2) is a sum of nonzero same-parity harmonics, all of the strict sign \((-1)^{k+1}\). Frequency zero remains strictly positive. There are \(N/2\) odd indices, \(N/2-1\) nonzero even indices, and the one zero-frequency index. This proves the all-size signature, including \(N=2\). \(\square\)

## Verification
The included `verify.py` evaluates eigenvalues directly by a real discrete Fourier sum, independently counts their signs, and compares the weak-damping signatures to the stated exact counts for several real and integral powers. It also evaluates the even-grid inertia for fixed damping outside the concavity interval and compares selected larger-grid counts with direct quadrature signs of low continuum Fourier coefficients. This test is numerical corroboration, not certification of all sizes or parameters. The infinite statements rely on the absolute continuity, Riemann--Lebesgue, and exact Fourier alias arguments above.

## Relationship to prior work
Da Costa, Mostajeran and Ortega [1] prove that the intrinsic Gaussian is not positive definite on the entire circle at any positive damping and exhibit a negative Fourier eigenvalue on a sufficiently fine cyclic sample; they do not classify the **number** of negative directions at all even sizes or supply the fixed-damping index correction. Feragen, Lauze and Hauberg [2] establish general geometric obstructions to all-scale geodesic Gaussian positivity, without counting negative Fourier modes. Gneiting [3] describes powered exponential covariance families and the positive definite regime of exponent at most one, but not the indefinite inertia law above exponent one. Available published finite-cycle investigations [4,5] determine the damping scale at which all eigenvalues finally become positive as cycle size changes; that is a different limit from the fixed \((\alpha,t)\) half-negative law and does not yield the universal all-size weak-damping signature. The proof uses standard Fourier aliasing and integration by parts, but the quantified complete inertia conclusions for the powered geodesic family are distinct from existence of a single negative witness.

## Limitations
The weak-damping interval is rigorously sufficient and may not be optimal. For arbitrary damping, the exact finite correction \(J_{\alpha,t}\) is defined by finitely many continuum Fourier signs rather than a closed elementary formula; the eventual grid cutoff is not explicitly computed. Very small negative eigenvalues may be missed by ordinary floating-point experiments. Only even equispaced grids are covered, and the proof does not establish anything for other sampling sets or for powers at most one. Historical priority has been compared against accessible primary papers and published related findings; equivalent statements in older, difficult-to-access periodization literature remain a risk. No independent mathematical audit has been performed.

## References
1. N. Da Costa, C. Mostajeran, J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (first public 2023-02-21), https://arxiv.org/abs/2302.10623.
2. A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (2014), https://arxiv.org/abs/1411.0296.
3. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (2011), https://arxiv.org/abs/1111.7077.
4. *A sharp \(\pi/n\) last-failure scale for geodesic Gaussian matrices on finite cycles*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-pi-n-last-failure-scale-for-geodesic-gaussian-matrices-o--6597725d7d73.
5. *The sharp \(\pi/N\) Gaussian covariance transition on discrete circles*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-sharp-pi-n-gaussian-covariance-transition-on-discrete-circle--07cd4e63f039.
