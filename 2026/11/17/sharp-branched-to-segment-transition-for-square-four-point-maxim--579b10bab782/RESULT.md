# Sharp branched-to-segment transition for square four-point maximal-distance minimizers

## Finding

Let \(a>0\) and let \(M_a=\{(-a,-a),(-a,a),(a,-a),(a,a)\}\). For each \(r\geq0\), define the exact minimal connected length
\[
L_a(r)=\inf\left\{\mathcal H^1(\Sigma):\ \Sigma\subset\mathbb R^2\text{ compact and connected},\quad \max_{p\in M_a}\operatorname{dist}(p,\Sigma)\leq r\right\}.
\]
Then the infimum is attained and
\[
\boxed{L_a(r)=\begin{cases}
2a(1+\sqrt3)-4r,&0\leq r\leq 2a/\sqrt3,\\
2a-2\sqrt{r^2-a^2},&2a/\sqrt3\leq r\leq\sqrt2 a,\\
0,&r\geq\sqrt2 a.
\end{cases}}
\]
The first two branches meet with common derivative \(-4\), but the shape of an explicit minimizer changes at the sharp critical radius \(r_c=2a/\sqrt3\): four positive leaf segments of a two-junction Steiner tree shrink to zero, leaving one straight segment. The formula treats all compact connected competitors, not only polygonal trees or fixed topologies.

## Assumptions and scope

Distances and lengths are Euclidean and \(\mathcal H^1\) denotes one-dimensional Hausdorff measure. The four prescribed sites are points, *not* the entire square boundary. Every real \(a>0\) and every real \(r\geq0\) are allowed. The zero-length regime permits a singleton set. The claimed geometric transition concerns the existence of the explicit optimal forms below; it does not claim that there are no other minimizers at transition radii.

## Proof

**1. Reduction to three convex topology problems.** For a fixed \(r\), write \(D_i=\overline B_r(c_i)\) for the four closed disks about the four square vertices \(c_i\). A competitor meets every \(D_i\). Choose a point \(x_i\in\Sigma\cap D_i\). A shortest Euclidean Steiner tree spanning these four (possibly repeated) points has length no larger than \(\mathcal H^1(\Sigma)\); conversely, any such Steiner tree meets all four disks and is feasible. The standard elementary structure theorem for a planar Euclidean four-terminal Steiner minimum tree says that it is either a full tree with at most two trivalent Steiner points or a degeneration of such a tree. Every such topology occurs as a degeneration of one of the three partitions of four labeled terminals into two unordered pairs. Introducing two junctions \(u,v\) (allowing zero-length edges and coincident junctions) therefore gives the exact reduction
\[
L_a(r)=\min_{\{I,J\}}\;\min_{u,v\in\mathbb R^2}
\left(\|u-v\|+\sum_{i\in I}\operatorname{dist}(u,D_i)+\sum_{j\in J}\operatorname{dist}(v,D_j)\right),
\]
where \(I,J\) range over the three two-plus-two partitions of the four vertices. Indeed, for fixed junctions, each selected leaf segment has minimum length \(\operatorname{dist}(u,D_i)=(\|u-c_i\|-r)_+\), attained by projection onto the closed disk. Every objective displayed here is jointly convex in \((u,v)\), coercive up to irrelevant zero-length degeneracies, and has a minimizer. The finite union of its segment minimizers attains the required global value.

**2. Adjacent-corner pairing.** Consider the partition with the two left vertices incident to \(u\) and the two right vertices incident to \(v\). Reflect the objective across the horizontal axis, which preserves each labeled pair, and average with its reflected image. By convexity, this produces a minimizing pair on the horizontal axis. Next apply reflection across the vertical axis *together with exchanging the two junctions*, and average again. A minimizer of the form \(u=(-t,0)\), \(v=(t,0)\) results. The case \(t<0\) cannot improve on \(-t>0\), because it moves each junction further from both of its assigned vertices without changing bridge length. Likewise no \(t>a\) improves on \(t=a\). Thus
\[
L_{\mathrm{side}}(r)=\min_{0\leq t\leq a}\left(2t+4\left(\sqrt{(a-t)^2+a^2}-r\right)_+\right).
\]
Put \(d(t)=\sqrt{(a-t)^2+a^2}\), which strictly decreases on \([0,a]\). Where \(d(t)>r\), the derivative of the minimized expression is \(2-4(a-t)/d(t)\), strictly increasing in \(t\). Its unique zero is
\[
t_*=a(1-1/\sqrt3),\qquad d(t_*)=2a/\sqrt3.
\]
For \(0\leq r\leq d(t_*)\), the unconstrained convex minimum occurs at \(t=t_*\), giving
\[L_{\mathrm{side}}(r)=2a(1+\sqrt3)-4r.\]
For \(d(t_*)\leq r\leq\sqrt2 a\), the minimum occurs instead at the first \(t\) with \(d(t)\leq r\), namely
\[
t_r=a-\sqrt{r^2-a^2}\in[0,t_*].
\]
On the left of \(t_r\) the expression is decreasing, while on the right it equals \(2t\) and increases. Consequently
\[L_{\mathrm{side}}(r)=2t_r=2a-2\sqrt{r^2-a^2}.\]
If \(r\geq\sqrt2 a\), the singleton at the origin is feasible and the length is zero. The adjacent pairing along the horizontal direction is congruent to the other adjacent pairing.

**3. Opposite-corner pairing cannot do better.** For the third partition, each pair consists of two opposite square corners. The objective is invariant under simultaneous central inversion \((u,v)\mapsto(-u,-v)\), which exchanges the two sites *within* each pair. By convexity, averaging gives an optimal choice \(u=v=0\). The third-pairing minimum is therefore
\[
L_{\mathrm{opposite}}(r)=4(\sqrt2 a-r)_+.
\]
For \(0\leq r\leq2a/\sqrt3\), this exceeds the side-pairing value because \(2\sqrt2>1+\sqrt3\). For \(2a/\sqrt3<r<\sqrt2a\), define the difference
\[
h(r)=4(\sqrt2 a-r)-2a+2\sqrt{r^2-a^2}.
\]
Here \(h(\sqrt2a)=0\) and \(h'(r)=-4+2r/\sqrt{r^2-a^2}<0\), because \(r>2a/\sqrt3\). Hence \(h(r)>0\) throughout the open interval. At and beyond \(\sqrt2a\), both branches vanish. Thus an adjacent pairing globally minimizes for every radius, and its formula is exactly \(L_a(r)\).

**4. Realization and threshold.** For \(r<r_c\), take junctions \(u=(-t_*,0)\), \(v=(t_*,0)\), join them by a horizontal bridge, and join each junction to the nearest point of each assigned vertex disk. Each of four leaf edges has positive length \(r_c-r\) and the bridge has length \(2t_*\). At \(r=r_c\), each leaf edge collapses to zero. For \(r_c<r<\sqrt2a\), the bridge segment \([(-t_r,0),(t_r,0)]\) alone is feasible: each of its endpoints is at distance exactly \(r\) from its two adjacent vertices. Finally, for \(r\geq\sqrt2a\), take \(\Sigma=\{0\}\). This completes the exact proof, including attainment and all boundary radii.

## Verification

The analytic reduction exhausts all three four-terminal Steiner topologies and their possible degenerations; no finite enumeration is substituted for that completeness argument. The standalone script `verify.py` minimizes independently, for every topology, the original four-variable disk-distance objective with a generic numerical optimizer. It passed 36 test configurations (three square sizes times twelve radius ratios) and checked exact branch agreement and first-derivative agreement at the critical radius. These finite diagnostics are not an infinite or formal proof.

## Relationship to prior work

Teplitskaya's 2025 review formulates maximal-distance minimizers and explicitly discusses four-point Steiner trees, including the fact that a full Steiner tree on square corners can fail to be an inverse minimizer for *any* four-point input (a different question). The 2026 length-optimization problem collection asks for explicit compact-set minimizers. Basok, Cherkashin and Teplitskaya (2022/2023) study that inverse question and prove structural results. The classical Euclidean Steiner theorem supplies the four-terminal topology reduction. Here the new statement is the **full, all-radius exact length profile for the fixed four-square-corner input**, including the nontrivial critical radius and two realizing constructions; it is not inferred from the inverse nonrealizability statement or from the known zero-radius square Steiner length. Published-result and primary-literature comparisons found no identified equation implying this complete profile, but historical priority is provisional.

## Limitations

The four prescribed sites are precisely the corners of a square; this does not solve the harder problem for the entire boundary or filled square, for rectangles of arbitrary aspect ratio, for five or more sites, or the inverse problem. At transition radii other optimal geometric realizations are not classified. The mathematical formula is exact; its historical originality is subject to undiscovered work under 'Steiner tree with neighborhoods', 'four-terminal disk networks', or related terminology. Independent review has not been performed.

## References

- Y. Teplitskaya, *Open problems on Steiner trees and maximal distance minimizers*, arXiv:2511.18217v1 (2025), Sections 1.1, 2, 2.4, https://arxiv.org/html/2511.18217.
- M. Basok, D. Cherkashin, Y. Teplitskaya, *Inverse maximal and average distance minimizer problems*, arXiv:2212.01903v2 (2023), Sections 1, 2, especially Corollary 2.16; https://cvgmt.sns.it/paper/5904/.
- Y. Teplitskaya and contributors, *Open problems from the Length Optimization event at MDS 2026*, arXiv:2611.03403v1 (2026), Section 3, https://arxiv.org/html/2611.03403v1.
- E. N. Gilbert and H. O. Pollak, *Steiner minimal trees*, SIAM Journal on Applied Mathematics 16 (1968), 1–29 (classical four-terminal Steiner topology theory).
