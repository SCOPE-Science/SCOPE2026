# Sharp exponential-to-quartic switching crossover in a majority-reset Rabi ensemble

## Finding

Consider an odd number \(N=2m+1\) of noninteracting qubits, with independent unitary evolution between *common* reset events under
\[
H_N=\sum_{j=1}^{N}(\Omega\sigma_x^{(j)}+\Delta\sigma_z^{(j)}),\qquad
\omega=\sqrt{\Omega^2+\Delta^2}>0.
\]
The event intervals are independent exponential random variables of rate \(\gamma>0\). At each event all spins are measured in the \(\sigma_z\) basis, and the full ensemble is reinitialized to the unanimously up or unanimously down state according to the strict measured majority. Starting in the all-up reset state, let \(T_N\) be the physical time of the *first* down-reset. Define
\[
 a=\frac{\Omega^2}{\omega^2},\quad P=\frac{\pi}{\omega},\quad
 B_N(q)=\sum_{k=m+1}^{N}\binom Nk q^k(1-q)^{N-k}.
\]
The exact per-event flip probability and mean first-switch time are
\[
 p_N=\frac{\gamma}{1-e^{-\gamma P}}\int_0^P e^{-\gamma t}
 B_N(a\sin^2(\omega t))\,dt,\qquad
 \mathbb E T_N=\frac1{\gamma p_N}.
\]

**Fixed subcritical detuning.** For fixed \(0<a<1/2\), put
\[
 I(a)=-\frac12\log(4a(1-a)),\qquad
 C(a)=\frac{2\gamma\sqrt a(1-a)}{\omega(1-2a)^{3/2}}
 \frac{e^{-\gamma P/2}}{1-e^{-\gamma P}}.
\]
As odd \(N\to\infty\),
\[
 \boxed{p_N\sim \frac{C(a)}{N}e^{-NI(a)},\qquad
 \mathbb ET_N\sim\frac{N}{\gamma C(a)}e^{NI(a)}.}
\]

**Critical finite-size window.** Fix \(\lambda\ge0\), \(\gamma>0\), and \(\omega>0\), and choose the coherent parameters for each odd \(N\) so that \(a_N=1/2-\lambda/\sqrt N\), with \(a_N>0\). Let \(\Phi\) denote the standard normal distribution function and put
\[
 F(\lambda)=\int_{-\infty}^{\infty}\Phi(-2\lambda-y^2)\,dy,\quad
 A(\lambda)=\frac{\gamma e^{-\gamma P/2}}{\omega(1-e^{-\gamma P})}F(\lambda).
\]
Then \(F(\lambda)>0\) and
\[
 \boxed{p_N\sim A(\lambda)N^{-1/4},\qquad
 \mathbb ET_N\sim\frac{N^{1/4}}{\gamma A(\lambda)}.}
\]
At the exact boundary \(\Omega=\Delta\),
\[
 F(0)=\frac{2^{1/4}\Gamma(3/4)}{\sqrt\pi}.
\]
The critical profile also satisfies \(F(\lambda)\sim e^{-2\lambda^2}/(4\lambda^{3/2})\) in the *subsequent* limit \(\lambda\to\infty\); this does not assert a uniform simultaneous limit.

**Switch-time universality.** Along either sequence above, the waiting time, not merely its mean, obeys
\[
 \boxed{\gamma p_N T_N\ \Longrightarrow\ \mathrm{Exp}(1),\qquad
 \frac{\mathrm{Var}(T_N)}{(\mathbb ET_N)^2}\longrightarrow1.}
\]
Thus the known exponentially long finite-size lifetime below the collective threshold changes to a polynomial quarter-power lifetime inside its natural critical window.

## Assumptions and scope

The spins are ideal, coherent, and noninteracting between resets; each reset is instantaneous, projective, and perfect. The exponential intervals are independent of preceding outcomes and spin states; \(\gamma\) is fixed and positive. The restriction to odd \(N\) removes the tie convention. The claim concerns the first majority-induced change of reset state, beginning immediately after a definite all-up reset, not an arbitrary initial nonequilibrium state or a mixing-time identity. For the fixed-detuning law \(0<\Omega<\Delta\) is fixed. For the critical-window law \(\Omega_N^2+\Delta_N^2=\omega^2\) and \(a_N=1/2-\lambda/\sqrt N\) are fixed for each \(N\). All asymptotics run through odd sizes.

## Proof

1. **Exact renewal reduction.** A single qubit initially up is measured down after free evolution of length \(t\) with probability \(q(t)=a\sin^2(\omega t)\). Since the qubits factorize, the down-majority probability is exactly \(B_N(q(t))\). Integrating against the exponential first-event duration gives \(p_N\). Since \(q(t)\) has period \(P\), partitioning the integral into periods yields the displayed finite-period identity. After any unsuccessful reset the same all-up state is restored, so cycles restart independently. If \(K\) counts cycles to the first successful flip, \(K\) is geometric with parameter \(p_N\). Although a cycle's duration and its flip outcome need not be independent, the durations are independent of the event of surviving *earlier* cycles. Summation or Wald's stopped-sum identity gives \(\mathbb ET_N=(\mathbb E\tau)/p_N=1/(\gamma p_N)\).

2. **Fixed-detuning sharp binomial tail.** For fixed \(q\in(0,1/2)\), Stirling's formula for the first successful count \(k=(N+1)/2\), followed by a geometric sum of consecutive mass ratios tending to \(q/(1-q)\), yields
\[
 B_N(q)\sim\sqrt{\frac{2}{\pi N}}\frac{\sqrt{q(1-q)}}{1-2q}
 [4q(1-q)]^{N/2}.
\]
The convergence is uniform for \(q\) in compact subintervals of \((0,1/2)\). The function \(q(t)\) has exactly one maximum \(a\) on \([0,P]\), at \(t=P/2\). With \(I(q)=-\tfrac12\log[4q(1-q)]\), a Taylor expansion there gives
\[
 I(q(t))=I(a)+\frac{(1-2a)\omega^2}{2(1-a)}(t-P/2)^2
 +O((t-P/2)^4).
\]
Away from that neighborhood, a binomial Chernoff bound gives a strictly greater exponential rate, so ordinary one-dimensional Laplace asymptotics apply to the uniform tail expression. The \(N^{-1/2}\) binomial factor times the \(N^{-1/2}\) saddle width gives \(N^{-1}\); simplification yields precisely \(C(a)\).

3. **Coalescing, quartic critical saddle.** Set \(a_N=1/2-\lambda/\sqrt N\) and \(t=P/2+y/(\omega N^{1/4})\). For each fixed real \(y\),
\[
 a_N\sin^2(\omega t)=\frac12-\frac{\lambda+y^2/2}{\sqrt N}+O(N^{-1}),
\]
so the binomial central-limit theorem, with odd \(N\), gives \(B_N(a_N\sin^2(\omega t))\to\Phi(-2\lambda-y^2)\). Hoeffding's inequality \(B_N(q)\le e^{-2N(1/2-q)^2}\) for \(q\le1/2\), together with the quadratic fall-off of \(\sin^2\) from its unique period maximum, supplies an integrable envelope in the rescaled coordinate proportional to \(e^{-c y^4}\). Outside a fixed neighborhood the integral is exponentially small. Dominated convergence in the exact finite-period identity proves the \(N^{-1/4}\) law and its coefficient. At \(\lambda=0\), Fubini's theorem for a standard normal variable \(Z\) gives \(F(0)=2\mathbb E\sqrt{Z_+}=2^{1/4}\Gamma(3/4)/\sqrt\pi\). The subsequent large-\(\lambda\) profile follows from Mills' ratio and a Gaussian saddle of width \(\lambda^{-1/2}\).

4. **Exponential first-switch limit.** Let \(\tau\sim\mathrm{Exp}(\gamma)\) be one cycle and \(J_N\) indicate its majority flip. Define \(U_N(s)=\mathbb E[e^{-s\tau}J_N]\). Independent renewal cycles imply the *exact* transform
\[
 \mathbb E[e^{-sT_N}]
 =\frac{U_N(s)}{s/(\gamma+s)+U_N(s)},\qquad s\ge0.
\]
The conditional distribution of \(\tau\) given \(J_N=1\) has a bounded expectation uniformly in \(N\): by periodicity it is a sum of a variable in \([0,P]\) and an independent geometric number of full periods with ratio \(e^{-\gamma P}\). Hence \(U_N(\theta\gamma p_N)=p_N(1+o(1))\) whenever \(p_N\to0\). Inserting \(s=\theta\gamma p_N\) gives the Laplace transform \(1/(1+\theta)\), \(\theta\ge0\), of the unit-mean exponential. The same conditional-cycle bound (including its second moment) in the exact second-moment renewal equation gives \(\mathbb ET_N^2/(\mathbb ET_N)^2\to2\), proving the variance ratio.

## Verification

`check.py` is a standalone finite numerical verifier (Python 3, NumPy, SciPy). It compares short-size exact binomial-integral probabilities against independently expanded finite Fourier–Laplace formulas; integrates fixed-detuning and critical-window probabilities for odd sizes up to \(N=2561\); checks the explicit gamma-function value at the boundary; and checks the exact renewal Laplace expression. It completed **37 assertions**. For example, with \(\omega=\sqrt5\), \(\gamma=0.7\), and fixed \(a=0.2\), it gives \(I(a)=0.22314355131420965\) and \(C(a)=0.4708631741573605\). With \(\lambda=0\), the critical coefficient is \(A(0)=0.25145077533127114\). These numerical checks corroborate but do not substitute for the analytical proof; no exhaustive numerical assertion about all \(N\) is made.

## Relationship to prior work

Magoni, Carollo, Perfetto and Lesanovsky establish the exact majority-measurement probability and a renewal transition integral for their Protocol II (arXiv:2202.12655, Supplemental Material, equations S3–S4). They also observe exponentially long finite-size equilibration on the subcritical side and use a Gaussian approximation for finite-size tails (equations S5–S11). Those underlying formulas and qualitative phenomenon are **prior work, not new claims here**. The current result identifies the sharp fixed-detuning large-deviation exponent and prefactor, the degenerate-saddle crossover \(a_N=1/2-\lambda/\sqrt N\) with its explicit quarter-power scaling function, and the first-switch waiting-time limit. In particular, a fixed-gap normal tail approximation does not establish the exact nonquadratic binomial rate \(I(a)\), while a fixed-gap large-deviation expansion is nonuniform at \(a=1/2\). Perfetto, Carollo, Magoni and Lesanovsky (arXiv:2106.13761) establish the general semi-Markov conditional-reset setting; that construction does not directly state these spin-specific critical switching asymptotics. Both the general renewal framework and standard binomial-tail/Laplace methods predate this calculation; the application of these methods to the exact crossover, not their invention, is claimed.

## Limitations

The theorem excludes even sizes, non-Poissonian resets, imperfect measurement, decoherence, interactions, and any claim about experimentally achieved system size. It provides neither a uniform error estimate when \(\lambda\) diverges with \(N\) nor an all-parameter global mixing-time theorem. First-switch times, transition counts and stationary-state convergence need not coincide. The original publication's exact integral makes the new asymptotics mathematically derivable, so priority must be assessed against any unlocated specialized analysis of that integral and related finite-size literature. No independent peer review or external validation is represented.

## References

- M. Magoni, F. Carollo, G. Perfetto, and I. Lesanovsky, “Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting,” first publicly available February 25, 2022; arXiv:2202.12655, especially Protocol II and Supplemental Material §II, equations S3–S11. https://arxiv.org/abs/2202.12655
- G. Perfetto, F. Carollo, M. Magoni, and I. Lesanovsky, “Designing non-equilibrium states of quantum matter through stochastic resetting,” first preprint June 25, 2021; arXiv:2106.13761, semi-Markov conditional-reset formulation. https://arxiv.org/abs/2106.13761
