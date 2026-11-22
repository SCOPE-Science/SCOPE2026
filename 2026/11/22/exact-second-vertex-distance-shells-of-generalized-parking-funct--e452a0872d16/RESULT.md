# Exact second vertex-distance shells of generalized parking-function polytopes

## Finding
For every integer \(n\ge4\) and positive integral vector \(\mathbf b=(b_1,\ldots,b_n)\) with \(b_1\ge2\), the second-largest **distinct squared Euclidean distance between vertices** of the generalized parking-function polytope admits an exact linear-size formula, including the number and forms of every realizing unordered vertex pair.

Write \(S_j=\sum_{i=1}^j b_i\) and \(t_j=S_{j+1}-1\) for \(0\le j<n\). Thus \(0<t_0<t_1<\cdots<t_{n-1}\). Define
\[
F(k)=\sum_{j=n-k}^{n-1}t_j^2\quad(0\le k\le n),\qquad m=\lfloor n/2\rfloor,\qquad D=F(m)+F(n-m).
\]
The maximal squared vertex separation is \(D\). Define three collections of positive **deficits** from \(D\):
\[
\begin{aligned}
\gamma_{\mathrm{miss}}&=t_m^2,\\
\gamma_{\mathrm{imb}}&=\begin{cases}t_m^2-t_{m-1}^2,&n=2m,\\ t_{m+1}^2-t_{m-1}^2,&n=2m+1,\end{cases}\\
\gamma_{\mathrm{ov}}(k)&=D-F(k)-F(n+1-k)+2t_{n-k}t_{k-1},
\quad 1\le k\le\left\lfloor\frac{n+1}{2}\right\rfloor.
\end{aligned}
\]
Then the **second distinct squared vertex distance** is
\[
\boxed{D_2=D-\Gamma,\qquad
\Gamma=\min\left\{\gamma_{\mathrm{miss}},\gamma_{\mathrm{imb}},
\gamma_{\mathrm{ov}}(k):1\le k\le\left\lfloor\frac{n+1}{2}\right\rfloor\right\}.}
\]
All quantities are explicit integer expressions in \(\mathbf b\), requiring \(O(n)\) arithmetic operations after partial sums. For every attaining candidate the complete corresponding set of unordered vertex pairs is described below; when several candidates tie, take their disjoint union.

* **Missing-coordinate class** (if \(\gamma_{\mathrm{miss}}=\Gamma\)): the two vertices have disjoint positive supports, with just one coordinate zero in both. Their positive-label counts are \((m-1,m)\) for even \(n=2m\), or \((m,m)\) for odd \(n=2m+1\). This gives \(n!\) pairs when \(n\) is even and \(n!/2\) when odd.
* **Imbalance class** (if \(\gamma_{\mathrm{imb}}=\Gamma\)): the positive supports partition all \(n\) coordinates; their positive-label counts are \((m-1,m+1)\) for even \(n\) or \((m-1,m+2)\) for odd \(n\). This gives \(n!\) pairs.
* **Single-overlap class** (for each \(k\) with \(\gamma_{\mathrm{ov}}(k)=\Gamma\)): put \(\ell=n+1-k\). The two vertices have positive-label counts \((k,\ell)\), cover all coordinates, and intersect in exactly one coordinate. That common coordinate contains the **smallest** positive label of each endpoint, respectively \(t_{n-k}\) and \(t_{k-1}\); all other positive entries are on disjoint supports and can be freely permuted. The number of unordered pairs is \(n!\) if \(k<\ell\), or \(n!/2\) if \(k=\ell\).

In each class, a vertex with \(r\) positive entries has exactly the labels \(t_{n-r},\ldots,t_{n-1}\), placed bijectively on its positive support. For odd \(n\), the middle overlap \(k=m+1\) always satisfies \(\gamma_{\mathrm{ov}}(m+1)=\gamma_{\mathrm{miss}}\), but the two corresponding pair classes are geometrically different. Consequently the prescribed enumeration counts every pair exactly once, even at all parameter-dependent ties.

The competition is nontrivial. For \(n=5\), the parameter vectors \((8,8,52,27,56)\), \((23,17,28,2,16)\), and \((38,38,25,25,64)\) give, respectively, an overlap-only winner, an imbalance-only winner, and a three-mechanism tie. In the last case \(\Gamma=10000\), \(D_2=102692\), and exactly \(240\) unordered pairs attain the second distance.

## Assumptions and scope
A \(\mathbf b\)-parking function is a positive integer vector whose sorted entries \(\beta'_i\) satisfy \(\beta'_i\le S_i\). Its convex hull in \(\mathbb R^n\) is denoted by \(\mathfrak X_n(\mathbf b)\). The metric is the standard coordinate Euclidean metric, with no dimension-dependent rescaling. Translating by \(-\mathbf1\) does not change distances. We use the Bayer–Borgwardt–Chambers–Daugherty–Dawkins–Deligeorgaki–Liao–McAllister–Morrison–Nelson–Vindas-Meléndez vertex theorem: after that translation, the vertices are precisely all distinct permutations of
\[
(\underbrace{0,\ldots,0}_{n-r\text{ entries}},t_{n-r},\ldots,t_{n-1}),\qquad 0\le r\le n.
\]
Here the condition \(b_1\ge2\) makes all positive labels nonzero and all vertex orbits distinct. Both the ordered values and their strict inequalities are necessary in the proof. The statement concerns second **distinct** squared distances among distinct vertices of the finite vertex set, not a nonexistent second-largest distance among all points of a continuum. The restriction \(n\ge4\) is part of the claim, not a numerical cutoff purported to be optimal.

## Proof
**1. Opposite rearrangement.** Write \(A_r=(0^{n-r},t_{n-r},\ldots,t_{n-1})\) in nondecreasing order. For any two fixed ranks \(r,s\), both squared norms are constant and maximizing squared separation amounts to minimizing their dot product. The rearrangement inequality places one sorted vector opposite the other. Hence the maximum within the rank pair is attained precisely in an opposite arrangement (up to permutations of zeros); strict positivity and strict inequality of the positive labels determine all overlap patterns. Call the resulting squared separation \(M(r,s)\). In particular
\[
M(r,s)=F(r)+F(s)\qquad\text{if }r+s\le n.
\]
If \(r+s=n+1\), exactly one coordinate overlaps, containing the two smallest positive labels, whence
\[
M(r,s)=F(r)+F(s)-2t_{n-r}t_{n-s}.
\]
No other arrangement at those ranks has the same squared distance unless it has that same described overlap configuration.

**2. First distance.** The successive increments \(F(r+1)-F(r)=t_{n-r-1}^2\) are strictly decreasing. Thus, for fixed \(r+s=n\), \(F(r)+F(s)\) is maximal only for the balanced ranks \(\{r,s\}=\{m,n-m\}\), giving \(D\). Ranks summing less than \(n\) can be enlarged without overlap, while ranks summing greater than \(n\) can be decreased, improving distance: in the opposite arrangement choose an endpoint whose smallest positive coordinate meets an equal-or-larger positive value of the other endpoint. Replacing that smallest coordinate by zero increases the squared separation from \((v-u)^2\) to \(v^2\) by \(u(2v-u)>0\), and reduces the rank sum by one. Such an endpoint exists whenever the rank sum exceeds \(n\). Iterating reduces to \(r+s=n\). This also proves that the only diameter rank pair is balanced and has disjoint positive supports.

**3. Rank profiles for the second distance.** For fixed sum \(r+s\le n\), strict concavity of \(F\) maximizes the sum for ranks as balanced as possible. The strongest rank profile with sum \(n-1\) therefore loses exactly \(t_m^2\) from \(D\); its ranks are those in the missing-coordinate class. Every sum less than \(n-1\) is strictly worse, because increasing an endpoint within disjoint supports strictly raises its squared norm. With sum \(n\), the best profile other than the balanced one has ranks displaced by one, giving the imbalance deficits in the statement; all further imbalance is strictly worse.

For sum exceeding \(n+1\), the rank-decrease argument in step 2 strictly increases the maximal squared separation until the sum becomes \(n+1\). Thus the only other candidates are the opposite arrangements with \(r+s=n+1\). After identifying a rank pair with its transpose, write \(r=k\le n+1-k=s\). The formula from step 1 gives precisely \(D-\gamma_{\mathrm{ov}}(k)\). All candidates are strictly below \(D\), because their rank profiles differ from the unique diametral profile or contain a positive overlap.

**4. Eliminating arrangements inside diametral ranks.** For ranks \(\{m,n-m\}\), a non-diametral arrangement necessarily contains at least one coordinate with two positive labels. Its squared separation is at least \(2t_m^2\) below \(D\) if \(n\) is even, and at least \(2t_mt_{m+1}>t_m^2\) below \(D\) if \(n\) is odd. Since the missing-coordinate candidate loses only \(t_m^2\), these nonoptimal arrangements cannot attain the second distance. For every other rank pair, any arrangement below its rank-pair maximum cannot attain the globally highest non-diametral distance, because that rank-pair maximum is either below the second distance or itself equals it. Therefore step 3 lists every second-distance pair, and the claimed formula follows.

**5. Counting all equality pairs.** For two distinct ranks with disjoint positive supports of total cardinality \(n\), choosing supports and permuting the distinct positive labels gives \(n!\) unordered pairs; if the rank sum is \(n-1\), the additional common-zero position still gives \(n!\). For identical ranks divide these counts by two. For a single-overlap pair, choose the shared coordinate, partition the other \(n-1\) coordinates into exclusive positive supports, and permute the remaining labels independently. Again there are \(n!\) ordered-by-rank choices, divided by two only when the ranks agree. Different candidate rank pairs or overlap patterns are disjoint. This establishes the equality classification and multiplicities, including ties.

## Verification
The standalone `verify.py` enumerates every vertex from the source theorem and every unordered vertex pair using exact integers, then independently extracts the largest and next-largest distinct squared distances with their multiplicities. It compares these with the formulas above for nine parameter vectors across dimensions four, five and six, including all three displayed phase examples and multiple distinct tie patterns. It prints `GENERALIZED_PARKING_SECOND_SHELL_EXACT_PASS cases=9`. These finite computations are corroboration, not an infinite proof. All infinite-domain assertions are supplied by the rank-profile and rearrangement proof.

## Relationship to prior work
Bayer and collaborators give the complete vertex/facet theory for arbitrary \(\mathbf b\), including combinatorial and circuit *graph* diameters. Those results supply the vertex premise here but not a second Euclidean distance level. Hanada–Lentfer–Vindas-Meléndez treat the two-parameter parking-function subfamily and polyhedral equivalences. Behrend and collaborators establish partial-permutohedron foundations.

An earlier result on partial permutohedra gives the **largest** Euclidean vertex distance for a consecutive-label specialization of the vertex orbit structure. A separate earlier result gives the second distinct vertex distance in the classical parking case, where \(b_1=1\) and the initial orbit degenerates. Neither supplies the present arbitrary, strictly positive unequal gaps, all-parameter competing overlap profiles and tie-count classification. Previously obtained second-distance results for Pitman–Stanley polytopes concern different standard coordinates; affine equivalence of related polytopes is not Euclidean isometry.

The value here is not the elementary maximum diameter, which is included only to normalize the deficit. It is the exact **next** distance, the exhaustive realizing-pair census and the parameter-dependent transition among missing-coordinate, imbalance and single-overlap mechanisms. Search comparisons cannot eliminate all unpublished or unindexed equivalent statements.

## Limitations
The theorem does not treat \(b_1=1\), where vertex-orbit coincidences alter multiplicities, or dimensions below four. It computes only the top two *distinct* squared-distance levels, not the full distance distribution or geodesic distances on the edge graph. It relies on the standard Euclidean coordinate realization: general affine maps to polymatroid or flow models need not preserve distances. Historical priority remains conditional on the inspected sources and indexed records; no independently conducted audit is claimed.

## References
1. M. M. Bayer, S. Borgwardt, T. Chambers, S. Daugherty, A. Dawkins, D. Deligeorgaki, H.-C. Liao, T. McAllister, A. Morrison, G. Nelson and A. R. Vindas-Meléndez, *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first public version 2024-03-12); *Discrete & Computational Geometry* 76 (2026), 339–377. https://arxiv.org/abs/2403.07387
2. M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first public version 2022-12-13). https://arxiv.org/abs/2212.06885
3. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial permutohedra*, arXiv:2207.14253 (first public version 2022-07-28). https://arxiv.org/abs/2207.14253
