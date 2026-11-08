# The degree-two exception for loop–parallel-pair covariance in configuration models

## Finding
For every finite nonnegative integer degree sequence \(\boldsymbol d=(d_1,\ldots,d_v)\) with even total degree \(N=\sum_i d_i\ge6\), form the configuration-model multigraph by pairing all \(N\) distinguishable half-edges uniformly. Let \(L\) count self-loops and let \(P=\sum_{i<j}\binom{X_{ij}}{2}\) count unordered pairs of parallel non-loop edges, where \(X_{ij}\) is edge multiplicity between distinct vertices. Set
\[
 a_i=\binom{d_i}{2},\quad S=\sum_i a_i,\quad T=\sum_{i<j}a_i a_j,\quad
 W=\sum_{i<j}a_i a_j(2d_i+2d_j-6).
\]
Then the **exact finite-model covariance** is
\[
 \operatorname{Cov}(L,P)=\frac{2[4ST-(N-1)W]}{(N-1)^2(N-3)(N-5)}.
\]
It vanishes if and only if \(T=0\) (in which case \(P=0\) identically). If \(T>0\), it is **positive if and only if** at least three vertices have degree two and all other vertices have degree zero; it is **strictly negative for every other degree sequence**. In particular, no cancellation at zero is possible for \(T>0\).

For a constant degree \(d\ge2\) on \(v\) vertices, whenever \(vd\ge6\) is even,
\[
 \operatorname{Cov}(L,P)=
 \frac{v(v-1)\binom{d}{2}^{\!2}\,[2vd(2-d)+4d-6]}{(vd-1)^2(vd-3)(vd-5)}.
\]
For \(d=2\) and \(v\ge3\), this is positive and asymptotic to \(1/(8v^2)\); for every fixed \(d\ge3\) it is negative and asymptotic to \(-(d-1)^2(d-2)/(2dv)\). This gives distinct finite-size dependence orders despite asymptotic independence of defect counts in familiar bounded-degree regimes.

## Assumptions and scope
Half-edges are individually labelled and a matching is selected uniformly among \((N-1)!!\) complete pairings. Loops contribute one to \(L\), even when several are at one vertex. A multiplicity \(X_{ij}\) contributes \(\binom{X_{ij}}{2}\) to \(P\), rather than just an indicator of \(X_{ij}\ge2\); triple edges therefore contribute three pairs. Degrees zero and one are permitted; all statements concern \(N\ge6\). No simplicity conditioning is imposed.

## Proof
**1. Exact joint moments.** A selected loop made of two prescribed stubs has probability \(1/(N-1)\). A selected pair of non-loop parallel edges, built with two stubs from each of two vertices and one of the two bijections, has probability \(1/[(N-1)(N-3)]\). Consequently,
\[
 \mathbb{E}L=\frac S{N-1},\qquad \mathbb{E}P=\frac{2T}{(N-1)(N-3)}.
\]
Given a selected parallel-edge pair at vertices \(i,j\), exactly \(N-4\) unpaired stubs remain. The available unordered within-vertex stub pairs number
\[
 S-a_i-a_j+\binom{d_i-2}2+\binom{d_j-2}2
 =S-(2d_i+2d_j-6),
\]
with terms for \(d_i,d_j\ge2\), the only pairs contributing. Each such compatible loop completes with conditional probability \(1/(N-5)\). Counting the \(2a_i a_j\) possible parallel-edge pairs gives
\[
 \mathbb{E}(LP)=\frac{2(ST-W)}{(N-1)(N-3)(N-5)}.
\]
Subtracting the product of expectations proves the covariance formula.

**2. Sign reduction.** Vertices of degree zero can be ignored. Temporarily suppose every remaining vertex has degree at least two and let \(e_i=d_i-2\ge0\). Define
\[
 E=\sum_i d_i e_i,\qquad R=\sum_{i<j}a_i a_j(e_i+e_j),\qquad G=(N-1)R-(E+1)T.
\]
Since \(2S=N+E\) and \(W=2(T+R)\), the covariance equals
\[
 \operatorname{Cov}(L,P)=-\frac{4G}{(N-1)^2(N-3)(N-5)}.
\]
Expanding \(NR-ET\) over a third vertex partitions \(G\) into pair and triple terms:
\[
 G=\sum_{i<j}a_i a_j(e_i+e_j+2e_ie_j-1)
 +\sum_{i<j<k}\frac{d_id_jd_k}{4}\,F(e_i,e_j,e_k),
\]
where
\[
 F(x,y,z)=(1+x)(1+y)(x+y-z)+(1+x)(1+z)(x+z-y)
 +(1+y)(1+z)(y+z-x).
\]
The polynomial identity
\[
 F=x+y+z+2(x^2+y^2+z^2)
 +\!\sum_{\rm sym}x^2y-3xyz\ge0
\]
holds for all \(x,y,z\ge0\): the six symmetric cubic monomials sum to at least \(6xyz\) by AM–GM. Furthermore \(F(0,0,z)=z+2z^2\ge3\) when \(z\ge1\).

If all remaining degrees equal two, \(G=-T<0\). Otherwise there is at least one vertex with \(e_k\ge1\). Pair terms are negative only when both endpoints have degree two, and then each such pair contributes exactly \(-1\). For each such pair and a fixed high-degree vertex \(k\), the distinct-vertex triple contributes at least \(d_kF(0,0,e_k)\ge9\), more than offsetting its \(-1\). All remaining pair and triple contributions are nonnegative. If no two degree-two vertices exist, the presence of at least two high-degree vertices makes a positive pair term; the only two-active-vertex edge case \((d_1,d_2)=(3,2)\) gives \(G=0\), but has odd total degree and so is not a matching model. For every admissible even \(N\) with \(T>0\), the result is \(G>0\) unless all active degrees equal two.

**3. Degree-one vertices.** Adding degree-one vertices leaves \(S,T,W\) unchanged but increases \(N\). Consequently, for \(T>0\), the sign-controlling expression \(4S/(N-1)-W/T\) strictly decreases. A high-degree vertex therefore continues to yield negative covariance after any degree-one vertices are added; in the borderline inactive-pair degree list \((3,2)\), one or more degree-one vertices makes the expression strictly negative. When there are \(r\ge2\) degree-two vertices and \(k\) degree-one vertices and no higher degrees, the same expression is \(4r/(2r+k-1)-2\), positive only for \(k=0\), zero for \(k=1\) (which forces odd total degree), and negative for \(k\ge2\). For \(r=2,k=0\), the total degree is four and is excluded. This proves the stated sign classification. If \(T=0\), at most one vertex has at least two half-edges, so no parallel non-loop pair can occur and \(P=0\).

**4. Regular specialization.** Set every degree equal to \(d\) in the exact formula. The numerator bracket is \(2vd(2-d)+4d-6\), which is exactly \(2\) when \(d=2\) and is strictly negative for \(d\ge3\) and \(v\ge2\). Expansion in \(1/v\) gives the two stated orders.

## Verification
Run `python3 checker.py` using only Python's standard library. The checker enumerates all labelled pairings for degree lists with even total at most ten, compares the exact moment formula to a direct rational covariance, tests the complete sign classification over degree vectors, checks the regular specialization, and independently verifies the triple polynomial identity on a finite grid. The proof above—not any finite enumeration—establishes the assertion for arbitrarily many vertices and unbounded degrees. A checked execution produced `PASS: 70950 exact assertions`.

## Relationship to prior work
Janson's configuration-model studies (2006; 2013) and Angel, van der Hofstad and Holmgren (first public 2016) provide the established matching model, defect expectations, and asymptotic simplicity/Poisson results. Angel et al. §3, especially cases (b1)–(b2), analyze precisely the compatible and incompatible loop–parallel-pair indicator configurations needed for Poisson approximation. Those computations overlap substantially with the **moment-counting step** above. The specific all-degree-sequence sign theorem, its unique degree-two positive family, and the different regular finite-size covariance orders were not found stated or proved in the inspected corresponding results. Unlike their asymptotic joint independence, this is an exact sign classification without moment/degree-growth assumptions. The possibility of implicit derivation from earlier joint moment machinery, or overlooked older regular-graph results, remains a priority limitation.

## Limitations
The theorem concerns the pairing-model multigraph, not a uniform simple graph, and \(P\) counts pairs of edges (not just vertex pairs with multiplicity at least two). The model excludes odd total degree and requires at least six half-edges. Historical priority has not been independently established; case-by-case covariance calculations in earlier literature may implicitly contain the formula, though the global sign argument is separate. None of the finite computations alone is an infinite proof.

## References
- Svante Janson, *The probability that a random multigraph is simple*, arXiv:math/0609802 (first submitted 2006-09-28), https://arxiv.org/abs/math/0609802.
- Svante Janson, *The probability that a random multigraph is simple. II*, arXiv:1307.6344 (first submitted 2013-07-24), https://arxiv.org/abs/1307.6344.
- Omer Angel, Remco van der Hofstad and Cecilia Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172 (first submitted 2016-03-23), https://arxiv.org/abs/1603.07172.
- N. C. Wormald, *Models of Random Regular Graphs*, Surveys in Combinatorics 1999, pp. 239–298, DOI:10.1017/CBO9780511721335.010 (survey metadata inspected; full text not available in this comparison).
