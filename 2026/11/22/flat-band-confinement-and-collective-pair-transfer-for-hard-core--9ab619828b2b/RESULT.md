# Flat-band confinement and collective pair transfer for hard-core bosons on complete bipartite networks

## Finding
For integers \(p,q\ge3\), let two indistinguishable hard-core bosons hop with unit amplitude along the edges of \(K_{p,q}\), with no onsite potentials or additional interactions. The Hilbert space has an orthonormal basis \(|S\rangle\) indexed by two-element subsets of the \(p+q\) sites. The Hamiltonian \(H\) has matrix entry one exactly when one occupied site moves along one edge to a vacant site.

Put \(N=\binom{p+q}{2}\), \(\Omega^2=4pq-2p-2q\), \(\alpha^2=q(p-2)\), and \(\beta^2=p(q-2)\). The *complete* spectrum, with additive multiplicities at collisions, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\pm\Omega&1\ \text{each}\\
\pm\alpha&p-1\ \text{each}\\
\pm\beta&q-1\ \text{each}\\
0&\frac{(p+q-1)(p+q-4)}2.
\end{array}
\]

Let \(|A\rangle\), \(|M\rangle\), and \(|B\rangle\) be normalized uniform superpositions respectively over pairs entirely in the first shore, pairs straddling the shores, and pairs entirely in the second shore. Then
\[
\max_{t\in\mathbb R}|\langle B|e^{-itH}|A\rangle|^2
=\frac{16pq(p-1)(q-1)}{(4pq-2p-2q)^2}.
\]
Perfect transfer between these two **collective** pair states occurs exactly when \(p=q\), at times \(t=(2k+1)\pi/\Omega\), \(k\in\mathbb Z\). In contrast, for any individual occupied pair in the first shore and any individual occupied pair in the second shore, perfect transfer is impossible throughout \(p,q\ge3\): its maximum probability is the displayed collective maximum divided by \(\binom p2\binom q2\).

For a single straddling configuration \(|a,b\rangle\), the exact return amplitude is
\[
\langle a,b|e^{-itH}|a,b\rangle=
\frac{(p-1)(q-1)}{pq}+
\frac{\cos(\Omega t)+(p-1)\cos(\alpha t)+(q-1)\cos(\beta t)}{pq}.
\]
Its stationary zero-energy projection has squared norm \((1-1/p)(1-1/q)\). In particular, uniformly for all real times,
\[
1-|\langle a,b|e^{-itH}|a,b\rangle|^2
\le \min\!\left\{1,\frac{4(p+q-1)}{pq}\right\}.
\]
This gives an all-time, asymptotically complete *localized-pair confinement* as both shore sizes tend to infinity, at the same time that the coherent collective pair transfer is perfect on every balanced graph.

## Assumptions and scope
The graph is the finite simple unweighted biclique \(K_{p,q}\) with \(p,q\ge3\). Each basis state is a normalized occupancy configuration with exactly two particles, no double occupancy, and one hopping term of coefficient one per permitted single-particle move. Quantum dynamics is unitary \(U(t)=e^{-itH}\) in units with \(\hbar=1\). Degenerate positive eigenvalues contribute multiplicities additively; the formula concerns adjacency/hopping, **not** the Laplacian, two distinguishable noninteracting particles, a coined/Grover walk, or dissipative collision dynamics. No infinite-volume thermodynamic claim is made.

## Proof
Write \(V_A\) and \(V_B\) for shore vertex sets. Arrange the two-particle basis in three layers: \(AA=\binom{V_A}{2}\), \(AB=V_A\times V_B\), and \(BB=\binom{V_B}{2}\). All edges of the configuration graph run between the middle layer and either outer layer. Let \(C_p\) be the unsigned \(p\)-by-\(\binom p2\) vertex–edge incidence matrix of \(K_p\); similarly define \(C_q\). On the middle layer, the squared singular-value matrix of the outer-to-middle coupling is
\[
BB^{\mathsf T}=(C_pC_p^{\mathsf T})\otimes J_q+J_p\otimes(C_qC_q^{\mathsf T}),
\]
where \(B\) in this display is the rectangular coupling matrix (not the normalized quantum state \(|B\rangle\)), and \(J_r\) is the all-ones \(r\)-by-\(r\) matrix. Indeed, \(B=[C_p\otimes\mathbf1_q\ \ \mathbf1_p\otimes C_q]\). The elementary identity \(C_rC_r^{\mathsf T}=(r-2)I_r+J_r\) follows by counting the \(r-1\) edges incident to each vertex and the unique edge incident to two different vertices.

Split \(\mathbb R^p=\langle\mathbf1_p\rangle\oplus\mathbf1_p^\perp\), and similarly for \(q\). The four tensor factors simultaneously diagonalize \(BB^{\mathsf T}\): they carry respectively the eigenvalues \(\Omega^2\) with dimension one, \(\alpha^2\) with dimension \(p-1\), \(\beta^2\) with dimension \(q-1\), and zero with dimension \((p-1)(q-1)\). Since \(p,q\ge3\), all three positive eigenvalues are strictly positive. Consequently \(\operatorname{rank}B=p+q-1\). The full block Hamiltonian \(\left(\begin{smallmatrix}0&B^{\mathsf T}\\B&0\end{smallmatrix}\right)\) has each nonzero singular value with both signs and has \(N-2(p+q-1)\) zero eigenvalues, giving the stated spectrum.

A localized middle-layer state \(|a,b\rangle=e_a\otimes e_b\) has squared projection lengths \(1/(pq)\), \((p-1)/(pq)\), \((q-1)/(pq)\), and \((p-1)(q-1)/(pq)\) onto the four tensor factors respectively. On the middle layer the even powers of \(H\) are powers of \(BB^{\mathsf T}\), and all odd powers have zero middle-to-middle block. Summing the exponential series proves the cosine return formula, including its static projection.

If \(w=(p-1)(q-1)/(pq)\), then the return amplitude \(R(t)\) is real and \(0\le1-R(t)\le2(1-w)\). Unitarity gives \(|R(t)|\le1\), hence \(1-|R(t)|^2=(1-R(t))(1+R(t))\le4(1-w)\). The additional bound one is automatic. Thus the confinement bound holds at every real time without assumptions about frequency rationality.

Finally the collective subspace \(\operatorname{span}\{|A\rangle,|M\rangle,|B\rangle\}\) is invariant, and its exact Hamiltonian is the symmetric three-site path
\[
H_{\rm coll}=\begin{pmatrix}0&g_A&0\\g_A&0&g_B\\0&g_B&0\end{pmatrix},\qquad
 g_A=\sqrt{2q(p-1)},\quad g_B=\sqrt{2p(q-1)}.
\]
Its eigenvalues are \(0,\pm\Omega\), with \(\Omega^2=g_A^2+g_B^2\), and direct exponentiation gives
\[
\langle B|e^{-itH}|A\rangle=\frac{g_Ag_B}{\Omega^2}\bigl(\cos(\Omega t)-1\bigr).
\]
The maximum squared modulus is \(4g_A^2g_B^2/\Omega^4\), equal to one precisely when \(g_A=g_B\), equivalently \(p=q\); the phase condition is \(\cos(\Omega t)=-1\). Since every individual first-shore pair has identical cross-shore amplitude to every individual second-shore pair by the independent shore permutations, and the corresponding uniform vectors each have \(\binom p2\) and \(\binom q2\) components, every such matrix element equals the collective element divided by \(\sqrt{\binom p2\binom q2}\). As these binomial factors exceed one in the stated range, localized perfect cross-shore transfer never occurs. This proves all assertions.

## Verification
Run `python3 VERIFY.py` with Python 3 and SymPy installed. It independently constructs the two-particle configuration Hamiltonian from allowed single hops, compares the complete nonzero Gram spectra, checks four nonzero even return moments and four distinct-shore transition moments for each pair of integers \(3\le p,q\le7\), and verifies the two-vertex-per-shore boundary separately. Reported result: `ALL_EXACT_CHECKS_PASSED 251`. These finite checks supplement, but do not replace, the analytic all-size proof above.

## Relationship to prior work
Audenaert, Godsil, Royle and Rudolph introduced symmetric graph powers as quantum exchange Hamiltonians and developed general spectral bounds; their inspected 2005 paper does not give this exact all-parameter biclique spectrum or collective-versus-localized transfer dichotomy. Large, Underwood and Feder proved many-hard-core-boson perfect transfer for suitably weighted paths (2014); the present unweighted complete bipartite base graph and the collective-state criterion are distinct. Dalfó and collaborators (2020) established Laplacian spectral results for token graphs, including bicliques, but those are not adjacency Hamiltonians and do not determine the return amplitude or transfer formula in this nonregular two-token graph. The specialized adjacency factorization and simultaneous transport/confinement classification are the contribution evaluated here. Search-based priority assessments remain provisional.

## Limitations
There is no assertion of unpublished global uniqueness, independent validation, an experimentally observed quantum device, or an infinite-system localization phase. The confinement statement is for initially occupied opposite-shore pairs; the perfect transfer statement is for uniform pairs initially within one shore. The boundary cases where a shore has only one or two vertices are outside the main spectral classification. Special degeneracies between the nonzero frequency families are included by summing multiplicities. Earlier unindexed or non-OA calculations of exactly the same symmetric-square adjacency spectrum remain possible.

## References
- K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251v1, first submitted 2005-07-12. https://arxiv.org/abs/math/0507251
- S. J. Large, M. S. Underwood, D. L. Feder, *Perfect quantum state transfer of hard-core bosons on weighted path graphs*, arXiv:1412.1022v1, first submitted 2014-12-02. https://arxiv.org/abs/1412.1022
- C. Dalfó et al., *On the Laplacian spectra of token graphs*, arXiv:2012.00808v1, first submitted 2020-12-01. https://arxiv.org/abs/2012.00808
