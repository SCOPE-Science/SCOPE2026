# Universal single-onset entanglement under mixed-axis qubit noise and global resetting

## Finding

A pair of coherently coupled qubits with **different local error axes** has an exact, universal, single-onset stationary entanglement phase diagram under full-state Poisson resetting. For every choice of strictly positive coherent coupling \(J\), bit-flip noise rate \(a\), and phase-flip noise rate \(b\), there exists exactly one critical positive reset rate \(r_c\). The unconditional stationary state is separable at \(0<r\le r_c\) and entangled at every \(r>r_c\). Unlike the established same-axis two-bit-flip model, no geometric-mean noise ceiling can prevent sufficiently rapid resetting from creating entanglement in this mixed-axis model.

The critical rate is the **unique positive zero** of the explicitly specified degree-eight polynomial \(P\) below. Its uniqueness holds over the full continuum of positive parameters. At large reset rate the Wootters concurrence obeys the strict asymptotic law

\[
C(r)=\frac{2J}{r}+O(r^{-2})\qquad(r\to\infty).
\]

## Assumptions and scope

Work with \(\hbar=1\) in the basis \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle\). Let \(X\), \(Z\) be Pauli matrices, \(H=J(X\otimes X)\), and fix \(J,a,b,r>0\). The Markovian master equation is

\[
\dot\rho=-i[H,\rho]+a[(X\otimes I)\rho(X\otimes I)-\rho]+b[(I\otimes Z)\rho(I\otimes Z)-\rho]+r(\rho_0-\rho),\qquad \rho_0=\lvert00\rangle\langle00\rvert.
\]

The local channels are one bit-flip channel and one phase-flip channel, with precisely the stated convention for their rates. Every full-state reset replaces the pair by the *separable* state \(\rho_0\). Entanglement refers to the averaged stationary two-qubit density operator, not individual monitored trajectories.

## Proof

**1. Unique stationary density operator and explicit solution.** Write \(\mathcal L_0\) for the Hamiltonian plus two local noise generators. Since this is a trace-preserving completely positive semigroup, for any \(r>0\)

\[
\rho_r=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(\rho_0)\,dt
\]

is positive, normalized and stationary. The reset term contracts differences of two states at least as fast as \(e^{-rt}\) in trace norm, hence the stationary state is unique. Define strictly positive denominators

\[
E=r(r+2b)+4J^2,\qquad O=(r+2a)(r+2a+2b)+4J^2,
\]

and real quantities

\[
\begin{gathered}
p=\frac{r(r+2b)}E,\quad h=\frac{r(r+2a+2b)}O,\quad q=\frac{Jr}E,\quad k=\frac{Jr}O,\\
s_e=\frac{r+a}{r+2a},\quad s_o=\frac a{r+2a},\quad z=\frac{p+h}{2},\quad w=\frac{p-h}{2}.
\end{gathered}
\]

The invariant real six-dimensional \(X\)-state sector reduces, after sum-and-difference variables, to two independent forced damped pairs:

\[
\begin{array}{ll}
\dot p=r(1-p)-4Jq,&\dot q=Jp-(r+2b)q,\\
\dot h=r-(r+2a)h-4Jk,&\dot k=Jh-(r+2a+2b)k.
\end{array}
\]

The even-sector probability satisfies \(\dot s_e=r+a-(r+2a)s_e\). Their unique fixed point gives

\[
\rho_r=\begin{pmatrix}
(s_e+z)/2&0&0&i(q+k)/2\\
0&(s_o-w)/2&i(k-q)/2&0\\
0&-i(k-q)/2&(s_o+w)/2&0\\
-i(q+k)/2&0&0&(s_e-z)/2
\end{pmatrix}.
\]

**2. Exactly one possible entanglement branch.** For any physical two-qubit \(X\)-state the Wootters concurrence is

\[
C(r)=\max\left\{0,\;q+k-\sqrt{s_o^2-w^2},\;|q-k|-\sqrt{s_e^2-z^2}\right\}.
\]

Set \(G=(q-k)^2-(s_e^2-z^2)\). Exact common-denominator calculation gives

\[
G=-\frac{8J^2Q}{(r+2a)^2E^2O^2},
\]

where \(Q\) is the polynomial obtained by multiplying the displayed expression for \(-G\) by \((r+2a)^2E^2O^2/(8J^2)\). Every nonzero monomial coefficient of \(Q\), expanded jointly in \(r,a,b,J\), is a strictly positive integer. This finite *exact symbolic coefficient certificate*, independently reconstructed and verified by the included `checker.py`, proves \(Q>0\) for all positive parameters; thus the second entanglement branch is strictly negative. The positivity statement is not inferred from numerical samples.

**3. The sharp polynomial and its one-crossing proof.** Set \(F=(q+k)^2-(s_o^2-w^2)\). Direct elimination gives

\[
F=\frac{4J^2P(r)}{(r+2a)^2E^2O^2},\qquad P(r)=\sum_{j=0}^8P_jr^j.
\]

The coefficients, writing \(t=J^2\), are

\[
\begin{aligned}
P_0={}&-64a^2t(a^2+ab+t)^2,\\
P_1={}&-64a^2(a+b)(ab+2t)(a^2+ab+t),\\
P_2={}&-16a^2(a^4+12a^3b+17a^2b^2+5a^2t+6ab^3+14abt+6b^2t),\\
P_3={}&-16a(2a^4+12a^3b+11a^2b^2+2ab^3-(3a^2+2ab)t-4t^2),\\
P_4={}&-4(3a^4+10a^3b+a^2b^2-(23a^2+20ab)t-4t^2),\\
P_5={}&4(5a^3+12a^2b+6ab^2+12at+4bt),\\
P_6={}&2(11a^2+14ab+2b^2+4t),\\
P_7={}&4(2a+b),\qquad P_8=1.
\end{aligned}
\]

Thus \(P_0,P_1,P_2<0\) and \(P_5,P_6,P_7,P_8>0\). The potentially ambiguous middle coefficients cannot introduce further sign changes. Indeed let \(B_3=-P_3/(16a)\) and \(B_4=-P_4/4\). For \(0<t\le a^2/20\), the polynomial \(B_3\) is strictly positive (it decreases with \(t\), and its evaluation at \(a^2/20\) has positive coefficients). If \(P_3\ge0\), therefore \(t>a^2/20\), where

\[
B_4-B_3=a^4-2a^3b-10a^2b^2-2ab^3-(20a^2+18ab)t<0.
\]

Consequently \(P_3\ge0\) forces \(P_4>0\). In either case the descending coefficient list of \(P\), after discarding any zeros, has **exactly one sign change**. Descartes' rule gives at most one positive zero. Since \(P(0)=P_0<0\) and \(P(r)\sim r^8>0\), continuity gives one positive zero \(r_c\), with \(P<0\) below and \(P>0\) above it. The first concurrence branch has exactly the sign of \(F\) because \(q+k+\sqrt{s_o^2-w^2}>0\), proving the complete classification.

**4. Strong-reset coefficient.** Direct expansion of the exact stationary formulas yields \(q+k=2J/r+O(r^{-2})\) and \(\sqrt{s_o^2-w^2}=O(r^{-2})\). The inactive branch remains negative. Therefore \(C(r)=2J/r+O(r^{-2})\), strictly positive at every sufficiently large finite rate for **arbitrarily large fixed positive** \(a,b\). The asymptotic is not uniform when the noise parameters grow together with \(r\).

## Verification

`checker.py` uses exact SymPy simplification and monomial coefficient checks of both \(P\) and \(Q\), including the exceptional middle-coefficient implication, and independently builds and solves the full complex \(16\times16\) Lindblad stationary linear system. Direct Wootters spin-flip eigenvalue concurrence is compared with the \(X\)-state formula. Its reproducible command is `python checker.py`, with NumPy and SymPy installed. It completed **880 numerical assertions** in addition to the symbolic identities and exact coefficient certificate. The finite random cases corroborate the derivation; the all-parameter theorem follows from the displayed identities, positivity certificate and Descartes argument, not from finite sampling.

## Relationship to prior work

The 2023 quantum-resetting treatment of Kulkarni and Majumdar establishes entanglement in an **isolated** coherently evolving two-spin pair and the stationary renewal resolvent. Rose, Touchette, Lesanovsky and Garrahan (2018) give the general resolvent and spectral resetting framework; neither generic resolvent is newly claimed. Hartmann, Dür and Briegel (2007) study **local per-qubit** reset generators in noisy interacting spin systems and already establish qualitative reset-stabilized steady-state entanglement. These antecedents do not provide the present specific full-joint-reset mixed-axis criterion.

The published *A sharp geometric-mean noise threshold for entanglement under global quantum resetting* treats **two bit-flip channels**, both commuting with \(X\otimes X\), and proves the contrasting condition \(J^2>ab\). That result does not imply the present universal positive onset: replacing the second bit flip by phase-flip noise changes the generator and removes the noise-product obstruction. The published *Exact reset-rate reciprocity and thermal entanglement boundary for a dephased qubit pair* treats a **pair-converting-only** Hamiltonian with two dephasing channels; its odd-parity populations are frozen by the dynamics, unlike the bit-flip-generated spectators here. Its finite reciprocal reset window cannot imply the present one-threshold eighth-degree sign law. These precise model differences are necessary; neither titles nor the use of the same concurrence formula are evidence of uniqueness.

## Limitations

The classification concerns exactly the specified two-qubit, one-flip/one-phase Markovian generator and **joint** reset to \(\lvert00\rangle\); it does not establish a many-body extension, thermal-bath detailed balance, non-Poisson resetting, universal optimal concurrence rate, or robustness under extra Hamiltonian fields. Arbitrarily large noise means *each fixed pair of finite rates*, not a uniform bound on the critical reset rate. The proof and symbolic sign certificate have not received independent scientific or publication-priority assessment. General channel-theoretic work not identified in the sources remains a possible implicit-coverage risk.

## References

1. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485 (first posted 2023-07-14), https://arxiv.org/html/2307.07485v2.
2. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/html/1806.01298v2.
3. L. Hartmann, W. Dür and H.-J. Briegel, *Entanglement and its dynamics in open, dissipative systems*, arXiv:quant-ph/0703138 (2007), https://arxiv.org/html/quant-ph/0703138v1.
4. *A sharp geometric-mean noise threshold for entanglement under global quantum resetting* (published result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-geometric-mean-noise-threshold-for-entanglement-under-gl--25a4a404999e.
5. *Exact reset-rate reciprocity and thermal entanglement boundary for a dephased qubit pair* (published result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-reset-rate-reciprocity-and-thermal-entanglement-boundary-f--1e0867d1d987.
6. W. K. Wootters, *Entanglement of formation of an arbitrary state of two qubits* (1998), arXiv:quant-ph/9709029, https://arxiv.org/abs/quant-ph/9709029.
