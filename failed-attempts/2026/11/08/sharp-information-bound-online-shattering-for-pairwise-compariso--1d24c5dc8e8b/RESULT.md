# Sharp information-bound online shattering for pairwise comparisons of up to six labels

## Finding

For an integer \(n\ge1\), write \([n]=\{0,1,\ldots,n-1\}\) and let \(\mathcal P_n\) be the family of all strict total orders on \([n]\). The instance domain is the set of unordered pairs \(\{a,b\}\) with \(a<b\); a query has label one precisely if \(a\) precedes \(b\) in the unknown order. Then
\[
\operatorname{VCdim}(\mathcal P_n)=n-1\qquad(n\ge1).
\]
For \(1\le n\le6\), the adaptive dimension meets the cardinality upper bound exactly:
\[
\operatorname{Ldim}(\mathcal P_n)=\lfloor\log_2(n!)\rfloor
\quad\text{for }1\le n\le6.
\]
Thus the online dimensions at orders one through six are \(0,1,2,4,6,9\). The first strict inequality between online and static dimensions occurs at \(n=4\). At \(n=6\), a complete depth-nine tree is feasible even though there are only \(720\) total-order hypotheses; its \(512\) leaf paths are certified by distinct explicit orders.

## Assumptions and scope

An order is a permutation \(p=(p_0,\ldots,p_{n-1})\) listing \([n]\) from first to last. A Boolean query is a distinct pair \(\{a,b\}\), standardized so \(a<b\). Its value is one when \(a\) appears before \(b\) in \(p\), zero otherwise. The VC dimension counts fixed sets of these pair queries shattered under every labeling. The Littlestone dimension is the largest depth of a complete binary adaptive query tree whose every root-to-leaf Boolean labeling is realized by some order. Query choices may depend on earlier answers. No restrictions on the learner's running time or the query sequence are imposed. All stated exact online values stop at six labels; no exact formula for larger ground sets is asserted.

## Proof

**Static shattering for arbitrary order.** Identify each pair query with an edge of the complete graph on the \(n\) labels. If the queried-edge set contains a cycle, orient the edges of that cycle consistently around it. This is a Boolean assignment incompatible with any strict total order because it entails a directed cycle. Therefore a VC-shattered support must be a forest. Conversely, assign arbitrary Boolean answers to edges of a forest. Orient every selected edge accordingly. Every orientation of a forest is acyclic; its reachability relation has a linear extension, and that strict total order realizes the prescribed answers. Hence the shattered supports are exactly forests. A spanning tree has \(n-1\) edges and is shattered, establishing \(\operatorname{VCdim}(\mathcal P_n)=n-1\) also for \(n=1\).

**Adaptive upper bound.** A complete binary tree of depth \(d\) has \(2^d\) distinct root-to-leaf Boolean histories. No deterministic hypothesis can realize two different histories, since they first differ on a query posed at the same node. A class of \(n!\) hypotheses thus has \(2^d\le n!\), and consequently \(\operatorname{Ldim}(\mathcal P_n)\le\lfloor\log_2(n!)\rfloor\) for every \(n\).

**Matching lower bounds through six labels.** The self-contained file `order_certificates.json` contains complete labeled binary trees for \(n=2,3,4,5,6\), of respective depths \(1,2,4,6,9\). Every internal node records a pair \(a<b\) to query, with child zero for \(a\) following \(b\) and child one for \(a\) preceding \(b\). Every leaf explicitly records a distinct permutation of the labels realizing every answer on its root-to-leaf path. `check_order_certificates.py` reconstructs the permutation universe independently and exhaustively checks every internal node, branch, path, and witness. There are respectively \(2,4,16,64,512\) leaves and \(1,3,15,63,511\) internal nodes. The upper bound proves that no greater depth is possible, so the five finite lower bounds are sharp. For \(n=1\) there is only one hypothesis, hence depth zero. These checks are finite complete certificates for the five specified orders, not an induction to arbitrary \(n\).

## Verification

Run `python check_order_certificates.py order_certificates.json` with standard Python 3. The verifier rebuilds the full \(n!\)-permutation universe for each \(n\), traverses every branch of each embedded tree, verifies that its leaf witness gives exactly the claimed pairwise comparisons, checks distinctness of witnesses and the required \(2^d\)-leaf count, and checks the strict hypothesis-cardinality barrier for depth \(d+1\). `build_order_certificates.py` provides an independent reproducible construction algorithm based on exact memoized minimax recursion over subsets of the permutation family. The saved output is `order_verification.txt`. Finite replay checks prove the finite online lower bounds because every branch and witness is explicitly covered; they are not estimates from random samples.

## Relationship to prior work

Guingona, Kolesnikov, Nierwinski and Soucy (first public 2021-09-10) analyze exact VC and Littlestone dimensions in a mathematical-logic framework for families of zero sets of linear combinations. Their theorem establishes equality of the two dimensions for those zero-set families. It does not cover the strict-total-order pairwise-comparator class here: this class already has unequal dimensions on four labels. This 2021 logic-based comparison motivates asking for exact dimensions and strict separations in another natural definable binary relation.

Goldman, Rivest and Schapire (1993, Section 4.2) directly studied adversarial online learning of total orders by pairwise comparisons. Their general lower bound grows on the order of \(n\log n\), while their halving method gives the elementary upper bound based on counting all total orders. Thus neither the online-learning model, its growth scale, nor the counting upper bound is new. The narrower result here is a complete finite calibration of *equality* in that counting bound for all orders up to six, including a concrete depth-nine tree on six labels. Their inspected general bounds do not determine these particular finite optimum values.

Johnson and Wickes (2021, arXiv v1; full text inspected in revised v2) study a different permutation-shattering notion: a set of \(k\) *items* must appear in all \(k!\) relative orders among a chosen family of permutations. Here a single permutation is a binary concept on *pair* instances, and the adaptive dimension uses binary mistake trees. Their results do not imply the finite comparator-tree thresholds. The static forest argument is elementary and is not claimed as an independent novel theorem.

## Limitations

The exact Littlestone formula is only proved for \(n\le6\); no assertion is made at \(n\ge7\). An asymptotically unbounded adaptive/static gap was already implied by earlier total-order learning work and is not claimed as new. Originality is assessed from accessible primary results, an actual semantic research-record search, and related mathematical-claim overlap comparisons, not from an exhaustive historical bibliography. A differently phrased prior exact finite decision-tree calculation remains a historical-priority risk. The reviewed tree certificates are deterministic finite objects, and independent mathematical auditing has not been performed.

## References

1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (first public 2021-09-10), https://arxiv.org/abs/2109.04805 .
2. S. A. Goldman, R. L. Rivest and R. E. Schapire, *Learning Binary Relations and Total Orders*, SIAM Journal on Computing 22(5) (1993), 1006–1034, DOI: 10.1137/0222062; author-hosted full text: https://people.csail.mit.edu/rivest/pubs/GRS93.pdf .
3. J. Robert Johnson and Belinda Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946v1 (first public 2021-12-03); https://arxiv.org/abs/2112.01946 .
