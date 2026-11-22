# The sharp \(N^{-1}\) recovery scale for monotonicity of Fourier-cutoff circle heat kernels

## Finding
Let the unit-diffusivity heat kernel on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) be represented, without a normalization factor, by
\[
H_t(\theta)=1+2\sum_{k=1}^{\infty}e^{-tk^2}\cos(k\theta),\qquad t>0.
\]
For an integer cutoff \(N\ge1\) and \(t\ge0\), define its symmetric Fourier projection
\[
H_{N,t}(\theta)=1+2\sum_{k=1}^{N}e^{-tk^2}\cos(k\theta)
\]
and its *eventual strict angular-monotonicity horizon*
\[
T_N=\inf\big\{a\ge0:\ H_{N,t}'(\theta)<0\text{ for every }t\ge a\text{ and every }0<\theta<\pi\big\}.
\]
Then every \(T_N\) is finite and
\[
\boxed{\lim_{N\to\infty}NT_N=\frac\pi2.}
\]
More explicitly, for every fixed \(c>\pi/2\), there exists \(N_c\) such that \(H_{N,t}\) is strictly decreasing throughout \((0,\pi)\) for every \(N\ge N_c\) and **every** \(t\ge c/N\). Conversely, for every fixed \(0<c<\pi/2\), every sufficiently large \(N\) has an angle \(\theta_N\in(0,\pi)\) with \(H'_{N,c/N}(\theta_N)>0\). This holds for both parity classes of \(N\). For the latter failure, one may choose
\[
\theta_N=\pi-\frac{\alpha_N}{N},\qquad
\alpha_N=\begin{cases}\pi/2,&N\text{ even},\\3\pi/2,&N\text{ odd}.\end{cases}
\]
The theorem concerns pointwise *angular shape preservation* rather than nonnegativity of the heat kernel or positivity of a discrete-grid matrix.

## Assumptions and scope
The circle has circumference \(2\pi\), the Laplacian is \(\partial_\theta^2\), and diffusivity is exactly one. The coefficient of the constant Fourier mode is one and both modes \(\pm k\) are retained for each \(1\le k\le N\); there is no halved Nyquist mode. Strict monotonicity is asserted only for \(0<\theta<\pi\), as the derivative necessarily vanishes at the two symmetry endpoints. The time \(T_N\) is an *eventual* horizon, not an assertion that the monotonicity set at finite \(N\) is a single interval. No claim about the exact finite-\(N\) value of \(T_N\) is made.

## Proof
Write
\[
F_t(\theta)=-\tfrac12H'_t(\theta)=\sum_{k\ge1}ke^{-tk^2}\sin(k\theta),\quad
F_{N,t}(\theta)=-\tfrac12H'_{N,t}(\theta)=\sum_{k=1}^{N}ke^{-tk^2}\sin(k\theta).
\]
Thus the desired angular monotonicity is exactly \(F_{N,t}(\theta)>0\) for every \(0<\theta<\pi\).

**1. Uniform lower bound for the untruncated derivative.** The Jacobi triple product, with \(q=e^{-t}\), gives
\[
H_t(\theta)=\prod_{m=1}^{\infty}(1-q^{2m})
 (1+2q^{2m-1}\cos\theta+q^{4m-2}).
\]
All factors in the second parentheses are strictly positive. Logarithmic differentiation, valid at each fixed \(t>0\), yields the exact identity
\[
F_t(\theta)=H_t(\theta)\sin\theta
\sum_{m=1}^{\infty}\frac{q^{2m-1}}
{1+2q^{2m-1}\cos\theta+q^{4m-2}}.
\]
For \(0<t\le1\), its first summand is at least \(q/(1+q)^2\ge e^{-1}/(1+e^{-1})^2\). Meanwhile Poisson summation gives
\[
H_t(\theta)=\sqrt{\frac\pi t}\sum_{m\in\mathbb Z}
 e^{-(\theta-2\pi m)^2/(4t)}
\ge\sqrt{\frac\pi t}\,e^{-\pi^2/(4t)}
\qquad(0\le\theta\le\pi).
\]
Therefore an absolute \(b>0\), for instance
\(b=\sqrt\pi e^{-1}/(1+e^{-1})^2\), satisfies
\[
F_t(\theta)\ge b\,t^{-1/2}e^{-\pi^2/(4t)}\sin\theta
\quad(0<t\le1,\ 0<\theta<\pi).\tag{1}
\]
This is a quantitative version of strict radial monotonicity of the full heat kernel, with the crucial antipodal Gaussian exponent.

**2. Sufficient times.** From \(|\sin(k\theta)|\le k\sin\theta\),
\[
|F_t(\theta)-F_{N,t}(\theta)|
\le\sin\theta\sum_{k>N}k^2e^{-tk^2}.
\]
Fix \(c>0\). For \(t\ge c/N\), substitute \(k=N+j\) and bound
\[
\sum_{k>N}k^2e^{-tk^2}
\le e^{-tN^2}\sum_{j=1}^{\infty}(N+j)^2e^{-2cj}
\le C_cN^2e^{-tN^2}.\tag{2}
\]
For \(c/N\le t\le1\), the ratio of (2) to (1), after cancelling \(\sin\theta\), is bounded by
\[
C'_cN^2\sqrt t\exp\left(-N^2t+\frac{\pi^2}{4t}\right).
\]
Its logarithmic derivative in \(t\) is \(1/(2t)-N^2-\pi^2/(4t^2)<0\) for \(0<t\le1\). Hence its maximum in this interval is at \(t=c/N\), and the maximum is at most
\[
C''_cN^{3/2}\exp\left[-N\left(c-\frac{\pi^2}{4c}\right)\right].\tag{3}
\]
If \(c>\pi/2\), (3) tends to zero. Consequently, for all sufficiently large \(N\), \(F_{N,t}>0\) simultaneously at all angles and all \(c/N\le t\le1\).

For \(t\ge1\), separate the first frequency and apply the same sine bound:
\[
F_{N,t}(\theta)\ge e^{-t}\sin\theta
\left(1-\sum_{k=2}^{\infty}k^2e^{-(k^2-1)t}\right).
\]
For integers \(k\ge2\), \(k^2\le4^{k-1}\) and \(k^2-1\ge3(k-1)\). Thus for \(t\ge1\) the sum is at most
\[
\sum_{j=1}^{\infty}4^je^{-3j}=\frac{4e^{-3}}{1-4e^{-3}}<1.
\]
So \(F_{N,t}>0\) for every \(N\ge1\) at every \(t\ge1\). This also proves the finiteness of each eventual horizon and, with (3), \(\limsup_{N\to\infty}NT_N\le\pi/2\).

**3. Necessary times and parity-selected negative derivative.** Fix \(0<c<\pi/2\), put \(t=c/N\), and select the angle \(\theta_N=\pi-\alpha_N/N\) given in the finding. The omitted sine-frequency tail is
\[
R_N=F_{c/N}(\theta_N)-F_{N,c/N}(\theta_N)
=\sum_{j=1}^{\infty}(N+j)
 e^{-\frac cN(N+j)^2}
(-1)^{N+j+1}\sin\big(\alpha_N(1+j/N)\big).
\]
Dividing by \(Ne^{-cN}\), all summands have the summable majorant \((1+j)e^{-2cj}\), so dominated convergence along each parity subsequence gives
\[
\frac{R_N}{Ne^{-cN}}\longrightarrow
(-1)^{N+1}\sin\alpha_N
\sum_{j=1}^{\infty}(-1)^je^{-2cj}
=\frac1{1+e^{2c}}>0.\tag{4}
\]
Here the parity-dependent sign in the first expression is constant along each subsequence and \((-1)^N\sin\alpha_N=1\). For the full derivative, differentiating the periodized Gaussian and using \(\theta_N=\pi-O(N^{-1})\) gives the bound
\[
0<F_{c/N}(\theta_N)
\le C_cN^{3/2}\exp\left(-\frac{\pi^2N}{4c}\right).\tag{5}
\]
Indeed the two nearest Gaussian images have distances \(\pi+O(N^{-1})\) and all other images are exponentially smaller; differentiating contributes a factor of order \(N^{3/2}\). Since \(\pi^2/(4c)>c\), (5) is \(o(Ne^{-cN})\). Equation (4) then gives \(F_{N,c/N}(\theta_N)=F_{c/N}(\theta_N)-R_N<0\) for all sufficiently large \(N\), for each parity. Equivalently \(H'_{N,c/N}(\theta_N)>0\). Thus \(\liminf_{N\to\infty}NT_N\ge\pi/2\), which completes the proof. \(\square\)

## Verification
The standalone finite-arithmetic diagnostic `verify.py` uses Python 3 and `mpmath` (90 decimal digits). It checks the Fourier/image formulas and Jacobi product, confirms the normalized omitted-tail limit at both parities, confirms the negative derivative at selected angles for times \(1.3/N\), and samples positive derivatives at \(1.7/N\), as well as finite derivative identities. The executed diagnostic returned **585 passed assertions**. For example \(F_{40,1.3/40}(\pi-\pi/80)\approx-7.1914668059\cdot10^{-23}\), while \(F_{40,1.7/40}(\pi-\pi/80)\approx3.8305127317\cdot10^{-23}\). Finite-precision samples do not prove uniform positivity or the infinite-cutoff asymptotic; the analytic bounds and dominated convergence above do.

## Relationship to prior work
Alonso-Orán, Chamizo, Martínez and Mas prove geodesic radial monotonicity for the *untruncated* heat kernel, with their first public preprint dated 2018-07-29; this gives the natural shape-preservation question but not a cutoff recovery scale. Dong Li (first public 2021-07-20) analyzes positivity and effective maximum principles for Fourier spectral methods; Sections 1–2 and Appendix B of the public full text concern kernel/operator norms and Fourier heat truncation, not a uniform angular derivative sign or its sharp constant. A published finite-grid Fourier-collocation result, *A sharp \(N^{-1}\) positivity-recovery horizon for Fourier-collocation heat flow* (2026), has an analogous exponential competition but tests **entrywise nonnegativity on sampled grid points** with a single Nyquist mode; its conclusion does not imply strict decreasingness of the distinct, symmetrically truncated continuous trigonometric polynomial on every angle. The grid-node count there is not the frequency cutoff used here. The present theorem is a distinct shape-preservation statement for both parity classes, not a rephrasing of sampled positivity.

## Limitations
The result establishes the leading sharp constant, not a finite-cutoff closed form, a second-order asymptotic, or a proof that the monotone-time set is connected. Its scope is the exact symmetric Fourier partial sum of the one-dimensional periodic Gaussian heat kernel, not Fourier collocation, general manifolds, different spectral multipliers, or discrete time integrators. Specialist priority may depend on older results formulated as eventual unimodality of truncated theta series; the literature comparison is best-knowledge, not a proof of uniqueness.

## References
1. D. Alonso-Orán, F. Chamizo, Á. D. Martínez, A. Mas, *Pointwise monotonicity of heat kernels*, arXiv:1807.11072, first submitted 2018-07-29, https://arxiv.org/abs/1807.11072 . Relevant: Theorem 1 and the proof of radial monotonicity.
2. Dong Li, *Effective maximum principles for spectral methods*, arXiv:2107.09438, first submitted 2021-07-20, https://arxiv.org/html/2107.09438v1 . Relevant: Sections 1–2 and Appendix B.
3. *A sharp \(N^{-1}\) positivity-recovery horizon for Fourier-collocation heat flow* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-n-1-positivity-recovery-horizon-for-fourier-collocation--d4274dc28d8b/RESULT.md . Relevant: Finding and proof, with different discrete-grid predicate and normalization.
