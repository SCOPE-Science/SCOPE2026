# Complete covariance sign diagram for induced triad counts in \(G(n,p)\)

## Finding

For an undirected binomial random graph \(G(n,p)\), the six mixed covariances of the complete four-class induced three-vertex census have an exact sign diagram. Five pairs have positive-covariance regimes: four have exactly one threshold and the one-edge/two-edge pair has two thresholds, hence negative dependence can reappear at intermediate edge densities. The remaining empty-triad/triangle pair is always negatively correlated.

Let \(N_j\) count unordered triples of vertices whose induced subgraph has exactly \(j\) edges, for \(j\in\{0,1,2,3\}\). For every integer \(n\ge3\) and every \(0<p<1\), define
\[
q_j=\binom{3}{j}p^j(1-p)^{3-j},\qquad d_j=\frac{q_j(j-3p)}{3p(1-p)}.
\]
The entire exact covariance matrix has entries
\[
\operatorname{Cov}(N_i,N_j)=\binom n3\left[\mathbf1_{i=j}q_i-q_iq_j+3(n-3)p(1-p)d_i d_j\right].
\]
For \(n=3\), all six mixed covariances are negative. For \(n\ge4\), set
\[
D=3n-8,\quad a=\frac{n-2}{D},\quad b=\frac{2n-5}{D},\quad c=\frac{n-3}{D},\quad d=\frac{2(n-3)}{D},\quad u_\pm=\frac{1\pm\sqrt{n/(3D)}}2.
\]
Then the covariance for each listed pair of classes is *positive* on exactly the stated open set:

| Pair of induced edge counts | Precisely positive when |
|---|---|
| \((0,1)\) | \(p>a\) |
| \((0,2)\) | \(p>b\) |
| \((0,3)\) | never |
| \((1,2)\) | \(p<u_-\) or \(p>u_+\) |
| \((1,3)\) | \(p<c\) |
| \((2,3)\) | \(p<d\) |

For each pair other than \((0,3)\), covariance is zero precisely at its displayed threshold(s) and is strictly negative elsewhere. In particular \(0<u_-<1/3<2/3<u_+<1\); there are two actual interior sign changes for the one-edge/two-edge pair for every \(n\ge4\).

## Assumptions and scope

The vertex set is fixed and labeled, of size integer \(n\ge3\). Every undirected edge is present independently with the same probability \(p\in(0,1)\). All counted triples are unordered sets of three distinct vertices, and their types include *absence* as well as presence of edges (induced counts). No asymptotic scaling, connectedness condition, graph conditioning, or independence among different triple types is assumed.

## Proof

For each triple \(S\), write \(I_j(S)\) for its type-\(j\) indicator. Every fixed triple has type probabilities \(q_j\). The covariance for two indicators on the *same* triple is exactly \(\mathbf1_{i=j}q_i-q_iq_j\). Two distinct triples with at most one common vertex depend on disjoint edge sets and hence are independent.

For two distinct triples sharing exactly one edge, let \(E\) be the indicator of that edge. Conditional on \(E\), their four other edges are mutually independent. Let \(h_j(e)=\Pr(\operatorname{Bin}(2,p)=j-e)\), taking probabilities outside \(\{0,1,2\}\) to be zero. The law of total covariance gives exactly \(p(1-p)[h_i(1)-h_i(0)][h_j(1)-h_j(0)]\). Differentiating the elementary binomial mass polynomial (or expanding the two cases) shows
\[
h_j(1)-h_j(0)=\frac{q_j(j-3p)}{3p(1-p)}=d_j.
\]
For any first triple there are precisely \(3(n-3)\) ordered choices of a distinct second triple sharing one of its three edges. Summing the two overlap cases over all ordered pairs of triples proves the covariance matrix formula for all \(n\ge3\).

For distinct \(i,j\), every factor outside the square brackets in
\[
\operatorname{Cov}(N_i,N_j)=\binom n3\frac{q_iq_j}{3p(1-p)}\big[(n-3)(i-3p)(j-3p)-3p(1-p)\big]
\]
is strictly positive. Write the bracket as \(R_{ij}(p)\). Elementary factorization gives
\[
\begin{aligned}
R_{01}(p)&=3p(Dp-(n-2)),\\
R_{02}(p)&=3p(Dp-(2n-5)),\\
R_{03}(p)&=-3p(1-p)D,\\
R_{13}(p)&=3(1-p)((n-3)-Dp),\\
R_{23}(p)&=3(1-p)(2(n-3)-Dp),\\
R_{12}(p)&=3D(p-u_-)(p-u_+).
\end{aligned}
\]
These factors prove all the stated signs and identify every equality case. If \(n=3\), distinct types are mutually exclusive indicators on the unique triple, so every mixed covariance is \(-q_iq_j<0\). For \(n\ge4\), the discriminant of \(R_{12}\) is positive, and \(n/[3(3n-8)]\) lies strictly between \(1/9\) and \(1\), establishing the positions of the two roots and concluding the classification.

## Verification

A standalone exact-rational checker `verify.py` enumerates all labeled simple graphs on three, four, and five vertices for seven rational edge probabilities, reconstructs the four triad counts, and compares every matrix entry to the closed formula. It checks 406 exact assertions, including threshold-sign comparisons. This is independent finite corroboration; the universal quantifiers are established by the preceding overlap argument and polynomial sign factorizations, not by the enumeration.

Run the checker from the extracted package directory using `python verify.py` with Python 3 and no third-party packages.

## Relationship to prior work

Induced motif counts and graph sampling are established statistical tools. Bhattacharya, Das and Mukherjee (arXiv:2011.03026, first posted November 5, 2020) analyze motif estimators in a *vertex-sampling* model, including Erdős–Rényi parent graphs; their questions concern consistency and asymptotic normality rather than the exact joint covariance-sign diagram for four induced triple classes in an unsampled binomial random graph. Their general sampling results do not directly state the all-six-pair thresholds above.

Wasserman's 1975/1977 work concerns a *directed* social-network triad census under a different distribution conditioned on individual choice counts. Its covariance-matrix methodology is important prior context, but its differing random-graph distribution does not directly furnish these six numerical sign thresholds. The complete original full text was not available for comparison, so possible implicit prior coverage remains a priority risk. Known general subgraph covariance methods also make a previously unstated equivalent possible; absence from search results alone is not proof of novelty.

## Limitations

The theorem is restricted to independent-edge undirected \(G(n,p)\) and triads defined by their count of present edges. It does not establish joint normality, confidence intervals, or the corresponding sign diagram for directed graphs, fixed-edge-count random graphs, arbitrary inhomogeneous edge laws or motifs on four or more vertices. The calculations are exact; historical originality remains subject to further literature assessment.

## References

1. B. B. Bhattacharya, S. Das and S. Mukherjee, *Motif Estimation via Subgraph Sampling: The Fourth Moment Phenomenon*, arXiv:2011.03026, first posted 2020-11-05. https://arxiv.org/abs/2011.03026
2. S. S. Wasserman, *Random Directed Graph Distributions in the Triad Census in Social Networks*, NBER Working Paper 0113, 1975 (subsequently 1977). https://www.nber.org/papers/w0113
