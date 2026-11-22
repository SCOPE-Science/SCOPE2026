# A sharp single-qubit age-information ceiling for Bell-reset Ising dimers

## Finding

For a Bernoulli-reset two-spin transverse-field Ising system prepared at each reset in the Bell state \(|\Phi^+\rangle\), the single-spin Holevo information about the equilibrium reset age has an exact, globally sharp coupling-and-gate-optimized bound. At a fixed reset probability \(0<p<1\), its maximum over all strictly positive coupling strengths and transverse fields is

\[
B(p)=h_2\!\left(\frac{3-2p}{2(2-p)}\right)-\frac{1}{2-p},
\qquad h_2(z)=-z\log_2 z-(1-z)\log_2(1-z).
\]

Equality occurs **if and only if** the two positive Hamiltonian coefficients coincide and the coherent gate phase is an odd half-turn. A projective measurement of \(\sigma_x\) on a single spin exactly achieves the bound. The optimal bound decreases strictly with reset probability, giving the universal sharp supremum

\[
\sup_{0<p<1,\,J,\Omega,T>0}\chi
=h_2(3/4)-\tfrac12
=0.311278124459\ldots\ \text{bits},
\]

which is approached as \(p\downarrow0\) along the exactly tuned couplings but never attained at positive \(p\).

## Assumptions and scope

Fix any step duration \(T>0\), arbitrary strictly positive \(J,\Omega\), and independent Bernoulli reset probability \(p\in(0,1)\). In units with \(\hbar=1\), define

\[
H=-J\,\sigma_z\otimes\sigma_z+
\frac{\Omega}{2}(\sigma_x\otimes I+I\otimes\sigma_x),
\quad U=e^{-iHT},\quad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Each step resets the two-qubit system to \(|\Phi^+\rangle\) with probability \(p\) or applies \(U\) with probability \(1-p\). For the stationary reset age \(M\), \(\Pr(M=m)=p(1-p)^m\), \(m=0,1,\dots\). The single-qubit conditional density matrix is \(\rho_m=\operatorname{Tr}_2(U^m|\Phi^+\rangle\langle\Phi^+|U^{\dagger m})\). Entropy \(S\) is the von Neumann entropy in bits and \(\chi=S(\mathbb E\rho_M)-\mathbb E S(\rho_M)\) is the Holevo information of the classical reset-age ensemble. The theorem addresses the ideal finite-dimensional unitary circuit, not a noisy hardware implementation, other reset states, or an entire spin chain.

## Proof

**1. Exact reduced states.** Set \(q=1-p\), \(\phi=T\sqrt{J^2+\Omega^2}\), and \(c=2J\Omega/(J^2+\Omega^2)\). By strict positivity, \(0<c\le1\), with equality exactly at \(J=\Omega\). Direct diagonalization in the Bell-symmetric sector (equivalently, Eq. (25) of Murauer et al.) yields

\[
\rho_m=\frac{I-y_m\sigma_x}{2},\qquad y_m=c\sin^2(m\phi),\qquad 0\le y_m\le1.
\]

Write \(\mu=\sum_{m=0}^\infty p q^m y_m\) and \(f(y)=h_2((1+y)/2)\). The states commute, so

\[
\chi=f(\mu)-\sum_{m=0}^\infty p q^m f(y_m).
\]

**2. A sharp entropy chord.** The binary entropy is strictly concave on its open domain; since \(f(0)=1\) and \(f(1)=0\), the chord inequality is \(f(y)\ge1-y\) for every \(y\in[0,1]\), with strict inequality for \(0<y<1\). Consequently

\[
\chi\le g(\mu):=h_2((1+\mu)/2)-1+\mu.
\]

Equality in this inequality requires all positive-weight \(y_m\) to lie in \(\{0,1\}\).

**3. The largest attainable mean polarization.** The absolutely convergent geometric trigonometric series gives

\[
\frac{\mu}{c}=
\sum_{m\ge0}p q^m\sin^2(m\phi)
=\frac12\left[1-
\frac{p(1-q\cos(2\phi))}{1-2q\cos(2\phi)+q^2}\right].
\]

Let \(t=\cos(2\phi)\in[-1,1]\). The derivative of the subtracted fraction is

\[
\frac{d}{dt}\frac{p(1-qt)}{1-2qt+q^2}
=\frac{pq(1-q^2)}{(1-2qt+q^2)^2}>0.
\]

Thus the sum is uniquely maximized at \(t=-1\), i.e. \(\phi=\pi/2+k\pi\) with integer \(k\ge0\) (because \(\phi>0\)); at this phase it equals

\[
\sum_{m\ge0}p q^m\sin^2(m\phi)
=\sum_{j\ge0}p q^{2j+1}=\frac{q}{1+q}.
\]

It follows that \(0\le\mu\le\mu_p:=q/(1+q)=(1-p)/(2-p)<1/2\). On \([0,1/2]\),

\[
g'(u)=1+\tfrac12\log_2\left(\frac{1-u}{1+u}\right)
\ge 1-\tfrac12\log_2 3>0.
\]

Hence \(\chi\le g(\mu_p)=B(p)\).

**4. Sharpness and all equality cases.** Achieving the upper bound entails \(\mu=\mu_p\) because \(g\) is strictly increasing. Both nonnegative factors in \(\mu=c\sum w_m\sin^2(m\phi)\) must then be maximal: \(c=1\) and \(\cos(2\phi)=-1\). These are exactly

\[
J=\Omega=\frac{(2k+1)\pi}{2\sqrt2\,T},\qquad k\in\{0,1,2,\ldots\}.
\]

At these parameters \(y_m=0\) for even ages and \(y_m=1\) for odd ages. The entropy chord is therefore also saturated, establishing all, and only, the claimed maximizers. Since \(\rho_m\) all commute in the \(\sigma_x\) eigenbasis, a local \(\sigma_x\) measurement produces a classical information channel whose mutual information is exactly \(\chi\); no collective measurement is required.

**5. Reset-rate law and absolute supremum.** The function \(\mu_p=(1-p)/(2-p)\) is strictly decreasing in \(p\), while \(g\) is strictly increasing on \([0,1/2]\). Therefore \(B(p)\) strictly decreases from \(g(1/2)=h_2(3/4)-1/2\) as \(p\downarrow0\) to \(g(0)=0\) as \(p\uparrow1\). For all \(p>0\), \(\mu_p<1/2\), so the absolute ceiling is a nonattained supremum. This concludes the proof.

## Verification

The accompanying standalone `verify.py` reconstructs the four-dimensional Hamiltonian, exponentiates the unitary, propagates the two-qubit Bell state, and takes a partial trace before computing the age-averaged entropy difference. It separately computes the analytic two-eigenvalue expression and bound. Thirty direct-matrix comparisons at positive parameters, and twenty tuned equality cases, all passed; the largest analytic/matrix discrepancy was below \(8\times10^{-13}\) bits. At \(p=0.1\) the exact optimized value is approximately \(0.3051585985360449\) bits. The proof above, not this finite diagnostic, establishes the all-parameter theorem. To reproduce, execute `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work

Murauer, Tornow, Kulkarni, Barkai, Majumdar and Singh Roy [1] introduce and experimentally evaluate the same Bell-reset Ising system. They derive the conditional reduced-state matrix, the geometric resetting kernel, the trajectory-averaged and ensemble-averaged entropies, and identify their Jensen gap with the Holevo information of the reset age. Those objects and identities are **not** claimed as new here. Their general dimension bound and plots do not give the sharp coupling-optimized fixed-probability information ceiling, equality classification, optimal single-spin measurement, or global numerical upper envelope proved above.

Wald, Yao, Platini, Hooley and Carollo [2] develop a general discrete-time quantum-reset framework, stationary mixtures and spectral resonances. That broader stationary-state construction does not itself imply the specific sharp Holevo optimization under two continuously tunable Ising coefficients. The binary-entropy chord and trigonometric series are classical tools; the contribution is their sharp application and equality characterization in this constrained physical model.

## Limitations

The theorem concerns a Bell preparation, two spins, the ideal noiseless Hamiltonian and the reset-age Holevo observable for one spin. It does not bound the two-spin information, the information in a larger block, concurrence, CHSH nonlocality, or noisy-device accessible information. The mathematical supremum over reset probabilities is approached as \(p\downarrow0\) and is not attained by a stationary reset process with strictly positive \(p\). Related unindexed literature could affect claims of publication priority; no external independent review has yet been performed.

## References

[1] J. Murauer, S. Tornow, M. Kulkarni, E. Barkai, S. N. Majumdar, and M. Singh Roy, *Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits*, arXiv:2610.40638v1 (first public version 2026-10-29), https://arxiv.org/abs/2610.40638. Particularly Eqs. (10), (25)–(29), (46)–(48), and Appendix B.

[2] S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, Quantum **9**, 1742 (2025), https://doi.org/10.22331/q-2025-05-13-1742.
