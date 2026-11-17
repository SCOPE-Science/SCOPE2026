# A Student-type occupation law and a sharp moment transition in a cubic global center

## Finding
Consider the cubic polynomial differential equation in its displayed, unrescaled physical time,
\[
\dot x=(1+3x^2)y,\qquad \dot y=-x-x^3+3xy^2.
\]
Every nonzero initial state lies on a periodic orbit. Define
\[
P(x)=1+3x^2,\qquad U(x)=\frac{\log P(x)-2/P(x)+2}{9},\qquad H(x,y)=\frac{y^2}{P(x)}+U(x).
\]
For each \(E>0\), let \(A_E>0\) be the unique solution of \(U(A_E)=E\), let \(T(E)\) be the minimal period of \(H=E\), and let \(X_E\) denote the \(x\)-coordinate at uniformly sampled physical time during that period. As \(E\to\infty\):
\[
A_E\sim\frac{e^{(9E-2)/2}}{\sqrt3},\qquad T(E)\sim\frac{4}{\sqrt{3E}},
\]
\[
X_E\Rightarrow X_\infty,\qquad
\Pr(X_\infty\in dx)=\frac{\sqrt3}{2(1+3x^2)^{3/2}}\,dx.
\]
The limiting law has a sharp absolute-moment threshold at exponent \(2\). For every fixed real \(q\ge0\), write \(M_q(E)=\mathbb E|X_E|^q\). Then
\[
\boxed{\begin{aligned}
M_q(E)&\longrightarrow\frac{3^{-q/2}}{2}B\!\left(\frac{q+1}{2},\frac{2-q}{2}\right),&&0\le q<2,\\[2pt]
M_2(E)&\sim3E,&&q=2,\\[2pt]
M_q(E)&\sim A_E^{q-2}\sqrt{\frac{\pi E}{2(q-2)}},&&q>2.
\end{aligned}}
\]
Here \(B\) is the Euler beta function; the \(q=0\) moment equals one. In particular the periodic orbits become exponentially wide while their physical periods shrink, and their limiting occupation law has finite mean absolute displacement but infinite variance. The statement is about the entire moment spectrum, including the exact coefficients of non-uniform-integrability beyond the threshold.

## Assumptions and scope
The state variables \(x,y\) and the time variable are real. There is no adjustable parameter in the displayed system. The energy \(E>0\) is the exact value of \(H\), not a generic geometric amplitude or canonical energy after time change. The orbit of \(H=E\) is traversed once in its minimal period. The probability \(X_E\) uses normalized *original-time* Lebesgue measure on this orbit. The exponent \(q\) is fixed before \(E\to\infty\). Weak convergence is against bounded continuous functions on the real line; it does not imply convergence of moments of order two or higher.

## Proof
**1. First integral and complete periodic ovals.** Direct differentiation gives
\[
U'(x)=\frac{2x(1+x^2)}{P(x)^2},\quad
H_x=\frac{-6xy^2}{P(x)^2}+U'(x),\quad H_y=\frac{2y}{P(x)}.
\]
Substituting the vector field shows exactly that \(H_x\dot x+H_y\dot y=0\): the terms of order \(y^3\) cancel and so do the remaining terms of order \(y\). The function \(U\) is even, strictly increasing on \((0,\infty)\), satisfies \(U(0)=0\) and tends to infinity. Thus \(H=E\) consists of two smooth graphs
\[
y=\pm\sqrt{P(x)[E-U(x)]},\qquad -A_E\le x\le A_E,
\]
joined regularly at their endpoints. The only equilibrium is \((0,0)\), so each nonzero compact oval is one minimal-period orbit. The identity \(U(A_E)=E\) is equivalent, with \(W_E=\log P(A_E)\), to \(W_E-2e^{-W_E}+2=9E\); hence \(W_E=9E-2+o(1)\), giving the claimed amplitude formula.

**2. Exact physical-time quadrature.** Along an orbit, \(|\dot x|=P(x)^{3/2}\sqrt{E-U(x)}\). Define for \(q\ge0\)
\[
I_q(E)=\int_0^{A_E}\frac{x^q\,dx}{P(x)^{3/2}\sqrt{E-U(x)}}.
\]
Symmetry and the two traversals of every interior position give
\[
T(E)=4I_0(E),\qquad M_q(E)=\frac{I_q(E)}{I_0(E)}.
\]
The *exact* occupation density, including both traversals, is
\[
 f_E(x)=\frac{2\,\mathbf 1_{\{|x|<A_E\}}}{T(E)P(x)^{3/2}\sqrt{E-U(x)}}.
\]

**3. An Abel-transform lemma.** Let \(x(v)>0\) be the inverse of \(U\) on the positive half-axis. The substitution \(v=U(x)\) gives
\[
I_q(E)=\int_0^E\frac{g_q(v)}{\sqrt{E-v}}\,dv,\qquad
g_q(v)=\frac{x(v)^{q-1}\sqrt{P(x(v))}}{2(1+x(v)^2)}.
\tag{1}
\]
Near \(v=0\), \(U(x)=x^2+O(x^4)\), so \(g_q(v)=\frac12v^{(q-1)/2}(1+o(1))\). At infinity, \(v=\frac29\log x+\frac{\log3+2}{9}+o(1)\), so
\[
g_q(v)\sim\frac{\sqrt3}{2}x(v)^{q-2},\qquad x(v)\sim \frac{e^{(9v-2)/2}}{\sqrt3}.
\tag{2}
\]
These endpoint expansions are uniform for the fixed exponent \(q\); they follow by direct expansion of the elementary functions in \(U\) and \(g_q\).

**4. The integrable range \(0\le q<2\).** Equation (2) makes \(g_q\) exponentially decaying at infinity and the zero-end singularity in (1) is integrable. Splitting (1) at \(E/2\), dominated convergence gives
\[
\sqrt E\,I_q(E)\longrightarrow\int_0^\infty g_q(v)\,dv
=\int_0^\infty\frac{x^q\,dx}{(1+3x^2)^{3/2}}.
\tag{3}
\]
For detail: on \([0,E/2]\), the factor \((1-v/E)^{-1/2}\) is at most \(\sqrt2\) and tends to one at every fixed \(v\); on \([E/2,E]\), the exponential tail of \(g_q\), together with \(\int_{E/2}^E(E-v)^{-1/2}dv=O(\sqrt E)\), gives a vanishing contribution after multiplication by \(\sqrt E\). The integral in (3) is \(\frac12 3^{-(q+1)/2}B((q+1)/2,(2-q)/2)\). At \(q=0\), it equals \(1/\sqrt3\), proving \(T(E)\sim4/\sqrt{3E}\); taking ratios proves the first moment regime.

**5. The critical order \(q=2\).** Formula (1) has a bounded kernel \(g_2(v)\to\sqrt3/2\). Set \(v=Es\) and apply dominated convergence using \((1-s)^{-1/2}\in L^1(0,1)\):
\[
\frac{I_2(E)}{\sqrt E}=\int_0^1\frac{g_2(Es)}{\sqrt{1-s}}\,ds\longrightarrow\sqrt3.
\]
Since \(I_0(E)\sim1/\sqrt{3E}\), this proves \(M_2(E)\sim3E\). No divergent second moment is inferred merely from weak convergence.

**6. The supercritical range \(q>2\).** Put \(\lambda=\frac92(q-2)>0\). Equation (2) gives \(g_q(v)\sim C_q e^{\lambda v}\) for some explicit positive constant \(C_q\). Therefore, with \(s=E-v\),
\[
\frac{I_q(E)}{g_q(E)}=\int_0^E\frac{g_q(E-s)/g_q(E)}{\sqrt s}\,ds
\longrightarrow\int_0^\infty\frac{e^{-\lambda s}}{\sqrt s}\,ds
=\sqrt{\frac\pi\lambda}.
\tag{4}
\]
For rigor, the positive ratio is bounded by \(C e^{-\lambda s}\) for all \(0\le s\le E\) and sufficiently large \(E\): use the exponential asymptotic of \(g_q\) above a fixed positive energy and boundedness of \(g_q(v)e^{-\lambda v}\) below it. Dominated convergence applies against \(s^{-1/2}ds\). Since \(g_q(E)\sim(\sqrt3/2)A_E^{q-2}\), (4) gives
\[
I_q(E)\sim \sqrt{\frac{\pi}{6(q-2)}}A_E^{q-2}.
\]
Dividing by \(I_0(E)\sim1/\sqrt{3E}\) proves the third regime.

**7. Limiting position law.** For each bounded continuous function \(F\), the same \(q=0\) Abel estimate, or direct tightness after splitting \(x\)-space at a fixed large radius and controlling the turning-point part, gives
\[
\int F(x)f_E(x)\,dx\longrightarrow
\int_{\mathbb R}F(x)\frac{\sqrt3}{2P(x)^{3/2}}\,dx.
\]
The proposed density integrates to one because \(\int_0^\infty P(x)^{-3/2}dx=1/\sqrt3\). A direct tightness proof follows from (3) with \(q=1\): \(\sup_{E\ge E_0}M_1(E)<\infty\) for sufficiently large \(E_0\), so Markov's inequality controls the outer tails. The pointwise density limit on every fixed compact interval and this tightness imply the weak limit. The beta formula for \(q<2\), and the divergence regimes for \(q\ge2\), establish its sharp moment threshold.

## Verification
The companion standard-library script `verify.py` evaluates the invariant derivative on an independent rational grid and recomputes the period and moments using a regularized quadrature in \(w=\log(1+3x^2)\). It checks the exact normalization \(M_0=1\), the predicted period constant \(4/\sqrt3\), the critical moment coefficient \(3\), and the leading coefficient for \(q=3\) at increasing energies. A separate symbolic simplification of \(dH/dt\) produced zero. The finite calculations corroborate constants only; the infinite-energy proof is Steps 1–7.

## Relationship to prior work
Llibre and Rondón (2023, arXiv:2310.07454v1), Theorem 2(f) and equation (35), classify the present system as a global center on choosing their parameters \(a_1=0\), \(b_1=-1\), \(d_1=0\) and the remaining parameters zero. That global-center classification is prior mathematics, not part of the novelty claim. The source was read through its theorem and the detailed case-(f) proof. Its full text does not assert the original-time occupation distribution, exponent-two moment threshold, or the three exact moment-asymptotic regimes.

Ghose-Choudhury and Guha (2016) give the general position-dependent-mass Hamiltonian period quadrature and sufficient period-monotonicity conditions. Their framework explains why a one-dimensional period integral exists but does not state this orbit-time probability law or its moment constants. Other published quantitative results on different Llibre–Rondón cubic subfamilies include a Cauchy-law order-one moment threshold for \(\dot x=(1+\kappa x^2)y,\ \dot y=-x\), and a log-position occupation law for \(\dot x=(1+2ax+kx^2)y,\ \dot y=-x+ax^2-kx^3-(a+kx)y^2\). Neither is the displayed system or implies its order-two transition: the invariant energy weights and physical-time occupation kernels differ. Another compared cubic Hamiltonian \(\dot x=P(x)y,\ \dot y=-x^3\) also has a different energy and a Cauchy rather than Student-type limit. General separable-Hamiltonian theory may cover the leading period scaling but does not directly establish the all-moment constants asserted here.

## Limitations
The result concerns a fixed, explicitly identified cubic global center, not all cases of the 2023 classification. The limits are not uniform as \(q\) approaches two while energy grows, and no rate of weak convergence or global monotonicity theorem is asserted. Existence of a more abstract published equivalent theorem is a residual priority risk; searches and relevant full-text comparisons do not prove absolute publication novelty. The included checker runs finite computations only, and independent mathematical validation has not been performed.

## References
1. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1, first public 2023-10-11, Theorem 2(f), equation (35), https://arxiv.org/pdf/2310.07454.
2. A. Ghose-Choudhury and P. Guha, *Monotonicity of the period function of the Liénard equation of second kind*, arXiv:1608.02910v1, 2016-08-08, section 2, https://arxiv.org/pdf/1608.02910.
3. A. Cima, A. Gasull and F. Mañosas, *Period Function for a Class of Hamiltonian Systems*, Journal of Differential Equations 168 (2000), 180–199, DOI:10.1006/jdeq.2000.3912; general period-function context, not asserted to have been checked in full.
4. *Cauchy time concentration and the order-one moment threshold in a cubic global center*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cauchy-time-concentration-and-the-order-one-moment-threshold-in--0ac06783efe2.
5. *Logarithmic occupation and the two-term high-energy period of a cubic global center*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-logarithmic-occupation-and-the-two-term-high-energy-period-of-a--8be50b06b677.
