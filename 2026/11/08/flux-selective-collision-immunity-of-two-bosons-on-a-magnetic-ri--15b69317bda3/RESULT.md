# Flux-selective collision immunity of two bosons on a magnetic ring

## Finding

For two identical noninteracting bosons on a magnetic cycle, strictly positive irreversible loss at **every double-occupation site** produces complete eventual capture at almost every magnetic flux, but a nonzero exactly protected subspace at a discrete set of fluxes. In particular, a quarter flux quantum creates protected bosonic states on **odd** rings, although zero flux does not.

Let \(n\ge3\), \(J\in\mathbb R\setminus\{0\}\), and let the total Peierls phase \(\Phi\in[0,2\pi)\). Put \(\omega=e^{2\pi i/n}\). On \(\mathcal H_1=\mathbb C^{\mathbb Z_n}\), let \(T|x\rangle=|x+1\rangle\) and
\[
h_\Phi=J\left(e^{i\Phi/n}T+e^{-i\Phi/n}T^\dagger\right).
\]
On \(\mathcal H_B=\operatorname{Sym}^2\mathcal H_1\), define \(H_\Phi=(h_\Phi\otimes I+I\otimes h_\Phi)|_{\mathcal H_B}\) and
\[
\Gamma=\sum_{x=0}^{n-1}\gamma_x|x,x\rangle\langle x,x|,\qquad \gamma_x>0,\qquad H_{\rm eff}=H_\Phi-i\Gamma/2.
\]
Here \(|x,x\rangle\) is normalized, and \(|x,y\rangle_+=(|x,y\rangle+|y,x\rangle)/\sqrt2\) for \(x\ne y\). The total collision-loss probability from a normalized density matrix \(\rho\) is \(\eta(\rho)=1-\lim_{t\to\infty}\operatorname{Tr}(e^{-itH_{\rm eff}}\rho e^{itH_{\rm eff}^\dagger})\).

Let \(U=T\otimes T\), \(S|x,y\rangle=|y,x\rangle\), and define, for \(p\in\mathbb Z_n\),
\[
Q_p=\frac1n\sum_{a=0}^{n-1}\omega^{pa}U^a,\qquad
|d_p\rangle=\frac1{\sqrt n}\sum_{x=0}^{n-1}\omega^{px}|x,x\rangle.
\]
When a resonance exists, its unique momentum is
\[
p_*\equiv\frac{\Phi}{\pi}-\frac n2\pmod n.
\]
The expression is an integer residue **only** at the fluxes below. The orthogonal projector onto the entire collision-dark *bosonic* subspace is
\[
\boxed{P_{\rm dark}=\begin{cases}
\displaystyle\frac{I+S}{2}Q_{p_*}-|d_{p_*}\rangle\langle d_{p_*}|,
&\cos((\Phi-\pi p_*)/n)=0,\\[5pt]
0,&\text{otherwise},
\end{cases}}
\]
where the first expression is understood as an operator on the ordered tensor product, restricted to \(\mathcal H_B\). The resonant fluxes and ranks are exactly
\[
\boxed{
\begin{array}{c|c|c}
\text{ring}&\Phi\pmod{2\pi}&\dim\operatorname{ran}P_{\rm dark}\\\hline
n\ \text{odd}&\pi/2,\ 3\pi/2&(n-1)/2\\
n\equiv0\pmod4&0&n/2\\
n\equiv0\pmod4&\pi&n/2-1\\
n\equiv2\pmod4&0&n/2-1\\
n\equiv2\pmod4&\pi&n/2
\end{array}}
\]
At every other flux the dark rank is zero. For every density matrix in the bosonic sector,
\[
\boxed{\eta(\rho)=1-\operatorname{Tr}(P_{\rm dark}\rho).}
\]
For a localized pair on distinct sites \(x\ne y\), its exact eventual survival probability is zero off resonance and, on resonance,
\[
\boxed{\langle x,y|_+P_{\rm dark}|x,y\rangle_+
=\frac{1+(-1)^{p_*}\mathbf1_{\{n\text{ even},\ y-x\equiv n/2\pmod n\}}}{n}.}
\]
A double-occupied initial state always has zero survival. These statements hold for *all* strictly positive, potentially unequal, loss rates, not just in a weak- or strong-loss limit.

## Assumptions and scope

The hopping is nearest-neighbor, uniform in magnitude, and periodic; the gauge-invariant sum of link phases is \(\Phi\). Both bosons have the same phase and hopping, with no coherent two-body interaction, dephasing, extra potentials, or missing collision detectors. The ring has at least three sites. The stated long-time loss is the no-jump norm deficit under \(H_{\rm eff}\), equivalently the integrated probability of an irreversible two-body-loss event from the two-particle sector. The finite-dimensional model assumes all rates \(\gamma_x>0\); their magnitudes need not agree. A physically distinct total flux is considered modulo \(2\pi\).

## Proof

**1. Identify exactly the indefinitely surviving states.** For any eigenpair \(H_{\rm eff}v=\lambda v\),
\[
\operatorname{Im}\lambda\,\|v\|^2=-\langle v,\Gamma v\rangle/2\le0.
\]
Equality forces \(\langle x,x|v\rangle=0\) for every \(x\), since every \(\gamma_x>0\). Conversely, any eigenvector of the Hermitian \(H_\Phi\) vanishing on the collision diagonal is an undamped eigenvector of \(H_{\rm eff}\). The span of these vectors reduces both \(H_\Phi\) and \(\Gamma\). The restriction of \(H_{\rm eff}\) to its orthogonal complement has no real eigenvalue; all its eigenvalues have strictly negative imaginary parts. Finite-dimensional Jordan normal form therefore gives decay to zero on that complement. Thus the asymptotic survival norm of every initial state is precisely its orthogonal projection onto this span. This also proves the density-matrix capture formula.

**2. Separate total momentum and exchange symmetry.** The normalized one-body plane waves
\[
|k\rangle=n^{-1/2}\sum_x\omega^{kx}|x\rangle,
\quad k\in\mathbb Z_n,
\]
are eigenvectors of \(h_\Phi\) with eigenvalues \(\epsilon_k=2J\cos((\Phi-2\pi k)/n)\). The free two-body eigenvectors are symmetrized unordered plane-wave pairs \(\{k,l\}\). At fixed total momentum \(p\equiv k+l\pmod n\), their energies satisfy
\[
E_{k,p-k}=4J\cos\left(\frac{\Phi-\pi p}{n}\right)\cos\left(\frac{\pi(2k-p)}n\right).
\]
Every such bosonic pair has a *nonzero* amplitude on the collision diagonal proportional to the same spatial Fourier mode \(\omega^{px}\). For a fixed energy, the diagonal Fourier modes of different total momenta are independent. Hence cancellation of the diagonal amplitudes is possible only among distinct unordered momentum pairs with the same \(p\) and energy.

**3. Identify all resonances, with no generic degeneracy loophole.** If \(\cos((\Phi-\pi p)/n)\ne0\), equality of two energies at the same \(p\) reduces to equality of two cosines. This forces \(k'=k\) or \(k'=p-k\pmod n\), which represents the *same* unordered bosonic pair. Its nonzero diagonal amplitude cannot cancel. Therefore no bosonic dark state exists in any nonresonant momentum sector. A resonant sector requires
\[
\cos((\Phi-\pi p)/n)=0\quad\Longleftrightarrow\quad
p\equiv\Phi/\pi-n/2\pmod n.
\]
For \(0\le\Phi<2\pi\), this has a solution precisely at \(\Phi=0,\pi\) when \(n\) is even, or at \(\Phi=\pi/2,3\pi/2\) when \(n\) is odd; at most one residue \(p\) qualifies. At resonance, **every** free two-particle plane wave with that total momentum has energy zero.

**4. Construct the complete projector and count its rank.** The operator \(Q_p\) is the orthogonal spectral projector of \(U\) onto eigenvalue \(\omega^{-p}\). The symmetric total-momentum sector is the range of \((I+S)Q_p/2\). Because every vector in it has free energy zero at resonance, the only obstruction to collision darkness is its one-dimensional diagonal image. The normalized vector \(|d_p\rangle\) lies in this sector, spans its collision-supported direction and is orthogonal to every collision-dark vector there. Subtracting \(|d_p\rangle\langle d_p|\) yields the stated orthogonal projector.

The involution \(k\mapsto p-k\) on the \(n\) ordered momenta has \(f\) fixed points satisfying \(2k\equiv p\pmod n\). The symmetric dimension is \((n+f)/2\), so the dark dimension is \((n+f)/2-1\). For odd \(n\), \(f=1\). For even \(n\), \(f=2\) if \(p\) is even and \(f=0\) otherwise. Substitution of \(p=n/2\) at zero flux and \(p=n/2+1\) at \(\pi\)-flux yields exactly the rank table.

**5. Compute localized capture and verify all boundaries.** For \(x\ne y\), the vector \(|x,y\rangle_+\) has zero overlap with \(|d_p\rangle\), and the diagonal of \(Q_p\) contributes \(1/n\). A second contribution occurs exactly when simultaneous translation exchanges the particles, i.e. if \(n\) is even and \(y-x\equiv n/2\pmod n\). That translation contributes \((-1)^p/n\). This proves the localized survival formula. For \(x=y\), every dark vector is orthogonal to \(|x,x\rangle\), so survival is zero. Absence of any resonant sector means \(P_{\rm dark}=0\), hence complete eventual capture of all bosonic initial states.

## Verification

The standalone `verify.py` (Python 3 with NumPy) constructs the *two-particle hopping and collision matrices* for all \(3\le n\le10\), at fluxes \(0,\pi/2,\pi,3\pi/2,\pi/3\): 40 cases. It tests Hermiticity, idempotence, commutation with free dynamics, complete annihilation of collision amplitudes, exchange symmetry, and all distinct-site localized-pair formulas. Independently, it diagonalizes the free two-boson matrix, groups degenerate eigenvalues and computes the nullities of their collision maps; it also counts real-axis eigenvalues of the genuinely lossy matrix with nonuniform strictly positive rates. Both independent counts agree with the derived dark dimension in all 40 cases. The program prints `PASS: 40 ring/flux cases; all matrix and capture checks passed` when run successfully. These computations are finite corroboration only: the proof for every \(n\) and every flux is in steps 1–5.

## Relationship to prior work

Krovi and Brun (2006) establish the general relation between quantum-walk detector-dark eigenstates and infinite hitting times, but not this simultaneous two-particle collision detector or its magnetic-flux arithmetic. Kepesidis and Hartmann (2012) study *one-particle* local loss at a single site in a Bose-Hubbard chain, including dark antisymmetric modes; neither magnetic-flux cycles nor two-body collision loss is their observable. Qin and collaborators (2014) develop two-particle quantum walks on one-dimensional periodic lattices with nearest-neighbor interactions, but without magnetic flux or simultaneous collision absorption. Polo, Naldesi, Minguzzi and Amico (2019) analyze the *full flux-dependent spectrum* of two interacting bosons on a ring and the persistent current for real on-site interactions. Their plane-wave dispersion and center-of-mass coupling are important antecedents, but the study does not evaluate a non-Hermitian two-body collision-loss projector, its rate-independent asymptotic capture law or the four flux-resonance classes above. These established Fourier, particle-exchange and loss-free-subspace principles are not asserted to be new.

An earlier exact zero-flux two-walker collision-loss analysis gives the special \(\Phi=0\) case. The present result is the *full flux classification*, including complete destruction of protected states at generic flux, **creation** of protected states at quarter flux on odd rings, and switching of the antipodal state between the integer and half-flux cases for even rings. Neither the zero-flux specialization nor its ring-parity conclusion covers those cases.

## Limitations

The discontinuity is for the strict infinite-time survival probability, not for survival at any fixed finite time. No uniform-in-flux convergence rate is claimed near the exceptional fluxes. The theorem excludes nonuniform hopping magnitudes, interactions, dephasing, missing collision detectors and finite-time conditional-jump statistics. The analytical inputs are standard Fourier diagonalization and the general dark-state mechanism. Historical originality cannot be inferred from an unsuccessful search alone; unindexed prior work on magnetic two-particle non-Hermitian transport remains a residual priority risk. The 2019 interacting two-boson Bethe-ansatz formalism is closely related, though its real-interaction observables do not directly determine the rate-independent irreversible-loss projector.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094, first public 10 June 2006. https://arxiv.org/abs/quant-ph/0606094
2. K. V. Kepesidis and M. J. Hartmann, *The Bose-Hubbard model with localized particle losses*, arXiv:1204.0981, first public 4 April 2012. https://arxiv.org/abs/1204.0981
3. X. Qin, Y. Ke, X. Guan, Z. Li, N. Andrei and C. Lee, *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349, first public 14 February 2014. https://arxiv.org/abs/1402.3349
4. J. Polo, P. Naldesi, A. Minguzzi and L. Amico, *Exact results for persistent currents of two bosons in a ring lattice*, arXiv:1911.07159, first public 17 November 2019. https://arxiv.org/abs/1911.07159
5. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003, first public 16 February 2010. https://arxiv.org/abs/1002.3003
