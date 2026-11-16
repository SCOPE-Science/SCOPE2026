# Perrin–Padovan Fourier sampling on maximal independent sets of cycles

## Finding
Let \(\mathcal M_n\) be the family of all **inclusion-maximal** independent sets of the labelled cycle \(C_n\), \(n\ge3\), sampled uniformly. Write \(X_j(I)=\mathbf1_{j\in I}\), and let \(K_n\) be the covariance matrix of \((X_0,\ldots,X_{n-1})\). Equivalently, the centered first-coordinate Walsh functions \(\chi_j(I)=(-1)^{X_j(I)}\) have Gram matrix \(4K_n\).

Define integer sequences by \(a_0=1\), \(a_1=0\), \(a_2=1\), and \(a_d=a_{d-2}+a_{d-3}\) for \(d\ge3\); let \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_d=P_{d-2}+P_{d-3}\) for \(d\ge3\). Then \(|\mathcal M_n|=P_n\), and the **complete exact Fourier covariance spectrum** is
\[
\boxed{\lambda_{n,k}=\frac{1}{P_n}\sum_{d=0}^{n-1}a_da_{n-d}\cos\!\left(\frac{2\pi kd}{n}\right)-\mathbf1_{k=0}\,n\left(\frac{a_n}{P_n}\right)^2,\quad k=0,\ldots,n-1.}
\]
The complete rank classification is
\[
\boxed{\operatorname{rank}K_n=\begin{cases}2&n=3,\\1&n=4,\\4&n=5,6,\\6&n=7,\\n&n\ge8.\end{cases}}
\]
Thus **every** centered first-coordinate Walsh frequency is identifiable exactly from cycle order eight onward. At order six, unlike every other noninjective case, the nullspace has **nonconstant** Fourier modes \(k=1,5\); its nonzero eigenvalues are \(1/25,2/5,2/5,3/5\).

Let \(\alpha\) denote the unique positive real root of \(\alpha^3=\alpha+1\), and set
\[
 A=\alpha^{-2},\quad B=\alpha^{-3}=1-A,\quad p=(2A+3B)^{-1},\quad Q(x)=1+A^2+(4-2A)x+4Bx^2.
\]
There is **uniform** convergence over the entire discrete Fourier grid,
\[
\lambda_{n,k}=\frac{pAB}{Q(\cos(2\pi k/n))}+O(n\alpha^{-3n/2}).
\]
The limiting least-variance mode is the zero spatial frequency, while the largest-variance modes approach \(\theta_*\) and \(2\pi-\theta_*\), where
\[
\cos\theta_*=-\frac{2-A}{4B}\in(-1,0).
\]
In particular, the sharp squared-frame-bound condition ratio has the nontrivial exact limit
\[
\boxed{\lim_{n\to\infty}\frac{\lambda_{\max}(K_n)}{\lambda_{\min}(K_n)}=\frac{Q(1)}{Q(-(2-A)/(4B))}=43.42455574592406\ldots.}
\]
Unlike the full independent-set ensemble, the greatest-variance asymptotic spatial frequency is **not** the alternating frequency. The limit is for \(n\ge8\), where all eigenvalues are positive.

## Assumptions and scope
The cycle is simple with vertices indexed modulo \(n\). A set is inclusion-maximal if it is independent and dominates all vertices omitted from it; it need not be of maximum cardinality. The measure assigns equal probability to **each labelled maximal independent set**, not to graph-automorphism orbits, not to random-greedy outputs, and not to all independent sets. The expectation inner product is probability-normalized; the squared condition ratio is unchanged by the factor four relating occupation indicators to centered Walsh characters. Every bound is stated for all integers in its indicated range; asymptotic error constants are independent of \(k\).

## Proof
**1. Transfer encoding and exact two-point moments.** A cyclic binary indicator belongs to \(\mathcal M_n\) exactly when it contains neither adjacent ones nor three consecutive zeros. Encode admissible consecutive-bit states by \(00,01,10\). Their transition matrix, in this order, is
\[
T=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}.
\]
The trace \(\operatorname{tr}(T^n)\) counts the cyclic words exactly; the characteristic polynomial is \(t^3-t-1\), so this trace equals \(P_n\). A return from state \(01\) to itself takes successive steps of length two or three, hence \((T^d)_{01,01}=a_d\), including \(d=0\). Let \(E\) project onto state \(01\). For every \(0\le d<n\), the occupation event at sites zero and \(d\) is counted by
\[
\operatorname{tr}(ET^dET^{n-d})=(T^d)_{01,01}(T^{n-d})_{01,01}=a_da_{n-d}.
\]
Therefore \(\mathbb E X_0=a_n/P_n\), \(\mathbb E X_0X_d=a_da_{n-d}/P_n\). The covariance is circulant, and its discrete Fourier diagonalization gives exactly the displayed formula, with the centering correction affecting only \(k=0\). Centered Walsh functions are minus twice the centered occupations.

**2. Exact injectivity threshold.** If \(\sum_j b_jX_j\) is constant on \(\mathcal M_n\), choose any site \(i\), two consecutive gaps of lengths \(2,3\) between selected sites \(i\) and \(i+5\), and interchange these gaps. The configurations have identical selected vertices except at \(i+2\) versus \(i+3\), so their constant linear statistic forces \(b_{i+2}=b_{i+3}\). This comparison is feasible when \(n=5\) (the endpoints coincide) or for \(n\ge7\), since each integer \(n-5\ge2\) is a sum of twos and threes and supplies the remaining cyclic gaps. Varying \(i\) shows that **every** such constant linear statistic has constant coefficients. Consequently the covariance kernel on these orders is either zero or precisely the constant line.

Every maximal independent set has cyclic gaps of length two or three; its cardinality is the number of those gaps. At \(n=5\) and \(n=7\) all maximal independent sets have the same size, giving one constant null direction. At even \(n\ge8\), one gap decomposition uses only twos and another replaces three twos by two threes; at odd \(n\ge9\), a decomposition uses one three and the rest twos and a second uses three more twos replaced by two threes. The resulting cardinalities differ, so the constant direction is **not** null and \(K_n\) is positive definite for every \(n\ge8\).

The remaining sizes are direct: \(\mathcal M_3\) consists of the three singleton sets, so rank is two; \(\mathcal M_4\) consists of the two alternating sets, so rank is one. At \(n=6\), the five maximal independent sets are the two alternating triples and the three opposite pairs, whose affine span has dimension four. Its Fourier eigenvalues, from the exact formula, are \((1/25,0,2/5,3/5,2/5,0)\). The rank of a covariance matrix with a positive mass at each support point equals the affine dimension of that support. The complete rank classification follows.

**3. Renewal spectral limit, with a uniform finite-size bound.** Let \(\beta,\bar\beta\) be the other two roots of \(t^3-t-1\). Their moduli are \(\alpha^{-1/2}\), hence \(\rho=|\beta|/\alpha=\alpha^{-3/2}<1\). The simple-root expansions of the two recurrences yield
\[
P_n=\alpha^n(1+O(\rho^n)),\qquad a_d=\alpha^d(p+O(\rho^d)),
\]
where the leading coefficient of the second expansion is \(p=(2\alpha^{-2}+3\alpha^{-3})^{-1}\), the residue at the simple pole of \((1-Az^2-Bz^3)^{-1}\) at \(z=1\). Write \(u_d=a_d\alpha^{-d}\) and \(c_d=p(u_d-p)\). Then \(|c_d|=O(\rho^d)\). The finite covariance row equals \(p(1-p)+O(\rho^n)\) at displacement zero and \(c_d+c_{n-d}+O(\rho^n)\) for all \(1\le d<n\). Therefore its complete Fourier transform differs by at most \(O(n\rho^n)\) from the absolutely convergent continuous spectral density
\[
S(\theta)=p(1-p)+2\sum_{d=1}^{\infty}c_d\cos(d\theta).
\]
This bound is **uniform in every** \(k\), including \(k=0\).

Set \(\phi(z)=Az^2+Bz^3\). The renewal generating function is \(\sum_{d\ge0}u_dz^d=(1-\phi(z))^{-1}\), initially for \(|z|<1\). Summing the absolutely convergent centered sequence and using an Abel limit on the unit circle gives, for \(\theta\ne0\),
\[
S(\theta)=p\frac{1-|\phi(e^{i\theta})|^2}{|1-\phi(e^{i\theta})|^2}.
\]
Writing \(x=\cos\theta\), elementary trigonometric expansion gives \(1-|\phi|^2=2AB(1-x)\) and \(|1-\phi|^2=2(1-x)Q(x)\). Thus \(S=pAB/Q(x)\) away from zero and, by continuity, also at zero. This supplies the asserted uniform limit without treating a finite enumeration as an infinite proof.

**4. Sharp extremal frequency and condition constant.** The polynomial \(Q\) is strictly convex because \(B>0\). Its unique minimum on \([-1,1]\) occurs at \(x_*=-(2-A)/(4B)\), which lies in \((-1,0)\): indeed \(0<A<2/3\), so \(2-A<4B\). As \(Q(1)-Q(-1)=8-4A>0\), its unique maximum on the interval occurs at \(x=1\). Since \(S=pAB/Q\), the limiting weakest mode is \(\theta=0\) and the strongest is \(\theta=\arccos x_*\) and its reflection. Uniform convergence and the density of Fourier grid frequencies give convergence of the minimum and maximum eigenvalues to these extrema. Their ratio is exactly the displayed expression. Positivity of \(Q\) is immediate from the factorization when \(x<1\) and from \(Q(1)=(2A+3B)^2>0\) at \(x=1\). All claims follow.

## Verification
The accompanying standalone `verify.py` requires only the Python 3 standard library. It enumerates every maximal independent set for \(3\le n\le15\), compares its cardinality and all first/second moments with the integer recurrence formulas **as exact rational numbers**, and compares exact rational matrix ranks with the claimed classification. It independently checks each Fourier eigenvalue against the rank count and evaluates the uniform asymptotic density at increasing cycle orders. The recorded run passed 553 tests. The proof, not these finite tests, establishes the assertions for every admissible cycle.

## Relationship to prior work
Bisdorff and Marichal establish Perrin counts and cyclic-composition descriptions; those combinatorial facts are not claimed as new. Brewster, Mynhardt and Teshima (2023) study the reconfiguration graph of **minimum-cardinality** maximal independent sets rather than Fourier observations of the uniform ensemble of **all** maximal independent sets. Baake, Birkner and Moody discuss general renewal-process diffraction, which covers the *general infinite-volume renewal-spectrum mechanism*; neither a general renewal identity nor a novel hard-rod process is claimed here. The contributions distinguished here are the **finite-labelled-cycle exact Fourier Gram eigenvalues**, the complete exceptional finite-rank and injectivity classification, and the sharp non-alternating extremum and explicit squared-condition limit for this specific sampling problem.

A previously published exact covariance spectrum for **all independent sets** of cycles, *The complete vertex-covariance spectrum of cycle stable-set polytopes* (2026), has a different ensemble, Fibonacci rather than Perrin enumeration, and a different sharp limiting condition ratio (five). The published *Minimal one-pass implications and exact Boolean trace rank for cycle maximal-independent-set contexts* (2026) treats the same object family but **Boolean traces/implication closures**, not Euclidean occupation covariance, its Fourier diagonalization, or frame bounds. The published *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles* (2026) explicitly addresses the **nonuniform random-order greedy law**, not the uniform measure here. These source comparisons are about statements and implications, not just titles.

## Limitations
The finite formulas concern **uniformly** sampled inclusion-maximal independent sets of a labelled cycle; they do not apply to random-order greedy maximal sets, fixed-size independent sets, all independent sets, or arbitrary renewal processes without modifying the model. The asymptotic condition constant is for the squared sampling bounds and is not the unsquared operator condition number (the latter is its square root). Classical hard-rod diffraction and renewal-correlation formulae are important antecedents; an earlier specialisation to exactly this cyclic finite-size first-Walsh Gram matrix cannot be completely ruled out without broader independent priority review. No independent mathematical audit has been performed.

## References
- R. C. Brewster, C. M. Mynhardt and L. E. Teshima, *The \(i\)-Graphs of Paths and Cycles*, arXiv:2303.08190v1, first posted 2023-03-14. https://arxiv.org/abs/2303.08190
- R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the \(n\)-cycle graph*, arXiv:math/0701647, first posted 2007-01-23. https://arxiv.org/abs/math/0701647
- M. Baake, M. Birkner and R. V. Moody, *Diffraction of stochastic point sets: explicitly computable examples*, arXiv:0803.1266 (2008). https://arxiv.org/abs/0803.1266
- *The complete vertex-covariance spectrum of cycle stable-set polytopes* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-vertex-covariance-spectrum-of-cycle-stable-set-poly--f7c01b21256b
- *Minimal one-pass implications and exact Boolean trace rank for cycle maximal-independent-set contexts* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-minimal-one-pass-implications-and-exact-boolean-trace-rank-for-c--5aa3700acbcd
- *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-uniformity-and-a-local-likelihood-ratio-obstruction-for-gr--9a6d94e819c5
