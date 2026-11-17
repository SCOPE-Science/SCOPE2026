# The complete Euclidean diameter graph of every diagonal cube section

## Finding
For every integer \(n\ge3\) and \(-n<t<n\), let
\[
P_{n,t}=[-1,1]^n\cap\{x:\sum_{i=1}^n x_i=t\},\qquad
q=(n-|t|)/2,\quad k=\lfloor q\rfloor,\quad r=q-k.
\]
The exact squared Euclidean diameter is
\[
\operatorname{diam}_2(P_{n,t})^2=
\begin{cases}
8k,&n=2m+1\ \text{and}\ m\le q\le m+\tfrac12,\\
8(k+r^2),&\text{otherwise}.
\end{cases}
\]
Here the integer case \(r=0\) is included in the second branch, except when the first branch applies, where both coincide. The number \(N_{n,t}\) of **unordered distinct diametral endpoint pairs** is
\[
N_{n,t}=\begin{cases}
0,&q=0,\\
\displaystyle\frac{n!}{2(k!)^2(n-2k)!},&r=0,\ q>0,\\
\displaystyle\frac{n!}{2(k!)^2},&n=2k+1,\ 0<r<1,\\
\displaystyle\frac{n!}{2(k!)^2(n-2k-2)!},&0<r<1,\ 2(k+1)\le n.
\end{cases}
\]
All diametral endpoints are vertices and the pairs are characterized explicitly in the proof. In particular, when \(n=2m+1\), the diameter is **constant** at \(\sqrt{8m}\) on the entire interval \(|t|\le1\); when \(n=2m\), the squared diameter equals \(4n-8|t|+2t^2\) for \(|t|\le2\). The diametral-pair count generally jumps at integer-section thresholds even though the diameter itself is continuous.

## Assumptions and scope
The ambient norm is the standard Euclidean norm inherited from \(\mathbb R^n\). A *diametral pair* means an unordered pair \(\{x,y\}\) of distinct points with \(\|x-y\|_2=\operatorname{diam}_2(P_{n,t})\). The degenerate cases \(t=\pm n\) are singleton sections with diameter and pair count both zero; the displayed formulas extend to them by the first count branch \(q=0\). All assertions are for arbitrary real \(t\), not merely rational offsets. No combinatorial genericity is assumed.

## Proof
**Vertex reduction.** Reflection through the origin interchanges \(P_{n,t}\) and \(P_{n,-t}\). For \(t\ge0\), the affine isometry up to factor two \(y_i=(1-x_i)/2\) identifies the section with \(Q_{n,q}=[0,1]^n\cap\{\sum_i y_i=q\}\). If \(q=k+r\), \(0\le r<1\), every vertex of \(Q_{n,q}\) is a permutation of
\[
v=(\underbrace{1,\ldots,1}_{k},r,\underbrace{0,\ldots,0}_{n-k-1})
\]
when \(r>0\); for \(r=0\) it has exactly \(k\) ones. This follows because at a vertex at most one coordinate can lie strictly between zero and one (otherwise an opposite perturbation preserves the sum and box constraints). Conversely every such point is a vertex. The squared Euclidean distance is strictly convex in either endpoint, so a nontrivial convex combination cannot be a diametral endpoint: all diametral pairs consist of vertices.

**Rearrangement.** Every vertex has squared norm \(k+r^2\) in \(y\) coordinates. The largest squared separation therefore equals \(2(k+r^2)-2I\), where \(I\) is the smallest inner product between two permutations of \(v\). The rearrangement inequality, proved by swapping an inverted pair, gives its minimum when the lists are oppositely ordered. In the original \(x\) coordinates squared distances are four times as large.

If \(r=0\), \(k\le n/2\), and the minimum inner product is zero: two disjoint \(k\)-subsets of ones. If \(0<r<1\) and \(2(k+1)\le n\), the two positive supports can be disjoint, again giving \(I=0\). In the only remaining case \(n=2m+1\), \(k=m\), and \(0<r\le1/2\), an overlap is forced. The unique optimal overlap type puts the two fractional coordinates at the same index and places their sets of \(m\) unit coordinates in the complementary \(2m\) indices, giving \(I=r^2\). An overlap involving a unit coordinate would contribute at least \(r>r^2\), while unit-unit overlap costs one. Hence the stated diameters are exact.

**Equality and enumeration.** In the integral case, equality holds precisely for disjoint \(k\)-subsets of unit-coordinate indices; the number of unordered pairs is \(n!/[2(k!)^2(n-2k)!]\). In the disjoint-support fractional case, one assigns disjoint sets of \(k\) unit coordinates and one distinguished fractional coordinate to each endpoint; this gives \(n!/[2(k!)^2(n-2k-2)!]\). In the odd central fractional case, one chooses the common fractional-coordinate position and partitions the other \(2m\) indices into two complementary \(m\)-subsets; this gives \(n!/[2(m!)^2]\). The strict equality cases of rearrangement prove no other pairs exist. The singleton convention finishes the endpoints.

Finally, the odd central condition \(m\le(n-|t|)/2\le m+1/2\) is equivalent to \(|t|\le1\), giving the plateau. For even \(n=2m\) and \(0<|t|<2\), \(k=m-1\) and \(r=1-|t|/2\); substitution yields \(8(m-1+r^2)=4n-8|t|+2t^2\), extending continuously to the endpoints. This completes the classification.

## Verification
The accompanying `verify.py` exhaustively enumerates vertices of \(Q_{n,q}\), computes every squared vertex distance as a rational number, and compares the maximum and the number of attaining unordered pairs against the closed formulas for **55 exact parameter cases** with \(3\le n\le7\). It reports a passed assertion for all cases. This finite diagnostic is not the proof of the all-dimensional or real-parameter claims; the vertex argument and rearrangement equality analysis above are.

## Relationship to prior work
Brandenburg, Curtis, Giardino, Meroni, and Padrol (2026) study the reconstruction of cube sections from their graphs. The present classification addresses their **Euclidean metric diameter graph**, which is not the graph of edges and is not fixed by combinatorial type: within one section chamber the diameter varies with the offset. Separate existing work determines the **minimum width** of diagonal cube sections and the Euclidean facial distance of integer hypersimplices. Neither invariant alone determines the full Euclidean diameter and all diametral-pair multiplicities at nonintegral offsets. The integer-slice diameter follows directly from the disjoint-support description and is not offered as a standalone novelty claim.

## Limitations
The result concerns only sections orthogonal to the all-ones vector, not arbitrary hyperplane sections of a cube or general sections of other parallelotopes. It gives Euclidean, not intrinsic graph-metric, diameters. Some highly relevant full manuscripts could not be read in this investigation; bibliographic and abstract evidence does not establish historical priority. No independent mathematical audit has been performed.

## References
1. M.-C. Brandenburg, J. Curtis, C. Giardino, C. Meroni, A. Padrol, *Reconstruction of slices of cubes*, arXiv:2610.09939v1 (first publicly posted 2026-10-07), https://arxiv.org/abs/2610.09939.
2. *A sharp minimum-width plateau for all diagonal sections of the hypercube* (2026-10-18), publicly available mathematical research record, for the distinct width invariant.
3. *Euclidean thickness and a two-orbit phase transition for hypersimplices* (2026-10-18), publicly available mathematical research record, for the distinct thickness invariant.
