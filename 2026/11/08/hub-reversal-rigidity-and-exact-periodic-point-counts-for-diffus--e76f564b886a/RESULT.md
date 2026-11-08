# Hub-reversal rigidity and exact periodic-point counts for diffusion on friendship graphs

## Finding
Let \(W_r=K_1\vee(rK_2)\) be the friendship graph made from \(r\ge2\) labelled triangles sharing one hub. In synchronous integer diffusion, each vertex sends one chip to each adjacent vertex carrying a strictly smaller integer label. Identify configurations differing by the addition of the same integer at every vertex, but do not identify different vertex labels or temporal phases.

Let \(N_r\) count translation classes that are **already periodic at time zero**. Then
\[
N_r=3^r+2(6r-2)^r\qquad(r\ge2).
\]
Normalize the hub label to zero and write \(D\) for its change in the first update. For initially periodic configurations, the hub-reversal spectrum is **exactly** \(D\in\{-2r,0,2r\}\), with respective populations \((6r-2)^r,3^r,(6r-2)^r\). In particular no intermediate nonzero hub displacement occurs, although the hub has \(2r\) neighbours.

There is one fixed translation class, the constant configuration; all remaining classes have primitive period two. Thus the number of distinct primitive-two temporal orbits, up to common chip translation but not graph automorphisms, is
\[
\frac{3^r+2(6r-2)^r-1}{2}.
\]
Moreover, \(N_r\sim2e^{-1/3}(6r)^r\) as \(r\to\infty\). For \(r=2,3,4,5\), the exact counts are \(209,8219,468593,34420979\), respectively. The single-triangle boundary \(r=1\) is the previously covered complete graph \(K_3\), which has \(19\) initially periodic translation classes; it is not asserted as a new case.

## Assumptions and scope
The graph is simple, undirected and vertex-labelled. Its hub is \(h\), and the remaining vertices are ordered labelled pairs \((a_j,b_j)\) for \(1\le j\le r\). Edges are \(ha_j,hb_j,a_jb_j\) for each \(j\). Every vertex label is an arbitrary integer. Write \(\operatorname{sgn}(t)\in\{-1,0,1\}\) for the sign of an integer.

The simultaneous update is
\[
F(x)_v=x_v+\sum_{u\sim v}\operatorname{sgn}(x_u-x_v).
\]
The dynamics commute with addition of a constant vector, and total chip mass is conserved. Hence a translation class satisfying \(F^2([x])=[x]\) must satisfy the exact equality \(F^2(x)=x\), because any common additive shift after two updates would alter the conserved total unless the shift were zero. All counts concern **initially periodic** classes, not the infinitely many transient configurations that eventually reach cycles.

## Proof
**0. Period reduction.** The finite-graph diffusion theorem of Long and Narayanan (Reference 2) shows that every integer-diffusion orbit eventually has period one or two. An already periodic orbit must therefore have least period one or two, and its initial state satisfies the exact relation \(F^2(x)=x\). This established general result is used as a premise; the new work is the graph-specific classification and count. The translation-normalized relation is also exact by the chip-sum argument above.

**1. Edge-reversal criterion.** For any finite simple graph, suppose \(F^2(x)=x\), and put \(y=F(x)\). For an edge \(uv\), orient its notation arbitrarily and set \(s_{uv}=\operatorname{sgn}(x_u-x_v)\) and \(t_{uv}=\operatorname{sgn}(y_u-y_v)\). Summing the update differences against \(y\) gives the identity
\[
0=\sum_v y_v(F^2(x)_v-x_v)
=-\sum_{uv\in E}(s_{uv}+t_{uv})(y_u-y_v).
\]
Each edge term is nonpositive, because whenever \(y_u\ne y_v\), the sum \(s_{uv}+t_{uv}\) either vanishes or has the sign of \(t_{uv}\). Thus every edge with \(y_u\ne y_v\) has \(s_{uv}+t_{uv}=0\). Interchange \(x\) and \(y\) (since \(F(y)=x\)) to obtain the same conclusion on every edge with \(x_u\ne x_v\). If both differences vanish, their two signs are zero anyway. Therefore every edge satisfies \(t_{uv}=-s_{uv}\). Conversely, if all edge signs reverse or remain zero, the next update reverses all transfers, giving \(F^2(x)=x\). This proves the necessary-and-sufficient criterion without assuming that a finite computation proves periodicity.

**2. Local triangle inequalities.** Normalize \(x_h=0\), and let \((a,b)\) be the two initial integer labels in one triangle. Set \(D=F(x)_h\). Then
\[
D=\sum_{j=1}^{r}(\operatorname{sgn}(a_j)+\operatorname{sgn}(b_j)),
\]
while the new labels of this pair relative to the updated hub are
\[
A=a-\operatorname{sgn}(a)+\operatorname{sgn}(b-a)-D,\qquad
B=b-\operatorname{sgn}(b)+\operatorname{sgn}(a-b)-D.
\]
The edge-reversal criterion is exactly
\[
\operatorname{sgn}(A)=-\operatorname{sgn}(a),\quad
\operatorname{sgn}(B)=-\operatorname{sgn}(b),\quad
\operatorname{sgn}(A-B)=-\operatorname{sgn}(a-b).
\]

For \(D=0\), a zero coordinate forces the other coordinate to be zero. If \(a>0\), then \(A<0\) forces \(a=1\) and \(b<a\), since the local change of \(a\) is at least \(-2\). The second coordinate must be \(b=-1\), as \(b=0\) violates its zero-edge condition and any smaller negative value cannot cross zero in a two-edge update. Reversing the pair and all signs handles the remaining cases. Consequently the local possibilities are exactly
\[
(a,b)\in\{(0,0),(1,-1),(-1,1)\} \qquad(D=0).
\]
Each has local contribution \(\operatorname{sgn}(a)+\operatorname{sgn}(b)=0\), so all \(3^r\) independent selections are globally consistent.

Now let \(D>0\). Negative \(a\) is impossible: its local change is at most \(2\), so \(A\le-1+2-D\le0\), whereas sign reversal requires \(A>0\). The same holds for \(b\). If either coordinate vanishes, its zero edge stays zero only when \(D=1\) and the other coordinate is \(1\) or \(2\). This gives precisely four ordered pairs \((0,1),(0,2),(1,0),(2,0)\), each contributing \(1\) to \(D\).

If both coordinates are positive, the internal edge sign reverses if and only if \(|a-b|\le1\): the one-step change in their difference is \(-2\operatorname{sgn}(a-b)\). For \(a=b=k>0\), inversion of each hub edge requires \(1\le k\le D\); for \((a,b)=(k,k+1)\) or \((k+1,k)\) it requires \(1\le k<D\). Thus the complete strictly-positive local set for every \(D\ge1\) is
\[
\mathcal A_D=
\{(k,k):1\le k\le D\}\cup
\{(k,k+1),(k+1,k):1\le k<D\},
\quad |\mathcal A_D|=3D-2.
\]
Every member contributes exactly \(2\) to the hub change. No other integer pair satisfies all three sign reversals.

**3. Global hub rigidity.** If \(D=1\) and \(r\ge2\), every triangle contributes at least \(1\) (by the previous classification), contradicting the identity expressing \(D\) as the sum of triangle contributions. If \(D\ge2\), all pairs must be strictly positive, each contributes \(2\), and hence necessarily \(D=2r\). There are then \(|\mathcal A_{2r}|^r=(6r-2)^r\) globally consistent labelled choices. Applying \(x\mapsto-x\), which commutes with diffusion up to sign, gives the same number for \(D=-2r\) and excludes all other negative values. Together with the \(D=0\) branch, this proves the claimed census and exact displacement spectrum.

**4. Temporal periods and growth.** The edge-reversal criterion ensures every counted class is fixed by the second iterate. A fixed state on a connected graph must have equal labels at all vertices: at a vertex of maximum value any strictly smaller neighbour would give a negative net update, so a fixed maximum has only equal neighbours; connectedness propagates equality. Thus there is exactly one fixed class. Every other counted class belongs to a temporal pair; dividing their count by two gives the orbit formula. Finally,
\[
(6r-2)^r=(6r)^r\left(1-\frac1{3r}\right)^r
\sim e^{-1/3}(6r)^r,
\]
and \(3^r\) is negligible by comparison.

## Verification
The attached `direct_dynamics.py` applies the diffusion rule by summing over graph edges, independently of the local classification. Its exhaustive normalized coordinate windows are \([-5,5]\) for \(r=1\), \([-7,7]\) for \(r=2\), and \([-6,6]\) for \(r=3\); it checks respectively \(121\), \(50625\), and \(4826809\) states. It confirms the exact hub-displacement populations. The proof above bounds all initially periodic nonhub coordinates by \(2r\) in magnitude for \(r\ge2\), so the last two domains contain every periodic state for those graph sizes.

The separate `local_poly_checker.py` enumerates possible integer ordered pairs directly from the three sign-reversal conditions and convolves their hub-change weights, checking every \(1\le r\le14\) against the stated formulas. Its bounded search is justified by the proved classification; its finite checks are supplementary, not a proof for arbitrary \(r\). Captured textual outputs are `direct_out.txt` and `local_out.txt`. Run both scripts with Python 3; the direct checker additionally uses NumPy.

## Relationship to prior work
Duffy, Lidbetter, Messinger and Nowakowski introduced the integer diffusion process and derived the general **property-plus** characterization of configurations already on periods of at most two; their relevant results concern paths, wheels, stars, complete graphs and complete bipartite graphs, not the labelled friendship-graph count or sharp hub-change spectrum. Long and Narayanan proved eventual period at most two for arbitrary finite graphs, but that general statement does not enumerate initial recurrent states. Mullen, Nowakowski and Cox counted two-periodic configurations on paths by orientation methods, not on graphs with triangular blocks. Those general and path-specific facts are credited as prior work; no claim of novelty is made for the edge-reversal criterion or general period bound. Earlier complete-graph counts include \(W_1=K_3\), excluded from the new scope.

## Limitations
The result counts configurations **already** on temporal periods; it does not classify their attracting transient basins, entry times, or fixed-total-chip counts. Translation is the only spatial equivalence: neither vertex permutations nor graph automorphisms are factored out. Evidence of originality is literature-led and best-knowledge rather than an exhaustive historical-priority certificate; an unindexed prior formula remains possible. Verification is computationally finite; the unbounded statement is established by the written proof. Independent mathematical audit has not been performed.

## References
1. C. Duffy, T. F. Lidbetter, M. E. Messinger and R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, initial public version submitted 2016-09-19, https://arxiv.org/abs/1609.05792 . Examined accessible arXiv HTML of version 5, especially Sections 1, 2 and 3.1.
2. J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, initial public version 2017-04-13, https://arxiv.org/abs/1704.04295 . Examined accessible full-text HTML, especially theorem and proof.
3. T. Mullen, R. Nowakowski and D. Cox, *Counting Path Configurations in Parallel Diffusion*, arXiv:2010.04750, first submitted 2020-10-09, https://arxiv.org/abs/2010.04750 . Examined accessible full-text HTML, especially introduction and path enumeration theorem.
