# Four vertices are sharp for a peak-capacity reversal in the Markovian SIR model

## Finding

Consider a finite connected, simple, undirected and unweighted contact graph \(G\). Start a continuous-time susceptible–infectious–removed (SIR) epidemic with exactly one infectious vertex \(v\), recovery rate \(1\) per infectious vertex, and infection rate \(\beta>0\) per infectious–susceptible edge. Write
\[
M_v=\max_{t\ge0}|I_t|,\qquad R_k(v;\beta)=\Pr_v(M_v\ge k).
\]
For any two capacity thresholds \(2\le k,\ell\le |V(G)|\), say their seed objectives *disagree* if the sets of maximizing vertices for \(R_k\) and \(R_\ell\) are disjoint.

**Theorem.** No connected graph with at most three vertices exhibits disagreement for any \(\beta>0\). Of the six connected four-vertex graph isomorphism classes, exactly the triangle with one pendant leaf (the *paw*) exhibits disagreement for some \(\beta>0\). Label its vertices \(0,1,2,3\) and edges
\[
E=\{03,12,13,23\},
\]
where \(3\) is the degree-three hub, \(1,2\) are the triangle's degree-two vertices, and \(0\) is the leaf. Let \(\beta_*\) be the unique positive root of
\[
q(\beta)=2\beta^4-32\beta^3-58\beta^2-33\beta-6;
\qquad \beta_*=17.6923778837\ldots.
\]
For all \(\beta>0\), the unique maximizer of \(R_2\) and of \(R_4\) is \(3\). For \(0<\beta<\beta_*\), the unique maximizer of \(R_3\) is \(3\); at equality its maximizers are \(1,2,3\); for \(\beta>\beta_*\), its maximizers are \(1,2\). Consequently four vertices are sharp for the re-entrant capacity ordering \(3\to\{1,2\}\to3\) as the target peak rises through \(2,3,4\).

## Assumptions and scope

Each vertex undergoes at most one infection and then permanent removal. Event clocks are independent and exponential. Peak size refers to the maximum along an individual realized epidemic, **not** the maximum of the expected prevalence curve, and neither to final outbreak size nor to the expected peak. All rates may be multiplied by a common positive constant; only the ratio \(\beta\) of transmission to recovery matters. The optimization varies the seed vertex while the contact graph and rates remain fixed. Statements are for connected graphs on \(2\), \(3\), or \(4\) vertices; no classification of larger, directed, weighted, or non-Markovian networks is claimed.

## Proof

For a susceptible set \(S\), infectious set \(I\), and target \(k\), let \(f_k(S,I)\) be the probability of ever reaching \(k\) simultaneous infectious vertices from this state. If \(|I|\ge k\), then \(f_k=1\). If \(I=\varnothing\) and \(|I|<k\), then \(f_k=0\). Otherwise put \(m_x=|N(x)\cap I|\) for each \(x\in S\) and \(\Lambda=|I|+\beta\sum_{x\in S}m_x\). First-event decomposition gives the **exact rational recurrence**
\[
f_k(S,I)=\frac{\sum_{y\in I}f_k(S,I\setminus\{y\})+\beta\sum_{x\in S}m_x f_k(S\setminus\{x\},I\cup\{x\})}{\Lambda}.
\]
Every transition removes an individual from \(S\) or from \(I\), and no vertex returns to \(S\), hence this recursion terminates. With \(S=V\setminus\{v\}\) and \(I=\{v\}\), it computes \(R_k(v;\beta)\) without approximation.

The connected simple graphs of orders \(2,3,4\) have respectively \(1,2,6\) unlabeled types: \(K_2\); \(P_3,K_3\); and \(P_4,K_{1,3}\), paw, \(C_4\), \(K_4\) minus one edge, \(K_4\). Applying the recurrence and reducing rational differences gives these maximizers for **every** \(\beta>0\): on \(P_3\), the center; on \(P_4\), its two internal vertices; on \(K_{1,3}\), the hub; on \(K_4\) minus one edge, the two degree-three vertices; and on each complete graph or cycle \(C_4\), all vertices. Each comparison is a rational function with positive denominator and numerator having nonnegative coefficients, except for the paw's middle-capacity comparison below. The attached checker constructs all \(43\) connected labeled graphs on two through four vertices, reduces them to these nine isomorphism classes, and verifies all \(82\) required nontrivial/routine winner comparisons symbolically by nonnegative polynomial coefficients.

For the paw, the decisive comparison between a degree-two triangle vertex and the hub is
\[
R_3(1;\beta)-R_3(3;\beta)=
\frac{\beta^2 q(\beta)}{(\beta+1)^2(\beta+2)(2\beta+1)^2(3\beta+1)(3\beta+2)}.
\]
Both degree-two triangle vertices are equivalent. The leaf is always inferior to them at capacity three, because
\[
R_3(1;\beta)-R_3(0;\beta)=
\frac{\beta^2(10\beta^4+34\beta^3+48\beta^2+29\beta+6)}{(\beta+1)^3(\beta+2)(2\beta+1)^2(3\beta+2)}>0.
\]
At the other capacities,
\[
R_2(1;\beta)-R_2(3;\beta)=-\frac{\beta}{(2\beta+1)(3\beta+1)}<0,
\]
\[
R_4(1;\beta)-R_4(3;\beta)=-\frac{\beta^3(29\beta^2+45\beta+18)}{(\beta+1)(\beta+3)(2\beta+1)(2\beta+3)(3\beta+1)(3\beta+2)}<0.
\]
The leaf also loses to the hub at capacities two and four by the same exact recurrence. The coefficient signs of \(q\) have precisely one sign change, while \(q(0)<0\) and \(q(\beta)\to+\infty\); Descartes' rule therefore gives exactly one positive root. Direct substitution gives \(q(17)<0<q(18)\). All the asserted regimes and their strictness follow.

## Verification

The standalone `verify.py` uses symbolic rational first-event recursion, enumerates all \(43\) connected labeled graphs through order four, reduces to the \(1+2+6\) graph isomorphism classes, and certifies \(82\) pairwise analytic comparisons by coefficient signs. It independently sums the probabilities of all possible event paths for all twelve seed/threshold combinations on the paw at \(\beta=18\), obtaining exact agreement with the symbolic calculation. For instance, for the hub and a triangle vertex, the three respective threshold differences at \(\beta=18\) are
\[
R_2(1)-R_2(3)=-\frac{18}{2035},\quad
R_3(1)-R_3(3)=\frac{39852}{951352325},\quad
R_4(1)-R_4(3)=-\frac{828144}{24629605}.
\]
Run `python verify.py` with Python 3 and SymPy. These computations are certificates for the stated finite classification; the proof of the continuous parameter regimes is polynomial positivity and the unique-root argument, not numerical sampling.

## Relationship to prior work

Van Mieghem (2014) develops exact Markovian SIR equations and describes the **maximum over time of mean prevalence**, a distinct statistic from the event \(\max_t |I_t|\ge k\). Economou, Gómez-Corral and López García (2015), Section 3.1, derive maximum-infective-count distributions for **SIS**, allowing reinfection, rather than permanent removal. Holme (2017) exhaustively analyzes small-network node importance under SIR through **expected final outbreak size, vaccination, and sentinel time**. Bucur and Holme (2020) revisit exact **expected final outbreak size** on small graphs. None of the inspected comparisons implies the specified paw-graph threshold or the minimum-order classification. The exact state-transition method is standard; the sharp optimizer classification and quartic switching threshold are the specific subject here.

## Limitations

This exact result does not apply to expected peak prevalence, alternative infection/recovery distributions, heterogeneous rates, contact-network interventions, or larger graphs. It is not an empirical hospital-capacity prediction. Historical priority is not independently established; the closest SIS peak-distribution study is methodologically related, and uninspected historical tables may contain the same special case.

## References

1. P. Van Mieghem, *Exact Markovian SIR and SIS epidemics on networks and an upper bound for the epidemic threshold*, arXiv:1402.1731v1 (public 2014-02-07), https://arxiv.org/abs/1402.1731.
2. A. Economou, A. Gómez-Corral, M. López García, *A stochastic SIS epidemic model with heterogeneous contacts*, Physica A 421 (2015), 78–97; online 2014-11-13, https://doi.org/10.1016/j.physa.2014.10.054.
3. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, Phys. Rev. E 96 (2017), 062305; arXiv:1708.06456, https://arxiv.org/abs/1708.06456.
4. D. Bucur and P. Holme, *Beyond ranking nodes: Predicting epidemic outbreak sizes by network centralities*, PLOS Comput. Biol. 16 (2020), e1008052, https://doi.org/10.1371/journal.pcbi.1008052.
