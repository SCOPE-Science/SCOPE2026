# Complete balanced-cut entanglement census of the Heawood graph state

## Finding

Let \(H\) be the point–line incidence graph of the Fano plane, with seven point vertices, seven line vertices, and twenty-one edges. Prepare the pure fourteen-qubit graph state \(\lvert H\rangle\) by applying one controlled-\(Z\) gate for each edge to \(\lvert+\rangle^{\otimes14}\). For each labelled seven-vertex subset \(A\subset V(H)\), let \(S(A)\) be the von Neumann entropy (in bits) of the reduced state on \(A\).

**Theorem.** The complete balanced-cut entanglement distribution is

\[
\#\{A\subset V(H):|A|=7,\ S(A)=r\}=\begin{cases}
100,&r=4,\\980,&r=5,\\1680,&r=6,\\672,&r=7,\\0,&\text{otherwise.}
\end{cases}
\]

Each reduced state has exactly \(2^{S(A)}\) equal nonzero eigenvalues \(2^{-S(A)}\); consequently **every** positive-order Rényi entropy agrees with \(S(A)\). The mean entropy over all \(\binom{14}{7}=3432\) labelled seven-subsets is exactly \(5021/858\) bits. There are \(672\) maximally entangled oriented cuts, or \(336\) unordered bipartitions, and they cross precisely \(11\) or \(13\) graph edges, with \(336\) oriented cuts in each crossing-edge class. Conversely the point-versus-line cut crosses all \(21\) edges but has only \(4\) entanglement bits. These counts treat \(A\) and its complement as distinct subsets, even though both have the same entropy.

## Assumptions and scope

Represent points and line normals by the seven nonzero binary triples \(p,\ell\in\mathbb F_2^3\setminus\{0\}\). Incidence is \(p\cdot\ell=0\) over \(\mathbb F_2\); this defines the fourteen distinct labelled vertices and their graph. An alternative cyclic Fano presentation has line sets \(\{i,i+1,i+3\}\) modulo seven, for \(i=0,\dots,6\). The seven-subset census is exhaustive for **this** specific ideal graph state, with no quotient by graph automorphisms or point–line duality and no noise, measurements, or edge weights.

## Proof

**1. Bipartite Schmidt spectrum.** For any graph-state split \(A\sqcup B=V(H)\), let \(C=\Gamma[A,B]\) be its binary cross-adjacency matrix. Local diagonal gates on the separate registers do not affect the Schmidt spectrum, and the remaining computational-basis amplitudes are proportional to \((-1)^{a^{\mathsf T}Cb}\). Summing over \(b\) in the reduced density matrix gives

\[
\rho_A(a,a')=2^{-|A|}\,\mathbf 1_{\{C^{\mathsf T}(a+a')=0\}}
\]

up to conjugation by a diagonal local unitary. If \(r=\operatorname{rank}_{\mathbb F_2}C\), this matrix has \(2^r\) identical nonzero eigenvalues \(2^{-r}\), hence every positive-order Rényi entropy, and its von Neumann entropy, equals \(r\) bits. This standard graph-state cut-rank fact is due to Hein, Eisert and Briegel [1]; the displayed calculation fixes the normalization.

**2. Splitting the incidence matrix.** If \(A\) contains \(a\) point vertices \(P_A\) and \(7-a\) line vertices \(L_A\), then its complement has point set \(P_B\) of size \(7-a\) and line set \(L_B\) of size \(a\). After permuting row and column orders, the cut matrix is block diagonal (up to transposition of one block) with binary square blocks

\[
M[P_A,L_B],\qquad M[P_B,L_A].
\]

Therefore

\[
S(A)=\operatorname{rank}_{\mathbb F_2}M[P_A,L_B]
+\operatorname{rank}_{\mathbb F_2}M[P_B,L_A].
\]

At the canonical \(a=7\) split, \(M_{p\ell}=1+p_1\ell_1+p_2\ell_2+p_3\ell_3\) over \(\mathbb F_2\). The four functions \(1,p_1,p_2,p_3\) are independent on the seven nonzero triples, as are their line analogues, so \(\operatorname{rank}_{\mathbb F_2}M=4\). This proves the surprising four-bit entropy at the cut containing all twenty-one edges.

**3. Exhaustive finite rank census.** For each integer \(a\in\{0,\dots,7\}\), list every \(a\)-subset of seven points and every \((7-a)\)-subset of seven lines, and evaluate the two binary ranks in Step 2 by exact Gaussian elimination. This is exhaustive because

\[
\sum_{a=0}^{7}\binom{7}{a}\binom{7}{7-a}=\binom{14}{7}=3432.
\]

The exact rank counts, by the number \(a\) of point vertices in \(A\), are:

| \(a\) | \(S=4\) | \(S=5\) | \(S=6\) | \(S=7\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 |
| 1 | 28 | 21 | 0 | 0 |
| 2 | 21 | 252 | 168 | 0 |
| 3 | 0 | 217 | 672 | 336 |
| 4 | 0 | 217 | 672 | 336 |
| 5 | 21 | 252 | 168 | 0 |
| 6 | 28 | 21 | 0 | 0 |
| 7 | 1 | 0 | 0 | 0 |
| **Total** | **100** | **980** | **1680** | **672** |

The full finite calculation is specified by the standalone standard-library program `verify_blocks.py`; the independent `verify_direct.py` instead builds the fourteen-by-fourteen adjacency matrix from binary scalar products and directly eliminates all \(3432\) seven-by-seven cut matrices. Thus the finite enumeration is exhaustive and exactly reproducible; no numerical rank tolerance or sampling is used.

**4. Crossing-edge profile and average.** The direct program also counts the graph edges crossing each cut, giving exactly \(336\) rank-seven cuts with \(11\) edges and \(336\) with \(13\) edges. Both point–line orientations have \(21\) crossing edges and rank four. The exact mean is

\[
\frac{4\cdot100+5\cdot980+6\cdot1680+7\cdot672}{3432}
=\frac{5021}{858}.
\]

Steps 1–4 prove the claimed Schmidt spectra and all tabulated counts for every balanced cut.

## Verification

From a directory containing the accompanying Python 3 standard-library files, run:

```text
python3 verify_direct.py
python3 verify_blocks.py
```

Expected markers are `DIRECT_OK histogram=[(4, 100), (5, 980), (6, 1680), (7, 672)]` and `BLOCKS_OK histogram=[(4, 100), (5, 980), (6, 1680), (7, 672)]`. The first script separately checks the canonical rank, exact entropy mean, maximal-cut crossing-edge counts, graph regularity, and adjacency symmetry; the second constructs a different Fano incidence model and applies separate matrix-elimination code to the two blocks in the analytic decomposition. Neither script uses probabilistic sampling or external packages.

## Relationship to prior work

The graph-state entropy/rank correspondence and the general flat-Schmidt-spectrum mechanism are established, not claimed as new [1,2]. Existing graph-state entanglement classification data explicitly cover graphs up to twelve qubits [3], whereas the present incidence graph has fourteen. A published projective-plane matching-gate-omission result [4] derives entanglement shifts at the **fixed entire point-versus-line cut** (including its four-bit baseline at order two), whereas the present finding enumerates entanglement under **all** balanced vertex bipartitions with no gates deleted. A separate Heawood result on minimum linear arrangements and cutwidth [5] counts edge boundaries, not ranks of binary cross-adjacency matrices. The examined sources do not give the histogram or its maximal-cut crossing-edge refinement. Historical priority beyond the checked material remains open.

## Limitations

This is a complete finite fourteen-qubit balanced-cut census, not a theorem for larger projective planes or noisy graph states. The all-subset rank distribution at unequal partition sizes is not assessed. Exact finite enumeration certifies this graph only; it does not prove a general size-asymptotic formula. Historical originality has not been independently certified.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, publicly posted 18 July 2003, especially Section III.2, https://arxiv.org/abs/quant-ph/0307130 .
2. A. Cosentino and S. Severini, *Weight of quadratic forms and graph states*, arXiv:0906.2488, publicly posted 13 June 2009, https://arxiv.org/abs/0906.2488 .
3. A. Cabello, L. E. Danielsen, A. J. López-Tarrida and J. R. Portillo, *Database of Entanglement in Graph States*, online introduction identifying the twelve-qubit scope, https://www.codetables.de/larsed/entanglement/ .
4. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes*, public scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768 .
5. *All optimal linear arrangements of the Heawood graph*, public scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-optimal-linear-arrangements-of-the-heawood-graph--dc3e824375f5 .
