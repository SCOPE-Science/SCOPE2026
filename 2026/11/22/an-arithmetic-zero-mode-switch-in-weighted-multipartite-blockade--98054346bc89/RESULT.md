# An arithmetic zero-mode switch in weighted multipartite blockade dynamics

## Finding

Fix an integer \(r\geq3\). Let \(K_{m_1,\ldots,m_r}\) be a complete multipartite graph with \(m_i\geq1\), and equip each vertex \(j\) in part \(i\) with a strictly positive real spin-flip amplitude \(\omega_{ij}\). Impose perfect nearest-neighbor excitation blockade: the physical basis contains only the empty configuration \(|\varnothing\rangle\) and the nonempty excitation subsets of a *single* part. On that space let \(H\) flip any one site when the resulting configuration is allowed, with matrix element \(\omega_{ij}\), zero onsite detuning, and \(\hbar=1\).

Define the exact signed-sum counts and their spectral fractions by
\[
 d_i=\#\left\{\varepsilon\in\{-1,+1\}^{m_i}:\sum_{j=1}^{m_i}\varepsilon_j\omega_{ij}=0\right\},
 \qquad a_i=2^{-m_i}d_i,
 \qquad q=\#\{i:d_i=0\}.
\]
Let \(P_0\) be the orthogonal projector onto \(\ker H\). Then the zero-energy spectral weight of the completely unexcited state is *exactly*
\[
 \boxed{\langle\varnothing|P_0|\varnothing\rangle =
 \begin{cases}
 \left(\displaystyle\sum_{i=1}^r a_i^{-1}-(r-1)\right)^{-1},&q=0,\\[2pt]
 0,&q\geq1.
 \end{cases}}
\]
This is also the Cesàro mean of its **complex return amplitude**:
\[
\lim_{T\to\infty}\frac1T\int_0^T
 \langle\varnothing|e^{-\mathrm i tH}|\varnothing\rangle\,dt
 =\langle\varnothing|P_0|\varnothing\rangle.
\]
The full zero-energy eigenspace has exact dimension
\[
 \boxed{\dim\ker H=
 \begin{cases}
 \displaystyle\sum_{i=1}^r d_i-r+1,&q=0,\\[2pt]
 \displaystyle\sum_{i:d_i>0}(d_i-1)+q-1,&q\geq1.
 \end{cases}}
\]
Consequently the vacuum has a stationary zero-energy component **if and only if each part separately admits an equal-sum signed partition of its local driving amplitudes**. The condition is a sharp arithmetic AND gate across all parts, not merely a parity test.

For homogeneous drive \(\omega_{ij}=1\), the vacuum weight vanishes whenever any \(m_i\) is odd. When all \(m_i\) are even, it equals
\[
 \left[\sum_{i=1}^r\frac{2^{m_i}}{\binom{m_i}{m_i/2}}-(r-1)\right]^{-1}.
\]
For fixed \(r\) and all even \(m_i\to\infty\), this is asymptotic to
\[
 \frac{\sqrt{2/\pi}}{\sum_i\sqrt{m_i}}.
\]
Parity is not a fundamental necessity under nonuniform drive: three parts of sizes \((3,2,4)\) with amplitude lists \((1,1,2)\), \((1,1)\), and \((1,1,1,1)\) have \((d_1,d_2,d_3)=(2,2,6)\), \(\dim\ker H=8\), and vacuum zero-energy weight \(3/20\). Perturbing only the third amplitude in the first part from \(2\) to \(2+\delta\), where \(0<|\delta|<1\), gives \(d_1=0\), \(\dim\ker H=6\), and zero vacuum spectral weight. This is an exact infinite-time spectral change; it does not imply discontinuity of finite-time amplitudes.

## Assumptions and scope

All \(r\) parts are labelled, nonempty, and pairwise fully connected; no edges occur within one part. Every \(\omega_{ij}\) is strictly positive and real, not necessarily integer or commensurate. There is exactly one unconstrained spin-flip transition per site, no diagonal terms, no loss, and no simultaneous excitations in different parts. The Hilbert dimension is \(1+\sum_i(2^{m_i}-1)\). The result asserts zero-energy spectral multiplicity and one specified spectral projection, not the complete nonzero spectrum.

## Proof

**1. Weighted-cube decomposition.** For each part \(i\), adjoin the common empty state to its nonempty subsets. Within those states its unconstrained spin-flip matrix is the weighted Boolean-cube operator
\[
 H_i=\sum_{j=1}^{m_i}\omega_{ij}X_j
\]
on \(\mathbb C^{2^{m_i}}\). The multipartite configuration graph is the union of these weighted cubes with their single empty-state vertices identified. Every nonempty configuration belongs to a unique cube. Thus \(H\) is the root amalgamation of the \(H_i\), with no duplicate root hopping terms.

**2. Local zero modes.** Tensor products of \(X\)-eigenvectors diagonalize \(H_i\), with eigenvalues \(\sum_j\varepsilon_j\omega_{ij}\). Hence \(\dim\ker H_i=d_i\). Every normalized tensor eigenvector has squared overlap \(2^{-m_i}\) with the empty basis state \(|0_i\rangle\), so
\[
\langle0_i|P_{\ker H_i}|0_i\rangle=a_i.
\]
If \(d_i>0\), the evaluation functional at \(0_i\) is nonzero on \(\ker H_i\), and its kernel has dimension \(d_i-1\). If \(d_i=0\), \(H_i\) is invertible. Since \(Z^{\otimes m_i} H_i Z^{\otimes m_i}=-H_i\) and \(Z^{\otimes m_i}|0_i\rangle=|0_i\rangle\), it follows that \(\langle0_i|H_i^{-1}|0_i\rangle=0\).

**3. Gluing equations.** A global vector gives restrictions \(v_i\) to each cube, all having a common root amplitude \(c\). It lies in \(\ker H\) exactly when there exist scalars \(\alpha_i\) such that
\[
H_i v_i=\alpha_i|0_i\rangle,\qquad
\sum_{i=1}^r\alpha_i=0,
\]
where the first equation expresses vanishing at every nonroot configuration and the second expresses vanishing at the shared root. If \(d_i>0\), inner product with a local zero eigenvector having nonzero root component forces \(\alpha_i=0\), so \(v_i\in\ker H_i\). If \(d_i=0\), then \(v_i=\alpha_iH_i^{-1}|0_i\rangle\) and its root amplitude is zero. Thus the presence of even one zero-free cube forces \(c=0\). When \(q=0\), the common \(c\) supplies one dimension, alongside \(d_i-1\) root-zero directions in every cube, giving \(\sum_i d_i-r+1\). When \(q\ge1\), the zero-bearing cubes supply \(\sum_{d_i>0}(d_i-1)\) directions, and the \(q\) root sources on invertible cubes satisfy one independent relation \(\sum\alpha_i=0\), giving \(q-1\) further directions. This proves the exact nullity formula.

**4. Root spectral projection.** When \(q\ge1\), every zero eigenvector vanishes at the shared root, so the projected vacuum weight is zero. When \(q=0\), fix global root amplitude \(c=1\). In cube \(i\), the least squared norm of a vector in \(\ker H_i\) with root amplitude one is \(1/a_i\), by Cauchy–Schwarz with equality at the local projected root vector. These local minimizers form a global zero mode, and gluing identifies the root \(r\) times, so their global squared norm is precisely \(\sum_i a_i^{-1}-(r-1)\). The squared norm of the evaluation functional on the global kernel is the reciprocal of this minimum, proving the projection formula. Its denominator is positive since \(0<a_i\le1\).

**5. Dynamics, homogeneous asymptotics, and boundary example.** The finite-dimensional spectral theorem makes the time average of \(e^{-\mathrm i tH}\) converge to \(P_0\). Equal driving amplitudes yield a zero signed sum exactly for even \(m_i\), with \(d_i=\binom{m_i}{m_i/2}\). Stirling's central-binomial asymptotic gives the stated fixed-part-count limit. For the specified \((3,2,4)\) example, direct signed-sum counting gives \((2,2,6)\); the gluing formulas give \(8\) and \(3/20\). The perturbation \(0<|\delta|<1\) removes all zero signed sums in the first part and leaves the other parts unchanged, giving \(6\) and zero.

## Verification

The standalone program `verify_kernel.py` builds the weighted PXP matrix **directly from globally permitted excitation configurations**, computes its exact rational nullspace and orthogonal kernel projection, and compares to signed-sum formulas in 17 cases of three or four parts. It includes both tuned odd-part resonances and their detuned counterparts. The independent program `verify_resolvent.py` builds the configuration matrix by separately enumerating bitstrings and checking the no-cross-part constraint, then checks 24 exact rational comparisons of
\[
\langle\varnothing|(zI-H)^{-1}|\varnothing\rangle=
 \left[\sum_i\left(2^{-m_i}\sum_{\varepsilon\in\{-1,+1\}^{m_i}}
 (z-\varepsilon\cdot\omega_i)^{-1}\right)^{-1}-(r-1)z\right]^{-1}
\]
against direct full-matrix inversion at three nonzero rational spectral parameters. Both passed; the check log is in `CHECKS.txt`. The infinite family is proved by the displayed argument, not inferred from the finite verifications.

## Relationship to prior work

Lesanovsky's 2010 preprint supplies an early Rydberg blockade/spin-constraint framework, but studies a one-dimensional effective constrained Hamiltonian and its ground state. Windt and Pichler (first posted December 14, 2021) analyze scar-related coherent dynamics on **equal-size complete bipartite** graphs with homogeneous driving, focusing on a thermodynamic scattering approximation, rather than exact multipartite, site-dependent zero-energy spectral projectors. Buijsman (first posted March 17, 2022) analyzes PXP zero-state counts in **open and periodic chains**, using chiral and inversion symmetries; those general methods do not state the displayed weighted multipartite equality. Prior spectral work on anisotropically weighted Boolean hypercubes likewise relates long-time quantum-walk mixing to signed sums; this local Walsh/signed-sum spectral observation is not claimed as new. The full text of that additional indexed result was inaccessible, so only its available published summary informed the comparison. General vertex-coalescence characteristic-polynomial identities are established in graph spectral theory, and are treated here as a proof technique rather than a new discovery. The claimed contribution is the explicit signed-partition-controlled physical spectral atom and exact nullity for arbitrary positive site drives on all multipartite networks with at least three parts, including the sharp example where unequal driving defeats the homogeneous parity criterion.

## Limitations

The condition is an exact-resonance statement, not stability under detuning: arbitrarily small generic changes of amplitudes remove exact zero signed sums. It does not characterize nonzero eigenvalue gaps, metastable lifetimes near resonance, probability decay, dephasing, losses, or finite-temperature effects. It makes no assertion of independent verification, or of a complete historical-priority search across unindexed literature. The no-cross-part-excitation constraint must be exact; finite interaction energies or nonzero onsite detunings are outside the theorem.

## References

1. I. Lesanovsky, *Many-body spin interactions and the ground state of a dense Rydberg lattice gas*, arXiv:1010.2349, first publicly posted 2010-10-12, https://arxiv.org/abs/1010.2349.
2. B. Windt and H. Pichler, *Squeezing Quantum Many-Body Scars*, arXiv:2112.07754, first publicly posted 2021-12-14, https://arxiv.org/abs/2112.07754.
3. W. Buijsman, *Number of zero-energy eigenstates in the PXP model*, arXiv:2203.09264, first publicly posted 2022-03-17, https://arxiv.org/abs/2203.09264.
4. *On the Adjacency, Laplacian, and Signless Laplacian Spectrum of Coalescence of Complete Graphs*, 2016, DOI:10.1155/2016/5906801, https://doi.org/10.1155/2016/5906801. General coalescence context, not a source for this exact multipartite zero-mode result.
5. *Sharp uniform-averaging design for anisotropically weighted hypercubes*, publicly indexed mathematical research record (summary examined; full text inaccessible), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-sharp-uniform-averaging-design-for-anisotropically-weighted-hype--58400972baab. Local signed-sum context only.
