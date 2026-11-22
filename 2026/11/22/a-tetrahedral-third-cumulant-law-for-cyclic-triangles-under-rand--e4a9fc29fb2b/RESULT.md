# A tetrahedral third-cumulant law for cyclic triangles under random orientations

## Finding

Let \(G=(V,E)\) be any finite simple graph. Orient each edge independently and fairly. For each unordered triangle \(T\subset V\), let \(I_T=1\) when its three oriented edges form a directed cycle, and let \(I_T=0\) otherwise. The following statements hold with no connectivity, regularity, or asymptotic assumptions.

**Three-triangle theorem.** For any three *distinct* triangles \(T_1,T_2,T_3\), their indicators have the independent \(\operatorname{Bernoulli}(1/4)\) joint law, except when they are three of the four triangular faces of one four-clique. In that exception, every pair remains independent but
\[
\Pr(I_{T_1}=I_{T_2}=I_{T_3}=1)=0,
\qquad
\mathbb E\!\left[\prod_{i=1}^3(I_{T_i}-1/4)\right]=-\frac1{64}.
\]
Therefore the full triangle-indicator family is 3-wise independent if and only if \(G\) contains no four-clique. Here 3-wise independence means that every subfamily of at most three distinct indicators is jointly independent; empty or short families satisfy this vacuously.

**Weighted third-cumulant law.** Give each triangle a deterministic real weight \(w_T\), and put \(Z_w=\sum_T w_T I_T\). Let \(\mathcal T(Q)\) denote the four triangular faces of a four-clique \(Q\). Then
\[
\begin{aligned}
\mathbb E Z_w &=\frac14\sum_Tw_T,\\
\operatorname{Var}(Z_w)&=\frac3{16}\sum_Tw_T^2,\\
\kappa_3(Z_w)&=\frac3{32}\sum_Tw_T^3
 -\frac3{32}\sum_{Q\cong K_4}\ \sum_{\substack{F\subseteq\mathcal T(Q)\\|F|=3}}\prod_{T\in F}w_T.
\end{aligned}
\]
The third cumulant \(\kappa_3(Z_w)\) is the centered third moment \(\mathbb E[(Z_w-\mathbb E Z_w)^3]\).

Write \(t(G)\) for the number of undirected triangles and \(q(G)\) for the number of four-cliques. For \(w_T=1\) the identities reduce to
\[
\operatorname{Var}(Z)=\frac{3t(G)}{16},\qquad
\kappa_3(Z)=\frac{3t(G)}{32}-\frac{3q(G)}8,
\qquad q(G)=\frac{4\operatorname{Var}(Z)-8\kappa_3(Z)}3.
\]
Thus the one-dimensional law of cyclic-triangle count identifies four-clique number from its second and third cumulants.

## Assumptions and scope

Each existing undirected edge has exactly two possible directions, sampled independently with probability \(1/2\); edges not in \(G\) have no direction. Triangle and four-clique counts refer to unlabelled vertex subsets, not cyclic orientation choices. Every \(K_4\) has four faces, and every three-face collection is counted exactly once in the inner sum. The weights are fixed real numbers and may have either sign. All finite simple graphs, including edgeless graphs, are included; empty sums are zero. No claim is made for biased or dependent orientations.

## Proof

Fix a total ordering of the vertices. For an edge \(a<b\), let \(s_{ab}\in\{-1,+1\}\) equal \(+1\) when \(a\to b\) and \(-1\) otherwise. These are independent symmetric Rademacher variables. On a triangle \(a<b<c\), direct enumeration of the eight orientations gives
\[
I_{abc}-\frac14=\frac{s_{ab}s_{bc}-s_{ab}s_{ac}-s_{ac}s_{bc}}4. \tag{1}
\]
Consequently \(\mathbb E I_T=1/4\). For distinct triangles, the sets of degree-two Walsh monomials appearing in (1) are disjoint: a pair of graph edges belongs to at most one triangle of a simple graph. Orthogonality of distinct Rademacher monomials therefore gives \(\operatorname{Cov}(I_T,I_U)=0\). Since each indicator is Bernoulli, distinct indicators are independent, and \(\operatorname{Var}(I_T)=3/16\).

For three distinct triangles, expand the product of their centered indicators using (1). A term has nonzero expectation only if every graph edge-sign occurs an even number of times. Each term is a product of three pairs of *different* edge-signs, so this can happen only when the three selected edge pairs form a 3-cycle on three distinct edge-sign variables. Thus each pair of underlying triangles must share a graph edge, and these three common edges must be different. Three distinct vertex triples with this incidence configuration are precisely three faces of a \(K_4\): the shared edges form a three-edge star on four vertices. (If all three triangles share just one edge, an odd occurrence of that sign prevents the cancellation.) Thus every non-tetrahedral three-indicator centered moment vanishes.

For the exceptional \(K_4\) triple, it is impossible to orient three faces cyclically: in any orientation of \(K_4\), at most two triangular faces are directed cycles. This standard tetrahedral obstruction can also be proved by orienting the edges around one directed triangular face and checking the three choices of the fourth vertex's incident directions. Consequently the triple all-one probability is zero. Since each marginal equals \(1/4\) and each pair is independent, expanding the centered product gives the exceptional value \(-1/64\). For a triple of Bernoulli variables with the stated marginals and pairwise joint probabilities, the full 8-state distribution is uniquely determined by its all-one probability; therefore the nonexceptional vanishing centered moment gives full three-way independence, not merely zero third correlation.

For a single Bernoulli\((1/4)\) variable, the third centered moment is \(\tfrac14\cdot\tfrac34\cdot\tfrac12=3/32\). In expanding \(\kappa_3(Z_w)\), any term with exactly two equal triangle indices and a different third index has expectation zero because \((I_T-1/4)^2=(1/2)(I_T-1/4)+3/16\), and distinct indicators are independent. The all-equal terms yield \((3/32)\sum_Tw_T^3\). Each unordered exceptional triple of distinct faces contributes \(6(-1/64)\prod w_T=-3\prod w_T/32\) through its six orders. There are exactly four such triples per four-clique, and no triple is counted by two different four-cliques. This proves the weighted formula. The unweighted identities and the stated three-wise criterion follow immediately, with the latter's converse witnessed by any three faces of an existing four-clique.

## Verification

The supplied standard-library `verify.py` independently enumerates every fair edge orientation of every labelled simple graph with two through five vertices, with exact integer arithmetic. It verifies the unweighted and alternating-sign weighted first three moments, all pairwise joint probabilities, and the all-one probabilities for all distinct triangle triples, without sampling. The checked graph count is 1,098 and the number of three-triangle tests is 1,004. Run `python3 verify.py`. The code is a finite cross-check only; the general result follows from the Walsh support and tetrahedral arguments above.

## Relationship to prior work

Moon's *Topics on Tournaments*, Chapter 6 (original 1968; publicly released 2013 digital edition), records the classical random-tournament mean and variance and, citing Moran (1947), the exact third centered moment \(-3\binom n3(n-4)/32\). The present formula specializes to that **known** expression on a complete graph; this case is explicitly **not** claimed as a new result. The surviving contribution concerns arbitrary fixed underlying graphs, the exact support of the mixed third-cumulant tensor, its weighted local formula, and the if-and-only-if three-wise independence criterion.

Reiher, Rödl and Schacht, *On a generalisation of Mantel's theorem to uniformly dense hypergraphs*, Example 1.4, explicitly use the known fact that four tournament vertices span at most two cyclic triangles; that local impossibility is credited here. Their extremal hypergraph conclusions do not assert independence of other triples of triangle events or the weighted third cumulant for an arbitrary fixed graph. Allen and collaborators study the number of orientations avoiding directed cycles of specified lengths in typical random graphs, not the full finite-graph mixed cumulant tensor. Results concerning orientation questions in random *cyclic total orders* concern a different probability model from independent edge orientations, and do not yield the Bernoulli joint laws here.

## Limitations

This theorem describes only moments through order three and three-indicator independence. It does not classify higher joint laws or establish sample-optimal graph recovery. The complete-graph moment formula and the tetrahedral obstruction are historical inputs, not new discoveries. Equivalences in older literature on tournament dependency graphs or orientation statistics remain a priority risk. Reproducibility checks are exhaustive only up to five vertices; they do not replace the proof for arbitrary finite graphs. No independent mathematical audit has occurred.

## References

1. J. W. Moon, *Topics on Tournaments* (Holt, Rinehart and Winston, 1968), Ch. 6, digital edition released June 5, 2013, https://ftp.gwdg.de/pub/misc/gutenberg/4/2/8/3/42833/42833-pdf.pdf. Chapter 6, Exercise 3 credits Moran (1947) for the third moment.
2. C. Reiher, V. Rödl, M. Schacht, *On a generalisation of Mantel's theorem to uniformly dense hypergraphs*, Example 1.4, https://www.math.uni-hamburg.de/personen/reiher/artikel/3edges.pdf.
3. P. Allen, Y. Kohayakawa, G. O. Mota, R. F. Parente, *On the number of orientations of random graphs with no directed cycles of a given length*, *Electron. J. Combin.* 21(1), P1.52 (2014), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i1p52/pdf/.
