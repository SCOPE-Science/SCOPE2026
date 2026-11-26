# Independent mathematical audit

## correctness

PASS

The coin is equivalent to a two-state axis chain with retention (1+q)/2 and conditionally independent fair signs. Consequently Cov(S_t,S_s)=min(t,s)I₂/2. Put s=(cos k₁+cos k₂)/2 and e=(cos k₁−cos k₂)/2. The eigenvalue equation becomes (λ−s)(λ−qs)=qe². The root near 1 is s+qe²/[(1−q)s]+O_q(|k|⁸); using the exact spectral projection gives amplitude 1−qe²/[(1−q)²s²]+O_q(|k|⁸). Taylor expansion gives the frozen L₄,L₆,A₄. Off the two saddles, the absolute-value transfer matrix has a strictly contracting square whenever either cosine has magnitude below one. At opposite cosine signs ±1 the eigenvalues solve λ²=q, so the spectral radius is still below one. Compactness and a uniform resolvent bound make the complement exponentially small. The two same-sign torus saddles contribute equally at even times; each normalized Gaussian integral is 1/(πn). Independently using N(0,2) even moments 2,12,120,1680 gives E[L₄]=(3q−1)/(2(1−q)), E[L₆]=(14q−2)/(3(1−q)), E[L₄²/2]=(187q²−98q+19)/(24(1−q)²) and E[A₄]=−q/(1−q)². The sum of the last three is (25q²+2q+1)/(8(1−q)²). Taylor on |k|≤n^(−1/2+η) for small η and Gaussian decay outside it give the asserted order of the remainder. Setting n=2m gives the coefficients, their cancellation at 1/3, the critical 5/16, and the stated inverse. At q=0 the exact central-binomial-square law is a separate normalization check.

## originality

PASS

Credit the exact active-walk model, transport blindness, general correlated-walk return methods, and the substantial mathematical overlap at first order with fourth-cumulant tomography. The supported distinct claim is the explicit return-at-time expansion through relative order m⁻² (particularly the first nonzero correction 5/16 at the cancellation). The priority limitations of the two historical return sources below do not establish coverage of this coefficient.

## value

PASS

Exact local return probabilities are a natural lattice observable distinct from displacement moments. The expansion quantifies when the local correction changes sign despite identical covariance, and gives the leading nonzero deviation where the first one cancels. This is more than recovering a hidden parameter again by a change of notation: it gives the return observable and its critical convergence rate and coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
