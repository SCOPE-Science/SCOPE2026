# Critical rare-antipodal-flip crossover in Boolean-cube cutoff profiles

## Finding
Consider the continuous-time random walk on the Boolean cube \(\{-1,+1\}^n\), initially all positive, in which coordinate \(i\) flips at rate \(1/n\), independently across coordinates, while an additional independent Poisson clock of rate \(\gamma_n\ge0\) flips **all** coordinates simultaneously. Write \(d_n(t)\) for total variation distance from uniform equilibrium and \(\chi_n^2(t)\) for its chi-square divergence.

For every fixed \(c\in\mathbb R\), let \(t_n(c)=\tfrac n4\log n+cn\) (which is positive for sufficiently large \(n\)). If \(\gamma_n n\log n\to\theta\in[0,\infty]\), put \(a=e^{-2c}\), \(h=e^{-\theta/2}\), with \(h=0\) at \(\theta=\infty\), and let \(Z\) be standard normal. Then
\[
\lim_{n\to\infty}d_n(t_n(c))=
F_h(a):=\frac12\mathbb E\left|e^{-a^2/2}\bigl(\cosh(aZ)+h\sinh(aZ)\bigr)-1\right|,
\]
and
\[
\lim_{n\to\infty}\chi_n^2(t_n(c))
=\cosh(a^2)-1+h^2\sinh(a^2).
\]
For each fixed \(a>0\), the total-variation profile \(F_h(a)\) is **strictly increasing** as \(h\) ranges from zero to one. Thus rare antipodal flips have a nontrivial continuous impact exactly when their expected number up to the ordinary cube cutoff is of constant order. For \(h=1\), \(F_1(a)=2\Phi(a/2)-1\), the classical Gaussian-tilt profile; for \(h=0\), \(F_0(a)=\tfrac12\mathbb E|e^{-a^2/2}\cosh(aZ)-1|\), the fully antipodally symmetrized profile. The intermediate \(0<h<1\) profiles are distinct from both endpoints.

The late-window behavior separates sharply:
\[
F_h(a)\sim\frac{h a}{\sqrt{2\pi}}\quad(a\downarrow0,\ h>0),
\qquad
F_0(a)\sim \varphi(1)a^2\quad(a\downarrow0),
\]
where \(\varphi(1)=e^{-1/2}/\sqrt{2\pi}\). For **every** sequence of nonnegative rates \(\gamma_n\), even without a limit, the walk has total-variation cutoff at \(\tfrac n4\log n\) with window of order \(n\).

## Assumptions and scope
Fix integer \(n\ge1\). Coordinate clocks are independent Poisson processes of intensity \(1/n\), and the simultaneous-complement clock is independent with intensity \(\gamma_n\in[0,\infty)\). Each clock arrival toggles the designated bits; clock events are never reset or resampled. The generator is the sum of coordinate-flip generators and the global-complement generator. Uniform equilibrium on all \(2^n\) states is unique, since the individual coordinate flips yield irreducibility. Transitivity makes worst-start and all-positive-start distances identical. The limit takes \(n\to\infty\) with fixed real \(c\); \(\theta=\infty\) means divergence to positive infinity. We use \(\|\mu-\pi\|_{\rm TV}=\frac12\sum_x|\mu(x)-\pi(x)|\) and \(\chi^2(\mu\|\pi)=\sum_x\pi(x)(d\mu/d\pi(x)-1)^2\). All logarithms are natural.

## Proof
**1. Exact independent-noise mixture.** Write \(b=e^{-2t/n}\) and \(h_t=e^{-2\gamma_n t}\). The parity of the common-clock count is even with probability \(w=(1+h_t)/2\). Conditional on even parity, each coordinate has an independent sign with mean \(b\); conditional on odd parity, all means are \(-b\). Thus, relative to uniform measure \(\pi_n\), the density is exactly
\[
L_{n,t}(x)=\frac{1+h_t}{2}\prod_{i=1}^n(1+bx_i)
+\frac{1-h_t}{2}\prod_{i=1}^n(1-bx_i),\qquad x\in\{-1,+1\}^n.
\tag{1}
\]
In particular, if \(j\) is the number of positive signs of \(x\), the exact finite-dimensional variation distance is
\[
\frac12\sum_{j=0}^n2^{-n}\binom nj\left|
\frac{1+h_t}{2}(1+b)^j(1-b)^{n-j}
+\frac{1-h_t}{2}(1-b)^j(1+b)^{n-j}-1\right|.
\tag{2}
\]
The Walsh character indexed by \(S\subseteq[n]\) has mean \(b^{|S|}\) if \(|S|\) is even, and \(h_t b^{|S|}\) if \(|S|\) is odd. Orthogonality gives the exact chi-square identity
\[
\chi_n^2(t)=\frac{(1+h_t^2)(1+b^2)^n+(1-h_t^2)(1-b^2)^n}{2}-1.
\tag{3}
\]

**2. Gaussian density limit and uniform integrability.** At \(t=t_n(c)\), \(b=e^{-2c}n^{-1/2}=a/\sqrt n\) exactly, while \(h_t\to h\). Under \(\pi_n\), the central limit theorem gives \(n^{-1/2}\sum_i x_i\Rightarrow Z\sim N(0,1)\). Taylor expansion of \(\sum_i\log(1\pm b x_i)\) gives \(\pm a n^{-1/2}\sum_i x_i-a^2/2+o_{\pi_n}(1)\). Equation (1) therefore converges in distribution under \(\pi_n\) to \(e^{-a^2/2}(\cosh(aZ)+h\sinh(aZ))\). Moreover, (3) implies \(\sup_n\mathbb E_{\pi_n}L_{n,t_n(c)}^2<\infty\), which ensures uniform integrability of \(|L_{n,t_n(c)}-1|\). Taking expectations proves the total-variation profile. Taking the limit in (3) proves the chi-square expression.

**3. Strict interpolation and late-window exponents.** Write \(A(z)=e^{-a^2/2}\cosh(az)-1\) and \(B(z)=e^{-a^2/2}\sinh(az)\). Symmetry of the Gaussian density gives the exact representation
\[
F_h(a)=\int_0^\infty\max\{|A(z)|,hB(z)\}\,\varphi(z)\,dz.
\tag{4}
\]
For each \(a>0\), \(A\) has a unique positive zero \(z_*=a^{-1}\operatorname{arcosh}(e^{a^2/2})\), and \(B(z_*)>0\). Hence the integral in (4) strictly increases whenever \(h\) increases, because a positive-length neighborhood of \(z_*\) has \(|A|\) smaller than both positive competing multiples of \(B\). The case where the smaller multiplier is zero follows by the same neighborhood. The classical \(h=1\) formula follows by lognormal likelihood-ratio integration. For fixed \(h>0\), the density deviation divided by \(a\) converges in \(L^1\) under normal law to \(hZ\), giving \(F_h(a)\sim h a/\sqrt{2\pi}\). At \(h=0\), division by \(a^2\) gives \((Z^2-1)/2\) in \(L^1\), so the leading TV coefficient is \(\frac14\mathbb E|Z^2-1|=\varphi(1)\).

**4. Cutoff for every antipodal rate.** The density is the mixture in (1), so convexity of total variation bounds its distance by the pure product-chain distance, which tends to zero after \(\tfrac n4\log n+cn\) as \(c\to+\infty\). Conversely, symmetrizing a measure with its antipodal image is a further Markov averaging, so its distance cannot exceed that of a mixture with any bias \(h_t\in[0,1]\). Thus at every \(n,t\), the distance is bounded **below** by the fully symmetrized distance with the same \(b\). At time \(t_n(c)\) the latter converges to \(F_0(e^{-2c})\). As \(c\to-\infty\), its Gaussian likelihood tends to zero in probability (since \(e^{-a^2/2}\cosh(aZ)\to0\)), while retaining mean one, so \(F_0(e^{-2c})\to1\). These uniform upper and lower comparison bounds establish the claimed cutoff irrespective of the behavior of \(\gamma_n\).

## Verification
The standalone Python script `verify.py` checks exact finite-dimensional densities by state enumeration, the binomial total-variation identity, Fourier/Walsh coefficients, the chi-square formula, and monotonicity for selected finite parameters, all with rational arithmetic. It separately evaluates the Gaussian integral by deterministic quadrature and compares it with large-binomial laws near the cutoff window. On execution the script reported `VERIFY_OK 4533 exact and deterministic finite checks`. Finite checks corroborate the algebra but are not evidence of a proof at arbitrary dimension: the analytical argument above proves the limits.

## Relationship to prior work
Baran and Šarković (2026) prove that lazy and simple walks on **randomly twisted** hypercube graphs have mixing time linear in dimension and no cutoff. This is a different graph and phenomenon; their investigation motivates identifying which kinds of long-range modifications genuinely alter a *classical* cube's cutoff profile. Diaconis, Graham and Morrison (1990) determine the ordinary cube's Gaussian cutoff, corresponding to the \(h=1\) endpoint; it is not claimed new. Nestoridi (2015) studies flipping a uniformly sampled fixed-size coordinate subset rather than superposing a rare global-complement Poisson clock. Collevecchio and Griffiths (2020) study more general nonlocal hypercube walks and spectral methods, without the particular critical rare-event interpolation presented here.

A directly relevant published result on a unicyclic two-endpoint-toggle chain finds a Gaussian–cosh profile for an even-cycle quotient at a special parameter. Its pure cosh endpoint is closely analogous to \(h=0\), and is not claimed as a new functional form. Another published result optimizes the spectral gap of priced folded-hypercube **edges**, not the present total-variation cutoff law for fixed Poisson intensities. The asserted contribution is the **critical one-parameter family** generated by a sparse all-bit flip process, its strict variation ordering, exact chi-square crossover and the discontinuity of the late-window decay exponent between fully symmetrized and finitely biased regimes. No unconditional priority claim is made outside the inspected sources.

## Limitations
The intermediate profiles require the precise scaling of the common-flip rate. The formula does not describe inhomogeneous coordinate rates, nonuniform initial laws, nonlinear interacting updates, or a time-varying global-clock intensity. The profile limit is pointwise in the cutoff-window parameter. The elementary Gaussian-mixture mechanism might also appear in prior folded-cube or coding-theoretic literature under different terminology. Priority has not been independently certified. Deterministic finite checks do not certify the infinite-dimensional convergence.

## References
1. Z. Baran and A. Šarković, *Mixing time of the lazy and simple random walk on a randomly twisted hypercube*, arXiv:2610.21976, first publicly posted 2026-10-15. https://arxiv.org/abs/2610.21976
2. P. Diaconis, R. L. Graham and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72. https://doi.org/10.1002/rsa.3240010105
3. E. Nestoridi, *A non-local random walk on the hypercube*, arXiv:1507.05690, first publicly posted 2015-07-21. https://arxiv.org/abs/1507.05690
4. A. Collevecchio and R. Griffiths, *Three steps mixing for general random walks on the hypercube at criticality*, arXiv:2002.09059, first publicly posted 2020-02-20. https://arxiv.org/abs/2002.09059
5. *Parity-dependent Gaussian–cosh cutoff profiles for unicyclic edge-toggle walks*, published mathematical research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-parity-dependent-gaussian-cosh-cutoff-profiles-for-unicyclic-edg--2ee94cfb912f
6. *Sharp antipodal-price threshold and edgewise rigidity for folded hypercube mixing*, published mathematical research record, 2026-10-13. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-sharp-antipodal-price-threshold-and-edgewise-rigidity-for-folded--bf23d5d98989
