# Triangle motifs are the exact third-moment discriminator in two-partner coextinction networks

## Finding

Let \(H\) be any finite, simple, undirected \(2\)-regular graph on \(n\ge3\) vertices, hence a disjoint union of cycles of length at least three. Construct a bipartite mutualistic incidence network with one primary species for each vertex of \(H\) and one secondary species for each edge of \(H\). A secondary species has exactly the two endpoints of its edge as obligate alternative partners: it disappears exactly when both have been removed. Uniformly remove exactly \(t\) of the \(n\) primary species without replacement, for any \(0\le t\le n\), and denote the number of coextinct secondary species by \(K_t\). Define

\[
q_s(n,t)=\frac{\binom{n-s}{t-s}}{\binom nt},
\]

interpreted as zero when \(t<s\) or \(s>n\). Let \(T(H)\) be the number of triangular components of \(H\), and let \((z)_j=z(z-1)\cdots(z-j+1)\) denote a falling factorial. Then, exactly,

\[
\begin{aligned}
\mathbb E K_t &= n q_2,\\
\mathbb E (K_t)_2 &= 2\left[nq_3+\left(\binom n2-n\right)q_4\right],\\
\mathbb E (K_t)_3 &= 6\Bigg[nq_4+n(n-4)q_5+\left(\binom n3-n(n-3)\right)q_6\\
&\hspace{35mm}+T(H)(q_3-3q_4+3q_5-q_6)\Bigg].
\end{aligned}
\]

All \(q_s\) on the right are evaluated at \((n,t)\). Hence every such network of the same order has the same exact mean and variance at *every* removal horizon. For \(n\ge6\), two such networks satisfy the exact third-factorial-moment contrast

\[
\mathbb E_H (K_t)_3-\mathbb E_{H'}(K_t)_3
=6\bigl(T(H)-T(H')\bigr)
\frac{\binom{n-6}{t-3}}{\binom nt},
\qquad 3\le t\le n-3.
\]

The contrast vanishes for horizons outside this range, and within it the third factorial moment determines \(T(H)\) uniquely. The minimum order where two incidence networks with these degree constraints can have identical means and variances for all horizons yet different coextinction laws is **\(n=6\)**: for \(t=3\), \(H=C_6\) and \(H'=C_3\sqcup C_3\) yield

\[
\begin{array}{c|rrrr}
&K_3=0&K_3=1&K_3=2&K_3=3\\\hline
C_6&2/20&12/20&6/20&0\\
C_3\sqcup C_3&0&18/20&0&2/20
\end{array}
\]

while both have \(\mathbb E K_3=6/5\), \(\operatorname{Var}(K_3)=9/25\). In particular \(\Pr(K_3=3)\) is zero for the six-cycle and \(1/10\) for two triangles.

## Assumptions and scope

The incidence network is static, simple, and unweighted; each primary has precisely two secondary partners and each secondary has exactly two *distinct*, obligate alternative primary partners, with no duplicate primary-partner pairs. Primary removals are a uniformly random fixed-size subset, not independently weighted risks. There is no rewiring, rescue, direct secondary extinction, or further cascade. The model is a deliberately restricted structural limit of the topological coextinction convention, not a demographic prediction. Disconnected incidence networks are allowed. The two guilds each contain \(n\) species.

## Proof

Write \(R\subseteq V(H)\) for the random uniform \(t\)-set. The coextinction count is exactly the number of induced edges,
\[
K_t=\sum_{e\in E(H)}\mathbf 1\{e\subseteq R\}=|E(H[R])|.
\]
Every fixed set of \(s\) primary vertices is contained in \(R\) with probability \(q_s(n,t)\). Since \(H\) is \(2\)-regular, it has \(n\) edges and exactly \(n\) unordered pairs of edges sharing a vertex. The other \(\binom n2-n\) edge pairs are vertex-disjoint. Expanding the first two falling factorial moments proves the first two formulas.

For the third moment, enumerate unordered triples of distinct edges by the number of vertices in their union. A triple covering three vertices is a triangle, of which there are \(T=T(H)\). A triple covering four vertices is a three-edge path, and there are \(n-3T\): every edge determines a consecutive three-edge path unless it lies in a triangular component, in which case its three-edge block is the entire triangle. There are \(n\) adjacent edge pairs in total. Of these, \(3T\) belong to triangles; each such pair has \(n-3\) third edges disjoint from its two-edge union. For each of the other \(n-3T\) adjacent pairs, exactly \(n-4\) edges are disjoint from its two-edge union. Thus triples covering five vertices number \(3T(n-3)+(n-3T)(n-4)=n(n-4)+3T\). Finally, triples covering six vertices number \(\binom n3-n(n-3)-T\) by subtraction. A triple with \(s\) union vertices survives precisely with probability \(q_s\). Multiplying these four counts by \(6\) for orderings and collecting the coefficient of \(T\) proves the displayed third moment formula.

For \(n\ge6\), inclusion–exclusion on three specified present and three specified absent vertices gives
\[
q_3-3q_4+3q_5-q_6
=\Pr(\text{specified 3 included, specified disjoint 3 excluded})
=\frac{\binom{n-6}{t-3}}{\binom nt}.
\]
This is strictly positive exactly when \(3\le t\le n-3\). Consequently the third-moment contrast identifies the triangle-component count, while the first two moments remain unchanged.

Every simple \(2\)-regular graph is a union of cycles of length at least three. For \(n=3,4,5\) the only isomorphism class is \(C_n\). At \(n=6\), both \(C_6\) and \(C_3\sqcup C_3\) are possible. Directly enumerating the \(\binom63=20\) triples of removed vertices gives the displayed exact distributions. This proves sharpness without relying on a finite search as the proof of minimality.

## Verification

The standalone `verify.py` enumerates every uniform removal subset for every nondecreasing cycle-length partition of orders \(3\) through \(11\), for every \(0\le t\le n\). It compares exact rational first, second, and third factorial moments with the formulas above. It independently verifies the binomial identity and both exact six-vertex distributions. All \(239\) tested cycle-partition/removal-horizon combinations passed. The infinite-order theorem follows from the combinatorial proof, not from this finite check.

## Relationship to prior work

The 2004 Memmott–Waser–Price topological coextinction convention removes one guild and declares a dependent species lost after all its partners disappear; their empirical network simulations compare random and degree-directed removal. Burgos et al. (arXiv 2006, journal 2007) study nestedness and attack-tolerance curves, particularly for preferential removal; neither states the exact fixed-size third-moment identification in \(2\)-regular incidence networks. Janson and Ruciński (2009) study upper-tail estimates for induced hypergraph counts under independent vertex sampling, a broad probabilistic framework but not this exact fixed-size classification. Bhattacharya, Das and Mukherjee (2020) study motif estimation under independent vertex sampling and asymptotic normality, not this finite hypergeometric coefficient. Vieira and Almeida-Neto (2014 online) incorporate ecological dependence weights and stochastic cascading, a distinct model; full-text comparison remains a priority risk. The mean/variance distinction and degree-conditioned second moments for pairwise coextinction have also appeared in related mathematical treatments; this claim isolates the exact higher-order triangle discriminant and the minimal \(6+6\)-species configuration, not the general induced-edge-count representation.

## Limitations

The derivation is a finite-network, fixed-size sampling identity; it neither predicts actual plant losses nor accounts for positive abundance, unequal functional dependence, extinction correlation beyond the exchangeable fixed-size choice, or adaptive rewiring. A triangle in \(H\) corresponds to three secondary specialists whose partner pairs lie among three primary species; it is not a literal ecological three-species food-web triangle. The formula does not assert that the third moment identifies the complete cycle decomposition: longer cycles become relevant for higher moments. General random induced-subgraph moment expansions are classical and may imply portions of the formula; priority of this specific complete moment identification and sharp cutoff requires independent historical checking.

## References

1. Memmott, J., Waser, N. M. and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proc. R. Soc. B 271, 2605–2611. First online 2004-12-06. https://doi.org/10.1098/rspb.2004.2909
2. Burgos, E., Ceva, H., Perazzo, R. P. J., et al. (2006 preprint; 2007 journal). *Why nestedness in mutualistic networks?* https://arxiv.org/abs/q-bio/0609005
3. Janson, S. and Ruciński, A. (2009). *Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs*. https://arxiv.org/abs/0905.0972
4. Kaiser-Bunbury, C. N., Muff, S., Memmott, J., et al. (2010). *The robustness of pollination networks to the loss of species and interactions*. https://doi.org/10.1111/j.1461-0248.2009.01437.x
5. Vieira, M. C. and Almeida-Neto, M. (2014 online). *A simple stochastic model for complex coextinctions in mutualistic networks*. https://doi.org/10.1111/ele.12394
6. Bhattacharya, B. B., Das, S. and Mukherjee, S. (2020 preprint). *Motif Estimation via Subgraph Sampling: The Fourth Moment Phenomenon*. https://arxiv.org/abs/2011.03026
