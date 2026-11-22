# Sharp quartic spectral subconvolution threshold and its critical lattice constant

## Finding
For every real \(a>0\), every real \(p\geq0\), and \(k=(k_1,k_2)\in\mathbb Z^2\), put
\[
 r(k)=(|k_1|^4+|k_2|^4)^{1/4},\qquad
 w_{a,p}(k)=\frac{e^{-a r(k)}}{(1+r(k))^p},\qquad
 S_{a,p}=\sup_{n\in\mathbb Z^2}\frac{\sum_{k\in\mathbb Z^2}w_{a,p}(k)w_{a,p}(n-k)}{w_{a,p}(n)}.
\]
Then the *sharp subconvolution phase boundary* is
\[
 S_{a,p}<\infty\quad\Longleftrightarrow\quad p>\frac74.
\]
Precisely at the boundary, for the lattice-axis sequence \(n=(N,0)\),
\[
 \lim_{N\to\infty}\frac{1}{\log N}
 \frac{(w_{a,7/4}*w_{a,7/4})(N,0)}{w_{a,7/4}(N,0)}
 =\frac{\sqrt2\,\Gamma(1/4)}{a^{1/4}}.
\]
For \(0\le p<7/4\), the same axis ratio is at least a positive constant (depending on \(a,p\)) times \(N^{7/4-p}\). Thus the endpoint is logarithmically divergent, not merely unbounded. As a consequence, for \(p>7/4\) the positive-definite Fourier kernel \(\sum_{k\in\mathbb Z^2}w_{a,p}(k)e^{ik\cdot(x-y)}\) generates a Hilbert space of continuous functions on \(\mathbb T^2\) closed under pointwise multiplication, with multiplication norm at most \(S_{a,p}^{1/2}\).

## Assumptions and scope
The torus is \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\) with normalized Haar measure; convolution of sequences uses ordinary counting measure. The fourth norm \(r\) and weights above are fixed exactly, with no hidden Fourier normalization. The Hilbert norm is \(\|f\|_{\mathcal H}^2=\sum_k|\widehat f(k)|^2/w_{a,p}(k)\). This theorem classifies the *subconvolution* property, and gives sufficiency for a Hilbert multiplication algebra; it does **not** assert that failure of subconvolution implies failure of bounded multiplication.

## Proof
**1. Uniform quartic support inequality.** For any \(x,y\in\mathbb R^2\) having fourth norm one, let \(\ell_x(z)=x_1^3z_1+x_2^3z_2\). The dual norm of \(\ell_x\) is one and \(\ell_x(x)=1\). The scalar identity
\[
 v^4-u^4-4u^3(v-u)=(v-u)^2\{6(u+(v-u)/3)^2+(v-u)^2/3\}
 \ge (v-u)^4/3
\]
implies, on summing both coordinates and using \(\sum_i x_i^4=\sum_i y_i^4=1\),
\[
 1-\ell_x(y)\ge\frac1{12}\|y-x\|_4^4.
\]
Consequently, for \(z\ne0\) and \(t=\|z\|_4\),
\[
 t-\ell_x(z)\ge \frac{t}{12}\|z/t-x\|_4^4.
\]

**2. A uniformly summable tilted lattice series.** Define
\[
 T_{a,p}(x)=\sum_{k\in\mathbb Z^2}
 \frac{\exp\{-a(\|k\|_4-\ell_x(k))\}}{(1+\|k\|_4)^p},\qquad\|x\|_4=1.
\]
For each unit lattice square, the logarithms of its summand (extended to the plane) differ by a uniformly bounded amount, independently of \(x\); this follows from the Lipschitz property of the norm and \(\|\ell_x\|_*=1\). Thus \(T_{a,p}(x)\) is at most a fixed multiple of the corresponding plane integral. In Euclidean polar coordinates \(z=R(\cos\theta,\sin\theta)\), fourth norm is comparable to \(R\), and the map \(\theta\mapsto z/\|z\|_4\) is uniformly bi-Lipschitz on the circle. Step 1 therefore gives
\[
 \|z\|_4-\ell_x(z)\ge cR\operatorname{dist}_{\mathbb S^1}(\theta,\theta_x)^4.
\]
The angular integral is at most \(C\min(1,R^{-1/4})\), uniformly in \(x\). Hence
\[
 \sup_{\|x\|_4=1}T_{a,p}(x)
 \le C_{a,p}\int_0^\infty R(1+R)^{-p}\min(1,R^{-1/4})\,dR<\infty
\]
whenever \(p>7/4\).

**3. Global subconvolution upper bound.** Fix \(n\ne0\); write \(R=\|n\|_4\), \(x=n/R\), \(r=\|k\|_4\), \(t=\|n-k\|_4\), and \(\delta=r+t-R\). Duality gives
\[
 \delta=(r-\ell_x(k))+(t-\ell_x(n-k)),
\]
with both summands nonnegative. Since \(1+R\le(1+r)+(1+t)\), for \(p\ge0\),
\[
 \frac{(1+R)^p}{(1+r)^p(1+t)^p}
 \le C_p\{(1+r)^{-p}+(1+t)^{-p}\},
 \quad C_p=\max(1,2^{p-1}).
\]
Taking the exponential factor into account and using symmetry under \(k\mapsto n-k\),
\[
 \frac{(w_{a,p}*w_{a,p})(n)}{w_{a,p}(n)}
 \le 2C_p T_{a,p}(x),
\]
which is bounded by Step 2. At \(n=0\), the ratio is \(\sum_k w_{a,p}(k)^2<\infty\).

**4. Sharp necessity.** Take \(n=(N,0)\), with \(N\ge2\). For integers \(1\le j\le N/2\) and \(|l|\le j^{3/4}\), concavity of the fourth root gives
\[
 0\le (j^4+l^4)^{1/4}-j\le\frac{l^4}{4j^3}\le\frac14,
\]
and the analogous bound for \(N-j\). Thus the exponential gap is at most \(1/2\), and the polynomial quotient in Step 3 is bounded below by \(c_p(1+j)^{-p}\). There are at least \(c j^{3/4}\) available integers \(l\), so
\[
 \frac{(w_{a,p}*w_{a,p})(N,0)}{w_{a,p}(N,0)}
 \ge c_{a,p}\sum_{j=1}^{\lfloor N/2\rfloor}j^{3/4-p}.
\]
This grows at least as \(N^{7/4-p}\) if \(p<7/4\) and as \(\log N\) at equality. Thus no smaller exponent can satisfy subconvolutivity.

**5. Exact logarithmic coefficient.** Set \(p=7/4\) and denote the axis ratio by \(C_N\). For the first endpoint define
\[
 B_j=\sum_{l\in\mathbb Z}
 \frac{\exp\{-a[(j^4+l^4)^{1/4}-j]\}}{(1+(j^4+l^4)^{1/4})^{7/4}}.
\]
Putting \(l=j^{3/4}y\) in the Riemann sum, with a split at \(|y|=K\) and quartic-exponential domination of the tails, yields
\[
 \lim_{j\to\infty}jB_j
 =\int_{\mathbb R}e^{-ay^4/4}\,dy
 =\frac{\Gamma(1/4)}{\sqrt2\,a^{1/4}}=:A_a.
\]
For each fixed \(0<\varepsilon<1/2\), in the endpoint range \(1\le j\le\varepsilon N\), the factor from the second leg \((N-j,l)\) differs multiplicatively from one by at most \(O_{a,K}(\varepsilon)+o_N(1)\) uniformly on \(|l|\le Kj^{3/4}\). The discarded \(|l|>Kj^{3/4}\) have an arbitrarily small fraction of the logarithmic mass once \(K\) is large, using the same quartic domination. Thus this range contributes \((A_a+o_\varepsilon(1))\log N\) in the successive limits \(N\to\infty\), then \(\varepsilon\downarrow0\). Reflection \(j\mapsto N-j\) gives the same contribution at the other endpoint.

For fixed \(\varepsilon\), the interior range \(\varepsilon N\le j\le(1-\varepsilon)N\) contributes \(O_{a,\varepsilon}(1)\): each summand in the \(j\)-sum has polynomial factor \(O_\varepsilon(N^{-7/4})\), while the sum in \(l\) of the quartic-defect exponential is \(O(N^{3/4})\). The exterior ranges \(j\le0\) and \(j\ge N\) contribute \(O_a(1)\) by the strict outward exponential gap. After division by \(\log N\), these terms disappear. Hence \(C_N/\log N\to2A_a\), as claimed.

**6. Fourier-Hilbert consequence.** The kernel coefficients are strictly positive and summable. Fourier coefficient Cauchy–Schwarz, followed by Step 3, gives \(\|fg\|_{\mathcal H}^2\le S_{a,p}\|f\|_{\mathcal H}^2\|g\|_{\mathcal H}^2\) first for trigonometric polynomials and then by density. This proves the asserted sufficient multiplication statement.

## Verification
The file `quartic_check.py` computes truncated positive convolution sums in ordinary double precision and checks the predicted critical scaling for several growing axis lengths. It independently tests the exact one-dimensional fourth-power convexity inequality on a finite rational grid. The proof above is analytic: these finite computations neither establish convergence nor certify the infinite supremum. No computationally obtained estimate is required to justify the phase boundary or critical constant.

## Relationship to prior work
Das and Giannakis [1] formulate subconvolutive spectral weights on compact abelian groups and prove their usefulness for reproducing-kernel Hilbert algebras. Their general criterion does not evaluate the quartic-norm exponential family or its critical lattice coefficient. Kaleta and Ponikowski [2, Proposition 3.5 and Lemma 3.6] obtain the Euclidean-radial continuous-density exponent \((d+1)/2\), hence \(3/2\) in dimension two. That result concerns Euclidean-almost-radially-decreasing densities; the present family is not uniformly comparable to a Euclidean-radial profile, since quartic and Euclidean norms differ by a nonzero fraction on rays and the resulting exponential ratio is unbounded. It also does not give the discrete quartic axis coefficient. The distinct \(7/4\) exponent records the quartic flatness of the axis norm rather than ordinary quadratic angular curvature. These comparisons bound, rather than prove, any assertion of historical priority.

## Limitations
The theorem is for the exact fourth norm on \(\mathbb Z^2\) and for all real \(a>0,p\ge0\). It does not classify all norms, prove a necessary condition for *ordinary* bounded pointwise multiplication when subconvolutivity fails, or assert an exact global best multiplication constant. The logarithmic coefficient is an axis asymptotic, not a claim that the axis always maximizes the global ratio at finite size. Published priority and independent mathematical validation remain unestablished.

## References
[1] S. Das and D. Giannakis, *On harmonic Hilbert spaces on compact abelian groups*, arXiv:1912.11664, first submitted 25 December 2019, https://arxiv.org/abs/1912.11664 ; particularly Theorem 4 and Section 4.

[2] K. Kaleta and D. Ponikowski, *On directional convolution equivalent densities*, arXiv:2109.06336, first submitted 13 September 2021, https://arxiv.org/abs/2109.06336 ; Proposition 3.5 and Lemma 3.6.
