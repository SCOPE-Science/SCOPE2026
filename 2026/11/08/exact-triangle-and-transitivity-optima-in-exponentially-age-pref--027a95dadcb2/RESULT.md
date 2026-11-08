# Exact triangle and transitivity optima in exponentially age-preferential random graphs

## Finding
Consider the two-parent, with-replacement, exponentially age-preferential random multigraph of Tang, Wang and Wu, after suppressing parallel edges to form a simple graph. Write \(q=e^{-\beta}\in(0,1)\). For the simple graph on vertices \(0,\ldots,n\), let \(T_n\) denote its number of unoriented triangles and \(W_n=\sum_v\binom{\deg(v)}2\) its number of connected (centered) vertex triples. Then, almost surely,
\[
\frac{T_n}{n}\longrightarrow t(q)
=\frac{2q(1-q)(3q^2+2q+1)}{(1+q)^2(1+q+q^2)},
\]
\[
\frac{W_n}{n}\longrightarrow w(q)
=\frac{20q^6+28q^5+43q^4+39q^3+26q^2+11q+1}
{(1+q)^2(1+q^2)(1+q+q^2)}.
\]
Consequently the global transitivity (closed-triplet proportion) converges almost surely to
\[
\frac{3T_n}{W_n}\longrightarrow c(q)=\frac{6q(1-q)(1+q^2)(3q^2+2q+1)}{20q^6+28q^5+43q^4+39q^3+26q^2+11q+1}.
\]
Each of \(t\) and \(c\) has precisely one maximizer on \((0,1)\), but **these maximizers are different**. The triangle-density optimizer \(q_T\) is the unique positive zero of
\[
P_T(q)=10q^5+16q^4+13q^3-q^2-q-1,
\]
whereas the transitivity optimizer \(q_C\) is the unique positive zero of
\[
P_C(q)=104q^{10}+178q^9+372q^8+426q^7+435q^6+276q^5+177q^4+42q^3+9q^2-2q-1.
\]
In particular, \(q_C\in(0.216,0.218)\), \(q_T\in(0.420,0.421)\), and \(q_C<q_T\). Numerically,
\[
(q_T,t(q_T))\approx(0.420413388248476,0.358584008455502),
\quad(q_C,c(q_C))\approx(0.216931020265475,0.328381073861177).
\]
In the original parameterization, the respective optimizers are \(\beta_T\approx0.866516794034297\) and \(\beta_C\approx1.528175854936848\).

## Assumptions and scope
Start at vertex \(0\). For each integer \(j\ge1\), introduce vertex \(j\) with two independent ordered parent choices from \(0,\ldots,j-1\), with
\[
\Pr(P_{j,r}=k)=\frac{e^{\beta k}}{\sum_{h=0}^{j-1}e^{\beta h}}
=\frac{(1-q)q^{j-1-k}}{1-q^j},\qquad r\in\{1,2\}.
\]
Parent choices at different arrivals are independent. Multiple selections of the same parent create parallel edges in the original multigraph. For the finding, **replace parallel edges by one edge**, then count only ordinary triangles and ordinary simple-graph degrees. This projection is essential for the stated constants. The number of vertices at the terminal time is \(n+1\), so normalization by \(n\) is equivalent asymptotically to normalization by the number of vertices. Every assertion holds for each fixed \(\beta>0\), not uniformly as \(\beta\) varies with \(n\). Global transitivity uses the standard convention \(3T_n/W_n\), with \(W_n>0\) for all sufficiently large \(n\) almost surely.

## Proof
**1. Stationary geometric-age coupling.** On a two-sided index set \(j\in\mathbb Z\), take i.i.d. pairs \((A_{j,1},A_{j,2})\), with independent geometric components
\[
\Pr(A_{j,r}=d)=p_d=(1-q)q^{d-1},\qquad d\ge1.
\]
Connect \(j\) to \(j-A_{j,1}\) and \(j-A_{j,2}\), retaining one edge for duplicate selections. This gives a stationary ergodic locally finite simple graph \(H\): the expected number of distinct later neighbors of a vertex is
\(\sum_{d\ge1}(2p_d-p_d^2)<\infty\), hence the actual number is finite almost surely. In fact its moments are finite, since it is a sum of independent Bernoulli variables with bounded sum of success probabilities.

The finite-model parent-age distribution at step \(j\) is exactly the geometric law conditioned on the event \(A_{j,r}\le j\). Couple it to the two-sided geometric variable so that the two choices agree when \(A_{j,r}\le j\), and otherwise independently redraw from that conditional law. This coupling has disagreement probability at most \(2q^j\) at step \(j\). By the first Borel–Cantelli lemma, only finitely many arrivals have any modified edge, almost surely. Both the two-sided graph and the projected growing graph have almost surely finite degrees at every vertex. Therefore those finitely many changed edges alter the total triangle count and centered-triple count by at most a finite random constant, uniformly in \(n\), when the growing graph is compared with the induced stationary graph \(H[\{0,\ldots,n\}]\).

To justify motif laws for the induced graph, for each fixed range \(R\) discard from \(H\) every edge longer than \(R\), obtaining a stationary ergodic finite-range graph \(H^{(R)}\). For each \(R\), its total triangle and centered-triple counts in an interval differ from the sums of the corresponding whole-graph vertex-local counts by at most a deterministic constant depending on \(R\): only vertices within distance \(R\) of either boundary are affected, and all degrees in \(H^{(R)}\) are at most \(2+2R\). Birkhoff's theorem thus supplies the almost-sure per-vertex density of each motif for \(H^{(R)}\). The motif counts are monotone under edge addition, and the corresponding local counts in \(H^{(R)}\) increase to those of \(H\) as \(R\to\infty\), with finite means. Sandwich the interval motif counts between the finite-range counts and the sums of the full local motif counts; then apply Birkhoff and monotone convergence. This proves almost-sure convergence of the untruncated motif densities and transfers it to the original growing graph by the coupling.

**2. Triangle intensity.** A triangle with youngest vertex \(j\), middle vertex \(i=j-a\), and oldest vertex \(k=i-b\) requires, at arrival \(j\), choosing the distinct parents \(i,k\) in either order, and, at arrival \(i\), choosing \(k\) at least once. These are independent events. Thus the stationary intensity is
\[
t(q)=\sum_{a,b\ge1}2p_a p_{a+b}(2p_b-p_b^2).
\]
Two geometric-series sums give
\[
t(q)=\frac{4q(1-q)}{(1+q)^2}
-\frac{2q(1-q)^4}{(1-q^2)(1-q^3)}
=\frac{2q(1-q)(3q^2+2q+1)}{(1+q)^2(1+q+q^2)}.
\]
Every triangle is counted exactly once at its youngest vertex, even though repeated parent choices are allowed in the original multigraph.

**3. Connected triples.** For a typical stationary vertex, let \(O\) be its number of distinct older neighbors and \(I\) its number of distinct younger neighbors. These counts are independent. Put
\[
s=\mathbb E O=2-\sum_{d\ge1}p_d^2=\frac{1+3q}{1+q}.
\]
Then \(\mathbb E\binom O2=\Pr(A_{0,1}\ne A_{0,2})=2q/(1+q)\). Writing \(r_d=2p_d-p_d^2\), the incoming-neighbor indicators are independent, \(\sum_d r_d=s\), and
\[
R=\sum_{d\ge1}r_d^2
=\frac{4(1-q)}{1+q}
-\frac{4(1-q)^2}{1+q+q^2}
+\frac{(1-q)^3}{1+q+q^2+q^3}.
\]
Therefore
\[
\mathbb E\binom{O+I}{2}
=\frac{2q}{1+q}+s^2+\frac{s^2-R}{2}=w(q),
\]
which simplifies to the rational expression stated above. Positivity of \(w(q)\) proves the asserted transitivity ratio limit.

**4. Strict and separated extrema.** Direct polynomial differentiation, with strictly positive denominators on \((0,1)\), gives
\[
t'(q)=-\frac{2P_T(q)}{(1+q)^3(1+q+q^2)^2},
\quad
c'(q)=-\frac{6P_C(q)}{(20q^6+28q^5+43q^4+39q^3+26q^2+11q+1)^2}.
\]
In increasing-degree coefficient order, each of \(P_T\) and \(P_C\) has exactly one sign change: its constant and low-order coefficients are negative, and all subsequent coefficients are positive. By Descartes' rule of signs each has at most one positive root. The constant terms are negative and the values at \(q=1\) are positive, so each has exactly one root in \((0,1)\). The derivatives switch from positive to negative there, giving unique strict global maxima. Evaluating the two integer polynomials at the rational endpoints of the disjoint isolating intervals above proves that the two maximizers differ and gives their strict order.

## Verification
The accompanying `verify.py` (Python 3, standard library only) independently enumerates every ordered two-parent history for small graph sizes and compares exact rational triangle and wedge expectations with independently derived finite-sum formulas, for several rational values of \(q\). It also checks the two stationary rational identities, controlled geometric-sum truncations, exact integer-polynomial differentiation identities, and rational isolating signs. It prints `PASS 58 ...` when all checks succeed. These checks are finite and do not themselves prove the almost-sure limits: those follow from the stationary coupling, local integrability, ergodic theorem, and monotone approximation in the proof.

## Relationship to prior work
Aguech, Mahmoud, Mohamed and Yang, *Exponentially preferential trees*, *Network Science* 13 (2025), e5, DOI 10.1017/nws.2025.3 (first public release verified 2025-04-14), introduce exponential-label attachment in its one-parent tree form. This finding studies the **natural independent two-parent extension** of their exponential-weight rule, with repeated choices allowed and multiplicities suppressed before motif counting. The one-parent tree has no triangles, so its degree results do not imply these formulas. The 2025 paper is the dated motivating source for this finding.

Pachon and Stephenson, *Clustering in a preferential attachment network with triangles*, arXiv:2504.02717v1 (2025-04-03), study a different model: an affine-degree choice mixed with a deliberate triangle-forming edge-selection operation. Their full-text clustering theorems do not imply the geometric-age model's rational constants or its two distinct optima.

Tang, Wang and Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329v1, was publicly posted **2026-11-02**. It independently studies the same multi-parent with-replacement extension and establishes random-walk recurrence and infinite collisions. Its complete text was inspected **only as a contemporaneous novelty comparison**, not used as the earliest motivating source; it does not provide the motif and optimization formulas. It does not alter the 2025-04-14 public date of the earlier exponential-weight rule from which the present structural question is developed.

Related age-dependent random connection models, including Gracar, Grauer, Lüchtrath and Mörters, arXiv:1810.03429, use spatial point processes and relative-age connection probabilities rather than these independent geometrically distributed parent ages. Their local-limit/clustering results are relevant methodological background but do not identify this model's rational expressions. Prior accessible work on the *same age-preferential extension* determined maximum-degree scaling, not triangles or centered triples. Targeted published-research searches and semantic comparisons to accessible mathematical records found no theorem covering the exact rational formulas and their unequal optimizers. Absence of a located antecedent is not a guarantee of absolute historical priority.

## Limitations
The theorem concerns simple-graph projection of the \(m=2\) with-replacement model at fixed \(\beta>0\). It does not give the number of triangles counted with parallel-edge multiplicity, the average *local* clustering coefficient, the case \(m\ge3\), an edge-density graphon limit, any fluctuation theorem, or quantitative convergence rates. The two endpoint limits \(q\to0\) and \(q\to1\) are limits of the **fixed-parameter density formulas**, not a theorem for sequences of parameters depending on graph size. Historical priority against all unpublished or unindexed literature has not been certified.

## References
1. R. Aguech, H. Mahmoud, H. Mohamed and Z. Yang. *Exponentially preferential trees*. *Network Science* **13** (2025), e5. Published online 2025-04-14. https://doi.org/10.1017/nws.2025.3
2. A. Pachon and R. Stephenson. *Clustering in a preferential attachment network with triangles*. arXiv:2504.02717v1, posted 2025-04-03. https://arxiv.org/html/2504.02717v1
3. J. Tang, F. Wang and X.-Y. Wu. *Random Walk on age-preferential random growth processes*. arXiv:2611.02329v1, posted 2026-11-02 (related comparison only). https://arxiv.org/html/2611.02329v1
4. P. Gracar, A. Grauer, L. Lüchtrath and P. Mörters. *The age-dependent random connection model*. arXiv:1810.03429, posted 2018-10-08. https://arxiv.org/abs/1810.03429
