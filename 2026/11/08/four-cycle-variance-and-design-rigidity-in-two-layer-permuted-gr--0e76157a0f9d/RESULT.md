# Four-cycle variance and design rigidity in two-layer permuted graph occupancy

## Finding

Let \(d\ge4\) and \(2\le r\le d-2\). In the two-layer permuted regular-graph path model, the number of unordered pairs of paths sharing their endpoint is a random quadratic occupancy statistic. Its expectation does not depend on the graph, but its **variance depends exactly on the dispersion of distinct-row common-out-neighbor counts**.

Let \(A\in\{0,1}^{d\times d}\) have every row and column sum equal to \(r\). With independent uniformly distributed permutation matrices \(\Pi_1,\Pi_2\), choose any fixed starting vertex \(i\) and write
\[
P=A/r,\qquad N_2(j)=r^2(e_i^\mathsf{T}\Pi_1P\Pi_2P)_j,\qquad C_2=\sum_{j=1}^d \binom{N_2(j)}2.
\]
Let \(c_{uv}=\sum_{j=1}^d A_{uj}A_{vj}\) for \(u<v\) and \(\mu=r(r-1)/(d-1)\). Then
\[
\boxed{\mathbb EC_2=\binom r2\mu,\qquad
\operatorname{Var}(C_2)=
\frac{r(r-1)(d-r)(d-r-1)}{d(d-1)(d-2)(d-3)}
\sum_{u<v}(c_{uv}-\mu)^2.}
\]
The coefficient is strictly positive throughout the stated range. Hence \(C_2\) is deterministic exactly when all distinct rows have identical codegree \(\mu\); such matrices are precisely the incidence matrices of symmetric \(2\)-\((d,r,\mu)\) designs. In particular, if \(\mu\notin\mathbb Z\), the variance is positive for every admissible matrix.

Writing \(C_4\) for the number of unordered \(K_{2,2}\) subgraphs (four-cycles) in the bipartite incidence graph of \(A\), one also has
\[
\sum_{u<v}(c_{uv}-\mu)^2
=2C_4+d\binom r2-\binom d2\mu^2.
\]
Thus exactly one classical motif count determines the graph-dependent collision variance at two layers.

## Assumptions and scope

All vertices are labeled; loops in the directed regular graph are allowed, though the explicit examples have no loops. Its adjacency matrix is binary, with no multiple directed edges. Each row has exactly \(r\) ones, and each column has exactly \(r\) ones. The two uniform permutations are independent and also independent of the fixed starting vertex. Each of the \(r^2\) possible two-step paths contributes one unit to its endpoint occupancy; two paths are paired without order. The theorem is finite and exact, for every integer \(d,r\) in the specified range and every choice of start. The displayed variance is with respect to both permutations.

## Proof

**1. Reduction to uniform sampling without replacement.** After the first permutation and the first transition, exactly \(r\) intermediate vertices each carry one path. Independently permuting them before the second transition gives a uniformly random size-\(r\) subset \(S\subseteq[d]\). The second-step multiplicity in column \(j\) is therefore \(N_2(j)=\sum_{u\in S}A_{uj}\). Double counting pairs of paths yields
\[
C_2=\sum_j\binom{\sum_{u\in S}A_{uj}}2
=\sum_{\{u,v\}\subseteq S}c_{uv}.
\]
This exact representation removes the dependence on the starting vertex.

**2. Zero row sums of centered codegrees.** As each of the \(r\) ones in row \(u\) belongs to a column of sum \(r\),
\[
\sum_{v\ne u}c_{uv}=r(r-1),\qquad
\sum_{u<v}c_{uv}=d\binom r2.
\]
Let \(h_{uv}=c_{uv}-\mu\), so that \(\sum_{v\ne u}h_{uv}=0\) and \(\sum_{u<v}h_{uv}=0\). Each unordered pair is contained in \(S\) with probability \(\alpha=(r)_2/(d)_2\). Consequently
\[
\mathbb EC_2=\alpha\,d\binom r2=\binom r2\mu.
\]
For variance, set \(Y=C_2-\mathbb EC_2=\sum_{\{u,v\}\subseteq S}h_{uv}\) and \(H=\sum_{u<v}h_{uv}^2\). In the expansion of \(\mathbb EY^2\), ordered identical-edge pairs contribute \(H\), ordered *distinct* edge pairs meeting at a vertex contribute \(-2H\), and ordered disjoint edge pairs contribute \(+H\). Indeed, for each \(u\), expanding \((\sum_{v\ne u}h_{uv})^2=0\) shows that the sum over ordered distinct adjacent edges is \(-2H\); the square of the global zero sum shows all ordered distinct edges total \(-H\), leaving \(+H\) for disjoint ones.

**3. Inclusion probabilities and factorization.** Let \(\beta=(r)_3/(d)_3\), \(\gamma=(r)_4/(d)_4\), using \((r)_4=0\) when \(r<4\). Identical, adjacent and disjoint pairs of edges are included in the sampled clique with probabilities \(\alpha\), \(\beta\), \(\gamma\), respectively. Therefore
\[
\operatorname{Var}(C_2)=\mathbb EY^2=(\alpha-2\beta+\gamma)H.
\]
Direct simplification of the falling-factorial ratio gives
\[
\alpha-2\beta+\gamma
=\frac{r(r-1)(d-r)(d-r-1)}{d(d-1)(d-2)(d-3)}>0.
\]
This proves the variance identity and its zero-variance equality characterization. Constant common row intersections together with constant row and column sums are the incidence axioms of a symmetric \(2\)-design (with rows interpreted as blocks). No assertion is made that such a design exists at every admissible parameter pair.

**4. Four-cycles.** Since \(C_4=\sum_{u<v}\binom{c_{uv}}2\),
\[
\sum_{u<v}(c_{uv}-\mu)^2
=\sum_{u<v}c_{uv}^2-\binom d2\mu^2
=2C_4+d\binom r2-\binom d2\mu^2.
\]

**5. Equal-parameter contrast.** On \(\mathbb Z/7\mathbb Z\), let \(A_{uv}=1\) when \(v-u\) belongs to a specified three-element subset. With offsets \(\{1,2,4\}\), every pair of rows shares exactly one out-neighbor, so \(H=0\). With offsets \(\{1,2,3\}\), the 21 distinct row pairs have seven codegrees of each value \(0,1,2\), so \(H=14\). Since \(\mu=1\) and the variance prefactor equals \(3/35\), the corresponding means are both \(3\), and the variances are \(0\) and \(14(3/35)=6/5\).

## Verification

The accompanying standalone `verify_collision.py` uses only the Python 3 standard library. It enumerates all uniform \(r\)-subsets and computes exact rational first and second moments, independently evaluating the codegree formula. Exhaustive binary circulant examples on orders \(4\) through \(9\), together with randomized degree-preserving exchanges, supplied 1,548 exact matrix/subset comparisons, and the two seven-vertex contrast examples were checked. Run `python3 verify_collision.py` in the extracted package directory. The finite checker tests only its specified examples; the proof above establishes all admissible orders and matrices.

## Relationship to prior work

Chiclana's *Poisson occupancy of paths on permuted regular graphs* (arXiv:2610.14724, initial posting 2026-10-10) introduced this independent-permutation path-occupancy model. Its Section 3.2 proves a Poincaré-based variance **bound** for the empirical generating function, while its covariance and Frobenius-norm identities address lower-order observables. Those results do not state the exact fourth-order variance of the two-step collision statistic, nor the symmetric-design zero-variance characterization. The present calculation specializes the general finite-population quadratic \(U\)-statistic variance mechanism to regular-graph codegrees. Classical symmetric-design theory supplies the language and background for the equality class; the existence or classification of such designs is not claimed here.

## Limitations

The result covers exactly two layers, binary regular matrices with a common degree in both layers, and \(2\le r\le d-2\). It does not identify the collision variance at larger depths, derive any asymptotic Poisson law, assert universal graph-independent fluctuations, or establish historical priority against every possible reformulation of finite-population \(U\)-statistics. Symmetric-design existence in arbitrary parameters is not implied. Historical overlap through generic degenerate \(U\)-statistic formulas remains a residual risk even though the model-specific design-rigidity theorem was not found in inspected sources.

## References

1. Rafael Chiclana, *Poisson occupancy of paths on permuted regular graphs*, arXiv:2610.14724 (initial public version 2026-10-10), https://arxiv.org/abs/2610.14724 ; Section 3.2 and covariance results.
2. Eric S. Lander, *Symmetric Designs: An Algebraic Approach*, Cambridge University Press (1983), Chapter 1, https://doi.org/10.1017/CBO9780511662164.002 .
3. W. Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, Annals of Mathematical Statistics 19 (1948), 293–325; general \(U\)-statistic background, https://doi.org/10.1214/aoms/1177730196 .
