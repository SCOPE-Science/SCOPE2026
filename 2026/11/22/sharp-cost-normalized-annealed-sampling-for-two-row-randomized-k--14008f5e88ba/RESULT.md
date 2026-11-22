# Sharp cost-normalized annealed sampling for two-row randomized Kaczmarz

## Finding
For two nonparallel, nonorthogonal normalized rows in the real plane and independent exact Kaczmarz projections, assign positive per-update costs \(a>b\) to the first and second rows and let \(c\in(0,1)\) be the absolute row inner product. If the expensive row is chosen with probability \(p\), then the sharp annealed decay factor of the **expected squared Euclidean error per update** is
\[
\Lambda(p,c)=\frac{1+\sqrt{1-4(1-c^4)p(1-p)}}{2}.
\]
The annealed decay exponent per **expected update cost** is \(F(p)=-\log\Lambda(p,c)/(b+(a-b)p)\), with \(F(0)=F(1)=0\). Its unique global maximizing law \(p_*(c;a,b)\) is the unique solution in \((0,1/2)\) of
\[
\frac{2(1-c^4)(1-2p)[b+(a-b)p]}{s(1+s)}
=(a-b)\log\!\left(\frac{2}{1+s}\right),\qquad
s=\sqrt{1-4(1-c^4)p(1-p)}.
\]
This law lies strictly between the square-root-price allocation and fair sampling, and changes strictly monotonically with coherence:
\[
\frac{\sqrt b}{\sqrt a+\sqrt b}<p_*(c;a,b)<\frac12,
\quad c_1<c_2\ \Longrightarrow\ p_*(c_1;a,b)>p_*(c_2;a,b).
\]
The endpoints and optimum have the sharp limits
\[
\begin{aligned}
\lim_{c\downarrow0}p_*&=\tfrac12,&
\lim_{c\uparrow1}p_*&=\frac{\sqrt b}{\sqrt a+\sqrt b},\\
\lim_{c\downarrow0}\max_p F(p)&=\frac{2\log2}{a+b},&
\max_p F(p)&\sim\frac{1-c^4}{(\sqrt a+\sqrt b)^2}\quad(c\uparrow1).
\end{aligned}
\]
More precisely, with \(\chi=(a-b)\log2/(a+b)\), the nearly orthogonal expansion is
\[
p_*(c;a,b)=\frac12-\frac{\chi}{2\sqrt{1-\chi^2}}c^2+o(c^2)\quad(c\downarrow0).
\]
For equal costs \(a=b\), the unique optimum is \(p=1/2\) for every \(0<c<1\). When the second row is more expensive, interchange the labels.

## Assumptions and scope
Let \(u_1,u_2\in\mathbb R^2\) be linearly independent unit row vectors and \(|u_1^\top u_2|=c\in(0,1)\). Let \(x^\star\) be the unique solution of \(u_i^\top x=d_i\) for \(i=1,2\). From any deterministic \(x_0\ne x^\star\), choose row labels independently with \(\Pr(I_k=1)=p\in(0,1)\) and update
\[
x_{k+1}=x_k+(d_{I_k}-u_{I_k}^\top x_k)u_{I_k}.
\]
Row \(1\) has a deterministic positive evaluation cost \(a\); row \(2\) costs \(b\). The expected work after \(k\) completed updates is \(k[b+(a-b)p]\). The performance criterion is explicitly the **annealed mean-square exponent divided by expected work**, defined through \(-\lim_{k\to\infty} k^{-1}\log\mathbb E\|x_k-x^\star\|_2^2\), divided by the expected cost per update. This is *not* the mean-square decay conditioned on a fixed random wall-clock budget and *not* the quenched exponent of a typical realization. Initialization and probability-selection overheads are excluded. Only static independent sampling laws are optimized.

## Proof
**Exact two-state mean-square recurrence.** Write \(e_k=x_k-x^\star\), and let \(Q_i=I-u_i u_i^\top\). Each \(Q_i\) projects onto a one-dimensional line; repetitions leave its norm fixed, while changing the label multiplies its squared norm by \(c^2\). For \(k\ge1\), let \(v_i(k)=\mathbb E[\|e_k\|^2\mathbf1_{\{I_k=i\}}]\). Then
\[
\binom{v_1(k+1)}{v_2(k+1)}
=\begin{pmatrix}p&pc^2\\(1-p)c^2&1-p\end{pmatrix}
\binom{v_1(k)}{v_2(k)}.
\]
The matrix has trace one and determinant \((1-c^4)p(1-p)\), proving the displayed eigenvalue formula. For \(0<p<1\) and \(0<c<1\), its entries are strictly positive, and at least one component of \(v(1)\) is positive for every nonzero initial error because the row normals span \(\mathbb R^2\). Perron–Frobenius therefore gives \(\lim_{k\to\infty}(\mathbb E\|e_k\|^2)^{1/k}=\Lambda(p,c)\). The initial error may affect the prefactor, not the exponent.

**Unique optimum.** Put \(d=1-c^4\), \(s=\sqrt{1-4dp(1-p)}\), \(D=a-b>0\), \(T=b+Dp\) and \(N=-\log[(1+s)/2]\). For \(0<p<1/2\),
\[
N'=\frac{2d(1-2p)}{s(1+s)},\qquad
\operatorname{sign}(F')=\operatorname{sign}(G),\quad G=N'T-DN.
\]
Direct differentiation, with \(m=c^4\), yields
\[
N''=-\frac{4d[\,m(1+2s)-s^3\,]}{s^3(1+s)^2},\qquad G'=T N''.
\]
As \(p\) increases from zero to one-half, \(s\) decreases from one to \(\sqrt m\). On \([\sqrt m,1]\), the bracket \(H(s)=m(1+2s)-s^3\) is strictly decreasing in \(s\), because \(H'(s)=2m-3s^2\le-m<0\). Thus \(G\) either strictly decreases throughout or first increases and then strictly decreases. Moreover \(G(0)=db>0\) and \(G(1/2)=-DN(1/2)<0\). It consequently has exactly one zero in \((0,1/2)\), at which \(F\) attains its strict maximum. For \(p\ge1/2\), \(N'\le0\) and \(D>0\), so \(F'<0\). The endpoints give exponent zero.

**Optimal-share bounds and monotonicity.** Define the analytic function \(h(z)=-\log[(1+\sqrt{1-4z})/2]\) for \(0<z<1/4\). Its absolutely convergent series
\[
h(z)=\sum_{n=1}^\infty\frac{\binom{2n}{n}}{2n}z^n
\]
has strictly positive coefficients, hence \(E(z)=zh'(z)/h(z)>1\). Moreover \(E\) is strictly increasing: assigning weights proportional to \(\binom{2n}{n}z^n/(2n)\) makes \(zE'(z)\) exactly the variance of the positive-integer index \(n\). Set \(z=d p(1-p)\). The positive sign of \(F'\) is equivalent on \((0,1/2)\) to
\[
E(z)\,\frac{T(1-2p)}{D p(1-p)}>1.
\]
The fraction after \(E\) is strictly decreasing from infinity to zero. The square-root-price allocation \(p_0=\sqrt b/(\sqrt a+\sqrt b)\) uniquely maximizes \(p(1-p)/T\), so its corresponding fraction is exactly one. Thus \(F'(p_0)>0\) and the unique optimum obeys \(p_0<p_*<1/2\). At fixed \(p\), increasing \(d\) strictly increases \(E(dp(1-p))\); the unique sign change therefore moves to larger \(p\). Since \(d=1-c^4\) decreases with \(c\), the optimizer is strictly decreasing in coherence.

**Endpoints.** As \(c\uparrow1\), uniformly on the compact interval \([0,1]\), \(h(dp(1-p))/d\to p(1-p)\), so the unique optimizer tends to the square-root-price maximizer and \(\max F/d\to1/(\sqrt a+\sqrt b)^2\). As \(c\downarrow0\), \(\Lambda(p,c)\to\max(p,1-p)\). On \([0,1/2)\), the limiting objective is \(-\log(1-p)/(b+Dp)\), whose derivative numerator \(G\) is positive because it starts at \(b\) and has positive derivative \(T/(1-p)^2\); to the right of one-half the limiting objective decreases. The optimizer tends to \(1/2\), giving the limiting maximum \(2\log2/(a+b)\). For the sharper boundary layer write \(u=1-2p\), \(m=c^4\), and \(s=\sqrt{m+(1-m)u^2}\). The stationary equation forces \(u\to0\) and, by balancing \(N'T=DN\), \(u/m^{1/2}\to\chi/\sqrt{1-\chi^2}\), where \(0<\chi<\log2<1\). This yields the displayed \(c^2\) correction.

## Verification
Run `python verify.py` with Python 3 and SciPy installed. It checks 600 exact-rational transition cases (three identities per case), 125 numerical optimizer instances (five diagnostics each), four monotonicity instances and eight limit checks: 2,441 successful assertions in total. Rational checks use `fractions.Fraction`; all numerical checks use an independently bracketed Brent root. These finite checks do not establish uniqueness, strict inequalities for every cost/coherence, or asymptotic laws; those follow from the analytic proof above.

## Relationship to prior work
Anderson, Collins, Haddock, Lok and Rebrova (2025, arXiv:2511.20877v1) establish general stochastic-iteration moment and concentration bounds and explicitly develop Kaczmarz examples; their bounds motivate distinguishing mean-square behavior from typical behavior. Agaskar, Wang and Lu (2014) already give the general exact-MSE transfer operator and per-*iteration* optimal annealed sampling through spectral-radius minimization. The transfer-matrix eigenvalue here is a two-row reduction of their known operator, not independently claimed as novel. The assessed addition is the *heterogeneous cost-normalized* optimizer: its unique implicit law, strict interval and coherence monotonicity, two singular limits and orthogonal boundary layer. The published one-step cost frontier for simplex frames uses a different one-step minimax criterion, while published finite-work two-row studies compare batch/skip policies, not heterogeneous single-row prices. These are implication distinctions, not claims of exhaustive priority.

## Limitations
The result concerns exact projections onto two consistent independent real equations, two deterministic per-row costs and a fixed independent Bernoulli sampler. It does not address iteration-varying policies, stochastic/inexact costs, wall-time-conditioned MSE, quenched error, inconsistent/noisy problems, nonorthogonal projection relaxations, or more than two rows. No external independent mathematical validation has been performed. Unindexed equivalent cost-sensitive optimization results remain possible; the uniqueness and asymptotic conclusions are supported by the stated proof only.

## References
- T. Anderson, M. Collins, J. Haddock, J. Lok, E. Rebrova, *Beyond Expectation: Concentration Inequalities for Randomized Iterative Methods*, first released 2025-11-25, arXiv:2511.20877v1, https://arxiv.org/abs/2511.20877.
- A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, IEEE GlobalSIP (2014), https://doi.org/10.1109/GlobalSIP.2014.7032145, openly readable at https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content.
- S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, first released 2020-07-06, arXiv:2007.02910, https://arxiv.org/abs/2007.02910 (state-dependent residual weighting, a different selection criterion).
