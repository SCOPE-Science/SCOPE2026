# Deterministic logspace recognition of Green-geodesic languages of free inverse monoids

## Finding

**Theorem.** Fix a finite alphabet \(X\) and the standard inverse-monoid generating alphabet \(\widetilde X=X\sqcup X^{-1}\). For the free inverse monoid \(\operatorname{FIM}(X)\), each of its Green-representative languages \(\mathcal D\text{-Geo}\), \(\mathcal R\text{-Geo}\), and \(\mathcal L\text{-Geo}\) is decidable by a deterministic Turing machine using \(O(\log(n+2))\) work-tape cells on an input word of length \(n\). In particular all three languages are deterministic polynomial-time, deterministic linear-space, and context-sensitive. For \(|X|\ge2\), combining this upper bound with the known lower bounds yields languages that are context-sensitive yet neither context-free nor co-context-free.

A concrete decision criterion is as follows. Write the word as \(w=s_1\cdots s_n\), let \(p_i\) be the value in the free group \(F(X)\) of the prefix of length \(i\), and set \(V=\{p_0,\ldots,p_n\}\), \(E=|V|-1\), \(\alpha=p_0=1\), and \(\beta=p_n\). Let \(d\) be the distance in the Cayley tree of \(F(X)\) (equivalently the freely reduced length of a word connecting the two vertices). Define

\[
\Delta=\max_{0\le i,j\le n}d(p_i,p_j),\quad
\epsilon_\alpha=\max_i d(\alpha,p_i),\quad
\epsilon_\beta=\max_i d(\beta,p_i).
\]

The following identities hold, with no hypothesis that the input itself is geodesic:

\[
\begin{aligned}
w\in\mathcal D\text{-Geo}&\iff n=2E-\Delta,\\
w\in\mathcal R\text{-Geo}&\iff n=2E-\epsilon_\alpha,\\
w\in\mathcal L\text{-Geo}&\iff n=2E-\epsilon_\beta.
\end{aligned}
\]

The metric description of these Green classes comes from Bodart–Carvalho–Monteiro [1]; the new result is a uniform logarithmic-space evaluation of all the quantities, via parity of edge traversals and logarithmic-space free-group equality.

## Assumptions and scope

The alphabet \(X\) is **fixed and finite**, so its size and the matrices representing its generators may be hardwired into the algorithm. Input size is the length of a word in \(\widetilde X^*\), including the empty word. The complexity claim is deterministic \(O(\log(n+2))\) auxiliary space on a read-only two-way input tape; it does **not** assert a uniform logarithmic-space bound when \(X\) is itself presented as part of the input. No restriction on rank beyond finiteness is needed for the upper bound. The context-free lower bounds used in the strict-separation conclusion require \(|X|\ge2\).

The Munn tree \(T(w)\) is the minimal connected subtree of the free-group Cayley graph containing all the prefix vertices \(p_i\). Every edge traversed by the input prefix walk belongs to this tree, and each tree edge appears in that walk. Thus \(|E(T)|=|V|-1\).

## Proof

**1. Minimal tours in the Munn tree.** Let \(T\) be any finite tree with \(E\) edges, with chosen start and finish vertices \(u,v\). Any edge on the simple path \([u,v]\) must be crossed an odd number of times, hence at least once; any edge outside this path must be crossed an even number of times, hence at least twice if the walk visits the whole tree. Therefore every visiting walk has length at least \(2E-d(u,v)\). Doubling all edges outside \([u,v]\) gives a connected multigraph with precisely two odd-degree vertices \(u,v\) (or a circuit when they coincide). An Euler walk traverses the original tree completely with exactly this length. Consequently the minimum length with fixed endpoints is **exactly** \(2E-d(u,v)\). Green \(\mathcal D\), \(\mathcal R\), and \(\mathcal L\) classes of free-inverse-monoid elements are described by unrooted Munn trees, Munn trees with initial root fixed, and Munn trees with final root fixed, respectively [1, Sections 2 and 4]. Optimizing the endpoint distance over the permitted choices gives the three displayed criteria, for arbitrary input words.

**2. Prefix group equality in logarithmic space.** Lipton and Zalcstein [2] proved that the word problem for every fixed finite-rank free group is in deterministic logspace. For completeness, one can use Sanov's faithful matrices \(A=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)\), \(B=\bigl(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\bigr)\) and send distinct free generators to distinct fixed conjugates \(A^iBA^{-i}\), which freely generate a subgroup. For each word of input-length \(O(n)\), the absolute values of matrix entries differ from those of the identity by at most \(C^{O(n)}\) for a constant \(C\) depending only on \(X\). Test the product modulo every integer \(2\le m\le cn\), where the constant \(c\) is sufficiently large. The elementary inequality \(\operatorname{lcm}(1,\ldots,N)\ge 2^{N-1}\) ensures that a nonzero bounded integer cannot be divisible by all these moduli. Each modular product uses just four \(O(\log n)\)-bit integers and an \(O(\log n)\)-bit modulus counter. This is an explicit logspace equality test for any pair of prefix values \(p_i,p_j\), by testing their quotient; it can also test equality of any two freely represented vertices. The empty input is handled separately.

**3. Counting vertices in logspace.** There are \(n+1\) prefix indices. Iterate \(i=0,\ldots,n\), and increment a binary counter only if \(p_i\) is different from every \(p_j\) with \(j<i\). Equality is decided by step 2, rerunning the input as often as necessary. The number of increments is \(|V|\). The loop indices, counter, and group-equality subroutine use \(O(\log(n+2))\) auxiliary cells. Hence \(E=|V|-1\) is computable within that space.

**4. Distances in logspace, without storing reduced words.** Fix two prefix indices \(i\le j\). The segment \(s_{i+1}\cdots s_j\) is a walk from \(p_i\) to \(p_j\) in the free-group Cayley **tree**. For each \(r\in\{i+1,\ldots,j\}\), let \(e_r=\{p_{r-1},p_r\}\) be the undirected edge traversed. Two such edges are equal exactly when their unordered endpoint pairs are equal in \(F(X)\), a logspace test by step 2. Enumerate the first occurrence of every distinct edge, count its occurrences in this segment modulo two, and increment a distance counter if and only if the parity is odd. Removing a tree edge separates the tree into two components; a walk crosses the resulting cut an odd number of times exactly when its endpoints lie in different components. Thus the parity is odd precisely for the edges of the unique simple path from \(p_i\) to \(p_j\). The counter is **exactly** \(d(p_i,p_j)\), which is at most \(n\). Only a constant number of \(O(\log(n+2))\)-bit indices, a parity bit, and the step-2 subroutine are held at any time.

**5. Maximum distances and decision.** Loop over all pairs of prefix indices, invoking step 4 and maintaining a maximum in an \(O(\log(n+2))\)-bit counter to compute \(\Delta\). Restrict the first or second index to \(0\) or \(n\) to obtain \(\epsilon_\alpha\) and \(\epsilon_\beta\). Evaluate the three integer equalities in the finding. All loops are polynomially bounded and reuse the same logarithmic workspace. This proves deterministic logspace recognition for all three languages. For \(|X|\ge2\), the previously proved non-context-free and non-co-context-free results of [1, Theorems 7.1, 7.2, 8.1, 8.2] give the final strict separation.

## Verification

An exact Python checker (`verify.py`) independently enumerated every word of length at most seven over \(\{a,a^{-1},b,b^{-1}\}\), a total of 21,845 inputs. It classified four Green equivalence relations via canonical Munn-tree data and exhaustively compared the shortest observed representative in each class with the four metric minima. There were 87,380 resulting class/length comparisons. Every comparison matched. A separate kernel checked 26,093 pairs of visited prefix vertices over every word of length at most five, independently testing modular-matrix free-group equality and the parity-of-edges distance against direct free reduction. Every test passed. The replay output is in `verification_output.txt`. The finite tests are corroboration, not a proof of unbounded-length correctness; the proof is the five-step argument above.

## Relationship to prior work

Bodart, Carvalho, and Monteiro [1] introduced the three Green-geodesic languages, proved their Munn-tree characterizations, established that they are neither context-free nor co-context-free in rank at least two, and explicitly asked whether these languages are context-sensitive (Section 11, question 1). **Those metric characterizations and the lower bounds are prior results, not new claims here.** The new assertion is that the unrooted/rooted Munn-tree metric optimization can in fact be carried out in **deterministic logarithmic space**, using edge-class parity without materializing the tree. The 1977 theorem of Lipton–Zalcstein [2] gives free-group equality in logspace, but does not discuss free inverse monoids or Green-geodesic languages. Brough–Johnson–Kambites–Nyberg-Brodda [3] proved a co-context-free *word problem*, a different language problem. Searches identified no earlier explicit logarithmic-space classification of these Green-geodesic languages. The proof is a short synthesis of established ingredients, and there remains a priority risk of an implicit earlier algorithmic observation.

## Limitations

The result is for the **standard** finite generating set and fixed rank; language complexity for arbitrary alternative generating sets is not determined. It does not establish context-freeness, indexed-language membership, optimality of the logarithmic-space bound, or the complexity of conjugacy-representative languages. The parity step specifically uses the fact that the universal Cayley graph of a free group is a **tree**. The finite verification cannot independently certify historical originality or replace the symbolic proof. No independent external review has been performed.

## References

[1] C. Bodart, A. Carvalho, A.-C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251 (first public version 2026-09-28), Sections 2, 4–8, 11. https://arxiv.org/abs/2609.35251

[2] R. J. Lipton, Y. Zalcstein, *Word Problems Solvable in Logspace*, Journal of the ACM 24 (1977), 522–526. DOI: 10.1145/322017.322031. Authorized 1976 technical report: https://engineering.yale.edu/download_file/view/75e51330-310e-4340-b4aa-a7b28a65ff57/431

[3] T. M. Brough, M. Johnson, M. Kambites, C.-F. Nyberg-Brodda, *Free inverse monoids are co-context-free*, arXiv:2511.00566 (2025).

