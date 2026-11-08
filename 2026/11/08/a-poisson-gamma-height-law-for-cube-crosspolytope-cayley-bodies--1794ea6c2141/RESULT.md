# A Poisson–gamma height law for cube–crosspolytope Cayley bodies

## Finding

**Theorem.** Fix positive scales \(a,b\), put \(\rho=b/a\), and for every integer \(d\ge2\) define the \((d+1)\)-dimensional Euclidean Cayley body
\[
K_d(a,b)=\operatorname{conv}\bigl((a[-1,1]^d\times\{0\})\cup (bB_1^d\times\{1\})\bigr),\quad
 B_1^d=\{x\in\mathbb R^d:\sum_i|x_i|\le1\}.
\]
Let \(X_d\) be uniform with respect to \((d+1)\)-dimensional volume on \(K_d(a,b)\), and let \(Z_d\in[0,1]\) be its last coordinate. Set \(H_d(\rho)=\sum_{k=0}^d \rho^k/k!\).

**Exact law and volume.** The Euclidean volume is
\[
 \operatorname{vol}_{d+1}K_d(a,b)=\frac{2^d a^d}{d+1}H_d(\rho).
\]
Moreover, if \(N_d\) is a variable with \(\Pr(N_d=k)=\rho^k/(k!H_d(\rho))\), \(0\le k\le d\), then the exact marginal distribution is the beta mixture
\[
 Z_d\mid (N_d=k)\sim \operatorname{Beta}(k+1,d-k+1).
\]
Equivalently, the height density at \(z\in(0,1)\) is
\[
 f_d(z)=\frac{d+1}{H_d(\rho)}\sum_{k=0}^d\binom dk\frac{\rho^k}{k!}\,z^k(1-z)^{d-k}.
\]

**Sharp non-Gaussian limit.** For every fixed \(\rho>0\),
\[
 dZ_d\ \xrightarrow[d\to\infty]{\mathrm{law}}\ T_\rho,
\]
where \(T_\rho\) is a compound-Poisson–gamma variable given by
\[
 T_\rho\ \stackrel{d}=\ E_0+\sum_{i=1}^{N}E_i,
 \qquad N\sim\operatorname{Poisson}(\rho),
\]
with independent \(E_i\sim\operatorname{Exp}(1)\) and the empty sum interpreted as zero. Its Laplace transform and density are exactly
\[
 \mathbb E e^{-sT_\rho}=\frac{1}{1+s}\exp\!\left(-\rho+\frac{\rho}{1+s}\right),\quad s\ge0,
\]
\[
 g_\rho(t)=e^{-\rho-t}\sum_{k=0}^\infty\frac{(\rho t)^k}{(k!)^2}
 =e^{-\rho-t}I_0(2\sqrt{\rho t}),\quad t>0.
\]
In particular, the height is concentrated at distance of order \(1/d\) above the cube level, and its scaled first two moments satisfy
\[
 \lim_{d\to\infty}d\,\mathbb E Z_d=1+\rho,
 \qquad \lim_{d\to\infty}d^2\operatorname{Var}(Z_d)=1+2\rho.
\]
The limit is not Gaussian and does not depend on the absolute horizontal scale \(a\).

## Assumptions and scope

The horizontal polytope on the lower level is an axis-aligned cube of coordinate half-width \(a\); the upper level is the standard axis-aligned \(\ell_1\)-crosspolytope of radius \(b\); both have common horizontal center and are placed one unit apart vertically. The ambient measure is ordinary Euclidean volume, not uniform sampling of vertices. All formulas hold for every integer \(d\ge2\) and positive finite \(a,b\); the convergence theorem fixes \(\rho=b/a\) as \(d\) grows. The modified Bessel function \(I_0\) is defined by the displayed power series, so the density formula requires no special-function conventions.

## Proof

**Step 1: Exact sections.** For \(0\le z\le1\), convexity and the definition of a Cayley join give the horizontal section
\[
 C_z=(1-z)a B_\infty^d+zb B_1^d.
\]
For arbitrary \(s,t\ge0\), the Minkowski sum \(sB_\infty^d+tB_1^d\) consists exactly of vectors \(x\) for which \(\sum_i (|x_i|-s)_+\le t\). To see this, coordinate clipping to \([-s,s]\) minimizes the \(\ell_1\)-distance to the box, with residual \(\sum_i(|x_i|-s)_+\). Partition its interior by the subset of coordinates outside the box and their signs. For each chosen set of size \(k\), the remaining \(d-k\) coordinates range in intervals of length \(2s\), while the positive excesses occupy a \(k\)-simplex of volume \(t^k/k!\). Summing over subsets and signs yields
\[
 \operatorname{vol}_d(sB_\infty^d+tB_1^d)
 =2^d\sum_{k=0}^d\binom dk\frac{s^{d-k}t^k}{k!}.
\]
Boundaries have measure zero; the formula also covers the endpoints by continuity.

**Step 2: Integrate and identify a beta mixture.** Substitute \(s=a(1-z)\) and \(t=bz\). Fubini gives total volume as the integral of the section volume. The elementary beta identity
\[
 \int_0^1 z^k(1-z)^{d-k}\,dz=\frac{k!(d-k)!}{(d+1)!}
\]
cancels the binomial factors and yields \(2^da^dH_d(\rho)/(d+1)\). Dividing the section polynomial by this volume shows that term \(k\) has total probability \(\rho^k/(k!H_d(\rho))\), and its normalized density is precisely \(\operatorname{Beta}(k+1,d-k+1)\). This proves the exact finite-dimensional statements.

**Step 3: Scaling limit.** The mixing weights converge in total variation to those of \(\operatorname{Poisson}(\rho)\), because \(H_d(\rho)\uparrow e^\rho\). For each fixed nonnegative integer \(k\), if \(Y_{d,k}\sim\operatorname{Beta}(k+1,d-k+1)\), then \(dY_{d,k}\) tends in distribution to \(\operatorname{Gamma}(k+1,1)\). One direct proof uses the beta density and the substitution \(z=t/d\): after multiplication by \(1/d\), it converges pointwise to \(t^ke^{-t}/k!\) and hence weakly, since this limiting density integrates to one. Truncate the mixing distribution at a fixed large \(k\), pass to the limit for the finite mixture, then remove the truncation using the Poisson tail bound. Thus \(dZ_d\) converges to the mixture of \(\operatorname{Gamma}(k+1,1)\) with Poisson weights, equivalently one exponential plus a Poisson number of independent exponentials.

**Step 4: Transform, density and moments.** The conditional gamma Laplace transform is \((1+s)^{-(k+1)}\). Averaging against \(e^{-\rho}\rho^k/k!\) gives the displayed closed transform. Averaging the gamma densities yields
\[
 e^{-\rho}\sum_{k\ge0}\frac{\rho^k}{k!}\frac{t^ke^{-t}}{k!}
 =e^{-\rho-t}\sum_{k\ge0}\frac{(\rho t)^k}{(k!)^2}.
\]
For moment convergence, the exact beta conditional moments are \(\mathbb EY_{d,k}=(k+1)/(d+2)\) and \(\mathbb EY_{d,k}^2=(k+1)(k+2)/((d+2)(d+3))\). Their mixing weights are bounded by an exponentially integrable Poisson majorant, so dominated convergence yields limiting first and second moments \(1+\rho\) and \(2+4\rho+\rho^2\), respectively, hence limiting variance \(1+2\rho\).

## Verification

The accompanying standalone `verify.py` independently evaluates the finite-dimensional beta-mixture normalization and first two moments with exact rational arithmetic for multiple dimensions and rational scale ratios. It also checks the section polynomial and the limiting mean and variance numerically. These checks are finite diagnostics; the all-dimensional section decomposition and dominated-convergence arguments above establish the result.

## Relationship to prior work

The two-height Cayley construction is standard in Hibi–Ohsugi–Tsuchiya (2018), whose work concerns integer decomposition and triangulations, not geometric sampling laws. The volume of Minkowski sums of cubes and crosspolytopes follows from standard mixed-volume principles, but the exact **beta mixture of Cayley heights** and its **Poisson–gamma non-Gaussian scaling limit**, including the Bessel density, were not found in the inspected related literature. Published work on Mahler products along the cube–crosspolytope Minkowski interpolation is especially close because it may use the same section-volume polynomial; that polynomial is not claimed to be original. The distributional limit and its geometric interpretation are the stated contribution.

## Limitations

The theorem fixes the ratio \(\rho\) as dimension increases and does not cover dimension-dependent ratios, arbitrary rotated crosspolytopes or non-Euclidean volume measures. The exact beta mixture follows by elementary geometry, and its absence in a limited search does not prove historical novelty; an equivalent limit law in unpublished or differently titled work is possible. No independent mathematical audit has been performed.

## References

- T. Hibi, H. Ohsugi and A. Tsuchiya, *Integer decomposition property for Cayley sums of order and stable set polytopes*, arXiv:1807.05989, publicly posted 2018-07-16. https://arxiv.org/abs/1807.05989
- G. Codenotti and F. Santos, *Unimodular covers of 3-dimensional parallelepipeds and Cayley sums*, arXiv:1907.12312, publicly posted 2019-07-29. https://arxiv.org/abs/1907.12312
- Classical Minkowski mixed-volume expansion and the beta integral, used explicitly in the proof.
