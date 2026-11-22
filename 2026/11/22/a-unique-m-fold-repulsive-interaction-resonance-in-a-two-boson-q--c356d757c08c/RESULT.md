# A unique \(m\)-fold repulsive-interaction resonance in a two-boson quantum star

## Finding
For every integer \(m\ge4\), let two indistinguishable bosons hop with amplitude \(-1\) along the edges of the unweighted star \(K_{1,m}\), with uniform onsite Hubbard repulsion \(U>0\). Then the characteristic polynomial of the two-boson Hamiltonian is exactly
\[
\begin{aligned}
\det(xI-H_U)&=(x-U)x^{m(m-3)/2}Q_{\mathrm{s}}(x)Q_{\mathrm{st}}(x)^{m-1},\\
Q_{\mathrm{s}}(x)&=x^3-Ux^2-4mx+2(m-1)U,\\
Q_{\mathrm{st}}(x)&=x^3-Ux^2-mx+(m-2)U.
\end{aligned}
\]
Each cubic has three distinct real roots, exactly one in each of \(( -\infty,0)\), \((0,U)\), and \((U,\infty)\). The two positive-energy branches in \((0,U)\) from the symmetric and standard sectors meet at exactly one repulsive interaction:
\[
\boxed{U_*=3\sqrt{m-3},\qquad E_*=\sqrt{m-3}.}
\]
At this value the common energy has **exact multiplicity \(m\)**: one permutation-symmetric eigenstate and an \((m-1)\)-dimensional leaf-standard multiplet. Below \(U_*\) the standard-sector middle root is larger; above it the symmetric-sector middle root is larger. Apart from the permanent symmetry-sector multiplicities and the zero and \(U\) flat eigenvalues, there are no other cross-sector collisions at any \(U>0\). For example, four leaves give \(U_*=3\), \(E_*=1\) and a fourfold level; seven leaves give \(U_*=6\), \(E_*=2\) and a sevenfold level.

## Assumptions and scope
The star has hub \(0\) and leaves \(1,\ldots,m\). With canonical bosonic operators \(b_i\) and \(n_i=b_i^\dagger b_i\), work exclusively in the two-particle Hilbert space of dimension \(\binom{m+2}{2}\), with
\[
H_U=-\sum_{i=1}^{m}(b_0^\dagger b_i+b_i^\dagger b_0)
 +\frac{U}{2}\sum_{i=0}^{m}n_i(n_i-1).
\]
The hopping strength is the energy unit. There is no dissipation, external potential, intersite interaction, magnetic phase, or hard-core exclusion. The result is exact for every \(m\ge4\) and \(U>0\); no thermodynamic, dilute-gas, or strong-coupling approximation is used. The term *middle root* means the unique cubic root strictly between zero and \(U\).

## Proof
**1. Symmetry decomposition.** Work in the normalized bosonic occupation states \(|ii\rangle=(b_i^\dagger)^2|\mathrm{vac}\rangle/\sqrt2\) and \(|ij\rangle=b_i^\dagger b_j^\dagger|\mathrm{vac}\rangle\) for distinct sites. Permutation of the leaves commutes with \(H_U\). Four orthonormal trivial-representation vectors are
\[
A=|00\rangle,\quad B=\frac1{\sqrt m}\sum_i|0i\rangle,\quad C=\frac1{\sqrt m}\sum_i|ii\rangle,
\quad D=\binom m2^{-1/2}\sum_{i<j}|ij\rangle.
\]
Their only nonzero off-diagonal couplings are
\[
\langle A,H_U B\rangle=-\sqrt{2m},\quad
\langle C,H_U B\rangle=-\sqrt2,\quad
\langle D,H_U B\rangle=-\sqrt{2(m-1)},
\]
while \(A,C\) have diagonal energy \(U\), and \(B,D\) energy zero. The doublon combination orthogonal to the combination coupled to \(B\) is an eigenvector of energy \(U\). Reordering the remaining three vectors gives the Jacobi block
\[
S_m=\begin{pmatrix}
U&-\sqrt{2(m+1)}&0\\
-\sqrt{2(m+1)}&0&-\sqrt{2(m-1)}\\
0&-\sqrt{2(m-1)}&0
\end{pmatrix},
\]
whose characteristic determinant is \(Q_{\mathrm{s}}\).

For any real leaf vector \(v=(v_i)\) satisfying \(\sum_i v_i=0\), \(\sum_i v_i^2=1\), define
\[
B(v)=\sum_i v_i|0i\rangle,\quad C(v)=\sum_i v_i|ii\rangle,
\quad D(v)=\frac1{\sqrt{m-2}}\sum_{i<j}(v_i+v_j)|ij\rangle.
\]
The identity \(\sum_{i<j}(v_i+v_j)^2=m-2\) makes these three orthonormal; different orthogonal \(v\)'s produce orthogonal blocks. The corresponding Jacobi block is
\[
T_m=\begin{pmatrix}
U&-\sqrt2&0\\
-\sqrt2&0&-\sqrt{m-2}\\
0&-\sqrt{m-2}&0
\end{pmatrix},
\]
with determinant \(Q_{\mathrm{st}}\). As the standard leaf representation has dimension \(m-1\), this block occurs \(m-1\) times.

The remainder lies in the span of distinct-leaf states \(|ij\rangle\). The hopping from such a state to a hub–leaf state is its unsigned vertex-edge incidence map. Its kernel has dimension \(\binom m2-m=m(m-3)/2\): the incidence matrix has full row rank because an annihilating row vector obeys \(a_i+a_j=0\) for every pair, and any triangle forces all \(a_i=0\). Every vector in that kernel has zero energy and zero doublon amplitude. The dimensions \(4+3(m-1)+m(m-3)/2=\binom{m+2}{2}\) exhaust the Hilbert space. The factorization follows.

**2. Exact root structure.** For \(m\ge4\) and \(U>0\), direct evaluation gives
\[
\begin{array}{c|cc}
&x=0&x=U\\\hline
Q_{\mathrm{s}}&2(m-1)U&-2(m+1)U\\
Q_{\mathrm{st}}&(m-2)U&-2U
\end{array}.
\]
Both cubics have negative leading behavior as \(x\to-\infty\) and positive leading behavior as \(x\to+\infty\). Hence each has one root in each of \(( -\infty,0)\), \((0,U)\), and \((U,\infty)\). Degree three leaves no additional roots or repeated roots. In particular, none coincides with the exact flat energies \(0\) or \(U\).

**3. The unique crossing.** Subtraction gives the exact identity
\[
Q_{\mathrm{s}}(x)-Q_{\mathrm{st}}(x)=m(U-3x).
\]
Any shared root must therefore equal \(x=U/3\). Substitution yields
\[
Q_{\mathrm{st}}(U/3)=\frac{2U}{27}\bigl(9(m-3)-U^2\bigr).
\]
For positive \(U\) and integer \(m\ge4\), the unique solution is \(U=3\sqrt{m-3}\). Its common root \(E=U/3=\sqrt{m-3}\) belongs to \((0,U)\). Both cubics have simple roots there, so the symmetric eigenspace contributes one dimension and the standard eigenspace contributes \(m-1\), giving exact multiplicity \(m\). There is no other intersector crossing.

**4. Level-order reversal.** Let \(e_{\mathrm{s}}(U),e_{\mathrm{st}}(U)\in(0,U)\) denote the two middle roots. Differentiating the cubic identities at the origin (with the roots approaching zero as \(U\downarrow0\)) yields
\[
 e_{\mathrm{s}}(U)=\frac{m-1}{2m}U+O(U^2),\qquad
 e_{\mathrm{st}}(U)=\frac{m-2}{m}U+O(U^2).
\]
The second coefficient exceeds the first by \((m-3)/(2m)>0\). Dividing each cubic by \(U\) shows that at large \(U\), the two middle roots converge respectively to \(\sqrt{2(m-1)}\) and \(\sqrt{m-2}\); the former is strictly larger. The roots vary continuously with \(U\), and step 3 allows only one common parameter. Their strict ordering therefore reverses exactly at \(U_*\), as claimed.

## Verification
Two standalone scripts accompany this report and require Python 3 with SymPy. Run `python3 verify_blocks.py` to construct the independent three-by-three Jacobi determinants, verify their symbolic difference and the all-size crossing equation, and check 27 concrete leaf numbers. Run `python3 verify_full.py` to construct the full two-particle occupation matrix from creation/annihilation rules, check 15 exact characteristic polynomials for four through eight leaves, and independently verify the \(m\)-fold eigenvalue nullity at \((m,U,E)=(4,3,1)\) and \((7,6,2)\). The full-matrix checker uses a nonorthonormal monomial basis with integer hopping entries; similarity preserves characteristic polynomials and ranks. The expected successful outputs are `BLOCK_IDENTITY_OK symbolic_cubics=2 symbolic_crossing=1 resonance_sizes=27` and `FULL_TWO_BOSON_OK polynomial_checks=15 exact_resonance_ranks=2`. The proof for all \(m\) is the symmetry decomposition and algebra above, not extrapolation from the finite checks.

## Relationship to prior work
Winkler et al. (2006) established the physically relevant repulsive two-boson Hubbard setting and pair spectroscopy on periodic optical lattices, without the star's leaf-permutation sectors. Gamble et al. (2010) gave the two-boson graph Hubbard operator and examined graph-isomorphism questions for strongly regular graphs; the common operator definition is established rather than new here.

Pouthier (2022), *Quantum self-trapping on a star graph*, addresses the **same underlying graph and two-exciton attractive Hubbard dynamics**, emphasizing excitation initially localized at the hub and self-trapping. Its accessible abstract does not report a positive-interaction standard-irrep versus symmetric-irrep crossing. The full paper could not be inspected, making it a material source-overlap risk; attractive and repulsive full spectra are related by bipartite sign reversal, so a complete spectral classification there would require close statement-level comparison. Its companion study concerns extended stars and an attractive strongly bound pair. No absence-of-priority claim is made based solely on the abstract.

The closest examined noninteracting bosonic collision-loss result on stars gives a zero-energy dark-space dimension \(m(m-3)/2\), agreeing with the flat factor here. However, collision-loss projectors at zero interaction neither give the two nonzero-interaction cubics nor entail the interaction-tuned \(m\)-fold crossing. A distinguishable-walker star reaction result concerns different exchange symmetry and hopping mismatch; its resonant capture condition is not the present repulsive Hubbard degeneracy.

## Limitations
The result addresses exactly two identical bosons, uniform onsite repulsion, uniform hub–leaf hopping, and a single unweighted star. It does not claim analogous spectral crossings for weighted spokes, nonuniform interaction, loss, decoherence, three or more particles, extended stars, or lattices. The crossing is symmetry-protected between distinct leaf-permutation sectors, and would generally split when that symmetry is broken. The inaccessible full star self-trapping paper is a significant historical-priority risk; independent verification and an exhaustive priority survey have not been performed.

## References
1. K. Winkler et al., *Repulsively bound atom pairs in an optical lattice*, arXiv:cond-mat/0605196v1, first public 2006-05-08, https://arxiv.org/abs/cond-mat/0605196 (full text and appendix examined).
2. J. K. Gamble et al., *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003v1, first public 2010-02-16, https://arxiv.org/html/1002.3003v1 (full text examined).
3. V. Pouthier, *Quantum self-trapping on a star graph*, Physical Review E 105, 044304 (2022), https://doi.org/10.1103/PhysRevE.105.044304 (abstract examined; full text unavailable).
4. V. Pouthier, *Two-exciton bound state quantum self-trapping in an extended star graph*, Journal of Chemical Physics 156, 155101 (2022), https://doi.org/10.1063/5.0087200 (abstract examined).
5. *A valence-four threshold for bosonic collision-dark states on weighted quantum stars*, available research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-valence-four-threshold-for-bosonic-collision-dark-states-on-we--2d5a557c2b86/RESULT.md (full result examined).
6. *Exact speed-resonance reaction laws for two quantum walkers on a star*, available research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-exact-speed-resonance-reaction-laws-for-two-quantum-walkers-on-a--1999b1ddea48/RESULT.md (full result examined).
