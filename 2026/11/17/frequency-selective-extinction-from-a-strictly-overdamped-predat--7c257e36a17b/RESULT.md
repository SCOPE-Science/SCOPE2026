# Frequency-selective extinction from a strictly overdamped predator–prey node

## Finding
For every sufficiently small positive forcing amplitude \(A\), the threshold predator–prey system below has three sharply contrasting responses, all from the same positive initial state. Every **frozen** growth rate in the forcing range leads to coexistence at a stable **real node**. Periodic growth forcing of angular frequency \(\sqrt5\) induces admissible crossing of the prey Allee threshold and causes **both populations to become extinct**. Forcing at either angular frequency \(1/100\) or \(100\) does not cross a threshold and instead approaches positive periodic coexistence. The positive-frequency maximum \(1/10\) of the linear prey gain occurs at \(\omega=\sqrt5\) without any nonzero imaginary eigenfrequency.

## Assumptions and scope
Take \(K=2\), \(a=b=m=1\), fixed predator threshold \(P_a=1\), and \(0<A<1\). Prescribe the time-dependent intrinsic prey growth \(\rho(t)=10+A\phi(t)\), with either a constant \(\phi(t)=\theta\in[-1,1]\) or a sinusoid \(\phi(t)=\sin(\omega t)\). Set \(N_a=1-9A/100\) and \((N(0),P(0))=(1,5)\). Away from switching surfaces, the complete equations are
\[
(\dot N,\dot P)=\begin{cases}
(\rho N(1-N/2)-NP,\ P(N-1)),&N>N_a,\ P>1,\\
(-\rho N-NP,\ P(N-1)),&N<N_a,\ P>1,\\
(-\rho N,-P),&N<N_a,\ P<1,\\
(\rho N(1-N/2),-P),&N>N_a,\ P<1.
\end{cases}
\]
At an encountered discontinuity, an admissible forward solution is understood in the Filippov differential-inclusion sense; no uniqueness at a possible tangency is asserted. All comparison trajectories start at the specified same state. Existence of some \(A_0>0\), rather than a numerical optimal amplitude cutoff, is claimed.

## Proof
**1. Stable-node baseline and a uniform perturbation estimate.** The smooth coexistence-region field at \(A=0\) has equilibrium \(E=(1,5)\) and Jacobian
\[
J=\begin{pmatrix}-5&-1\\5&0\end{pmatrix},\qquad
\operatorname{spec}(J)=\left\{-\frac{5-\sqrt5}{2},-\frac{5+\sqrt5}{2}\right\}.
\]
Thus the equilibrium is a strict stable node, not a focus. For every frozen \(\rho=10+A\theta\), the coexistence equilibrium is \(E_\theta=(1,(10+A\theta)/2)\). Its eigenvalues remain distinct, real, and negative for sufficiently small \(A\): the frozen Jacobian is \(J_\theta=\begin{pmatrix}-(10+A\theta)/2&-1\\ (10+A\theta)/2&0\end{pmatrix}\), with characteristic discriminant \(\rho(\rho-8)/4>0\) for \(\rho=10+A\theta>8\).

Write \(u=N-1\), \(v=P-5\). Inside the coexistence region, the exact equations are
\[
\begin{pmatrix}\dot u\\\dot v\end{pmatrix}
=J\begin{pmatrix}u\\v\end{pmatrix}
+\frac A2\begin{pmatrix}\phi(t)\\0\end{pmatrix}
+\begin{pmatrix}-5u^2-uv-(A/2)u^2\phi(t)\\uv\end{pmatrix}.
\]
Since \(J\) is Hurwitz, there are \(M,\gamma>0\) such that \(\|e^{Jt}\|\le M e^{-\gamma t}\). Variation of constants and a small-data bootstrap give, uniformly in \(t\ge0\), all measurable \(\|\phi\|_\infty\le1\), and small \(A>0\),
\[
\|(u(t),v(t))-A z_1(t)\|\le C A^2,\qquad
\sup_{t\ge0}\|(u(t),v(t))\|\le C_1 A,
\]
for the unrestricted smooth coexistence-region flow, where \(\dot z_1=Jz_1+(\phi/2,0)^\mathsf T\), \(z_1(0)=0\). The constants are independent of forcing frequency and frozen value. Indeed the nonlinear remainder is bounded by \(C_2\|z\|^2\) when \(A\le1\), so the Duhamel bounds close uniformly using \(\int_0^\infty M e^{-\gamma s}\,ds<\infty\). In particular \(P(t)=5+O(A)>1\) for all time.

**2. Frozen-rate prey excursion stays strictly above the Allee level.** Put \(\mu_1=(5-\sqrt5)/2\), \(\mu_2=(5+\sqrt5)/2\) and \(\Delta=\mu_2-\mu_1=\sqrt5\). The prey impulse kernel and its integral are
\[
k(t)=(e^{Jt})_{11}=\frac{\mu_2 e^{-\mu_2t}-\mu_1e^{-\mu_1t}}{\Delta},\qquad
I(t)=\int_0^t k(s)\,ds=\frac{e^{-\mu_1t}-e^{-\mu_2t}}{\Delta}.
\]
For frozen \(\phi=\theta\), the first-order prey coordinate is \(u_1(t)=\theta I(t)/2\). The maximum of \(I(t)\) occurs at \(t_*=\log(\mu_2/\mu_1)/\Delta\) and is \(I(t_*)=e^{-\mu_1t_*}/\mu_2\). The elementary strict inequality \(\log z>2(z-1)/(z+1)\) for \(z>1\) gives \(t_*>2/5\). Also \(\mu_1>11/8\), \(\mu_2>7/2\), and \(e^{11/20}>1+11/20+(11/20)^2/2\); consequently
\[
\sup_{t\ge0,\,|\theta|\le1}|u_1(t)|
=\frac{I(t_*)}{2}
<\frac1{7[1+11/20+(11/20)^2/2]}
<\frac9{100}.
\]
The uniform \(O(A^2)\) remainder implies \(N(t)>1-9A/100=N_a\) for every frozen forcing, for all sufficiently small \(A\). Since \(P(t)>1\), the full Filippov solution remains in the first region, and local stability of \(E_\theta\) yields convergence to that stable node.

**3. A resonance-selected downward crossing despite real eigenvalues.** For \(\phi(t)=\sin(\sqrt5\,t)\), the first-order prey coordinate has the exact closed form
\[
u_1(t)=\frac{\sin(\sqrt5\,t)-e^{-\mu_1t}+e^{-\mu_2t}}{10}.
\]
Let \(\delta=3\pi/2-2\sqrt5\). Elementary rational enclosures for \(\pi\) and \(\sqrt5\) give \(0<\delta<1/4\), hence \(\sin(2\sqrt5)=-\cos\delta<-31/32\). Since \(e^{-2\mu_1}>e^{-2\mu_2}\), the exact formula proves
\[
u_1(2)<-\frac{31}{320}<-\frac9{100}.
\]
For all small enough \(A>0\), the unrestricted smooth solution therefore satisfies \(N(2)<N_a\) while \(P(t)>1\) on \([0,2]\). Starting above \(N_a\), it must encounter the prey threshold and admits a forward Filippov continuation into \(N<N_a\). A possible tangential contact before the strict crossing can be followed on the smooth side; this proves existence, not uniqueness, of the extinction continuation. Once below \(N_a<1\), the prey equation gives \(\dot N\le-(10-A)N\). The predator satisfies \(\dot P\le-(1-N_a)P\) while \(P>1\), and subsequently \(\dot P=-P\). Therefore \((N(t),P(t))\to(0,0)\).

**4. Slow/fast safe frequencies and exact bandpass gain.** For \(\phi(t)=\sin(\omega t)\), the first-order prey response is
\[
u_1(t;\omega)=\frac12\int_0^t k(s)\sin(\omega(t-s))\,ds.
\]
Since \(\int_0^\infty k(s)\,ds=0\), subtraction of the instantaneous sine gives the uniform low-frequency bound
\[
\sup_{t\ge0}|u_1(t;\omega)|
\le\frac\omega2\left(\int_0^\infty s|k(s)|\,ds+\sup_{t\ge0}t\left|\int_t^\infty k(s)\,ds\right|\right)
\le\frac\omega2\left(\frac1\Delta+\frac1{e\mu_1\Delta}\right).
\]
Integration by parts gives the uniform high-frequency bound
\[
\sup_{t\ge0}|u_1(t;\omega)|
\le\frac{1+2\sqrt5}{2\omega}.
\]
At \(\omega=1/100\), the first bound is less than \(0.004\); at \(\omega=100\), the second is less than \(0.028\). Hence the uniform \(O(A^2)\) approximation keeps the nonlinear trajectories strictly above \(N_a\), with predators above \(P_a\). The smooth periodic perturbations of a Hurwitz equilibrium admit unique nearby locally attracting periodic trajectories, and exponential difference estimates in a local Lyapunov norm show convergence from \(E\). Thus neither low nor high frequency causes tipping.

Finally, the first-coordinate steady harmonic transfer gain is
\[
G(\omega)=\frac{\omega}{2\sqrt{(5-\omega^2)^2+25\omega^2}},\qquad\omega>0.
\]
Writing \(z=\omega^2\) shows \(4G(\omega)^2=z/(z^2+15z+25)\), whose derivative has the sign of \(25-z^2\). Thus the unique positive-frequency gain maximum is \(G(\sqrt5)=1/10\), even though the eigenvalues are both real and negative. This completes the single three-regime contrast.

## Verification
The accompanying standalone file `verify.py` checks the exact Jacobian, polynomial remainder, Green kernel, resonant closed form, the frozen excursion and low/high-frequency bounds, and representative numerical trajectories at two small amplitudes. Executing `python verify.py` with SymPy, NumPy and SciPy available produces `VERIFY_OK`. Finite integrations illustrate, but do not prove, the all-small-amplitude statements; the uniform perturbation and threshold arguments above establish those quantifiers.

## Relationship to prior work
Gao, Poloni, Wang and Lewis (2026) introduced the frequency-induced tipping mechanism in this same threshold predator–prey system. Their principal resonance and extinction examples use a **stable focus** with a nonzero damped natural frequency. Their Appendix A records the stable-node regime but does not establish the specific node-to-extinction forcing contrast proved here. An earlier comparison result gives a weak-forcing extinction construction under a strictly positive focus frequency; it does not establish this example with the distinct real eigenvalues or its optimal node transfer gain. Standard linear systems theory supplies the convolution and transfer identities, not by itself the nonlinear threshold/no-threshold Filippov conclusion.

## Limitations
The amplitude condition is existential, not optimized. The prey threshold depends on forcing amplitude and approaches the coexistence prey coordinate as the amplitude vanishes. The frequency selection is proved for the explicit coefficients and forcing phase, not for arbitrary predator–prey models. At a potential tangential threshold encounter only the existence of an admissible extinction continuation is asserted; full Filippov uniqueness is not proved. Smooth regularizations, stochastic perturbations and arbitrary initial populations are outside the theorem. Historical priority is provisional and independent external validation has not been performed.

## References
1. Shan Gao, Silas Poloni, Hao Wang, Mark Lewis, *Frequency-induced Tipping: Resonance-Driven Tipping in a Threshold Predator-Prey System*, arXiv:2610.39113v1, first posted 2026-10-29, https://arxiv.org/html/2610.39113v1 . Relevant material: Results §§2.1–2.4, Methods §4.1, Appendix A and Appendix C1.
2. Classical linear variation-of-constants formula, matrix exponential decay for Hurwitz matrices, and local persistence of hyperbolic periodic responses (standard theorems; not claimed as new).
