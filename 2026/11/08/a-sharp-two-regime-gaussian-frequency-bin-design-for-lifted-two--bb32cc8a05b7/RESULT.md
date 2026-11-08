# A sharp two-regime Gaussian frequency-bin design for lifted two-tone spectrograms

## Finding
For a Gaussian-window short-time Fourier transform of two monochromatic components, the symmetric two-frequency-bin measurement operator admits an explicit four-value real singular spectrum. Its optimal smallest singular value has a unique optimal bin offset and a sharp transition between two design regimes. The transition is at
\[
a_*=\left(\frac{\operatorname{arsinh}(1/\sqrt2)}{4\pi\sqrt3}\right)^{1/2}=0.1739344875\ldots.
\]
The optimizing bins are determined by a unique hyperbolic-equation root below the threshold and by an explicit arcsinh formula above it. This is a theorem about the *linear intensity lifting* in a specified Hilbert--Schmidt and periodic-data norm, not a universal nonlinear noise bound.

## Assumptions and scope
Fix real \(a>0\). Define the Gaussian \(g(t)=e^{-\pi t^2}\) and two monochromatic waves
\[
f_c(t)=c_-e^{-2\pi iat}+c_+e^{2\pi iat},\qquad c_-,c_+\in\mathbb C.
\]
These waves need not belong to \(L^2(\mathbb R)\); the Gaussian short-time transform integral converges absolutely for each wave. Set
\[
V_gf(s,\omega)=\int_{\mathbb R}f(t)g(t-s)e^{-2\pi i\omega t}\,dt,
\qquad T=(2a)^{-1}.
\]
Fix a positive symmetric frequency-bin offset \(x>0\). The data space is \(L^2([0,T],ds/T;\mathbb R)^2\), with the squared norm being the sum of the two normalized integrals. The input is the **real** Hilbert space \(\operatorname{Herm}(2)\) with \(\|H\|_{\mathrm{HS}}^2=\operatorname{tr}(H^2)\). Let
\[
H=\begin{pmatrix}X&Z\\\bar Z&Y\end{pmatrix},\qquad
u=e^{-\pi(x+a)^2},\quad v=e^{-\pi(x-a)^2}.
\]
The measurement \(\mathcal M_{a,x}(H)=(I_{-x},I_{+x})\) is the linear extension from \(H=cc^*\) of the intensities \(|V_gf_c(s,\pm x)|^2\). Explicitly,
\[
\begin{aligned}
I_{+x}(s)&=u^2X+v^2Y+uv(Ze^{-4\pi ias}+\bar Ze^{4\pi ias}),\\
I_{-x}(s)&=v^2X+u^2Y+uv(Ze^{-4\pi ias}+\bar Ze^{4\pi ias}).
\end{aligned}
\]
All optimization and injectivity claims concern the fixed Gaussian, symmetric bin pairs and these norms; they do not optimize over all asymmetric pairs or window functions.

## Proof
**Exact spectrum.** Gaussian integration gives, up to a factor of modulus one,
\[
V_g f_c(s,+x)=u c_-e^{-2\pi ias}+v c_+e^{2\pi ias},
\]
with \(u,v\) interchanged at the negative bin. The three functions \(1,\cos(4\pi as),\sin(4\pi as)\) are mutually orthogonal over one period, and the latter two have squared average \(1/2\). The orthonormal real input coordinates are \(X,Y,\sqrt2\Re Z,\sqrt2\Im Z\). Accordingly, on the diagonal coordinates the measurement has matrix
\[
\begin{pmatrix}u^2&v^2\\v^2&u^2\end{pmatrix}
\]
with singular values \(u^2+v^2\) and \(v^2-u^2\), since \(v>u>0\) for \(a,x>0\). Both off-diagonal coordinates have singular value \(\sqrt2 uv\). The maximal singular value is \(u^2+v^2\), by the arithmetic--geometric mean inequality, and the smallest is
\[
m_a(x)=\min\{D_a(x),B_a(x)\},\quad
D_a(x)=2e^{-2\pi(x^2+a^2)}\sinh(4\pi ax),\quad
B_a(x)=\sqrt2e^{-2\pi(x^2+a^2)}.
\]
Both quantities are strictly positive for \(x>0\), proving linear injectivity and therefore phaseless identifiability up to a common phase on rank-one positive semidefinite matrices.

**Sharp optimization.** The quotient \(D_a(x)/B_a(x)=\sqrt2\sinh(4\pi ax)\) is strictly increasing from zero to infinity. Thus the two branches cross exactly at
\[
x_C(a)=\frac{\alpha}{4\pi a},\qquad \alpha=\operatorname{arsinh}(1/\sqrt2).
\]
The first branch has log derivative
\[
\frac{D'_a(x)}{D_a(x)}=4\pi\bigl(a\coth(4\pi ax)-x\bigr).
\]
The function \(x\mapsto x\tanh(4\pi ax)\) is strictly increasing from zero to infinity. Consequently, \(D_a\) has a unique maximum at the unique positive solution \(x_D\) of \(x_D\tanh(4\pi ax_D)=a\), and \(x_D>a\). The second branch \(B_a\) is strictly decreasing for \(x>0\). Therefore the minimum of the two branches is maximized **uniquely** at
\[
x_{\mathrm{opt}}(a)=\min\{x_D(a),x_C(a)\}.
\]
At the crossover, \(\coth\alpha=\sqrt3\). Hence \(D'_a(x_C)\) has the sign of \(\sqrt3 a-x_C\), and \(x_D\le x_C\) holds precisely for \(a\le a_*\), where
\[
a_*^2=\frac{\alpha}{4\pi\sqrt3}.
\]
This proves the two-regime formula including uniqueness and equality at the critical parameter. If \(a\ge a_*\), evaluating \(B_a(x_C)\) gives the exact optimal value
\[
\sup_{x>0}m_a(x)=\sqrt2\exp\!\left(-2\pi a^2-\frac{\alpha^2}{8\pi a^2}\right).
\]
For \(a\downarrow0\), the root equation implies \(x_D\to(4\pi)^{-1/2}\); Taylor expansion of \(D_a(x_D)\) gives
\[
\sup_{x>0}m_a(x)\sim4\sqrt{\pi/e}\,a.
\]
In the large-separation regime the exact value above is \(\sqrt2e^{-2\pi a^2}(1+O(a^{-2}))\).

**Why one bin cannot suffice.** For a single bin with positive responses \(U,V\), the real linear measurement has one constant Fourier coefficient and one complex oscillatory coefficient, so has rank at most three on four-dimensional \(\operatorname{Herm}(2)\). Indeed the diagonal null direction is \(\operatorname{diag}(V^2,-U^2)\). Even on rank-one inputs, a generic pair \((X,Y,Z)\) is indistinguishable from \((V^2Y/U^2,U^2X/V^2,Z)\). Both triples obey \(|Z|^2=XY\), but they correspond to distinct phase orbits unless a special balancing identity holds. For the two symmetric bins \(x>0\), the positive singular spectrum already proved gives injectivity on the whole Hermitian space.

## Verification
The standalone `CHECKER.py` evaluates the exact singular-value formulas independently of a numerical period quadrature, constructs the full real lifted measurement matrix on an orthonormal Hermitian basis, and checks its SVD in eight separation regimes. It also samples the global optimization curve densely and verifies the predicted root switch and critical constant. The checker is numerical corroboration; the calculus and orthogonality argument above prove the result for all real \(a,x>0\).

Run with Python, NumPy and SciPy: `python CHECKER.py`. Dependencies are documented in `requirements.txt`. The tested offset interval is finite and sampling a grid cannot establish global optimality.

## Relationship to prior work
Alaifari and Wellershoff (first public 2019) established stability estimates for discrete finite-dimensional Gabor phase retrieval using ambiguity coefficients and graph-component phase propagation. Their results do not select optimal pairs of **continuous frequency bins** for a two-monochromatic-wave Gaussian intensity lifting. Wellershoff (2022) proved uniqueness of bandlimited \(L^2(\mathbb R)\) functions from two distinct Gabor frequency lines sampled in time; this is a uniqueness statement without a sharp smallest singular value or optimal symmetric-bin placement. Alaifari, Bartolucci, Steinerberger, and Wellershoff studied the distinction between sampled uniqueness and stability, again without the present two-tone maximin design. Grohs and Liehr (arXiv:2109.02494) prove inversion and stable approximation in Gaussian shift-invariant spaces from frequency-varying samples on a lattice of time slices, not a two-tone symmetric frequency-bin maximin design. Bartusel (2023) characterizes injectivity for full STFT data in \(L^2\) signal classes using support connectedness, not this two-bin quantitative operator. The present calculation addresses a different signal class (two tempered plane waves) and a specifically normalized linear lifting. These contrasts concern the inspected results, not every possible formulation in the wider literature.

## Limitations
This does **not** establish the globally optimal offset among asymmetric bin pairs, nonlinear phase-orbit stability constants, or bounds for broadband \(L^2\) signals, finite-window observations, variable Gaussian width, noisy magnitude rather than intensity data, or other signal families. The Gaussian is normalized to have integral one, not unit \(L^2\) norm; changing its amplitude rescales all singular values. Historical priority of the exact two-tone design transition remains provisional. The computational test is finite; no independent mathematical audit has been undertaken.

## References
1. R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first public 12 January 2019), later *Journal of Fourier Analysis and Applications* 27, 6 (2021), DOI:10.1007/s00041-020-09802-1.
2. M. Wellershoff, *Sampling at twice the Nyquist rate in two frequency bins guarantees uniqueness in Gabor phase retrieval*, arXiv:2206.03946 (8 June 2022), later *Journal of Fourier Analysis and Applications* 29, 7 (2023).
3. R. Alaifari, F. Bartolucci, S. Steinerberger, M. Wellershoff, *On the connection between uniqueness from samples and stability in Gabor phase retrieval*, arXiv:2205.07013 (14 May 2022), later *Sampling Theory, Signal Processing, and Data Analysis* 22, 6 (2024), DOI:10.1007/s43670-023-00079-1.

4. P. Grohs and L. Liehr, *Stable Gabor Phase Retrieval in Gaussian Shift-Invariant Spaces via Biorthogonality*, arXiv:2109.02494 (6 September 2021), later *Constructive Approximation* 59 (2024), 61–111, DOI:10.1007/s00365-023-09629-1.
5. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Zd and Rd*, *Journal of Fourier Analysis and Applications* 29, 53 (2023), DOI:10.1007/s00041-023-10026-2.
