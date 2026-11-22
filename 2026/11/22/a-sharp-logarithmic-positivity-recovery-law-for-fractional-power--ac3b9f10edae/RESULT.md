# A sharp logarithmic positivity-recovery law for fractional powered-exponential kernels on finite cycles

## Finding

**Theorem.** Fix any real \(1<p<2\). For \(N\in4\mathbb N\), let the cycle distance on \(\mathbb Z/N\mathbb Z\) be
\[d_N(j,k)=\min\{|j-k|,N-|j-k|\}\]
and define the real symmetric circulant matrix
\[K_{N,t,p}(j,k)=\exp\bigl(-t\,d_N(j,k)^p\bigr),\qquad t>0.\]
Define the **last-failure parameter**
\[T_N(p)=\sup\{t>0:\lambda_{\min}(K_{N,t,p})<0\},\]
using zero for the empty set. The set is bounded for every \(N\), and it is nonempty for all sufficiently large \(N\in4\mathbb N\). Its sharp asymptotic is
\[\boxed{\displaystyle\lim_{\substack{N\to\infty\\4\mid N}}\frac{N^pT_N(p)}{\log N}=2^p(p-1).}\]
More explicitly, for every \(a>2^p(p-1)\), all large admissible \(N\) yield strictly positive definite \(K_{N,t,p}\) **simultaneously for every** \(t\ge a\log N/N^p\). For every \(0<a<2^p(p-1)\), the matrix at \(t=a\log N/N^p\) has a strictly negative eigenvalue at its Nyquist Fourier frequency.

There is an exact-order local crossover. Put \(M=N/2\), \(C_p=2\eta(-p)>0\), with \(\eta(s)=(1-2^{1-s})\zeta(s)\) by analytic continuation. For fixed \(h\in\mathbb R\), set
\[t_M(h)=\frac{(p-1)\log M+h}{M^p}.\]
For sufficiently large \(M\), this is positive, and the Nyquist eigenvalue satisfies
\[\boxed{\displaystyle\lim_{\substack{M\to\infty\\2\mid M}}\frac{\lambda_M(t_M(h))}{t_M(h)}=C_p-\frac p2e^{-h}.}\]
Thus the Nyquist eigenvalue crosses from negative to positive across the fixed-order window centered at \(h=\log(p/(2C_p))\); this does **not** assert that the Nyquist mode alone determines the finite-matrix last-failure threshold at this finer order.

## Assumptions and scope

The dimension is one (cycle geometry), the vertex count is a multiple of four, and the exponent is fixed strictly between one and two. The distance is the integer-edge shortest-path distance, **not** the chordal or angular distance with circumference normalized to a fixed constant. No uniformity is asserted as \(p\downarrow1\) or \(p\uparrow2\). The limit concerns positive semidefiniteness of the full circulant Gram matrix, not validity of a continuum geodesic covariance on the circle.

## Proof

**1. Fourier reduction and the stable reference.** Write \(N=2M\) with \(M\) even and \(f_t(x)=e^{-t x^p}\) for nonnegative real \(x\). Let \(\theta_k=\pi k/M\), \(0\le k<N\). Circulant diagonalization gives
\[\lambda_k(t)=1+2\sum_{j=1}^{M-1}f_t(j)\cos(j\theta_k)+(-1)^k f_t(M).\]
Compare this with the absolutely convergent infinite-lattice Fourier series
\[F_t(\theta)=\sum_{j\in\mathbb Z}e^{-t|j|^p}e^{ij\theta}.\]
Let \(q_t\) be the density whose real Fourier transform is \(e^{-t|\xi|^p}\). Since \(0<p<2\), symmetric-stable density bounds give a constant \(c_p>0\) such that
\[q_t(x)\ge c_p\frac{t}{(t^{1/p}+|x|)^{1+p}}\qquad(t>0,\ x\in\mathbb R).\]
Poisson summation yields \(F_t(\theta)=2\pi\sum_{m\in\mathbb Z}q_t(\theta+2\pi m)\), so, for \(0<t\le2\) and \(0\le\theta\le\pi\),
\[F_t(\theta)\ge c'_p\frac{t}{(t^{1/p}+\theta)^{1+p}}.\tag{1}\]
In particular, this lower bound is of order \(t^{-1/p}\) near zero and at least a constant multiple of \(t\theta^{-1-p}\) when \(\theta\ge t^{1/p}\). The stated stable density bound is standard (see Bae–Kang–Kim–Lee and their cited stable-like heat-kernel estimate); it is a premise external to this proof, not an unverified numerical inference.

**2. Exact wrap-error bound.** For \(k\not\equiv0\pmod N\), put \(z=e^{i\theta_k}\). The Fourier grid identity \(e^{iM\theta_k}=(-1)^k\) gives
\[\lambda_k(t)-F_t(\theta_k)=(-1)^k\left(f_t(M)-2\operatorname{Re}\sum_{\ell\ge0}f_t(M+\ell)z^\ell\right).\tag{2}\]
Let \(d_\ell=f_t(M+\ell)-f_t(M+\ell+1)\). Elementary summation by parts and \(\operatorname{Re}(1-z)^{-1}=1/2\) yield the **exact** identity
\[\lambda_k(t)-F_t(\theta_k)=2(-1)^k\operatorname{Re}\left[\frac{z}{1-z}\sum_{\ell\ge0}d_\ell z^\ell\right].\tag{3}\]
For \(tM^p\to\infty\) the function \(f_t\) is convex on \([M,\infty)\), hence \(d_\ell\) is nonnegative, nonincreasing and tends to zero. Applying the Dirichlet bound to its series and the mean-value estimate for \(d_0\),
\[|\lambda_k(t)-F_t(\theta_k)|\le C_p\frac{tM^{p-1}e^{-tM^p}}{\theta_k^2},\qquad0<\theta_k\le\pi.\tag{4}\]
A separate absolute-tail estimate, using \(x^p\ge M^p+pM^{p-1}(x-M)\) for \(x\ge M\), gives
\[|\lambda_k(t)-F_t(\theta_k)|\le C_p e^{-tM^p}\left(1+\frac{M}{tM^p}\right).\tag{5}\]
Both estimates are valid uniformly when \(0<t\le2\) and \(tM^p\) exceeds a sufficiently large fixed threshold depending on \(p\). At frequency zero the eigenvalue is a sum of strictly positive entries, so it needs no error bound.

**3. Uniform high-parameter positivity.** Fix \(a>2^p(p-1)\) and assume \(t\ge a\log N/N^p\), with \(t\le2\). Write \(A=tM^p\), so \(A\ge(a/2^p)\log N\). For \(0<\theta_k<t^{1/p}\), (1) and (5) give the relative error
\[\frac{|\lambda_k-F_t(\theta_k)|}{F_t(\theta_k)}\le C_p e^{-A}\left(t^{1/p}+A^{(1-p)/p}\right)=o(1).\]
For \(t^{1/p}\le\theta_k\le\pi\), (1) and (4) yield
\[\frac{|\lambda_k-F_t(\theta_k)|}{F_t(\theta_k)}\le C_p M^{p-1}e^{-A}\theta_k^{p-1}=o(1).\]
Both errors tend to zero **uniformly in all** such \(t\) and nonzero frequency indices because \(a/2^p>p-1\). Thus every eigenvalue is strictly positive when \(N\) is large. For \(t\ge2\), Gershgorin gives
\[\lambda_k(t)\ge1-2\sum_{j\ge1}e^{-2j^p}\ge1-\frac{2}{e^2-1}>0,\]
so positivity holds for the entire half-line of parameters.

**4. Negative Nyquist direction and the constant.** Take any \(0<a<2^p(p-1)\) and \(t=a\log N/N^p\). At \(k=M\), \(\theta_M=\pi\) and \((-1)^M=1\). Formula (3) becomes
\[\lambda_M(t)-F_t(\pi)=-\sum_{\ell\ge0}(-1)^\ell d_\ell.\tag{6}\]
The derivatives \(f_t''>0\) and \(f_t^{(3)}<0\) on \([M,\infty)\) for large \(N\) because \(tM^p\asymp\log N\to\infty\). Hence \(b_\ell=d_\ell-d_{\ell+1}\) is nonnegative and decreasing, and the alternating-series identity
\[2\sum_{\ell\ge0}(-1)^\ell d_\ell-d_0=\sum_{\ell\ge0}(-1)^\ell b_\ell\]
implies \(\sum(-1)^\ell d_\ell=d_0/2+O(b_0)\). Direct differentiation yields \(b_0/d_0=O(\log N/N)\), while
\[d_0\sim ptM^{p-1}e^{-tM^p}.\]
By the stable-density Fourier representation and the small-time stable-density tail, \(F_t(\pi)/t\to C_p=2\eta(-p)>0\) as \(t\downarrow0\). Consequently
\[\frac{\lambda_M(t)}t=C_p-\frac p2 M^{p-1}e^{-tM^p}(1+o(1))+o(1).\tag{7}\]
Since \(M^{p-1}e^{-tM^p}=M^{p-1-a/2^p}\,2^{-a/2^p}\to\infty\), the eigenvalue is negative for every sufficiently large \(N\). The upper and lower parts establish the stated limit for \(T_N(p)\).

**5. Critical Nyquist window.** Substitute \(t=((p-1)\log M+h)/M^p\) in (7). Then \(M^{p-1}e^{-tM^p}=e^{-h}\), proving the second displayed limit. Positivity of \(C_p\) follows from the positive stable density, or from \(\eta(-p)=(1-2^{1+p})\zeta(-p)>0\) for \(1<p<2\).

## Verification

The companion `verify.py` computes every Fourier eigenvalue of finite circulant matrices and compares the Nyquist eigenvalue with the analytic critical-window limit. It executed 48 supplementary sign checks for \(p\in\{1.2,1.5,1.8\}\), cycle sizes \(N\in\{256,512,1024,2048\}\), and widely separated parameter multipliers, as well as 24 high-precision crossover evaluations. All completed without assertion failures. Numerical sampling is not used to prove either the uniform-in-time assertion or the infinite-size limit; those follow from steps 1–5.

## Relationship to prior work

Huang–Li [1] analyze circular Matérn covariance and its finite-grid conditional autoregressive approximation, emphasizing that simply transplanting Euclidean covariance functions to circles can fail. Their finite-grid Fourier formulas involve rational cosine spectra, not the graph-distance powered exponential matrix or its last-failure scaling. Bae–Kang–Kim–Lee [2] study two-sided jump heat-kernel bounds, supplying the stable comparison that underlies (1), but not the finite-cycle reflection error. A published result on **squared** geodesic Gaussian kernels has an order-\(N^{-1}\) last-failure threshold with constant \(\pi\). That result does not imply the present fractional-power \((\log N)/N^p\) transition: the stable reference spectrum has a nonzero order-\(t\) tail for every fixed \(p<2\), a tail which disappears at \(p=2\). The present claim is a combined sharp threshold, all-larger-parameters guarantee, and exact critical Nyquist scaling for strictly fractional exponents.

## Limitations

The theorem is restricted to cycles of size divisible by four. It makes no claim for odd cycle sizes, other even congruence classes, or uniform limits as the exponent approaches the endpoints. The finer critical-window statement concerns **one eigenvalue**, not the exact finite-size last-failure value beyond leading order. The outside stable-density estimate is a classical input; no independent priority certification is claimed. A broader literature source not discovered in the comparisons could affect historical originality, although it would not change the proof.

## References

[1] C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856v1 (first public 2022-01-30), https://arxiv.org/abs/2201.12856.

[2] J. Bae, J. Kang, P. Kim, and J. Lee, *Heat kernel estimates for symmetric jump processes with mixed polynomial growths*, arXiv:1804.06918v1 (first public 2018-04-18), https://arxiv.org/abs/1804.06918. See introduction formula (1.3) and its cited stable-like estimate.
