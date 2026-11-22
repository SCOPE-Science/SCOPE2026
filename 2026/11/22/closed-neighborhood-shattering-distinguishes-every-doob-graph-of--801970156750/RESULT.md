# Closed-neighborhood shattering distinguishes every Doob graph of fixed diameter

## Finding
Let \(S\) be the Shrikhande graph, let \(K_4\) be the complete graph on four vertices, and let \(D(m,n)=S^{\square m}\square K_4^{\square n}\), where \(m,n\) are nonnegative integers and \(d=2m+n\ge3\). For every vertex \(v\), let \(N[v]\) denote its closed graph neighborhood. The class is \(\mathcal C_{m,n}=\{N[v]:v\in V(D(m,n))\}\). Write \(\Phi_{m,n}(z)=\sum_{k\ge0}s_k(m,n)z^k\), where \(s_k\) counts unordered \(k\)-vertex sets shattered by this class. Then
\[
\boxed{\Phi_{m,n}(z)=1+4^d z+\frac{4^d}{2}\left(3d+9\binom d2\right)z^2+4^d\left(27\binom{d+1}{3}-8m\right)z^3.}
\]
There are no shattered supports of size four or more, and \(\operatorname{VCdim}(\mathcal C_{m,n})=3\). Thus among the \(\lfloor d/2\rfloor+1\) Doob graphs of a fixed diameter \(d\ge3\), all having the Hamming graph's intersection array, the cubic shattering coefficients are pairwise distinct. Each Shrikhande factor reduces the cubic coefficient by exactly \(8\cdot4^d\) relative to \(H(d,4)=D(0,d)\).

## Assumptions and scope
Use the Cayley realization of \(S\) on \((\mathbb Z/4\mathbb Z)^2\) with six nonzero generators \((1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\). Each \(K_4\) factor is represented by \(\mathbb Z/4\mathbb Z\), with all three nonzero differences as generators. Graph products are Cartesian; the vertex count is \(4^{2m+n}\), and a closed radius-one ball has \(1+6m+3n=1+3d\) vertices. Every vertex is eligible as a center. A query support \(A\) is shattered precisely if \(\{N[v]\cap A:v\in V\}=2^A\). The claimed formula concerns these **closed** radius-one balls, not open neighborhoods or arbitrary graph balls.

## Proof
**1. Counting two-point supports.** The Doob graphs have the same intersection array as \(H(d,4)\), hence exactly \(3d\) vertices at distance one and \(9\binom d2\) at distance two from each vertex. Any pair of vertices at distance greater than two has no common closed-neighborhood center and cannot be shattered. For any pair at distance at most two, a closed ball containing both exists. The two singleton traces exist because distinct neighborhoods have degree \(3d\), while their intersection has fewer than \(1+3d\) vertices; the empty trace exists because \(4^d\) exceeds the union of two radius-one balls for \(d\ge3\). Consequently all and only pairs at distance one or two are shattered. Counting ordered pairs and dividing by two gives \(s_2=4^d(3d+9\binom d2)/2\). Every singleton is shattered, so \(s_1=4^d\).

**2. Factor geometry for triples.** Fix a center \(o\). Its closed ball consists of \(o\), the six neighbors in each Shrikhande factor and the three neighbors in each complete factor. Let \(g_i\in\{6,3\}\) be the arm size of factor \(i\); thus there are \(m\) arms of size six and \(n\) arms of size three. Every shattered triple \(A\) must lie inside some closed ball, because its full positive trace is required. We count such triples by centers, assigning weight \(1/c(A)\) to \(A\subseteq N[o]\), where \(c(A)=|\{v:A\subseteq N[v]\}|\) is the number of common centers. Vertex transitivity means the total number of shattered triples equals \(4^d\) times the weighted count in the ball of \(o\).

The complete list of **shattered** centered triple shapes is:

| Shape within \(N[o]\) | Number before center weights | Weighted contribution |
|---|---:|---:|
| Three noncentral points in three different factors | \(\sum_{i<j<k}g_ig_jg_k\) | Same |
| Two noncentral points in one factor and one in another | \(\sum_i\binom{g_i}{2}\sum_{j\ne i}g_j\) | Same |
| \(o\) and two noncentral points in different factors | \(\sum_{i<j}g_ig_j\) | Same |
| Three noncentral points in a single Shrikhande factor | \(14m\) | \(14m\) |
| \(o\) and two noncentral points in one Shrikhande factor | \(9m\) | \(5m\) |

No triple supported solely in a complete-graph factor is shattered. In each of the first three rows, the common closed-ball center is unique. The fourth row has 14 shattered triples per Shrikhande factor, each with a unique center. In the fifth row there are nine shattered configurations per factor, three with one common center and six with three common centers, hence weight \(3+6/3=5\). These finite, **exact** local statements hold whenever \(d\ge3\); their complete adjacency-and-trace verification is furnished by `verify_doob.py` (specifically the four three-factor templates and the Shrikhande local table). The classification is exhaustive because a triple in \(N[o]\) meets one, two, or three factors, possibly including \(o\), and there are no other factor-position patterns. The finite patterns exhaust every factor type, irrespective of the number of unused factors.

It follows that the weighted triple count per center is
\[
T=\sum_{i<j<k}g_ig_jg_k+\sum_i\binom{g_i}{2}\sum_{j\ne i}g_j+\sum_{i<j}g_ig_j+19m.
\]
Substituting \(g_i=6\) for the \(m\) Shrikhande factors and \(g_i=3\) for the \(n\) complete factors, then collecting elementary symmetric polynomials, gives the identity
\[
T=27\binom{2m+n+1}{3}-8m.
\]
The independent exact checker verifies both expressions on all tested families. As above \(s_3=4^dT\).

**3. No four-point support.** Suppose four points \(A\) are shattered. Some closed ball contains all four; by translation put its center at \(o\). If its noncentral points occupy at least three distinct Cartesian factors, choose a triple using one point from each of those factors. The only radius-one ball containing those three points is \(N[o]\), which also contains the remaining point. Thus the triple-positive/fourth-negative trace is impossible. A shattered four-set must therefore use at most two noncentral factors (possibly together with \(o\)).

There are only three types of such factor pairs: two complete factors, one Shrikhande and one complete factor, and two Shrikhande factors. Their entire trace feasibility is preserved by embedding the chosen factors in, respectively, \(D(0,4)\), \(D(1,3)\), and \(D(2,2)\), adjoining two spare complete factors. Indeed, a center whose nonzero factor coordinates lie outside the selected factors can contribute at most a singleton trace or the empty trace; two spare coordinates realize all such external possibilities. Every center with nonzero components within the selected factors is already represented inside the corresponding template. The `verify_doob.py` certificate enumerates **every** four-subset of the zero-centered closed ball in each of these three templates and checks all possible centers and all 16 requested traces, finding no shattered four-set. This finite obstruction, combined with the reduction, proves the global four-point impossibility, not merely a checked range. Larger shattered sets would contain shattered four-subsets, so all higher coefficients vanish.

**4. Positivity and separation.** For \(d\ge3\), the computed \(T\) is positive, hence VC dimension is three. The cubic coefficient is strictly decreasing in \(m\) at fixed \(d\), with exact step \(8\cdot4^d\). All Doob graphs of fixed \(d\) share their intersection array, so this provides a complete distinction within that parameter family by a neighborhood-shattering invariant.

## Verification
`verify_doob.py` (Python 3, standard library) independently builds all factor generators and closed-neighborhood traces. It checks the centered singleton/pair/triple/four-pattern tables in seven finite templates, checks the local Shrikhande multiplicities and independent weighted counts in thirteen product cases, and checks the equality of the two formulas for \(T\). It prints `DOOB_NEIGHBORHOOD_SHATTER_PASS templates=7 family_samples=13`. As a separate implementation, `doob_census.cpp` (C++17) enumerates all shattered supports of orders zero through four **without using the proof's factor reduction** for the two 64-vertex graphs \(H(3,4)\) and \(D(1,1)\). It returns, respectively, \((1,64,1152,6912,0)\) and \((1,64,1152,6400,0)\). These exhaustive finite certificates prove the explicitly reduced local obligations; they are not treated as extrapolations to all orders.

## Relationship to prior work
Krotov's 2018 study supplies the Doob-graph construction, intersection-array background and coding-theoretic motivation, but not neighborhood shattering. Adler, Benediktsson and Macpherson (2020 preprint) investigate VC dimension of **open** Hamming adjacency neighborhoods, rather than these closed Doob families. The known exact closed-neighborhood Hamming polynomial gives the \(m=0\) specialization. A separate exact finite comparison of the Shrikhande graph and rook graph gives the 16-vertex, diameter-two case, which does not imply any product formula or the fixed-diameter all-family separation here. General graph-VC computation algorithms also do not determine these coefficients. The new comparison is precisely the uniform defect \(8m4^d\) for \(d\ge3\), with the structural proof above.

## Limitations
The theorem excludes diameter below three; it does not provide arbitrary-radius, open-neighborhood, or restricted-center formulas. It proves a coefficientwise distinction within the Doob family, not a universal relation between graph spectra and shattering polynomials. Historical unindexed equivalents are possible and independent mathematical validation has not been performed. The finite template enumerations are indispensable to the given proof of the nontrivial local trace statements.

## References
1. D. S. Krotov, *The existence of perfect codes in Doob graphs*, arXiv:1810.03772 (first public 2018-10-09), https://arxiv.org/abs/1810.03772.
2. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042 (first public 2020-07-31), https://arxiv.org/abs/2007.16042.
3. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, LIPIcs SEA 2024, article 8, https://doi.org/10.4230/LIPIcs.SEA.2024.8.
4. *Closed-neighborhood shattering polynomials of all Hamming graphs*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-closed-neighborhood-shattering-polynomials-of-all-hamming-graphs--6c82fc864f93.
5. *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-closed-neighborhood-shattering-polynomial-separation-of-the-sh--670b6697d463.
