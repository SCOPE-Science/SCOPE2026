# The five-cell onset and complete synchrony-profile census for two-input zero-Hopf networks

## Finding

Consider connected regular directed networks on five labelled cells with one edge type, exactly two incoming arrows at every cell, and loops and parallel arrows permitted. Impose the zero-Hopf spectral condition: the adjacency matrix has simple eigenvalues \(2\), \(0\), and \(\pm i\omega\), with \(\omega>0\), and no other imaginary-axis eigenvalues. An admissible one-dimensional coupled-cell vector field uses the same smooth function of the cell state and its unordered pair of inputs at every site.

For each network, let \(b(G)\) be the number of proper nontrivial synchrony polydiagonals, i.e. invariant coordinate-equality subspaces strictly larger than full synchrony and strictly smaller than the entire phase space. The complete distribution of \(b(G)\), counting networks up to simultaneous relabelling of all five cells, is

| \(b(G)\) | All connected classes | Strongly connected classes |
|---|---:|---:|
| 0 | 2 | 2 |
| 1 | 12 | 6 |
| 2 | 59 | 22 |
| 3 | 40 | 16 |
| 4 | 59 | 8 |
| 5 | 4 | 1 |
| 6 | 15 | 1 |
| **Total** | **191** | **56** |

Thus precisely **two** connected isomorphism classes are *synchrony-primitive*: they have no proper nontrivial synchrony polydiagonals. Both are strongly connected, have trivial graph automorphism group, and have characteristic polynomial
\[
\chi_A(t)=t(t-2)(t+1)(t^2+1).
\]
Canonical representatives of the two classes (rows indexed by receiving cell and columns by input source) are
\[
A_1=\begin{pmatrix}
0&0&0&0&2\\
0&0&0&1&1\\
1&0&1&0&0\\
0&1&1&0&0\\
0&0&0&2&0
\end{pmatrix},\qquad
A_2=\begin{pmatrix}
0&0&0&0&2\\
0&0&1&1&0\\
1&0&1&0&0\\
1&1&0&0&0\\
0&1&0&1&0
\end{pmatrix}.
\]

This is the **first possible cell count** for synchrony-primitive two-input zero-Hopf networks: under the same simple-spectrum condition, four cells are the minimum for zero-Hopf networks and none of the nine four-cell connected classes is synchrony-primitive. The four-cell exclusion is established in the motivating paper and independently checked here; it is not a new discovery.

## Assumptions and scope

An adjacency matrix \(A=(a_{ij})\) has entries in \(\{0,1,2\}\), and every row sums to two; \(a_{ij}\) counts directed arrows from cell \(j\) into cell \(i\). Connectivity means weak connectivity of this directed multigraph, while strong connectivity requires directed reachability in both directions between every pair. Equivalent networks are related by simultaneous row/column permutation.

A partition \(\pi\) of the cells is *balanced* when every pair \(i,j\) in the same partition block receives an equal total number of arrows from each partition block \(B\):
\[
\sum_{k\in B}a_{ik}=\sum_{k\in B}a_{jk}.
\]
This condition is equivalent to invariance of its coordinate-equality subspace under every smooth input-symmetric admissible vector field. The one-block partition (full synchrony) and all-singletons partition (full phase space) are always balanced and are excluded from \(b(G)\).

No assertions are made about all smooth-network normal forms, nonlinear bifurcation existence for every coupling function, or the absence of invariant linear subspaces other than polydiagonals.

## Proof

**Step 1: exhaustive finite universe and exact spectral filter.** There are \(\binom{6}{2}=15\) possible rows with nonnegative integer entries summing to two. Hence precisely \(15^5=759375\) labelled five-cell adjacency matrices exist. For each matrix, compute the integer traces \(s_j=\operatorname{tr}(A^j)\) for \(j=1,2,3,4\), and the determinant, using only integer arithmetic.

For a five-cell zero-Hopf matrix, the nontrivial fifth eigenvalue must be real, say \(r\), and the imaginary pair must be \(\pm i\sqrt c\), with \(c>0\). Because \(A\) has integral characteristic polynomial, \(r=s_1-2\) and \(c=(4+r^2-s_2)/2\) are integers. The required simple-spectrum characteristic polynomial is
\[
(t-2)t(t-r)(t^2+c),\qquad r\notin\{0,2\},\quad c\in\mathbb Z_{>0}.
\]
It is equivalent to the six elementary tests
\[
\begin{aligned}
r&=s_1-2\notin\{0,2\},\\
2c&=4+r^2-s_2>0\ \text{and even},\\
s_3&=8+r^3,\\
s_4&=16+r^4+2c^2,\\
\det A&=0.
\end{aligned}
\]
This equivalence follows from Newton's identities: four power sums determine the first four characteristic coefficients, and zero determinant fixes the constant coefficient. Row sums ensure \(2\) is an eigenvalue. Thus the exact filter is both necessary and sufficient and does not rely on numerical eigenvalue tolerances.

**Step 2: quotient by relabelling.** Reject matrices whose underlying undirected graph is disconnected. Enumerate all \(5!\) permutations of the cells; choose the lexicographically least simultaneous row-and-column permutation as the canonical representative. The resulting exact classes number \(191\), comprising \(21960\) labelled matrices; \(56\) classes are strongly connected. The provided representative file lists each canonical matrix. A separate direct enumeration of all \(759375\) input matrices agrees with the sums of the representatives' orbit sizes, so the class list exhausts the universe. The underlying 191-class spectral census is an earlier result; here it serves as independently rechecked input to the new synchrony classification.

**Step 3: synchrony spaces.** The restricted-growth-string recursion lists all \(B_5=52\) partitions of five cells exactly once. For every canonical representative, apply the balancedness criterion to each of these partitions; subtract the two trivial ones. The frequencies yield the displayed distribution. Direct directed reachability tests give the third column. In the zero-balanced-partition subcollection, precisely the two displayed matrices remain, and direct permutation tests show each has automorphism group of order one.

**Step 4: sharp onset.** A simple zero-Hopf spectrum requires at least the four distinct eigenvalues \(2,0,\pm i\omega\); therefore fewer than four cells cannot qualify. The corresponding exhaustive four-cell verification yields nine connected two-input zero-Hopf isomorphism classes, and every one has a nontrivial balanced partition, agreeing with Aguiar--Dias--Mokhtari's four-cell synchrony theorem. The two five-cell representatives prove existence at the next size. This proves sharpness.

## Verification

The self-contained files `verify_synchrony.py`, `five_cell_representatives.json`, and `four_cell_representatives.json` jointly reproduce the exact finite proof. Run `python3 verify_synchrony.py` from the directory containing these files. Only the Python standard library is required.

The checker verifies all \(759375\) five-cell row-sum-two matrices with exact integer traces/determinants, the \(191\) canonical classes and their orbit-size sum, the \(56\) strongly connected classes, all \(52\) partitions per class, the synchrony-frequency table, the precise two primitive matrices, and the four-cell exclusion. A finite exhaustive verification is sufficient here because the theorem's domain is exactly the finite class of five-cell matrices (with the four-cell comparison).

## Relationship to prior work

Aguiar, Dias and Mokhtari introduce the zero-Hopf network setting and fully classify connected four-cell valency-two networks, including their synchrony lattice options; their Theorem 10 excludes four-cell valency-two networks with no nontrivial synchrony space. Their work does not classify five-cell synchrony profiles. A prior complete five-cell **spectral** enumeration supplies the total of 191 classes, the 56 strongly connected count and their spectral multiplicities; none of those numerical spectral totals is proposed as new here. The new assertion is the complete balanced-partition distribution and the sharp identification of exactly two synchrony-primitive five-cell classes.

## Limitations

The result is finite and restricted to one edge type, valency two, five cells (and the four-cell minimality comparison), with loops and multiple arrows allowed. Other network conventions, especially coloured or individually distinguished inputs, have different notions of balanced partitions. The existence of a network with an appropriate spectrum does not by itself establish a nonlinear zero-Hopf bifurcation for every admissible vector field. Search-based novelty checks cannot rule out uncatalogued earlier enumerations; independent review has not been performed.

## References

1. M. Aguiar, A. Dias, F. Mokhtari, *Zero-Hopf networks*, arXiv:2611.15221v1, first public version 11 November 2026. https://arxiv.org/html/2611.15221v1
2. M. Aguiar, A. Dias, M. Golubitsky, M. Leite, *Bifurcations from regular quotient networks: A first insight*, 2009. Its quotient-network framework is background for the balanced-partition viewpoint; no five-cell enumeration from this article is asserted.
