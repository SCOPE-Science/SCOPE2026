# The first fractional-packing gap for single-leaf deletion codes of unrooted phylogenetic trees

## Finding

For every integer \(n\ge4\), let \(\mathcal T_n\) be the set of all unrooted, fully resolved, nonplane binary phylogenetic trees whose leaves carry exactly the distinct labels \(0,1,\ldots,n-1\). All internal vertices have degree three. For a leaf \(i\), define \(T\setminus i\) by deleting that leaf and suppressing its resulting degree-two neighbor. A *single-leaf-deletion code* is a subset \(C\subseteq\mathcal T_n\) such that, for every label \(i\), the trees \(\{T\setminus i:T\in C\}\) are pairwise distinct. Write \(M_n\) for the maximum code size, and \(P_n\) for the associated fractional packing optimum, defined below.

The following finite boundary is exact:

\[
M_4=P_4=1,\qquad M_5=P_5=3,\qquad M_6=P_6=15,
\]

whereas

\[
P_7=105,\qquad M_7\le104<105.
\]

Thus seven taxa are the first size at which the natural single-leaf restriction packing relaxation is not integral. This result does **not** determine the exact value of \(M_7\).

## Assumptions and scope

The leaf labels are retained by the receiver and the identity of the deleted leaf is therefore observable from the remaining label set. Topologies are unrooted, unordered and unweighted. Tree isomorphisms fix all leaf labels; internal vertices are unlabelled. The result concerns **exactly one** deleted leaf, not arbitrary induced subtrees or deletion of two or more leaves. The fractional packing LP has one nonnegative weight \(x_T\) for every \(T\in\mathcal T_n\) and constraints

\[
\sum_{T\in\mathcal T_n:\ T\setminus i=S}x_T\le1
\quad (i\in\{0,\ldots,n-1\},\ S\in\mathcal T_{n-1}(\{0,\ldots,n-1\}\setminus\{i\})).
\]

Its objective is to maximize \(\sum_T x_T\). Identical shapes on different remaining label sets are distinct observations.

## Proof

**Packing upper bound and fractional equality.** There are \((2n-5)!!\) labeled binary unrooted trees on \(n\) leaves: each tree with \(n-1\) leaves has exactly \(2n-5\) edges on which the new leaf can be inserted. For any fixed deleted label, there are exactly \((2n-7)!!\) possible received trees. Each input tree has exactly one output at that fixed label. Summing all inequalities for this label gives

\[
M_n\le P_n\le(2n-7)!!.
\]

Every received \((n-1)\)-leaf tree has exactly \(2n-5\) distinct extensions at the missing label. Hence setting every fractional variable to \(1/(2n-5)\) is feasible and has objective \((2n-7)!!\). Consequently \(P_n=(2n-7)!!\) for every \(n\ge4\).

**Attainment through six leaves.** The witnesses in `witnesses.json` consist of complete lists of split signatures for respectively \(1,3,15\) trees at \(n=4,5,6\). `checker.py` independently reconstructs these codebooks and checks that, for every deleted leaf, all \((2n-7)!!\) output topologies are hit exactly once. For \(n=6\), the particularly natural witness consists of all fifteen trees with three disjoint cherries: a cherry is a pair of leaf-neighbors sharing an internal vertex. Deleting any leaf of a three-cherry tree leaves a five-leaf tree. Conversely, a five-leaf binary tree has two cherries and one other leaf; pairing that remaining leaf with the deleted label uniquely restores a three-cherry tree. Thus the restriction map is bijective for each label, proving \(M_6=15\). The witnesses for \(n=4,5\) give the smaller equalities.

**Strict failure at seven leaves.** At \(n=7\), there are exactly \(945\) distinct source trees and exactly \(7\cdot105=735\) labeled receiver states. Each source belongs to exactly seven receiver sets, and each receiver has exactly nine possible source extensions. If a code had \(105\) members, the preceding upper bound would force it to cover every receiver state exactly once. Thus a hypothetical attaining code is exactly an *exact cover* of the 735 receivers by 105 of the 945 seven-element source rows.

`checker.py` constructs all 945 tree topologies, their seven outputs, and the complete 945-by-735 incidence list in `incidence7.txt`, using edge insertion and canonical nontrivial bipartitions. The same script independently verifies every deletion output by literal leaf removal and degree-two contraction, and by restricting split bipartitions. All 735 receivers have nine sources. An exhaustive exact-cover depth-first search with the minimum-remaining-options rule, implemented independently in `dlx.cpp` (dancing links) and `branch.cpp` (in-place availability counts), explores all possible exact covers. Neither uses randomization, truncation, timeouts, symmetry reduction or external optimization solvers. Both terminate with no cover, after 2,561,709 recursive calls on the delivered incidence list. This exhausts every possible 105-member code and proves \(M_7\le104\).

Combining this integer obstruction with the explicit uniform fractional solution proves the asserted first integrality gap.

## Verification

The source code, complete incidence data and explicit smaller optimal codebooks are included as standalone files. Run `sh reproduce.sh` in the extracted directory, with a standard Python 3 interpreter and a C++17 compiler. It reconstructs and checks the observations and both exact-cover searches; the expected final messages are `NO FOUND` from the first solver and `UNSAT` from the second. The script rejects any discrepancy. The exact-cover search is a complete finite proof, not a heuristic, floating-point optimization or inference from a timeout. No untested claim about the integer optimum at seven leaves is used.

## Relationship to prior work

Martin and Thatte (2012) study maximum agreement subtrees for pairs of phylogenetic trees. Their agreement restriction is the same tree operation, but their extremal bounds concern the size of common retained leaf sets rather than packing *families* of trees so that every one-leaf restriction remains distinct. Vakati and Fernández-Baca (2014) characterize agreement and compatibility of families of partially labeled trees through display-graph cuts; those existence criteria do not yield the seven-taxon exact-cover obstruction. Research on six-taxon quartet tomography uses a different observation (Fourier moments of quartet membership, rather than a complete single-leaf-deletion tree topology). These works motivate a leaf-deletion information channel but do not imply the claimed first integrality gap.

## Limitations

The numerical result at seven taxa is a nonattainment theorem and upper bound, **not** an exact evaluation of \(M_7\). The result does not address rooted trees, unlabeled taxa, multiple missing taxa, or optimal capacities for \(n\ge8\). An exhaustive finite search establishes the seven-taxon nonattainment; no short human-only impossibility argument is claimed. Historical priority is qualified by the possibility of work not present in accessible searches or indices. No independent mathematical audit has been carried out.

## References

1. Daniel M. Martin and Bhalchandra D. Thatte, *The maximum agreement subtree problem*, initial public preprint 2012-01-25, https://arxiv.org/abs/1201.5168.
2. Sudheer Vakati and David Fernández-Baca, *Characterizing compatibility and agreement of unrooted trees via cuts in graphs*, Algorithms for Molecular Biology 9 (2014), article 13, https://doi.org/10.1186/1748-7188-9-13.
3. *Two-quartet Fourier tomography of arbitrary six-taxon tree mixtures*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-two-quartet-fourier-tomography-of-arbitrary-six-taxon-tree-mixtu--357afb0253bc.
