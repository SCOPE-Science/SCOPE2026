# Exact online shattering rank of the shift-graph adjacency relation

## Finding

Let \(n\ge 2\), and let \(\operatorname{Sh}_2(n)\) be the ordinary undirected shift graph. Its vertices are pairs \((i,j)\) with \(1\le i<j\le n\); two vertices \((i,j)\) and \((k,\ell)\) are adjacent if and only if \(j=k\) or \(\ell=i\). Let \(\mathcal N_n=\{N(v):v\in V(\operatorname{Sh}_2(n))\}\) denote its open-neighborhood set system, without adjoining any additional concepts.

**Theorem.** Its deterministic realizable Littlestone dimension (equivalently, finite thicket dimension) is exactly

\[
\operatorname{Ldim}(\mathcal N_n)=
\begin{cases}
0,&n=2,\\
1,&n=3,\\
2,&n=4,5,\\
3,&n\ge6.
\end{cases}
\]

In particular, the online dimension stabilizes at three already at the six-label shift graph. The same adjacency concept family over the infinite ordered set \(\mathbb N\) has Littlestone dimension three. The latter statement concerns the adjacency formula alone and makes no assertion about the complete first-order theory of this infinite graph.

## Assumptions and scope

The universe of membership queries is the graph's entire vertex set. Hypotheses are the distinct open neighborhoods of vertices, viewed as binary classifiers on that same universe. A labeled complete binary tree of depth \(d\) is shattered if every sequence of \(d\) positive/negative answers is consistent with some hypothesis; instance labels may depend on earlier answers. The empty neighborhood arising at an isolated vertex is retained, but no separately introduced empty or universal concept is allowed. For \(n=2\), the sole concept is empty and its Littlestone dimension is zero.

All arguments are exact and hold for every integer \(n\ge2\). The infinite extension uses the same pairs and adjacency on \(\mathbb N\). The result does not address higher-rank shift graphs, closed neighborhoods, arbitrary induced subgraphs, sample complexity, or graph-theory stability of the full first-order theory.

## Proof

**Positive-branch structure and the universal upper bound.** Fix a queried vertex \(x=(a,b)\) with \(a<b\). The set of hypotheses answering positively is indexed by two disjoint arms

\[
A_x=\{(i,a):1\le i<a\},\qquad
B_x=\{(b,j):b<j\le n\}.
\]

Write \(P_x=A_x\cup B_x\). For another query \(y=(c,d)\) with \(c<d\), a center \((i,a)\in A_x\) answers positively exactly if \(a=c\) or \(i=d\), while a center \((b,j)\in B_x\) answers positively exactly if \(j=c\) or \(b=d\). If \(c=a\), the positive hypotheses include all of \(A_x\), and from \(B_x\) include either all (when \(d=b\)) or none. If \(d=b\), they analogously include all of \(B_x\), and either all or none of \(A_x\). In the remaining case, a positive center in \(A_x\) requires \(d<a\), while one in \(B_x\) requires \(c>b\). These are incompatible with \(c<d\), since \(a<b\). Therefore every query restricted to \(P_x\) has its positive fiber equal to \(\varnothing\), a singleton, \(A_x\), \(B_x\), or \(P_x\).

On each individual arm, every query either includes that entire arm, excludes it, or selects at most one center. Hence either arm has Littlestone dimension at most one: every informative query has a branch with at most one hypothesis. In any informative split of \(P_x\), the positive branch is a singleton or one entire arm, and consequently has dimension at most one. This proves \(\operatorname{Ldim}(P_x)\le2\). Any depth-four shattered tree for the full family would have a depth-three shattered positive subtree after its root query, an impossibility. Thus \(\operatorname{Ldim}(\mathcal N_n)\le3\) for every \(n\), including the infinite case.

**Smaller orders.** For any query \((a,b)\), the positive fiber has \(a-1+n-b\le n-2\) hypotheses. A binary mistake tree of depth two needs at least four different hypotheses. For \(n\le5\), therefore, every positive fiber has Littlestone dimension at most one, and the whole class has dimension at most two. For \(n\le3\), every positive fiber has at most one hypothesis, so the whole class has dimension at most one. When \(n=2\), there is only one hypothesis, giving dimension zero.

**Depth-two witness at \(n=4\).** Query \((2,3)\) at the root. After answer one, query \((1,3)\); after answer zero, query \((1,2)\). The four sequences of answers \(11,10,01,00\) are realized respectively by centers \((3,4),(1,2),(2,3),(1,3)\). Each center has exactly the required adjacency labels along its branch. This proves the lower bound two for \(n=4\), hence also for \(n=5\) by inclusion.

**Depth-three witness at \(n=6\).** Use the following complete adaptive tree; each query is represented by the vertex pair at that node:

| Previous answers | Query |
|---|---|
| Empty prefix | `(3,4)` |
| `1` | `(1,4)` |
| `11` | `(5,6)` |
| `10` | `(1,2)` |
| `0` | `(1,2)` |
| `01` | `(4,5)` |
| `00` | `(1,3)` |

The eight paths admit the following actual center hypotheses:

| Answers | Center realizing the path |
|---|---|
| `111` | `(4,5)` |
| `110` | `(4,6)` |
| `101` | `(2,3)` |
| `100` | `(1,3)` |
| `011` | `(2,4)` |
| `010` | `(2,5)` |
| `001` | `(3,4)` |
| `000` | `(1,2)` |

Direct substitution into the adjacency rule checks all twenty-four required labels. Hence the dimension is at least three for \(n=6\). The same tree and witnesses remain valid in every larger shift graph and in the infinite one, since their labels depend only on equality of the coordinates appearing in the displayed pairs. This attains the upper bound.

The lower bounds one for \(n=3\) and zero for \(n=2\) are immediate from the edge between \((1,2)\) and \((2,3)\) and from the unique empty neighborhood at \(n=2\), respectively. This completes the proof.

## Verification

The accompanying standalone Python file `check_shift_online.py` independently constructs the adjacency matrices and evaluates the full recursive minimax definition of Littlestone dimension for all orders from two through nine. The exact outcomes were \(0,1,2,2,3,3,3,3\), with 22,917 distinct recursive states visited in total. It separately checks all eight leaves of the displayed depth-three tree, the four leaves of the depth-two tree, and the critical two-arm positive-fiber classification for all orders from two through twelve. The final checker output was `SHIFT_NEIGHBORHOOD_VERIFIED exact_cases=8 total_states=22917 checked_arm_orders=11 depth3_leaves=8`.

These computations are finite cross-checks. The universal upper bound and the extension to arbitrary \(n\) are proved by the arm decomposition; the general lower bound is proved by embedding the explicit six-label tree.

## Relationship to prior work

Halevi, Kaplan and Shelah (2021 preprint, subsequently published in 2024) develop a theory of stable graphs with large chromatic number and use shift graphs as canonical examples and obstructions, explicitly defining them in Example 2.3 and recording their chromatic behavior in Fact 2.4. Their results are much broader in model theory but do not state this exact finite Littlestone-dimension sequence or the six-label threshold. Walker (2022) develops tree dimension and the general Littlestone shattering framework, without computing shift-graph adjacency ranks. Wu's 2025 thesis directly treats shift-graph *static* open-neighborhood VC dimension (Proposition 3.4), rather than the adaptive rank computed here. Thus the new conclusion is distinguished by its adaptive quantifier structure, exact threshold, and explicit mistake trees.

The shift graphs have unbounded chromatic number even though their adjacency concept families have a uniform online bound of three. The chromatic behavior itself is established prior literature and is not claimed as new. Finite-dimensional online rank alone does not establish stability of the complete theory of the infinite shift graph.

## Limitations

The proof establishes the statement for ordinary rank-two shift-graph *open* neighborhoods only. It does not settle higher-coordinate shift graphs or augmented hypothesis classes, and it makes no assertion of a new bound for chromatic number. Literature searches and inspection of the most relevant accessible works did not find an equivalent finite-rank theorem, but unindexed publications or alternative names for this exact incidence system might affect historical priority. No independent external mathematical audit has occurred.

## References

1. Y. Halevi, I. Kaplan, and S. Shelah, *Infinite Stable Graphs with Large Chromatic Number II*, arXiv:2103.13931, first public version 25 March 2021; Journal of the European Mathematical Society 26 (2024), 4585–4614. https://arxiv.org/abs/2103.13931
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first public version 23 March 2022. https://arxiv.org/abs/2203.12211
3. Z. Wu, *Investigations of the Chromatic Threshold*, University of Warwick doctoral thesis, June 2025, Proposition 3.4, p. 24. https://wrap.warwick.ac.uk/id/eprint/195162/
