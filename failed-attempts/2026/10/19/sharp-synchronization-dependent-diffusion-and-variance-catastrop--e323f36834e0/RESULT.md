# Sharp synchronization-dependent diffusion and variance catastrophe in a nonreciprocal Brownian dimer

## Finding
Consider the four-state stochastic coupling protocol defined below, with positive parameters \(K,\lambda,a,D\), and synchronization \(0\leq\chi<1\). Set
\[
\alpha=\lambda(1-\chi),\qquad
A=a^2,\qquad
B=K(K+\lambda)(K+2\alpha)-A(K+\alpha),\qquad
N=(K+\lambda)(K+2\alpha)-A.
\]
There exists a unique stationary interparticle-separation law for every parameter choice, but it has finite second moment **if and only if** \(B>0\). On precisely this region, every stationary center-of-mass increment has finite variance and its exact law of second moments is
\[
\operatorname{Var}(X_t-X_0)
=Dt+A w\left[\frac{t}{K+2\lambda}-\frac{1-e^{-(K+2\lambda)t}}{(K+2\lambda)^2}\right],\qquad
w=\frac{DN}{2B},\quad t\geq0.
\]
Consequently the exact effective diffusivity is
\[
\boxed{\mathcal D(\chi)=\frac D2+\frac{AD\,N}{4(K+2\lambda)B}.}
\]
The normalized velocity autocorrelation has the *same* exponential decay rate \(K+2\lambda\) at every synchronization, even though its amplitude and existence depend sharply on synchronization.

The complete synchronization response is as follows. If \(0<A<K(K+\lambda)\), finite diffusivity exists at every \(0\leq\chi<1\) and \(\mathcal D\) **decreases strictly** with \(\chi\). At the exact surface \(A=K(K+\lambda)\), finite diffusivity exists at every \(\chi<1\), but is **independent of \(\chi\)**: \(\mathcal D=D/2+AD/[2K(K+2\lambda)]\). If
\(K(K+\lambda)<A<K(K+2\lambda)\), put
\[
\alpha_c=\frac{K[A-K(K+\lambda)]}{2K(K+\lambda)-A},\qquad
\chi_c=1-\frac{\alpha_c}{\lambda}.
\]
Then \(0<\chi_c<1\); finite diffusivity exists exactly for \(0\leq\chi<\chi_c\), increases strictly throughout this interval, and diverges with the sharp simple pole
\[
\boxed{\mathcal D(\chi)\sim
\frac{DA^2\alpha_c}{4K(K+2\lambda)[2K(K+\lambda)-A]\lambda}
\frac1{\chi_c-\chi}.}
\]
For \(A\geq K(K+2\lambda)\), no \(0\leq\chi<1\) admits a finite stationary increment variance. Whenever \(B\leq0\), \(\mathbb E[(X_t-X_0)^2]=\infty\) at **every** \(t>0\), despite the existence of the stationary separation law.

A separate endpoint effect occurs at perfect synchronization \(\chi=1\): its four-state chain separates into reciprocal and nonreciprocal classes. When \(0<a<K\), both classes have finite separation second moment, with center diffusivities \(D/2\) and \(D/2+AD/[2K(K+2\lambda)]\), respectively; the \(\chi\uparrow1\) ergodic limit is their arithmetic mean, not the second (pure nonreciprocal) class value.

## Assumptions and scope
Let \(S_t\) be an autonomous continuous-time Markov chain on the ordered states \((++),(+-),(--),(-+)\), with generator \(Q\). Every transition between neighboring states on this four-cycle occurs at rate \(\alpha=\lambda(1-\chi)\); every transition between opposite states occurs at rate \(\beta=\lambda\chi\). Here \(\lambda,K,a,D>0\) and \(0\leq\chi<1\), hence \(\alpha>0\). The unique stationary law of \(S\) is uniform.

For states in the displayed order define the sum fluctuations \(\phi=(a,0,-a,0)\) and difference fluctuations \(\psi=(0,a,0,-a)\). Let \(W^X,W^Y\) be independent standard two-sided Brownian motions, independent of the chain. The position of the center \(X\) and relative displacement \(Y\) solve
\[
 dY_t=-(K+\phi(S_t))Y_t\,dt+\sqrt{4D}\,dW^Y_t,\qquad
 dX_t=-\tfrac12\psi(S_t)Y_t\,dt+\sqrt D\,dW^X_t.
\]
These are the coordinates of the two-particle fluctuating-spring Langevin model, with \(K=2\bar k\), \(a=2\kappa_0\), and \(D=D_x\). The assertion concerns stationary increments of the free center, with \((S,Y)\) started from its unique stationary law. It does not assert stationarity of \(X\) itself.

## Proof
**1. Existence of the stationary separation.** The chain with \(\alpha>0\) is irreducible and reversible, with stationary probabilities \(1/4\). Its stationary mean of \(\phi\) vanishes. The stationary stochastic convolution
\[
Y_t=\sqrt{4D}\int_{-\infty}^t
\exp\left(-\int_s^t[K+\phi(S_u)]\,du\right)\,dW^Y_s
\]
exists almost surely: by the two-sided ergodic theorem the inner time integral divided by \(t-s\) tends to \(K>0\). This also gives uniqueness by contraction along each two-sided chain path. No finite variance is presumed.

**2. Exact second-moment boundary.** The conditional Gaussian second moment from the above stochastic convolution is finite after stationary averaging exactly when
\(\int_0^\infty \boldsymbol\pi^{\mathsf T}e^{[Q-2\operatorname{diag}(K+\phi)]s}\mathbf1\,ds<\infty\).
By irreducibility and Perron--Frobenius positivity for Metzler matrices this is equivalent to positive definiteness of the symmetric matrix
\(H=2\operatorname{diag}(K+\phi)-Q\). In the orthonormal sum/difference basis for each pair of opposite chain states, one mode has eigenvalue \(2(K+2\lambda)>0\); the remaining block is twice
\[
\begin{pmatrix}
K+\alpha&a&-\alpha\\
a&K+\lambda&0\\-\alpha&0&K+\alpha
\end{pmatrix}.
\]
Schur complementation of the two positive diagonal pivots \(K+\lambda\) and \(K+\alpha\) shows strict positivity precisely when
\[
K+\alpha-\frac{a^2}{K+\lambda}-\frac{\alpha^2}{K+\alpha}>0,
\]
which, after multiplying by \((K+\lambda)(K+\alpha)>0\), is exactly \(B>0\). At equality the leading exponential rate is zero and the integral still diverges, by strictly positive Perron projections.

**3. Amplitude and autocorrelation.** In the finite-second-moment regime put
\(w_i=\mathbb E[Y_0^2\mathbf1_{\{S_0=i\}}]\). Stationarity and Itô's formula yield
\(Hw=D\mathbf1\), since each state receives \(4D\times(1/4)=D\) of noise variance per unit time. The permutation exchanging the two nonreciprocal states gives \(w_{+-}=w_{-+}=:w\). Write \(U=w_{++}+w_{--}\), \(V=w_{++}-w_{--}\). The reduced equations are
\[
(K+\alpha)U+aV-2\alpha w=D,\qquad
(K+\lambda)V+aU=0,\qquad
2(K+\alpha)w-\alpha U=D.
\]
Their unique solution gives \(w=DN/(2B)\). In particular \(w>0\).

The key exact eigenfunction identity is
\[
[Q-\operatorname{diag}(K+\phi)]\psi=-(K+2\lambda)\psi.
\]
Thus, conditioning on the initial separation and chain state,
\(\mathbb E[\psi(S_t)Y_t\mid S_0,Y_0]=e^{-(K+2\lambda)t}\psi(S_0)Y_0\).
For the zero-mean propulsion \(v_t=-\psi(S_t)Y_t/2\) this implies the **exact** stationary covariance
\[
\mathbb E[v_0v_t]=\frac{a^2w}{2}e^{-(K+2\lambda)|t|}.
\]
The independent center Brownian noise contributes \(Dt\) to increment variance. Integrating the covariance over the time square proves the finite-time formula and its effective-diffusivity limit, with no truncation or asymptotic interchange beyond the integrability already established.

**4. Complete phase diagram and its boundaries.** Differentiation of the explicit rational conditional moment gives
\[
\frac{\partial w}{\partial\alpha}
=\frac{Da^2[K(K+\lambda)-a^2]}{2B^2}.
\]
Because \(d\alpha/d\chi=-\lambda\), this proves strict monotonicity and its reversal, and establishes constancy exactly when \(A=K(K+\lambda)\). Moreover \(B\) is affine and strictly increasing in \(\alpha\) throughout any nonempty stability region. Solving \(B=0\) yields the displayed \(\alpha_c\), while \(B(0)=K[K(K+\lambda)-A]\) and \(B(\lambda)=(K+\lambda)[K(K+2\lambda)-A]\). These endpoint signs establish all four regimes, including the boundary equalities. The pole follows by substituting \(B=[2K(K+\lambda)-A]\lambda(\chi_c-\chi)\) and \(N(\alpha_c)=A\alpha_c/K\).

If \(B\leq0\), irreducibility and the positive Perron eigenvector show \(\mathbb E[Y_0^2\mathbf1_{\{S_0=(+-)\}}]=\infty\). Condition on \(S_0=(+-)\) and no subsequent chain transition before a fixed \(t>0\), an event of strictly positive conditional probability independent of \(Y_0\). On that event the center displacement is a nonzero multiple of \(Y_0\), namely \(-a(1-e^{-Kt})Y_0/(2K)\), plus a finite-variance Gaussian term independent of \(Y_0\). Its squared expectation is infinite. The same holds unconditionally for every \(t>0\).

At \(\chi=1\), the two opposite-state classes are closed. In the nonreciprocal class \(\phi=0\), so \(\mathbb E Y^2=2D/K\) and \(\psi^2=a^2\); in the reciprocal class \(\psi=0\). The two formulas at the endpoint follow directly. For \(a<K\), the limit \(\alpha\downarrow0\) in the ergodic expression gives \(w\to D/(2K)\), yielding exactly the arithmetic mean of their diffusivities.

## Verification
`CHECK.py` performs exact rational 4-state linear-system solves, calculates all four conditional second moments independently of the reduced formula, verifies the killed-generator eigenfunction identity, compares the Green--Kubo diffusion correction, and checks the derivative factorization. It passed 828 parameter-grid configurations and 27 exact compensation-surface identities. The checks include both monotonicity regimes and finite-second-moment boundaries; the analytic proof supplies the infinite-domain implications. Run `python3 CHECK.py` with a standard Python 3 interpreter.

For example, take \(K=2\), \(\lambda=D=1\), and \(a^2=7\). The critical synchronization is \(\chi_c=3/5\), and \(\mathcal D(0)=59/48\), \(\mathcal D(1/2)=9/4\); at all \(\chi\ge3/5\) with \(\chi<1\), the stationary center increment variance is infinite. At the exact compensation strength \(a^2=6\), the diffusion coefficient is instead \(7/8\) for every \(\chi<1\).

## Relationship to prior work
Cocconi, Alston and Bertrand introduce the fluctuating nonreciprocal Brownian dimer and its four-state correlated telegraph generator. Their main text explicitly restricts the discrete-fluctuation mean-square-displacement calculation to perfect synchronization \(\chi=1\) with the nonreciprocal initial class; their supplement evaluates the same exceptional sector and the reciprocal sector. The new statement concerns all \(\chi<1\), where both sectors communicate, and derives the exact stability and synchronization phase diagrams rather than re-deriving the known perfect-synchrony formula.

Huang, Jansen, Mandjes, Spreij and De Turck provide general moment machinery for Markov-modulated Ornstein--Uhlenbeck processes. Behme and Sideris give broader stationary exponential-functional machinery. These general frameworks support the mathematical method but do not directly state the special physical center-of-mass correlation eigenmode, the rational four-state diffusion law, the exact flatness surface, or the sharp synchronization-driven second-moment catastrophe. A general theorem not yet located may imply part of the result; independent priority validation is not claimed.

## Limitations
The result is an exact second-moment classification for the specified harmonic, Markov-switching, nonrepulsive model, not an assertion about all nonreciprocal particle dimers. Divergence is of the stationary increment **second moment**, not proof of absence of a stationary separation distribution or a claim about almost-sure ballistic motion. No explicit heavy-tail exponent, non-Gaussian scaling limit, entropy-production law, finite-time relaxation from arbitrary initial conditions, or nonlinear steric-force extension is asserted. The \(\chi=1\) endpoint is nonergodic and must not be substituted silently into the \(\chi<1\) result.

## References
1. L. Cocconi, H. Alston, and T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1 (first public 2023-04-16), especially equations (1), (2), (14)--(18), and supplementary equations and Fig. S1.
2. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, and K. De Turck, *Markov-modulated Ornstein--Uhlenbeck processes*, arXiv:1412.7952v1 (2014), for general modulated-OU moment methods.
3. A. Behme and A. Sideris, *Markov-modulated generalized Ornstein--Uhlenbeck processes and an application in risk theory*, arXiv:2012.10712v1 (2020), for existence and stationary exponential-functional methods.
