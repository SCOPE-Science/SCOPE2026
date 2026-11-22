# Unattained sharp two-particle transport ceiling on balanced bicliques

## Finding

For every pair of integers \(m,n\ge3\), let two indistinguishable hard-core bosons hop with unit amplitude along the edges of the complete bipartite graph \(K_{m,n}\), without double occupancy. Start from a basis state with one particle in each part. Let \(P_{m,n}(t)\) be the probability, at time \(t\ge0\), that both particles occupy the same bipartition class. Then
\[
\boxed{P_{m,n}(t)=\frac{\sin^2(\omega_0t)+(m-1)\sin^2(\omega_A t)+(n-1)\sin^2(\omega_B t)}{mn},}
\]
where
\[
\omega_0=\sqrt{4mn-2m-2n},\quad \omega_A=\sqrt{n(m-2)},\quad\omega_B=\sqrt{m(n-2)}.
\]
In particular, \(P_{m,n}(t)\le(m+n-1)/(mn)\) for all times and the infinite-time Cesàro mean is \((m+n-1)/(2mn)\).

On every balanced biclique \(m=n=r\ge3\), this bound is the **exact global supremum** yet is **never attained at any finite time**:
\[
\boxed{\sup_{t\ge0}P_{r,r}(t)=\frac{2r-1}{r^2},\qquad P_{r,r}(t)<\frac{2r-1}{r^2}\ \text{for every finite }t.}
\]
At \(t_r=\pi/(2r)\), \(rP_{r,r}(t_r)\to2\). On the identical configuration graph, the *classical* symmetric exclusion process with unit directed-edge transition rates, also started from opposite parts, instead has same-part probability
\[
C_r(t)=\frac{r-1}{2r-1}(1-e^{-(4r-2)t}),\qquad C_r(t_r)\longrightarrow\frac{1-e^{-2\pi}}2.
\]
Thus at the same physically specified short time, coherent same-part transport vanishes as \(2/r\), whereas classical same-part transport stays positive.

The full hopping characteristic polynomial, with repeated factors counted, is
\[
\det(zI-H)=z^{\binom{m+n}{2}-2(m+n-1)}(z^2-\omega_0^2)(z^2-\omega_A^2)^{m-1}(z^2-\omega_B^2)^{n-1}.
\]

## Assumptions and scope

The graph is finite and simple, with left part \(A\) of \(m\) vertices and right part \(B\) of \(n\) vertices, where \(m,n\ge3\). The orthonormal Hilbert-space basis consists of unordered two-element vertex subsets. The Hermitian operator \(H\) has matrix entry one precisely when one particle can move across one base edge to a vacant vertex; it has zero diagonal. Equivalently, \(H\) is the adjacency matrix of the two-token graph \(F_2(K_{m,n})\). The unitary evolution is \(e^{-itH}\), with \(\hbar=1\). The initial state is one basis vector \(|a,b\rangle\), \(a\in A,b\in B\); all choices are symmetry-equivalent. The final observable projects onto configurations with both tokens in \(A\) or both in \(B\). The classical comparison uses the standard continuous-time two-token exclusion generator \(Q=H-D\), where \(D\) is the degree diagonal, not a generator with total jump rate normalized to one. For the classical comparison we restrict to \(m=n=r\). The supremum is over all real nonnegative time; no finite observation window is substituted for it.

## Proof

**1. Exact singular-value blocks.** Partition unordered token states into \(AA=\binom A2\), \(AB=A\times B\), and \(BB=\binom B2\). A move flips exactly one token's shore, so there are no transitions within the \(AB\) block nor within \(AA\cup BB\). In the ordered orthonormal decomposition \((AA\oplus BB)\oplus AB\),
\[
H=\begin{pmatrix}0&W\\W^{\mathsf T}&0\end{pmatrix}.
\]
For an \(s\)-element set, let \(B_s\) be the unsigned edge-by-vertex incidence matrix of \(K_s\), so \((B_s)_{\{i,j\},k}=1\) exactly when \(k\in\{i,j\}\). The one-hop rule gives
\[
W=\begin{pmatrix}B_m\otimes\mathbf1_n^{\mathsf T}\\\mathbf1_m^{\mathsf T}\otimes B_n\end{pmatrix},\qquad
B_s^{\mathsf T}B_s=(s-2)I_s+J_s.
\]
The two block rows enumerate respectively a right token moving left, and a left token moving right. It follows directly that
\[
W^{\mathsf T}W=\bigl((m-2)I_m+J_m\bigr)\otimes J_n + J_m\otimes\bigl((n-2)I_n+J_n\bigr).
\]
Resolve each coordinate space into constants and their orthogonal complements. The four tensor sectors have squared singular values and multiplicities
\[
\begin{array}{c|c|c}
\text{sector}&\text{squared singular value}&\text{multiplicity}\\\hline
\mathbf1_m\otimes\mathbf1_n&4mn-2m-2n&1\\
\mathbf1_m^{\perp}\otimes\mathbf1_n&n(m-2)&m-1\\
\mathbf1_m\otimes\mathbf1_n^{\perp}&m(n-2)&n-1\\
\mathbf1_m^{\perp}\otimes\mathbf1_n^{\perp}&0&(m-1)(n-1).
\end{array}
\]
The three positive values exist because \(m,n\ge3\). Each nonzero singular value produces two eigenvalues of \(H\), one of each sign. The remaining eigenvalues are zero, with total dimension \(\binom{m+n}{2}-2(m+n-1)\). This proves the characteristic polynomial.

**2. Exact coherent probability.** The exact propagator starting in \(AB\) is block-off-diagonal with transition operator \(-iW\sin(t\sqrt{W^{\mathsf T}W})/\sqrt{W^{\mathsf T}W}\), interpreted continuously at zero singular values. The squared probability of entering \(AA\oplus BB\) therefore equals the expectation of \(\sin^2(t\sqrt{W^{\mathsf T}W})\) in the initial \(AB\) unit vector. Its squared projections onto the constant-constant, left-standard, and right-standard sectors are, respectively, \(1/(mn)\), \((m-1)/(mn)\), and \((n-1)/(mn)\). The remaining \((m-1)(n-1)/(mn)\) lies in the zero-energy sector and cannot reach same-shore states. Substitution gives the asserted trigonometric law and its universal upper bound. Every positive frequency has time-average squared sine equal to \(1/2\), proving the exact Cesàro mean without assuming incommensurate frequencies.

**3. Exact, unattained balanced supremum.** For \(m=n=r\), the two positive frequencies relevant to the same-part probability are
\[
\omega_0=2\sqrt{r(r-1)},\qquad \omega_1=\sqrt{r(r-2)},
\]
with \(P_{r,r}(t)=r^{-2}[\sin^2(\omega_0t)+2(r-1)\sin^2(\omega_1t)]\). Their ratio is \(2\sqrt{(r-1)/(r-2)}\), which is irrational for every integer \(r\ge3\). Indeed, the consecutive, coprime positive integers \(r-1,r-2\) could have rational square-root ratio only if both were integer perfect squares; consecutive strictly positive squares do not exist. By irrational linear-flow density on the two-torus, there are times for which both \(\sin^2\) terms approach one arbitrarily closely. Therefore the upper bound \((2r-1)/r^2\) is the exact supremum. If it were attained at a finite time, both positive sine-square terms would equal one, forcing \(\omega_0/\omega_1\) to equal a ratio of odd positive integers, contrary to irrationality. The supremum is thus never reached.

At \(t_r=\pi/(2r)\), \(\omega_0t_r=\pi\sqrt{1-1/r}\to\pi\) and \(\omega_1t_r=(\pi/2)\sqrt{1-2/r}\to\pi/2\). Hence \(rP_{r,r}(t_r)\to2\). No assertion of a finite-time optimum at \(t_r\) is made.

**4. Classical contrast.** Under classical continuous-time exclusion on \(K_{r,r}\), a configuration with tokens on opposite shores has \(2(r-1)\) successful edges leading to a same-shore configuration; a same-shore configuration has \(2r\) successful edges returning to opposite shores. The partition is therefore lumpable, and its same-shore probability \(C_r\), with \(C_r(0)=0\), satisfies
\[
C_r'(t)=2(r-1)(1-C_r(t))-2r C_r(t).
\]
Solving the scalar ODE gives the displayed classical formula. At \(t_r=\pi/(2r)\), \((4r-2)t_r\to2\pi\), and its limit is \((1-e^{-2\pi})/2\). The classical lumpability calculation is standard and is not claimed as an independent discovery.

## Verification

The reproducibility script `verify_two_token.py` constructs each two-token hopping matrix directly by enumerating every permitted single-token move. Without using the incidence-block construction, it verifies exact characteristic-polynomial equality via integer symbolic arithmetic for six cases \((m,n)\in\{(3,3),(3,4),(4,4),(3,5),(4,5),(5,5)\}\), and it checks the exact time-dependent same-shore formula through direct complex matrix exponentiation at four positive times per case. For balanced graphs it separately checks classical same-shore probabilities by exponentiating the full exclusion generator at three times. It also prints numerical large-\(r\) comparisons for \(r=4,8,16,32,64,128\); these illustrate, but do not prove, the limits. Execution of this exact packaged script passed all assertions. The all-size and all-time arguments are the analytic block and irrationality proofs above, not finite experimentation.

Reproduce with Python 3 and the public NumPy, SciPy and SymPy libraries: `python verify_two_token.py`.

## Relationship to prior work

Audenaert, Godsil, Royle and Rudolph (2005) defined the symmetric-square graph and connected its adjacency operator to exchange Hamiltonians; that general construction is used rather than claimed. Dalfó and coauthors (2020) developed token-graph Laplacian relations. A published complete-bipartite **two-token Laplacian** factorization uses incidence-sector blocks on exactly the same configuration graph. Those blocks are a close methodological antecedent and make the present singular-value calculation short, but a combinatorial Laplacian spectrum does not itself determine the adjacency propagator or the all-time same-shore observable. The published collision-loss biclique-boson projector concerns noninteracting bosons that may occupy a common site until lost; nevertheless its double-centered cross-shore zero-energy subspace remains stationary under the hard-core Hamiltonian here. Consequently its explicit projector already implies the elementary all-time upper envelope \((m+n-1)/(mn)\), which is **not claimed as new**. That projector does not establish whether this bound is sharp, attained, or approached for the present coherent unitary process. The published balanced-biclique noncollision/exclusion traffic calculation contains the classical two-state rates used here; those rates are not new. Another published two-particle biclique entanglement result uses a discrete-time Grover arc walk, not this continuous-time hard-core Hamiltonian. The present assessed claim is specifically the sharp **unattained**, all-size coherent transport ceiling, its exact time-resolved probability and the quantum/classical short-time contrast, not incidence linear algebra, generic quantum evolution, or the classical lumping as isolated facts.

## Limitations

The theorem assumes unit uniform adjacency hopping, exactly two hard-core bosons, a complete bipartite graph with both shores of size at least three, an opposite-shore localized initial state, and a same-shore aggregate observable. The optimality assertion is a supremum over arbitrarily long times: attaining a given approximation quality may require long observation times, and no quantitative optimal waiting-time law is proved. For rectangular graphs the universal upper bound is proved but not asserted to be globally sharp for every pair of sizes. No claim is made about independently moving soft-core bosons, finite collision losses, decoherence, disordered edges, or higher particle counts. Closely related block decompositions are already published, and an unindexed direct formula or simpler historical implication remains a priority risk; absence from search results does not certify novelty. No independent scientific validation has been performed.

## References

1. K. Audenaert, C. Godsil, G. Royle and T. Rudolph, *Symmetric Squares of Graphs*, first public arXiv version July 12, 2005, https://arxiv.org/abs/math/0507251.
2. C. Dalfó and coauthors, *On the Laplacian spectra of token graphs*, first public arXiv version December 1, 2020, https://arxiv.org/abs/2012.00808.
3. M. A. Reyes, C. Dalfó and M. A. Fiol, *On two algebras of token graphs*, https://doi.org/10.1007/s40590-023-00583-3 (methodological antecedent; not used as the focal archive date).
4. *Exact Laplacian spectrum and spanning-tree count of two-token complete-bipartite graphs*, public research record `40156451790b` (same configuration graph, different operator and observable).
5. *Collision-dark boson projector and size-two anomaly on complete bipartite networks*, public research record `f8fb928d3537` (different no-jump model).
6. *Exact traffic dynamics and path-space entropy for two noncolliding walkers on balanced bicliques*, public research record `84ed4797c0f0` (classical reference).
7. *Exact two-particle entanglement spectra on complete bipartite graphs*, public research record `19cb5844655b` (discrete-time quantum-walk reference).
