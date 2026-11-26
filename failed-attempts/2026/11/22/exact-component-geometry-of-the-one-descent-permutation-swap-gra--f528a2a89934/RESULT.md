# Exact component geometry of the one-descent permutation swap graph

## Finding

For each integer \(n\ge3\), let \(\mathcal E_n\) be the set of permutations \(\pi=(\pi_1,\ldots,\pi_n)\) of \([n]\) having **exactly one descent**, meaning exactly one index \(d\in\{1,\ldots,n-1\}\) with \(\pi_d>\pi_{d+1}\). Let \(G_n\) be the undirected graph on \(\mathcal E_n\) joining two permutations exactly when one is obtained from the other by swapping consecutive **positions**, and the result still has exactly one descent. Then

\[
G_n\cong\underbrace{P_{n-1}\sqcup\cdots\sqcup P_{n-1}}_{n-1\text{ copies}}\ \sqcup\ (2^n-n^2+n-2)K_1.
\]

Here \(P_m\) is a path on \(m\) vertices, and \(K_1\) is an isolated vertex. Consequently, the number of edges is \((n-1)(n-2)\), the number of components is \(2^n-n^2+2n-3\), and every nontrivial component has diameter \(n-2\). The number of vertices of degrees \(0,1,2\), respectively, is
\[
2^n-n^2+n-2,\quad 2(n-1),\quad(n-1)(n-3).
\]
In particular, a uniformly selected one-descent permutation is mobile with probability precisely \((n-1)^2/(2^n-n-1)\), which tends to zero exponentially. The trivial boundary \(n=2\) consists of one isolated permutation.

An explicit path-component labeling is available. For \(1\le j,t\le n-1\), define the one-line permutation \(\pi^{(j,t)}\) by the following concatenations of consecutive increasing lists (an empty range denotes the empty list):
\[
\pi^{(j,t)}=\begin{cases}
(1,\ldots,t-1,\ j+1,\ t,\ldots,j,\ j+2,\ldots,n),&t\le j,\\
(1,\ldots,j-1,\ j+1,\ldots,t+1,\ j,\ t+2,\ldots,n),&t\ge j.
\end{cases}
\]
The formulas coincide at \(t=j\). For fixed \(j\), the vertices \(\pi^{(j,1)},\ldots,\pi^{(j,n-1)}\) form one path in this order; all other permutations in \(\mathcal E_n\) are isolated. Thus two distinct states are reachable if and only if they have these representations for a common \(j\), and then their exact move distance is \(|t-t'|\). In each nontrivial component there is exactly one inverted pair of **consecutive values**, namely \((j,j+1)\) in inverse-descent notation.

## Assumptions and scope

All symbols \(1,\ldots,n\) are individually labeled and distinct; positions are linearly indexed, not cyclic. Only one swap of immediately adjacent positions is allowed per step. A move is legal precisely when the **total** descent count remains one; it need not preserve the position of the descent. No additional permutation-pattern restrictions are imposed. Graphs have no loops and no parallel edges. The finite computer experiments below check small instances but are not used as an infinite proof.

## Proof

**1. The only potentially legal swaps are beside the descent.** Write a one-descent permutation as two increasing blocks
\[
\pi=(a_1,\ldots,a_{d-1},x\mid y,b_1,\ldots,b_{n-d-1}),\qquad x>y,
\]
where every displayed block is increasing. Denote \(a=a_{d-1}\) when \(d>1\) and \(b=b_1\) when \(d<n-1\). Any adjacent swap outside the three position-pairs at indices \(d-1,d,d+1\) creates a new descent but cannot remove the old one; it is illegal. The possible moves are exactly:

- Swapping positions \(d-1,d\) (when \(a\) exists) is legal if and only if \(a<y\): the old descent disappears, and the swapped pair creates one descent at \(d-1\).
- Swapping positions \(d+1,d+2\) (when \(b\) exists) is legal if and only if \(x<b\): it creates a descent at \(d+1\) and removes the old descent.
- Swapping positions \(d,d+1\) removes the old descent and creates a descent at \(d-1\) precisely when \(a>y\), and at \(d+1\) precisely when \(x>b\), with nonexistent neighbors contributing zero. It is legal exactly when one of these two conditions holds.

For an interior descent \(1<d<n-1\), the central-swap condition is also equivalent to \(a<y\) or \(x<b\), because exactly one of \(a>y\) and \(x>b\) holds. At \(d=1\), a central swap is additionally legal if \(x>b\); at \(d=n-1\), it is additionally legal if \(a>y\). Thus a vertex is nonisolated precisely when at least one of the outside-swap inequalities holds, or when one of these two **endpoint** central-swap exceptions holds.

**2. The inequalities force the path templates.** If \(a<y\), every element in the first block excluding \(x\) is below every element in the second block. Because \(x>y\), the first \(d-1\) values must be exactly \(1,\ldots,d-1\). The second block then begins at \(y=d\), and its omitted larger value is \(x\ge d+1\). Hence the permutation is the first displayed template \(\pi^{(j,t)}\) with \(j=x-1\) and \(t=d\le j\). If instead \(x<b\), all elements of the first block are below those in the second block excluding \(y\). The latter must therefore be \(d+2,\ldots,n\), and the first block consists of \(1,\ldots,d+1\) with \(y\le d\) omitted. This is the second template with \(j=y\) and \(t=d\ge j\). The two outside-swap cases overlap only at \(x=d+1,y=d\), when both templates give \((1,\ldots,d-1,d+1,d,d+2,\ldots,n)\). The endpoint central-swap exceptions yield the same templates: when \(d=1\) and \(x>b\), the first block is the singleton \(x\), the rest are the remaining numbers in increasing order, so \(\pi=\pi^{(x-1,1)}\); when \(d=n-1\) and \(a>y\), the last block is the singleton \(y\), so \(\pi=\pi^{(y,n-1)}\). This exhausts all mobile vertices including both endpoints.

**3. Every template list is one simple path, and the lists are disjoint.** Each \(\pi^{(j,t)}\) has exactly one descent. For \(t<j\), exchanging the adjacent entries \(j+1\) and \(t\) sends \(\pi^{(j,t)}\) to \(\pi^{(j,t+1)}\); for \(t\ge j\), exchanging \(j\) and \(t+2\) does the same. The preceding local-swap criterion shows there are no additional feasible neighbors other than these predecessor/successor steps. Alternatively, any adjacent swap preserving the number of descents cannot swap two *consecutive values*: all third values lie either below both or above both, so swapping such a pair changes the descent count by exactly one. Hence the inversion status of every consecutive-value pair is invariant under all legal moves. The template \(\pi^{(j,t)}\) has exactly one inverse descent, at the value index \(j\), proving that templates with distinct \(j\) are disjoint and no edge crosses their lists. Therefore there are exactly \(n-1\) disjoint path components, each on \(n-1\) vertices; every other vertex is isolated.

**4. Count the other vertices.** A one-descent permutation is uniquely determined by the nonempty proper subset \(A\subset[n]\) appearing before its unique descent: the letters of \(A\) and of \([n]\setminus A\) are each increasing. Such a concatenation has *zero* descents exactly when \(A=\{1,\ldots,d\}\), one choice for each \(d=1,\ldots,n-1\). Thus \(|\mathcal E_n|=(2^n-2)-(n-1)=2^n-n-1\). Subtracting \((n-1)^2\) template states gives \(2^n-n^2+n-2\) isolated vertices, and the remaining formulas follow from the disjoint union. Exact path distances are the differences between the integer path indices; no shorter route exists because the graph has no chords. Finally \((n-1)^2/(2^n-n-1)=O(n^2/2^n)\).

## Verification

The standalone standard-library Python script `checker.py` constructs \(\mathcal E_n\) independently by enumerating permutations, computes all legal adjacent swaps by recomputing descents, and separately constructs the claimed templates. Running `python3 checker.py` compares the full edge sets, path-component sizes, degree distributions, and formulas for each \(3\le n\le9\). It independently compares breadth-first-search distances with \(|t-t'|\) for every ordered pair in the proposed nontrivial components for \(3\le n\le8\). It also checks basic integer boundary inequalities at larger lengths. This is a finite test only; the exact all-length claim is supplied by the preceding proof.

## Relationship to prior work

Adjacent-swap reconfiguration is established generally, and Ito, Yamanaka, Hirayama and Kobayashi (2023) prove optimal rerouting of the **linear extensions of a fixed poset**, whereas the one-descent class here is an Eulerian statistic level set, not a linear-extension set of a common poset. Mütze (2023) surveys permutation Gray codes and minimal-change enumerations. Smith (2014) and the subsequent fixed-descent-pattern-poset work study a *pattern-containment* partial order, not the induced graph under adjacent-position swaps. The classical Eulerian formula \(2^n-n-1\) counts the total one-descent states but does not determine their swap connectivity.

The numeric sequence of isolated counts agrees (with matching indices) with OEIS A324172, which counts *crossing subsets*; that entry does not assert the present permutation-reconfiguration interpretation, graph decomposition, or shortest-path classification. Equality of sequences is not taken as a novelty certificate. Published comparisons on adjacent-swap graphs of derangements, pattern-avoiding permutations and fixed-point restrictions have different domains and do not imply this Eulerian-layer classification without a new reduction.

## Limitations

Only permutations with exactly one descent and one-step adjacent-position transpositions are treated. The graph for two or more descents, nonadjacent swaps, or other generation rules is not classified. The disconnected graph has no finite global all-pairs distance; the distance formula applies within mobile components and an isolated state reaches only itself. The literature search does not exclude an earlier result under a different name or an unindexed equivalent; no claim of historical uniqueness or independent certification is made.

## References

1. T. Ito, K. Yamanaka, T. Hirayama and Y. Kobayashi, *Reconfiguration of Linear Extensions*, IPSJ SIG Technical Report, 2023-AL-191 No. 1, repository first public January 12, 2023 (PDF heading January 19, 2023), https://ipsj.ixsq.nii.ac.jp/records/223364 and https://ipsj.ixsq.nii.ac.jp/record/223364/files/IPSJ-AL23191001.pdf.
2. T. Mütze, *Combinatorial Gray Codes—an Updated Survey*, Electronic Journal of Combinatorics DS26, first published July 14, 2023, https://www.combinatorics.org/ojs/index.php/eljc/article/view/ds26.
3. J. P. Smith, *On the Möbius Function of Permutations with One Descent*, Electronic Journal of Combinatorics 21 (2014), https://doi.org/10.37236/3559.
4. J. P. Smith, *Intervals of Permutations with a Fixed Number of Descents Are Shellable*, Discrete Mathematics 339 (2016), 118–126; preprint https://arxiv.org/abs/1405.2560.
5. OEIS A324172, *Number of subsets of \(\{1,\ldots,n\}\) that cross their complement*, https://oeis.org/A324172.
