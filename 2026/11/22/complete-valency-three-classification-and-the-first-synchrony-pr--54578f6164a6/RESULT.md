# Complete valency-three classification and the first synchrony-primitive four-cell zero-Hopf networks

## Finding
For a connected regular four-cell directed multigraph of input valency three, let \(A\) be its nonnegative integer adjacency matrix with every row sum equal to \(3\). Call the network *zero-Hopf* when its adjacency spectrum consists of four simple numbers \(3,0,i\omega,-i\omega\) with \(\omega>0\). Up to simultaneous row-and-column permutation, there are **exactly 109** such networks. Their complete spectrum and robust synchrony classification are:

| \(\omega^2\) | Labeled adjacency matrices | Nonisomorphic networks | No proper synchrony | Exactly one | Exactly two |
|---:|---:|---:|---:|---:|---:|
| \(1\) | 1560 | 65 | 0 | 47 | 18 |
| \(2\) | 840 | 36 | 1 | 27 | 8 |
| \(3\) | 176 | 8 | 2 | 5 | 1 |
| Total | 2576 | 109 | **3** | 79 | 27 |

A *proper synchrony* here means a coordinate-equality polydiagonal of dimension two or three invariant for every smooth admissible input-symmetric coupled-cell vector field; the always-present full synchrony and the whole state space are excluded. In particular, **exactly three** nonisomorphic valency-three networks have no proper robust synchrony, represented by

\[
A_{2}=\begin{pmatrix}0&0&1&2\\1&1&0&1\\1&1&1&0\\0&0&2&1\end{pmatrix},\qquad
A_{3a}=\begin{pmatrix}0&0&0&3\\1&1&0&1\\1&1&1&0\\0&0&2&1\end{pmatrix},\qquad
A_{3b}=\begin{pmatrix}0&0&1&2\\2&1&0&0\\0&2&1&0\\0&1&1&1\end{pmatrix}.
\]

Their respective values of \(\omega^2\) are \(2,3,3\). Combining this classification with the established nonexistence at valency one and the absence of synchrony-primitive networks at valency two gives **three as the minimum input valency** for a synchrony-primitive four-cell zero-Hopf network.

## Assumptions and scope
Networks are directed multigraphs on four cells, allowing repeated edges and loops. An entry \(A_{ij}\) is the nonnegative integer multiplicity of edges entering cell \(i\) from cell \(j\); every row sums to three. Connected means that the underlying undirected graph is connected. Isomorphism means simultaneous permutation of the four cell labels (not arbitrary row permutations independently of columns). The spectral condition is exact, with simple algebraic eigenvalues \(3,0,\pm i\omega\). A partition \(\mathcal P\) gives robust synchrony precisely when for every pair \(i,j\) in one block \(B\) and every block \(C\), the equality \(\sum_{\ell\in C}A_{i\ell}=\sum_{\ell\in C}A_{j\ell}\) holds. Only the thirteen nontrivial partitions of four cells are tested.

## Proof
**Spectrum reduction.** Since every row sum is three, \(3\) is an eigenvalue. For a four-cell zero-Hopf matrix its characteristic polynomial is
\[
\det(tI-A)=t(t-3)(t^2+q)=t^4-3t^3+qt^2-3qt,\qquad q=\omega^2>0.
\]
The coefficient of \(t^2\), a sum of integer principal minors, shows \(q\) must be a positive integer. Newton identities give the necessary and sufficient exact conditions
\[
\operatorname{tr}A=3,\qquad \operatorname{tr}(A^2)=9-2q,\qquad
\operatorname{tr}(A^3)=27,\qquad \det A=0.
\]
They are sufficient because the first three power sums and determinant determine the four characteristic coefficients. Moreover \(\operatorname{tr}(A^2)=\sum_i A_{ii}^2+2\sum_{i<j}A_{ij}A_{ji}\geq\sum_i A_{ii}^2\geq3\): four nonnegative integers with sum three have sum of squares at least three. Hence \(q\leq3\). No other positive squared imaginary frequency can occur.

**Exhaustive finite classification.** A length-four nonnegative integer vector with sum three has exactly \(\binom63=20\) possibilities. Therefore exactly \(20^4=160000\) labeled matrices satisfy the row-sum constraint. The included `verify_census.py` examines every one by an integer-only trace/determinant predicate, connectedness of the underlying graph, and the equivalent principal-minor coefficients. For each survivor it selects the lexicographically smallest row-major matrix under the \(4!=24\) simultaneous cell permutations. This gives respectively 65, 36, and 8 distinct canonical representatives for \(q=1,2,3\), alongside the labeled counts in the table. Burnside's fixed-incidence sums, calculated separately from the number of distinct canonical representatives, are respectively 1560, 864, and 192, exactly 24 times the three class counts. All 109 representatives are explicitly recorded in `canonical_representatives.csv`.

**Synchrony test.** The balanced-input criterion is both sufficient and necessary for *robust* synchrony: on a polydiagonal, each admissible input-symmetric coupling receives the same self-state for cells in a block and receives identical multisets of other-block states exactly when all blockwise incoming multiplicities match. If a blockwise multiplicity differs, choose the common smooth coupling to be a sum of one-variable interpolation functions that isolates that input-block value; the two cells then have unequal derivatives at a state with distinct values across blocks, disproving invariance for every admissible field. Every set partition of the four cells is uniquely represented by a restricted-growth word, yielding fifteen partitions in total. Discarding the one-block and the four-singleton partitions leaves thirteen. For each canonical representative, the balanced-input-sums criterion in the assumptions is checked over every remaining partition using exact integers. The counts of admissible proper partitions are \((0,1,2)\) with distributions \((0,47,18)\), \((1,27,8)\), and \((2,5,1)\) at \(q=1,2,3\) respectively. No third or greater count arises. The three displayed matrices are precisely the canonical representatives with zero proper balanced partitions. Since canonicalization preserves the partition condition, this settles the nonisomorphic classification. Valency one cannot support a four-cell zero-Hopf network and the nine valency-two connected cases all have a proper synchrony space by the initiating paper; the three valency-three examples therefore establish the claimed minimal valency.

## Verification
Run `python3 verify_census.py` in the directory containing the included standalone script. It uses only the Python standard library and deterministically rewrites `canonical_representatives.csv`. It asserts the total labeled input count, the complete spectrum-conditioned labeled and orbit counts, two distinct characteristic-coefficient formulae on accepted matrices, independent Burnside incidence checks, and all three synchrony distributions. An additional exact symbolic characteristic-polynomial check of every one of the 109 canonical matrices, using SymPy outside the standalone package, also passed. These computational facts are exhaustive finite checks, not sample-based extrapolations. The file `canonical_representatives.csv` is the complete sorted list of class representatives, including each frequency and proper-synchrony count.

## Relationship to prior work
Aguiar, Dias and Mokhtari's *Zero-Hopf networks* (first public version 11 November 2026) introduces this network class, develops its general four-cell synchrony-lattice possibilities, and classifies the nine connected **valency-two** cases. Its general results do not tabulate the valency-three classes, their squared imaginary frequencies, or the precise number of synchrony-primitive networks at odd valency three. The three valency-three representatives also do not follow from the paper's explicit even-valency scaling family. The present classification retains the original definition of network isomorphism and robust input-symmetric synchrony. It is an exact finite extension, not a new normal-form or nonlinear bifurcation theorem.

## Limitations
The table covers precisely four cells and valency three, with loops and multiplicities allowed. It does not classify higher valencies, larger cell counts, formal normal forms, or nonlinear zero-Hopf unfolding dynamics. It also does not assert that different network isomorphism classes give different nonlinear bifurcation scenarios. Priority remains subject to specialized earlier coupled-cell catalogues not known to be fully searchable. The numerical counts are supported by exhaustive executable integer enumeration rather than a short closed-form orbit-count identity.

## References
1. M. Aguiar, A. Dias and F. Mokhtari, *Zero-Hopf networks*, arXiv:2611.15221v1, 11 November 2026, https://arxiv.org/html/2611.15221v1. Sections 2–5 and 7: definitions, balanced partitions, general four-cell synchrony, and valency-two classification.
2. M. Golubitsky and R. Lauterbach, work on center eigenspaces and codimension-one bifurcations of coupled-cell networks, as cited and discussed in Reference 1; invoked only for historical context, not as an unverified premise of the finite classification.
