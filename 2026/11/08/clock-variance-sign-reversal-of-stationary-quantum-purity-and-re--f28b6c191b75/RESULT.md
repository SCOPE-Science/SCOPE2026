# Clock-variance sign reversal of stationary quantum purity and reset overlap

## Finding

Let a finite-dimensional closed quantum system evolve unitarily between complete, instantaneous resets to a fixed density matrix. Suppose successive reset intervals have the two-stage Coxian law \(T=E_a+B E_b\), where \(E_a\) and \(E_b\) are independent exponentials of rates \(a,b>0\), and \(B\) is an independent Bernoulli random variable with success probability \(q\in[0,1]\). Write \(\rho_*\) for the equilibrium-renewal stationary ensemble, \(P=\operatorname{tr}(\rho_*^2)\) for its purity, \(O=\operatorname{tr}(\rho_*\rho_0)\) for its overlap with the reset state, and \(c_T^2=\operatorname{Var}(T)/(\mathbb ET)^2\).

In any energy eigenbasis of the Hamiltonian, with energy gaps \(\omega_{jk}=E_j-E_k\) in units \(\hbar=1\), the exact discrepancy is

\[
\boxed{
P-O=\frac{ab}{2}(1-c_T^2)
\sum_{j,k}|(\rho_0)_{jk}|^2\,
\frac{\omega_{jk}^{2}}{(a^2+\omega_{jk}^{2})(b^2+\omega_{jk}^{2})}.
}
\]

Consequently, for every noncommuting reset state \([H,\rho_0]\ne0\), the sign of \(P-O\) is exactly the sign of \(1-c_T^2\), independently of the Hamiltonian spectrum and dimension. If \([H,\rho_0]=0\), the discrepancy vanishes. For pure \(\rho_0\), \(O\) is the squared Uhlmann–Jozsa fidelity with the reset pure state; for mixed \(\rho_0\), \(O\) is only the Hilbert–Schmidt overlap.

The entire two-stage phase classification is sharp. When \(a\le b\), every \(q>0\) gives \(P>O\) for noncommuting states. When \(a>b\), the unique interior crossover is

\[
\boxed{q_c=1-\frac ba: \quad 0<q<q_c\Rightarrow P<O,\quad q_c<q\le1\Rightarrow P>O.}
\]

The equality points are exactly \(q=0\), and additionally \(q=q_c\) when \(a>b\). At both equality points the entire waiting-time law, not only its coefficient of variation, is exponential.

For a pure, equal-energy-weight, two-level reset state, \(|P-O|\) at fixed \(a,b,q\) is largest over positive energy gaps at precisely \(|\omega|=\sqrt{ab}\), and its maximum is

\[
\boxed{\max_{\omega>0}|P-O|=\frac{a^2bq|b-a+aq|}{2(b+aq)^2(a+b)^2}.}
\]

At an equality point all gaps tie at zero discrepancy; the uniqueness assertion for this optimal gap applies only when the prefactor is nonzero.

## Assumptions and scope

The Hilbert space has finite dimension \(d\ge2\), the Hamiltonian \(H\) is time-independent and Hermitian, and \(\rho_0\) is an arbitrary density operator. Set \(\hbar=1\); \(a,b>0\) and \(q\in[0,1]\). All \(E_a,E_b,B\) variables are independent and each reset interval uses fresh independent variables. Between resets the state follows \(\rho(t)=e^{-iHt}\rho_0e^{iHt}\). The ensemble is observed in stationary equilibrium-renewal age, rather than immediately following a synchronized reset. The reset intervals have a smooth, nonlattice finite-mean distribution, so standard regenerative convergence also yields this stationary ensemble from the synchronized preparation. No Markovian decoherence is included between resets.

## Proof

**1. Stationary renewal transform.** The mean waiting time is \(\mu=1/a+q/b=(b+aq)/(ab)\). The Laplace transform of the waiting time is

\[
L_T(s)=\frac{a}{a+s}\left(1-q+q\frac{b}{b+s}\right).
\]

At stationarity the elapsed time \(A\) since the most recent reset has density \(\Pr(T>t)/\mu\), hence its Fourier–Laplace transform is

\[
z(\omega):=\mathbb E[e^{-i\omega A}]
=\frac{1-L_T(i\omega)}{i\omega\mu}
=\frac{ab(b+aq+i\omega)}{(b+aq)(a+i\omega)(b+i\omega)}.
\]

The value at zero is defined continuously as \(z(0)=1\). This formula remains valid when the two exponential rates coincide.

**2. Spectral identity.** In the energy eigenbasis, \((\rho_*)_{jk}=(\rho_0)_{jk}z(\omega_{jk})\). Since \(\rho_0\) is Hermitian and \(z(-\omega)=\overline{z(\omega)}\),

\[
P-O=\sum_{j,k}|(\rho_0)_{jk}|^2\bigl(|z(\omega_{jk})|^2-\operatorname{Re}z(\omega_{jk})\bigr).
\]

Direct multiplication of the rational transform gives the exact, sign-factored identity

\[
|z(\omega)|^2-\operatorname{Re}z(\omega)
=\frac{a^2bq(b-a+aq)}{(b+aq)^2}\,
\frac{\omega^2}{(a^2+\omega^2)(b^2+\omega^2)}.
\]

Independently, the moment calculation for \(T=E_a+B E_b\) gives

\[
c_T^2=\frac{a^{-2}+q(2-q)b^{-2}}{(a^{-1}+qb^{-1})^2},
\qquad \frac{ab}{2}(1-c_T^2)=\frac{a^2bq(b-a+aq)}{(b+aq)^2}.
\]

Combining proves the boxed formula. Every summand in the spectral kernel is nonnegative; the sum is strictly positive exactly when some nonzero-energy-gap coherence of \(\rho_0\) is present, equivalently \([H,\rho_0]\ne0\).

**3. Crossover and equality laws.** The signed prefactor is proportional to \(q(b-a+aq)\). For \(q>0\), its only possible zero is \(q_c=1-b/a\), admissible exactly when \(a>b\), proving the complete ordering. For \(q=0\), the interval law is \(\operatorname{Exp}(a)\). If \(a>b\) and \(q=1-b/a\), direct simplification of \(L_T(s)\) yields \(b/(b+s)\), so the entire interval law is \(\operatorname{Exp}(b)\). No other positive \(q\) makes the variance equal to the squared mean. Stationary purity equals reset overlap also at commuting states, irrespective of the clock.

**4. Sharp spectral witness.** For a pure qubit with equal weights on two eigenvectors, its two off-diagonal entries have squared modulus \(1/4\), so the spectral sum equals \(\omega^2/[2(a^2+\omega^2)(b^2+\omega^2)]\). Writing \(u=\omega^2>0\), the derivative of \(u/[(a^2+u)(b^2+u)]\) has the sign of \(a^2b^2-u^2\). The unique positive maximizer is \(u=ab\), at which the kernel equals \(1/(a+b)^2\). This proves the optimum and the equality-point exception.

## Verification

The included standalone program `verify.py` uses independent symbolic simplification of the age transform, spectral factorization, moment identity and optimum, as well as exact-rational two-level density-matrix tests. It independently integrates the equilibrium age survival function for randomly generated two-, three-, and five-level mixed states and compares the resulting state and purity difference with the theorem. Execute `python verify.py` after installing the declared `requirements.txt` dependencies. The analytical identities above, rather than the finite numerical tests, establish the infinite parameter and dimension quantifiers.

## Relationship to prior work

Sevilla and Valdés-Hernández (2022) established a renewal formulation for quantum states with arbitrary reset-time distributions and studied purity and fidelity in their general setting; in particular, their energy-basis formulas underlie the stationary transform used here. Kulkarni and Majumdar (2023) observed coincidence of steady-state purity and initial-state fidelity for their Poisson-reset spin model and explicitly noted that an explanation of the equality was of interest. The result here does not claim a new renewal framework or the Poisson case. It classifies the **opposite signs and exact crossover** for a naturally parameterized non-Poisson two-stage clock, for all finite-dimensional Hamiltonians and reset states, and identifies a sharp qubit energy-gap witness. Its formulas are algebraically derivable from prior general renewal expressions; publication priority of this specialized classification is not independently established.

## Limitations

No statement is made for arbitrary non-Coxian renewal laws, finite-time purity, time-dependent Hamiltonians, dissipative between-reset channels, or a generalized fidelity for mixed reset states. The two exponential representations at the crossover are distributional equivalences, not evidence of unique hidden internal switching. The optimal spectral-gap statement is a qubit witness, not a universal optimization over all possible dimensions. Independent expert audit and independent publication-priority verification have not been performed.

## References

1. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643v1 (first submitted 12 September 2022), https://arxiv.org/html/2209.05643v1 . See Sections 2, 3.1, and 3.3 for renewal-state, spectral, purity and fidelity formulas.
2. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485v2 (first submitted 14 July 2023), https://arxiv.org/html/2307.07485v2 . See Section III.2 for the Poisson purity–fidelity observation.
