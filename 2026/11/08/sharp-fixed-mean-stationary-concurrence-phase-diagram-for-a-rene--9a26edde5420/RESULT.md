# Sharp fixed-mean stationary concurrence phase diagram for a renewal-reset entangling pair

## Finding

Fix \(\Omega>0\) and \(\mu>0\). For every strictly positive, integrable, i.i.d. renewal interval \(T\) with \(\mathbb ET=\mu\), let \(\rho_*\) be the equilibrium-renewal ensemble-averaged two-qubit state described below. Its Wootters concurrence satisfies
\[
 C(\rho_*)=\frac{\mathbb E[1-\cos(\Omega T)]}{m},\qquad m=\Omega\mu.
\]
Let \(\xi\in(\pi/2,\pi)\) be the unique nonzero solution of \(\tan(\xi/2)=\xi\), and set \(c_*=(1-\cos\xi)/\xi=\sin\xi\). Then the exact sharp maximum *or supremum*, according to the endpoint, is
\[
 U(m)=\begin{cases}
 c_*,&0<m\le\xi,\\
 (1-\cos m)/m,&\xi\le m\le\pi,\\
 2/m,&m\ge\pi.
 \end{cases}
\]
Numerically \(\xi=2.33112237041442\ldots\) and \(c_*=0.724611353776708\ldots\). The infimum is always zero. Consequently the complete attainable set of concurrences is
\[
 \{C(\rho_*):\mathbb E T=\mu,\ T>0\}=
 \begin{cases}
 (0,U(m)),&0<m<\xi,\\
 (0,U(m)],&\xi\le m<2\pi,\\
 [0,U(m)],&m\ge2\pi.
 \end{cases}
\]
For \(0<m<\xi\), an optimizing two-point sequence uses a near-zero reset duration and a duration \(\xi/\Omega\), but no positive-duration clock attains the supremum. For \(\xi\le m\le\pi\), the unique maximizer is \(T=\mu\) almost surely. For \(m>\pi\), the maximizers are precisely those clocks supported on the positive odd half-periods \(\Omega T\in\{\pi,3\pi,5\pi,\ldots\}\) with mean \(m\). The minimum is attained if and only if \(m\ge2\pi\), precisely on positive full periods \(\Omega T\in\{2\pi,4\pi,6\pi,\ldots\}\) with mean \(m\).

## Assumptions and scope

Use the basis \(\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}\). Each reset exactly prepares \(|00\rangle\), and between resets the state evolves under the entangling interaction
\[
 H=\frac{\hbar\Omega}2\sigma_x\otimes\sigma_x,\qquad \Omega>0.
\]
The intervals \(T_1,T_2,\ldots\) are independent and identically distributed, satisfy \(T_j>0\) almost surely, and have finite mean \(\mu=\mathbb ET_j\). No density, higher moment, or nonlattice assumption is imposed. At an equilibrium observation epoch the age \(B\) has law \(\mathbb P(B\in da)=\mathbb P(T>a)\,da/\mu\) on \(a\ge0\). Define \(\rho_*\) as the expectation of the pure state at age \(B\). Such a stationary age mixture exists for every permitted law, including deterministic periods; convergence from an initially synchronized reset at a fixed deterministic observation time is **not** asserted for arithmetic or periodic renewal clocks. Concurrence is applied to \(\rho_*\), not averaged across pure trajectories.

## Proof

**1. Stationary reduction.** After elapsed age \(a\), the reset state becomes
\[
 |\psi(a)\rangle=\cos(\Omega a/2)|00\rangle-i\sin(\Omega a/2)|11\rangle.
\]
The state \(\rho_*=\mathbb E[|\psi(B)\rangle\langle\psi(B)|]\) has populations only in the \(|00\rangle,|11\rangle\) sector, with coherence \(\langle00|\rho_*|11\rangle=(i/2)\mathbb E\sin(\Omega B)\). The two-qubit spin-flip/Wootters formula reduces on this supported \(X\)-state to \(C(\rho_*)=2|\langle00|\rho_*|11\rangle|\). By the equilibrium-age formula and Fubini (absolute integrability follows from \(\mathbb ET<\infty\)),
\[
 \mathbb E\sin(\Omega B)=\frac1\mu\int_0^\infty\mathbb P(T>a)\sin(\Omega a)\,da
 =\frac1{\Omega\mu}\mathbb E[1-\cos(\Omega T)]\ge0.
\]
This proves the concurrence formula and avoids interchanging the concurrence of each trajectory with that of the mixed ensemble.

**2. Global upper concave envelope.** Put \(X=\Omega T>0\), \(\mathbb EX=m\), and \(f(x)=1-\cos x\). For \(x\in(0,\pi)\), the ratio \(f(x)/x\) increases from zero and has a single maximum \(c_*\) at \(\xi\), since its derivative has the sign of \(x\sin x-(1-\cos x)\), whose unique nonzero zero in this interval solves \(\tan(x/2)=x\). Indeed, \(x\mapsto\tan(x/2)-x\) first decreases, then strictly increases to infinity, with its turning point at \(x=\pi/2\). For \(x\ge\pi\), \(f(x)/x\le2/\pi<c_*\). Define
\[
 h(x)=\begin{cases}c_*x,&0\le x\le\xi,\\1-\cos x,&\xi\le x\le\pi,\\2,&x\ge\pi.\end{cases}
\]
Its derivatives match at \(\xi\) because \(f'(\xi)=\sin\xi=c_*\), and at \(\pi\) because \(f'(\pi)=0\); the middle segment has \(f''(x)=\cos x<0\). Thus \(h\) is concave. It majorizes \(f\): on the first segment by the maximal ratio, on the middle segment by equality, and on the last by \(f\le2\). Jensen now gives
\[
 C(\rho_*)=\frac{\mathbb E f(X)}m\le\frac{\mathbb E h(X)}m\le\frac{h(m)}m=U(m).
\]
The same argument shows that \(h\) is the least concave majorant, as its linear and constant faces are supported by the \(f\)-contact points described next.

**3. Upper-bound rigidity and attainability.** Below \(\xi\), equality between \(h\) and \(f\) in \([0,\xi]\) occurs only at zero and at \(\xi\). Since \(X>0\), equality at a mean \(m<\xi\) is impossible. Nevertheless, for any \(0<\varepsilon<m\), let \(X\) take values \(\varepsilon\) and \(\xi\), with probability \((\xi-m)/(\xi-\varepsilon)\) at \(\varepsilon\). These positive two-point laws have mean \(m\) and their concurrence increases to \(c_*\) as \(\varepsilon\downarrow0\). On \([\xi,\pi]\), strict concavity of the middle part of \(h\), together with its strict contact geometry across adjoining faces, forces the unique optimizer \(X=m\) almost surely (including endpoints). For \(m>\pi\), equality requires \(f(X)=2\) almost surely, equivalently \(X\in\{\pi,3\pi,5\pi,\ldots\}\); these laws exist with any mean \(m\ge\pi\) by mixing consecutive odd half-periods.

**4. Lower bound and full interval.** Since \(f\ge0\), one has \(C\ge0\). Equality holds exactly when \(X\) is supported on the zeros \(\{2\pi,4\pi,6\pi,\ldots\}\); as the zero value of \(X\) is excluded, the smallest possible mean for such a law is \(2\pi\). Conversely, for every \(m\ge2\pi\), a mixture of consecutive positive full periods attains any specified mean and gives \(C=0\). For \(m<2\pi\), mixing \(X=\varepsilon\) with \(X=2\pi\) to keep mean \(m\), then letting \(\varepsilon\downarrow0\), makes the concurrence tend to zero. Since convex mixtures of admissible probability laws with the same mean preserve that mean and make \(C\) affine, every strictly intermediate concurrence is attained. This completes the sharp range and all endpoint classifications.

## Verification

The standalone `checker.py` requires Python 3, NumPy and SciPy; run `python checker.py`. It checks the formula against the spin-flipped four-dimensional Wootters matrix, randomized discrete renewal laws, deterministic and two-point endpoint distributions, the exceptional nonattainment limit, the exponential-clock benchmark, and an independent finite-support linear program. It reports 1466 passing finite assertions. These finite tests support reproducibility but **do not replace** the analytical proof for arbitrary laws.

For exponential reset intervals of mean \(\mu\), the special-case concurrence is \(C_{\rm exp}(m)=m/(1+m^2)\), whose best value over \(m>0\) is \(1/2\). At \(m=1\), the deterministic value is \(1-\cos1=0.45969769\ldots\), whereas suitably randomized positive intervals approach \(0.72461135\ldots\). This is a comparison of equal-mean reset-time protocols, not of individually optimized Hamiltonians.

## Relationship to prior work

Kulkarni and Majumdar (arXiv:2307.07485, first public 2023-07-14) studied stationary two-qubit entanglement and concurrence under *Poissonian* reset, for a different ferromagnetically coupled-spin Hamiltonian; their optimization concerns interaction and reset rate in that family. Sevilla and Valdés-Hernández (arXiv:2209.05643) develop arbitrary-renewal stationary density operators and their coherence/purity/fidelity, supplying the appropriate age-mixture background but not a fixed-mean Wootters concurrence envelope. Eule and Metzger (arXiv:1510.07876) give a classical renewal approach to stochastic resetting, while Wald and collaborators (arXiv:2410.11497) analyze discrete-gate two-qubit correlations, mainly with constant step-reset probability, and non-Poissonian steady-state existence. Those results do not present the specific upper plateau, the sharp switching values \(\xi,\pi,2\pi\), or the equality cases here. The concave-envelope/Jensen machinery and Wootters formula are classical tools, not claimed as inventions. The theorem is a complete exact result for the specified entangling interaction, not a claim about all coupled-spin Hamiltonians.

## Limitations

This is an ensemble-state concurrence theorem for an ideal instantaneous product-state reset and fixed continuous-time \(\sigma_x\otimes\sigma_x\) coupling. The supremum below \(m=\xi\) requires arbitrarily short (but positive) interval components and may not be physically accessible with a minimum reset duration. The equilibrium mixture exists for deterministic clocks, but their synchronized-time trajectories remain periodic and need not converge to a time-independent ensemble. The result says nothing about noise, imperfect reset gates, a different entangling Hamiltonian, individual-trajectory concurrence, or the external priority of broader unindexed optimal-control results.

## References

1. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485 (first public 2023-07-14), https://arxiv.org/abs/2307.07485 .
2. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643 (2022), https://arxiv.org/abs/2209.05643 .
3. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876 (2015), https://arxiv.org/abs/1510.07876 .
4. S. Wald and collaborators, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (2024), https://arxiv.org/abs/2410.11497 .
5. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Phys. Rev. Lett. 80, 2245 (1998), https://doi.org/10.1103/PhysRevLett.80.2245 .
