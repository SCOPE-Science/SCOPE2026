# Sharp cubic correction and weighted cutoff for a fully discrete Hilbert kernel

## Finding

The exact large-distance difference between Petrov's fully discrete Hilbert kernel and the Riesz–Titchmarsh kernel has a cubic leading term, not merely the previously available quadratic-order upper bound. Its first two nonzero asymptotic terms determine a sharp weighted convolution-algebra threshold and a sharp finite-stencil approximation rate.

For every integer \(n\ge 0\), put \(w=n+\tfrac12\) and
\[
D(n)=K_{\mathrm d}(n)-\frac{1}{\pi(n+1/2)}.
\]
Then, as \(n\to+\infty\),
\[
\boxed{D(n)=-\frac{1}{4\pi w^3}-\frac{7}{16\pi w^5}+O(w^{-7}).}
\]
For all integers \(n\), \(D(-n-1)=-D(n)\). Thus, for every real \(\alpha\),
\[
\boxed{\sum_{n\in\mathbb Z}(1+|n+1/2|)^\alpha|D(n)|<\infty\quad\Longleftrightarrow\quad\alpha<2.}
\]
For \(R>0\), let \(D^{>R}(n)=D(n)\mathbf1_{\{|n+1/2|>R\}}\). Then
\[
\boxed{\sum_{n\in\mathbb Z}|D^{>R}(n)|=\frac{1+o(1)}{4\pi R^2}\quad(R\to\infty).}
\]
The convolution operator with kernel \(D^{>R}\) has exactly this norm on both \(\ell^1(\mathbb Z)\) and \(\ell^\infty(\mathbb Z)\). Its norm on any \(\ell^p(\mathbb Z)\), \(1\le p\le\infty\), is at most this quantity.

## Assumptions and scope

The fixed operator is the boundary Hilbert transform associated with harmonic extensions on \(\mathbb Z\times\mathbb N\) from Petrov's work, in the source's Fourier and convolution conventions. For \(0\le\theta\le\pi\), define
\[
\rho(\theta)^{1/2}=\sqrt{1+\sin^2(\theta/2)}-\sin(\theta/2),\qquad
f(\theta)=\rho(\theta)^{1/2}-1.
\]
The kernel difference is explicitly
\[
D(n)=\frac1\pi\int_0^\pi f(\theta)\sin((n+\tfrac12)\theta)\,d\theta,\qquad n\in\mathbb Z.
\]
These formulas uniquely fix normalization. The remainder statement is for integer \(n\to+\infty\), with the negative-index asymptotic obtained from the exact antisymmetry. The weights use the half-integer location to avoid conflating opposite kernel indices.

## Proof

**Endpoint structure.** The function \(f\) is real analytic on a neighborhood of \([0,\pi]\). Its Taylor expansion at zero is
\[
f(\theta)=-\frac\theta2+\frac{\theta^2}{8}+\frac{\theta^3}{48}-\frac{7\theta^4}{384}+O(\theta^5).
\]
Hence \(f(0)=0\), \(f''(0)=1/4\), and \(f^{(4)}(0)=-7/16\). At the other endpoint, \(\sin((\pi+t)/2)=\cos(t/2)\) is an even function of \(t\). Hence \(f(\pi+t)\) is even, so \(f^{(2j+1)}(\pi)=0\) for all nonnegative integers \(j\).

**Oscillatory expansion.** Set \(w=n+1/2>0\). The identities \(\cos(\pi w)=0\) and \(\sin(\pi w)=(-1)^n\), together with the endpoint vanishing above, permit repeated integration by parts. The first four integrations give
\[
\int_0^\pi f(\theta)\sin(w\theta)\,d\theta
=-\frac{f''(0)}{w^3}+\frac1{w^4}\int_0^\pi f^{(4)}(\theta)\sin(w\theta)\,d\theta.
\]
Integrating the remaining term twice more yields
\[
\int_0^\pi f(\theta)\sin(w\theta)\,d\theta
=-\frac{f''(0)}{w^3}+\frac{f^{(4)}(0)}{w^5}-\frac1{w^6}\int_0^\pi f^{(6)}(\theta)\sin(w\theta)\,d\theta.
\]
Here the possible terms at \(\pi\) vanish because \(f'(\pi)=f^{(3)}(\pi)=f^{(5)}(\pi)=0\), while sine factors vanish at zero. The last integral is \(O(w^{-1})\): one more integration by parts produces bounded endpoint terms and the integral of the bounded continuous function \(f^{(7)}\). Substitution of the two derivatives proves the announced \(O(w^{-7})\) expansion.

**Reflection.** In the defining integral, replacing \(n\) by \(-n-1\) changes the sine factor's sign, proving \(D(-n-1)=-D(n)\) exactly.

**Weighted summability.** The nonzero leading coefficient gives, uniformly on sufficiently large positive and reflected negative indices,
\[
|D(n)|\sim \frac{1}{4\pi |n+1/2|^3}.
\]
Comparison with the one-dimensional power series \(\sum_{k\ge1}k^{\alpha-3}\) proves convergence exactly when \(\alpha-3<-1\), that is, \(\alpha<2\). At the threshold there is a logarithmic divergence; above it, power-law divergence.

**Truncation constant and operator norms.** By reflection the two tails are identical. Since \(\sum_{k>R}k^{-3}\sim (2R^2)^{-1}\), each positive half contributes \((8\pi R^2)^{-1}\) and their sum \((4\pi R^2)^{-1}\). For any absolutely summable convolution kernel \(a\), the \(\ell^1\to\ell^1\) norm equals \(\|a\|_1\), attained on the unit impulse; the \(\ell^\infty\to\ell^\infty\) norm equals \(\|a\|_1\), attained at one coordinate by choosing input signs to match the kernel. Young's inequality gives the bound for intermediate \(p\). Apply these facts to \(a=D^{>R}\).

## Verification

Run `python CHECK.py` with Python 3, SymPy and SciPy installed. The script independently checks the Taylor coefficients symbolically and compares numerical quadrature of the defining Fourier integral against the two-term expansion at several positive indices, as well as the exact reflected-index relation. The finite computations are consistency checks, not a proof of the asymptotic, and the sharp weighted cutoff and operator-norm statements follow from the analytic argument above.

## Relationship to prior work

Petrov's original 2025 preprint, subsequently published in 2026, introduces the same fully discrete Hilbert transform. Its Section 4.2, Lemma 4.2 gives \(K_{\mathrm d}(n)=1/[\pi(n+1/2)]+O(n^{-2})\) and proves that the correction belongs to \(\ell^1\). The present result uses the same kernel representation but gives the first two nonzero coefficients, the exact polynomially weighted \(\ell^1\) threshold, and the sharp two-sided truncation norm asymptotic. Petrov cites earlier work of Ciaurri and collaborators on semi-discrete Riesz–Titchmarsh transforms; those operators and conventions differ from the fully discrete correction calculated here.

## Limitations

The result does not assert sharp intermediate \(\ell^p\) truncation norms for \(1<p<\infty\), does not extend automatically to higher-dimensional lattice harmonic extensions, and does not show that all discretizations of the Hilbert transform have the same cubic correction. The claims concern asymptotic tails, not a closed form for each finite kernel value. The novelty comparison is limited to the accessible literature inspected and does not establish publication priority independently.

## References

1. L. Petrov, *Harmonic Extensions on \(\mathbb Z\times\mathbb N\) and a Discrete Hilbert Transform*, arXiv:2510.16494, publicly posted October 18, 2025, especially Section 4 and Lemma 4.2. https://arxiv.org/abs/2510.16494
2. L. Petrov, *Discrete harmonic extensions and a discrete Hilbert transform*, Canadian Mathematical Bulletin, published online October 27, 2026, DOI:10.4153/S0008439526102641. https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/discrete-harmonic-extensions-and-a-discrete-hilbert-transform/82DB8FEDC5D74E809CF59F5DC984DA64
3. Ó. Ciaurri, M. Gillespie, L. Roncal, J. L. Torrea and J. L. Varona, *Harmonic analysis associated with a discrete Laplacian*, J. Anal. Math., 2017; referenced for related semi-discrete Riesz–Titchmarsh transforms, not as a source of the new estimates.
