# Second Euclidean vertex-chord shell of classical parking-function polytopes: a parity law and two exceptional counts

## Finding
Let \(n\ge2\), and let \(P_n\subset\mathbb R^n\) be the convex hull of classical parking functions of length \(n\), using their standard integer coordinates. Write \(V_n\) for its distinct vertices. The *second vertex-chord shell* is the second-largest distinct squared Euclidean distance between unordered pairs of different vertices in \(V_n\); it is not the second-largest distance between arbitrary points of the continuous polytope.

The known squared Euclidean diameter is denoted by \(D_n\) and is reconstructed here solely as a reference value:
\[
D_n=2F(n)-F(\lfloor n/2\rfloor)-F(\lceil n/2\rceil),\qquad F(t)=\frac{(t-1)t(2t-1)}6.
\]
The new exact gap \(\Delta_n\) from the largest to the second distinct squared vertex-chord distance is
\[
\boxed{\Delta_n=\begin{cases}
n-1,&n\text{ even},\\
\min\{(n-1)^2/4,\ 2(n-1)\},&n\text{ odd}.
\end{cases}}
\]
Thus the second distance is exactly \(D_n-\Delta_n\). Its unordered-pair multiplicity has the exceptional two-dimension law
\[
\boxed{N_n=\begin{cases}2n!,&n\in\{4,9\},\\n!,&n\notin\{4,9\}.\end{cases}}
\]
Every second-shell pair is classified below by the two vertex layers and the number and labels of overlapping high coordinates. The only equality competition in odd dimensions occurs at \(n=9\), where two structurally different near-diametral mechanisms tie; the smaller exceptional multiplicity at \(n=4\) is an even-dimensional tie.

## Assumptions and scope
A parking function is a tuple of positive integers whose nondecreasing rearrangement \(b_1\le\cdots\le b_n\) satisfies \(b_i\le i\) for each \(1\le i\le n\). The known vertex description of \(P_n\) is: for each \(1\le k\le n\), the \(k\)-layer \(L_{n,k}\) consists of all distinct permutations of
\[
u_{n,k}=(\underbrace{1,\ldots,1}_{k\text{ entries}},k+1,k+2,\ldots,n).
\]
These layers are disjoint. A *high* coordinate is one strictly larger than \(1\). To classify second-shell pairs, put \(m=\lfloor n/2\rfloor\), and write the unordered pair of layers as \(\{k,l\}\) with \(k\le l\).

- If \(n=2\), the only second-shell layer pair is \(\{1,2\}\). If \(n=2m\ge4\), it is \(\{m-1,m+1\}\), with an additional pair \(\{1,2\}\) only at \(n=4\).
- If \(n=2m+1\), the layer pairs are \(\{m,m\}\) and \(\{m+1,m+1\}\) for \(m\le4\), and \(\{m-1,m+2\}\) for \(m\ge4\). At \(m=4\), all three occur.

For every listed layer pair with \(k+l=n\), the high supports of the two vertices are complementary. For \(k+l=n+1\), they are disjoint and leave exactly one common low coordinate. For \(k+l=n-1\), they overlap in exactly one coordinate, where the two entries are respectively the smallest high labels \(k+1\) and \(l+1\); all other coordinates carry a high entry in precisely one vertex. Within each permitted high support, all permutations of the remaining distinct high labels are allowed. These conditions are necessary and sufficient.

## Proof
**Step 1 (known vertices, exact rearrangement maximum).** By the vertex theorem of Amanbayeva--Wang, every vertex belongs to exactly one stated layer. For two given layers \(k,l\), the largest squared coordinate distance is achieved by opposite sorting of the two layer profiles, by the ordinary rearrangement inequality applied to their inner product. Define
\[
A_{k,i}=\begin{cases}1,&i\le k,\\i,&i>k,\end{cases}\qquad
B_{l,i}=\begin{cases}n+1-i,&i\le n-l,\\1,&i>n-l.\end{cases}
\]
With \(M_{k,l}=\sum_{i=1}^n(A_{k,i}-B_{l,i})^2\), direct expansion gives
\[
M_{k,l}=2F(n)-F(k)-F(l)-2J_{k,l},
\quad J_{k,l}=\begin{cases}
\displaystyle\sum_{i=k+1}^{n-l}(i-1)(n-i),&k+l<n,\\
0,&k+l\ge n.
\end{cases}
\]
This equality is valid for every integer \(1\le k,l\le n\). For \(k+l=n-1\), the sum has one term and \(J_{k,l}=kl\).

**Step 2 (only three neighboring layer-sum slices can compete).** When \(k+l<n\), at least one of \(k,l\) does not exceed \((n-1)/2\). Increasing that layer index by one changes precisely one profile entry from \(k+1\) to \(1\) (or symmetrically from \(l+1\) to \(1\)) against an opposite entry at least as large as the old entry. It strictly increases \(M_{k,l}\). Repeating shows that any profile with \(k+l\le n-2\) is strictly dominated by a profile with sum \(n-1\). When \(k+l>n\), decreasing either layer index greater than one changes a common \(1\) entry into a high value and strictly increases \(M_{k,l}\). Thus a profile with \(k+l\ge n+2\) is strictly dominated by one with sum \(n+1\). The maximizers for sum \(n\) yield the already-known diameter: balancing the strictly convex \(F(k)+F(n-k)\) gives \(k,l\in\{m,\lceil n/2\rceil\}\).

**Step 3 (best candidates after the diameter).** On the slice \(k+l=n\), strict discrete convexity of \(F\), with \(F(t+1)-F(t)=t^2\), gives the next-best deficit \(2m-1\) when \(n=2m\ge4\), attained only at \(\{m-1,m+1\}\), or \(4m\) when \(n=2m+1\) and \(m\ge2\), attained only at \(\{m-1,m+2\}\). There is no distinct second profile on this slice for \(n=2,3\).

On the slice \(k+l=n+1\), balancing the same convex function gives deficit \(m^2\) relative to \(D_n\), at \(\{m,m+1\}\) when \(n=2m\), and at \(\{m+1,m+1\}\) when \(n=2m+1\). On the slice \(k+l=n-1\), minimize \(F(k)+F(l)+2kl\) with fixed \(k+l=n-1\). Its second discrete difference is \(2n-8\), so for \(n\ge5\) it is minimized at balanced layers, while for \(n=4\) both allowable layer pairs tie; \(n=3\) has just \(\{1,1\}\), and \(n=2\) has no such pair. The resulting deficits are \(m^2-1\) at \(\{m-1,m\}\) for \(n=2m\ge4\), and \(m^2\) at \(\{m,m\}\) for \(n=2m+1\). Comparing these candidates proves the formula for \(\Delta_n\) and the complete list of layer pairs in the assumptions. The sole extra even tie is at \(m=2\) (\(n=4\)); the sole odd tie between \(m^2\) and \(4m\) is at \(m=4\) (\(n=9\)).

**Step 4 (exclude submaximal arrangements of diameter layers).** For balanced diameter layers, an optimal pairing has disjoint high supports, and any other pairing necessarily has a high--high collision and an equal number of low--low collisions. Replacing one collided high pair \((a,b)\) and one low--low pair \((1,1)\) by \((a,1)\) and \((1,b)\) increases squared distance by \(2(a-1)(b-1)\). Every high label in these layers exceeds \(m\); consequently, any nonoptimal arrangement loses at least \(2m^2\) from \(D_n\), strictly more than \(\Delta_n\). All second-shell pairs therefore attain the maximum of one of the non-diameter layer profiles from Step 3. For \(k+l=n\) or \(n+1\), equality requires disjoint high supports; for \(k+l=n-1\), equality requires exactly one high--high collision between the smallest high labels. This gives the asserted exhaustive geometric classification.

**Step 5 (multiplicity).** For each eligible unordered distinct-layer pair \(\{k,l\}\), choosing supports and permuting all remaining distinct high labels gives exactly \(n!\) unordered second-shell pairs. When \(k=l\), there are instead \(n!/2\) unordered pairs. For sum \(n-1\), fix the common coordinate containing the two smallest high labels, choose the partition of the remaining coordinates, and independently permute the rest; the count is again \(n!\) for distinguishable layers, \(n!/2\) for equal layers. The corresponding support partition argument works for sums \(n\) and \(n+1\). In even dimensions there is generally one distinct-layer candidate, except two at \(n=4\); in odd dimensions there are generally two equal-layer candidates (total \(n!\)) or one distinct-layer candidate, except all three at \(n=9\). This establishes the formula for \(N_n\).

## Verification
Run \(`python3 verify.py`\) using only the Python standard library. The checker independently enumerates all distinct parking-polytope vertices and every vertex pair through dimension \(6\), verifies both the first and second distinct distance, layer classification, and unordered-pair counts, and checks all oppositely sorted layer-pair maxima through dimension \(150\). The finite checks substantiate, but are not substitutes for, Steps 1--5. The exhaustive outputs are specified in VERIFICATION.md.

## Relationship to prior work
Amanbayeva--Wang gives the essential vertex classification (first publicly posted 2021-04-17). Behrend and collaborators identify the translation to the partial permutohedron \(\mathcal P(n,n-1)\). An earlier exact result on the Euclidean *diameter* of general partial permutohedra already supplies \(D_n\) and the balanced diametral geometry; no novelty is claimed for those. Here the new object is the *second distinct vertex-chord shell*: its exact gap, the additional neighboring-layer maximizers, all equality configurations, and the multiplicity anomalies at dimensions \(4\) and \(9\). This is not the combinatorial one-skeleton diameter studied in generalized parking-function literature, and is not implied by the first diameter's numerical value. The closest prior-result summary was accessible, but its complete linked technical document was not; this creates a priority qualification.

## Limitations
The statement concerns the standard Euclidean realization and distances among *vertices*, not all points of the continuous polytope (which has no isolated second-largest distance). It does not address arbitrary generalized parking parameters or higher chord shells. The possible existence of an older second-shell result under *partial permutohedron* or *win-vector polytope* terminology remains a bibliographic risk. Independent audit has not been performed.

## References
1. A. Amanbayeva and D. Wang, *The Convex Hull of Parking Functions of Length n*, arXiv:2104.08454 (first public posting 2021-04-17), https://arxiv.org/abs/2104.08454.
2. R. E. Behrend et al., *Partial permutohedra*, arXiv:2207.14253 (first posting 2022-07-28), https://arxiv.org/abs/2207.14253.
3. T. Hanada, G. Lentfer and A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, arXiv:2212.06885 (first posting 2022-12-13), https://arxiv.org/abs/2212.06885.
4. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first posting 2024-03-12), https://arxiv.org/abs/2403.07387.
5. *The Euclidean diameter of partial permutohedra saturates exactly at* \(m=2n\), prior research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-euclidean-diameter-of-partial-permutohedra-saturates-exactly--cb2829b66c5c. Only the searchable research summary, not its complete technical document, was available for comparison.
