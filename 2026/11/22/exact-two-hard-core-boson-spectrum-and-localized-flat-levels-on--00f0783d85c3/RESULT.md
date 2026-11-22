# Exact two-hard-core-boson spectrum and localized flat levels on friendship quantum networks

## Finding

For every integer \(m\geq3\), let \(F_m=K_1\vee(mK_2)\) be the friendship graph consisting of \(m\) triangles sharing one hub. Put two identical hard-core bosons on its \(2m+1\) sites, with real unit hopping on every graph edge and no on-site or density–density potential. In the orthonormal basis of unordered occupied pairs, the Hamiltonian \(H_m\) moves one occupied site to an unoccupied adjacent site with matrix element one. Its dimension is \(d_m=\binom{2m+1}{2}=m(2m+1)\).

The **complete characteristic polynomial**, with algebraic multiplicities, is
\[
\begin{aligned}
\det(\lambda I-H_m)={}&(\lambda+2)^{\binom m2}\lambda^{m(m-2)}(\lambda-2)^{m(m-3)/2}\\
&\cdot(\lambda^2+\lambda-2m+2)^m\\
&\cdot(\lambda^3-3\lambda^2+(4-2m)\lambda+4)^{m-1}\\
&\cdot(\lambda^3-3\lambda^2+(4-4m)\lambda+4).
\end{aligned}
\]

In particular at least \(d_m-5m\) eigenvectors lie in the fixed-energy subspaces \(-2,0,2\); compactly supported eigenvectors occur at all three energies when \(m\ge4\), while the fixed \(2\)-energy sector is absent for \(m=3\). If \(\mu_m=d_m^{-1}\sum_{j=1}^{d_m}\delta_{\lambda_j(H_m)}\) is the normalized eigenvalue-counting measure, then
\[
\mu_m\Longrightarrow\tfrac14\delta_{-2}+\tfrac12\delta_0+\tfrac14\delta_2
\qquad(m\to\infty).
\]
No claim is made that the remaining \(5m\) levels are pairwise distinct or avoid the three fixed energies; accidental eigenvalue coincidences are already accounted for by the polynomial.

## Assumptions and scope

The sites are a hub \(h\) and \((i,\sigma)\), \(1\le i\le m\), \(\sigma\in\{0,1\}\). Edges are \(h\!\sim\!(i,0)\), \(h\!\sim\!(i,1)\), and \((i,0)\!\sim\!(i,1)\), for every \(i\), with no further edges. Exactly two bosons occupy distinct sites. There are no double occupancies, diagonal energies, or magnetic phases; the hopping amplitude is one. Reversing the overall hopping sign reflects the stated spectrum. A physical hopping strength \(J>0\) multiplies every displayed energy by \(J\).

For occupied pairs \(S,T\subset V(F_m)\) with \(|S|=|T|=2\), set \((H_m)_{S,T}=1\) exactly when \(S\triangle T\) is one edge and zero otherwise. This convention removes any ambiguity about bosonic normalization.

## Proof

**1. Separate the local petal reflections.** Set \(X_{i,\sigma}=|\{h,(i,\sigma)\}\rangle\), \(Y_i=|\{(i,0),(i,1)\}\rangle\), and \(Z_{ij}^{\sigma\tau}=|\{(i,\sigma),(j,\tau)\}\rangle\) for \(i<j\). Let
\[
u_i=\frac{X_{i,0}+X_{i,1}}{\sqrt2},\qquad
v_i=\frac{X_{i,0}-X_{i,1}}{\sqrt2}.
\]
On each four-dimensional cross-petal space, Fourier-transform the two binary leaf labels, giving normalized orthogonal vectors \(W_{ij}^{++},W_{ij}^{-+},W_{ij}^{+-},W_{ij}^{--}\), where \(+\) denotes the normalized sum and \(-\) the normalized difference. The two independent leaf-swap operations act on that space with energies \(2,0,0,-2\).

The \(\binom m2\) vectors \(W_{ij}^{--}\) do not couple to hub-occupied states, because summation over either antisymmetric leaf label vanishes. They are eigenvectors with eigenvalue \(-2\), proving the first factor.

**2. The antisymmetric one-petal sectors.** For each fixed \(i\), the vector \(v_i\) has diagonal matrix element \(-1\) and couples with amplitude \(\sqrt2\) to each of the \(m-1\) cross-petal modes antisymmetric at petal \(i\) and symmetric at the other petal. Every such cross-petal mode has diagonal element zero. The normalized sum couples to \(v_i\) with amplitude \(\sqrt{2(m-1)}\), giving the block
\[
\begin{pmatrix}-1&\sqrt{2(m-1)}\\ \sqrt{2(m-1)}&0\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^2+\lambda-2m+2\). Its \(m-2\) orthogonal cross-petal contrasts have eigenvalue zero. Distinct choices of \(i\) are orthogonal invariant sectors. Consequently the full antisymmetric contribution is \((\lambda^2+\lambda-2m+2)^m\lambda^{m(m-2)}\).

**3. The symmetric sectors and unsigned incidence matrix.** In the orthonormal bases of \(u_i,Y_i,W_{ij}^{++}\), let \(B\) be the \(m\times\binom m2\) unsigned vertex–edge incidence matrix of \(K_m\): \(B_{i,\{r,s\}}=1\) when \(i\in\{r,s\}\). The remaining block is exactly
\[
H_+=\begin{pmatrix}I_m&\sqrt2I_m&\sqrt2B\\\sqrt2I_m&0&0\\\sqrt2B^{\mathsf T}&0&2I_{\binom m2}\end{pmatrix}.
\]
For \(m\ge3\), \(BB^{\mathsf T}=(m-2)I_m+\mathbf1\mathbf1^{\mathsf T}\) is positive definite. Its eigenvalues are \(2(m-1)\) on the all-ones line and \(m-2\) on the orthogonal standard space. Thus \(\ker B\) has dimension \(\binom m2-m=m(m-3)/2\) and yields eigenvalue \(2\).

On each of the \(m-1\) standard directions, the three-by-three matrix, with coordinates \((u,Y,W)\), is
\[
\begin{pmatrix}1&\sqrt2&\sqrt{2(m-2)}\\\sqrt2&0&0\\\sqrt{2(m-2)}&0&2\end{pmatrix},
\]
with characteristic polynomial \(\lambda^3-3\lambda^2+(4-2m)\lambda+4\). On the all-ones direction the coupling to the cross-petal incidence modes is \(2\sqrt{m-1}\), giving
\[
\begin{pmatrix}1&\sqrt2&2\sqrt{m-1}\\\sqrt2&0&0\\2\sqrt{m-1}&0&2\end{pmatrix}
\]
and characteristic polynomial \(\lambda^3-3\lambda^2+(4-4m)\lambda+4\). All displayed blocks are real symmetric. Their orthogonal direct sum exhausts the dimension \(m(2m+1)\), proving the asserted factorization for all \(m\ge3\).

**4. Compact eigenstates and limiting measure.** Each \(W_{ij}^{--}\) is supported on four two-particle configurations and has energy \(-2\). In a fixed petal \(i\), the difference of two distinct cross-petal modes antisymmetric at \(i\) and symmetric at the other petals is a zero-energy eigenvector supported on eight configurations. For \(m\ge4\), an alternating four-cycle in the edge set of \(K_m\) belongs to \(\ker B\); its linear combination of four \(W^{++}\) vectors is a compact eigenvector of energy \(2\). The dimensions of these three fixed-energy sectors are respectively \(\binom m2\), \(m(m-2)\), and \(m(m-3)/2\). All other blocks together have dimension exactly \(5m\), so their normalized spectral mass vanishes as \(m\to\infty\). Dividing the fixed-sector dimensions by \(m(2m+1)\) yields \(1/4,1/2,1/4\), which proves weak convergence against every bounded continuous test function.

## Verification

The standalone script `VERIFY.py` constructs the Hamiltonian independently from the adjacency lists of the \(2m+1\) base graph and the unordered-pair exclusion rule. It computes its exact integer characteristic polynomial using SymPy and compares that polynomial, coefficient for coefficient, to the asserted closed factorization for every \(m\in\{3,4,5,6,7\}\), with matrix sizes \(21,36,55,78,105\). All five tests pass. The script contains no precomputed eigenvalue tables. This finite check is a safeguard; the general theorem follows from the invariant-space calculation above.

## Relationship to prior work

Audenaert–Godsil–Royle–Rudolph (2005, arXiv:math/0507251) define symmetric powers of graphs and identify their quantum exchange-Hamiltonian meaning. Their general construction includes the present hard-core two-particle Hamiltonian, but their studied families and general spectral bounds do not state the above friendship-family factorization or the three extensive compact-mode dimensions.

Cioabă–Haemers–Vermette–Wong (2013, arXiv:1310.6529) determine the **single-particle** adjacency spectrum and spectral determination of friendship graphs. The two-excitation hard-core operator is not the one-particle adjacency matrix, and its spectrum is not obtained by simply adding two one-particle energies on this network with cycles.

A closely related published calculation, *Integral Laplacian spectrum and spanning-tree complexity of two-token friendship graphs* (2026, published-finding corpus record c081d2602b88), determines the entire **combinatorial Laplacian** spectrum of exactly the same two-token graph. Its full proof was examined, including the hub/pair incidence decomposition and degree analysis. It does not determine the **adjacency** characteristic polynomial treated here: the two-token graph is nonregular, with vertex degrees 2, 4, and \(2m\), so \(L=D-H_m\) is not a constant spectral shift. In particular, an integral Laplacian spectrum does not imply the three distinct cubic/quadratic factors, fixed adjacency energy levels, or asymptotic level-counting measure above. The common incidence-matrix strategy and underlying two-token graph are explicitly prior work; the diagonalization of the hopping operator and its flat-state conclusion are the distinct claim.

Large–Underwood–Feder (2014, arXiv:1412.1022) give the hard-core many-boson construction and exact perfect-state-transfer results **on weighted paths**. The path-specific Tonks–Girardeau reduction does not apply to the cyclic friendship graph. Reyes–Dalfó–Fiol (2023, arXiv:2310.16929) investigate general token-graph spectral relations and walk-/distance-regular cases; friendship graphs with \(m\ge2\) are neither regular nor covered by an explicitly evaluated family in the accessible material. The present result is an explicit new calculation rather than a claim of inventing the token-graph framework.

## Limitations

The claim is restricted to exactly two hard-core excitations, uniform real hopping, and ideal finite friendship graphs with \(m\ge3\). It does not establish entanglement measures, finite-time transport bounds, robustness to edge disorder, or spectra for three or more excitations. The empirical eigenvalue measure counts levels with multiplicity, not local spectral weights for an arbitrary initial state. Unlocated earlier equivalent computations cannot be ruled out solely by literature search; independent scholarly validation has not been performed.

## References

1. K. Audenaert, C. Godsil, G. Royle, and T. Rudolph, *Symmetric Squares of Graphs*, first public version 2005-07-12, https://arxiv.org/abs/math/0507251 (journal version: J. Combin. Theory B 97 (2007) 74–90).
2. S. M. Cioabă, W. H. Haemers, J. Vermette, and W. Wong, *The graphs with all but two eigenvalues equal to ±1*, first public version 2013-10-24, https://arxiv.org/abs/1310.6529.
3. S. J. Large, M. S. Underwood, and D. L. Feder, *Perfect quantum state transfer of hard-core bosons on weighted path graphs*, first public version 2014-12-02, https://arxiv.org/abs/1412.1022.
4. M. A. Reyes, C. Dalfó, and M. A. Fiol, *On the spectra and spectral radii of token graphs*, first public version 2023-10-25, https://arxiv.org/abs/2310.16929.
5. *Integral Laplacian spectrum and spanning-tree complexity of two-token friendship graphs*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-laplacian-spectrum-and-spanning-tree-complexity-of-two--c081d2602b88
