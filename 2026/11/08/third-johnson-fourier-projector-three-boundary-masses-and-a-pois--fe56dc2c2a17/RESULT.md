# A Poisson–Charlier cusp for the third Johnson projector

## Finding

Let \(P^{(3)}_{n,k}\) be the canonical orthogonal projector onto the degree-three Johnson harmonic component on the uniform slice of \(k\)-subsets of \([n]\), where \(n\ge 2k\ge6\). Write \(N_{n,k}\) for its \(\ell^\infty\)-operator norm, which is also its \(\ell^1\)-operator norm. If \(k/\sqrt n\to c\in(0,\infty)\), then
\[
 n^{-3/2}N_{n,k}\longrightarrow \Phi(c)=\frac{\mathbb E|C_3(Z_{c^2};c^2)|}{6c^3},\qquad Z_\lambda\sim\operatorname{Poisson}(\lambda),
\]
where \(C_3(j;\lambda)=(j)_{\underline{3}}-3\lambda(j)_{\underline{2}}+3\lambda^2j-\lambda^3\) and \((j)_{\underline r}\) is the falling factorial. The sparse limiting norm profile is not differentiable at \(c=\sqrt3\). Its one-sided derivatives there satisfy
\[
 \Phi'_+(\sqrt3)-\Phi'_-(\sqrt3)=6e^{-3}.
\]
At the ends of the sparse scale, \(\Phi(c)\sim 4c^3/3\) as \(c\downarrow0\), and \(\Phi(c)\to\sqrt{2/\pi}(1+4e^{-3/2})/6\) as \(c\to\infty\). The latter equals the normalized limit of \(N_{n,k}\) in the positive-density regime \(k/n\to\rho\in(0,1/2]\). The cusp arises when a zero of the limiting cubic crosses an integer overlap with positive probability. Thus the stability constant for this harmonic truncation has a feature specific to the sparse overlap law, invisible to the positive-density Gaussian limit.

## Kernel and normalization

For a fixed \(k\)-set \(S\) and uniform \(k\)-set \(T\), put \(J=|S\cap T|\). Its probabilities are
\[
 p_j=\binom kj\binom{n-k}{k-j}/\binom nk,\qquad 0\le j\le k.
\]
Let \(h\) be the monic degree-three polynomial orthogonal to degrees \(0,1,2\) for these weights. The Gram system is invertible since the law has at least four positive support points. The standard Johnson filtration has degree at most \(r\) spanned by the functions \(T\mapsto\mathbf1_{U\subset T}\) for \(|U|=r\); the space of degree exactly \(3\) is the orthogonal difference between degrees at most \(3\) and at most \(2\), of dimension \(d_3=\binom n3-\binom n2\). The radial polynomial \(h(|S\cap T|)\) lies in this difference: it has degree at most three, and stabilizer-averages of degree-at-most-two functions are polynomials of degree at most two in \(J\). In fact, averaging the indicator for \(|U|=r\le2\) with \(i=|U\cap S|\) gives \((J)_{\underline i}(k-J)_{\underline{r-i}}/[(k)_{\underline i}(n-k)_{\underline{r-i}}]\).

The normalized-counting-measure kernel of the orthogonal projection is
\[
 K(S,T)=d_3h(J)/h(k).
\]
Indeed the projection commutes with permutations, so each row belongs to the stabilizer-invariant space of degree three. The averaging calculation just given also applies to \(r=3\), showing that such a row is a polynomial in \(J\) of degree at most three. Orthogonality to the lower degrees makes it proportional to \(h(J)\), and the constant diagonal equals the rank by the trace identity. The denominator is positive since the monic orthogonal cubic has all its zeros inside the support interval. Symmetry and transitivity give \(N_{n,k}=\mathbb E|K(S,T)|\) (the sharp norm is the absolute row sum), and projection idempotence gives \(\mathbb E[K(S,T)^2]=d_3\). Consequently \(n^{-3/2}|K|\) is uniformly integrable in each limit used below.

## Sparse limit and the cusp

The factorial moments of the overlap are \(\mathbb E(J)_{\underline r}=(k)_{\underline r}^2/(n)_{\underline r}\) by counting ordered tuples in the intersection. If \(k/\sqrt n\to c>0\), these moments converge for each fixed \(r\) to \(\lambda^r\), where \(\lambda=c^2\). The method of moments gives \(J\Rightarrow Z_\lambda\), since the Poisson law is moment-determinate. The Gram system for \(h\) therefore converges to the Poisson Gram system. Its monic cubic is \(C_3(j;\lambda)\): the coefficient of \(t^3/3!\) in \(e^{-\lambda t}(1+t)^j\) is this polynomial, and multiplying by \((j)_{\underline r}\) and taking Poisson expectation gives \(\lambda^r(1+t)^r\), with no term of degree three for \(r<3\). Hence \(h\to C_3\) coefficientwise and \(h(k)\sim k^3\sim c^3n^{3/2}\). The kernel limit in distribution is \(C_3(Z_\lambda;\lambda)/(6c^3)\), and uniform integrability proves the norm limit.

At \(\lambda=3\), the polynomial factors as \((j-1)(j^2-11j+27)\), whose only integer zero is \(j=1\). The \(j=1\) summand of \(\Phi(\sqrt\lambda)\) is
\[
 e^{-\lambda}\lambda^{3/2}|3-\lambda|/6.
\]
The sum of all other terms is continuously differentiable near \(\lambda=3\): for sufficiently large \(j\) the leading cubic term dominates uniformly on a compact neighborhood of \(3\), and the finitely many remaining nonzero terms keep their signs on a possibly smaller neighborhood. The derivative series converges uniformly there by the factorial decay of the Poisson probabilities, even after multiplication by a fixed power of \(j\). Thus the derivative jump in \(\lambda\) is twice \(e^{-3}3^{3/2}/6\). Multiplying by \(2\sqrt3\) to convert to the variable \(c\) gives \(6e^{-3}\).

As \(\lambda\downarrow0\), the terms at \(j=0,1,2,3\) in the unnormalized expectation are respectively asymptotic to \(1,3,3,1\) times \(\lambda^3\), with the tail \(O(\lambda^4)\). This gives \(4c^3/3\). As \(\lambda\to\infty\), put \(Y=(Z_\lambda-\lambda)/\sqrt\lambda\). Then \(\lambda^{-3/2}C_3(Z_\lambda;\lambda)=Y^3-3Y+O(\lambda^{-1/2})(1+Y^2+|Y|)\). The Poisson Gaussian limit, with moment convergence through order six (from the cumulants), gives \(\lim_{c\to\infty}\Phi(c)=\mathbb E|G^3-3G|/6\) for a standard normal \(G\). Integration across \(0,\pm\sqrt3\) yields the displayed constant.

## Positive-density comparison

If \(k/n\to\rho\in(0,1/2]\), the mean and variance of \(J\) are \(\mu=k^2/n\) and \(\sigma^2=k^2(n-k)^2/[n^2(n-1)]\). The standardized hypergeometric variable \(Y=(J-\mu)/\sigma\) tends to the standard normal; moment convergence follows from the sampling-without-replacement exponential tail bound, since \(\sigma^2\) and \(k\) are both of order \(n\). The monic cubic \(h(\mu+\sigma y)/\sigma^3\) therefore tends coefficientwise to \(y^3-3y\). As \((k-\mu)/\sigma=\sqrt{n-1}\), substitution gives \(h(k)/\sigma^3\sim n^{3/2}\). Together with \(d_3\sim n^3/6\) and the kernel second moment, this proves the positive-density norm comparison.

## Relationship to prior work and scope

The Johnson harmonic decomposition and its Hahn polynomial description are classical. In particular the Hahn difference equation (NIST DLMF, §18.22(ii), equations 18.22.10–11) already supplies a weighted summation-by-parts formula for finite absolute sums after splitting by signs. Neither that identity nor such a finite boundary formula is claimed here as new. Work on the first and second Johnson projectors concerns different degrees. The result here identifies the sparse third-projector profile and evaluates the jump at its mean-three integer crossing; it does not classify all cusps, treat fixed \(k\), or claim priority for classical Gaussian or Poisson polynomial limits. The analytic proof, not finite checks of kernel normalization or numerical approximations to the cusp, establishes the limit and the jump.

References: F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533; Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142; M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra **17** (2008), 154–167; NIST DLMF §§18.19 and 18.22.
