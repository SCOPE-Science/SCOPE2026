# Boundary-notch transition for Fourier Lebesgue constants

## Finding
For every fixed nonnegative integer \(j\), put \(D_n(t)=\sum_{k=-n}^n e^{ikt}\), \(K_{n,j}(t)=D_n(t)-e^{i(n-j)t}\) (\(n\ge j\)), and use normalized Haar measure on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Let
\[
  h(s)=\frac1{2\pi}\int_0^{2\pi}|1-se^{i\phi}|\,d\phi,\qquad s\ge0.
\]
The following exact edge-notch limit exists for every \(j\):
\[
  \boxed{\lim_{n\to\infty}(\|K_{n,j}\|_1-\|D_n\|_1)=C_j
  =\frac1\pi\int_0^\pi\frac{h(|1-e^{it}+e^{i(j+1)t}|)-4/\pi}{2\sin(t/2)}\,dt.}
\]
The integrand is integrable at zero in its bounded-extension sense. At the exact spectral edge, \(C_0=0\); deleting the next-to-edge frequency has a strictly positive limit \(C_1>0\). In particular, there is a discontinuous-in-offset transition between the edge and the first interior notch, although both projected kernels have the same leading logarithmic norm growth. The explicit numerical quadrature gives \(C_1\approx0.1991\); the mathematical result does not require this approximation.

## Assumptions and scope
The offset \(j\) is fixed before the bandwidth \(n\) tends to infinity, \(n\) is an integer tending through positive values, and deletion removes exactly one frequency \(n-j\) from the symmetric band \([-n,n]\). No conclusion is claimed when \(j\) grows with \(n\). All displayed norms are \(\|f\|_1=(2\pi)^{-1}\int_{-\pi}^{\pi}|f(t)|dt\).

## Proof
**Exact reduction.** For \(z=e^{it}\ne1\), the geometric-sum identity gives
\[
 D_n(t)=z^{-n}\frac{1-z^{2n+1}}{1-z},\quad
 K_{n,j}(t)=z^{-n}\frac{1-z^{2n-j}H_j(z)}{1-z},\qquad H_j(z)=1-z+z^{j+1}.
\]
Therefore the difference of absolute values is
\[
 \frac{|1-e^{i(2n-j)t}H_j(e^{it})|-|1-e^{i(2n+1)t}|}{|1-e^{it}|}.
\]
**Averaging and the singularity.** For each fixed \(\epsilon>0\), these numerators define continuous functions of \((t,\phi)\) on \([\epsilon,2\pi-\epsilon]\times\mathbb T\). The elementary oscillatory averaging lemma states that for any such continuous \(F\), \(\int F(t,m t)dt\to\int(2\pi)^{-1}\int F(t,\phi)d\phi\,dt\) as the integer \(|m|\to\infty\); prove this first for trigonometric monomials in \(\phi\) using Riemann–Lebesgue and then by uniform trigonometric approximation. Apply separately to both terms, since their fast frequencies both diverge. The elementary reverse-triangle inequality gives \(\big||K_{n,j}(t)|-|D_n(t)|\big|\le1\) *uniformly*; hence excluded arcs of total length \(2\epsilon\) contribute at most \(\epsilon/\pi\) to the normalized difference. Moreover, because \(|H_j(e^{it})-1|=|e^{i(j+1)t}-e^{it}|\le j|e^{it}-1|\), and \(h\) is 1-Lipschitz, the limiting quotient is bounded near zero for fixed \(j\). Let \(\epsilon\downarrow0\). Conjugation symmetry supplies the displayed integral on \([0,\pi]\), while \(h(1)=(2\pi)^{-1}\int|1-e^{i\phi}|d\phi=4/\pi\).

**The edge and first interior notch.** Since \(H_0(z)=1\), the first assertion is exact. For \(j=1\), the identity \(|1-e^{it}+e^{2it}|=|1-2\cos t|\) holds. Write \(r(t)=|1-2\cos t|\), \(d(t)=2\sin(t/2)\). The function \(h\) is 1-Lipschitz, nondecreasing for \(s\ge0\) (the circular mean of the modulus of an analytic function), and obeys \(h(s)\ge s\) by Jensen's inequality. Therefore the negative contribution on \((0,\pi/2)\), where \(0\le r(t)\le1\), is bounded in magnitude by
\[
 N=\int_0^{\pi/3}2\sin(t/2)\,dt+\int_{\pi/3}^{\pi/2}\frac{\cos t}{\sin(t/2)}\,dt=N_1+N_2,
\]
with \(N_1=4-2\sqrt3\) and \(N_2=2\log(\tan(\pi/8)/\tan(\pi/12))+4(\cos(\pi/4)-\cos(\pi/6))\). On \((\pi/2,\pi)\), the integrand is nonnegative. Put \(\tau=\arccos((1-4/\pi)/2)\). For \(t\ge\tau\), Jensen yields \(h(r(t))-4/\pi\ge r(t)-4/\pi\), so the positive contribution is at least
\[
 P=\int_{\tau}^{\pi}\frac{1-2\cos t-4/\pi}{2\sin(t/2)}\,dt
 =4\cos(\tau/2)+(1+4/\pi)\log\tan(\tau/4).
\]
Direct elementary enclosures of the displayed constants give \(P>0.83\), \(N_1<0.54\), and \(N_2<0.24\), whence \(P-N>0.05\) and \(C_1\ge(P-N)/\pi>0\). These bounds are intentionally conservative; the exact lower estimate is approximately \(0.02113\).

## Verification
Run `python verify_notch.py` (NumPy dependency) to test the exact finite-band numerator identity and compute a two-dimensional midpoint approximation. With \(\delta=0.1\), \(3000\) radial midpoints and \(2500\) angular midpoints, the approximation to the truncated contribution is \(0.200104553094\). The analytic tail, radial and angular errors together total less than \(0.09034\), so even with an additional \(0.001\) conservative numeric margin the lower bound remains above \(0.108\). The explicit elementary inequality in the proof supplies an independent positivity argument without numerical quadrature. The infinite-band formula itself follows by analysis, not experiments.

## Relationship to prior work
Ortigueira and Bengochea, *On the Lebesgue Constants*, first public preprint May 27, 2024, analyzes the complete even and odd Dirichlet kernels and classical Lebesgue-constant asymptotics. It does not insert a moving one-frequency notch a bounded distance inside the spectral boundary. The previously established fixed-frequency-removal asymptotics keep the deleted frequency independent of \(n\), whereas the present claim fixes its distance from the moving upper edge; these regimes are not implications of one another. No universal claim of bibliographic novelty is made beyond the documented comparisons.

## Limitations
No uniformity is proved for offsets \(j\) depending on \(n\); no strict positivity claim is made here for every \(j\ge2\), and no elementary closed form is claimed for \(C_1\). The numerical decimal is explanatory only. Prior specialized studies of one-hole Fourier idempotents may require further bibliographic investigation.

## References
1. Manuel Duarte Ortigueira and Gabriel Bengochea, *On the Lebesgue Constants*, first public preprint 2024-05-27, https://www.preprints.org/manuscript/202405.1746 ; peer-reviewed version *Axioms* 13 (2024), 505, https://doi.org/10.3390/axioms13080505.
2. E. Liflyand and A. Podkorytov, *Lebesgue constants of Riesz type means of negative order*, *Journal of Mathematical Analysis and Applications* (2021), https://doi.org/10.1016/j.jmaa.2021.125618 (a related, different summability family).
