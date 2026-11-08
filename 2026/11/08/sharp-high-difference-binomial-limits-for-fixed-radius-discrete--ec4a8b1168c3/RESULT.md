# Sharp high-difference binomial limits for fixed-radius discrete Fourier smoothers

## Finding
For each fixed integer \(n\ge 2\), let \(\nabla f(j)=f(j+1)-f(j)\). Among real symmetric kernels \(u\) supported on \(\{-n,\ldots,n\}\) with \(\sum_j u(j)=1\), let \(\mathcal C_{n,k}\) be the minimum of the operator norm of \(f\mapsto \nabla^k(u*f)\) on \(\ell^2(\mathbb Z)\). Let \(\mathcal C^+_{n,k}\) be the same minimum subject also to \(\widehat u(\theta)\ge0\) at every frequency. Set
\[
 c_n=\min_{Q(z)=z^n+\cdots}\sup_{z\ge0}e^{-z}|Q(z)|,\qquad
 c_n^+=\min_{\substack{Q(z)=z^n+\cdots\\Q\ge0\ \mathrm{on}\ [0,\infty)}}\sup_{z\ge0}e^{-z}Q(z),
\]
where the polynomials have real coefficients. Then the sharp limits are
\[
 \boxed{\lim_{k\to\infty}(k/2)^n2^{-k}\mathcal C_{n,k}=c_n,\qquad
 \lim_{k\to\infty}(k/2)^n2^{-k}\mathcal C^+_{n,k}=c_n^+>c_n.}
\]
Every sequence of minimizing kernels in either problem converges coefficientwise to the centered binomial kernel
\[
 \boxed{u_\infty(j)=4^{-n}\binom{2n}{n+j}\quad(-n\le j\le n).}
\]
Every worst-case Fourier frequency lies within \(O(k^{-1/2})\) of the Nyquist frequency \(\pi\) modulo \(2\pi\). For radius \(n=2\), the first unrestricted sharp constant beyond the radius-one model is
\[
 \boxed{c_2=0.21691547125616746776\ldots,\qquad
 c_2^+=4W(e^{-1})^2=0.31017000630053558458\ldots,\quad c_2^+/c_2=1.42991186614918\ldots.}
\]
The first constant has an exact two-scalar characterization: \(d>2\) is the unique solution of \(e^d(d-2)=d+2\); \(t>0\) is the unique solution of \(t^2+(d-2)t+2-d=(d+2)e^{-t-d}\); and \(c_2=t^2+(d-2)t+2-d\). Here \(W\) denotes the nonnegative real branch of the Lambert function satisfying \(W(x)e^{W(x)}=x\).

## Assumptions and scope
All minima are taken over **real, symmetric, normalized** kernels of the stated fixed support radius. Fourier positivity means nonnegativity of the entire real-valued symbol, not nonnegativity of the kernel coefficients. The order \(k\) tends to infinity through positive integers while \(n\) is fixed. The operator norm is the exact \(\ell^2(\mathbb Z)\) multiplier norm. The constants \(c_n,c_n^+\) are natural weighted minimax invariants and are not assumed to have elementary closed forms for general \(n\). The radius-one case has been treated previously and is excluded from the novel claim.

## Proof
**1. Fourier reduction and scaling.** Since \(\widehat u\) is real, even, and a cosine polynomial of degree at most \(n\), every admissible kernel corresponds bijectively to a real polynomial \(r\) of degree at most \(n\) with \(r(0)=1\), via \(\widehat u(\theta)=r((1-\cos\theta)/2)\). The Fourier-positivity condition is exactly \(r(y)\ge0\) for \(0\le y\le1\). Plancherel and \(|e^{i\theta}-1|=2\sqrt{(1-\cos\theta)/2}\) give
\[
 \mathcal C_{n,k}=2^k\min_{r(0)=1}\max_{0\le y\le1}y^{k/2}|r(y)|,
\]
with the analogous nonnegative-polynomial restriction for \(\mathcal C^+_{n,k}\). Put \(K=k/2\), \(z=K(1-y)\), and \(Q_K(z)=K^n r(1-z/K)\). Then \(Q_K(K)=K^n\), \(\deg Q_K\le n\), and
\[
 K^n2^{-k}\mathcal C_{n,k}=\min_{\deg Q\le n,\,Q(K)=K^n}
 \max_{0\le z\le K}(1-z/K)^K|Q(z)|. \tag{1}
\]
The restricted problem in (1) additionally has \(Q\ge0\) on \([0,K]\).

**2. Existence and upper bound.** Fixed-degree minima exist: evaluating candidate polynomials at \(n+1\) distinct interior points and using an invertible Vandermonde matrix bounds their coefficients on every norm-bounded sublevel set. The same observation proves existence in the two limiting problems, whose norm is \(\|e^{-z}Q(z)\|_{L^\infty([0,\infty))}\). For any monic polynomial \(P\) of degree \(n\), the competitor \(Q_K=K^nP/P(K)\) satisfies the normalization for large \(K\). Since \((1-z/K)^K\le e^{-z}\) and \(K^n/P(K)\to1\), the limsup in (1) is at most \(\|e^{-z}P\|_\infty\). If \(P\ge0\) on the half-line, this is also a legal positive competitor. Taking respective infima gives the desired two upper bounds.

**3. Compactness and lower bound.** Choose minimizers \(Q_K\). The preceding upper bound is uniform. For any fixed distinct \(z_0,\ldots,z_n\ge0\), and \(K>\max z_i\), the weights \((1-z_i/K)^K\) are bounded away from zero. Thus \(|Q_K(z_i)|\) are uniformly bounded. Vandermonde inversion bounds every coefficient, so each sequence \(K\to\infty\) has a coefficientwise convergent subsequence. Writing \(Q_K(z)=\sum_{j=0}^n a_{j,K}z^j\), the constraint \(Q_K(K)=K^n\) gives \(a_{n,K}+\sum_{j<n}a_{j,K}K^{j-n}=1\); therefore the limiting polynomial is monic. In the positive problem it is nonnegative for every fixed \(z\ge0\), hence on the whole half-line. At each fixed \(z\), \((1-z/K)^K\to e^{-z}\), establishing the matching lower bound on the limiting sup norm. Consequently both sharp limits hold.

**4. Binomial limit and frequency localization.** The classical weighted alternation argument for the Haar space of real polynomials of degree \(\le n-1\) shows that the exponential-weighted monic minimizer is unique and exhibits \(n+1\) alternating nonzero weighted extrema on the half-line. In particular it changes sign when \(n\ge1\). The nonnegative limiting feasible set has a minimizer but cannot contain this unique signed minimizer, so \(c_n^+>c_n\). Coefficient boundedness of the minimizing \(Q_K\) implies, uniformly for \(0\le y\le1\),
\[
 r_K(y)=K^{-n}Q_K(K(1-y))\longrightarrow(1-y)^n.
\]
Since \((1+\cos\theta)^n/2^n=\cos^{2n}(\theta/2)=4^{-n}\sum_{j=-n}^n\binom{2n}{n+j}e^{ij\theta}\), Fourier coefficients converge to the displayed binomial law. To locate maximizing frequencies, use the uniform coefficient bound \(|Q_K(z)|\le C(1+z)^n\) for \(0\le z\le K\), and \((1-z/K)^K\le e^{-z}\). For large fixed \(R\), the weighted norm on \(z\ge R\) is strictly below the positive limiting optimum, uniformly in large \(K\); every maximizing \(z\) is therefore \(O(1)\). Since \(z=K(1+\cos\theta)/2\), this yields \(\operatorname{dist}(\theta,\pi+2\pi\mathbb Z)=O(k^{-1/2})\).

**5. Explicit five-tap constants.** For \(n=2\), write \(Q(z)=z^2+az+b\). Weighted alternation has three extrema at \(0<t_1<t_2\) together with \(0\), of signs \(+,-,+\). The two interior critical points satisfy \(Q'(t_i)=Q(t_i)\). Putting \(d=t_2-t_1\) yields \(a=2-2t_1-d\), \(b=t_1^2+(d-2)t_1+2-d\), \(Q(t_1)=2-d\), and \(Q(t_2)=2+d\). Equality of the two weighted interior amplitudes forces \(e^d(d-2)=d+2\), with a unique solution \(d>2\). Equality with the endpoint amplitude gives the unique positive root \(t_1=t\) in the statement. The resulting weighted polynomial has precisely the three alternating maximum points \(0,t,t+d\); the usual two-sign-change argument for a monic quadratic proves global uniqueness and optimality. For the nonnegative quadratic, write \(Q(z)=(z-\sqrt b)^2+(a+2\sqrt b)z\) with \(b=Q(0)\ge0\) and \(a+2\sqrt b\ge0\), equivalent to \(Q\ge0\) on the half-line. Hence its weighted norm dominates that of \((z-s)^2\), \(s\ge0\), and equality is attainable. For \(0\le s\le2\), the latter has maximum \(\max\{s^2,4e^{-s-2}\}\); when \(s>2\) an additional interior critical point occurs, but the endpoint value \(s^2>4\) already exceeds the candidate minimum. Equating the two branches on \([0,2]\) yields the unique minimizer \(s=2W(e^{-1})\), proving \(c_2^+=4W(e^{-1})^2\).

## Verification
The supplementary `CHECK.py` reconstructs the double-root/alternation equations with high precision, independently verifies the quadratic minimax sign pattern and the Lambert-W constant, and tests Fourier-to-polynomial scaling and convergence for multiple finite derivative orders. The infinite-degree assertions rely on the uniform coefficient compactness and tail bounds above; numeric experiments do not replace those arguments. Execute `python CHECK.py` with `mpmath`, `numpy`, and `scipy` available.

## Relationship to prior work
Gaitán, Garzón, and Madrid (arXiv:2604.25074, first posted April 28, 2026) derive exact sharp smoothing inequalities at small derivative orders and note that other orders remain open. Their Lemma 5.2 supplies the finite-order weighted alternation framework; their Theorem 1.10 relates unrestricted and Fourier-positive extremizers at doubled support/order. Neither furnishes the fixed-support, high-derivative-order sharp limit or the unrestricted radius-two exponential Chebyshev constant above. Kravitz–Steinerberger and Richardson treat the first and second derivatives. An earlier published three-point result handles support radius one for every order; that case is excluded. The positive radius-two constant can also be deduced by combining that radius-one result with the Gaitán–Garzón–Madrid squaring relation, and is stated here only to quantify the comparison with the newly determined unrestricted radius-two constant. Standard weighted-Chebyshev uniqueness and alternation are prior mathematical tools, not claimed as discoveries.

## Limitations
The support radius is fixed before \(k\to\infty\); no uniformity in growing \(n\) is claimed. Explicit numerical evaluation is supplied for \(n=2\), not all higher \(n\), whose constants are given by exact variational definitions. No exact finite-order optimal kernel or error rate beyond \(o(1)\) is claimed. The signed and Fourier-positive admissible classes differ; a positive Fourier transform does not imply nonnegative convolution coefficients. A publication-priority search cannot exclude every obscure equivalent under another normalization.

## References
1. J. Gaitán, C. Garzón, and J. Madrid, *The smoothest average and some extremal problems for polynomials*, arXiv:2604.25074 (2026), https://arxiv.org/abs/2604.25074.
2. N. Kravitz and S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, Bull. Lond. Math. Soc. 53 (2021), 1801–1815, https://doi.org/10.1112/blms.12543.
3. S. Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713 (2023), https://arxiv.org/abs/2310.09713.
4. G. Novello, K. Schiefermayr, and M. Zinchenko, *Weighted Chebyshev Polynomials on Compact Subsets of the Complex Plane*, Operator Theory: Advances and Applications 285 (2021), 357–370, https://doi.org/10.1007/978-3-030-75425-9_18.
5. *All-order sharp three-point smoothest averages* (2026), published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-order-sharp-three-point-smoothest-averages--97ecaa4cd5e9.
