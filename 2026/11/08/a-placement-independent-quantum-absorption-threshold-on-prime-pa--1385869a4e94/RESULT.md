# A placement-independent quantum absorption threshold on prime Paley networks

## Finding

Let \(p\ge5\) be a prime with \(p\equiv1\pmod4\), and let \(P(p)\) be its undirected Paley graph. A coherent excitation moves with the graph adjacency Hamiltonian, and any nonempty chosen set of \(t\) vertices acts as irreversible absorbers with independent arbitrary positive rates. Write \(m=(p-1)/2\).

**Theorem.** For *every* absorbing set \(T\subseteq\mathbb Z/p\mathbb Z\) with \(1\le t=|T|\le p\), the loss-free spectral subspace has exact dimension

\[
\dim\mathcal D_T=2\max\{m-t,0\}.
\]

Thus the network absorbs every initial one-excitation state eventually exactly when \(t\ge m\), independently of which sites are chosen and of their strictly positive loss rates. If \(t<m\), every untrapped site has a strictly positive nondecaying component. For uniformly random untrapped initial sites (provided \(t<p\)), the exact mean asymptotic absorption efficiency is

\[
\overline\eta_T=\begin{cases}(t+1)/(p-t),&1\le t<m,\\1,&m\le t<p.\end{cases}
\]

The order-nine (nonprime) Paley graph demonstrates the limitation: four absorbers can either leave a dark mode or eliminate all dark modes, depending on placement.

## Assumptions and scope

The vertices of \(P(p)\) are the residue classes \(x\in\mathbb Z/p\mathbb Z\); two distinct vertices are adjacent exactly when their difference is a nonzero quadratic residue. The standard orthonormal position states are \(|x\rangle\) in \(\mathbb C^p\). With \(A\) the real symmetric adjacency matrix, the unnormalized surviving wavefunction obeys

\[
 i\,\frac{d}{d\tau}\psi(\tau)=H_{\mathrm{eff}}\psi(\tau),\quad H_{\mathrm{eff}}=A-i\Gamma_T,\quad \Gamma_T=\sum_{x\in T}\gamma_x|x\rangle\langle x|,\ \gamma_x>0.
\]

For unit-norm initial \(\psi_0\), eventual absorption is \(\eta(\psi_0)=1-\lim_{\tau\to\infty}\|e^{-iH_{\mathrm{eff}}\tau}\psi_0\|^2\). Every claimed limit exists. The physically equivalent constant-degree Laplacian hopping Hamiltonian differs from \(-A\) by a scalar and a sign, which do not change the dark subspace or asymptotic efficiency. The theorem concerns coherent one-particle dynamics without disorder, dephasing, or time-dependent sinks; it says nothing about mean capture time.

## Proof

**1. Three distinct spectral sectors.** Let \(\zeta=e^{2\pi i/p}\), and let \(\phi_j(x)=p^{-1/2}\zeta^{jx}\) for \(j\in\mathbb Z/p\mathbb Z\). The quadratic Gauss sum identity gives the eigenvalues of the adjacency matrix:

\[
A\phi_0=m\phi_0,\qquad A\phi_j=\frac{-1+\chi(j)\sqrt p}{2}\,\phi_j\quad(j\ne0),
\]

where \(\chi\) is the Legendre symbol. Therefore there are three mutually orthogonal eigenspaces: a one-dimensional constant sector and two sectors \(E_+\), \(E_-\), each of dimension \(m\), respectively indexed by quadratic residues and nonresidues in Fourier space.

**2. Dark states are precisely node-vanishing eigenvectors.** A vector is permanently loss-free exactly when it belongs to an eigenspace of \(A\) and vanishes at every absorbing site. Indeed, if \(H_{\mathrm{eff}}v=\lambda v\), then \(\operatorname{Im}\lambda\|v\|^2=-\langle v,\Gamma_Tv\rangle\); a real eigenvalue forces \(v(x)=0\) for all \(x\in T\), and then \(Av=\lambda v\). Conversely such a vector evolves only by a phase. Their orthogonal sum \(\mathcal D_T\) reduces both \(A\) and \(\Gamma_T\). On its orthogonal complement all effective-Hamiltonian eigenvalues have strictly negative imaginary parts, so finite-dimensional Jordan theory makes the surviving norm tend to zero there. Consequently

\[
\lim_{\tau\to\infty}\|e^{-iH_{\mathrm{eff}}\tau}\psi_0\|^2=\|P_{\mathcal D_T}\psi_0\|^2.
\]

**3. Every trap restriction has maximum rank.** For an arbitrary spectral frequency set \(J\subseteq\mathbb Z/p\mathbb Z\) of size \(r\), the restriction map from its Fourier span to the coordinates in \(T\) has matrix \((\zeta^{xj})_{x\in T,j\in J}\), up to a nonzero scalar. Chebotarev's nonvanishing Fourier-minors theorem (Tao, Lemma 1.3) says every square submatrix of the prime-order Fourier matrix is nonsingular. Hence its rectangular restriction has rank \(\min\{t,r\}\): choose a square minor with that size. The constant sector has zero kernel because \(T\ne\varnothing\). Each of \(E_+\) and \(E_-\) has vanishing-on-\(T\) kernel of dimension \(m-\min\{t,m\}\). Their direct sum has dimension \(2\max\{m-t,0\}\), proving the sharp all-placement threshold. Since \(\Gamma_T\) is strictly positive on the chosen coordinates, its numerical values do not affect this argument.

**4. Every untrapped site sees a dark mode below threshold.** Fix \(t<m\) and \(v\notin T\). Since the restriction matrix of either \(m\)-dimensional Fourier eigenspace to \(T\cup\{v\}\) has rank \(t+1\), the functional evaluating at \(v\) is nonzero on its kernel of evaluation at \(T\). Some dark vector is therefore nonzero at \(v\). Thus \(\|P_{\mathcal D_T}|v\rangle\|^2>0\), and absorption from \(|v\rangle\) is strictly less than one.

**5. Uniform-source efficiency.** All dark vectors vanish on \(T\), so

\[
\sum_{v\notin T}\|P_{\mathcal D_T}|v\rangle\|^2=\operatorname{tr}P_{\mathcal D_T}=\dim\mathcal D_T.
\]

Averaging the limiting absorbed probability over the \(p-t\) remaining sites gives \(1-2(m-t)/(p-t)=(t+1)/(p-t)\) for \(t<m\), and one for \(t\ge m\).

**6. Sharp prime-order boundary.** The Paley graph over \(\mathbb F_9=\mathbb F_3[i]\) with \(i^2=-1\) is isomorphic to the \(3\times3\) rook graph, because the nonzero squares are \(\{\pm1,\pm i\}\). Write its vertices as \((a,b)\in\{0,1,2\}^2\). For the four traps in the upper-left \(2\times2\) block, the nonzero vector \(f(a,b)=\alpha_a+\beta_b\), with \(\alpha=(1,1,-2)\) and \(\beta=(-1,-1,2)\), vanishes on all four traps. Row/column-sum computation gives \(Af=f\), so it is dark. By contrast the four traps with row-major indices \(\{0,1,3,5\}\) have a full-rank nine-dimensional Krylov span. In the matrix formed from \(|s\rangle,A|s\rangle,A^2|s\rangle\) in that order for each of these four \(s\), the nine zero-based columns \((0,1,2,3,4,6,7,9,10)\) form a square matrix of determinant exactly \(6\). Its rank is nine, so this placement absorbs every state. Therefore the arbitrary-placement robustness fails already at order nine.

## Verification

The standalone standard-library program `verify.py` reconstructs all prime Paley adjacency matrices directly from quadratic residues, checks their strongly regular identity, and determines exact modular Krylov ranks for every nonempty absorbing subset of sizes up to the threshold for \(p=5\) and \(p=13\). It also checks 200 seeded subsets for \(p=17\). For any eigenvalue of \(A\), the Krylov span generated by absorber position vectors has the same rank as the bright space. Since \(A\) has exactly three distinct eigenvalues, the powers through \(A^2\) suffice. Nonzero ranks modulo a prime certify corresponding nonzero rational minors. The program verifies the order-nine explicit dark mode and an exact integer nine-by-nine determinant of \(6\) for the contrasting complete-capture placement. These are finite checks only; the proof for every prime relies on the inspected Chebotarev theorem, not finite extrapolation.

Run with `python verify.py`. No third-party Python packages are necessary.

## Relationship to prior work

Tao's prime-order Fourier-minor theorem is used as a **previously established mathematical lemma**, not claimed here. Agliari, Mülken and Blumen study trapping in quantum walks on rings, and Le, Donati, Severini and Caruso describe dark subspaces in coherent transport. Burgarth and collaborators connect graph walk matrices to controllability. Razzoli, Paris and Bordone explicitly evaluate **one** trap on strongly regular networks including Paley graphs, obtaining the single-trap efficiency \(2/(p-1)\) for an untrapped position source. This is exactly the \(t=1\) specialization of the present formula and is expressly not new. Their conclusions identify the use of more than one trap as a further question. The present contribution is the all-site-placement, all-positive-rate multi-trap rank law, its exact averaged efficiency, its per-source below-threshold obstruction and an explicit failure when prime order is dropped. None of the examined primary sources states the joint multi-trap conclusion, though it is built using their general tools.

## Limitations

The claim does not cover prime-power Paley graphs in general, arbitrary on-site disorder, unequal coherent hopping weights, decoherence, finite-time relaxation rates, or a speed guarantee for absorption. Other prime-order real circulant families may share a related full-spark mechanism; no uniqueness of Paley graphs is claimed. The older Fourier-minor and dark-space principles make the deduction comparatively short, and unindexed earlier multi-trap derivations remain a real priority risk. Independent scientific validation has not been performed.

## References

1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, first public arXiv posting 2003-08-29, arXiv:math/0308286, Lemma 1.3 and Theorem 1.1. https://arxiv.org/abs/math/0308286
2. E. Agliari, O. Mülken and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, first public arXiv posting 2009-03-19, arXiv:0903.3288. https://arxiv.org/abs/0903.3288
3. D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475 (2011). https://arxiv.org/abs/1111.1475
4. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, J. Phys. A 51 (2018) 365306. https://doi.org/10.1088/1751-8121/aad3e6
5. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, first public arXiv posting 2020-11-27, arXiv:2011.13794, particularly Sec. 4.2 and Sec. 6. https://arxiv.org/abs/2011.13794
