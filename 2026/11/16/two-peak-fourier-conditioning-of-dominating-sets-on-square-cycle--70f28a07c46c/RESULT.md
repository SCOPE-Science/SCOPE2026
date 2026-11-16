# Two-peak Fourier conditioning of dominating sets on square cycles

## Finding
For every integer \(n\geq3\), sample uniformly from the dominating vertex sets of the square \(C_n^2\) of the labelled cycle (where cyclic distance at most two defines adjacency). Write \(X_j\in\{0,1\}\) for membership at site \(j\), and let \(K_n=(\operatorname{Cov}(X_i,X_j))_{0\leq i,j<n}\). Then \(K_n\) is positive definite for every \(n\), and all its eigenvalues are given exactly by the five-state transfer formula in the next section.

Let \(t\) be the unique root in \((0,1)\) of
\[
 t+t^2+t^3+t^4+t^5=1,
\]
and put \(\mu=\sum_{j=1}^{5}j t^j\), \(\rho=1/\mu\). Define polynomials \(P,Q\) by
\[
\begin{aligned}
P(x)={}&4t^3(t+1)-4(t^2-t+1)(t^2+t-1)x\\
 &-8(t-1)(t^3+2t^2+t-1)x^2+16(2t-1)x^3,\\
Q(x)={}&-2(3t^4+2t^3-t^2-1)\\
 &+4(3t^4+4t^3+2t^2+4t-3)x+8t(4t^3+3t^2-1)x^2\\
 &-16(t^4+2t^3+2t^2+4t-3)x^3\\
 &-32(t^4+t^3+t^2+t-1)x^4.
\end{aligned}
\]
The exact Fourier eigenvalue at mode \(k\) converges, uniformly over \(0\leq k<n\), to
\[
 S(2\pi k/n)=\rho\frac{P(\cos(2\pi k/n))}{Q(\cos(2\pi k/n))},
\qquad \sup_{0\leq k<n}|\lambda_{n,k}-S(2\pi k/n)|\longrightarrow0.
\]
The positive profile \(S\) has **exactly two strict interior local maxima** as a function of \(\theta\in[0,\pi]\). Its unique global maximum on that interval occurs at \(\theta_*=\arccos(x_*)\), where \(x_*\in(0.218869,0.218871)\) is the unique root there of \(P'Q-PQ'\). Its unique global minimum occurs at \(\theta=0\). The other interior maximum occurs at cosine in \((-0.829815,-0.829814)\) and is strictly smaller.

Consequently, with \(\kappa_n=\lambda_{\max}(K_n)/\lambda_{\min}(K_n)\),
\[
\boxed{\lim_{n\to\infty}\kappa_n=\frac{P(x_*)Q(1)}{Q(x_*)P(1)}=1.479580816665\ldots.}
\]
The strongest asymptotic harmonic has angular frequency \(\theta_*=1.350140478835\ldots\), rather than alternating frequency \(\pi\).

## Assumptions and scope
The cycle is simple for \(n\geq3\), and all nonempty dominating sets receive equal mass (no fugacity or size conditioning). Its square has edges between distinct vertices at cyclic distance one or two. A set dominates precisely when every cyclic block of five positions contains a selected vertex. In particular, this is the condition that its indicator word has no five consecutive cyclic zeros, also for \(3\leq n<5\) with repeated indices interpreted cyclically. These conventions are essential. Eigenvalues refer to the unscaled covariance (equivalently, the probability-normalized Gram of centered coordinate indicators); the ratio is the squared-energy condition number, not its square root. The theorem concerns the complete finite spectrum via a fixed-size matrix formula and its limiting extrema; it does not assert that the exact maximizing finite Fourier index is unique.

## Proof
**1. Exact finite covariance.** Let \(M\) be the \(5\times5\) matrix with state indices \(r=0,1,2,3,4\):
\[
 M_{r,0}=1\ (0\leq r\leq4),\qquad M_{r,r+1}=1\ (0\leq r\leq3),
\]
all other entries being zero. State \(r\) records the number of consecutive zeros after the latest selected vertex; a transition to state zero writes a one, and a transition to state \(r+1\) writes a zero. Since the all-zero word has no closed state path, a closed path of length \(n\) corresponds bijectively to an allowed cyclic word. Put
\[
 Z_n=\operatorname{tr}(M^n),\quad a_n=(M^n)_{0,0},\quad b_{n,j}=(M^j)_{0,0}(M^{n-j})_{0,0}.
\]
Then \(\Pr(X_0=1)=a_n/Z_n\) and \(\Pr(X_0=X_j=1)=b_{n,j}/Z_n\), for \(0\leq j<n\), where \(j=0\) correctly gives the one-point moment. Translation invariance makes the covariance circulant; therefore its **complete exact spectrum**, including multiplicities indexed by \(k\), is
\[
\boxed{\lambda_{n,k}=\sum_{j=0}^{n-1}
 \left(\frac{b_{n,j}}{Z_n}-\frac{a_n^2}{Z_n^2}\right)e^{-2\pi i kj/n},\qquad0\leq k<n.}
\]
The result is real because the covariance is symmetric. Every all-one word and every word obtained from it by changing exactly one coordinate to zero occurs with positive probability. If a real linear combination of coordinates had zero variance, its evaluations on these \(n+1\) affinely spanning words would force all coefficients to vanish. Thus \(K_n\) is positive definite.

**2. Infinite-volume renewal limit.** The matrix \(M\) is primitive: its directed state graph is strongly connected and has a self-loop at zero. Its Perron root \(\Lambda\) is the unique real number greater than one satisfying \(\Lambda^5=\Lambda^4+\Lambda^3+\Lambda^2+\Lambda+1\), so \(\Lambda=t^{-1}\). The Perron-chain law between successive selected sites has independent gaps \(G\in\{1,2,3,4,5\}\) with \(\Pr(G=j)=t^j\): along each path from reset to reset, the Doob-transform eigenvector factors telescope and leave \(\Lambda^{-j}\); their sum is one. The renewal density is \(\rho=1/\mathbb E G=1/\mu\).

Let \(u_d\) denote the probability of a renewal at displacement \(d>0\) given a renewal at zero. Its generating function is
\[
 \sum_{d\geq1}u_d z^d=\frac{\phi(z)}{1-\phi(z)},\qquad
 \phi(z)=\sum_{j=1}^{5}t^j z^j.
\]
The stationary indicator covariance is \(c(0)=\rho-\rho^2\) and \(c(d)=\rho u_d-\rho^2\) for \(d\ne0\), with reflection at negative displacements. Positivity and aperiodicity of the five gap probabilities imply exponentially fast renewal convergence \(u_d\to\rho\), e.g. by the rational generating function and separation of its other poles from the unit circle. Fourier transformation yields, away from angular frequency zero,
\[
 S(\theta)=\rho\frac{1-|\phi(e^{i\theta})|^2}{|1-\phi(e^{i\theta})|^2}.
\]
Both numerator and denominator have a factor \(1-\cos\theta\). Cancelling it and reducing powers of \(t\) by its defining polynomial produces exactly \(\rho P(\cos\theta)/Q(\cos\theta)\), including its continuous value at \(\theta=0\); the algebraic identities are reproduced in `verify_symbolic.py`. The denominator is strictly positive on \([-1,1]\): for \(\theta\ne0\), it comes from \(|1-\phi(e^{i\theta})|^2/(1-\cos\theta)>0\), while its removable endpoint value is \(Q(1)>0\). The numerator is also positive by the strict inequality \(|\phi(e^{i\theta})|<1\) for \(\theta\not\equiv0\), and at zero by \(S(0)=\rho\operatorname{Var}(G)/\mu^2>0\).

The Perron decomposition of \(M\), with non-Perron spectral radius strictly below \(\Lambda\), compares cyclic two-point probabilities to their stationary counterparts by an error exponentially small in the shorter complementary arc. Splitting displacements at \(n/2\), then summing the Fourier series and its exponentially decaying tails, gives \(\sup_k|\lambda_{n,k}-S(2\pi k/n)|=O(n\eta^{n/2})\) for some \(\eta\in(0,1)\). In particular the Fourier extrema converge to the extrema of the continuous positive profile \(S\).

**3. Exact peak count and ordering.** Set \(R(x)=P'(x)Q(x)-P(x)Q'(x)\), reducing coefficient powers of \(t\) modulo \(t^5+t^4+t^3+t^2+t-1\). Its degree is six; its seven coefficients are listed and checked in `verify_symbolic.py` and `verify.py`. The defining root lies rigorously in the rational interval
\[
 \frac{508660391641}{10^{12}}<t<\frac{508660391643}{10^{12}}.
\]
For \(H(y)=(1+y)^6R((y-1)/(y+1))\), exact rational interval evaluation gives the coefficient signs from constant to degree six as
\[
 (+,-,-,+,+,+,-).
\]
Descartes' rule therefore bounds the number of roots of \(R\) in \((-1,1)\), including multiplicity, by three. The signs of \(R\) at the endpoints of each of the three disjoint rational intervals
\[
 \left(-\frac{829815}{10^6},-\frac{829814}{10^6}\right),\quad
 \left(-\frac{353447}{10^6},-\frac{353446}{10^6}\right),\quad
 \left(\frac{218869}{10^6},\frac{218871}{10^6}\right)
\]
are opposite. Hence there are **exactly three simple interior critical points**, with no others. Their order and derivative signs make the first and third local maxima and the middle one a local minimum. Exact rational interval evaluation of \(P/Q\) at the three intervals and \(x=\pm1\) proves the third critical point is uniquely highest and \(x=1\) is uniquely lowest. The same certificate proves
\[
 1.479577768<\frac{P(x_*)Q(1)}{Q(x_*)P(1)}<1.479583866.
\]
The narrow high-precision value stated above follows by root isolation. Full exact rational calculations, including all Descartes signs, endpoint comparisons and the strict peak ordering, are implemented in the standalone `verify.py`. This completes the proof.

## Verification
Run `python verify.py` and `python verify_symbolic.py` in the directory containing these files. The first uses Python's standard library only and checks exact enumeration against transfer matrix formulas for each \(3\leq n\leq14\), exact rational interval peak certificates, and numerical convergence of every Fourier eigenvalue along five larger cycle lengths. The second uses SymPy and checks three exact polynomial identities modulo the defining quintic. These finite checks supplement, but do not replace, the all-length arguments and the exact rational root certificate.

## Relationship to prior work
Galvin and Zhang (arXiv:2408.12731, first posted 2024-08-22) prove unimodality and cardinality recurrences for dominating sets of powers of paths and cycles, thereby motivating the square-cycle ensemble. Earlier work of Beaton and Brown (arXiv:2012.11813) and Arocha and Llano (arXiv:1601.01268) treats domination counts for ordinary cycles. The general renewal diffraction formalism and its continuous spectra are established by Baake and Koesters (arXiv:1007.3084). Those results supply context and general renewal tools: the claimed additional content here is the finite square-cycle covariance spectrum, uniform finite-to-infinite Fourier convergence, and the certified two-local-peak classification and sharp limiting condition number for the specific five-gap weights. No novelty is claimed for the general renewal transform formula or for domination counting recurrences.

## Limitations
No finite-length closed trigonometric formula for the location of an extremal discrete index is asserted; the exact finite spectrum is computable from a five-state transfer matrix, and the sharp extremal statement is asymptotic. The numerical decimal is not a standalone exact certificate: the algebraic root isolation is. The claim does not extend without new analysis to other powers, weighted domination laws, or noncyclic boundary conditions. Historical priority remains provisional, especially for an earlier exact specialization of a renewal diffraction result to the five-gap law. No independent mathematical audit has been performed.

## References
1. D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731v1, first public 2024-08-22, https://arxiv.org/abs/2408.12731.
2. I. Beaton and J. I. Brown, *On the Unimodality of Domination Polynomials*, arXiv:2012.11813v1, first public 2020-12-22, https://arxiv.org/html/2012.11813v1.
3. J. L. Arocha and B. Llano, *The number of dominating \(k\)-sets of paths, cycles and wheels*, arXiv:1601.01268, first public 2016-01-06, https://arxiv.org/abs/1601.01268.
4. M. Baake and H. Koesters, *Random point sets and their diffraction*, arXiv:1007.3084, first public 2010-07-19, https://arxiv.org/abs/1007.3084.
