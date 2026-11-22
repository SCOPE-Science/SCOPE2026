# A rational-window spectral boundary layer for periodic boxcar averaging

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry normalized Lebesgue measure, and let \(H=L^2_0(\mathbb T;\mathbb C)\). For \(0<\alpha<1\) define the *periodic boxcar average* \(A_\alpha:H\to H\) by
\[
(A_\alpha f)(x)=\frac1\alpha\int_0^\alpha f(x+u)\,du.
\]
Write \(s_1(A_\alpha)\ge s_2(A_\alpha)\ge\cdots>0\) for its nonzero singular values, counted with multiplicity, and \(N_\alpha(t)=\#\{k:s_k(A_\alpha)>t\}\) for \(t>0\).

**Fixed-window arithmetic law.** For every \(0<\alpha<1\),
\[
\lim_{t\downarrow0}tN_\alpha(t)=\lim_{k\to\infty}ks_k(A_\alpha)=C(\alpha),\quad
C(\alpha)=\begin{cases}
\displaystyle\frac{4}{\pi^2\alpha},&\alpha\notin\mathbb Q,\\[4pt]
\displaystyle\frac{2}{\pi\alpha b}\cot\frac{\pi}{2b},&\alpha=a/b\in\mathbb Q\ \text{in lowest terms},\quad b\ge2.
\end{cases}
\]
In particular \(A_\alpha\in\mathcal S_p\) exactly when \(p>1\), for \(p>0\) (interpreting quasi-Schatten classes if \(p<1\)), and
\[
\lim_{p\downarrow1}(p-1)\sum_{k\ge1}s_k(A_\alpha)^p=C(\alpha).
\]
The normalized coefficient \(\alpha C(\alpha)\) is strictly lower at every rational window length than its common irrational value.

**Critical rational-detuning law.** Fix coprime integers \(1\le a<b\), let \(\alpha_0=a/b\), fix \(\lambda\in\mathbb R\), and set \(\alpha(t)=\alpha_0+\lambda t\) (which belongs to \((0,1)\) for all sufficiently small \(t>0\)). Then the following limit exists *for every* real \(\lambda\), without any Diophantine assumption:
\[
\boxed{\lim_{t\downarrow0}tN_{\alpha(t)}(t)=F_{a/b}(\lambda):=\frac{2}{\pi\alpha_0 b}\sum_{r=0}^{b-1}\int_0^1\mathbf 1\!\left\{\left|\sin\pi\!\left(\frac{ra}{b}+\frac{\lambda u}{\pi\alpha_0}\right)\right|>u\right\}\,du.}
\]
The function \(F_{a/b}\) is continuous and even, with
\[
F_{a/b}(0)=\frac{2}{\pi\alpha_0 b}\cot\frac{\pi}{2b},\qquad
\lim_{|\lambda|\to\infty}F_{a/b}(\lambda)=\frac4{\pi^2\alpha_0}.
\]
This is a finite-resolution transition between rational and irrational spectral densities.

**A strict resonance dip at the half-circle window.** With \(\alpha_0=1/2\), for every \(0\le|\lambda|\le1/2\),
\[
F_{1/2}(\lambda)=\frac2\pi\,y_{|\lambda|},\qquad
y_{|\lambda|}\in(0,1],\qquad y_{|\lambda|}=\cos(2|\lambda|y_{|\lambda|}).
\]
There is exactly one such root. Hence \(F_{1/2}(\lambda)<F_{1/2}(0)=2/\pi\) whenever \(0<|\lambda|\le1/2\), although \(\lim_{|\lambda|\to\infty}F_{1/2}(\lambda)=8/\pi^2>2/\pi\). In fact \(F_{1/2}(\lambda)=(2/\pi)(1-2\lambda^2+O(\lambda^4))\) as \(\lambda\to0\). The crossover therefore is not monotone in detuning magnitude.

## Assumptions and scope
The circle has circumference one and \(L^2\) uses normalized arclength. The zero Fourier mode is excluded: on full \(L^2\), it contributes the single singular value \(1\), which does not alter any displayed limit. The operator is linear over complex scalars; on real mean-zero \(L^2\) the sine/cosine multiplicities coincide. All limits are taken for fixed \(\alpha\) or fixed \((a,b,\lambda)\) as specified. The near-rational result is a *joint* limit, not the fixed-window law applied to a moving window.

## Proof
**1. Exact spectrum and counting.** The orthonormal Fourier vectors \(e_n(x)=e^{2\pi i n x}\), \(n\in\mathbb Z\setminus\{0\}\), diagonalize \(A_\alpha\), with multipliers
\[
m_n(\alpha)=e^{\pi i n\alpha}\frac{\sin(\pi n\alpha)}{\pi n\alpha}.
\]
Therefore \(A_\alpha\) is compact and normal, and the nonzero singular multiset consists of two copies of \(\lvert\sin(\pi n\alpha)\rvert/(\pi n\alpha)\), \(n=1,2,\ldots\), with vanishing terms omitted. Thus
\[
N_\alpha(t)=2\sum_{n\ge1}\mathbf1\!\{\lvert\sin(\pi n\alpha)\rvert>\pi\alpha nt\}.
\tag{1}
\]
The sum is finite since \(n\le(\pi\alpha t)^{-1}\) for every included term. For rational \(\alpha=a/b\), infinitely many terms vanish, but infinitely many remain positive because \(b\ge2\).

**2. Fixed windows.** Put \(h=\pi\alpha t\) and \(G(u,x)=\mathbf1\{\lvert\sin(\pi x)\rvert>u\}\). For \(u\in[0,1]\), this is a bounded Riemann-integrable function on \([0,1]\times\mathbb T\), because its boundary consists of measure-zero curves. For irrational \(\alpha\), equidistribution of \(\{n\alpha\}\), applied on each of finitely many macroscopic blocks of integers and followed by a block-mesh refinement, gives
\[
\lim_{h\downarrow0}h\sum_{n\ge1}G(nh,\{n\alpha\})
=\int_0^1\int_0^1G(u,x)\,dx\,du
=\int_0^1\lvert\sin(\pi x)\rvert\,dx=\frac2\pi.
\]
The block step can be established first for products of continuous functions of \(u\) and \(x\), then by upper/lower rectangle approximations since the discontinuity set has product measure zero. Equation (1) yields \(C(\alpha)=4/(\pi^2\alpha)\).

If \(\alpha=a/b\) in lowest terms, split \(n\) into its \(b\) residue classes. Each residue is a regular mesh with spacing \(bh\), whence
\[
\lim_{h\downarrow0}h\sum_{n\ge1}G(nh,\{na/b\})
=\frac1b\sum_{r=0}^{b-1}\int_0^1G(u,ra/b)\,du
=\frac1b\sum_{r=1}^{b-1}\sin\frac{\pi r}{b}
=\frac1b\cot\frac\pi{2b}.
\]
The last identity follows from summing the finite sine progression. Substitution in (1) proves the rational coefficient. The strict inequality \(b^{-1}\cot(\pi/(2b))<2/\pi\) follows from \(\cot z<1/z\) for \(0<z<\pi/2\).

**3. Critical detuning.** Let \(\alpha(t)=\alpha_0+\lambda t\), and set \(h_0=\pi\alpha_0t\). On integers \(n\equiv r\pmod b\),
\[
\{n\alpha(t)\}=\left\{\frac{ra}{b}+\frac{\lambda}{\pi\alpha_0}(nh_0)\right\},\qquad
\pi\alpha(t)nt=(1+\lambda t/\alpha_0)(nh_0).
\]
Each residue contributes a Riemann sum of spacing \(bh_0\). Its indicator boundary is contained in the zero set of the real-analytic function \(u\mapsto \sin^2\pi(ra/b+\lambda u/(\pi\alpha_0))-u^2\), which is not identically zero on \([0,1]\); hence the boundary has zero length. The upper cutoff converges to \(u=1\). Taking residue-class Riemann limits in (1) gives the boxed formula.

For fixed \(\lambda\), the same measure-zero boundary and dominated convergence give continuity in \(\lambda\). The substitution \(r\mapsto-r\) modulo \(b\), together with the evenness of \(\lvert\sin\pi x\rvert\), proves \(F(-\lambda)=F(\lambda)\). At \(\lambda=0\), the constant is the rational value. As \(|\lambda|\to\infty\), oscillatory averaging in the continuous variable \(u\) yields
\[
\int_0^1G\left(u,ra/b+\frac{\lambda u}{\pi\alpha_0}\right)du
\longrightarrow\int_0^1\int_0^1G(u,x)\,dx\,du=\frac2\pi
\]
for every residue, by continuous periodic approximation away from the measure-zero boundary. Summing proves the irrational-end value.

**4. Half-window dip and Schatten consequences.** For \(\alpha_0=1/2\), the two integrands in the boxed formula become \(\mathbf1\{\lvert\sin(2\lambda u)\rvert>u\}\) and \(\mathbf1\{\lvert\cos(2\lambda u)\rvert>u\}\). For \(0\le\lambda\le1/2\), the sine event is empty because \(\sin(2\lambda u)\le2\lambda u\le u\). The cosine is positive, strictly decreasing and crosses \(u\) at the unique solution \(y_\lambda=\cos(2\lambda y_\lambda)\). Integration gives \(F_{1/2}(\lambda)=2y_\lambda/\pi\); strict decrease away from zero follows. Implicit expansion gives \(y_\lambda=1-2\lambda^2+O(\lambda^4)\), and the nonmonotone conclusion follows from \(8/\pi^2>2/\pi\).

Finally, the positive constant limit \(tN_\alpha(t)\to C(\alpha)\) is equivalent by monotonicity of the counting function to \(ks_k\to C(\alpha)\). Comparison with the harmonic sequence gives \(\mathcal S_p\) membership and the asserted \(p\downarrow1\) Abelian limit (split the series into finitely many initial terms and a tail bounded between \((C\pm\varepsilon)^pk^{-p}\)).

## Verification
The accompanying standalone checker calculates the exact Fourier multiplier and the threshold count using deterministic frequency truncation at \(\lfloor(\pi\alpha t)^{-1}\rfloor\), compares several fixed rational and irrational windows with their predicted limits, and checks the critical half-window \(\lambda\)-scaling against an independently bisected root of \(y=\cos(2\lambda y)\). It also checks symmetry and source-formula normalization. Numerical examples support, but are not used in place of, the proofs above.

## Relationship to prior work
Johnstone and Raimondo's *Periodic boxcar deconvolution and Diophantine approximation* (Annals of Statistics, 2004; arXiv first version dated 2005-03-29) uses this exact boxcar Fourier multiplier and establishes the rational-kernel obstruction and Diophantine-dependent minimax deconvolution rates. Those facts are established prior art. Its main theorems concern noise-dependent statistical minimax risks over smoothness classes, not the ordered singular-value counting limit or the joint critical \(\alpha(t)=a/b+\lambda t\) detuning formula. The present statement does not claim novelty for the multiplier, Weyl equidistribution, or the abstract rearrangement/Abelian principles.

Dron and Zhuk's archival studies of modified Steklov averages address sharp approximation estimates and moduli of continuity. These are related operator families but do not on the available inspected abstract establish the present spectral-detuning limit. General periodic trace and operator spectral-asymptotic techniques offer additional comparisons; none of the examined records established the explicit moving-parameter crossover or its nonmonotone half-window resonance dip. An unindexed earlier equivalent, including in statistical inverse-problem literature, remains a risk.

## Limitations
The law is for a one-dimensional unit circle, the rectangular window kernel, normalized \(L^2\), and frequencies away from the constant mode. It supplies limiting coefficients, not uniform error bounds in window length, a convergence rate for arbitrary irrational windows, or noisy statistical minimax risks. The critical detuning parameter must remain fixed as the threshold tends to zero; no uniform two-parameter limit is claimed.

## References
1. I. M. Johnstone and M. Raimondo, *Periodic boxcar deconvolution and diophantine approximation*, Annals of Statistics 32 (2004), 1781–1804; openly available full paper arXiv:math/0503663v1, posted 2005-03-29, https://arxiv.org/pdf/math/0503663.
2. I. M. Johnstone, G. Kerkyacharian, D. Picard, M. Raimondo, *Wavelet deconvolution in a periodic setting*, Journal of the Royal Statistical Society Series B 66 (2004), 547–573, https://doi.org/10.1111/j.1467-9868.2004.02056.x.
3. V. O. Dron and V. V. Zhuk, *On approximation of periodic functions by modified Steklov averages in \(L^2\)*, Zap. Nauchn. Sem. POMI 429 (2014), 20–33, https://www.mathnet.ru/eng/znsl6064.
4. Weyl equidistribution theorem for irrational rotations (classical; used only in its standard elementary form).
