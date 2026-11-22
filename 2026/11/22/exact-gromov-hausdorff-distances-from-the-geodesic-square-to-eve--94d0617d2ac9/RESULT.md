# Exact Gromov–Hausdorff distances from the geodesic square to every odd regular circle sample

## Finding

Let \(P_n\) be the set of \(n\) equally spaced points on a Euclidean unit circle, **with the shorter-arc distance inherited from the circle**, rather than Euclidean chord distance or the intrinsic metric of the polygonal edges. For **every odd integer** \(m\ge5\),
\[
\boxed{d_{\mathrm{GH}}(P_4,P_m)=\frac{\pi(m-1)}{4m}=\frac\pi4-\frac\pi{4m}.}
\]
This supplies the odd-cardinality family in the exact geodesic-square-to-regular-polygon problem. For example, the seven-point case equals \(3\pi/14\), and the nine-point case equals \(2\pi/9\). The obstruction is an odd cycle whose edges would all have to map to edges of a bipartite four-cycle under any correspondence of smaller distortion. The upper bound is attained by an explicit four-block cyclic map.

## Assumptions and scope

For \(n\ge2\), identify \(P_n\) with indices \(0,1,\ldots,n-1\), and define
\[
d_n(i,j)=\frac{2\pi}{n}\min\{|i-j|,\,n-|i-j|\}.
\]
A correspondence \(R\subseteq P_4\times P_m\) is a relation surjecting onto both factors. Its distortion is
\[
\operatorname{dis}(R)=\max_{(x,y),(x',y')\in R}|d_4(x,x')-d_m(y,y')|.
\]
The finite-space correspondence formula is \(2d_{\mathrm{GH}}(P_4,P_m)=\min_R\operatorname{dis}(R)\). The **lower bound** is for all, including multivalued and noncyclic, correspondences. Only the constructive upper-bound correspondence is a cyclic single-valued surjection from \(P_m\) onto \(P_4\). The circle radius is one throughout, so its circumference is \(2\pi\).

## Proof

Fix an odd \(m\ge5\) and put \(\theta=(m-1)/(4m)\). To avoid factors of \(2\pi\), write \(\rho_n=d_n/(2\pi)\). The distinct distances in \(P_4\) under \(\rho_4\) are \(0,1/4,1/2\).

**Lower bound: an odd-cycle obstruction.** Choose an integer \(s\) by
\[
s=\begin{cases}(m-1)/4,&m\equiv1\pmod4,\\(m+1)/4,&m\equiv3\pmod4.\end{cases}
\]
Then \(1\le s<m/2\) and \(s/m=1/4\pm1/(4m)\). Consequently
\[
\min\{s/m,\,1/2-s/m\}=\theta.
\]
Suppose that a correspondence \(R\) had \(\operatorname{dis}(R)<2\pi\theta\). For each \(y_i\in P_m\), select any \(x_{f(i)}\in P_4\) with \((x_{f(i)},y_i)\in R\). This selection is possible by surjectivity onto \(P_m\); it need not be surjective onto \(P_4\). Every pair \(y_i,y_{i+s}\) has normalized distance \(s/m\), with indices interpreted modulo \(m\). Since the discrepancy from the square distances \(0\) and \(1/2\) is at least \(\theta\), the assumed strict inequality forces
\[
\rho_4(f(i),f(i+s))=1/4\qquad\text{for every }i.
\]
Thus \(f(i)\) and \(f(i+s)\) are adjacent vertices of a four-cycle, so their labels have opposite parity. The permutation \(i\mapsto i+s\pmod m\) decomposes into cycles of common length \(m/\gcd(m,s)\). This length is **odd** because \(m\) is odd. Label parity cannot alternate consistently around any such odd cycle. This contradiction proves \(\operatorname{dis}(R)\ge2\pi\theta\) for every correspondence \(R\), and hence \(d_{\mathrm{GH}}\ge\pi\theta\).

**Upper bound: consecutive four-block matching.** Write \(m=4k+1\) or \(m=4k+3\), with \(k\ge1\). Partition the cyclic indices \(0,\ldots,m-1\) into four consecutive, nonempty blocks \(B_0,B_1,B_2,B_3\), of respective sizes
\[
(|B_0|,|B_1|,|B_2|,|B_3|)=
\begin{cases}(k+1,k,k,k),&m=4k+1,\\(k+1,k+1,k+1,k),&m=4k+3.\end{cases}
\]
Map every \(y_i\in B_j\) to square vertex \(x_j\). This map is surjective, and its graph is a correspondence. We check all three square-distance classes, measuring distance in circumference-normalized units.

If two indices lie in the **same block**, their shorter circular index separation is at most \(k\), so the distance mismatch from target \(0\) is at most \(k/m\le\theta\).

If their labels are **adjacent modulo four**, the indices are distinct, hence their source distance lies in \([1/m,(m-1)/(2m)]\). Their square target distance is \(1/4\); its largest deviation on this interval is at most
\[
\max\left\{\frac14-\frac1m,\,\frac{m-1}{2m}-\frac14\right\}
=\frac{m-2}{4m}<\theta.
\]

Finally, if their square labels are **opposite**, the shorter path between the index blocks has to cross at least one full intervening block. Each intervening block has at least \(k\) elements; therefore the two indices are separated by at least \(k+1\) cyclic steps, and their normalized circular distance is at least \((k+1)/m\). For either odd residue class,
\[
\frac{k+1}{m}\ge\frac{m+1}{4m}=\frac12-\theta.
\]
Since their source distance is at most \(1/2\), its mismatch from the opposite-square target \(1/2\) is at most \(\theta\).

These cases exhaust all pairs in the graph correspondence, so its distortion is at most \(2\pi\theta\). Together with the universal lower bound this proves the displayed identity. Equality is visible in the construction: for \(m=4k+1\), the endpoints of the size-\(k+1\) block lie \(k\) steps apart and map to the same square vertex; for \(m=4k+3\), suitable points in opposite blocks have separation \(k+1\), yielding deviation \(\theta\).

## Verification

The self-contained standard-library script `check_odd_polygon.py` uses only integer arithmetic: for each odd \(m\), multiplying normalized distance by \(4m\) makes the four-point distances integer multiples of \(m\) and the \(m\)-point distances integer multiples of \(4\). Running `python check_odd_polygon.py` successfully checks the proposed correspondence's **exact** scaled distortion \(m-1\) and the parity-step obstruction for all \(199\) odd sizes \(5\le m\le401\). It additionally searches every surjective single-valued map \(P_m\to P_4\) modulo square rotation for \(m=5,7,9\), inspecting respectively \(60\), \(2100\), and \(46620\) maps, finding exactly the claimed minima. These finite checks are regression checks, **not** a substitute for the all-odd analytic lower bound or an enumeration of arbitrary correspondences.

## Relationship to prior work

Lim–Mémoli–Smith (2021, arXiv:2105.00611, Appendix C, Question VI) explicitly asks for all distances between regular samples of the circle, and determines circle-to-sample and consecutive-sample values. In particular, \(P_4\) to \(P_5\) is already known and is included only as a compatible endpoint. Talipov (2022, arXiv:2210.09971, Theorems 3.1–3.3) settles divisible cardinalities and comparisons with two- or three-vertex spaces; none of those statements covers \(P_4\) versus odd \(m\ge7\). A published exact \(P_4\)-to-\(P_{4k+2}\) formula handles the remaining even nondivisible cardinalities, using a different fiber-packing obstruction. Its statement explicitly excludes odd target cardinalities, and neither it nor the divisible-case theorem implies the present odd-cycle argument. Together these sources and the present theorem give the full \(P_4\)-to-\(P_m\) profile for \(m\ge4\). This is a statement-level novelty comparison, not a guarantee of absolute historical priority.

## Limitations

The new theorem is for **odd integer** target cardinalities \(m\ge5\), with the inherited **circle shorter-arc metric** on finite vertex sets; it does not concern polygon-edge length metrics, chord distances, arbitrary four-point spaces, or pairs with source cardinality other than four. It provides an optimal correspondence but does not classify every optimal correspondence. The case \(m=5\) follows already from the known consecutive-cardinality theorem. The historical originality assessment is limited to inspected and searchable sources, with potential unindexed or later equivalent arguments as residual risk. No independent audit has been conducted.

## References

1. S. Lim, F. Mémoli, Z. Smith, *The Gromov–Hausdorff distance between spheres*, arXiv:2105.00611 (first public 3 May 2021), Appendix C and Question VI, https://arxiv.org/html/2105.00611v6.
2. T. Talipov, *Gromov–Hausdorff distance between vertex sets of regular polygons inscribed in a given circle*, arXiv:2210.09971 (first public 18 October 2022), Theorems 3.1–3.3, https://arxiv.org/html/2210.09971v1.
3. *Exact Gromov–Hausdorff distances from the geodesic square to regular \(4k+2\)-gons*, dated published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-gromov-hausdorff-distances-from-the-geodesic-square-to-reg--5c67e3568e56.
