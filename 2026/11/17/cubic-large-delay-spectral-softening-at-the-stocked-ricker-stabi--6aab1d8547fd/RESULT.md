# Cubic large-delay spectral softening at the stocked Ricker stability boundary

## Finding

Consider the stocked, delayed Ricker population recurrence
\[
x_{n+1}=x_n\exp(r-x_{n-N})+h,
\qquad h>0,\quad N\in\{1,2,3,\ldots\}.
\]
At its delay-independent limiting stability threshold,
\[
X=\frac{h+\sqrt{h^2+4h}}{2},\qquad
r_*=X+\log\left(1-\frac{h}{X}\right),
\]
define \(b=X-h=h/X\in(0,1)\) and \(a=1-b\in(0,1)\). The positive equilibrium is \(X\). Write \(\rho_N\) for the spectral radius of its \((N+1)\)-dimensional linearization.

**Theorem.** For every fixed \(h>0\) and every integer \(N\ge1\), all characteristic multipliers lie strictly in the open unit disk. As \(N\to\infty\),
\[
\boxed{\rho_N=1-\frac{a\pi^2}{2b^2N^3}+O_h(N^{-4}).}
\]
For all sufficiently large \(N\), the largest-modulus eigenvalues consist of exactly one simple complex-conjugate pair. Its member in the upper half-plane has phase
\[
\arg\lambda_N=\frac{\pi}{N}-\frac{\pi}{bN^2}+O_h(N^{-3}).
\]
Thus the spectral e-folding time is
\[
\frac{1}{-\log\rho_N}\sim\frac{2b^2}{a\pi^2}N^3,
\]
and the phase oscillation period is \(2N+2/b+O_h(N^{-1})\). For \(h=1\), the coefficient in the spectral-radius gap is exactly \(\pi^2/2\). This resolves the distinction between strict stability for each finite recruitment delay and almost-neutral relaxation as the delay grows.

## Assumptions and scope

The stocking amount \(h\) is held fixed as \(N\to\infty\). The growth parameter equals \(r_*\) exactly; no claim is made for other parameters. Initial histories near \(X\) are considered only when translating the spectral result into nonlinear local stability. All \(O_h\)-constants may depend on this fixed positive \(h\), not on \(N\). Multipliers and phase refer to the one-step companion map; oscillation periods are in generations. The theorem also applies to the abstract polynomial family \(\lambda^{N+1}-a\lambda^N+(1-a)\) for fixed \(0<a<1\).

## Proof

**1. Equilibrium and characteristic polynomial.** Every equilibrium \(x>h\) solves \(r=x+\log(1-h/x)\). Its right side is strictly increasing because its derivative is \(1+h/[x(x-h)]>0\); hence the positive equilibrium is unique for a given \(r\). The defining quadratic relation \(X(X-h)=h\) yields \(b=X-h=h/X\), so \(a=(X-h)/X=1-b\) and \(r_*=X+\log a\). Linearizing at \(X\), with \(u_n=x_n-X\), gives
\[
u_{n+1}=a u_n-Xa u_{n-N}=a u_n-bu_{n-N},
\]
since \(Xa=X-h=b\). Thus \(P_N(\lambda)=\lambda^{N+1}-a\lambda^N+b\).

**2. Strict stability for every finite delay.** At a zero \(\lambda\) of \(P_N\),
\[
b=|\lambda|^N|\lambda-a|.
\]
If \(|\lambda|>1\), then this is at least \(|\lambda|^N(|\lambda|-a)>1-a=b\), impossible. If \(|\lambda|=1\), equality in \(|\lambda-a|\ge1-a\) would force \(\lambda=1\), but \(P_N(1)=2b\ne0\). Therefore \(|\lambda|<1\) for every zero. This already implies local exponential attraction for each fixed \(N\) by the finite-dimensional hyperbolic fixed-point theorem.

**3. A near-unit conjugate pair and its coefficient.** Put \(\epsilon=1/N\) and \(\lambda=\exp(\epsilon z)\). The root equation becomes
\[
\exp(z)\left(\exp(\epsilon z)-a\right)=-b.
\]
Near \((z,\epsilon)=(i\pi,0)\), use the analytic logarithm branch near \(1\), and define
\[
H(z,\epsilon)=z+\log\left(\frac{\exp(\epsilon z)-a}{b}\right)-i\pi.
\]
Here \(H(i\pi,0)=0\) and \(\partial_zH(i\pi,0)=1\). The analytic implicit-function theorem therefore supplies a unique branch \(z_+(\epsilon)\) near \(i\pi\). Expanding through second order gives
\[
z_+(\epsilon)=i\pi-\frac{i\pi}{b}\epsilon
+\left(\frac{i\pi}{b^2}-\frac{a\pi^2}{2b^2}\right)\epsilon^2
+O_h(\epsilon^3).
\]
Its complex conjugate is another branch. Therefore
\[
\log|\lambda_+|=-\frac{a\pi^2}{2b^2N^3}+O_h(N^{-4}),
\qquad
\arg\lambda_+=\frac{\pi}{N}-\frac{\pi}{bN^2}+O_h(N^{-3}).
\]
In particular at least one root has modulus \(1-O_h(N^{-3})\).

**4. No other mode can dominate.** Let \(\lambda_N\) be a root of largest modulus, write \(R_N=|\lambda_N|\) and its principal argument \(\theta_N\). Step 2 and the constructed branch show \(1-O_h(N^{-3})\le R_N<1\), so \(R_N^N=1+O_h(N^{-2})\). The root identity gives \(|\lambda_N-a|=b+O_h(N^{-2})\). Using
\[
|\lambda_N-a|^2=(R_N-a)^2+2aR_N(1-\cos\theta_N)
\]
and \(R_N-a=b+O_h(N^{-3})\), we obtain \(1-\cos\theta_N=O_h(N^{-2})\), hence \(\theta_N=O_h(N^{-1})\). Consequently \(z_N=N\log\lambda_N\) is bounded; its real part is \(O_h(N^{-2})\). Rewriting the root equation on the same local logarithm branch yields
\[
z_N+\log\left(\frac{e^{z_N/N}-a}{b}\right)
=(2m_N+1)i\pi,
\]
for some integer \(m_N\). Since \(z_N\) is bounded, the integers \(m_N\) range over a finite set. For each such fixed integer \(m\), the same analytic implicit-function argument as in step 3 gives
\[
\log|\lambda_{N,m}|=-\frac{a(2m+1)^2\pi^2}{2b^2N^3}+O_{h,m}(N^{-4}).
\]
The two smallest possible values of \((2m+1)^2\) are achieved exactly at \(m=0,-1\), and every other value is at least \(9\). Since only finitely many \(m\) occur among maximal roots, these two branches strictly dominate all the others for large \(N\). The implicit-function theorem gives simplicity and complex conjugacy. Exponentiating the logarithmic modulus expansion yields the asserted \(\rho_N\), and division of \(2\pi\) by the phase expansion gives the stated oscillation period.

**5. Exact example.** With \(h=1\), \(X=(1+\sqrt5)/2\), \(b=(\sqrt5-1)/2\) and \(a=b^2\). Thus \(a/b^2=1\), so \(N^3(1-\rho_N)\to\pi^2/2\). No finite-delay unit-modulus eigenvalue is required or present.

## Verification

The standalone `CHECKER.py` evaluates the characteristic equation and asymptotic coefficient at several large delays with 55-digit arithmetic and verifies the analytic expansion by symbolic series identities. For \(h=1\), observed values of \(-N^3\log|\lambda_+|\) at \(N=100,300,1000\) are approximately \(4.7002710\), \(4.8555050\), and \(4.9108974\); they approach \(\pi^2/2\approx4.9348022\). These finite checks are diagnostics; the proof is the analytic argument above.

## Relationship to prior work

AlSharawi, Cánovas and Kallel's February 2024 treatment analyzes the same arbitrary-delay stocked Ricker family through order-preserving embeddings and establishes a delay-uniform sufficient condition for global stability; its §4.1 compares local thresholds for small delays. AlSharawi and Kallel's July 2024 work focuses on one-delay and periodic stocking, equilibrium stability and Neimark–Sacker behavior. Neither inspected text supplies the cubic spectral-radius asymptotic, its explicit coefficient or the unique dominant high-delay conjugate pair. Kuruklis (1994) establishes general necessary and sufficient stability criteria for the exact abstract linear difference equation, while AlSharawi–Cánovas (2025) gives another general Schur stability method and a fixed two-lag Ricker illustration. Those published stability conditions, which are not asserted as new, do not by themselves supply the sharp large-delay damping coefficient. The general large-delay pseudocontinuous-spectrum picture for continuous-time delay differential equations (Lichtner–Wolfrum–Yanchuk) motivates but does not directly state the discrete stocked-Ricker result. The precise implication comparison, searches and unresolved literature risks are recorded separately in `AUDIT.json`.

## Limitations

This is a sharp **linearized** relaxation-time statement. For each fixed \(N\) it implies local nonlinear exponential attraction in an \(N\)-dependent neighborhood, but no uniform-in-\(N\) nonlinear prefactor, neighborhood size, global basin statement or nonlinear transient formula is proved. The branch comparison proves uniqueness only for sufficiently large delays, not every \(N\). The asymptotic is not uniform as \(h\to0\) or \(h\to\infty\). Broader, especially unindexed, discrete-delay spectral literature may contain an equivalent derivation.

## References

- Z. AlSharawi, J. S. Cánovas and S. Kallel, *Attractors in k-dimensional discrete systems of mixed monotonicity*, arXiv:2402.14127v1 (first public 2024-02-21), especially §4.1. https://arxiv.org/pdf/2402.14127
- Z. AlSharawi and S. Kallel, *Global stability in the Ricker model with delay and stocking*, arXiv:2407.21551v1 (first public 2024-07-31), especially §3. https://arxiv.org/pdf/2407.21551
- S. A. Levin and R. M. May, *A note on difference-delay equations*, Theoretical Population Biology **9** (1976), 178–187. https://doi.org/10.1016/0040-5809(76)90043-5
- S. A. Kuruklis, *The asymptotic stability of \(x_{n+1}-ax_n+bx_{n-k}=0\)*, Journal of Mathematical Analysis and Applications **188** (1994), 719–731. https://doi.org/10.1006/jmaa.1994.1457
- Z. AlSharawi and J. S. Cánovas, *Increasing delay as a strategy to prove stability*, arXiv:2505.11372v1 (2025), §5.1. https://arxiv.org/pdf/2505.11372
- M. Lichtner, M. Wolfrum and S. Yanchuk, *The spectrum of delay differential equations with large delay*, SIAM Journal on Mathematical Analysis **43** (2011), 788–802. https://doi.org/10.1137/090766796
