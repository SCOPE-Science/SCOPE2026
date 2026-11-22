# Exact two-particle hopping spectrum and protected peripheral pairs on complete-split quantum networks

## Finding
For integers \(r,m\ge3\), let \(G_{r,m}=K_r\vee\overline{K_m}\): a complete core of \(r\) vertices connected to every one of \(m\) mutually nonadjacent peripheral vertices. Two indistinguishable hard-core excitations hop along edges with unit amplitude and cannot occupy the same vertex. Their one-hop Hamiltonian \(H_{r,m}\) is the adjacency matrix of the two-token graph of \(G_{r,m}\).

Define three polynomials
\[
\begin{aligned}
A(z)&=(z-r+4)(z+1)-m(r-2),\\
B(z)&=z(z-r+1)-r(m-2),\\
C(z)&=(z-2r+4)\bigl[z(z-r+1)-2r(m-1)\bigr]-2m(r-1)z.
\end{aligned}
\]
**Complete spectral factorization:**
\[
\boxed{\det(zI-H_{r,m})=(z+2)^{r(r-3)/2}(z+1)^{(r-1)(m-1)}z^{m(m-3)/2}A(z)^{r-1}B(z)^{m-1}C(z).}
\]
This determines all eigenvalues and their algebraic multiplicities for every pair of integer parameters, including any accidental coincidences between the displayed factors.

The complete zero-energy space has dimension \(m(m-3)/2\). It consists exactly of pair states supported entirely on distinct peripheral vertices, satisfying at each peripheral vertex a zero-sum constraint on incident pair coefficients. For every normalized, localized peripheral pair \(|ij\rangle\), the zero-energy projection has squared norm
\[
\|P_0|ij\rangle\|^2=\frac{m-3}{m-1}.
\]
Consequently, uniformly for all real times \(t\), the probability that both particles occupy peripheral vertices obeys
\[
\Pr_t(\text{both peripheral})\ge\frac{m-3}{m-1},
\]
and for \(m\ge6\), the return probability to the initial pair obeys
\[
|\langle ij|e^{-itH_{r,m}}|ij\rangle|^2\ge\left(\frac{m-5}{m-1}\right)^2.
\]
Thus the complete two-body spectrum exhibits a flat band whose dimension is independent of the number of core vertices, and peripheral-pair localization becomes arbitrarily strong as peripheral size grows.

## Assumptions and scope
The graph is finite, simple, and unweighted, with \(r,m\ge3\). The Hilbert space has orthonormal basis \(|uv\rangle\) indexed by unordered sets of two distinct vertices. The Hamiltonian has off-diagonal matrix element one precisely when one occupied vertex can move along an edge to a previously unoccupied vertex; diagonal entries vanish. This is a **hard-core** two-particle Hamiltonian, not the noninteracting two-boson tensor-square Hamiltonian allowing double occupancy. Dynamics is the unitary \(e^{-itH_{r,m}}\), without disorder, interactions beyond hard-core exclusion, dissipation, or time-dependent driving. All eigenvalue multiplicities are over \(\mathbb C\).

## Proof
**Pair-sector operator.** Write \(A\) for the core vertex set and \(B\) for the independent peripheral set. Partition the two-particle basis into pairs \(AA\), mixed pairs \(AB\), and peripheral pairs \(BB\), of dimensions \(\binom r2\), \(rm\), and \(\binom m2\). Define the unsigned incidence matrix \(U_s\) of the complete graph \(K_s\): it is an \(s\times\binom s2\) matrix, with exactly two ones in each column. Put \(\mathbf1_s\) for the all-ones column vector and \(J_s=\mathbf1_s\mathbf1_s^{\mathsf T}\). In this ordered basis the exact hopping operator is
\[
H_{r,m}=\begin{pmatrix}
U_r^{\mathsf T}U_r-2I&U_r^{\mathsf T}\otimes\mathbf1_m^{\mathsf T}&0\\
U_r\otimes\mathbf1_m&(J_r-I_r)\otimes I_m&\mathbf1_r\otimes U_m\\
0&\mathbf1_r^{\mathsf T}\otimes U_m^{\mathsf T}&0
\end{pmatrix}.
\]
Indeed, two occupied core vertices can slide through the clique; a mixed pair can slide its core particle within the clique, slide its peripheral particle into an unoccupied core site, or move its core particle to an unoccupied peripheral site; and a peripheral pair can only hop to mixed pairs. Every allowed transition has amplitude one.

**Invariant incidence decomposition.** For every \(s\ge3\),
\[
U_sU_s^{\mathsf T}=(s-2)I_s+J_s.
\]
On the constant-vector direction this has eigenvalue \(2(s-1)\), and on the orthogonal standard subspace it has eigenvalue \(s-2\); hence \(U_s\) has full row rank. The pair space \(\mathbb C^{\binom s2}\) decomposes orthogonally as the span of \(U_s^{\mathsf T}\mathbf1_s\), the image of the standard subspace under \(U_s^{\mathsf T}\), and \(\ker U_s\), of dimensions \(1,s-1,s(s-3)/2\). The mixed space splits according to the constant and standard subspaces in each tensor factor.

The kernel \(\ker U_r\) of the core incidence map has eigenvalue \(-2\), with multiplicity \(r(r-3)/2\). The standard-core tensor standard-periphery mixed sector has eigenvalue \(-1\), with multiplicity \((r-1)(m-1)\). The peripheral-pair subspace \(\ker U_m\) has eigenvalue zero, with multiplicity \(m(m-3)/2\).

For each of the \(r-1\) standard-core directions, the remaining coupled two-dimensional block has matrix
\[
M_A=\begin{pmatrix}r-4&\sqrt{m(r-2)}\\ \sqrt{m(r-2)}&-1\end{pmatrix},
\]
whose characteristic polynomial is \(A(z)\). For each of the \(m-1\) standard-peripheral directions, the remaining coupled block is
\[
M_B=\begin{pmatrix}r-1&\sqrt{r(m-2)}\\ \sqrt{r(m-2)}&0\end{pmatrix},
\]
whose characteristic polynomial is \(B(z)\). The three uniform sectors span the block
\[
M_C=\begin{pmatrix}
2r-4&\sqrt{2m(r-1)}&0\\
\sqrt{2m(r-1)}&r-1&\sqrt{2r(m-1)}\\
0&\sqrt{2r(m-1)}&0
\end{pmatrix},
\]
whose characteristic polynomial is \(C(z)\). Taking determinants of these orthogonal blocks proves the factorization. The total degree is exactly \(\binom{r+m}{2}\), so no sector is omitted.

**Exact zero space.** For every \(r,m\ge3\), the constant terms are
\[
A(0)=4-r-m(r-2)<0,\quad B(0)=-r(m-2)<0,\quad C(0)=4r(r-2)(m-1)>0.
\]
Thus no other factor contributes zero; the whole zero eigenspace is precisely \(\ker U_m\) inside the \(BB\) sector. An element \(\sum_{i<j}c_{ij}|ij\rangle\) lies in it if and only if \(\sum_{j\ne i}c_{\min(i,j),\max(i,j)}=0\) for each peripheral vertex \(i\). The strict nonvanishing of the other factors is essential here.

**Protected dynamics.** Let \(P_0\) be the orthogonal projector onto this zero eigenspace. Peripheral permutations commute with \(P_0\) and act transitively on all \(\binom m2\) peripheral pairs. Consequently all its diagonal entries on peripheral pairs coincide. Their sum is the rank \(m(m-3)/2\), so each equals \((m-3)/(m-1)\). For a peripheral pair vector \(\psi\), write \(\psi=P_0\psi+(I-P_0)\psi\). The first term remains stationary under the unitary evolution. The two terms stay orthogonal, and the first is supported entirely on peripheral pairs. It follows that the time-dependent peripheral-pair probability is at least \(\|P_0\psi\|^2\). The return amplitude is \(\langle\psi,e^{-itH}\psi\rangle=d+z(t)\), where \(d=(m-3)/(m-1)\) and \(|z(t)|\le1-d\). For \(m\ge6\) we obtain \(|d+z(t)|\ge2d-1=(m-5)/(m-1)>0\), proving the claimed return bound.

## Verification
The complete `verify_split_bosons.py` program is supplied. It constructs the two-particle matrix directly by enumerating all unordered vertex pairs and allowed single-particle hops. This is separate from constructing the incidence blocks used in the proof. On the sixteen pairs of parameter values \(3\le r,m\le6\), it compares the entire numerical spectrum with the displayed factored polynomial and verifies the exact zero-dimensional subspace and all zero-mode basis vectors. On five smaller parameter pairs it compares the full exact integer characteristic polynomial. It also verifies the exact peripheral projector diagonal and the predicted invariant-time lower bound using direct numerical diagonalization at multiple times. The output is `PASS: 16 independent matrix vs factorization cases, 5 exact charpolys, full dark eigenspaces.` The arbitrary-parameter assertion follows from the block proof, not from extrapolating these finite checks.

## Relationship to prior work
Audenaert, Godsil, Royle, and Rudolph (arXiv:math/0507251; first public 2005-07-12) established the symmetric-square/quantum-exchange construction, cospectrality for strongly regular inputs, and general spectral bounds. Their foundational method is credited, and their inspected work did not specify the present full complete-split characteristic polynomial. Reyes, Dalfó, and Fiol (2024) study token-graph spectral radii, equitable partitions, and certain regular input families; their publicly available article does not state the full spectrum of the nonregular complete-split family. Gamble et al. (2010) address two-particle walks on arbitrary graphs and graph isomorphism, not the complete exact factorization here.

A closely related published result, *A valence-four threshold for bosonic collision-dark states on weighted quantum stars* (2026), proves an incidence-kernel dark subspace of dimension \(q(q-3)/2\) under **two noninteracting bosons with on-site collision loss on a weighted star**. Its full primary result was checked. The linear-algebra mechanism and the leaf-pair projection in that star model are prior art and **not** claimed as new in themselves. The new statement assessed here is the entire spectrum, with all nonzero factors and multiplicities, for two **hard-core** particles on a split network with a clique core of at least three mutually connected sites. The star result neither gives this graph family nor the coupled core, mixed, and peripheral spectral blocks; it does not imply the displayed characteristic polynomial. The peripheral flat-band bounds are a consequence and physical interpretation of the new full factorization. No historical search can guarantee absolute novelty.

## Limitations
Only the specified homogeneous unit hopping and two hard-core particles are covered. Arbitrary nonuniform edge weights, diagonal disorder, other particle numbers, loss, finite-temperature effects, and interacting soft-core bosons are outside the result. The all-time return bound is a lower bound, not an exact return law. The zero-energy mode count is exact for the domain \(r,m\ge3\); no assertions are made about degenerate smaller cases. Historical priority remains provisional: other treatments of two-token spectra on complete-split or threshold graphs may exist outside the inspected corpus. Independent scientific audit has not been performed.

## References
- K. Audenaert, C. Godsil, G. Royle, and T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251, first submitted 2005-07-12, https://arxiv.org/abs/math/0507251.
- M. A. Reyes, C. Dalfó, and M. A. Fiol, *On the spectra and spectral radii of token graphs*, Boletín de la Sociedad Matemática Mexicana 30 (2024), article 11, https://doi.org/10.1007/s40590-023-00583-3.
- J. K. Gamble et al., *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003, first submitted 2010-02-16, https://arxiv.org/abs/1002.3003.
- *A valence-four threshold for bosonic collision-dark states on weighted quantum stars*, publicly indexed 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-valence-four-threshold-for-bosonic-collision-dark-states-on-we--2d5a557c2b86.
