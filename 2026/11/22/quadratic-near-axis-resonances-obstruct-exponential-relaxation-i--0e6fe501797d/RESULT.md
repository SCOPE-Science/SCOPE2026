# Quadratic near-axis resonances obstruct exponential relaxation in two-speed threshold resetting

## Finding

A ballistic particle repeatedly travels left from \(L>0\) to an absorbing threshold at zero and instantaneously returns to \(L\). Its speed is independently resampled after each return, taking the value \(L/a\) with probability \(p\in(0,1)\) and \(L/b\) with probability \(q=1-p\), where \(a,b>0\) are distinct flight durations. Set \(\mu=pa+qb\). The process begins with a fresh speed draw at time zero. Let \(P_t\) be its position law and \(m(t)=\mathbb E[X_t/L]\), with positions defined immediately *after* a reset at a hitting instant.

**Classical arithmetic comparison (not asserted as new).** Suppose \(b/a\in\mathbb Q\), and uniquely write \(a=mh\), \(b=nh\) with coprime positive integers \(m,n\) and \(h>0\). For each \(s\in[0,h)\), define the discrete probability law
\[
\nu_s=\frac h\mu\left[p\sum_{j=0}^{m-1}\delta_{L(1-(s+jh)/a)}+q\sum_{j=0}^{n-1}\delta_{L(1-(s+jh)/b)}\right].
\]
Then \(P_{kh+s}\to\nu_s\) in total variation as the integer \(k\to\infty\), exponentially in \(k\). In particular,
\[
\lim_{k\to\infty}m(kh+s)=\frac12+\frac{h/2-s}{\mu}.
\]
The limiting mean therefore follows a nonconstant sawtooth of period \(h\), with a jump between the left and right phase limits.

**Main finding: incommensurate case.** Suppose \(b/a\notin\mathbb Q\). Then \(P_t\) converges *weakly* to the uniform probability law on \([0,L]\), hence \(m(t)\to1/2\), but for **every** \(\beta>0\),
\[
m(t)-\frac12\ne O(e^{-\beta t})\qquad(t\to\infty).
\]
For each finite \(t\), \(P_t\) is purely atomic, so its total variation distance to that continuous uniform law remains exactly one. Thus weak spatial relaxation and exponential relaxation of the physical mean are sharply distinct.

The obstruction to exponential relaxation is quantitative. Choose any sequence of positive integers \(K\to\infty\) and integers \(M\) such that \(\delta_K=2\pi(Kb/a-M)\to0\), which exists by irrational approximation. The renewal denominator
\[
D(z)=1-pe^{-az}-qe^{-bz}
\]
has simple, nonzero roots \(\zeta_K\), for all sufficiently large such approximants, with
\[
\boxed{\ \zeta_K=\frac{2\pi iK}{a}-i\frac q\mu\delta_K-\frac{pqa^2}{2\mu^3}\delta_K^2+O(\delta_K^3).\ }
\]
These roots are genuine, uncancelled poles of the Laplace transform of \(m(t)\). Their real parts approach zero strictly from the left, with leading distance \(pqa^2\delta_K^2/(2\mu^3)\).

## Assumptions and scope

The flight times take precisely the two fixed values \(a,b\), with independent draws between completed flights and a fixed starting position \(L\). Both probabilities are strictly between zero and one; there is no diffusion or waiting at the threshold. The law at a reset instant is right-continuous, assigning the particle to \(L\). Weak convergence means convergence against all continuous functions on \([0,L]\). Total variation is normalized as \(\sup_A|P(A)-Q(A)|\). The arithmetic formula includes phases \(s=0\) but does not identify its value with the left-phase limit \(s\uparrow h\). The root expansion is along integer approximants with \(\delta_K\to0\), not a uniform expansion at arbitrary frequencies.

## Proof

**1. Renewal representation.** Put \(F=p\delta_a+q\delta_b\), the probability law of a flight duration, and let
\[
U=\sum_{j=0}^{\infty}F^{*j}
\]
be the renewal measure, including the initial renewal at zero. For a bounded continuous spatial test function \(g\), define
\[
B_g(u)=\sum_{T\in\{a,b\}}\Pr(T)\,g\bigl(L(1-u/T)\bigr)\,\mathbf1_{[0,T)}(u).
\]
Conditioning on the time of the most recent completed flight gives the exact formula
\[
\mathbb E[g(X_t)]=\int_{[0,t]}B_g(t-s)\,U(ds).
\tag{1}
\]
There is no contribution from incomplete flights preceding their last reset; each possible final flight is represented in the integrand.

**2. Arithmetic phase and its rate.** If \(a=mh\) and \(b=nh\), write \(u_k=U(\{kh\})\). The exact recurrence is \(u_0=1\) and
\[
u_k=p\,u_{k-m}\mathbf1_{k\ge m}+q\,u_{k-n}\mathbf1_{k\ge n}\quad(k\ge1).
\]
Its generating function is
\[
\sum_{k\ge0}u_k z^k=\frac1{1-pz^m-qz^n}.
\]
There is a simple pole at \(z=1\), of residue corresponding to \(h/\mu=1/(pm+qn)\). There is no other pole on the closed unit disk: the triangle inequality forces \(z^m=z^n=1\) for any unit-modulus zero of the denominator, and coprimality forces \(z=1\). Since the denominator is a polynomial, the other poles lie outside a disk of radius strictly larger than one. Consequently \(u_k=h/\mu+O(\rho^k)\) for some \(0<\rho<1\).

For \(t=kh+s\), a currently unfinished flight of type \(T=mh\) can have only the ages \(s+jh\) with \(0\le j<m\), and similarly for \(nh\). Formula (1), evaluated at these atoms of \(U\), therefore yields the announced law \(\nu_s\) and total-variation error \(O(\rho^k)\). Its mass is \(h(pm+qn)/\mu=1\). Its normalized mean is
\[
\frac h\mu\left[p\sum_{j=0}^{m-1}\left(1-\frac{s+jh}{mh}\right)+q\sum_{j=0}^{n-1}\left(1-\frac{s+jh}{nh}\right)\right]
=\frac12+\frac{h/2-s}{\mu}.
\]
This completes the arithmetic assertion.

**3. Incommensurate weak limit.** When \(b/a\) is irrational, no nonzero frequency \(\omega\) satisfies \(pe^{-i\omega a}+qe^{-i\omega b}=1\). Thus \(F\) is nonarithmetic in the renewal-theorem sense. The function \(B_g\) in (1) is compactly supported and directly Riemann integrable. The nonarithmetic key renewal theorem gives
\[
\lim_{t\to\infty}\mathbb E[g(X_t)]
=\frac1\mu\int_0^\infty B_g(u)\,du
=\frac1L\int_0^L g(x)\,dx.
\]
The limit is uniform for each continuous \(g\), proving weak convergence. For fixed finite \(t\), at most \(\lfloor t/\min(a,b)\rfloor\) flights can finish, hence there are only finitely many possible speed sequences and positions. The atomic probability \(P_t\) is mutually singular with the continuous uniform law, giving total variation distance one.

**4. An exact mean transform.** Apply (1) with \(g(x)=x/L\). The Laplace transform for \(\Re z>0\) is
\[
\mathcal Lm(z)=\frac{B(z)}{D(z)},\quad
B(z)=\frac1z-\frac{p(1-e^{-az})/a+q(1-e^{-bz})/b}{z^2},\quad
D(z)=1-pe^{-az}-qe^{-bz}.
\tag{2}
\]
The apparent singularity of \(B\) at zero is removable, with \(B(0)=\mu/2\), while \(D(z)=\mu z+O(z^2)\). Thus the steady-state pole at zero has residue \(1/2\), matching the weak-limit mean.

**5. High-frequency resonances.** Because \(b/a\) is irrational, continued fractions give arbitrarily large \(K\) and integer \(M\) such that \(\delta_K=2\pi(Kb/a-M)\to0\). Near \(z=2\pi iK/a\), put \(z=2\pi iK/a+w\). The equation \(D(z)=0\) becomes
\[
G(w,\delta)=1-pe^{-aw}-qe^{-bw-i\delta}=0.
\]
At \((w,\delta)=(0,0)\), \(G_w=\mu\ne0\), so the analytic implicit-function theorem provides a unique small root \(w(\delta)\). Implicit differentiation gives
\[
w'(0)=-\frac{iq}{\mu},\qquad
w''(0)=-\frac{pqa^2}{\mu^3},
\]
which proves the displayed quadratic root expansion. Since \(p,q>0\), its real part is negative for all sufficiently small nonzero \(\delta\), and approaches zero quadratically. The roots are simple because \(G_w\to\mu\). Furthermore, \(|\zeta_K|\to\infty\) and \(e^{-a\zeta_K},e^{-b\zeta_K}\to1\), so (2) gives
\[
B(\zeta_K)=\frac1{\zeta_K}+O(|\zeta_K|^{-2})\ne0.
\]
Thus every sufficiently high such root is a genuine, uncancelled pole of \(\mathcal Lm\).

If there existed \(\beta>0\) with \(m(t)-1/2=O(e^{-\beta t})\), its Laplace transform would be analytic on \(\Re z>-\beta\). On the right half-plane it equals \(B(z)/D(z)-1/(2z)\) by (2), and the identity theorem would then forbid any nonzero pole in that wider half-plane. The sequence \(\zeta_K\) contradicts this, proving the nonexponential claim for the **specified physical mean observable**, not merely for a generic renewal test function.

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic to check normalized finite-time laws and phase limits for 20 coprime duration/probability choices and four phases each. It also checks complex near-resonance roots using irrational duration ratio \(\sqrt2\), the quadratic displacement formula, pole simplicity, and noncancellation of the mean numerator. It passes 19,578 deterministic assertions with Python's standard library. These finite checks are not substitutes for the renewal theorem, analytic-continuation argument, or the implicit-function proof.

For the illustrative case \(L=1\), \(a=1\), \(b=2\), \(p=2/5\), \(q=3/5\), and phase \(s=1/4\), the limiting atoms and their masses are \(3/4\) with mass \(1/4\), \(7/8\) with mass \(3/8\), and \(3/8\) with mass \(3/8\). Their mean is \(21/32\), agreeing exactly with the sawtooth formula.

Reproduction: run `python checker.py` using Python 3.9 or later; no external packages, network access, or source data files are required.

## Relationship to prior work

Das, Majumdar, and Pal (2026) establish the renewal description for threshold-reset ballistic motion, derive uniform equilibrium for velocity-density families, and analyze the *single deterministic speed* limit with a periodic delta peak (their Sections II–III and VII, equations (12), (17), and (47)–(50)). These results are premises here. The present finding concerns the irrational-duration nonexponential mean-position theorem and its explicitly calculated uncancelled quadratic quasipole sequence. The rational phase formula is supplied only as a classical lattice-renewal comparison; no originality is claimed for individual rational-duration examples or for generic phase-locking. The original paper does not explicitly give the particular irrational mean-observable resonance coefficient or its no-exponential-decay implication.

The arithmetic and nonarithmetic key renewal theorems, the elementary renewal generating function, continued-fraction approximation, and the analytic implicit-function theorem are established tools, not proposed discoveries. Boyer's work on Diophantine conditions and Fourier–Laplace renewal spectra already explains why general renewal remainders can lack exponential bounds. The assessed contribution is the exact identification of this obstruction in the concrete two-speed threshold-reset *mean-position observable*, with an explicit quadratic resonance coefficient and direct proof of noncancellation. The arithmetic comparison is not the claimed novelty. Broader renewal theory may contain equivalent statements upon specialization; publication priority requires independent expert comparison.

## Limitations

The analysis is for exactly two positive flight durations, i.i.d. speed draws, immediate right-continuous resets, and a bounded spatial interval. The irrational result proves weak convergence but not a sharp subexponential rate; different irrational ratios can have different Diophantine approximation behavior. The pole expansion is only along small mismatch subsequences and does not describe all poles. No result is claimed for speed distributions with more than two atoms, Gaussian noise, finite resetting duration, or robustness to measurement error. The work has had only self-review; independent scientific audit has not been performed.

## References

1. R. Das, S. N. Majumdar and A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733v1 (first public submission 12 November 2026), https://arxiv.org/abs/2611.16733 ; full text https://arxiv.org/html/2611.16733.
2. J.-B. Boyer, *The speed of convergence in the renewal theorem*, arXiv:1506.07625 (2015), https://arxiv.org/abs/1506.07625 ; especially Sections 2 and 4 on weakly Diophantine measures and renewal spectra.
3. *Blackwell renewal theorem*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Blackwell_renewal_theorem (classical arithmetic/nonarithmetic renewal context).
