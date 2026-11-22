# The equilibrium-age variance controls optimal renewal-clock phase-selection resonance

## Finding
Consider a stationary renewal reset clock with independent waiting times \(T_r=S/r\), where \(S>0\) almost surely, \(\mathbb E S=1\), and \(\mathbb E S^3<\infty\). At every reset, a weak periodic drive instantaneously selects the output branch \(B\operatorname{sgn}(\cos(\omega t))\), for \(B>0\), but this output is invisible for a fixed maturation interval \(\tau>0\). Subsequently it stays at that selected value until the next reset, while the drive phase itself is never reset. This is an exact renewal *step-response model*, not an assertion about the exact quartic-well trajectory.

Let \(G_S(r,\omega)\) be the amplitude of the first Fourier harmonic of the ensemble mean, and define \(H_S(r,\omega)=\pi G_S(r,\omega)/(4B)\). Write
\[
\sigma_S^2=\frac{\mathbb E S^3}{3}-\frac{(\mathbb E S^2)^2}{4}.
\]
Then \(\sigma_S^2\ge 1/12>0\). For each sufficiently small \(\omega>0\), global maximizers of \(H_S(\cdot,\omega)\) on \(r>0\) exist, and **every** such maximizer obeys
\[
r_*(\omega)\sim\left(\frac{\sigma_S^2}{\tau}\right)^{1/3}\omega^{2/3},
\qquad
\max_{r>0}H_S(r,\omega)
=1-\frac32(\sigma_S^2\tau^2)^{1/3}\omega^{2/3}+o(\omega^{2/3}).
\]
Among all *fixed* renewal waiting-time laws of unit mean and finite third moment, the asymptotic optimal reset-rate prefactor and the optimized amplitude-loss coefficient are uniquely minimized by deterministic intervals \(S=1\). For exponential intervals, \(\sigma_S^2=1\); for deterministic intervals, \(\sigma_S^2=1/12\), giving a sharp prefactor ratio \(12^{1/3}\). For Erlang intervals of integer shape \(k\ge1\) and mean one,
\[
\sigma_S^2=\frac{(k+1)(k+5)}{12k^2}.
\]
The result concerns varying \(r\) at fixed law of \(S\), not uniform optimization over clock laws that themselves depend on \(\omega\).

## Assumptions and scope
The renewal process is initialized in its equilibrium stationary age distribution, independently of the deterministic periodic forcing. Each waiting time equals \(S/r\) for an iid copy of a fixed positive random variable \(S\). The reset phase is the actual forcing phase at the reset event, and no reset changes the forcing clock. Maturation delay \(\tau>0\) is deterministic and does not depend on forcing phase. Between completion of maturation and the next reset the selected output is constant. Output before maturation is zero. All statements concern the first harmonic of the **ensemble-mean periodic response** at forcing frequency \(\omega\), not a pathwise signal-to-noise ratio or entropy production. A stationary phase randomization is included for deterministic intervals.

## Proof
Let \(A_r\) denote the stationary time since the last reset. The renewal occupation formula shows that \(V=r A_r\) has density
\[
f_V(v)=\Pr(S>v),\qquad v\ge0,
\]
since \(\int_0^\infty\Pr(S>v)\,dv=\mathbb E S=1\). The output at observation time \(t\) is \(B\operatorname{sgn}(\cos[\omega(t-A_r)])\mathbf1_{\{A_r\ge\tau\}}\). The first harmonic of the square wave has amplitude \(4B/\pi\), hence, exactly,
\[
H_S(r,\omega)=\left|\int_{r\tau}^\infty\Pr(S>v)e^{-i(\omega/r)v}\,dv\right|
=\left|\mathbb E[e^{-i(\omega/r)V}\mathbf1_{\{V\ge r\tau\}}]\right|.\tag{1}
\]
In particular, \(\mathbb E V=\mathbb E S^2/2\) and \(\mathbb E V^2=\mathbb E S^3/3\), giving \(\operatorname{Var}(V)=\sigma_S^2\). The density is positive on some interval adjacent to zero, so \(|\mathbb E e^{-i z V}|<1\) for all \(z\ne0\), and its characteristic function tends to zero as \(|z|\to\infty\).

Put \(d=r\tau\) and \(z=\omega/r\). Since \(\Pr(S>v)\to1\) as \(v\downarrow0\), the omitted short-age integral equals \(d+o(d)\). Finite \(\mathbb E V^2\) gives the characteristic expansion \(1-i(\mathbb E V)z-\tfrac12(\mathbb E V^2)z^2+o(z^2)\). Taking the modulus yields, jointly as \(d,z\to0\),
\[
H_S(r,\omega)=1-r\tau-\frac{\sigma_S^2\omega^2}{2r^2}
+o\!\left(r+\frac{\omega^2}{r^2}\right).\tag{2}
\]
The cross terms vanish at the stated order because the truncated integral has mass \(O(d)\) and phase variation at most \(O(d|z|)\).

For fixed \(\omega>0\), (1) is continuous in \(r\), tends to zero as \(r\downarrow0\) by the Riemann--Lebesgue lemma, and tends to zero as \(r\to\infty\) by \(\Pr(V\ge r\tau)\to0\). Thus the maximum is attained. Set \(\varepsilon=\omega^{2/3}\). The trial rate \(r=\varepsilon\) gives \(\max H_S\ge1-C\varepsilon\). Every maximizing rate therefore obeys \(\Pr(V<r\tau)\le C\varepsilon\) from \(H_S\le\Pr(V\ge r\tau)\), and the age density tends to one at zero; consequently \(r=O(\varepsilon)\). Using the triangle inequality in (1), \(|\mathbb E e^{-izV}|\ge H_S-\Pr(V<r\tau)\ge1-C'\varepsilon\). Nonlattice absolute continuity and decay of this characteristic function force \(z\to0\), and \(1-|\mathbb E e^{-izV}|\sim\sigma_S^2 z^2/2\) implies \(z^2=O(\varepsilon)\). Hence each maximizer satisfies \(c\varepsilon\le r\le C\varepsilon\) for some positive constants.

On this compactly rescaled interval, expansion (2) holds uniformly. Writing \(r=y\varepsilon\) turns the leading amplitude loss into
\[
\varepsilon\left(\tau y+\frac{\sigma_S^2}{2y^2}\right).
\]
This strictly convex function of \(y>0\) has the unique minimizer \(y=(\sigma_S^2/\tau)^{1/3}\) and minimum \(3(\sigma_S^2\tau^2)^{1/3}/2\). Compactness and uniform convergence prove the two asymptotics for **all** global maximizers.

Finally Cauchy--Schwarz and Jensen yield
\[
\mathbb E S^3\ge(\mathbb E S^2)^2,
\qquad\mathbb E S^2\ge1,
\]
so \(\sigma_S^2\ge(\mathbb E S^2)^2/12\ge1/12\); equality holds only if \(S=1\) almost surely. Gamma moment substitution proves the Erlang formula and the Poisson case.

## Verification
Run \(\texttt{python3 check_resonance.py}\) with Python, NumPy and SciPy installed. The checker evaluates exact finite-frequency harmonic transforms for Erlang clock orders \(1,2,3,5,12\) and the deterministic clock, optimizes over reset rate numerically at four driving frequencies, compares the slow-drive coefficients, and verifies the Erlang age-variance identities and the Poisson special case. The mathematical argument above, not numerical convergence, proves the universal claim.

## Relationship to prior work
Wang, Li, Zhu, Cherstvy, Metzler and Xu (arXiv:2611.01991, first publicly submitted 2026-11-01), *Weak-Signal Amplification through Stochastic Resetting*, establish a Poisson-reset resonance mechanism and a phase-selected step-response coarse-graining (especially main Eq. (11), Supplementary Eqs. (S28)--(S45)). Those statements supply the physical motivation and the Poisson \(\omega^{2/3}\) benchmark. They do **not** state the finite-third-moment arbitrary-renewal-clock theorem, its equilibrium-age-variance coefficient, its all-global-optimizers localization, or the sharp unique deterministic-clock bound.

Published research on gamma-distributed maturation latency under **Poisson** resetting changes the latency law, whereas the present statement changes the **inter-reset waiting-time law** and keeps maturation fixed. General renewal resetting theory supplies the stationary-age identity; general non-Markovian stochastic-resonance results concern different driven two-state transitions. Such ingredients are credited, not claimed new. The asserted extension is the full sharp stationary phase-selection optimization for general renewal clocks, conditional on no stronger unindexed equivalent result.

## Limitations
The step-response model is a deliberately idealized limit: this does not prove the same coefficients for exact nonlinear double-well trajectories or for phase-dependent maturation. The distribution of \(S\) is fixed as \(\omega\downarrow0\), positive with unit mean and finite third moment. Heavy-tailed clocks without the third moment may have a different optimal scaling. Only the leading slow-frequency optimization and its unique deterministic prefactor floor are proved; finite-frequency uniqueness of a maximizing rate and pointwise stochastic dominance between reset protocols are not asserted. Literature equivalence remains subject to wider human search.

## References
1. W. Wang, K. Li, J. Zhu, A. G. Cherstvy, R. Metzler, Y. Xu, *Weak-Signal Amplification through Stochastic Resetting*, arXiv:2611.01991v1 (2026-11-01), https://arxiv.org/abs/2611.01991 .
2. I. Goychuk and P. Hänggi, *Non-Markovian Stochastic Resonance*, arXiv:cond-mat/0303413 (2003), https://arxiv.org/abs/cond-mat/0303413 .
3. I. Goychuk, P. Hänggi, J. L. Vega and S. Miret-Artés, *Non-Markovian Stochastic Resonance: three state model of ion channel gating*, arXiv:physics/0601070 (2006), https://arxiv.org/abs/physics/0601070 .
4. A. S. Bodrova and I. M. Sokolov, *Resetting processes with noninstantaneous return*, Physical Review E 101, 052130 (2020), https://doi.org/10.1103/PhysRevE.101.052130 .
5. *Unique Poisson-reset resonance with gamma-distributed maturation latency*, published published-finding corpus record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unique-poisson-reset-resonance-with-gamma-distributed-maturation--44b415aa0d29 .
