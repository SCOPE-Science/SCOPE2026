# Exact online shattering rank and stability boundary for finite prefix ultrametric balls

## Finding

Let \(b\ge2\), \(h\ge0\) be integers. On the set \(X_{b,h}=[b]^h\) of length-\(h\) words, consider \(\mathcal C_{b,h}\), the family of **all nonempty prefix cylinders** \([v]=\{x\in X_{b,h}:v\text{ is a prefix of }x\}\) for words \(v\) of lengths from \(0\) through \(h\). Repeated sets are identified; none repeat for \(b\ge2\). With \(\mathcal C^0_{b,h}=\mathcal C_{b,h}\cup\{\varnothing\}\), the exact Littlestone dimensions are

\[
\operatorname{Ldim}(\mathcal C_{b,h})=
\begin{cases}
0,&h=0,\\
1,&(b,h)=(2,1),\\
1+\lfloor\log_2(h+1)\rfloor,&\text{otherwise, }h\ge1,
\end{cases}
\qquad
\operatorname{Ldim}(\mathcal C^0_{b,h})=1+\lfloor\log_2(h+1)\rfloor.
\]

The ordinary VC dimensions are

\[
\operatorname{VCdim}(\mathcal C_{b,h})=
\begin{cases}
0,&h=0,\\
1,&(b,h)=(2,1),\\
2,&\text{otherwise, }h\ge1,
\end{cases}
\quad
\operatorname{VCdim}(\mathcal C^0_{b,h})=
\begin{cases}1,&h=0,\\2,&h\ge1.\end{cases}
\]

These are all-inclusive sets of balls for the standard finite prefix ultrametric. In particular, the optimal deterministic realizable online mistake bound grows logarithmically with hierarchy depth even though the static VC dimension is at most two; except for the two indicated small cases, the online rank is independent of branching factor.

A model-theoretic consequence: given any sequence of these finite two-sorted ball/leaf incidence structures with branching \(b_i\ge2\) and heights \(h_i\ge0\), and any nonprincipal ultrafilter \(U\), the incidence formula \(x\in B\) is **stable** in the ultraproduct if and only if there is a finite \(H\) for which \(\{i:h_i\le H\}\in U\). The statement is about this formula, not about the stability of the complete ambient theory.

## Assumptions and scope

Every tree is the full rooted \(b\)-ary tree of height \(h\); its hypotheses are descendant-leaf sets of *all* nodes, queried on leaves (not on internal nodes). A complete binary mistake tree of depth \(d\) consists of leaf queries at its internal nodes, with all \(2^d\) answer paths realized by hypotheses. Rank zero means there is no query with both answers realizable. The empty hypothesis is absent from \(\mathcal C_{b,h}\), and included only in \(\mathcal C^0_{b,h}\).

For \(h\ge1\), equip the leaves with \(d(x,y)=2^{-\operatorname{lcp}(x,y)}\) for distinct words, and \(d(x,x)=0\), where \(\operatorname{lcp}\) is longest common-prefix length. The cylinder of length \(j\) is the closed metric ball of radius \(2^{-j}\) around any contained leaf (radius zero also represents a singleton). Hence the family contains exactly the distinct nonempty metric balls. At \(h=0\) there is one leaf and one nonempty concept.

## Proof

**Step 1 (chain lemma).** A strict inclusion chain of \(m\ge1\) nonempty, distinct subsets has Littlestone dimension \(\lfloor\log_2m\rfloor\). The concept-count upper bound follows because a depth-\(d\) complete mistake tree requires at least \(2^d\) different concepts. To attain the bound, arrange the nested concepts from largest to smallest and query a point in the difference between the \(k\)-th and \((k+1)\)-st concepts. Such a point exists by strict inclusion. This separates the concept chain into a prefix and suffix of prescribed sizes; repeatedly split approximately in half to build depth \(\lfloor\log_2m\rfloor\). The argument still holds after restriction to either subchain.

**Step 2 (universal upper bound).** For any leaf \(x\), exactly its \(h+1\) ancestral cylinders contain \(x\); they form a strict chain. Consequently the positive version space after a first membership query has rank \(\lfloor\log_2(h+1)\rfloor\) by Step 1. The usual finite Littlestone recurrence is

\[
R(F)=\max\!\left(\{0\}\cup\{1+\min(R(F^+_x),R(F^-_x)):\;F^+_x,F^-_x\ne\varnothing\}\right).
\]

Thus both \(\mathcal C_{b,h}\) and \(\mathcal C^0_{b,h}\) have rank at most \(1+\lfloor\log_2(h+1)\rfloor\).

**Step 3 (nonempty-class lower bound and small cases).** For \(h=0\) there is only one hypothesis, so rank is zero. For \(h=1\), the hypotheses are the entire leaf set and \(b\) singleton sets. If \(b=2\), any membership query has a positive chain of two hypotheses and a negative singleton, so the rank is one. If \(b\ge3\), querying a leaf leaves a positive chain of two concepts and at least two distinct negative singleton concepts. Both branches have rank at least one, giving rank two; Step 2 matches it.

For \(h\ge2\) proceed inductively. For any leaf \(x\), the positive branch has rank \(r_h=\lfloor\log_2(h+1)\rfloor\). The negative branch contains every cylinder in any sibling subtree of the first edge of \(x\); after identifying its leaves, this subfamily is precisely \(\mathcal C_{b,h-1}\). Induction and the just-checked bases give

\[
\operatorname{Ldim}(\mathcal C_{b,h-1})\ge \lfloor\log_2(h+1)\rfloor
\quad(h\ge2),
\]

since the logarithmic floor increases by at most one per height increment, with the only potentially missing increase at \(h=2\) supplied by the rank-one binary height-one class. So both first-query branches have rank at least \(r_h\), and \(\operatorname{Ldim}(\mathcal C_{b,h})\ge1+r_h\). With Step 2 this proves the exact formula at all heights.

**Step 4 (empty-hypothesis normalization).** For \(h=0\) the two hypotheses are the singleton and the empty set; one membership query separates them, giving rank one. For \(h=1\) and \(b\ge2\), querying a leaf yields a positive chain of two concepts, while the negative branch contains the empty set and at least one other singleton, giving both branches rank at least one. Hence rank two. For \(h\ge2\), the nonempty subfamily already attains the Step 2 upper bound. This proves the formula for \(\mathcal C^0_{b,h}\).

**Step 5 (VC dimension).** The cylinder family is laminar: any two cylinders are disjoint or one contains the other. A three-point support cannot be shattered: its three different two-point traces would have pairwise nonempty intersections and no containment, contradicting laminarity. If \(b^h\ge3\), every pair of distinct leaves is shattered: the root gives the full trace, the leaf singletons give the two individual traces, and a third singleton gives the empty trace. If \(b^h=2\), the nonempty class cannot give an empty trace on the two-point support, but it shatters each singleton. If \(b^h=1\), no singleton is shattered without the empty hypothesis. Adding \(\varnothing\) gives VC dimension one on the singleton domain and two on all larger domains. This proves the VC formulas. Indeed, the shattered-support enumerator for \(b^h\ge3\) is \(1+b^h z+\binom{b^h}{2}z^2\) for either normalization.

**Step 6 (ultraproduct stability).** Existence of a fixed-depth complete mistake tree is a first-order existential condition on the two-sorted incidence structure, involving finitely many leaf and ball variables. The proved formula makes such trees exist in the factor structures at unbounded depths exactly when their heights tend to infinity along \(U\). By Łoś's theorem, the ultraproduct has complete mistake trees of every finite depth precisely when the heights are unbounded modulo \(U\). The standard model-theoretic characterization of a stable formula as one with bounded finite Littlestone/thicket dimension (equivalently no order property) gives the stated equivalence. If the heights are bounded modulo \(U\), the explicit rank bound is uniform, so the formula is stable. No statement is made about all formulas of the ambient theory.

## Verification

A standalone Python 3 checker (`verify.py`) constructs all distinct finite prefix cylinders as bitmasks, computes Littlestone dimension by the *unrestricted* all-query minimax recurrence, and independently checks ordinary VC dimension by enumerating traces on supports. Eighteen exhaustive parameter/normalization cases were verified, including binary heights through three, ternary heights through two, and quaternary heights through one. The program also checks the arithmetic used in the inductive inequality for heights from two through one thousand. Its terminal success string is `ALL_PREFIX_BALL_CHECKS_PASS 18 independent finite cases`. These are finite corroborations only; Steps 1–6 prove all-parameter statements.

## Relationship to prior work

Walker (2022) studies tree dimension and Sauer–Shelah bounds on leaf sets of trees, including their connection to Littlestone shattering. The present hypotheses, by contrast, are the individual descendant-leaf *cylinders* and queries are individual leaves; an exact online rank for this class is not stated in the sections inspected. Guingona–Kolesnikov–Nierwinski–Soucy (2021) determine Littlestone and VC dimensions for algebraic zero-set families, not the prefix-ball incidence system. Dovgoshey–Kostikov (2023) describe ultrametric balls via labeled trees without an online rank or stability criterion. Avdiukhin et al. (2023) study hierarchical-tree learning via tuple labels and different concept classes; their abstract was inspected but not their complete paper. These contrasts are comparisons of mathematical objects and quantifiers, not a proof of global historical priority. A more general result for laminar set systems, or an equivalent statement under tree-indexed learning terminology, might imply this exact formula and remains a priority risk.

## Limitations

The exact rank theorem assumes full homogeneous branching at each level, and the conclusion need not hold for nonregular, pruned, or arbitrary-height laminar trees without modification. For the finite checker, only the specified small test cases were exhaustively evaluated; its height-1000 arithmetic checks do not replace the induction. Comprehensive historical priority, including equivalence under alternative laminar-learning formulations, is not established. The ultraproduct result concerns only the incidence formula with leaf and ball sorts.

## References

1. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211v1, first posted 2022-03-23. https://arxiv.org/abs/2203.12211
2. V. Guingona, A. Kolesnikov, J. Nierwinski and C. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first posted 2021-09-10. https://arxiv.org/abs/2109.04805
3. O. Dovgoshey and V. Kostikov, *Locally finite ultrametric spaces and labeled trees*, arXiv:2308.06626v1, first posted 2023-08-12. https://arxiv.org/abs/2308.06626
4. D. Avdiukhin et al., *Tree Learning: Optimal Algorithms and Sample Complexity*, arXiv:2302.04492v1, first posted 2023-02-09. https://arxiv.org/abs/2302.04492
