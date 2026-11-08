# Persistent aging correlations under position-only resetting of Brownian diffusivity

## Finding

A particle whose instantaneous diffusion coefficient is itself the square of an independent Brownian motion has a fundamentally different response to **position-only** Poisson resetting than to resetting both the position and the diffusivity. The position-only protocol has no stationary position distribution, but admits an exact non-Gaussian \(\sqrt t\)-scaled law and a multi-time aging limit with a nonzero, explicitly computable squared-displacement correlation.

Let \(B,W\) be independent standard one-dimensional Brownian motions, \(N\) an independent Poisson process of rate \(r>0\), and \(\Lambda>0\). Define \(\Omega_t=\sqrt2\Lambda B_t\), \(D_t=\Omega_t^2\). Starting at \(X_0=0\), evolve \(dX_t=\sqrt2\Omega_t\,dW_t\) between arrivals of \(N\), and set \(X_t=0\) at every arrival **without changing \(\Omega_t\)**. Using a signed \(\Omega_t\) in the stochastic integral is distributionally equivalent to using the physical coefficient \(|\Omega_t|=\sqrt{D_t}\), conditional on the environment and reset clock.

For any \(0<s_1<\cdots<s_m\), as \(T\to\infty\),
\[
\left(\frac{X_{s_jT}}{\sqrt T}\right)_{j=1}^m
\Rightarrow
\left(2\Lambda B_{s_j}\sqrt{E_j}\,G_j\right)_{j=1}^m,
\]
where \(B\) on the right is a standard Brownian motion, \(E_j\) are independent exponentials of rate \(r\), and \(G_j\) are independent standard normals, with the families mutually independent. The same \(B\) couples every time coordinate, while the microscopic reset ages and driving-noise increments become independent.

At one observation time, \(X_t/\sqrt t\Rightarrow Y\), where \(Y=2\Lambda Z\sqrt E\,G\) for mutually independent \(Z,G\sim N(0,1)\) and \(E\sim\mathrm{Exp}(r)\). Writing \(b=\sqrt2\Lambda/\sqrt r\), this is a product of an independent standard normal and a symmetric Laplace variable of scale \(b\). Its characteristic function is
\[
\phi_Y(k)=\mathbb E\frac{1}{1+b^2k^2 Z^2}
=\frac{\sqrt\pi}{\sqrt2\,b|k|}
\exp\!\left(\frac{1}{2b^2k^2}\right)
\operatorname{erfc}\!\left(\frac{1}{\sqrt2\,b|k|}\right),\quad k\ne0,
\]
with \(\phi_Y(0)=1\). Its positive, continuous-away-from-zero density is
\[
f_Y(x)=\frac{1}{b\sqrt{2\pi}}\int_0^\infty\frac{1}{z}
\exp\!\left(-\frac{z^2}{2}-\frac{|x|}{bz}\right)dz,\quad x\ne0.
\]
It has a logarithmic central singularity and a stretched-exponential tail:
\[
f_Y(x)=\frac{1}{b\sqrt{2\pi}}\log\frac b{|x|}+O(1)\quad(x\to0),
\qquad
f_Y(x)\sim\frac1{b\sqrt3}\left(\frac b{|x|}\right)^{1/3}
\exp\!\left[-\frac32\left(\frac{|x|}{b}\right)^{2/3}\right]\quad(|x|\to\infty).
\]
In particular \(\mathbb P(|X_t|\le R)\to0\) for every fixed \(R<\infty\), so there is no finite stationary position law.

Despite exponential decay of the **linear** position memory, the squared-displacement correlation survives on a macroscopic time ratio. For every \(c>1\),
\[
\boxed{\lim_{t\to\infty}\operatorname{Corr}(X_t^2,X_{ct}^2)=\frac{2}{17c}.}
\]
The corresponding ordinary covariance is exactly \(\mathbb E[X_tX_{t+h}]=e^{-rh}\mathbb E[X_t^2]\) and therefore vanishes on proportional lags. The squared-position correlation comes from the common, unreset Brownian environment, not from shared post-reset particle noise.

## Assumptions and scope

All random processes start at zero. The Poisson clock has constant rate \(r>0\), and its jumps instantaneously reset only \(X\), not \(B\) or \(\Omega\). Brownian drivers and clock are independent. Limits hold for fixed \(\Lambda,r>0\), fixed finite \(m\), and fixed positive observation-time ratios. The limiting squared-correlation formula is for \(c>1\); it must not be extended to \(c=1\), where the correlation is identically one. Differential entropy, first-passage, finite-rate environmental resets, and heavy-tailed reset clocks are not covered.

## Proof

**1. Last reset representation and exact second moments.** Let \(A_t\) be time since the last Poisson arrival (with \(A_t=t\) if there has been none). Then
\[
X_t=2\Lambda\int_{t-A_t}^t B_s\,dW_s.
\]
The age \(A_t\) is independent of \(B,W\) and has the law \(\min(E,t)\) for \(E\sim\mathrm{Exp}(r)\). Conditional Itô isometry yields
\[
M_2(t):=\mathbb E[X_t^2]=4\Lambda^2 J_1(t),\qquad
J_j(t)=\int_0^t e^{-r(t-s)}s^j\,ds.
\]
In particular
\[
J_1(t)=\frac t r-\frac{1-e^{-rt}}{r^2},\qquad
J_2(t)=\frac{t^2}r-\frac{2t}{r^2}+\frac{2(1-e^{-rt})}{r^3},
\]
so \(M_2(t)/t\to4\Lambda^2/r\).

**2. Fourth moment and environmental mixed moment.** Given an age \(A_t=a\), \(X_t\) is centered Gaussian conditional on the entire environment \(B\) with variance \(4\Lambda^2\int_{t-a}^t B_s^2ds\). The Gaussian fourth-moment identity \(\mathbb E[B_s^2B_u^2]=su+2\min(s,u)^2\) gives
\[
M_4(t):=\mathbb E[X_t^4]
=48\Lambda^4\left[3t^2\mathbb E A_t^2-\frac{11}{3}t\mathbb E A_t^3+\frac54\mathbb E A_t^4\right].
\]
Here \(\mathbb E A_t^j=j\int_0^t a^{j-1}e^{-ra}da\), so these formulas are exact for every \(t\ge0\). Because \(\mathbb E A_t^j\to j!/r^j\),
\[
M_4(t)/t^2\to288\Lambda^4/r^2,\qquad
\operatorname{Var}(X_t^2)/t^2\to272\Lambda^4/r^2.
\]
Likewise, by another Gaussian fourth-moment identity, with \(\Omega_t=\sqrt2\Lambda B_t\),
\[
K(t):=\mathbb E[X_t^2\Omega_t^2]
=8\Lambda^4\bigl[tJ_1(t)+2J_2(t)\bigr],\qquad
K(t)/t^2\to24\Lambda^4/r.
\]

**3. Exact two-time moment closure.** Conditional on \((X_t,\Omega_t)=(x,\omega)\), future environmental variance obeys \(\mathbb E\Omega_{t+h}^2=\omega^2+2\Lambda^2h\). The reset/no-reset generator equation for conditional mean squared position is
\[
\mathbb E[X_{t+h}^2\mid X_t=x,\Omega_t=\omega]
=e^{-rh}x^2+\frac{2(1-e^{-rh})}{r}\omega^2
+\frac{4\Lambda^2}{r}\left[h-\frac{1-e^{-rh}}r\right].
\]
Multiplying by \(X_t^2\) and averaging supplies the exact formula
\[
\mathbb E[X_t^2 X_{t+h}^2]
=e^{-rh}M_4(t)+\frac{2(1-e^{-rh})}{r}K(t)
+\frac{4\Lambda^2}{r}\left[h-\frac{1-e^{-rh}}r\right]M_2(t).
\]
At \(h=(c-1)t\), \(c>1\), the preceding limits give
\[
\frac{\mathbb E[X_t^2X_{ct}^2]}{ct^2}\longrightarrow
\frac{16\Lambda^4}{r^2}\left(1+\frac2c\right).
\]
Subtracting the product of second moments and dividing by the square root of the product of the two squared-position variances yields \(2/(17c)\). For the first power, conditioning on the reset/no-reset event and using the martingale property of the driving noise gives \(\mathbb E[X_tX_{t+h}]=e^{-rh}M_2(t)\) exactly.

**4. Joint aging limit.** For each selected time \(s_jT\), replacing \(B_u\) in the post-reset integral by \(B_{s_jT}\) has conditional Itô error with squared expectation bounded by
\[
\frac{4\Lambda^2}{T}\mathbb E\int_{s_jT-A_{s_jT}}^{s_jT}(B_u-B_{s_jT})^2du
=\frac{2\Lambda^2}{T}\mathbb E[A_{s_jT}^2]\le\frac{4\Lambda^2}{r^2T}.
\]
This uses independence of the reset clock and Brownian environment; hence the error vanishes in \(L^2\). The microscopic ages near finitely many macroscopically separated observation times converge jointly to independent rate-\(r\) exponentials: an overlap between two corresponding Poisson windows requires a no-reset interval of length proportional to \(T\), whose probability is exponentially small. Brownian scaling makes \((B_{s_jT}/\sqrt T)_j\) exactly equal in law to \((B_{s_j})_j\). Conditional driving-noise increments on disjoint post-reset windows are independent Gaussian increments of variances equal to their ages. These facts prove the claimed finite-dimensional convergence.

Uniform integrability for the required polynomial moments follows from conditional Gaussian moment bounds, \((\int_{t-A}^tB_s^2ds)^q\le A^{q-1}\int_{t-A}^t|B_s|^{2q}ds\), the bounded exponential-age moments, and \(\mathbb E|B_s|^{2q}\le C_q t^q\) for \(s\le t\). This justifies, independently of the exact closure, passage to second/fourth and mixed fourth moments in the aging limit.

**5. One-time distribution and its boundaries.** Given \(Z\), mixing a centered normal with conditional variance \(4\Lambda^2Z^2 E\) over an independent exponential \(E\) yields a centered Laplace variable of scale \(b|Z|\). Integrating over \(|Z|\) gives the displayed density and characteristic function; the complementary-error-function representation follows by the elementary Gaussian rational integral. Splitting the density integral between \(|x|/b\) and a fixed small positive constant gives the logarithmic singularity. For the tail, the exponent \(z^2/2+|x|/(bz)\) has its unique nondegenerate minimum at \(z=(|x|/b)^{1/3}\); a one-dimensional Laplace expansion yields the coefficient and exponent displayed above. Because \(Y\) is continuous and has no atom at zero, the nondegenerate \(X_t/\sqrt t\) weak limit implies \(\mathbb P(|X_t|\le R)\to0\), precluding a finite stationary position distribution.

## Verification

The standalone `verify.py` evaluates exact moments in two independent representations, the characteristic function against Gaussian quadrature, the density against an independent logarithmic-coordinate integral, finite-time cross-moment identities, and convergence of the squared-correlation formula at several time ratios. To run it: `python verify.py`. Standard-library Python 3 suffices. Its finite numerical checks do not establish the weak limit or novelty; those rely respectively on the proof above and the comparison below.

## Relationship to prior work

Santra, Basu and Sabhapandit (arXiv:2205.00549, first public 2022-05-01) introduce the same Brownian-squared stochastic diffusivity, derive free ballistic spreading and stationary laws under *simultaneous* reset of position and diffusivity, and explicitly list position-only resetting as an open protocol in their concluding discussion. Their fully renewed reset process cannot yield the present nonstationary scaling law or persistent shared-environment aging correlation. Bodrova, Chechkin and Sokolov (arXiv:1812.05664, first public 2018-12-13) analyze *nonrenewal* position-only resetting for a deterministic time-dependent diffusion coefficient; its Gaussian increments do not supply the Brownian-volatility normal-times-Laplace mixing or the nonzero macroscopic squared-memory law. Di Bello et al. (2023) use the term *partial resetting* for multiplication of the position by a fixed factor in a spatially homogeneous Markov or Lévy process, rather than resetting only the position coordinate of an evolving stochastic-diffusivity pair. These comparisons distinguish scope and implication; no claim of globally certified novelty is made.

## Limitations

The result requires independent Poisson position resets and an unbounded, Brownian-square diffusivity. The singular limit as the volatility-reset rate tends to zero is not uniform in observation time. The asymptotic two-time law assumes \(c>1\) fixed, rather than a fixed lag or the diagonal \(c=1\). No claim is made about other environmental processes, higher-dimensional spatial diffusion, thermal equilibrium, or robustness to feedback resets. The mathematical argument is analytical and has not received independent expert review. Bibliographic searches and the inspected sources do not eliminate every possible unindexed equivalent or general theorem.

## References

1. I. Santra, U. Basu, S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (2022-05-01), https://arxiv.org/pdf/2205.00549 . Especially Eqs. (1)–(3), (35)–(39), and Section 7.
2. A. S. Bodrova, A. V. Chechkin, I. M. Sokolov, *Non-renewal resetting of scaled Brownian motion*, arXiv:1812.05664v2 (originally public 2018-12-13), https://arxiv.org/pdf/1812.05664 . Especially Eqs. (1)–(3), (15), (18)–(23) and Sections III–V.
3. M. Magdziarz, K. Taźbierski, *Stochastic representation of processes with resetting*, arXiv:2310.06416 (2023), https://arxiv.org/abs/2310.06416 . Background on jump-diffusion representations, not a source of the explicit Brownian-volatility aging result.
4. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski, R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, New Journal of Physics (2023), DOI:10.1088/1367-2630/aced1d, https://www.agnld.uni-potsdam.de/papers/2023_DiBCheHarPalMe_NJP.pdf . Especially Sections 1–2, where partial resetting means a multiplicative state reset.
