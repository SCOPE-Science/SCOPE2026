# Exact comparable-pair law and a half-mixed-stratum identity for a complete positive-root signed order polytope

## Finding
For every integer \(n\ge2\), let \(P_n=\{e_i+e_j:1\le i<j\le n\}\) be the complete positive-pair type-\(B_n\) signed poset, and let its signed order polytope, in the standard Euclidean coordinates, be
\[
Q_n=\{x\in[-1,1]^n:x_i+x_j\ge0\text{ for every }i<j\}.
\]
Let \(X,Y\) be independent and uniformly distributed by ordinary \(n\)-dimensional Lebesgue volume on \(Q_n\). Write \(C\) for the event that \(X\le Y\) or \(Y\le X\) coordinatewise, and let \(N\) be the total number of strictly negative coordinates among both points. Then
\[
\boxed{\operatorname{Vol}_n(Q_n)=2,\qquad
\Pr(X\le Y)=\frac{n}{2^n(2n-1)},\qquad
\Pr(C)=\frac{n}{2^{n-1}(2n-1)}.}
\]
Moreover, conditional on comparability, the number of negative coordinates in the two points satisfies the exact, three-atom law
\[
\boxed{\Pr(N=0\mid C)=\frac{2n-1}{4n},\quad
\Pr(N=1\mid C)=\frac12,\quad
\Pr(N=2\mid C)=\frac1{4n}.}
\]
Thus, **exactly half of comparable pairs cross from a one-negative-coordinate cap to the nonnegative cube, in every dimension**. In particular, the ordinary-order-polytope lower bound \(\Pr(C)\ge 2^{1-n}\) does not extend to signed order polytopes: here the ratio to that cube probability is \(n/(2n-1)<1\), converging to \(1/2\).

## Assumptions and scope
The underlying vector order is the usual product order, and is **not** the signed-poset order on roots. Coordinates are labeled, and neither point is sampled uniformly from vertices. All boundaries have Lebesgue probability zero. The root set \(P_n\) is a signed poset in Reiner's sense: its roots are nonnegative two-support vectors, no opposite root is present, and no positive combination of distinct such roots can be a different type-\(B\) root (nonnegativity and two-support restrictions preclude it). Beck and Hlavacek's definition of signed order polytope therefore yields exactly \(Q_n\), which is full-dimensional for \(n\ge2\).

The numerical probability bound is explicitly a statement about this full-dimensional family. It does not assert an extremal inequality across all signed posets, nor does it claim the ambient coordinatewise order is invariant under arbitrary signed-permutation transformations of the defining root system.

## Proof
**1. Full-volume sign partition.** At most one coordinate of a point in \(Q_n\) can be strictly negative, because two negative coordinates would violate their pair inequality. Apart from null boundaries, \(Q_n\) is the disjoint union of the positive unit cube \(B=[0,1]^n\) and the \(n\) sets
\[
A_i=\{x:x_i=-t,\ 0<t<1,\ t\le x_j\le1\text{ for }j\ne i\}.
\]
Each cap has volume \(\int_0^1(1-t)^{n-1}\,dt=1/n\), so \(\operatorname{Vol}_n(Q_n)=1+n(1/n)=2\). Under normalized uniform volume, each of the two sign classes (cube or some cap) has probability \(1/2\); conditional on being in a cap, its index is uniform, its depth has density \(f_n(t)=n(1-t)^{n-1}\), and its other coordinates are independent \(\operatorname{Unif}[t,1]\) conditional on depth.

**2. Two cube points.** Conditional on \(X,Y\in B\), coordinates are independent uniforms, so \(\Pr(C\mid B,B)=2^{1-n}\) (the two orientations intersect in a probability-zero event). Multiplying by the type probability \(1/4\) gives
\[
p_0:=\Pr(C,N=0)=2^{-n-1}.
\]

**3. A cap and a cube.** Conditional on one point being in \(A_i\) and the other in \(B\), the cap point must be the coordinatewise *smaller* point: the reverse orientation is impossible at index \(i\). Conditional on its negative depth \(t\), the probability of the necessary comparisons at all other coordinates is \(((1-t)/2)^{n-1}\), since an independent uniform on \([t,1]\) is less than a uniform on \([0,1]\) with probability \((1-t)/2\). Thus
\[
\Pr(C\mid\text{exactly one cap})
=\frac{n}{2^{n-1}}\int_0^1(1-t)^{2n-2}\,dt
=\frac{n}{2^{n-1}(2n-1)}.
\]
The mixed-type probability is \(1/2\), hence
\[
p_1:=\Pr(C,N=1)=\frac{n}{2^n(2n-1)}.
\]

**4. Two caps.** Points in different caps are incomparable because their negative coordinates occupy different indices. The probability of two independent cap points sharing the same index is \(1/(4n)\), including their type probabilities. Given that common index, choose depths \(t,u\), each independently with density \(f_n\). In the orientation \(X\le Y\), necessarily \(t\ge u\); conditional on this, for every other coordinate
\[
\Pr(X_j\le Y_j\mid t,u)=\frac{1-t}{2(1-u)}.
\]
Integrating over the triangle \(0\le u\le t\le1\), and doubling for the reverse orientation, gives
\[
\begin{aligned}
\Pr(C\mid\text{both in the same cap})
&=\frac{2n^2}{2^{n-1}}
\int_0^1\int_0^t(1-t)^{2n-2}\,du\,dt\\
&=\frac{2n^2}{2^{n-1}}\int_0^1 t(1-t)^{2n-2}\,dt\\
&=\frac{n}{2^{n-1}(2n-1)}.
\end{aligned}
\]
(The final beta integral is \(1/[2n(2n-1)]\).) Accounting for the probability \(1/(4n)\) of a matching cap index yields
\[
p_2:=\Pr(C,N=2)=\frac{1}{2^{n+1}(2n-1)}.
\]

**5. Normalization and comparison.** Add the three disjoint contributions:
\[
\Pr(C)=p_0+p_1+p_2
=\frac{(2n-1)+2n+1}{2^{n+1}(2n-1)}
=\frac{n}{2^{n-1}(2n-1)}.
\]
Coordinatewise exchangeability of \(X,Y\) implies the one-way probability is half the two-way value. Dividing \(p_0,p_1,p_2\) by \(\Pr(C)\) gives the three conditional probabilities. Finally, comparison with the cube probability \(2^{1-n}\) gives the sharp ratio \(n/(2n-1)\), strictly below one for \(n\ge2\).

## Verification
The standalone `checker.py` uses exact rational beta integrals to test the independent sign-stratum expressions and the final formula for every integer dimension \(2\le n\le80\). A second check independently samples pairs by rejecting points from the *ambient* cube \([-1,1]^n\) unless all signed-root inequalities hold, instead of using the proof's mixture sampler. Across dimensions \(2,3,4,5,6\) it tests 240,000 independently sampled pairs against the derived probabilities and their sign composition. Execute with `python3 checker.py`; the observed marker is `SIGNED_POSITIVE_PAIR_COMPARABILITY_PASS exact_dimensions=79 ambient_rejection_pairs=240000`. The Monte Carlo component is only a diagnostic; the above exact integrals prove every dimension.

An exact uniform sampler, available directly from the proof, selects the positive cube with probability \(1/2\), otherwise a uniform cap index. For a cap draw, sample independent \(U,V_1,\ldots,V_{n-1}\sim\operatorname{Unif}[0,1]\), put \(T=1-U^{1/n}\), the selected coordinate equal to \(-T\), and all other coordinates equal to \(T+(1-T)V_j\).

## Relationship to prior work
Beck and Hlavacek introduce signed order polytopes, their defining root inequalities, and polyhedral and Ehrhart structure; the present positive-pair family is a direct specialization of their framework. Their inspected 2023 full text does not report a two-point product-order comparability law. Previously published *Sharp Catalan and cube bounds for comparable random points of order polytopes* proves \(2^{1-n}\) as a sharp lower bound for **ordinary** order polytopes and provides the FKG/association explanation. That theorem does not apply here: for \(n\ge2\), the vectors with first two coordinates \((-1,1)\) and \((1,-1)\) (and all remaining coordinates \(1\)) belong to \(Q_n\), but their coordinatewise minimum does not. Therefore \(Q_n\) is not closed under coordinatewise minimum, and its uniform density does not satisfy the distributive-lattice hypothesis used in that earlier argument. The present exact formula quantifies a genuine signed-order boundary of that prior theorem.

Fried's simplex stochastic-dominance probability concerns a different product-order encoding and yields a classical chain benchmark. Jacobovic and Zuk treat covariance and Pareto maxima of cube samples, not the present signed-polytope distribution. The novelty asserted here is the exact *two-point* law and three-stratum conditional structure for this complete positive-pair signed-order family, not the existing definition, the cube benchmark, or the general beta integral.

## Limitations
The result is an exact statement for this specified positive-pair family, with all dimensions \(n\ge2\); it does not classify all signed posets and does not prove an optimal lower bound among them. Historical priority is provisional: an unindexed equivalent calculation under another name for this orthant-truncated cube could exist. The mathematical proof is elementary but the probability mix is nontrivial; finite simulations do not imply the infinite-dimensional theorem. No independent mathematical audit has been performed.

## References
1. Matthias Beck and Max Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, first public November 8, 2023, Definitions 1.5–1.6. https://arxiv.org/html/2311.04409v1
2. *Sharp Catalan and cube bounds for comparable random points of order polytopes*, published October 25, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-sharp-catalan-and-cube-bounds-for-comparable-random-points-of-or--de03dacfde51/RESULT.md
3. Sela Fried, *The probability that two random points on the n-probability simplex are comparable with respect to the first order stochastic dominance and the monotone likelihood ratio partial orders*, arXiv:1910.01752v1, first public October 3, 2019. https://arxiv.org/html/1910.01752v3
4. Royi Jacobovic and Or Zuk, *A correlation inequality for random points in a hypercube with some implications*, arXiv:2209.00346v1, first public September 1, 2022. https://arxiv.org/html/2209.00346v1
