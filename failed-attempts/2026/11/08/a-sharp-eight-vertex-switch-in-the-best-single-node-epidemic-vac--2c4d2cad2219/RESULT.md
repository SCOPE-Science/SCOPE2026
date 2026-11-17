# A sharp eight-vertex switch in the best single-node epidemic vaccination

## Finding

**Theorem (first tree-order switch).** Let \(T\) be a finite tree on \(n\ge2\) vertices. One vertex \(v\) is perfectly vaccinated and removed before an epidemic. From the \(n-1\) survivors, choose one initial infected individual uniformly. Each contact edge transmits independently with the same probability \(p\in(0,1)\), so the final infected set is the open bond-percolation component of that initial individual. Write \(E_T(v;p)\) for the mean number eventually infected, including the seed.

**(a)** On every tree with \(2\le n\le7\) vertices, there exists a *single maximum-degree vertex* \(v_*\) that minimizes \(E_T(v;p)\) simultaneously for **all** \(p\in(0,1)\).

**(b)** For the eight-vertex tree with vertices \(0,1,\ldots,7\) and edges
\[
\{01,02,03,34,45,56,67\},
\]
there is no vaccination vertex optimal over all transmissibilities. Let \(p_*\in(0,1)\) be the unique root of
\[
p_*^3+p_*^2=1,\qquad p_*\approx0.75487766624669.
\]
For \(0<p<p_*\) the unique optimum is the degree-three hub \(v=0\). For \(p_*<p<1\) it is the first handle vertex \(v=3\). Exactly at \(p=p_*\), vertices \(0\) and \(3\) tie and all other vertices are strictly worse. Consequently eight is the smallest tree order admitting a change in its optimal single-vaccine location as \(p\) varies.

The exact comparison is
\[
E_T(3;p)-E_T(0;p)=\frac{2p}{7}(1-p^2-p^3).
\]
At \(p=1/2\), hub vaccination yields \(15/8=1.875\) expected infections versus \(55/28\approx1.964286\) at the handle. At \(p=9/10\), these become approximately \(3.326886\) versus \(3.188286\), reversing the preferred choice.

## Assumptions and scope

The network is a finite, simple, undirected *tree*. Exactly one vertex is vaccinated before the seed is sampled, and vaccinated individuals cannot be infected or transmit. Transmissions along different remaining edges are independent Bernoulli events with common \(p\). The initial seed is uniform over the remaining \(n-1\) vertices. The objective is *expected final outbreak size* per one seed, not the probability of a large outbreak, extinction time, vaccination cost, the spectral invasion threshold, or influence maximization from a fixed seed.

The phrase "smallest tree order" refers to this precise model and outcome. It does not assert that eight is minimal among *all connected graphs*: cyclic graphs have different behavior. The endpoint \(p=0\) gives identical outbreak size one for all vaccinations, and \(p=1\) may introduce additional ties. Therefore the uniqueness assertions in (b) are explicitly restricted to \(0<p<1\).

## Proof

**1. Pair-distance identity.** For any tree \(T\) on \(n\) vertices and deleted \(v\), define \(a_d(v)\) as the number of unordered pairs of distinct surviving vertices at distance exactly \(d\) within one component of \(T-v\). Since trees have unique paths, such a pair is connected in the open-edge graph if and only if all \(d\) edges of that path transmit, with probability \(p^d\). For a realized percolation with component sizes \(s_1,\dots,s_k\) summing to \(n-1\), the conditional average seed-component size is \(\sum_j s_j^2/(n-1)\). Counting ordered pairs, then taking expectations, gives the *exact finite identity*
\[
E_T(v;p)=1+\frac{2}{n-1}\sum_{d=1}^{n-2}a_d(v)p^d. \tag{1}
\]
No approximation, asymptotic limit, or independence between different infected branches is used in (1).

**2. Finite exhaustive certificate for part (a).** Every labelled tree on \(n\ge2\) labelled vertices has a unique Prüfer sequence of length \(n-2\). Enumerate all \(n^{n-2}\) sequences for each \(n\in\{2,3,4,5,6,7\}\). For each corresponding tree and each possible vaccinated vertex, calculate the integer vector \((a_0(v),a_1(v),\ldots,a_{n-2}(v))\), with \(a_0(v)=0\), by a breadth-first search in the remaining forest. Let \(m=n-2\). For a candidate maximum-degree vertex \(v\), the difference polynomial against competitor \(w\) is
\[
F_w(p)-F_v(p)=\sum_{d=0}^m c_dp^d,
\qquad F_v(p)=\sum_{d=0}^m a_d(v)p^d.
\]
Convert it into the degree-\(m\) Bernstein basis. Its coefficient of \(\binom mjp^j(1-p)^{m-j}\) is
\[
b_j=\sum_{d=0}^j c_d\frac{\binom jd}{\binom md}\qquad (0\le j\le m).
\]
The verifier evaluates \(m!b_j\) *exactly as integers*, checks \(b_j\ge0\) for every \(j\), and finds a single vertex of maximum degree for which this holds against **every** competitor. As all Bernstein basis functions are nonnegative on \([0,1]\), every verified difference is nonnegative on \([0,1]\), proving the same vertex minimizes (1) for every \(p\in(0,1)\). The complete numbers of labelled trees examined are \(1,3,16,125,1296,16807\), totaling \(18248\); there is no sampling of tree types. The standalone `verify.py` implements the enumeration and exact test.

**3. Eight-vertex witness.** Direct pair-distance counting gives the following polynomials; symmetrical leaves \(1,2\) agree:
\[
\begin{aligned}
F_0&=4p+3p^2+2p^3+p^4,\\
F_3&=5p+3p^2+p^3,\\
F_4&=5p+4p^2,\\
F_5&=5p+4p^2+2p^3,\\
F_6&=5p+5p^2+3p^3+2p^4,\\
F_7&=6p+6p^2+4p^3+3p^4+2p^5,\\
F_1&=F_2=6p+5p^2+4p^3+3p^4+2p^5+p^6.
\end{aligned}
\]
For each \(w\in\{1,2,4,5,6,7\}\), one has \(F_w(p)>F_3(p)\) on \(0<p<1\). For example, \(F_4-F_3=p^2(1-p)>0\), \(F_5-F_3=p^2+p^3>0\), and the remaining four differences have strictly positive monomial or Bernstein representations on the open interval. The verifier checks all six exact comparisons. Hence the only possible minimizers are vertices \(0\) and \(3\). Subtraction yields
\[
F_3-F_0=p(1-p^2-p^3).
\]
The function \(p^2+p^3\) increases strictly from zero to two on \((0,1)\), so it crosses one exactly once, at \(p_*\). Formula (1) multiplies the difference by \(2/7\), proving all of part (b) including uniqueness and ties.

## Verification

Run `python3 verify.py` from the directory containing this document and the included standalone verifier. Python 3 standard library alone is sufficient. A successful run emits the precise Prüfer-sequence counts for \(n=2,\ldots,7\), all eight exact distance profiles, and confirmation of forty independently calculated expectations. The verifier first exhausts all \(18248\) labelled trees and checks every prospective comparison using integer-scaled Bernstein coefficients. For the eight-vertex witness, it additionally enumerates all \(2^7\) open/closed edge configurations for five rational transmissibilities and independently compares those exact fractions to (1) for all eight vaccine choices. This last finite numerical cross-check does **not** substitute for the symbolic polynomial factorization proving the entire continuum of \(p\).

## Relationship to prior work

Britton, Janson and Martin-Löf (2007) give the independent-transmission epidemic and network-vaccination framework for asymptotic degree-distribution random graphs. Preciado and collaborators (2013) optimize vaccination in a heterogeneous SIS/spectral framework; the objective is not the present finite Reed–Frost outbreak mean. Altarelli and collaborators (2013) develop network immunization algorithms, including SIR message-passing approximations and tree recursions; those techniques can evaluate immunization performance but do not themselves state the eight-node crossover or the sharp minimal-tree-order certificate. Holme (2017) is particularly close: it computes exact single- and multi-vaccine SIR node-importance quantities for every connected graph on three through seven vertices, though it does not examine eight-vertex networks or establish the present tree-specific maximum-degree/first-switch statement. Its continuous-time SIR model differs in higher joint moments, while the mean on a *tree* can be compared via single-path transmission probabilities. The present theorem is an explicit small-tree structural classification in a fixed independent-edge model, not a claim of novelty for the general vaccination objective.

## Limitations

Part (a) is a rigorously reproducible finite exhaustive classification, not a proof of an analogous statement for arbitrary larger trees. The finding is mathematical, with no contact-network data or claims of validated public-health policy. Only a single perfectly vaccinated vertex and homogeneous independent edge transmissibility are treated. Since the seven-vertex computations are finite, future independent review of the implementation and historical comparison remains appropriate. Related post-2016 exact graph-importance work is acknowledged even though the motivating epidemic model was first publicly available in 2007.

## References

1. T. Britton, S. Janson, A. Martin-Löf, “Graphs with specified degree distributions, simple epidemics and local vaccination strategies,” first public arXiv version **2007-02-01**, https://arxiv.org/abs/math/0702021.
2. V. M. Preciado et al., “Optimal Vaccine Allocation to Control Epidemic Outbreaks in Arbitrary Networks,” first public arXiv version **2013-03-16**, https://arxiv.org/abs/1303.3984.
3. F. Altarelli et al., “Containing epidemic outbreaks by message-passing techniques,” first public arXiv version **2013-09-11**, https://arxiv.org/abs/1309.2805.
4. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” first public arXiv version **2017-08-22**, https://arxiv.org/abs/1708.06456; *Phys. Rev. E* **96**, 062305 (2017), https://doi.org/10.1103/PhysRevE.96.062305.
5. K. J. Sharkey et al., “Exact Equations for SIR Epidemics on Tree Graphs,” *Bulletin of Mathematical Biology* **77**, 614–645 (2015), https://doi.org/10.1007/s11538-013-9923-5.
