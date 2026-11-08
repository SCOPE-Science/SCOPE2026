# A singular reset-point layer and sharp total variation for nearly complete Brownian resetting

## Finding

Fix positive diffusivity \(D\) and Poisson reset rate \(r\). Between resets a real particle is Brownian with generator \(D\partial_{xx}\); each reset maps its position to \(aX\), with \(-1<a<1\). Write \(c=|a|\), \(\lambda=\sqrt{r/D}\), and let \(\mu_c\) and \(p_c\) denote the stationary law and density. The fully resetting law is \(\mu_0(dx)=p_0(x)dx\), where \(p_0(x)=\frac\lambda2e^{-\lambda|x|}\).

**Theorem (singular strong-reset asymptotics).** As \(c\downarrow0\):

1. **Inner-layer profile:** uniformly for \(y\) in each fixed compact real interval,
   \[
   \frac{p_c(cy/\lambda)-p_0(cy/\lambda)}c
       \longrightarrow -\frac\lambda2e^{-|y|}.
   \]
   In particular, the rounded cusp has the nontrivial microscopic profile
   \[
   \frac{p_c(cy/\lambda)-p_c(0)}c
     \longrightarrow -\frac\lambda2\bigl(|y|+e^{-|y|}-1\bigr).
   \]
2. **Outer density:** uniformly on compact subsets of \(\mathbb R\setminus\{0\}\),
   \[
   \frac{p_c(x)-p_0(x)}{c^2}\longrightarrow p_0(x).
   \]
3. **Signed-measure redistribution:** for each bounded \(C^2\) test function with bounded uniformly continuous second derivative,
   \[
   \frac{\int f\,d\mu_c-\int f\,d\mu_0}{c^2}
     \longrightarrow \int f\,d\mu_0-f(0).
   \]
   Thus the weak *distributional* perturbation equals \(\mu_0-\delta_0\), even though every difference quotient is an absolutely continuous signed measure.
4. **Sharp total variation:** with \(\|\nu-\eta\|_{\mathrm{TV}}=\sup_B|\nu(B)-\eta(B)|\),
   \[
      \lim_{c\downarrow0}\frac{\|\mu_c-\mu_0\|_{\mathrm{TV}}}{c^2}=1,
      \qquad
      \|\mu_c-\mu_0\|_{\mathrm{TV}}\leq\frac{c^2}{1-c^2}
      \quad(0\le c<1).
   \]
5. **One crossing and a logarithmic distinction scale:** for each \(0<c<1\), there is exactly one \(x_c>0\) such that \(p_c(x_c)=p_0(x_c)\), with \(p_c(x)<p_0(x)\) precisely when \(|x|<x_c\). It satisfies
   \[\frac{\lambda x_c}{c\log(1/c)}\longrightarrow1.\]
   Consequently, the total-variation maximizing event is exactly \(\{|x|>x_c\}\) (up to null sets). The \(c\)-scale cusp rounding and the larger \(c\log(1/c)\) sign-change scale are distinct.

All statements and constants are independent of the sign of \(a\). This is a singular *parameter* limit of stationary laws, not a statement about time-to-stationarity.

## Assumptions and scope

The reset times form an independent rate-\(r\) Poisson process; Brownian noise is independent of resets. The process is not absorbed and has no drift. All assertions concern the unique invariant probability measure for \(|a|<1\). The strong-reset limit keeps \(D,r\) fixed; dimension is one; densities are with respect to Lebesgue measure. Total variation uses the half-\(L^1\) convention for probability densities. The sign of a rescaling factor is irrelevant to invariant one-time distributions because every Brownian inter-reset displacement is symmetric.

## Proof

**1. Stationary perpetuity.** A Brownian displacement over a rate-\(r\) exponential time is symmetric Laplace with density \(p_0(x)\): its characteristic function is \(r/(r+Dk^2)=1/(1+k^2/\lambda^2)\). The Poisson backward-age decomposition, or the stationary fixed-point equation at a reset event, then gives
\[
 X_c\;\stackrel d=\;\sum_{j=0}^{\infty}c^jY_j,
 \qquad Y_j\stackrel{\rm iid}\sim p_0.
\]
The sum converges in \(L^2\) and almost surely, and the innovation is independent of the preceding scaled position. For negative \(a\), absorb alternating signs into the independent symmetric \(Y_j\). This is the unique invariant law by contraction under identical noise and reset clocks, or uniqueness of the perpetuity. Put \(Z_c=\sum_{j\ge1}c^jY_j\) independently of \(Y_0\). Then \(p_c=p_0*\mathcal L(Z_c)\) and
\[
 \mathbb E Z_c=0,\qquad
 \mathbb E Z_c^2=\frac{2c^2}{\lambda^2(1-c^2)},\qquad
 \lambda Z_c/c\longrightarrow\lambda Y_1\quad\hbox{in }L^2.
\]
In particular, all moments of \(\lambda Z_c/c\) of each fixed finite order are uniformly bounded for small \(c\), and its exponential moments exist in a fixed neighborhood of the origin.

**2. Inner layer.** Let \(W_c=\lambda Z_c/c\). At \(x=cy/\lambda\),
\[
 \frac{p_c(x)-p_0(x)}c=\frac\lambda{2c}\left(\mathbb E e^{-c|y-W_c|}-e^{-c|y|}\right).
\]
The bound \(|e^{-ct}-1+ct|\le c^2t^2/2\) for \(t\ge0\), combined with the uniform second moments of \(W_c\), makes the remainder uniformly \(o(1)\) on compact sets of \(y\). Since \(W_c\to W\) in \(L^1\), where \(W\) is unit-scale Laplace, the limit is \(-\lambda(\mathbb E|y-W|-|y|)/2\). Direct integration gives \(\mathbb E|y-W|=|y|+e^{-|y|}\). Subtract the profile at \(y=0\) and the expansion of \(p_0(cy/\lambda)\) to obtain the rounded-cusp formula.

**3. Outer limit and signed distribution.** Away from zero, \(p_0\) is analytic. For any compact set separated from zero by \(\delta>0\), the event \(|Z_c|<\delta/2\) permits the same-sign identity \(p_0(x-Z_c)=p_0(x)e^{\lambda\operatorname{sgn}(x)Z_c}\). Uniform exponential moments of \(Z_c/c\) make the complementary event exponentially small in \(1/c\). Taylor expansion yields
\[
 \mathbb E e^{\lambda\operatorname{sgn}(x)Z_c}
       =1+\frac{\lambda^2\mathbb E Z_c^2}{2}+o(c^2)
       =1+c^2+o(c^2),
\]
locally uniformly in \(x\ne0\), proving the outer limit. Independently, for a smooth test function \(f\), Taylor's formula and \(\mathbb E Z_c=0\) give
\[
 \frac{\mathbb E f(Y_0+Z_c)-\mathbb E f(Y_0)}{c^2}
    \longrightarrow\frac1{\lambda^2}\mathbb E f''(Y_0).
\]
The distributional derivative of the Laplace density is the finite signed measure \(p_0''=\lambda^2p_0\,dx-\lambda^2\delta_0\). Integration by parts (equivalently distributional duality) gives the claimed \(\mu_0-\delta_0\) limit. Bounded uniform continuity of \(f''\) justifies the Taylor remainder uniformly after division by \(c^2\).

**4. Matching sharp upper and lower bounds in total variation.** The finite signed measure \(p_0''\) has total variation norm \(2\lambda^2\). The integral second-order translation identity for functions whose second distributional derivative is a measure yields
\[
 \|p_0(\cdot-z)-p_0+zp_0'\|_{L^1}
       \le\frac{z^2}{2}\|p_0''\|_{\rm var}=\lambda^2z^2.
\]
Averaging over centered \(Z_c\) cancels the first-order term, hence
\[
 \|p_c-p_0\|_{L^1}\le \lambda^2\mathbb E Z_c^2
       =\frac{2c^2}{1-c^2}.
\]
This proves the stated global total-variation upper bound.

For the reverse bound, fix \(\varepsilon>0\), and set \(A_\varepsilon=\{x:|x|>\varepsilon\}\). For every \(|z|<\varepsilon\), direct Laplace integration gives
\[
 \mathbb P(|Y_0+z|>\varepsilon)=e^{-\lambda\varepsilon}\cosh(\lambda z).
\]
Because \(Z_c/c\) has uniformly controlled exponential moments near the origin, contributions from \(|Z_c|\ge\varepsilon\) and their \(\cosh\) replacements are \(o(c^2)\). Moreover, \(\mathbb E Z_c^4=O(c^4)\), so \(\mathbb E\cosh(\lambda Z_c)=1+\lambda^2\mathbb E Z_c^2/2+O(c^4)=1+c^2+o(c^2)\). Consequently,
\[
 \frac{\mu_c(A_\varepsilon)-\mu_0(A_\varepsilon)}{c^2}
    \longrightarrow e^{-\lambda\varepsilon}.
\]
Take the supremum over measurable events and then send \(\varepsilon\downarrow0\). This gives the matching lower limit \(1\).

**5. Uniqueness and location of the sign change.** For \(x\ge0\), write
\[
 R_c(x)=\frac{p_c(x)}{p_0(x)}=\mathbb E e^{\lambda x-\lambda|x-Z_c|}.
\]
Splitting on \(Z_c\le x\) gives \(R_c'(x)=2\lambda\mathbb E[e^{2\lambda x-\lambda Z_c}\mathbf1_{\{Z_c>x\}}]>0\). The derivatives are justified by dominated convergence and the continuous law of \(Z_c\). At zero, \(R_c(0)=\mathbb E e^{-\lambda|Z_c|}<1\); at infinity, \(R_c(x)\uparrow\mathbb E e^{\lambda Z_c}=\prod_{j\ge1}(1-c^{2j})^{-1}>1\). This proves a unique crossing and its strict sign regions.

For its location, the known stationary product \(\prod_{j\ge0}(1+c^{2j}k^2/\lambda^2)^{-1}\) admits the absolutely convergent partial-fraction density expansion, for each fixed \(0<c<1\),
\[
 p_c(x)=\frac{\lambda K_c}{2}\sum_{n=0}^\infty
  \frac{(-1)^n c^{n^2}}{\prod_{m=1}^n(1-c^{2m})}
  e^{-\lambda|x|/c^n},\qquad
 K_c=\prod_{m=1}^\infty(1-c^{2m})^{-1}.
\]
(The formula follows by extracting the simple-pole residues of the product; it is also an equivalent form of the cited fixed-multiplier stationary density.) Uniformly for \(x\ge0\) and \(0<c\le1/3\), division by \(p_0(x)\) gives
\[
 R_c(x)=K_c\left(1-\frac{c}{1-c^2}e^{-\lambda x(1/c-1)}
        +O(c^4e^{-\lambda x(1/c^2-1)})\right),
 \qquad K_c=1+c^2+O(c^4).
\]
At \(x=(1-\eta)c\log(1/c)/\lambda\), for any fixed \(0<\eta<1\), the negative term of order \(c^{2-\eta}\) dominates the \(c^2\) positive offset, whereas at \(x=(1+\eta)c\log(1/c)/\lambda\) the positive offset dominates. By the proved monotonicity, the unique crossing lies between these two values for all sufficiently small \(c\). Sending \(\eta\downarrow0\) establishes the location asymptotic. The sign regions identify the total-variation maximizing event, completing the proof.

## Verification

The bundled `verify.py` exercises characteristic-function products and the exact finite-Laplace partial-fraction densities, including normalization, the inner-layer profile, tail-event lower bounds, the total-variation upper bound, and the unique density-ratio crossing at several finite contraction factors. Execute `python3 verify.py` using the standard library only. These are finite numerical diagnostics; the proof above, not the diagnostics, establishes infinite-series convergence, uniform asymptotics, and the exact limiting coefficient.

## Relationship to prior work

Pierce's 2022 proportional-reset advection-diffusion paper derives the governing pantograph equation, stationary moments and density, including its strong-reset exponential limit. Di Bello et al. (2023) give a product characteristic function and exact stationary density for partial Brownian resetting. Biroli et al. (2024) provide an exact stationary density for both positive and negative multipliers and discuss its smooth peak and exponential tail; their small-multiplier appendix concerns mean first-passage time, not the stationary-law total-variation limit. The result here does **not** claim the invariant distribution, its Fourier product, or smoothness at a fixed nonzero multiplier as new. Its scope is the singular transition as the multiplier tends to zero: a matched central/outer expansion, a unique logarithmic-scale sign crossing, the signed deficit at the reset point, and the sharp probability-metric coefficient. Exact known finite-parameter densities determine these quantities in principle, so priority for the derived asymptotic requires checking for implicit or unindexed treatments.

## Limitations

No extension is asserted to positive drift, non-Poisson resetting, random reset multipliers, higher dimensions, or the limit \(c\uparrow1\). Weak convergence of the rescaled signed differences is stated on bounded smooth tests, not convergence in total variation to \(\mu_0-\delta_0\), which would be impossible since the finite-\(c\) differences are absolutely continuous. The parameter asymptotic does not imply a rate of temporal relaxation. The logarithmic crossing is a stationary density decision boundary, not a hitting-time threshold. Because earlier work solves the invariant density exactly, originality is specifically the singular-limit theorem and sharp coefficient; that limitation must be retained in any priority assessment.

## References

- J. Kevin Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (first posted 2022-04-14), https://arxiv.org/abs/2204.07215 .
- C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski, and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722 (first posted 2023-05), https://arxiv.org/html/2305.13722v2 .
- M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (first posted 2024-06-12), https://arxiv.org/html/2406.08387v1 .
- M. Kolb and S. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive* (2026), DOI:10.1112/blms.70314. Its convergence-to-stationarity question is distinct from convergence between stationary laws as the multiplier vanishes.
