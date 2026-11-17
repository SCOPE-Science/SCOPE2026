# Exact collision-loss dark projector for two quantum walkers on a cycle

## Finding

Let \(n\ge3\), let \(A_n\) be the adjacency matrix of the simple cycle \(C_n\), and let \(J\in\mathbb R\setminus\{0\}\). On the ordered two-particle Hilbert space \(\mathcal H=\mathbb C^{\mathbb Z_n}\otimes\mathbb C^{\mathbb Z_n}\), define
\[
H_0=J(A_n\otimes I+I\otimes A_n),\qquad
\Gamma=\sum_{x\in\mathbb Z_n}\gamma_x\,|x,x\rangle\langle x,x|,
\qquad\gamma_x>0.
\]
Write \(U(t)=\exp[-it(H_0-i\Gamma/2)]\), \(S|x,y\rangle=|y,x\rangle\), and \(T|x,y\rangle=|x+1,y+1\rangle\), with coordinates modulo \(n\). For even \(n\) put
\[
Q_{\pi}=\frac1n\sum_{a=0}^{n-1}(-1)^aT^a,
\qquad |d_{\pi}\rangle=\frac1{\sqrt n}\sum_{x=0}^{n-1}(-1)^x|x,x\rangle.
\]
Then the exact orthogonal projector onto all indefinitely surviving states is
\[
\boxed{
P_{\rm dark}=\frac{I-S}{2}+
\begin{cases}
0,&n\text{ odd},\\[3pt]
\dfrac{I+S}{2}Q_{\pi}-|d_{\pi}\rangle\langle d_{\pi}|,&n\text{ even}.
\end{cases}}
\]
For any initial density operator \(\rho\), the eventual integrated collision-loss probability is
\[
\boxed{\eta(\rho)=1-\operatorname{Tr}(P_{\rm dark}\rho).}
\]
The answer is independent of every strictly positive, potentially unequal, loss rate \(\gamma_x\). Its dark dimension is
\[
\operatorname{rank}P_{\rm dark}=
\begin{cases}
\dfrac{n(n-1)}2,&n\text{ odd},\\[4pt]
\dfrac{n(n-1)}2+\dfrac{n+f_n}{2}-1,&n\text{ even},
\end{cases}
\quad
f_n=\begin{cases}2,&n\equiv0\pmod4,\\0,&n\equiv2\pmod4.\end{cases}
\]
Thus every bosonic (swap-symmetric) initial state is eventually absorbed for odd \(n\), whereas even \(n\) supports \(n/2\) symmetric dark states if \(4\mid n\), or \(n/2-1\) if \(n\equiv2\pmod4\).

For two distinct locations \(x,y\), the normalized symmetric pair \(|x,y\rangle_+=(|x,y\rangle+|y,x\rangle)/\sqrt2\) has survival probability
\[
\boxed{\langle x,y|_+P_{\rm dark}|x,y\rangle_+=
\begin{cases}
0,&n\text{ odd},\\[3pt]
\dfrac{1+(-1)^{n/2}\mathbf1_{\{y-x\equiv n/2\pmod n\}}}{n},&n\text{ even}.
\end{cases}}
\]
For example, on the four-site ring a symmetric adjacent pair survives with probability \(1/4\), whereas a symmetric antipodal pair survives with probability \(1/2\). Antisymmetric pairs always survive, and states \(|x,x\rangle\) are eventually absorbed with probability one.

## Assumptions and scope

The graph \(C_n\) is the simple nearest-neighbor cycle with unit edges, \(n\ge3\), and hopping is identical and real for both particles, with \(J\ne0\). Distinguishable-particle coordinates are used; restriction to the symmetric or antisymmetric subspace respectively describes two bosons or two fermions. Each collision site has strictly positive two-body loss \(\gamma_x\); no assumption of equal loss rates is made. There are no other potentials, interactions, or loss sites. The loss probability means the decrease of the squared norm under the finite-dimensional non-Hermitian no-jump evolution, not an instantaneous meeting probability or a finite-time detection rate.

## Proof

**1. The general loss-free criterion.** For any eigenvector \(v\) of \(H_0-i\Gamma/2\) with eigenvalue \(\lambda\), taking the imaginary part of its inner product with \(v\) gives \(\operatorname{Im}\lambda\,\|v\|^2=-\langle v,\Gamma v\rangle/2\). Hence \(\operatorname{Im}\lambda\le0\), and equality forces \(\langle x,x|v\rangle=0\) for every \(x\). Conversely, every \(H_0\)-eigenvector orthogonal to all collision sites is a real-eigenvalue vector of the lossy operator. Their span is reducing for both \(H_0\) and \(\Gamma\); on its orthogonal complement no real-axis eigenvalue remains, so finite-dimensional dissipative evolution converges to zero there, including in the presence of Jordan blocks. The strong-limit survival norm is therefore exactly the squared norm of the orthogonal projection onto the span of these loss-free eigenvectors. This proves the density-operator formula once that projector is evaluated.

**2. Momentum and collision amplitude.** Put \(\omega=e^{2\pi i/n}\). The normalized two-particle Fourier modes \(|k,l\rangle=n^{-1}\sum_{x,y}\omega^{kx+ly}|x,y\rangle\) are eigenvectors of \(H_0\) with energy \(E_{k,l}=2J[\cos(2\pi k/n)+\cos(2\pi l/n)]\). With total momentum \(p\equiv k+l\pmod n\), their collision amplitudes are \(\langle x,x|k,p-k\rangle=n^{-1}\omega^{px}\). Since these Fourier functions of \(x\) are independent for different \(p\), a fixed-energy vector vanishes on the entire collision diagonal precisely when its coefficients sum to zero separately in every total-momentum sector.

**3. Nonresonant sectors.** At fixed \(p\), the dispersion is
\[
E_{k,p-k}=4J\cos(\pi p/n)\cos(2\pi k/n-\pi p/n).
\]
When \(\cos(\pi p/n)\ne0\), equal energies within a total-momentum sector have \(k'=k\) or \(k'=p-k\pmod n\); this follows from the complete solutions to equality of two cosines. The collision-annihilating combination in each distinct pair is the antisymmetric exchange combination \(|k,p-k\rangle-|p-k,k\rangle\). A fixed point \(2k\equiv p\pmod n\) has nonzero collision amplitude and contributes no dark state. Thus all nonresonant dark modes lie in the \(-1\) eigenspace of particle swap \(S\), which is itself automatically orthogonal to every diagonal site.

**4. The unique resonant sector.** The coefficient \(\cos(\pi p/n)\) vanishes exactly when \(n\) is even and \(p=n/2\). Every one of its \(n\) Fourier modes has energy zero. Consequently its whole space is \(\operatorname{ran}Q_\pi\), with \(Q_\pi=n^{-1}\sum_a(-1)^aT^a\). The collision map on this space has rank one: its normalized detected direction is \(|d_\pi\rangle\), and its orthogonal complement is dark. The antisymmetric portion was already counted in step 3, so the additional dark part is \((I+S)Q_\pi/2-|d_\pi\rangle\langle d_\pi|\). The two summands of the stated projector are orthogonal projections onto perpendicular invariant subspaces, giving the exact formula without double-counting.

**5. Dimension and local-pair consequences.** The full antisymmetric subspace has dimension \(n(n-1)/2\). In the resonant sector, \(S\) permutes the \(n\) momentum pairs \((k,n/2-k)\), with \(f_n\) fixed pairs satisfying \(2k\equiv n/2\pmod n\). This congruence has two solutions if \(4\mid n\) and none if \(n\equiv2\pmod4\). Therefore the symmetric resonant eigenspace has dimension \((n+f_n)/2\), from which the detected direction must be removed. For a normalized symmetric off-diagonal pair, only the even-\(n\) symmetric resonant projector contributes. Evaluating its two translation orbits gives the displayed value \([1+(-1)^{n/2}\mathbf1_{\{y-x\equiv n/2\}}]/n\). The diagonal vector term has zero overlap with any off-diagonal pair. For \(|x,x\rangle\), every dark vector has zero diagonal amplitude, and for antisymmetric inputs all loss is identically zero. These identities conclude the proof for all dimensions and all positive loss rates.

## Verification

The included standalone `verify.py` constructs the nearest-neighbor two-particle adjacency matrix and the integer matrix \(M=2nP_{\rm dark}\) without floating-point arithmetic. For every \(3\le n\le10\), it verifies symmetry, exact idempotence \(M^2=2nM\), commutation \([M,H_0]=0\), zero collision rows, trace-derived dimension, and the symmetric-pair survival formula for every pair of distinct locations. As an independent check, it constructs the full Krylov span of the collision-site basis under adjacency, over each of two prime fields, without using the proposed projector. The resulting accessible ranks agree with \(n^2-\operatorname{rank}P_{\rm dark}\): respectively \(6,8,15,19,28,32,45,51\) for \(n=3,4,\ldots,10\). Exact finite checks support but do not replace steps 1–5 of the all-\(n\) proof. Run `python3 verify.py` with Python 3 and no third-party packages.

## Relationship to prior work

Krovi and Brun (2006) prove general quantum-walk infinite-hitting-time mechanisms associated with eigenstates invisible to a detector. Their single-detector framework motivates the loss-free eigenspace criterion but does not give this two-particle, all-collision-site projector or its finite-ring parity classification. Štefaňák, Kiss, Jex, and Mohring (2007) study meeting probabilities for two discrete-time coined walkers on an infinite line, including particle statistics; their model and time-resolved observable do not imply the stated eventual irreversible loss projector. Qin et al. (2014) analyze two-particle continuous-time lattice walks with nearest-neighbor interaction and periodic boundaries, but their dynamical and bound-pair results do not specify simultaneous loss at every double-occupancy state or its exact all-state capture law. Kepesidis and Hartmann (2012) study *single-particle localized* loss in a Bose–Hubbard lattice, a different detector and geometry. In particular, established fermionic exclusion and standard Fourier diagonalization are not independently claimed as new; the claimed contribution is the complete finite-cycle loss projector, its loss-rate universality, and the bosonic even/odd and mod-four trapping laws.

## Limitations

The claim requires nonzero uniform nearest-neighbor hopping and strictly positive loss at **every** collision site. It does not address an interacting Hubbard Hamiltonian, one or more missing detectors, anisotropic hopping, dephasing, finite-time capture rates, or quantum-jump trajectories beyond the integrated loss probability. The underlying Fourier and exchange ingredients are classical; an earlier unindexed two-body observability or dissipative lattice result might already imply this precise projector and remains a literature-priority risk. The verification program checks finite sizes only; completeness at arbitrary size follows from the analytical proof, not from extrapolation.

## References

1. V. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094, first submitted 10 June 2006. https://arxiv.org/abs/quant-ph/0606094
2. M. Štefaňák, T. Kiss, I. Jex and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985, first submitted 14 May 2007. https://arxiv.org/abs/0705.1985
3. X. Qin, Y. Ke, X. Guan, Z. Li, N. Andrei and C. Lee, *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349, first submitted 14 February 2014. https://arxiv.org/abs/1402.3349
4. K. V. Kepesidis and M. J. Hartmann, *The Bose-Hubbard model with localized particle losses*, arXiv:1204.0981, first submitted 4 April 2012. https://arxiv.org/abs/1204.0981
