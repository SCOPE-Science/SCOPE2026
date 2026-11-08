# The first entropy deficit for online pairwise comparison of total orders

## Finding

Let \(\mathcal P_n\) be the set of all strict total orders on \([n]\). For each unordered pair \(\{i,j\}\), \(i<j\), its binary label is one precisely when \(i\) precedes \(j\) in the unknown order. Then

\[
\operatorname{Ldim}(\mathcal P_7)=11<12=\lfloor\log_2(7!)\rfloor.
\]

After a positive observation that \(1\) precedes \(2\), the remaining 2,520 orders have Littlestone dimension exactly \(10\). Previously established ranks on \(1\le n\le6\) are \(0,1,2,4,6,9\), each equal to \(\lfloor\log_2(n!)\rfloor\); thus seven is the first cardinality-ceiling deficit in the total-order comparison family. No claim is made about larger sizes.

## Assumptions and scope

The labels represent *relative order*, not the edges of a Hamiltonian path. A complete binary mistake/shattering tree of depth \(d\) has one queried pair at every internal node and admits at least one compatible total order at each of its \(2^d\) leaves. An unknown target order may differ between different root-to-leaf paths, but must remain consistent along each single path. All comparisons are noiseless and binary. Relabeling the seven elements preserves the concept class.

## Proof

For a finite nonempty version space \(V\) of total orders, define \(B(V,d)\) to mean that a full comparison-query tree of depth \(d\) can be shattered by \(V\). Base case: \(B(V,0)\) holds. For \(d>0\),

\[
B(V,d)\iff\bigvee_{1\le i<j\le7}\left(
 B(V_{i<j},d-1)\land B(V_{j<i},d-1)
\right),
\]

where \(V_{i<j}\) and \(V_{j<i}\) are the orders realizing the indicated outcomes. For an empty version space the predicate is false at every depth. In particular, \(B(V,d)\) is false when \(|V|<2^d\). This is an exact equivalence, not a heuristic, because the root pair and both subtrees exhaust the possible binary query trees; the cardinality pruning is logically necessary.

The attached `permutation_comparison_verify.py` implements this recurrence in two different exhaustive representations. The first stores each version space as a bit mask on all \(7!=5040\) orders. Each of the 21 pair queries partitions the bit mask, and the recursion checks all 21 possible root choices. The second stores the transitive closure of the precedence constraints as a strict partial order, counts its linear extensions by an exact subset recurrence, and for each incomparable pair inserts either directed precedence relation and recomputes its closure. Every comparison-consistent version space is exactly the set of linear extensions of such a partial order, so the second enumeration is exhaustive as well. In both implementations the only pruning uses the necessary inequality \(|V|\ge2^d\); no search cutoff or sampling occurs.

The two enumerations each verify \(B(\mathcal P_7,11)=\mathrm{true}\) and \(B(\mathcal P_7,12)=\mathrm{false}\). They also both verify for \(V=\{\pi:1\text{ precedes }2\}\) that \(B(V,10)=\mathrm{true}\) and \(B(V,11)=\mathrm{false}\). Symmetry makes all possible root comparisons equivalent, so the latter conditional result also gives the stated full rank. The attached `permutation_comparison_witness.json` is an explicit, breadth-first list of all 2,047 internal pair labels for a full depth-11 tree; an *independent trace test within the verifier*, using the total-order bit masks rather than the poset strategy used to construct the tree, checks that all 2,048 paths have a witnessing total order. This certifies the lower bound constructively. The recurrence exhaustion certifies the upper bound.

For \(1\le n\le6\), the same two implementations obtain \(0,1,2,4,6,9\). Direct comparison with \(\lfloor\log_2(n!)\rfloor\) proves the first-deficit assertion within \(1\le n\le7\).

## Verification

Place `permutation_comparison_verify.py` and `permutation_comparison_witness.json` together, then run `python3 permutation_comparison_verify.py` using standard Python 3 (no third-party packages). Expected terminal marker: `PERMUTATION_COMPARISON_7_PASS complete_tree_leaves= 2048 minimum_number_of_witnessing_permutations= 1`. The program independently evaluates every depth predicate required for \(n=1,\ldots,7\), checks the positive-condition rank on seven elements, and verifies every witness leaf. It examines 74,797 memoized predicate states for seven elements in each of the two exact representations. The assertion on depth 12 is a finite exhaustive mathematical certificate, not an asymptotic or inductive claim.

## Relationship to prior work

The standard Littlestone-dimension recurrence and the elementary cardinality bound are established tools, not contributions here. Feng, Geneson, Lee, and Slettnes (2022), Section 5.2, define this exact binary comparison setting at their parameter \(r=1\); their Theorems 25 and 26 give general bounds and an asymptotic lower-bound strategy, not the seven-element exact value. Goldman, Rivest, and Schapire (1993) study online learning of total orders and polynomial algorithms with general mistake bounds; their accessible abstract does not contain this exact finite rank. A previously recorded finite calculation establishes the ranks through six elements; the new mathematical boundary is the first failure at seven, which is not implied by those six cases. A related two-chain-interleaving entropy deficit concerns a proper subfamily of permutations with a different set of allowed comparisons and does not settle the full seven-element class.

## Limitations

This is a reproducible computer-assisted **finite** theorem for seven elements, not an all-size formula. The 1993 paper's entire publisher-hosted full text was not accessible for a complete theorem-by-theorem comparison, so its historical-priority risk remains; its abstract and relevant open thesis discussion were examined. The two code implementations and the explicit witness have not been independently audited by an outside mathematician. A failed keyword search alone is not considered evidence of uniqueness.

## References

- Raymond Feng, Jesse Geneson, Andrew Lee, Espen Slettnes, *Sharp bounds on the price of bandit feedback for several models of mistake-bounded online learning*, arXiv:2209.01366v1, September 3, 2022, Section 5.2. https://arxiv.org/pdf/2209.01366
- Sally A. Goldman, Ronald L. Rivest, Robert E. Schapire, *Learning Binary Relations and Total Orders*, SIAM Journal on Computing 22(5), 1006–1034 (1993), https://doi.org/10.1137/0222062.
- Sally A. Goldman, *Learning Binary Relations, Total Orders, and Read-once Formulas*, MIT PhD thesis (1990), https://people.csail.mit.edu/rivest/student-theses/phd-1990-goldman.pdf.
- Badih Ghazi, Ravi Kumar, Pasin Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, https://proceedings.mlr.press/v132/ghazi21a.html.
