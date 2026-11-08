# A two-thirds fast-cycle law for optimal resetting in a Brownian Otto protocol

## Finding

In a two-temperature overdamped harmonic Otto protocol, a particle is independently reset to the trap minimum at Poisson rate \(r\geq0\). Its two isochoric contact stages have equal duration \(\tau>0\), and the harmonic stiffness switches instantaneously between \(k_H>k_C>0\). The hot stage has stiffness \(k_H\) and bath temperature \(T_H\); the cold stage has stiffness \(k_C\) and bath temperature \(T_C\). Assume
\[
T_H>T_C>0,\qquad \frac{T_H}{k_H}>\frac{T_C}{k_C}.
\]
Let \(W_\tau(r)\) denote the average mechanical work extracted exclusively at the two stiffness quenches per cycle in the unique periodic second-moment state. This definition does not include the energy consumed or delivered by implementing resets.

Set
\[
\Delta k=k_H-k_C,\quad a=2k_H,\quad b=2k_C,\quad
\alpha=T_H-T_C,\quad \beta=T_Hb-T_Ca,\quad K=(T_H+T_C)(a-b).
\]
Here \(\Delta k,\alpha,\beta,K\) are positive. For every \(\tau>0\),
\[
W_\tau(r)=\Delta k\,\frac{\alpha r+\beta}{(r+a)(r+b)}
\frac{\bigl(1-e^{-(r+a)\tau}\bigr)\bigl(1-e^{-(r+b)\tau}\bigr)}{1-e^{-(2r+a+b)\tau}}.
\tag{1}
\]
Every \(W_\tau\) has at least one global maximizer on \([0,\infty)\). As \(\tau\downarrow0\), **every** choice \(r_\tau\) of a global maximizer satisfies the same sharp asymptotic law
\[
\boxed{\displaystyle r_\tau\sim c_*\tau^{-2/3},\qquad c_*^3=\frac{3K}{\alpha}=\frac{6(T_H+T_C)(k_H-k_C)}{T_H-T_C}.}
\tag{2}
\]
In particular, all global maximizers are positive for sufficiently small \(\tau\); no finite-cycle uniqueness is claimed. The maximum mechanical output has the two-term expansion
\[
\boxed{\displaystyle \max_{r\geq0}W_\tau(r)
=\Delta k\,\tau\left[\frac{\alpha}{2}
-\frac{3K}{8c_*}\tau^{2/3}+o(\tau^{2/3})\right].}
\tag{3}
\]
By comparison, \(W_\tau(0)/(\Delta k\tau)\to\beta/(a+b)<\alpha/2\). Thus optimal resetting changes the leading fast-cycle work coefficient and has an anomalous, noninteger control exponent.

## Assumptions and scope

Set mobility and Boltzmann's constant equal to one. During a stage with stiffness \(k\) and temperature \(T\), the coordinate obeys the overdamped stochastic equation \(dX_t=-kX_t\,dt+\sqrt{2T}\,dB_t\), and, independently, instantaneous resets replace \(X_t\) by zero at Poisson rate \(r\). A reset does not alter the externally prescribed stage clock. The hard/hot and soft/cold stages are each of length \(\tau\), in that order; bath and stiffness changes are ideal instantaneous quenches with continuous particle position. The two-stage periodic second moment is considered after transients. Only the mechanical work of those prescribed stiffness quenches is optimized, not total accounting after reset-actuator costs, entropy production, efficiency or net power including implementation costs. The theorem is for strictly positive stiffnesses and temperatures satisfying the displayed engine ordering. No assumptions on a Gaussian stationary distribution are needed.

## Proof

**1. Periodic moment balance.** Write \(v(t)=\mathbb E[X_t^2]\). Itô's formula and the reset jump term give \(\dot v=-(2k+r)v+2T\) in each constant stage. Put \(A=r+a\), \(B=r+b\), \(m_H=2T_H/A\), \(m_C=2T_C/B\), and denote by \(v_H\) and \(v_C\) the moments at the ends of the hot and cold stages. Then
\[
v_H=e^{-A\tau}v_C+(1-e^{-A\tau})m_H,\qquad
v_C=e^{-B\tau}v_H+(1-e^{-B\tau})m_C.
\]
The period map contracts second moments by \(e^{-(A+B)\tau}<1\), hence it has a unique periodic second moment. Eliminating the two unknown moments yields
\[
v_H-v_C=F_\tau(r)(m_H-m_C),\quad
F_\tau(r)=\frac{(1-e^{-A\tau})(1-e^{-B\tau})}{1-e^{-(A+B)\tau}}.
\]
The hard-to-soft quench extracts \(\Delta k\,v_H/2\), and the reverse quench costs \(\Delta k\,v_C/2\). Thus \(W_\tau=\Delta k(v_H-v_C)/2\). Inserting \(m_H-m_C=2(\alpha r+\beta)/(AB)\) proves (1). It also gives \(W_\tau(r)>0\). The expression is continuous on \([0,\infty)\) and tends to zero as \(r\to\infty\) for each fixed positive \(\tau\), so a global maximizer exists.

**2. Global upper envelope.** Set \(s=a+b\), and normalize
\[
G_\tau(r)=\frac{W_\tau(r)}{\Delta k\tau}
=g(r)H_\tau(r),\quad g(r)=\frac{\alpha r+\beta}{2r+s}
=\frac\alpha2-\frac{K}{2(2r+s)},
\]
\[
H_\tau(r)=\frac{(A+B)F_\tau(r)}{AB\tau}.
\]
With \(x=A\tau/2>0\) and \(y=B\tau/2>0\), elementary hyperbolic identities show
\[
H_\tau(r)=\frac{x+y}{xy(\coth x+\coth y)}<1
\]
because \(z\coth z>1\) for every \(z>0\). Hence \(0<G_\tau(r)<\alpha/2\), uniformly in \(r\geq0\). For \((A+B)\tau\to0\), expansion of \(\sinh\) at zero gives, uniformly on such regions,
\[
H_\tau(r)=1-\frac{AB\tau^2}{12}
+O((A+B)^4\tau^4).
\tag{4}
\]

**3. A matching benchmark.** For any fixed \(c>0\), choose \(r=c\tau^{-2/3}\). Then \(r\to\infty\), \(r\tau\to0\), and equations above give
\[
G_\tau(c\tau^{-2/3})
=\frac\alpha2-\tau^{2/3}\left(\frac{K}{4c}+\frac{\alpha c^2}{24}\right)+o(\tau^{2/3}).
\tag{5}
\]
In particular, \(\max G_\tau\to\alpha/2\).

**4. Tight scale of every optimizer.** Choose any maximizing \(r_\tau\). Since \(G_\tau(r_\tau)\to\alpha/2\) but \(g(r)<\alpha/2\) for bounded \(r\), necessarily \(r_\tau\to\infty\). Furthermore \(r_\tau\tau\to0\): otherwise, along a subsequence with \(r_\tau\tau\to u\in(0,\infty]\), the hyperbolic formula for \(H\), using \(A/B\to1\), gives \(H\to2\tanh(u/2)/u<1\) if \(u<\infty\), and \(H\to0\) if \(u=\infty\). This contradicts \(G_\tau(r_\tau)\to\alpha/2\).

By benchmarking (5), there is a constant \(C>0\) such that
\[
\frac\alpha2-G_\tau(r_\tau)\le C\tau^{2/3}.
\]
This deficit decomposes into the nonnegative terms \(\alpha/2-g(r_\tau)\) and \(g(r_\tau)[1-H_\tau(r_\tau)]\). The former equals \(K/[2(2r_\tau+s)]\), proving \(r_\tau\ge c_1\tau^{-2/3}\) for small \(\tau\). Since \(r_\tau\to\infty\) and \(r_\tau\tau\to0\), the uniform expansion (4) gives \(1-H_\tau(r_\tau)\ge c_2r_\tau^2\tau^2\) and \(g(r_\tau)\ge\alpha/4\) for small \(\tau\). Thus \(r_\tau\le c_3\tau^{-2/3}\). The family \(c_\tau=r_\tau\tau^{2/3}\) therefore remains in a compact subinterval of \((0,\infty)\).

**5. Unique scaling limit and optimal value.** Equation (5) is uniform when \(c\) lies in any fixed compact subset of \((0,\infty)\). By maximality, each subsequential limit of \(c_\tau\) must minimize
\[
f(c)=\frac{K}{4c}+\frac{\alpha c^2}{24},\qquad c>0.
\]
Its derivative vanishes exactly at \(c^3=3K/\alpha\); its second derivative \(K/(2c^3)+\alpha/12\) is strictly positive. Therefore all subsequential limits agree at \(c_*\), proving (2). Substituting \(c_*\) into (5), and using \(\alpha c_*^3=3K\), gives (3). Finally, \(G_\tau(0)\to g(0)=\beta/s=\alpha/2-K/(2s)<\alpha/2\), completing the claimed no-reset comparison.

## Verification

The accompanying standalone `verify_claim.py` checks the symbolic two-stage fixed-point formula, the exact identity for \(K\), the second-order hyperbolic attenuation expansion, and the unique minimizer equation. It also independently integrates the variance ODE for multiple parameter choices and numerically optimizes the exact work for four shrinking half-periods. In the example \(T_H=4\), \(T_C=1\), \(k_H=3\), \(k_C=1\), the predicted coefficient is \(c_*=20^{1/3}\), and the ratio between optimized reset rate and \(c_*\tau^{-2/3}\) approaches one. Numerical tests support the analytic proof; they are not themselves a proof of the all-parameter and all-optimizer statements. Run with `python verify_claim.py` using Python with SymPy and SciPy installed.

## Relationship to prior work

Lahiri and Gupta [1] analyze a Brownian harmonic heat engine with Poisson resetting and a **linearly time-varying stiffness**, finding numerically nonmonotone extracted mechanical work versus resetting rate and carefully distinguishing mechanical output from resetting work. Their four-stroke Stirling protocol is not the fixed-stiffness, two-contact instantaneous-quench Otto protocol of (1), and their analysis does not state the short-contact \(\tau^{-2/3}\) law or the sharp correction (3). The present work adopts that physical distinction between mechanical quench work and reset-actuator costs rather than claiming a net-efficiency theorem.

Olsen and coauthors [2] study the thermodynamic cost of finite-time resetting by *switching between exploration and return potentials*, not a deterministic two-temperature Otto protocol with independent origin resets. Kumar and coauthors [3] examine two- and three-level **quantum** Otto engines with resetting during thermal contacts; their state space and reset rule are different, and their work analysis does not give the classical harmonic short-cycle scale. Farago [4] studies entropy production over individual resetting cycles in a single thermal bath, rather than quench work in a two-temperature protocol. Basic variance and quench-work formulas are standard; the claim of contribution is only the globally optimized fast-cycle exponent and coefficient with the required all-maximizer argument. Published general results could still make this asymptotic accessible by further reductions, and no priority guarantee is asserted.

## Limitations

The result is an asymptotic theorem as \(\tau\downarrow0\), not a finite-\(\tau\) uniqueness theorem. The reset map is instantaneous and pinned to the trap minimum; mobility is one; stages have equal length; stiffness is constant within each contact; the thermal baths are ideal. Only quench-extracted mechanical work is optimized. Resetting requires external physical resources whose energetic costs are not specified here; consequently no claim is made about positive **net** output or heat-engine efficiency once reset costs are included. Finite-time reset implementation, arbitrary driving protocols, stochastic work fluctuations and nonsymmetric contact lengths are outside the result. A comparison of explicitly published formulas does not rule out every unpublished or implicit prior derivation.

## References

[1] S. Lahiri and S. Gupta, *Efficiency of a microscopic heat engine subjected to stochastic resetting*, arXiv:2308.15212, first posted 2023-08-29, https://arxiv.org/abs/2308.15212.

[2] K. S. Olsen, D. Gupta, F. Mori, and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, arXiv:2310.11267, first posted 2023-10-17, https://arxiv.org/html/2310.11267v5.

[3] A. Kumar, S. Lahiri, T. Bagarti, and S. Banerjee, *Two and three-state quantum heat engines with stochastic resetting*, arXiv:2503.06124, first posted 2025-03-08, https://arxiv.org/abs/2503.06124.

[4] O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445, first posted 2026-05-27, https://arxiv.org/abs/2605.28445.
