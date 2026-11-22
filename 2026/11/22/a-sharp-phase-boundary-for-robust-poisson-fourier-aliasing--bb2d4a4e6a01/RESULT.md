# A sharp phase boundary for robust Poisson Fourier aliasing

## Finding

Let \(0<A<B\), \(C\ge0\), and let \(N\ge1\) be an arbitrary integer. We determine the **unique globally optimal center and scale of a Cauchy reference measure** for minimizing the worst squared \(L^2\) Fourier aliasing of Poisson kernels arising from *every positive mixture* of Cauchy measures with location \(|c|\le C\) and scale \(A\le a\le B\). A single choice works for every Fourier sampling resolution \(N\). It has a sharp two-regime law:

\[
\boxed{m_*=0,\qquad s_*=
\begin{cases}
\sqrt{AB-C^2},&0\le C^2\le A(B-A)/2,\\[3pt]
\sqrt{A^2+C^2},&C^2\ge A(B-A)/2.
\end{cases}}
\]

Set
\[
\boxed{R_*^2=
\begin{cases}
\displaystyle\frac{A+B-2\sqrt{AB-C^2}}{A+B+2\sqrt{AB-C^2}},&0\le C^2\le A(B-A)/2,\\[8pt]
\displaystyle\frac{\sqrt{A^2+C^2}-A}{\sqrt{A^2+C^2}+A},&C^2\ge A(B-A)/2.
\end{cases}}
\]

For the randomly phase-shifted \(N\)-point Fourier sampler of the transformed target, its **exact minimax variance** is
\[
\boxed{\inf_{m\in\mathbb R,\,s>0}\;\sup_{\nu\in\mathcal M}\operatorname{Var}(Q_{N,m,s}[\nu])
=\frac{2R_*^{2N}}{1-R_*^{2N}}.}
\]
The infimum is attained uniquely at \((m_*,s_*)\), and the supremum is attained by a single Cauchy component at a specified extreme location and scale. In particular \(0<R_*<1\) and the sharp worst root-mean-square error is asymptotic to \(\sqrt2 R_*^N\) as \(N\to\infty\). The scale \(s_*\) first **decreases** and then **increases** with the allowed location spread \(C\), with a genuine cusp at \(C=\sqrt{A(B-A)/2}\). Before the cusp, both extreme component scales determine the bound; afterwards, **only the narrowest component scale** is active.

By homogeneity this is also the exact minimax **relative variance** for unnormalized nonzero positive mixtures with an unknown mass; the normalized formulation fixes the mass at one without loss of generality. The exact variance for one Poisson kernel is standard Fourier aliasing; the new statement is the sharp all-mixture, all-reference-parameter minimax solution with its active-obstruction transition and independent-of-resolution optimizer.

## Assumptions and scope

The Cauchy density of location \(c\in\mathbb R\), scale \(a>0\), is
\[
p_{c,a}(x)=\frac{a}{\pi((x-c)^2+a^2)}.
\]
Define \(\mathcal M\) as the set of all probability mixtures \(f_\nu(x)=\int p_{c,a}(x)\,d\nu(c,a)\), where \(\nu\) is a Borel probability measure supported on the compact rectangle \(\{(c,a): |c|\le C,\ A\le a\le B\}\). This includes all finite positive mixtures and the point masses representing a single component; negative and complex coefficients are not permitted. More generally, if \(\mu\) is any nonzero finite positive measure on the same rectangle with unknown total mass \(M=\mu(\mathcal R)>0\), the same estimator applied to \(f_\mu\) has expectation \(M\) and the **same sharp minimax relative variance** \(\operatorname{Var}(Q)/M^2\), by applying the probability-mixture theorem to \(\mu/M\). Thus the statement also gives a robust relative-error guarantee for an unknown positive mixture normalizer.

For an arbitrary reference location \(m\in\mathbb R\) and scale \(s>0\), let its inverse Cauchy quantile function be
\[
X_{m,s}(t)=m+s\tan(\pi(t-1/2)),\qquad 0<t<1.
\]
Choose one random shift \(U\sim\operatorname{Unif}[0,1)\), shared by an entire cyclic grid, and define
\[
\boxed{Q_{N,m,s}[\nu](U)=\frac1N\sum_{j=0}^{N-1}
\frac{f_\nu\bigl(X_{m,s}((j+U)/N)\bigr)}{p_{m,s}\bigl(X_{m,s}((j+U)/N)\bigr)}.}
\]
The event of evaluating at an infinite quantile has probability zero, so the rule is defined almost surely. Because \(p_{m,s}(x)\,dx=dt\), one has \(\mathbb E Q_{N,m,s}[\nu]=\int_\mathbb R f_\nu(x)\,dx=1\). We use variance with respect to the single uniform shared shift \(U\), not independently jittered individual sample nodes. This variance is also the squared \(L^2([0,1])\) norm of the Fourier aliasing error after cyclic averaging.

All positive constants and quantifiers above are exact. The optimizer is over **all real reference locations**, not just centered references. The positive mixture class is arbitrary, not restricted to two atoms. Other integrands multiplying the mixture, deterministic phases, and other reference families are outside scope.

## Proof

**Step 1. Cauchy-to-Poisson conjugacy and exact Fourier aliasing.** Fix a target component \(p_{c,a}\). By the Cauchy quantile change of variable, the one-periodic function
\[
h_{m,s;c,a}(t)=\frac{p_{c,a}(X_{m,s}(t))}{p_{m,s}(X_{m,s}(t))}
\]
is a circular Poisson kernel, up to angular rotation and reflection. Explicitly, its Fourier series has coefficients of magnitude \(r^{|k|}\), \(k\in\mathbb Z\), where
\[
\boxed{r^2=r^2(m,s;c,a)=\frac{(c-m)^2+(a-s)^2}{(c-m)^2+(a+s)^2}.}
\]
One can obtain this directly by substituting \(X_{m,s}(t)\), clearing the common \(1+\tan^2(\pi(t-1/2))\) factor, and writing the positive denominator as a linear combination of \(1,\cos 2\pi t,\sin 2\pi t\). Equivalently, the Cayley map from the upper half-plane to the disk sends the target point \(c+ia\) relative to the reference point \(m+is\) to a complex \(w\) with \(|w|=r\); the boundary harmonic-measure density is \((1-|w|^2)/|e^{2\pi it}-w|^2\), possibly with a reflected angular coordinate. Since \(a,s>0\), \(0\le r<1\).

The Fourier series converges absolutely. Averaging on a cyclic grid of size \(N\) deletes every mode except multiples of \(N\), and averaging over \(U\) makes the nonzero surviving characters orthogonal. Therefore
\[
\mathbb E Q_{N,m,s}[\delta_{(c,a)}]=1,
\quad
\operatorname{Var}\bigl(Q_{N,m,s}[\delta_{(c,a)}]\bigr)
=\sum_{\ell\in\mathbb Z\setminus\{0\}}r^{2N|\ell|}
=\frac{2r^{2N}}{1-r^{2N}}.
\]
This is a known Fourier calculation and is not claimed as new.

**Step 2. Positive mixtures add no worse alias than a component.** For arbitrary \(\nu\in\mathcal M\), linearity and compactness permit interchanging the component integral with the grid and with expectation. By Minkowski's inequality in the mean-zero Hilbert space \(L^2(U)\),
\[
\bigl\|Q_{N,m,s}[\nu]-1\bigr\|_{L^2(U)}
\le\int\bigl\|Q_{N,m,s}[\delta_{(c,a)}]-1\bigr\|_{L^2(U)}\,d\nu(c,a)
\le\sup_{|c|\le C,\,A\le a\le B}\sqrt{\frac{2r^{2N}}{1-r^{2N}}}.
\]
Equality of the outer supremum is attained when \(\nu\) is a Dirac measure at a maximizing component. Since \(r\mapsto 2r^{2N}/(1-r^{2N})\) is strictly increasing for \(0<r<1\), minimizing worst variance is equivalent to minimizing \(\max r^2\). This step is essential: the claimed bound is exact even for arbitrary mixtures, not merely an upper estimate.

**Step 3. The globally optimal reference location is uniquely zero.** Write \(d^2=(c-m)^2\). Then
\[
r^2=1-\frac{4as}{d^2+(a+s)^2},
\qquad
\frac{\partial r^2}{\partial d^2}=
\frac{4as}{\bigl(d^2+(a+s)^2\bigr)^2}>0.
\]
For any \(m\), the maximum over \(c\in[-C,C]\) occurs at the farthest endpoint, at distance \(C+|m|\), independently of \(a\). For every fixed \(s>0\), every \(m\ne0\) strictly enlarges the worst ratio relative to \(m=0\). Thus the unique optimum center is \(m_*=0\).

**Step 4. Only the two extreme target scales can obstruct.** Now write
\[
T_a(s)=1-r^2(0,s;C,a)=\frac{4as}{C^2+(a+s)^2}.
\]
For any fixed \(s>0\), differentiation in \(a\) gives
\[
\frac{\partial}{\partial a}\left(\frac{a}{C^2+(a+s)^2}\right)
=\frac{C^2+s^2-a^2}{\bigl(C^2+(a+s)^2\bigr)^2}.
\]
The function first increases and then decreases, so its minimum over \([A,B]\) is attained at \(A\) or \(B\). Hence the robust objective is \(\max r^2=1-\min\{T_A(s),T_B(s)\}\). Each \(T_a(s)\) increases up to its *unique* maximum at \(s=\sqrt{a^2+C^2}\) and decreases thereafter. Equality \(T_A(s)=T_B(s)\), for distinct \(A<B\), is equivalent to
\[
s^2=AB-C^2.
\]
This crossing exists for positive \(s\) exactly when \(C^2<AB\); the \(B\)-constraint is active to its left and the \(A\)-constraint to its right. The complete maximization can therefore be checked by monotonicity on either side.

**Step 5. The sharp phase boundary.** Let \(s_A=\sqrt{A^2+C^2}\). The crossing \(s_0=\sqrt{AB-C^2}\), when it exists, satisfies \(s_0\ge s_A\) exactly when \(2C^2\le A(B-A)\). In this regime, the lower envelope \(\min(T_A,T_B)\) increases up to \(s_0\) and decreases afterwards: its unique maximizer is \(s_0\). If \(2C^2>A(B-A)\), the lower envelope instead increases up to \(s_A\) and decreases afterwards: its unique maximizer is \(s_A\); this remains true if \(C^2\ge AB\), where no positive crossing exists. At equality the two formulas coincide, so the optimizer is always unique.

In the crossing regime, substituting \(C^2=AB-s_0^2\) gives
\[
T_A(s_0)=T_B(s_0)=\frac{4s_0}{A+B+2s_0}.
\]
In the single-active-scale regime, putting \(s_A^2=A^2+C^2\) gives
\[
T_A(s_A)=\frac{2A}{s_A+A}.
\]
Subtracting each expression from one yields exactly the asserted two formulas for \(R_*^2\). Monotonicity of the geometric Fourier tail in \(r\) proves the minimax variance for every integer \(N\ge1\).

**Step 6. Location-spread cusp and asymptotics.** Since \(A<B\), the threshold \(C_*=\sqrt{A(B-A)/2}\) is positive. On \(0<C<C_*\), differentiation gives \(ds_*/dC=-C/\sqrt{AB-C^2}<0\); on \(C>C_*\), it gives \(ds_*/dC=C/\sqrt{A^2+C^2}>0\). Their one-sided derivatives at \(C_*\) have opposite nonzero signs, proving a genuine cusp and the narrow-then-wide response. The positive constant \(R_*<1\) is independent of \(N\), so summing the geometric Fourier tail gives
\[
\frac{2R_*^{2N}}{1-R_*^{2N}}=2R_*^{2N}(1+O(R_*^{2N})),
\quad
\operatorname{RMSE}_{\min\max}=\sqrt2 R_*^N(1+O(R_*^{2N})).
\]
All estimates refer to fixed \(A,B,C\) and \(N\to\infty\).

## Verification

The included `verify.py` is a standalone Python 3 verifier (standard library only). It calculates target/reference Cauchy ratios at quantile-sampled nodes and integrates the squared shifted-grid error over the shift independently of the closed Fourier formula. It compares the integral with the claimed geometric spectral tail, samples arbitrary target mixture measures, tests off-center references, two extreme-scale constraints, the optimizer and both sides of the transition. A fixed random seed makes the test reproducible. Its execution yielded **15,968 successful supplementary assertions**. Finite tests do not prove the universal statements above; Steps 1–6 constitute the proof.

As a concrete illustration, take \(A=1\), \(B=9\), so \(C_*=2\). The unique optimal width equals \(3\) at \(C=0\), decreases to \(\sqrt5\) at \(C=2\), and increases to \(\sqrt{10}\) at \(C=3\). The optimizer does not depend on \(N\), although the exact minimax risk decays exponentially in \(N\).

## Relationship to prior work

Hyvönen and Suzuki (arXiv:2604.27758v1, first public 30 April 2026) treat Möbius-transformed trapezoidal quadrature for polynomial weights; Section 4, Proposition 4.1 covers exact polynomial moments at matched scale for a basic Cauchy-type weight. It neither states this minimax Fourier-aliasing problem over all reference locations and scales nor its location-uncertainty phase boundary. Suzuki, Hyvönen and Karvonen (arXiv:2407.13650v1) developed Möbius quadrature and a randomized full-grid rule in their Section 4, including general Sobolev error estimates. These **methods and the random shift** are prior art, not new ingredients. Potts and Weidensager (arXiv:2608.00260v1, first public 31 July 2026) develop inverse-distribution sampling and Fourier aliasing for general continuous Fourier transforms, with deterministic approximation and analytically optimized tail profiles, but without this exact robust Poisson-family minimax law.

Two specifically comparable published mathematical findings were inspected in full. *Sharp sampling crossover for independently shifted near-boundary Poisson quadrature* derives the known exact single-Poisson shifted-grid variance and a joint near-boundary sampling-rate law, but does not optimize a reference measure against a location-scale rectangle. *Parity-sharp exactness and scale optimization for Cauchy-mixture Möbius trapezoids* considers **deterministic zero-shift** normalization of **centered** finite mixtures and parity-dependent roots, not randomly shifted Fourier-tail risk, unknown locations, or the robust reference-center phase boundary. The present result is therefore not an implication of their stated complete theorems, despite using the same classical Poisson series and Cayley transformation. This is a relative originality comparison, not proof of global publication priority.

## Limitations

The exact theorem concerns a fixed shared random shift of one cyclic sampling grid, positive mixtures of Cauchy densities, and reference densities restricted to the Cauchy location-scale family. It does not optimize over every conceivable sampling density or every randomized algorithm. It does not give a uniform bound for arbitrary additional test functions or for noisy function evaluations, and it does not assert that the best reference for normalized mass is best for every Fourier frequency. Exact minimax aliasing is not the same as exact integration for individual shifts. The phase boundary is for a **rectangular** uncertainty set; other uncertainty geometries may behave differently. General hyperbolic Chebyshev-center literature might contain equivalent geometric reductions under other terminology. Independence and formal external verification have not been established.

## References

1. N. Hyvönen and Y. Suzuki, *Möbius-Transformed Trapezoidal Rule for Polynomial Weights*, arXiv:2604.27758v1, 30 April 2026, https://arxiv.org/pdf/2604.27758 .
2. Y. Suzuki, N. Hyvönen and T. Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650v1, 18 July 2024, https://arxiv.org/html/2407.13650v1 .
3. D. Potts and L. Weidensager, *Approximating the Fourier Transform from Non-equispaced Discrete Samples*, arXiv:2608.00260v1, 31 July 2026, https://arxiv.org/abs/2608.00260 ; author's public full text https://www-user.tu-chemnitz.de/~potts/paper/approxFourierTransform.pdf .
4. *Sharp sampling crossover for independently shifted near-boundary Poisson quadrature*, public mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-sharp-sampling-crossover-for-independently-shifted-near-boundary--40e29c300ddc/RESULT.md .
5. *Parity-sharp exactness and scale optimization for Cauchy-mixture Möbius trapezoids*, public mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-parity-sharp-exactness-and-scale-optimization-for-cauchy-mixture--4c38c0a9043c/RESULT.md .
