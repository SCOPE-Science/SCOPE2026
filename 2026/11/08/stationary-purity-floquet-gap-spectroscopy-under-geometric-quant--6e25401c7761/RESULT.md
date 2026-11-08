# Stationary-purity Floquet-gap spectroscopy under geometric quantum resetting

## Finding
Let a finite-dimensional unitary evolution be interrupted independently on each discrete step with reset probability \(p\in(0,1)\) to a fixed pure state. Write \(\rho_p\) for its ensemble stationary density matrix and \(\mathcal P(p)=\operatorname{Tr}(\rho_p^2)\) for its global purity. With the reset parameter \(z=p^2/(1-p)\), the following **exact spectral characterization and inverse statement** hold:

\[
\mathcal P(z)=B_0+\sum_{j=1}^{m}B_j\frac{z}{z+a_j},\qquad
1-\mathcal P(z)=\sum_{j=1}^{m}\frac{a_j B_j}{z+a_j}.
\]

Here \(a_j\in(0,4]\) are precisely the distinct nonzero squared chordal gaps \(2[1-\cos(\theta_i-\theta_k)]\) between occupied Floquet eigenphases, \(B_j>0\) are their total ordered-pair reset-state spectral weights, and \(B_0+\sum_j B_j=1\). Consequently, if \(m\ge1\), purity is strictly increasing and strictly concave as a function of \(z>0\), and its deficit is a finite positive Stieltjes transform. **Knowledge of \(m\) and exact global purity at any \(2m\) distinct reset probabilities reconstructs every \(a_j\) and \(B_j\) uniquely**, without state tomography.

This spectroscopy does **not** generally reconstruct the individual Floquet eigenphases: there are two inequivalent six-level diagonal unitaries, equipped with equal-weight pure reset vectors, whose purity curves are identical for every \(p\in(0,1)\). Thus the accessible invariant is the *weighted chordal-gap distribution*, not a labeled quasienergy spectrum.

## Assumptions and scope
Fix a complex Hilbert space \(\mathbb C^d\), \(d\ge1\), a unitary \(U\), and a normalized pure reset vector \(|\psi\rangle\). The ideal discrete protocol has independent Bernoulli resets of probability \(p\) at every step and is observed immediately after the step. With \(\rho_0=|\psi\rangle\langle\psi|\), its stationary ensemble is the absolutely convergent sum
\[
\rho_p=p\sum_{n=0}^{\infty}(1-p)^n U^n\rho_0U^{-n}.
\]
Take an orthonormal eigenbasis \(U|i\rangle=e^{\mathrm i\theta_i}|i\rangle\), define \(s_i=|\langle i|\psi\rangle|^2\ge0\), and retain only occupied indices with \(s_i>0\). For ordered pairs let
\[
a_{ik}=2[1-\cos(\theta_i-\theta_k)]\in[0,4].
\]
Combine equal values into \(B_a=\sum_{i,k:a_{ik}=a}s_is_k\). List distinct positive values as \(a_1,\ldots,a_m\); let \(B_0\) aggregate all zero-gap pairs. This definition is eigenbasis-independent even for degenerate eigenvalues, since each weight is the squared overlap with the corresponding eigenspaces. \(m\) is assumed known only for the finite-sample reconstruction. When \(m=0\), purity is identically one and there is no positive gap to reconstruct.

## Proof
**1. Renewal and spectral kernel.** In the given eigenbasis, absolute convergence of the geometric renewal sum yields
\[
(\rho_p)_{ik}=\langle i|\psi\rangle\langle\psi|k\rangle\frac{p}{1-(1-p)e^{\mathrm i(\theta_i-\theta_k)}}.
\]
Since \(\rho_p\) is Hermitian, \(\operatorname{Tr}\rho_p^2=\sum_{i,k}|(\rho_p)_{ik}|^2\), and therefore
\[
\mathcal P(p)=\sum_{i,k}s_is_k\frac{p^2}{p^2+2(1-p)[1-\cos(\theta_i-\theta_k)]}.
\]
Division by \(1-p\) gives the stated formula in \(z=p^2/(1-p)\). The sum of all ordered-pair weights is \((\sum_i s_i)^2=1\), giving the stated deficit representation and positive weights. This holds at exact degeneracies and repeated chordal gaps without a generic-spectrum assumption.

**2. Complete shape law.** For every integer \(n\ge1\), differentiation of the finite sum gives
\[
(-1)^{n-1}\mathcal P^{(n)}(z)
=n!\sum_{j=1}^{m}\frac{a_jB_j}{(z+a_j)^{n+1}}>0
\]
when \(m\ge1\). Hence \(\mathcal P'(z)>0\), \(\mathcal P''(z)<0\), \(\mathcal P(0+)=B_0\), and \(\mathcal P(+\infty)=1\). Because \(z(p)\) increases bijectively from zero to infinity, purity is strictly increasing in the physical reset probability; concavity is asserted in \(z\), not in \(p\).

**3. Exact finite-sample identification.** Define \(F(z)=1-\mathcal P(z)\). Its \(m\) distinct negative poles \(-a_j\) and nonzero positive residues \(a_jB_j\) give the reduced rational form \(F=N/D\) with monic \(D\) of degree \(m\), \(\deg N\le m-1\), and \(\gcd(N,D)=1\). For any distinct \(z_1,\ldots,z_{2m}>0\), let \(f_\ell=F(z_\ell)\); the coefficients are obtained from the **linear** conditions
\[
N(z_\ell)=f_\ell D(z_\ell),\quad 1\le\ell\le 2m,
\]
with \(D\) monic. If another pair of those degrees solved these conditions, the polynomial \(ND'-N'D\), of degree at most \(2m-1\), would vanish at \(2m\) distinct positive nodes, hence vanish identically. Both fractions would agree, and their reduced denominator of degree \(m\) would be the same monic \(D\), forcing identical numerator. Thus the square coefficient system has a unique solution. Factor \(D\) to obtain \(a_j\), then take residues \(c_j=\lim_{z\to-a_j}(z+a_j)F(z)=a_jB_j\) to obtain \(B_j=c_j/a_j\). No noise stability or unknown-\(m\) identification is asserted.

**4. Exact nonidentifiability of individual phases.** Consider integer sets
\[
A=\{0,1,4,10,12,17\},\qquad
B=\{0,1,8,11,13,17\}.
\]
Their multisets of positive differences agree exactly and contain each of \(1,2,\ldots,13,16,17\) once. Let \(\delta=\pi/18\), let \(U_A\) and \(U_B\) be diagonal six-level unitaries with eigenphases \(\delta A\) and \(\delta B\), respectively, and use \(|\psi\rangle=6^{-1/2}\sum_{i=1}^{6}|i\rangle\) for both. Their zero-gap weights agree; all 15 positive differences have the same multiplicity, so the formula in step 1 gives \(\mathcal P_A(p)=\mathcal P_B(p)\) for every \(p\in(0,1)\). Their phase spans are \(17\pi/18<\pi\), and their unique long complementary circle arc identifies the endpoints. A common phase rotation would require \(A=B\) after normalization, and a rotation plus reflection would require \(B=17-A\); both are false. Thus no phase rotation, reversal, or permutation identifies the two spectra. This is a *known homometric-set mechanism* transferred to the reset observable, not a claim that the integer sets themselves are newly discovered.

## Verification
The accompanying `verify.py` requires only Python 3's standard library. Running `python3 verify.py` checks 849 deterministic arithmetic/numerical assertions: 149 exact-rational values in a three-level example; stationary density-matrix purity computed independently from complex matrix entries; strict derivative signs; exact four-point rational coefficient and residue recovery; the six-point difference identity; and 99 independent numerical evaluations of the homometric purity equality. These finite computations corroborate explicit identities, while steps 1–4 above supply the universal proof.

For reproduction of the rational reconstruction, take \(U=\operatorname{diag}(1,\mathrm i,-1)\), with \(s=(1/2,1/3,1/6)\). Then \(m=2\), \((a_1,a_2)=(2,4)\), and
\[
1-\mathcal P(z)=\frac{8/9}{z+2}+\frac{2/3}{z+4}
=\frac{(14/9)z+44/9}{z^2+6z+8}.
\]
Purity at \(p=1/5,2/5,3/5,4/5\) yields the denominator and numerator exactly by the four linear equations. The residues recover \(B_2=4/9\) and \(B_4=1/6\).

## Relationship to prior work
Wald, Yao, Platini, Hooley, and Carollo (2024; published 2025) give the general geometric-reset stationary state and its quasienergy-resolvent structure, from which the forward purity identity can be derived; those stationary-state formulas are **not** claimed as new. Murauer et al. (October 29, 2026) analyze entropies, concurrence, and phase-matching diagnostics for resetting Floquet/Ising qubits, motivating a scalar global observable but not presenting a full purity-gap inverse theorem. Classical rational interpolation and homometric sets are established mathematical tools; their generic theorems and the classical six-point example are not claimed as new. The scope of the proposed contribution is the reset-dependent global-purity spectral measure, its exact finite-measurement recovery, and the explicit **spectral information boundary** within this physical protocol.

The earlier continuous-time reset resolvent treatment of Rose et al. (2018) concerns a related but distinct clock and does not by itself state the discrete-time purity inverse characterization. Its full text was not evaluated for a possible equivalent specialized inference; this is a residual priority risk.

## Limitations
This theorem assumes exact unitary evolution, a pure fixed reset vector, independent Bernoulli resetting, and exact infinite-time stationary ensemble purity. It does not apply directly to noisy gates, mixed reset states, or arbitrary nongeometric waiting times. In finite-precision experiments, rational interpolation can be ill-conditioned, especially near colliding quasienergy gaps; no statistical uncertainty or stability bound is proved. The number of distinct positive chordal gaps is assumed known in the finite-sample statement. The spectrum is recovered only up to its occupied weighted chordal-gap measure: signed gaps, phase labels, and individual quasienergies are generally not identifiable. Generic rational interpolation and the homometric-set example have existing mathematical antecedents; publication priority for their physical specialization remains subject to a comprehensive independent literature review.

## References
1. J. Murauer et al., *Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits*, arXiv:2610.40638v1, first submitted 2026-10-29. https://arxiv.org/html/2610.40638v1
2. S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1, first submitted 2024-10-15; *Quantum* **9**, 1742 (2025). https://arxiv.org/html/2410.11497v3
3. D. C. Rose, H. Touchette, I. Lesanovsky, J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, *Physical Review E* **98**, 022129 (2018). https://doi.org/10.1103/PhysRevE.98.022129
4. J. Rosenblatt and P. Seymour, *The structure of homometric sets*, *SIAM Journal on Algebraic and Discrete Methods* **3** (1982). https://doi.org/10.1137/0603035
