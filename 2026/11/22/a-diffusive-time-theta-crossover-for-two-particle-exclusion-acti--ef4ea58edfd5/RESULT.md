# A diffusive-time theta crossover for two-particle exclusion activity on a ring

## Finding

Consider the continuous-time symmetric simple exclusion process on the cycle \(C_n\), \(n\ge3\), with exactly two indistinguishable particles, each accepted nearest-neighbor hop occurring at rate one. Start with the uniform distribution on unordered occupied pairs. Write \(K_n(t)\) for the total number of accepted hops up to time \(t\ge0\), and set \(N=n-1\), \(J=\lfloor (n-2)/2\rfloor\),
\[
\mu_n=\frac{4(n-2)}{n-1},\qquad
\lambda_{j,n}=8\sin^2\!\left(\frac{\pi j}{n-1}\right).
\]
For every integer \(n\ge3\) and real \(t\ge0\), the **exact, finite-observation-time** activity cumulants are
\[
\boxed{\begin{aligned}
\mathbb E K_n(t)&=\mu_n t,\\
\operatorname{Var} K_n(t)&=\mu_n t+\frac{64}{N^2}\sum_{j=1}^{J}\cos^2\!\left(\frac{\pi j}{N}\right)
\left[\frac{t}{\lambda_{j,n}}-\frac{1-e^{-\lambda_{j,n}t}}{\lambda_{j,n}^{2}}\right].
\end{aligned}}
\tag{1}
\]
The empty sum for \(n=3\) means \(K_3(t)\) is Poisson of mean \(2t\). For every \(n\ge4\), the time-window Fano ratio \(F_n(t)=\operatorname{Var}K_n(t)/(\mu_n t)\) is strictly increasing for \(t>0\), with \(F_n(0+)=1\) and
\[
\lim_{t\to\infty}F_n(t)=1+\frac{n-3}{3(n-1)}.
\tag{2}
\]
The long-time value in (2), **but not the finite-time expression (1)**, is already implied by the general periodic-SSEP activity-cumulant formula of Appert-Rolland, Derrida, Lecomte and van Wijland (2008, Section II.1, equation (12)). Equation (2) is included as a consistency boundary, not asserted as a new result.

The **new diffusive observation-window law** is as follows. For each real \(x>0\), letting \(t=x(n-1)^2\) and then \(n\to\infty\) yields
\[
\boxed{\Phi(x):=\lim_{n\to\infty} F_n\bigl(x(n-1)^2\bigr)
=\frac43-\frac{1}{4\pi^4x}\sum_{j=1}^{\infty}\frac{1-e^{-8\pi^2j^2x}}{j^4}.}
\tag{3}
\]
The series is absolutely convergent for every \(x>0\). Its crossover is strictly increasing, with \(\Phi(0+)=1\) and \(\Phi(\infty)=4/3\). Both endpoints have sharper expansions:
\[
\boxed{\begin{aligned}
\Phi(x)&=1+\frac{8\sqrt2}{3\sqrt\pi}\sqrt{x}-4x+o(x),&&x\downarrow0,\\
\Phi(x)&=\frac43-\frac{1}{360x}+O\!\left(\frac{e^{-8\pi^2x}}{x}\right),&&x\to\infty.
\end{aligned}}
\tag{4}
\]
In particular, the fixed-time dilute limit and the long-time limit do not commute:
\[
\lim_{t\to\infty}\lim_{n\to\infty}F_n(t)=1,
\qquad
\lim_{n\to\infty}\lim_{t\to\infty}F_n(t)=\frac43.
\tag{5}
\]

## Assumptions and scope

The vertices of \(C_n\) are integers modulo \(n\). A configuration consists of two distinct occupied vertices. Each directed nearest-neighbor occupied-to-vacant exchange is an independent exponential-rate-one transition; rejected attempts are omitted from \(K_n(t)\). The starting law is uniform over the \(\binom n2\) configurations and is invariant under the reversible dynamics. We count the sum of all accepted hops, not a signed current, a tagged-particle displacement, an occupation-time integral, or an asymptotic tilted-ensemble observable. The exact formula (1) holds at **every finite time**, including early windows, and is not inferred from an infinite-time cumulant. Rates have physical units inverse time. For \(n=3\) the graph is the simple triangle with no duplicated edge. Formula (3) concerns the joint scaling where the particle count remains two and the observation time is quadratic in the number of sites.

## Proof

**1. Relative-gap reduction and stationary intensity.** Give the two particles uniformly random labels for analysis. The clockwise gap \(D\) from the first to the second takes values \(1,\ldots,N=n-1\). Uniformly sampling an ordered pair of distinct sites makes \(D\) uniform over these \(N\) values. Under particle hops, \(D\) is a reflecting nearest-neighbor walk on \(\{1,\ldots,N\}\), with rate \(2\) on each permitted gap transition:
\[
(Qf)(k)=2\mathbf1_{\{k>1\}}[f(k-1)-f(k)]+2\mathbf1_{\{k<N\}}[f(k+1)-f(k)].
\]
The full accepted-hop intensity conditional on \(D=k\) is
\[
a(k)=4-2\bigl(\mathbf1_{\{k=1\}}+\mathbf1_{\{k=N\}}\bigr).
\]
(The factor two records the two rejected directed hops when the particles are adjacent.) Averaging over uniform \(D\) gives \(\mu_n=4-4/N\). For \(n=3\), \(N=2\) and this intensity is constantly two, so the jump-time process is Poisson.

**2. Marked-jump covariance identity.** On the original \(\binom n2\) unordered-pair state space, let \(L\) be the reversible generator and \(B\) its nonnegative off-diagonal jump-rate operator (with zero diagonal). The marked-count generating semigroup has generator \(L_z=L+(e^z-1)B\). The stationary uniform measure \(\pi\) obeys \(B1=a\) and \(\langle1,Bf\rangle_\pi=\langle a,f\rangle_\pi\), by symmetry of the transition rates. Differentiating the generating semigroup twice at \(z=0\) and subtracting the squared mean gives the exact **finite-time** identity
\[
\operatorname{Var} K_n(t)=\mu_n t+2\int_0^t(t-u)\,
\langle a-\mu_n,e^{uL}(a-\mu_n)\rangle_\pi\,du.
\tag{6}
\]
Since \(a\) depends only on \(D\), the autocovariance in (6) equals the uniform-endpoint autocovariance under \(Q\), and counts all allowed transitions, with no approximation of the jump-intensity observable.

**3. Reflecting-cosine spectrum.** The orthonormal eigenmodes of \(-Q\) in the uniform gap law are the constant mode and, for \(h=1,\ldots,N-1\),
\[
v_h(k)=\sqrt2\cos\!\left(\frac{\pi h(k-1/2)}N\right),
\qquad \Lambda_h=4\bigl[1-\cos(\pi h/N)\bigr].
\]
For \(a-\mu_n=-2(\mathbf1_{\{k=1,N\}}-2/N)\), all odd-indexed cosine coefficients vanish. The squared uniform-projection onto \(h=2j\) is exactly \(32\cos^2(\pi j/N)/N^2\), with eigenvalue \(\Lambda_{2j}=\lambda_{j,n}\). Therefore
\[
\langle a-\mu_n,e^{uQ}(a-\mu_n)\rangle
=\frac{32}{N^2}\sum_{j=1}^{J}\cos^2\!\left(\frac{\pi j}N\right)e^{-\lambda_{j,n}u}.
\tag{7}
\]
Substitute (7) into (6) and integrate \(\int_0^t(t-u)e^{-\lambda u}du=t/\lambda-(1-e^{-\lambda t})/\lambda^2\) to prove (1). Each term of \(F_n(t)-1\) is a positive multiple of \(1/\lambda-(1-e^{-\lambda t})/(\lambda^2t)\), a strictly increasing function for positive \(t\). This proves strict time-window monotonicity when \(n\ge4\).

**4. Infinite-time benchmark and dilute noncommutativity.** The stationary mean-zero solution of \(-Qg=\mathbf1_{\{1,N\}}-2/N\), with gap coordinates \(k=0,\ldots,N-1\), has
\[
g(k)=\frac{(N-1)(N-2)}{12N}-\frac k2+\frac{k(k+1)}{2N}.
\]
Direct substitution at the endpoints and interior gives the Poisson equation, with \(\sum_k g(k)=0\). Evaluating its endpoint Green pairing in (6) yields (2). The same value follows from the previously published general ring cumulant cited above; it is **not a novelty claim**. For each fixed \(t\), (1) gives \(F_n(t)\to1\): the adjacent-particle stationary probability is \(2/N\), and the variance correction is bounded by \(2t^2\operatorname{Var}_\pi(a)=O(t^2/N)\). Combining with (2) proves (5).

**5. Diffusive limit and edge asymptotics.** In (1), fix \(j\) and let \(N\to\infty\) with \(t=xN^2\). Then \(N^2\lambda_{j,n}\to8\pi^2j^2\), while \(\cos(\pi j/N)\to1\). The elementary inequality \(\sin(\pi j/N)\ge2j/N\) for \(1\le j\le J\) gives a summable \(O(j^{-2})\) majorant for each contribution to the Fano ratio, establishing termwise convergence by dominated summation. Rearranging the limiting sum with \(\sum_{j\ge1}j^{-2}=\pi^2/6\) yields (3). Termwise monotonicity of \((1-e^{-cj^2x})/x\) shows strict increase, and dominated convergence gives both limits.

For large \(x\), use \(\sum_{j\ge1}j^{-4}=\pi^4/90\) and bound the exponentially small remainder by \(O(e^{-8\pi^2x})\) to obtain the second expansion in (4). For small \(x\), differentiate \(S(x)=\sum_{j\ge1}(1-e^{-8\pi^2j^2x})/j^4\) twice:
\[
S''(x)=-(8\pi^2)^2\sum_{j\ge1}e^{-8\pi^2j^2x}.
\]
Poisson summation for the Gaussian, or the Jacobi theta identity, gives
\[
\sum_{j\ge1}e^{-8\pi^2j^2x}
=\frac{1}{2\sqrt{8\pi x}}-\frac12+O\!\left(x^{-1/2}e^{-1/(8x)}\right).
\]
Integrate twice using \(S(0)=0\) and \(S'(0)=8\pi^2\sum_{j\ge1}j^{-2}=4\pi^4/3\). Substitution into (3) produces precisely the \(\sqrt x\) cusp and the linear correction in (4). These arguments establish the asserted all-size and scaling limits without inferring an infinite statement from finite experiments.

## Verification

Two runnable, standalone Python standard-library scripts accompany this result: `verify_event_moments.py` independently constructs the **full unordered two-particle configuration chain** and its marked-jump moment equations; numerical uniformization checks (1) for 70 distinct configurations of ring size and observation time, with sizes \(3\) through \(16\). `verify_green_limit.py` uses exact rational arithmetic to solve 248 reflecting-gap Poisson equations, tests the long-time cumulant against the published 2008 expression, and checks 12 finite diffusive-scale approximations to (3). Commands: `python3 verify_event_moments.py` and `python3 verify_green_limit.py`. These finite checks corroborate, but do not replace, the analytic proof.

## Relationship to prior work

Appert-Rolland, Derrida, Lecomte and van Wijland (2008), *Universal cumulants of the current in diffusive systems on a ring*, explicitly compute the **long-time cumulants of total activity** for general particle count and ring length, including the full long-time Fano ratio that specializes to (2). Their Section II.1 defines the time-asymptotic eigenvalue and gives the exact second long-time cumulant in equation (12). Consequently this work does **not** claim a novel long-time cumulant formula or a new tilted-generator framework. Its proposed increment is the full observation-time function (1), its strictly increasing window-to-window ratio, and the two-particle **diffusive-time scaling curve, square-root onset and noncommuting limits** (3)--(5). A time-asymptotic eigenvalue alone does not determine the finite-time transient covariance spectral weights or the limit (3).

Lecomte, Garrahan and van Wijland (2012), *Inactive dynamical phase of a symmetric exclusion process on a ring*, analyze activity-biased dynamical phases on periodic rings and size-dependent regimes of that **long-time biased ensemble**. The inspected model and methods are closely relevant, but its reported claims do not provide the exact finite-time dilute-particle crossover (1)--(4). Previously published finite-network results establish the universal Poisson-activity criterion, the long-time noise for Hamming graphs, and integrated **occupation** noise on cycles, which are mathematically different observables or limit procedures. Known transition-semigroup methods and theta-function asymptotics underlie the proof and are not claimed as new. A differently indexed historical computation of the same finite-time SSEP second cumulant cannot be excluded.

## Limitations

The exact result is for the symmetric, homogeneous **two-particle** canonical stationary ring at rate one per successful directional hop; the new crossover fixes particle count two while allowing ring size and observation time to diverge together. It does not prove analogous laws at positive macroscopic density, nonstationary initialization, general graphs, asymmetric hopping, higher count cumulants, or the full counting-process weak limit. Its rigorous scope is the displayed variance and Fano ratio. The earlier long-time value is acknowledged as known. Historical originality is based on examined literature and indexed comparisons, not an exhaustive priority certificate; no independent scientific audit has been performed.

## References

1. C. Appert-Rolland, B. Derrida, V. Lecomte and F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590v1, public 2008-04-16; Section II.1, particularly equations (1) and (12), https://arxiv.org/html/0804.2590v1 .
2. V. Lecomte, J. P. Garrahan and F. van Wijland, *Inactive dynamical phase of a symmetric exclusion process on a ring*, arXiv:1203.1600v1, public 2012-03-07; Introduction and main activity-biased model, https://arxiv.org/abs/1203.1600 .
3. G. S. Causer, M. C. Bañuls and J. P. Garrahan, *Finite time large deviations via matrix product states*, arXiv:2108.11418, first public 2021-08-25, https://arxiv.org/abs/2108.11418 .
