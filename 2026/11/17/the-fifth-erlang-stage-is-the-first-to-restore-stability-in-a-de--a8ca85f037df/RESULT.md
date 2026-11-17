# The fifth Erlang stage is the first to restore stability in a delayed neuronal center

## Finding
For every pair of real constants \(a>b>0\), consider the characteristic equation of a linearized delay system
\[
\Delta_q(\lambda,\tau)=\lambda^2+a-b\left(1+\frac{\tau\lambda}{q}\right)^{-q}=0,
\qquad q\in\{1,2,3,4,5,6\},\quad \tau>0.
\]
The factor corresponds to the gamma/Erlang delay kernel with integer shape \(q\) and fixed mean delay \(\tau\). Spectral stability means that every characteristic root lies strictly in the open left half-plane.

There is a sharp, parameter-independent three-part classification:

1. For \(q=1,2\), the equilibrium is spectrally stable at every finite positive mean delay.
2. For \(q=3,4\), it is stable precisely when \(0<\tau<\tau_1(q)\), and it has a right-half-plane conjugate pair for every \(\tau>\tau_1(q)\).
3. For \(q=5,6\), it is stable precisely on \((0,\tau_1(q))\cup(\tau_2(q),\infty)\), and has exactly one unstable conjugate pair for \(\tau_1(q)<\tau<\tau_2(q)\).

The two exact thresholds, when the indicated index exists, are
\[
\tau_j(q)=\frac{q\tan(j\pi/q)}{\sqrt{a-(-1)^j b\cos^q(j\pi/q)}},
\qquad 1\le j<q/2.
\]
At each threshold the characteristic equation has a simple pair of purely imaginary roots, so neither threshold belongs to an exponentially stable interval. Thus **five Erlang stages are the minimum required for delay-induced loss and subsequent restoration of linear stability**, uniformly for every \(a>b>0\).

This applies to the type-2, delay-free center of the reduced theta-neuron population model of Bîrdac, Fikl, Kaslik and Mureşan whenever its paper-defined coefficients satisfy \(a=a_2(z_\star)>b=b_2(\kappa,z_\star)>0\). It concerns the linearized macroscopic order-parameter dynamics, not a full nonlinear or finite-population attraction theorem.

## Assumptions and scope
Fix arbitrary real \(a>b>0\) and integer \(1\le q\le6\). The delay law is the probability density
\[
 g_{q,\tau}(s)=\frac{(q/\tau)^q}{\Gamma(q)}s^{q-1}e^{-qs/\tau},\quad s\ge0,
\]
whose mean is \(\tau\), whose variance is \(\tau^2/q\), and whose Laplace transform is \(\left(1+\tau\lambda/q\right)^{-q}\). The characteristic polynomial of its finite linear-chain representation is
\[
P_q(\lambda,\tau)=(\lambda^2+a)\left(1+\frac{\tau\lambda}{q}\right)^q-b.
\]
Roots of this polynomial are exactly the eigenvalues of the \(q+2\)-dimensional Erlang linear-chain realization for each \(\tau>0\). No claim is made for noninteger gamma shape, other kernels, \(b\le0\), \(a\le b\), or \(q\ge7\). The center at \(\tau=0\) is neutrally stable and is excluded from the stated open stability windows.

## Proof
**Initial stability.** As \(\tau\downarrow0\), two roots approach \(\pm i\sqrt{a-b}\). Implicit differentiation of \(\Delta_q\) at \(\tau=0\) gives
\[
\lambda_\pm(\tau)=\pm i\sqrt{a-b}-\frac b2\tau+O(\tau^2).
\]
The other \(q\) polynomial roots lie near \(-q/\tau\): after setting \(u=\tau\lambda/q\), the polynomial equation becomes \((q^2u^2+a\tau^2)(1+u)^q=b\tau^2\), and every remaining root satisfies \(u\to-1\). Hence all roots lie strictly left for sufficiently small positive \(\tau\).

**Complete imaginary-root census.** Suppose \(\lambda=i\omega\), \(\omega>0\), and put \(x=\tau\omega/q>0\). The Erlang factor has modulus \((1+x^2)^{-q/2}\) and argument \(-q\arctan x\). Since \(\omega^2-a\) is real, the imaginary part vanishes exactly when
\[
q\arctan x=j\pi,\qquad j\in\mathbb{Z}_{>0},\qquad j<q/2.
\]
There are no other positive-frequency solutions. For each such \(j\), \(x=\tan(j\pi/q)\), the factor equals \((-1)^j\cos^q(j\pi/q)\), and the real equation gives
\[
\omega_j^2=a-(-1)^j b\cos^q(j\pi/q)>0,
\qquad \tau=\tau_j(q).
\]
Zero cannot be a characteristic root because \(\Delta_q(0,\tau)=a-b>0\). For \(q=1,2\) there are no finite thresholds; for \(q=3,4\) exactly \(j=1\); and for \(q=5,6\) exactly \(j=1,2\).

**Simple crossing and its direction.** At the \(j\)-th threshold write \(B=(-1)^j b\cos^q(j\pi/q)\), \(x=\tan(j\pi/q)\), and \(h=(1+ix)^{-1}\). Differentiating the characteristic equation implicitly gives
\[
\lambda'(\tau)=-\frac{B\lambda h}{2\lambda+B\tau h},\qquad
\operatorname{Re}\lambda'(\tau_j)=-\frac{2B\omega_j^2}{(1+x^2)|2i\omega_j+B\tau_jh|^2}.
\]
The denominator is nonzero because the denominator's real part is \(B\tau_j/(1+x^2)\ne0\). Therefore the crossing is simple, strictly **rightward for odd \(j\)** and strictly **leftward for even \(j\)**. A complex-conjugate pair changes the number of roots in the right half-plane by exactly two. This conclusion follows from the explicit derivative and root continuity; it is not inferred from numerical root searches.

**Global root count.** For \(q=5,6\),
\[
\tau_1(q)<\frac{q\tan(\pi/q)}{\sqrt a}
<\frac{q\tan(2\pi/q)}{\sqrt a}<\tau_2(q),
\]
using \(b>0\) and the positive cosines. Thus the first crossing creates exactly one unstable pair; the second removes it, and there are no other finite imaginary-root or zero-root crossings. The small-delay root count therefore proves all three regimes for every \(\tau>0\). The cases \(q=1,2,3,4\) follow identically.

## Verification
The bundled `verification/check_gamma.py` evaluates the characteristic polynomial directly and checks the predicted thresholds, exact phase identities, and transverse crossing signs for several independent parameter choices. All numerical checks supplement, and do not replace, the exhaustive analytic count of possible imaginary roots and the continuity argument. In the concrete example \(a=4,b=2\), the thresholds are approximately \(\tau_1(5)=1.6768703772\), \(\tau_2(5)=7.6996347832\), \(\tau_1(6)=1.5739820059\), and \(\tau_2(6)=5.2165696032\).

## Relationship to prior work
Bîrdac, Fikl, Kaslik and Mureşan (2026), equations (5.1)–(5.8), derive this scalar characteristic form for the type-2 center and the general imaginary-root phase criterion. Their Examples 5.5–5.6 establish the absence of Hopf crossings for weak and strong Gamma kernels (Erlang shapes one and two), and their Example 5.7 and Proposition 5.8 analyze discrete delay. The present contribution is the **complete first-six-shape spectral stability classification**, including the universal finite-smoothing reentrance at the minimal shape five and exact threshold/crossing directions. It does not claim discovery of the underlying characteristic equation, the Erlang transform, or the general phase method.

Earlier distributed-delay bifurcation methods of Yuan and Bélair (2011) and the Erlang linear-chain method provide broader context; a fully general phase condition alone does not state the parameter-uniform five-stage reentrance classification. The possibility of an older equivalent result under another model name remains a historical-priority limitation.

## Limitations
The result describes linear exponential stability (equivalently the local exponential attraction of a hyperbolic equilibrium in the corresponding well-posed distributed-delay system), not global attraction, nonlinear Hopf criticality, existence or orbital stability of any born periodic orbit, basin volumes, or finite-network corrections. The origin and thresholds are nonhyperbolic. For \(q\ge7\), more than two candidate crossings can occur and their delay order may depend on the ratio \(b/a\); no unproved monotone-order assertion for those shapes is made. The inspected primary preprint contains a broad kernel phase criterion, so novelty depends on the additional complete sharp stability classification rather than a new characteristic-equation technique.

## References
1. L. Bîrdac, A. Fikl, E. Kaslik and R. Mureşan, *Macroscopic Multistability and Bifurcations in Theta-Neuron Networks with Distributed Delays*, arXiv:2607.17645v1, first public July 20, 2026. https://arxiv.org/abs/2607.17645 ; accessible full text: https://www.researchgate.net/publication/410636196_Macroscopic_Multistability_and_Bifurcations_in_Theta-Neuron_Networks_with_Distributed_Delays
2. Y. Yuan and J. Bélair, *Stability and Hopf Bifurcation Analysis for Functional Differential Equation with Distributed Delay*, SIAM Journal on Applied Dynamical Systems 10 (2011), 551–581, DOI:10.1137/100794493. https://doi.org/10.1137/100794493
3. D. H. Nevermann and C. Gros, *Mapping dynamical systems with distributed time delays to sets of ordinary differential equations*, Journal of Physics A 56 (2023), 345702, DOI:10.1088/1751-8121/acea06. https://doi.org/10.1088/1751-8121/acea06
