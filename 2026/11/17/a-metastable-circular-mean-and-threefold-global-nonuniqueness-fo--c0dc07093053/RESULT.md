# A metastable circular mean and threefold global nonuniqueness for embedded periodic trajectories

## Finding

Put \(u_0=(5-2\sqrt3)/4\). For every \(u_0<u<1/2\), consider the three regular, embedded, analytic periodic curves in \(\mathbb R^3\)
\[
\gamma_j(t)=(\cos t,\sin t,\sqrt{2u}\cos(2t+2\pi j/3)),\qquad j=0,1,2,
\]
with \(t\in\mathbb R/(2\pi\mathbb Z)\). In the time-phase-only quotient \(L^2(S^1,\mathbb R^3)/S^1\), under the equal-weight squared phase-aligned Fréchet functional, the arithmetic mean \(c_0(t)=(\cos t,\sin t,0)\) is a **strict local minimizer modulo phase shifts but not a global minimizer**. Every global minimizer is a regular embedded closed curve having both its fundamental planar harmonic and its second vertical harmonic nonzero; global minimizers occur in **at least three inequivalent phase-shift classes**.

For the alternating optimal-phase-alignment and arithmetic-averaging iteration initialized at \(c_0\), the iteration stays at this suboptimal strict local minimum forever. More quantitatively,
\[
\mathcal F([c_0])=u,\qquad
\mathcal F([c_0])-\inf\mathcal F\ \geq\ \frac{4u-5+2\sqrt3}{9}>0.
\]
For example, the exact parameter \(u=2/5\) is in this open interval, with gap at least \((10\sqrt3-17)/45>0\).

Each of the three sample loops is independently realizable as an exponentially orbitally attracting periodic solution of a smooth autonomous **polynomial** vector field, in a one-parameter polynomial family. This is a structural witness of a **stable but globally incorrect** arithmetic-initialized phase-alignment result with at least three genuine, embedded global mean shapes; no numerical solution of the global optimization problem is assumed.

## Assumptions and scope

Use the normalized real Hilbert space \(H=L^2(\mathbb R/(2\pi\mathbb Z);\mathbb R^3)\) with
\[
\langle f,g\rangle=\frac1{2\pi}\int_0^{2\pi}f(t)\cdot g(t)\,dt,
\quad (T_\theta f)(t)=f(t+\theta),
\quad d([f],[g])=\min_{\theta\in S^1}\|f-T_\theta g\|.
\]
The quotient identifies **only circular shifts of the time parameter**, not spatial rotations, reflection, orientation reversal or arbitrary time warping. Define
\[
\mathcal F([c])=\frac13\sum_{j=0}^2 d([c],[\gamma_j])^2.
\]
The minimization is over the full Hilbert quotient, not a restricted Fourier ansatz or only curves that solve the motivating vector fields. The input parameter \(u\) is strictly between \(u_0\) and \(1/2\); equality endpoints are not claimed. The input period is exactly \(2\pi\). A global mean is a phase class; its representative may depend on the global phase gauge.

## Proof

**1. Complete reduction to a compact alignment problem.** For arbitrary independent shifts \(\theta_j\), let \(g_j=T_{\theta_j}\gamma_j\) and \(m_{\boldsymbol\theta}=\frac13\sum_jg_j\). The Hilbert variance identity gives
\[
\frac13\sum_j\|c-g_j\|^2=\|c-m_{\boldsymbol\theta}\|^2+\frac13\sum_j\|g_j\|^2-\|m_{\boldsymbol\theta}\|^2.
\]
Compactness of the three phase circles makes every alignment minimum attainable. Joint minimization therefore shows that *all* global Fréchet means, without an a priori Fourier restriction, are the classes of averages \(m_{\boldsymbol\theta}\) maximizing their squared Hilbert norm. Every \(\gamma_j\) has norm squared \(1+u\). Put
\[
Z=\sum_{j=0}^2e^{i\theta_j},\qquad
W=\sum_{j=0}^2e^{i(2\theta_j+2\pi j/3)}.
\]
Orthogonality of the first planar and second vertical harmonics gives exactly
\[
m_{\boldsymbol\theta}(t)=\frac13\big(\operatorname{Re}(Ze^{it}),\operatorname{Im}(Ze^{it}),\sqrt{2u}\operatorname{Re}(We^{2it})\big),
\quad
\|m_{\boldsymbol\theta}\|^2=\frac{|Z|^2+u|W|^2}{9}.
\]
Hence \(\inf\mathcal F=1+u-\frac19\max_{\boldsymbol\theta}(|Z|^2+u|W|^2)\).

**2. Exact global improvement.** At the unshifted alignment \(\theta_j=0\) the planar sum has \(Z=3\) and the vertical sum vanishes, \(W=0\). Thus \(c_0=(\cos t,\sin t,0)\), \(\|c_0\|^2=1\) and \(\mathcal F([c_0])=u\). Consider instead the three shifts \((\theta_0,\theta_1,\theta_2)=(0,-\pi/6,+\pi/6)\). Direct addition yields \(Z=1+\sqrt3\) and \(W=2\), so
\[
|Z|^2+u|W|^2=4+2\sqrt3+4u>9
\]
exactly when \(u>u_0\). By Step 1 this proves both the strict inequality \(\inf\mathcal F<u\) and the stated quantitative gap; the numerical value of the true global minimum is unnecessary.

**3. At least three different global mean classes.** Let \(\boldsymbol\theta\) be *any* maximizer. Step 2 gives \(|Z|^2+u|W|^2>9\). If \(W=0\), the triangle inequality implies the objective is at most \(9\). If \(Z=0\), the objective is at most \(9u<9\). Thus \(Z\ne0\) and \(W\ne0\) for every maximizing alignment. Let \(\omega=e^{2\pi i/3}\). Cyclically permuting alignment labels by \(\theta'_j=\theta_{j+1\pmod3}\) preserves \(Z\) and changes \(W\) to \(\omega^{-1}W\), so it preserves the objective and produces another global minimizer. Iterating gives three mean representatives with coefficient pairs \((Z,W)\), \((Z,\omega^{-1}W)\), \((Z,\omega^{-2}W)\). Under a common phase shift by \(s\), coefficients change as \((Z,W)\mapsto(e^{is}Z,e^{2is}W)\). Thus the nonzero ratio \(W/Z^2\) is phase-invariant, whereas the three displayed ratios are distinct. All three global means are consequently inequivalent. Because \(Z\ne0\), each mean's first two coordinates parameterize a nondegenerate circle injectively; these mean curves are regular embedded closed curves in \(\mathbb R^3\).

**4. The circular mean is a strict local minimum in the full quotient.** For any representative \(c\in H\), let \(q_j(c)=\max_s\langle c,T_s\gamma_j\rangle\). The Fréchet functional lifts to
\[
\mathcal F(c)=\|c\|^2+(1+u)-\frac23\sum_jq_j(c).
\]
At \(c_0\), the cross-correlation is \(\langle c_0,T_s\gamma_j\rangle=\cos s\), which has its unique nondegenerate global maximum at \(s=0\). Compactness, the strictly negative curvature there and the implicit-function theorem imply each \(q_j\), hence \(\mathcal F\), is twice continuously Fréchet differentiable in an \(H\)-neighborhood of \(c_0\). Its gradient vanishes since \(\frac13\sum_j\gamma_j=c_0\). Differentiating the maximizing shift gives, for any \(h\in H\),
\[
D^2\mathcal F(c_0)[h,h]=2\|h\|^2-\frac23\sum_{j=0}^2\langle h,\dot\gamma_j\rangle^2.
\]
Let \(V(t)=(-\sin t,\cos t,0)\), \(p=\langle h,V\rangle\), and let \(A\cos2t+B\sin2t\) be the orthogonal projection of the third component of \(h\) onto second harmonics. Harmonic orthogonality and the three equispaced phases give the exact identity
\[
\frac13\sum_j\langle h,\dot\gamma_j\rangle^2=p^2+u(A^2+B^2).
\]
On the normal slice \(\langle h,V\rangle=0\), Bessel's inequality yields \((A^2+B^2)/2\le\|h\|^2\), hence
\[
D^2\mathcal F(c_0)[h,h]\ge 2(1-2u)\|h\|^2>0\qquad(h\perp V,\ h\ne0).
\]
The one missing tangent direction \(V\) is exactly the circular-shift orbit of \(c_0\). Because that orbit is free near \(c_0\), the normal slice supplies a local gauge. Continuity of the Hessian and its positive lower bound on the slice prove that \([c_0]\) is a **strict local** minimizer in the full quotient. Step 2 has already proved it is **not global**, giving a nonempty interval of metastability rather than merely a stationary saddle.

**5. Exact algorithm trap.** The arithmetic initialization of the alternating phase-alignment/averaging method is \(c_0\). Its unique best alignment against each \(\gamma_j\) is zero, as the cross-correlation is \(\cos s\); the averaging step therefore returns \(c_0\). Induction gives a constant iteration at this strict local but globally suboptimal mean.

**6. Realization by polynomial attracting periodic orbits.** Set \(a=\sqrt{2u}\) and \(\phi=2\pi j/3\). Define the real quadratic polynomial \(P_\phi(x,y)=a[(x^2-y^2)\cos\phi-2xy\sin\phi]\), the planar Hopf field \(X=-y+(1-x^2-y^2)x\), \(Y=x+(1-x^2-y^2)y\), and the polynomial vector field
\[
\dot x=X,\quad \dot y=Y,\quad
\dot z=P_{\phi,x}X+P_{\phi,y}Y-(z-P_\phi).
\]
Its solutions include \(\gamma_j(t)\). In polar coordinates \(\dot r=r(1-r^2)\), \(\dot\vartheta=1\), while \(e=z-P_\phi(x,y)\) satisfies \(\dot e=-e\). Thus the orbit is smooth and embedded with least period \(2\pi\) and transverse Floquet multipliers \(e^{-4\pi}\) and \(e^{-2\pi}\). This establishes that each sample arises as an exponentially attracting limit cycle in a polynomial family; the three curves need not be orbits of one fixed vector field.

## Verification

A standalone standard-library checker `verify_threefold.py` evaluates all exact trigonometric identities defining the competitor, the Hessian's three-phase orthogonality, the strict interval inequalities, the cyclic symmetry on coefficient pairs and representative numerical squared distances. The checker can be run from an extracted copy of this complete package using `python3 verify_threefold.py`. Its finite tests support but are not a substitute for the continuous and infinite-dimensional proof in Steps 1--6.

## Relationship to prior work

Hering and Kuehn (2026, Sections 3--4) define the phase-only quotient, establish existence and introduce the alternating alignment-and-average iteration, while explicitly noting nonuniqueness and the lack of a global convergence guarantee. The new contribution here is a **particular symmetric three-trajectory polynomial-flow family**, a rigorous open interval in which the initialization is a *strict local minimum despite global suboptimality*, and an *at-least-three-class* global-minimizer obstruction.

Earlier explicit two-trajectory constructions establish one-to-two bifurcations and, in one case, a trapped arithmetic initialization **which is not a local minimizer**; these do not imply the simultaneous local-stability and threefold-global-degeneracy statements for this three-sample model. An oppositely oriented circle ensemble yields a continuum of degenerate means through a different chirality mechanism. General finite-orthogonal-group orbit-space certification techniques and older curve-registration methods likewise do not directly classify this continuous-phase three-loop example. Full historical uniqueness is not asserted merely from database searches.

## Limitations

The interval \((u_0,1/2)\) is **sufficient**, not claimed sharp; the proof guarantees at least three, not exactly three, global mean classes. It does not compute the exact global minimum or basins of attraction of the alignment iteration. Time parametrization is essential; arbitrary time warps, arc-length parametrization and ambient rotations are outside scope. The three sample cycles are realized by three parameter members of a smooth polynomial family, not necessarily one common vector field. Results are proved within the normalized \(L^2\) quotient; independent mathematical audit and exhaustive historical-priority assessment have not been carried out.

## References

1. P. Hering and C. Kuehn, *Fréchet Means of Periodic Orbits in Dynamical Systems: Geometry, Dynamics, and Diagnostics*, arXiv:2606.10748v1, first public 2026-06-09. https://arxiv.org/abs/2606.10748 . Sections 3, 3.1 and 4.
2. *Sharp two-harmonic bifurcation of periodic-orbit Fréchet means and an alignment-algorithm trap*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-harmonic-bifurcation-of-periodic-orbit-fr-chet-means-a--6edf7370e38b .
3. *A sharp bifurcation of phase-aligned means of embedded periodic orbits*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-bifurcation-of-phase-aligned-means-of-embedded-periodic--46a4a3015050 .
4. *Chirality-balanced phase-quotient means collapse and are discontinuously selected by elliptic perturbations*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-chirality-balanced-phase-quotient-means-collapse-and-are-discont--a834cfd6398b .
5. D. G. Mixon, T. Needham and N. Willey, *Certifiably Correct Fréchet Means in Orbit Spaces*, arXiv:2610.24191v1, first public 2026-10-16. https://arxiv.org/abs/2610.24191 .
6. J. Bigot, *Fréchet means of curves for signal averaging and application to ECG data analysis*, arXiv:1111.1855v1, 2011-11-08. https://arxiv.org/abs/1111.1855 .
