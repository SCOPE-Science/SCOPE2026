# Endpoint-exception correlations and a sharp boundary-pair crossover in random-source path outbreaks

## Finding

A uniform random source on a finite path produces a geometry-dependent sign law for eventual outbreak co-infection. On the path with vertices \(1,\ldots,n\), let \(X_i\) indicate that vertex \(i\) belongs to the open-edge component of an independently uniformly chosen source, with all edges retained independently with probability \(p\). For every \(n\ge3\), every \(0<p<1\), and every distinct \(i,j\) with \(1\le i<j\le n\):

1. The endpoint pair is always strictly anticorrelated: \(\operatorname{Cov}(X_1,X_n)<0\).
2. Every other pair is negatively correlated for sufficiently small \(p>0\), but strictly positively correlated for all \(p<1\) sufficiently close to one. More precisely, writing \(\varepsilon=1-p\),
   \[
   \operatorname{Cov}(X_i,X_j)=\frac{i(i-1)+(n-j)(n-j+1)}{2n}\,\varepsilon+O_n(\varepsilon^2),
   \]
   and the displayed coefficient is strictly positive exactly when \((i,j)\ne(1,n)\). The endpoint pair instead has
   \[
   \operatorname{Cov}(X_1,X_n)=-\frac{n^2-1}{12}\varepsilon^2+O_n(\varepsilon^3).
   \]
3. For the boundary-adjacent pair \((1,2)\), there is exactly one sign-switch probability \(p_n\in(0,1)\). The covariance is negative for \(0\le p<p_n\), zero at \(p_n\), and positive for \(p_n<p<1\). Its sharp large-path law is
   \[
   p_n=\frac1{2n}+\frac5{8n^2}+O(n^{-3}).
   \]

The second assertion is an existence-and-boundary classification, not a claim of unique thresholds for all other pairs. The three-vertex path is also a two-leaf star; the contribution is the path-family geometric dichotomy, including arbitrarily long paths, rather than novelty of that smallest graph alone.

## Assumptions and scope

Fix an integer \(n\ge3\). The undirected contact graph is the simple path \(P_n\). Choose a source \(S\) uniformly from its \(n\) vertices, independently of the edge states. Each edge is open with the same probability \(p\in[0,1]\), mutually independently. The final outbreak is exactly the connected open component containing \(S\). An infected vertex includes the initial source. Each \(X_v\) is a binary indicator of eventual infection, not current infectiousness at a finite time.

The independent-bond construction is a precise contagion model in its own right. It should not be conflated with arbitrary Markovian SIR processes, where transmission events sharing a random infectious duration can be dependent. No inference about general graphs, heterogeneous contact probabilities or correlated seeds is asserted.

For \(1\le i<j\le n\), put \(d=j-i\) and define
\[
G_i(p)=\sum_{v=1}^n p^{|v-i|},\qquad
H_{ij}(p)=d+1+\sum_{a=1}^{i-1}p^a+\sum_{b=1}^{n-j}p^b.
\]
The exact marginal and joint probabilities are
\[
\mathbb P(X_i=1)=\frac{G_i(p)}n,\qquad
\mathbb P(X_i=X_j=1)=\frac{p^d H_{ij}(p)}n,
\]
and therefore
\[
\operatorname{Cov}(X_i,X_j)=\frac{n p^d H_{ij}(p)-G_i(p)G_j(p)}{n^2}.
\]
These formulas also give a direct, finite exact calculation for any specified pair.

## Proof

**Exact probabilities.** Conditional on source \(S=v\), infecting \(i\) requires every edge between \(v\) and \(i\) to be open; this has probability \(p^{|v-i|}\). Infecting both \(i<j\) requires every edge in the smallest interval containing \(v,i,j\) to be open. The required number of edges is \(d\) if \(i\le v\le j\), \(d+i-v\) if \(v<i\), and \(d+v-j\) if \(v>j\). Summing over uniformly distributed \(v\) yields the claimed formulas.

**End-to-end strict negativity.** At the endpoints, \(G_1(p)=G_n(p)=\sum_{a=0}^{n-1}p^a\), whereas the joint probability is \(p^{n-1}\). Thus
\[
\operatorname{Cov}(X_1,X_n)=p^{n-1}-\left(\frac1n\sum_{a=0}^{n-1}p^a\right)^2.
\]
The strict arithmetic-geometric-mean inequality for the positive, unequal terms \(1,p,\ldots,p^{n-1}\) gives \(n^{-1}\sum p^a>p^{(n-1)/2}\) when \(0<p<1\). This proves strict negativity. Writing \(p=e^{-t}\) and using the variance \((n^2-1)/12\) of a uniform integer on \(\{0,\ldots,n-1\}\) gives the displayed quadratic expansion in \(\varepsilon=1-p\).

**High-transmissibility boundary classification.** Let \(Y_v=1-X_v\). Since \(\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(Y_i,Y_j)\), calculate their joint failure probability with \(p=1-\varepsilon\). With probability \(1-O_n(\varepsilon)\), all edges are open; with probability \(\varepsilon+O_n(\varepsilon^2)\), any particular single edge \((t,t+1)\) is the only closed edge. Both \(i<j\) fail exactly if either \(t<i\) and the source is on the left (probability \(t/n\)), or \(t\ge j\) and the source is on the right (probability \((n-t)/n\)). Therefore
\[
\mathbb P(Y_i=Y_j=1)=\frac\varepsilon n
\left(\sum_{t=1}^{i-1}t+\sum_{t=j}^{n-1}(n-t)\right)+O_n(\varepsilon^2).
\]
Each individual failure probability is \(O_n(\varepsilon)\), so the product of the marginals is \(O_n(\varepsilon^2)\). Simplifying the arithmetic sums proves the coefficient in the finding. It vanishes precisely for \(i=1,j=n\). At \(p=0\), the infected component consists only of its source, giving \(\operatorname{Cov}(X_i,X_j)=-1/n^2\) for every distinct pair; continuity proves the asserted negative low-\(p\) regime and at least one intermediate zero for every nonendpoint pair.

**Unique sign switch for the boundary-adjacent pair.** Set
\[
F_n(p)=n^2\operatorname{Cov}(X_1,X_2)
=n p\left(2+\sum_{a=1}^{n-2}p^a\right)
-\left(\sum_{a=0}^{n-1}p^a\right)
\left(1+2p+\sum_{a=2}^{n-2}p^a\right).
\]
Empty sums are zero. Since \(F_n(1)=0\), the quotient \(Q_n(p)=F_n(p)/(1-p)\) is a polynomial of degree \(2n-4\). Write \(A(v)=1+\operatorname{dist}(v,\{1,2\})\) and \(B(v,w)=v-1+|w-2|\) for \(v,w\in\{1,\ldots,n\}\). The identities
\[
F_n(p)=n\sum_{v=1}^{n}p^{A(v)}-\sum_{v,w=1}^{n}p^{B(v,w)}
\]
show that the coefficient of \(p^k\) in \(Q_n\) is
\[
a_k=n\#\{v:A(v)\le k\}-\#\{(v,w):B(v,w)\le k\}.
\]
At \(k=0\), \(a_0=-1\). For every integer \(1\le k\le2n-4\), the first count is \(\min(n,k+1)\). For each fixed \(w\), the second count has at most \(\min(n,k+1)\) choices of \(v\); it has strictly fewer for \(w=n\), since \(B(v,n)=v+n-3\). Consequently \(a_k>0\) throughout this range. Thus \(Q_n(p)=-1+\sum_{k=1}^{2n-4}a_kp^k\) is strictly increasing for \(p>0\). The preceding one-edge calculation gives \(Q_n(1)=n(n-1)(n-2)/2>0\), so exactly one root exists in \((0,1)\), with the claimed signs.

**Sharp crossover scale.** For fixed positive \(c\) and bounded \(d\), substituting \(p=c/n+d/n^2\) into the exact formula yields, uniformly on compact ranges of \(c,d\),
\[
F_n(p)=2c-1+\frac{2d+c^2-3c}{n}+O(n^{-2}).
\]
The monotone-polynomial root therefore has leading coefficient \(c=1/2\); cancellation of the next coefficient gives \(d=5/8\). The derivative \(F_n'(p)=2n+O(1)\) uniformly for \(p=1/(2n)+O(n^{-2})\), so the residual \(O(n^{-2})\) implies a root error \(O(n^{-3})\). This proves the expansion.

## Verification

The independent Python 3 script `check.py` uses only standard-library exact fractions and enumerates every open-edge configuration and every source for paths through nine vertices. It compares computed marginals and joint events with the closed formulas for three rational transmission probabilities, checks the strict polynomial coefficients for every path length from three through one hundred, and checks the single-edge expansion coefficient across all pairs for lengths through thirty. It also checks endpoint strict negativity for lengths through sixty. Executing `python3 check.py` from the directory containing the script produces `PASS: 20483 exact rational assertions`. The analytical proofs, not the finite enumerations, establish the unrestricted statements.

For \(n=4\) and \(p=1/2\), the exact covariance of the boundary-adjacent pair is \(41/512>0\), while that of the two endpoints is \(-97/1024<0\). This displays both signs simultaneously under the same transmission model.

## Relationship to prior work

Kenah and Robins (2007) give the epidemic-percolation network framework and connect outbreaks to percolation components. Van den Berg, Häggström and Kahn (2004) establish conditional positive/negative association theorems for fixed-root percolation clusters; their conditioning and observables differ from unconditional node indicators with a uniformly random source. Sharkey et al. (2013) derive exact tree-epidemic state equations, while Hall and Siebert (2021 preprint) study exact single-root tree trajectories; neither develops the random-root final-status pair covariance sign geometry claimed here.

Cator and Van Mieghem (2014), together with Rodríguez, Roldán-Correa and Valencia (2018), discuss correlation of contemporaneous infectious-state variables and an associated controversy about Markovian SIR dynamics. Those are not the eventually-ever-infected indicators of the present independent-bond, random-source model. The earlier frameworks can be used to motivate or derive component probabilities, but their displayed conclusions do not imply the endpoint-exception and sharp boundary-adjacent threshold theorem without an additional calculation.

## Limitations

The model uses independently retained undirected bonds and exactly one uniformly distributed outbreak source. A general stochastic SIR epidemic can have dependencies between outward transmissions, and finite-time infectious states are different variables. The theorem does not claim one sign transition for every nonendpoint pair, nor a universal transition rate for heterogeneous probabilities or graphs other than paths. Literature priority remains provisional because an equivalent identity might appear under reliability, influence-propagation or stochastic-order terminology. The finite checker is not a formal proof and does not establish anything about an infinite network.

## References

- J. van den Berg, O. Häggström, J. Kahn, *Some Conditional Correlation Inequalities for Percolation and Related Processes*, arXiv:math/0408176 (first posted 2004-08-13). https://arxiv.org/html/math/0408176v1
- E. Kenah, J. M. Robins, *Network-based analysis of stochastic SIR epidemic models with random and proportionate mixing*, Journal of Theoretical Biology (online 2007-09-15). https://pmc.ncbi.nlm.nih.gov/articles/PMC2186204/
- K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs* (online 2013-12-18). https://link.springer.com/article/10.1007/s11538-013-9923-5
- E. Cator, P. Van Mieghem, *Nodal infection in Markovian susceptible-infected-susceptible and susceptible-infected-removed epidemics on networks are non-negatively correlated* (2014-05-01). https://doi.org/10.1103/PhysRevE.89.052802
- P. M. Rodríguez, A. Roldán-Correa, L. A. Valencia, *Comment on Nodal infection in Markovian ...* (arXiv 2018-07-18). https://arxiv.org/abs/1807.06909
- C. L. Hall, B. A. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation* (arXiv 2021-08-16). https://arxiv.org/abs/2108.07128
