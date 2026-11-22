# Sharp triameter at minimum degree two

## Finding

For every integer \(n\ge3\), let \(M_2(n)\) be the maximum triameter among all finite connected simple \(n\)-vertex graphs with minimum degree at least two. Then
\[
M_2(n)=\begin{cases}
3,&n=3,\\
4,&n=4,\\
6,&n=5,\\
2n-5,&n\ge6.
\end{cases}
\]
In particular, the minimum-degree-two case of the exact extremal triameter problem admits a sharp, uniform answer in every order.

## Assumptions and scope

Every graph here is finite, simple, undirected, connected and unweighted. Graph distance \(d_G(u,v)\) is the number of edges in a shortest path. For three distinct vertices define \(p_G(a,b,c)=d_G(a,b)+d_G(a,c)+d_G(b,c)\), and \(\operatorname{tr}(G)=\max p_G(a,b,c)\). The minimum degree condition \(\delta(G)\ge2\) requires every vertex to have at least two neighbors. The theorem takes the maximum across all such graphs of each order, not the triameter of each individual graph. We do not classify all attaining graphs.

## Proof

**Canonical three-point projection.** We use the following published lemma of Hak and Kozerenko [1, Lemma 3.2], whose explicit distance-ball construction and non-expansion proof are inspected in [1, Section 3]. For every triple of distinct vertices with perimeter \(p\), there is a surjective, nonexpanding map \(\varphi:V(G)\to V(H)\) onto a canonical model with
\[
|V(H)|=\left\lceil\frac p2\right\rceil+1.
\]
Nonexpanding means \(d_H(\varphi(u),\varphi(v))\le d_G(u,v)\); in particular an edge in \(G\) maps to a single vertex or an edge in \(H\). When \(p\) is even, \(H\) is a three-legged tree (possibly a path, with at most one zero-length leg). When \(p\) is odd, \(H\) is a triangle with three vertex-disjoint pendant paths of nonnegative lengths; their combined length is \((p-3)/2\). Every edge of \(H\) has an antecedent edge of \(G\). For reference, the leg lengths are \(\ell_i=(d_G(a_i,a_j)+d_G(a_i,a_k)-d_G(a_j,a_k)-\varepsilon)/2\) with \(\varepsilon=p\bmod 2\). They are nonnegative integers by the metric triangle inequalities. The cited proof builds the even model from the disjoint short-distance regions around the three feet, and the odd model from the three disjoint closed distance balls; each geodesic between feet maps onto its corresponding model geodesic, proving surjectivity and edge coverage.

Since the map is surjective, \(\lceil p/2\rceil+1\le n\), so \(p\le2n-2\). If \(p=2n-2\) then \(H\) is a tree on \(n\) vertices and \(\varphi\) is a bijection. For any edge in \(H\), an antecedent edge in \(G\) exists. No other distinct-vertex edge in \(G\) can map outside the edges of \(H\). Thus \(G\cong H\), contradicting the minimum degree condition because every nontrivial tree has a leaf.

If \(n\ge4\) and \(p=2n-3\), then \(p\) is odd and \(H\) also has \(n\) vertices. Again edge coverage and nonexpansion, combined with bijectivity, imply \(G\cong H\). But the combined length of the attached paths is \(n-3>0\), so \(H\) has a degree-one vertex, contradiction. Therefore \(\operatorname{tr}(G)\le2n-4\) whenever \(n\ge4\).

**New one-double-fibre obstruction.** Let \(n\ge6\) and suppose for contradiction some triple has \(p=2n-4\). This is even, so its canonical model \(H\) is a tree with \(|V(H)|=n-1\) and \(n-2\ge4\) edges. The surjection \(\varphi\) from the \(n\) vertices of \(G\) has precisely one fibre of size two, over some vertex \(z\in V(H)\), and all other fibres have size one.

Let \(x\) be any leaf of \(H\), with sole neighbor \(y\). If \(z\notin\{x,y\}\), both fibres at \(x\) and \(y\) are singletons. Denote their unique preimages by \(u\) and \(v\). Every neighbor of \(u\) maps, by nonexpansion, either to \(x\) or to \(y\). There is no different vertex in the fibre over \(x\), and only \(v\) in the fibre over \(y\). Hence \(\deg_G(u)\le1\), contradiction. Thus \(z\in\{x,y\}\), i.e. \(d_H(z,x)\le1\), for **every** leaf \(x\) of \(H\).

Such a \(z\) cannot exist. Indeed, a path with at least four edges has endpoints at distance at least four. A three-legged tree with three positive leg lengths totaling at least four has one leg of length at least two, whose end is at distance at least three from the end of any other positive leg. If one leg has length zero, the remaining two legs form a path with at least four edges. Therefore the canonical tree \(H\) has two leaves \(x,x'\) at distance at least three. No vertex of a graph lies within distance one of both, by the triangle inequality. This contradiction excludes \(p=2n-4\), and proves \(\operatorname{tr}(G)\le2n-5\) for \(n\ge6\).

**Constructions and small orders.** For \(n\ge6\), take two vertex-disjoint triangles with distinguished vertices \(s,t\) and connect \(s,t\) by a simple path of length \(L=n-5\). The resulting graph has \(L+5=n\) vertices and minimum degree two. Choose both non-distinguished vertices \(a,b\) of the first triangle and one non-distinguished vertex \(c\) of the second. Then \(d(a,b)=1\), \(d(a,c)=d(b,c)=L+2\), and the resulting perimeter is \(2L+5=2n-5\). For \(n=3\), the only admissible graph is the triangle and has triameter three. For \(n=4\), the four-cycle has triameter four and meets the general upper bound \(2n-4\). For \(n=5\), the complete bipartite graph \(K_{2,3}\) has minimum degree two and its three vertices in the larger shore are pairwise distance two, yielding triameter six, again meeting \(2n-4\). This completes the proof.

## Verification

The accompanying standalone `verify.py` enumerates every labelled graph of orders three through six having minimum degree at least two, filters to connected graphs, calculates exact all-pairs shortest paths and all triple perimeters, and verifies the formula at each order. It independently constructs and checks the triangle-barbell witness for each order six through twenty. An additional independent unlabelled atlas census in NetworkX checked the result through seven vertices, with qualifying graph counts \(1,3,11,61,507\) and respective maxima \(3,4,6,7,9\). These checks corroborate but do not replace the infinite proof.

## Relationship to prior work

Hak and Kozerenko [1] introduce the surjective nonexpanding canonical three-point projection (Lemma 3.2), prove general packing/vertex-connectivity bounds, and explicitly ask in Question 2 for the exact maximum triameter at given order and minimum degree. Their general minimum-degree bound does not yield the sharp value here; the exact vertex-connectivity extremum in their Theorem 1.3 also does not fix the minimum-degree-two maximum, because connectivity-one extremizers can have leaves, while biconnectivity excludes the sharp bridge examples. The new step is the size-one-defect fibre obstruction to the value \(2n-4\), followed by the sharp double-triangle-barbell construction.

Das and Abdioğlu [2, Theorem 4.3] characterize graphs with triameter \(2n-3\). This is consistent with, but insufficient to imply, the new exclusion of \(2n-4\) at minimum degree two. The general extremal order bound \(2n-2\) was known much earlier [1, Introduction]. No priority or independence certification is asserted for this result; separate historical review remains appropriate.

## Limitations

Only the exact maximum for minimum degree at least two is determined. All equality graphs are not classified; higher fixed minimum degrees and quantitative stability are not addressed. The structural proof relies on the cited, fully stated canonical projection lemma, rather than deriving that lemma anew. Computations over small graphs do not constitute an infinite proof. Historical priority is based on the cited inspected sources and targeted searches, not an exhaustive bibliography; no independent audit has been performed.

## References

[1] Artem Hak and Sergiy Kozerenko, *Triameter, distance packings, and vertex connectivity*, arXiv:2611.17259v1, first public November 12, 2026, Section 3 (especially Lemma 3.2) and Section 7 (Question 2). https://arxiv.org/html/2611.17259v1

[2] Angsuman Das and Cihat Abdioğlu, *On Triameter of a Graph*, Necmettin Erbakan University Journal of Science and Engineering **7** (2025), 535–543, especially Section 4 and Theorem 4.3. https://dergipark.org.tr/en/download/article-file/4516837
