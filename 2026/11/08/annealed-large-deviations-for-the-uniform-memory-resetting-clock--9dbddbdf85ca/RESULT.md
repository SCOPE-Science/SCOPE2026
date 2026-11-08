# Annealed large deviations for the uniform-memory resetting clock

## Finding

Consider the *unwrapped operational clock* \(Q_t\) defined below. At every Poisson resetting event it is replaced by its value at a uniformly selected **past physical time**, and otherwise it increases at unit speed. For any reset rate \(r>0\), put \(z=rt\) and \(Y_z=rQ_{z/r}\). For each \(s<1\), its exact moment-generating function and its logarithmic asymptotic are
\[
\mathbb E e^{sY_z}={}_1F_1\!\left(-\frac{s}{1-s};1;-(1-s)z\right)
\sim\frac{[(1-s)z]^{s/(1-s)}}{\Gamma(1/(1-s))}\quad(z\to\infty).
\]
In particular, the **annealed** laws of \(Y_z/\log z\) obey a full large-deviation principle (LDP) with speed \(\log z\) and the good, explicit rate function
\[
I(y)=\begin{cases}(\sqrt y-1)^2,&y\ge0,\\+\infty,&y<0.\end{cases}
\]
Thus for every Borel set \(B\subset\mathbb R\), with \(B^\circ\) and \(\overline B\) denoting its interior and closure,
\[
-\inf_{y\in B^\circ} I(y)\le\liminf_{z\to\infty}\frac{\log\Pr(Y_z/\log z\in B)}{\log z}
\le\limsup_{z\to\infty}\frac{\log\Pr(Y_z/\log z\in B)}{\log z}
\le-\inf_{y\in\overline B}I(y).
\]
This includes both exceptionally short and exceptionally long effective evolution times. The same clock additionally has an exact mean, a sharp variance asymptotic, and a central-limit refinement:
\[
\mathbb EY_z=\gamma+\log z+E_1(z),\qquad
\operatorname{Var}(Y_z)=2\log z+2\gamma-2-\frac{\pi^2}{6}+o(1),
\]
\[
\frac{Y_z-\log z}{\sqrt{2\log z}}\ \Longrightarrow\ \mathcal N(0,1).
\]
Here \(\gamma\) is Euler's constant, \(E_1(z)=\int_z^\infty e^{-u}\,du/u\), and the statements involving \(\log z\) concern \(z\to\infty\). The result is independent of the Hamiltonian whose trajectory this clock parameterizes.

## Assumptions and scope

On a probability space supporting a rate-\(r\) Poisson clock, initialize \(Q_0=0\). Between event times, let \(Q_t\) increase at speed one. At each event at physical time \(t>0\), independently draw \(U\) uniformly on \([0,t]\), conditional on the complete pre-event history, and set \(Q_t=Q_{U}\). This recursive construction defines a unique càdlàg, nonnegative process satisfying \(0\le Q_t\le t\). At the selected past time use its post-reset/right-continuous value; since \(U\) is continuous, event-time ambiguity has probability zero.

The clock can be used for a quantum system with any fixed self-adjoint Hamiltonian \(H\): its realization is the unitary orbit at effective time \(Q_t\), \(e^{-iHQ_t}\rho_0 e^{iHQ_t}\). Even when that orbit has repetitions, \(Q_t\) is defined by the above unwrapped recursion, not inferred from the density matrix. The probability statements are **annealed**, i.e. averaged over both Poisson events and uniformly sampled past times, rather than conditioned on a fixed sequence of waiting times. No assertion is made for nonuniform memory kernels, non-Poisson reset clocks, or arbitrary independent resetting-to-initial-state protocols.

## Proof

**1. The exact moment generator.** Dimensionless time gives the same process with unit reset rate. For real \(s\), let \(F_s(z)=\mathbb E[e^{sY_z}]\). In an infinitesimal interval \(dz\), ordinary drift multiplies the exponential observable at rate \(s\), whereas a reset replaces its conditional expectation with the time average of previous expectations. Therefore, for \(z>0\),
\[
F_s'(z)=(s-1)F_s(z)+\frac1z\int_0^zF_s(u)\,du,\qquad F_s(0)=1.
\]
The process is bounded by \(z\), so differentiation and all finite-time exponential moments are legitimate. Multiplying by \(z\) and differentiating gives
\[
zF_s''(z)+[1+(1-s)z]F_s'(z)-sF_s(z)=0,
\quad F_s(0)=1,\quad F_s'(0)=s.
\]
For \(s\ne1\), set \(w=-(1-s)z\) and \(a=-s/(1-s)\). This is Kummer's equation \(wF_{ww}+(1-w)F_w-aF=0\). The regular solution with the stated initial values is exactly \({}_1F_1(a;1;w)\). At \(s=1\), the moment is still finite at each fixed \(z\), but the displayed parameterization by \(a\) is not used.

**2. Logarithmic cumulant limit.** For each fixed \(s<1\), the negative-real-argument Kummer asymptotic (with \(a=-s/(1-s)<1\)) is
\[
{}_1F_1(a;1;-x)=\frac{x^{-a}}{\Gamma(1-a)}[1+O_s(x^{-1})]
\quad(x\to\infty),
\]
including the terminating-polynomial cases by continuity. Taking \(x=(1-s)z\), and noting \(\Gamma(1-a)=\Gamma(1/(1-s))>0\), yields
\[
\Lambda(s):=\lim_{z\to\infty}\frac1{\log z}\log\mathbb E e^{sY_z}
=\frac{s}{1-s}\quad(s<1).
\]
For \(s>1\), the event that no reset has occurred up to physical time \(z/r\) has probability \(e^{-z}\) and forces \(Y_z=z\). Therefore \(\mathbb E e^{sY_z}\ge e^{(s-1)z}\), so \(\Lambda(s)=+\infty\). At \(s=1\), monotonicity of the moment-generating function in \(s\), because \(Y_z\ge0\), implies \(\liminf\log\mathbb E e^{Y_z}/\log z\ge\sup_{s<1}\Lambda(s)=+\infty\). Thus \(\Lambda(s)=+\infty\) for \(s\ge1\).

**3. Full annealed LDP.** The proper extended-real cumulant function \(\Lambda\) is lower semicontinuous, differentiable on \(( -\infty,1)\), contains zero in the interior of its effective domain, and is steep at the finite domain boundary because \(\Lambda'(s)=1/(1-s)^2\to\infty\) as \(s\uparrow1\). Its domain also provides exponential tightness: for any \(0<s<1\) and \(R>0\), the exponential Markov bound gives
\[
\limsup_{z\to\infty}\frac1{\log z}\log\Pr(Y_z>R\log z)
\le\Lambda(s)-sR\to-\infty\quad(R\to\infty).
\]
There is no negative tail because \(Y_z\ge0\). Consequently the full one-dimensional Gärtner–Ellis theorem applies. For \(y>0\), maximizing \(sy-s/(1-s)\) over \(s<1\) gives the unique solution \(s=1-y^{-1/2}\), and hence \(I(y)=(\sqrt y-1)^2\). The limit as \(y\downarrow0\) is \(I(0)=1\); for \(y<0\) the Legendre transform diverges. The finite level sets of \(I\) are closed and bounded. This proves the claimed full LDP, including the left endpoint, using the steep cumulant theorem and approximation from \(y>0\).

**4. Mean and Gaussian fluctuations.** Differentiating the scalar equation once with respect to \(s\) at \(s=0\), the mean \(m(z)=\mathbb EY_z\) solves \(zm''+(1+z)m'=1\), with \(m(0)=0\). Its unique regular derivative is \(m'(z)=(1-e^{-z})/z\), which integrates to \(m(z)=\gamma+\log z+E_1(z)\).

Kummer's asymptotic is uniform for complex \(s\) in a fixed sufficiently small neighborhood of zero; the exponentially small second asymptotic branch is harmless there. Hence, uniformly in this neighborhood,
\[
\log F_s(z)=\frac{s}{1-s}\log z+
\frac{s}{1-s}\log(1-s)-\log\Gamma\!\left(\frac1{1-s}\right)+O(z^{-1}).
\]
Expand at zero using \(\log\Gamma(1+u)=-\gamma u+\pi^2u^2/12+O(u^3)\). The coefficient of \(s^2\) in the last expression is \(\log z+\gamma-1-\pi^2/12+o(1)\); twice this is the variance displayed above. Finally substitute \(s=iu/\sqrt{2\log z}\) and subtract the centering \(s\log z\). The resulting logarithmic characteristic function tends to \(-u^2/2\), proving the central limit theorem by Lévy's continuity theorem.

## Verification

`CHECK.py` is a standalone Python standard-library checker. It compares exact rational power-series coefficients obtained from the renewal evolution equation with an independently formed Kummer/Pochhammer expansion, checks the mean identity by two quadratures, checks Legendre optimization over a deterministic grid, and simulates the defining random-clock recursion (including the bound \(0\le Q_t\le t\)). The finite tests support, but do not replace, the all-parameter derivation above. Run with `python3 CHECK.py`. The test is deterministic and uses an explicit random seed.

## Relationship to prior work

The exact energy-basis hypergeometric factor and the operational-time construction are in de Mauro, Kulkarni and Majumdar (2026), especially their Eq. (12) and Appendix B. Those parts are **not** claimed as new. Their long-time results treat coherence decay and typical quantum spreading, including the leading clock \(\log(rt)/r\), rather than the full annealed large-deviation tails for the clock.

Boci and Mailler (2023), Theorem 1.4, give a broad *quenched* large-deviation principle for monkey walks with reinforced relocation; their Remark 1.5 explicitly separates the annealed upper bound as not established by that theorem. The result here supplies a complete annealed LDP, with its exact rate, for the particular uniform-memory **Poisson** clock obtained from the quantum reset protocol. It does not generalize their quenched result to arbitrary kernels or random run lengths. Prior classical central-limit theory for monkey walks provides further context; the Gaussian refinement here is presented as a quantified companion, not as the principal priority claim. General large-deviation theory is used in a specialized application, not claimed as original.

## Limitations

This is a sharply specified exponential-run, uniform-memory case; the general annealed monkey-walk problem remains open beyond assumptions where independent methods already apply. Because the 2026 source provides the *exact* hypergeometric characteristic function, the new LDP is a derived, not independent-model, theorem; further indexing of specialization literature may change its priority. The theorem concerns the stochastic operational clock and its induced mixture of unitary evolutions, not a universal state-space LDP for every Hamiltonian or initial state. The Gaussian limit is a second-order statement at typical fluctuations; the LDP concerns fixed fractional departures on the \(\log z\) scale. No independent audit has been performed.

## References

1. G. de Mauro, M. Kulkarni, S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1, first submitted 2026-08-03, https://arxiv.org/abs/2608.02297 ; full text https://arxiv.org/html/2608.02297 .
2. E.-S. Boci, C. Mailler, *Large deviations principle for a stochastic process with random reinforced relocations*, arXiv:2105.02633v3, https://arxiv.org/abs/2105.02633 ; Theorem 1.4 and Remark 1.5.
3. NIST Digital Library of Mathematical Functions, §13.7 (confluent hypergeometric asymptotics), https://dlmf.nist.gov/13.7 .
4. J. M. Meylahn, S. Sabhapandit, H. Touchette, *Large deviations for Markov processes with resetting*, Phys. Rev. E 92, 062148 (2015), https://doi.org/10.1103/PhysRevE.92.062148 (distinguishable fixed-state-reset setting).
