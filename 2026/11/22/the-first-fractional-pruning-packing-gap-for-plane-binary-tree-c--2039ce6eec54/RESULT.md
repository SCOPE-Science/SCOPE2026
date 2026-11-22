# The first fractional pruning-packing gap for plane binary tree codes

## Finding

Consider the set \(\mathcal T_n\) of *unlabelled, rooted, ordered full binary tree shapes* having exactly \(n\) internal vertices. A channel chooses one terminal leaf, deletes that leaf and its parent fork, and promotes the surviving sibling subtree to the parent's former position. A one-pruning-correcting code \(\mathcal C\subseteq\mathcal T_n\) consists of tree shapes whose sets of possible received shapes are pairwise disjoint.

Let \(M_n\) be the largest size of such a code and let \(P_n\) be the optimum of the associated fractional deletion-output packing linear program. At every integer \(1\le n\le6\), the exact values are

\[
(M_1,M_2,M_3,M_4,M_5,M_6)=(1,1,2,3,7,15),
\qquad
(P_1,P_2,P_3,P_4,P_5,P_6)=(1,1,2,3,7,205/13).
\]

In particular, \(n=6\) is the first strict fractional-packing gap in this family: \(P_6-M_6=10/13\). The integral optimum still equals the floor of the fractional bound.

## Assumptions and scope

A leaf is represented by a dot, and an internal node is an ordered pair of its left and right children, encoded as `(left,right)`. The tree family is defined recursively by \(\mathcal T_0=\{\bullet\}\) and

\[
\mathcal T_n=\bigcup_{k=0}^{n-1}\{(L,R): L\in\mathcal T_k,\ R\in\mathcal T_{n-1-k}\}\quad(n\ge1).
\]

The union is over distinct ordered shapes, not nonplane isomorphism classes. There are \(C_n=\frac1{n+1}\binom{2n}{n}\) shapes in \(\mathcal T_n\). Leaves are indistinguishable and positions are not supplied to the decoder. No label, branch length, left-right reflection, or rotation is factored out.

For a nonleaf \(t=(L,R)\), define its one-pruning shadow \(D(t)\subseteq\mathcal T_{n-1}\) recursively by

\[
D((L,R))= \begin{cases}\{R\},&L=\bullet,\\ \{(U,R):U\in D(L)\},&L\ne\bullet\end{cases}
\ \cup\
\begin{cases}\{L\},&R=\bullet,\\ \{(L,V):V\in D(R)\},&R\ne\bullet.\end{cases}
\]

The two displayed sets are united, so repeated outputs from different leaf choices are counted only once. A code is correct exactly when \(D(t)\cap D(u)=\varnothing\) for distinct codewords \(t,u\). Thus the channel removes exactly one leaf and suppresses its parent, not an arbitrary matched parenthesis pair or a single bit of a balanced-word representation.

Let \(A_{s,t}=1\) for \(s\in D(t)\), and zero otherwise. Define

\[
P_n=\max\left\{\sum_{t\in\mathcal T_n}x_t:\ x_t\ge0,\ Ax\le\mathbf1\right\}
=\min\left\{\sum_{s\in\mathcal T_{n-1}}y_s:\ y_s\ge0,\ A^\mathsf T y\ge\mathbf1\right\}.
\]

## Proof

**Exact shadow enumeration.** The recursive grammar enumerates precisely every rooted plane full binary tree shape in \(\mathcal T_n\). A leaf removal either happens at the root (one root child is a leaf, yielding the other child) or within exactly one nonleaf root child (yielding its recursively pruned child, with the opposite subtree unchanged). This establishes the displayed recursion for all choices of the deleted leaf and proves that the finite incidence matrix in `certificates.json` describes the channel exactly.

**Primal and dual certificates.** For each \(n=1,\ldots,6\), the data file enumerates every source shape and every received shape in split-size-lexicographic order, its entire source-to-output incidence, and rational sparse vectors `fractional_primal` and `fractional_dual`. All components are nonnegative; the exact inequalities \(Ax\le\mathbf1\) and \(A^\mathsf T y\ge\mathbf1\) hold, and both objectives equal the corresponding stated \(P_n\). Weak duality proves equality; no floating-point tolerance is used in verification. At \(n=6\) the matching exact objectives equal \(205/13\).

**Integer lower bounds and upper bounds.** For each length the file gives `codeword_indices` whose deletion shadows are pairwise disjoint, proving \(M_n\ge 1,1,2,3,7,15\), respectively. The last code is the 15 shapes with zero-based indices

`0, 4, 7, 33, 48, 55, 56, 69, 74, 76, 83, 98, 124, 127, 131`

in the 132-shape enumeration specified in the data. Every integral code gives a feasible fractional packing by assigning weight 1 to its codewords and 0 to the other shapes. Hence \(M_n\le\lfloor P_n\rfloor\) (including \(P_n=205/13<16\)). The upper bound equals the exhibited code size at all six lengths. At lengths up to five the LP itself is integral at its optimum, whereas at length six \(205/13-15=10/13>0\). This proves both the complete six-length table and the first strict-gap assertion.

## Verification

All necessary evidence is included: `certificates.json`, `verify.py`, and `alternate_verify.py`. With Python 3 and no third-party libraries, run `python3 verify.py` and `python3 alternate_verify.py` in the same directory. Both implementations regenerate all tree shapes and their deletion shadows from the definition independently, verify every source/output incidence in the certificate, confirm each codebook's disjoint shadows, and check rational primal-dual feasibility and exact equality of the two objective sums. The first uses a preorder token representation; the second uses a recursive ordered-pair representation. Expected final markers are `VERIFY_OK` and `ALTERNATE_OK`.

The finite certificate includes every relevant tree shape and every source-to-output incidence, not a partial sample. The mathematical upper bounds follow from the rational witnesses plus weak duality, not from an unverified optimizer log. This is a finite classification for \(n\le6\), not a proof about all lengths.

## Relationship to prior work

Tree-edit studies of phylogenetic structures include leaf removal but generally retain taxon labels and study distances rather than the size of error-correcting codes on unlabelled ordered shapes [1]. Classical deletion-code work uses a hypergraph and fractional covering/packing technique for strings [2]; the linear-programming method is therefore not new here. Grammar-based compression of binary trees addresses lossless coding without an unknown tree-pruning error [3].

Related enumerations of Dyck or balanced-word deletion outputs address other channels. In particular, deleting an arbitrary matched parenthesis pair is more permissive than suppressing a parent of a terminal leaf in a full tree. A code for the latter need not be a code for the former. Likewise, deleting one binary character from a Dyck representation is not this tree-edit operation. The result claimed here is the exact shape-code capacity and fractional-packing threshold for the explicitly defined pruning channel.

## Limitations

Only \(1\le n\le6\) and only one unknown leaf pruning are considered. There is no asserted result for larger trees, multiple prunings, subtree deletion, labeled or unordered trees, prefix-code robustness, or arbitrary Dyck bit deletion. The measured fractional integrality gap does not imply a failure of integer rounding: \(\lfloor205/13\rfloor=15\). Computational discovery of the witnesses used numerical optimization, but all final conclusions are backed by directly checkable, exact rational certificates. Prior-art searches cannot exclude unindexed historical computations or different equivalent formulations. Independent mathematical validation has not been performed.

## References

[1] Koperwas and Walczak, *Tree edit distance for leaf-labelled trees on free leafset and its comparison with frequent subsplit dissimilarity and popular distance measures*, BMC Bioinformatics 12, 204 (published May 25, 2011), https://doi.org/10.1186/1471-2105-12-204.

[2] Kulkarni and Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, initially submitted November 13, 2012, https://arxiv.org/abs/1211.3128.

[3] Zhang, Yang and Kieffer, *A Universal Grammar-Based Code For Lossless Compression of Binary Trees*, arXiv:1304.7392, initially submitted April 27, 2013, https://arxiv.org/abs/1304.7392.
