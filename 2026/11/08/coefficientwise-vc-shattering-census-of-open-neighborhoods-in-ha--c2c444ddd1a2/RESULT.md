# Coefficientwise VC-shattering census of open neighborhoods in Hamming graphs

## Finding

Let \(d\ge1\) and \(q\ge2\) be integers. On the Hamming graph \(H(d,q)\), with vertex set \([q]^d\), let \(N(c)=\{x:d_H(x,c)=1\}\) be its **open** neighborhood. For \(0\le k\le q^d\), let \(s_k(d,q)\) count unordered \(k\)-vertex supports \(S\) for which every subset of \(S\) is a trace \(S\cap N(c)\) of some center \(c\). Define the complete shattering polynomial \(\Phi_{d,q}(z)=\sum_k s_k(d,q)z^k\). Then

\[
\Phi_{d,q}(z)=1+q^d z+s_2(d,q)z^2+s_3(d,q)z^3,
\]

with no higher-degree terms. Its quadratic coefficient is

\[
s_2(d,q)=\begin{cases}
0,&d=1\text{ or }(d,q)=(2,2),\\
2^{d-1}\binom d2,&q=2,\ d\ge3,\\
\displaystyle\frac{q^d}{2}\left[d(q-1)+\binom d2(q-1)^2\right],&q\ge3,\ d\ge2.
\end{cases}
\]

Put

\[
A_{d,q}=\mathbf1_{\{d\ge2,\ q\ge4\}}\,d q^{d-1}\binom q3,
\]
\[
B_{d,q}=\mathbf1_{\{d\ge2,\ q\ge4\}}\,q^d d(d-1)\binom{q-1}{2}(q-1),
\]
\[
C_{d,q}=\mathbf1_{\{d\ge3,\ q\ge3\text{ or }d\ge4\}}\,q^d\binom d3(q-1)^3.
\]

Then \(s_3(d,q)=A_{d,q}+B_{d,q}+C_{d,q}\). Every shattered triple belongs to exactly one of three types: (A) three vertices on a single coordinate line, (B) two noncentral neighbors of a center differing along one coordinate and a third neighbor along another coordinate, or (C) three neighbors of a center differing along three distinct coordinates. The stated indicator conditions are both necessary and sufficient for each type.

For example,

\[
\Phi_{2,4}(z)=1+16z+120z^2+320z^3,
\quad
\Phi_{3,3}(z)=1+27z+243z^2+216z^3,
\]
\[
\Phi_{4,2}(z)=1+16z+48z^2+64z^3.
\]

The already established VC-dimension thresholds are recovered: the dimension is one for \(d=1\) and for \((d,q)=(2,2)\), two for \((d,q)=(2,3)\) and \((d,q)=(3,2)\), and three in every remaining case. The coefficientwise formulas and three-type counts, not those dimension thresholds, are the finding.

## Assumptions and scope

All graph vertices are distinct labeled words; supports are *unordered sets of vertices*, not multisets or ordered samples. The hypotheses are exactly the open neighborhoods, with **no** extra empty, full, or closed-neighborhood concepts. Every center in \([q]^d\) is available. The alphabet is an arbitrary \(q\)-element set; only equality of symbols matters. The theorem holds for all stated integer parameters without asymptotic assumptions.

## Proof

**Intersection geometry.** If centers \(u,v\) have Hamming distance one, their open neighborhoods intersect in the \(q-2\) other vertices on their common coordinate line. If their distance is two, the neighborhoods intersect in exactly the two intermediate words. At larger distance the intersection is empty. Consequently, a triple contained in two *distinct* open neighborhoods must lie entirely on a single coordinate line. In particular, any non-collinear triple contained in a neighborhood has a unique containing center.

**Singletons and pairs.** The empty support is shattered because the family is nonempty. Every one-point support has both signs: a center equal to the queried vertex excludes it, while an adjacent center includes it. A pair can be shattered only if its two vertices have distance one or two, because its all-positive trace requires a common neighbor.

For distance one, a common neighbor exists exactly when \(q\ge3\). A center at either queried vertex realizes a singleton trace; if \(d\ge2\), choosing a third symbol in the differing coordinate and changing a second coordinate realizes the empty trace. If \(d=1\), no center misses both vertices. Thus distance-one pairs are shattered exactly for \(d\ge2,q\ge3\).

For distance two, either of the two intermediate words realizes the all-positive trace, and a queried vertex itself realizes the empty trace. A singleton trace exists if a third alphabet symbol can be inserted into one differing coordinate (\(q\ge3\)), or if a third coordinate is available to change (\(d\ge3\)). If \((d,q)=(2,2)\), the two common neighbors have the all-positive trace and the queried vertices have the empty trace, so no singleton trace exists. This proves the pair classification. Counting pairs at distances one and two gives the quadratic coefficient above.

**Triples and their witnesses.** Any shattered triple must lie in \(N(c)\) for some center \(c\), since the all-positive trace must occur. Each member of \(N(c)\) differs from \(c\) in one coordinate. The multiplicities of these coordinates for a three-point support are therefore exactly \(3\), \(2+1\), or \(1+1+1\).

In type A, the three points lie on one coordinate line. A common open-neighborhood center outside the triple on that line requires \(q\ge4\), and singleton traces require a second coordinate \(d\ge2\). These conditions suffice: choose a fourth symbol on the line for the all-positive trace; choose a queried point as center to include the other two; change a second coordinate while matching a selected symbol to obtain its singleton; and change that second coordinate with the fourth line symbol to obtain the empty trace. Thus type A occurs exactly when \(d\ge2,q\ge4\).

In type B, write the triple, relative to \(c\), as two distinct changes \(i:a\) and \(i:b\) on axis \(i\), and one change \(j:t\) on another axis \(j\). To include both axis-\(i\) points while excluding the axis-\(j\) point requires a center on the first coordinate line whose symbol is different from the base symbol and both \(a,b\); hence \(q\ge4\) is necessary. It is sufficient: this third nonbase symbol realizes the pair; a two-coordinate change \((i:a,j:t)\), respectively \((i:b,j:t)\), realizes each mixed pair; centering at one of the two same-axis points realizes the other as a singleton; a different nonbase symbol on axis \(j\) realizes the axis-\(j\) singleton; the axis-\(j\) point itself realizes the empty trace; and \(c\) realizes the full triple. Thus type B occurs exactly when \(d\ge2,q\ge4\).

In type C, the three points are on different axes \(i,j,k\). The center \(c\) realizes the full triple; changes along any two of these axes realize the corresponding pair; and any one of the selected points, used as a center, realizes the empty trace. To isolate a single selected point, one can instead change its axis to a *different* nonbase symbol when \(q\ge3\); if \(q=2\), one must change its own axis together with a fourth, unused coordinate, which exists exactly when \(d\ge4\). The binary \(d=3\) case has no singleton trace because every neighbor of a chosen point is either \(c\), which sees all three, or a two-axis word, which sees two. Thus type C occurs exactly when \(d\ge3\) and \((q\ge3\text{ or }d\ge4)\).

**Counting triples.** Type A triples choose a coordinate line and three of its \(q\) symbols. There are \(d q^{d-1}\) coordinate lines, giving \(A_{d,q}\). Type B and type C triples have a unique center, by the intersection geometry. Type B chooses its center, an ordered pair of distinct axes, two distinct nonbase symbols on the first axis and one on the second: \(B_{d,q}\). Type C chooses its center, three distinct axes and one nonbase symbol on each: \(C_{d,q}\). Their center-relative axis multiplicities distinguish the three types, so the counts add without overlap.

**No shattered quadruple.** If a four-point set \(S\) were shattered, some center \(c\) would have \(S\subseteq N(c)\). If \(S\) meets at least two coordinate-axis groups of \(N(c)\), it has a triple \(T\) meeting at least two such groups. Such a triple has no containing open-neighborhood center other than \(c\), but \(c\) also contains the fourth point, making trace \(T\) on \(S\) impossible. If all four vertices lie on one coordinate line, the trace on \(S\) of a center on that line is either all of \(S\) or \(S\) minus one point, while an off-line center meets \(S\) in at most one point. No two-point trace can occur. Either way \(S\) is not shattered. Heredity of shattering excludes every larger support. This completes the polynomial classification.

## Verification

The standalone file `verify_hamming_open.py` implements direct exhaustive trace enumeration from the Hamming distance-one definition, independent of the center-relative proof. Running `python3 verify_hamming_open.py` tests fourteen parameter pairs, compares the complete counts through degree three against the formulas, and classifies all shattered triples by their three pairwise-distance signatures. It also exhaustively excludes every four-point support whenever the grid has at most 27 vertices. Its terminal status is `ALL_QARY_OPEN_HAMMING_SHATTERING_CHECKS_PASS`. These finite tests are not a substitute for the universal proof above.

## Relationship to prior work

Adler, Benediktsson and Macpherson (2020 preprint; 2022 journal) prove the sharp upper bound three and the exact VC-dimension threshold for **open** neighborhoods of Hamming graphs (Theorems 4.6–4.7), as well as a VC-density result (Theorem 4.8). Their accessible Section 4 was compared against the present three-type classification and coefficient formulas. The dimension thresholds and upper bound are credited, rather than asserted as new. Coudert, Csikós, Ducoffe and Viennot (2024) develop a general algorithm for graph VC dimension, primarily using **closed** neighborhoods; this does not supply the all-parameter open-neighborhood counts. A distinct exact closed-neighborhood census for \(H(d,q)\) counts a different family: for instance its cubic coefficient at \((d,q)=(2,4)\) is \(288\), versus the open-neighborhood value \(320\) here. The present result establishes the coefficientwise open-neighborhood census directly, rather than inferring it from an existing VC bound or from closed-neighborhood counts.

## Limitations

No claim is made for Hamming-distance balls of radius other than exactly one, for induced subgraphs of Hamming graphs, or for any unrestricted random sampling model. The proof concerns full Hamming graphs with a common alphabet size in every coordinate. Comparisons to available publications and research records do not settle all historical priority under alternative terminology. Independent mathematical validation has not been performed.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first public version 2020-07-31), especially Section 4; *Discrete Applied Mathematics*, DOI:10.1016/j.dam.2021.09.017.
2. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8, published 2024-07-11.
3. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel and Y. Vaxès, *Sample Compression Schemes for Balls in Graphs*, arXiv:2206.13254 (2022-06-27); *SIAM Journal on Discrete Mathematics* 37 (2023), DOI:10.1137/22M1527817. (Context for the distinction between general ball families and the radius-one trace census.)
