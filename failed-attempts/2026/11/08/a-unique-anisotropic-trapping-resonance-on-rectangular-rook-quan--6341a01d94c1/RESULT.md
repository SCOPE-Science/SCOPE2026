# A unique anisotropic trapping resonance on rectangular rook quantum networks

## Finding

For unequal integers \(m,n\ge 2\), consider coherent one-excitation transport on the rook graph \(K_m\square K_n\) with positive hopping strengths \(a,b\) along the two clique coordinates. A single vertex \((1,1)\) has irreversible loss rate \(2\kappa\), with arbitrary \(\kappa>0\), and no other noise or loss. Let \(\eta_{ij}\) denote the eventual probability of absorption when the initial excitation is localized at \((i,j)\).

**Theorem.** Put \(R=(am=bn)\). Away from \(R\), the complete efficiency table is

| Source relative to \((1,1)\) | \(\eta_{ij}\) when \(am\ne bn\) |
|---|---|
| At \((1,1)\) | \(1\) |
| Same first coordinate, \(i=1,j\ne1\) | \(1/(n-1)\) |
| Same second coordinate, \(i\ne1,j=1\) | \(1/(m-1)\) |
| Different in both coordinates, \(i\ne1,j\ne1\) | \(1/((m-1)(n-1))\) |

At the single resonance \(am=bn\), subtract the following **exact nonnegative deficit** from each corresponding entry in the preceding table:

| Source class | Deficit \(\eta_{\mathrm{off}}-\eta_{\mathrm{res}}\) |
|---|---|
| At the trap | \(0\) |
| \(i=1,j\ne1\) | \(\dfrac{(m-1)n}{m(n-1)(m+n-2)}\) |
| \(i\ne1,j=1\) | \(\dfrac{(n-1)m}{n(m-1)(m+n-2)}\) |
| \(i\ne1,j\ne1\) | \(\dfrac{(m-n)^2}{mn(m-1)(n-1)(m+n-2)}\) |

The theorem concerns the **rectangular class \(m\ne n\)**, for which the graph is not strongly regular. Its exact formulas hold for all \(m,n\ge2\) with \(m\ne n\), \(a,b,\kappa>0\), and every site. The efficiency is independent of \(\kappa\) and constant as a function of the positive coupling ratio \(a/b\) except at \(a/b=n/m\). At that single anisotropic ratio, the loss is strictly positive from **all three nontrap source classes**, including sites in neither the target row nor its column; the last deficit is strictly positive precisely because \(m\ne n\). This establishes a geometry-induced resonance boundary not captured by ordinary strongly regular graph formulas. When \(m=n=q\), the same projector computation reduces to the **previously published** strongly regular efficiency \(1/[2(q-1)]\) for neighbors and \(1/(q-1)^2\) for nonneighbors at isotropic couplings; that special case is not claimed as novel.

## Assumptions and scope

The site Hilbert space is \(\mathbb C^m\otimes\mathbb C^n\), with standard basis \(|i,j\rangle\). Write \(A_s=\mathbf1_s\mathbf1_s^{\mathsf T}-I_s\), the adjacency matrix of \(K_s\). The hopping Hamiltonian and the absorbing effective evolution generator are

\[
H=aA_m\otimes I_n+bI_m\otimes A_n,\qquad
G=-\mathrm iH-\kappa|1,1\rangle\langle1,1|.
\]

For a unit basis vector \(|i,j\rangle\), let \(\psi(t)=e^{tG}|i,j\rangle\). Define the limiting capture probability by

\[
\eta_{ij}=2\kappa\int_0^\infty|\langle1,1|\psi(t)\rangle|^2\,dt
=1-\lim_{t\to\infty}\|\psi(t)\|^2.
\]

All quantities are finite-dimensional and the stated limit exists. The two factors are complete graphs, not a complete bipartite graph. The words *rook graph* and *Cartesian product of complete graphs* refer to the same object. All indices are labeled; the principal theorem assumes \(m,n\ge2\) and \(m\ne n\), and all three rates are strictly positive. The auxiliary square case is stated solely for comparison with previously published strongly regular results. The study concerns eventual trapping, not mean trapping time, finite-time transfer, dephasing, or multiple sinks.

## Proof

**1. The exactly absorbed subspace.** Let \(P_e\) be the orthogonal spectral projector of the Hermitian matrix \(H\) at each **distinct** eigenvalue \(e\), and write \(|s\rangle=|1,1\rangle\). Define

\[
\mathcal B=\operatorname{span}\{P_e|s\rangle:P_e|s\rangle\ne0\},\qquad
\mathcal D=\mathcal B^\perp.
\]

Both subspaces are \(H\)-invariant, \(|s\rangle\in\mathcal B\), and the loss operator annihilates \(\mathcal D\). On \(\mathcal B\), an eigenvector of \(G\) with real part of eigenvalue zero would, by taking the real part of its inner-product equation, have zero overlap with \(|s\rangle\); it would then be an eigenvector of \(H\) in \(\mathcal B\) orthogonal to \(|s\rangle\). This is impossible, since \(\mathcal B\) contains exactly one line \(\mathbb C P_e|s\rangle\) per distinct eigenvalue, each with nonzero trap overlap. Consequently all eigenvalues of \(G|_{\mathcal B}\) have strictly negative real parts, and the \(\mathcal B\) component decays to zero. The component in \(\mathcal D\) evolves unitarily. Therefore

\[
\eta_{ij}=\|\operatorname{Proj}_{\mathcal B}|i,j\rangle\|^2
=\sum_{e:P_e s\ne0}
\frac{|\langle s|P_e|i,j\rangle|^2}{\langle s|P_e|s\rangle}.
\]

This formula proves independence from \(\kappa>0\) and prevents incorrectly counting different eigenvectors at the same eigenvalue as separately absorbing channels.

**2. Four tensor spectral sectors.** Write \(Q_r=\mathbf1_r\mathbf1_r^{\mathsf T}/r\) and \(R_r=I_r-Q_r\). Because \(A_r=(r-1)Q_r-R_r\), the four orthogonal projectors of the tensor decomposition are

\[
P_{00}=Q_m\otimes Q_n,\quad P_{01}=Q_m\otimes R_n,\quad
P_{10}=R_m\otimes Q_n,\quad P_{11}=R_m\otimes R_n,
\]

with respective eigenvalues

\[
a(m-1)+b(n-1),\quad a(m-1)-b,\quad -a+b(n-1),\quad -a-b.
\]

For \(a,b>0\), the **only** possible equality between different displayed energies is the middle pair, and it occurs precisely at \(am=bn\). Every displayed projector has positive diagonal weight at \(|s\rangle\), so all four sectors are present off resonance. Put \(d_{uv}=\langle s|P_{uv}|s\rangle\) and \(c_{uv}=\langle s|P_{uv}|i,j\rangle\). Their trap weights are

\[
(d_{00},d_{01},d_{10},d_{11})
=\frac{(1,n-1,m-1,(m-1)(n-1))}{mn}.
\]

Every off-diagonal entry of \(Q_r\) equals \(1/r\), whereas those of \(R_r\) equal \(-1/r\); the diagonal entries of \(R_r\) equal \((r-1)/r\). Applying the first step to four *distinct* energies gives the product formula for off-resonance capture:

\[
\eta_{ij}^{\mathrm{off}}=
\left(\mathbf1_{\{i=1\}}+\frac{\mathbf1_{\{i\ne1\}}}{m-1}\right)
\left(\mathbf1_{\{j=1\}}+\frac{\mathbf1_{\{j\ne1\}}}{n-1}\right).
\]

This gives the first table, including \(m=2\) and \(n=2\).

**3. Combining the colliding channels.** At \(am=bn\), the true eigenprojector for the merged energy is \(P_{01}+P_{10}\), not two distinct projectors. Its contribution to efficiency is

\[
\frac{|c_{01}+c_{10}|^2}{d_{01}+d_{10}},
\]

in place of \(|c_{01}|^2/d_{01}+|c_{10}|^2/d_{10}\). The lost amount is exactly

\[
\Delta_{ij}=\frac{|c_{01}d_{10}-c_{10}d_{01}|^2}
{d_{01}d_{10}(d_{01}+d_{10})}\ge0.
\]

For \(i=1,j\ne1\), the pair \((c_{01},c_{10})=(-1,m-1)/(mn)\); for \(i\ne1,j=1\), it is \((n-1,-1)/(mn)\); for \(i\ne1,j\ne1\), it is \((-1,-1)/(mn)\); and at the trap it equals \((d_{01},d_{10})\). Inserting these four pairs and the displayed weights yields all four entries of the second table. At \(m\ne n\), every nontrap source class has a strictly positive resonance loss; for the comparison case \(m=n=q\), the neighboring efficiency halves while the nonneighbor deficit vanishes, agreeing with the known strongly regular law. No asymptotic argument is needed. This completes the proof.

## Verification

The accompanying `checker.py` constructs the full labeled Hamiltonian independently, forms the exact Krylov span \(\operatorname{span}\{|s\rangle,H|s\rangle,\ldots\}\), and computes its orthogonal projection using rational matrix algebra. It checks all four initial-site orbits, both spectral regimes, and \(m,n\in\{2,3,4,5\}\). The file also independently computes late-time non-Hermitian evolution for selected small networks and verifies the infinite-time formula to tolerance \(10^{-8}\). Reproduction: `python checker.py` with Python, SymPy, NumPy and SciPy. The analytic proof, not the finite tests, covers unbounded \(m,n\) and continuous positive couplings and loss rates.

## Relationship to prior work

Plenio and Huelga (arXiv:0807.4902, posted 30 July 2008) introduce the noise-assisted excitation-transport setting. Caruso and collaborators (arXiv:0901.4454, posted 28 January 2009) analyze invariant dark spaces for coherent trapping, including complete networks and a general invariant-space method. Le and collaborators (2018, DOI 10.1088/1751-8121/aad3e6) examine dark states and coupling perturbations, with explicit complete-graph and path–cycle cylinder examples. Razzoli, Paris and Bordone (arXiv:2011.13794; Entropy 23 (2021), §4.2, Equation (25)) prove an **exact strongly regular graph single-trap efficiency law**, directly covering the isotropically weighted square rook network \(K_q\square K_q\). We explicitly exclude that known isotropic square case from the novelty assertion. Rectangular rook graphs with \(m\ne n\) are not strongly regular: two adjacent vertices in the same first-coordinate clique have \(n-2\) shared neighbors, while two adjacent vertices in the same second-coordinate clique have \(m-2\), unequal when \(m\ne n\). Their strong-regularity equation thus cannot imply the rectangular resonance formula. The present argument **uses** the previously known dark-space principle; its proposed new assertion is the rectangular all-size two-parameter efficiency classification, the unique anisotropic ratio \(am=bn\), and the exact strictly positive source-dependent resonance losses in all three nontrap classes. The general spectral methods in those sources can be specialized to compute this case, but the inspected source statements do not provide or imply the rectangular piecewise formulas. Related exact absorber-number work on a cyclic ladder and an unweighted 16-vertex rook graph addresses different observables and does not imply the stated one-sink weighted all-size efficiency law.

## Limitations

The source must be a localized vertex state and the target exactly one vertex. No assertion is made about mean absorption times, finite observation windows, nonzero dephasing, additional losses, arbitrary site potentials, or multiple traps. The jump is an infinite-time idealization: as the coupling ratio approaches resonance, the near-dark decay time may diverge, so finite-time efficiencies need not jump. The general dark-space principle and the isotropic square rook specialization of the strongly regular efficiency theorem are established prior work. Only the rectangular anisotropic classification is asserted as a potentially new result; historical novelty of its particular formulas remains subject to independent scrutiny; searchable literature and the examined primary papers cannot prove absolute priority.

## References

1. M. B. Plenio and S. F. Huelga, *Dephasing assisted transport: Quantum networks and biomolecules*, arXiv:0807.4902 (first public 2008-07-30), https://arxiv.org/html/0807.4902v1.
2. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454 (first public 2009-01-28), https://arxiv.org/html/0901.4454v2.
3. T. P. Le, L. Donati, S. Severini, and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, J. Phys. A 51 (2018) 365306, https://doi.org/10.1088/1751-8121/aad3e6.
4. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, Entropy 23 (2021) 85, https://arxiv.org/abs/2011.13794.
