# Global two-cycle rigidity and sharp trapping threshold for cross-polytope farthest-vertex contractions

## Finding

**Theorem.** Let \(d\ge3\), let \(P_d=\{x\in\mathbb R^d:\sum_{i=1}^{d}|x_i|\le1\}\), and let \(0<\lambda\le1/2\). Given \(x\in P_d\), choose a Euclidean farthest vertex \(v(x)\) among \(\{\pm e_1,\ldots,\pm e_d\}\), resolving any ties by a fixed deterministic convention, and set \(F_\lambda(x)=\lambda x+(1-\lambda)v(x)\). Then \(F_\lambda\) has **exactly \(d\) prime-period-two orbits, no fixed points and no other periodic orbits**. These orbits are
\[
\mathcal O_j=\left\{\pm\frac{1-\lambda}{1+\lambda}e_j\right\},\qquad 1\le j\le d.
\]
For every \(x\in P_d\), its orbit converges geometrically to one of these two-cycles (with the appropriate parity of the iterate). At most two preliminary iterations are needed before the winning coordinate index remains constant forever and its sign alternates. Each two-cycle has a basin of normalized \(d\)-dimensional Lebesgue measure exactly \(1/d\).

The restriction \(\lambda\le1/2\) is **sharp for the immediate coordinate-trapping property**: for every \(1/2<\lambda<1\) there are interior points with a unique farthest vertex whose winning coordinate index changes at the next iteration. This last statement does **not** classify the attractors for \(\lambda>1/2\).

## Assumptions and scope

Distances are Euclidean; \(e_j\) are standard orthonormal coordinate vectors; the polytope is the closed unit \(\ell_1\)-ball with regular cross-polytope vertices. Farthest means maximizing ordinary Euclidean distance, not minimizing it. A fixed deterministic vertex-label convention resolves ties, including the origin; all conclusions are independent of the particular convention. The map is in general discontinuous on tie hypersurfaces. A basin means the initial points whose forward orbits converge to the given two-cycle; the \(d\)-dimensional volume statement is normalized by \(\operatorname{Vol}(P_d)\). No statement of global attraction for larger \(\lambda\) is made.

## Proof

Put \(c=1-\lambda\), so \(c\ge\lambda\). For a vertex \(v=\sigma e_j\),
\[
\|x-v\|_2^2=\|x\|_2^2+1-2\sigma x_j.
\]
Hence every farthest vertex is \(-\operatorname{sgn}(x_j)e_j\) for an index \(j\) at which \(|x_j|\) is maximal; if \(x_j=0\), either sign is allowed. Once any nonzero winning coordinate is chosen, let \(m=|x_j|>0\). Since \(\lambda m\le\lambda\le c\), the updated winning coordinate changes sign and has absolute value \(c-\lambda m\), while every other coordinate \(i\ne j\) has absolute value \(\lambda|x_i|\).

**Interior trapping.** If \(x\in\operatorname{int}(P_d)\) and \(m>0\), then, for every \(i\ne j\),
\[
|F_\lambda(x)_j|-|F_\lambda(x)_i|
=c-\lambda(|x_j|+|x_i|)
\ge c-\lambda\|x\|_1>c-\lambda\ge0.
\]
Thus after one step index \(j\) is the *unique* largest-magnitude coordinate. Reapplication shows it is forever selected and its sign alternates. This also resolves all positive-coordinate ties after a single step.

**Entry into the interior.** For \(S=\|x\|_1\), if the chosen maximum is \(m>0\), the update gives
\[
\|F_\lambda(x)\|_1=\lambda S+c-2\lambda m<\lambda+c=1,
\]
because \(S\le1\) and \(m>0\). At \(x=0\), \(\|F_\lambda(0)\|_1=c<1\). Therefore every orbit enters the interior after one step, and after at most one further step has a unique permanently winning coordinate. All tie conventions work.

**Convergence and exhaustive periods.** On the trapped coordinate \(j\), write \(u_n=|x_{n,j}|\). It obeys
\[
u_{n+1}=c-\lambda u_n,\qquad
u_n-\frac{c}{1+\lambda}=(-\lambda)^n\left(u_0-\frac{c}{1+\lambda}\right)
\]
(with \(n=0\) indexing the trapped phase). For \(i\ne j\), \(|x_{n,i}|=\lambda^n|x_{0,i}|\). Hence in each parity class the orbit converges to one of the two points \(\pm[c/(1+\lambda)]e_j\), with an \(O(\lambda^n)\) error. Direct substitution shows that the two points swap under \(F_\lambda\), because the farthest vertex is the opposite coordinate vertex. Every periodic orbit must coincide with its own parity limits; thus these are all periodic orbits, and all have prime period two. In particular there is no fixed point.

**Basin volume.** Off the measure-zero union of ties \(|x_i|=|x_j|\), the basin index is simply the uniquely largest absolute-coordinate index of the starting point: the interior-trapping argument applies to every nonboundary point. Signed coordinate permutations preserve \(P_d\) and Lebesgue volume and act transitively on these \(d\) regions. Their union is full measure, so each has normalized volume \(1/d\). Boundary points and ties can be assigned arbitrarily by the tie convention without changing volume.

**Sharpness of the trapping endpoint.** Fix \(\lambda\in(1/2,1)\), and examine points \(x\) close to \((1/2,1/2,0,\ldots,0)\) from inside \(P_d\), with \(x_1>x_2>0\). The first farthest vertex is \(-e_1\). At the limit point, the two relevant updated coordinate magnitudes are \(|(3\lambda/2)-1|\) and \(\lambda/2\). For every \(1/2<\lambda<1\),
\[
\left|\frac{3\lambda}{2}-1\right|<\frac\lambda2,
\]
(the left inequality follows from \(\lambda>1/2\), the right from \(\lambda<1\)). By continuity, the second coordinate uniquely dominates the first after one update at sufficiently close interior points. Thus the winner switches, proving the cutoff is optimal for the stated immediate-trapping mechanism.

## Verification

The included `verify.py` uses exact rational arithmetic to test the farthest-vertex rule, trapping, the two-cycle formulas, and exact basin representative behavior in several dimensions and contraction parameters including \(\lambda=1/2\). It also explicitly constructs and verifies sharpness witnesses above the cutoff. These finite tests corroborate the identities but do not prove the all-dimensional theorem; the argument above is independent of the checker.

## Relationship to prior work

Abdulaziz's *The Chaos Game Versus Uniform Rotation: From Sierpinski Gaskets to Periodic Orbits* (first public 2024-06-17, arXiv:2407.02506, §5) studies the farthest-vertex contraction game for planar regular polygons, including the even-vertex case with attracting period-two orbits. The planar four-vertex cross-polytope case is thus **not** claimed as new; \(d\ge3\) is essential to the asserted new scope. The present classification treats the higher-dimensional regular cross-polytope for every \(0<\lambda\le1/2\), including global trapping and exact basin volume, and proves a sharp threshold for the trapping property.

The regular-simplex farthest-vertex problem is geometrically distinct: a regular \(d\)-simplex has \(d+1\) vertices and may have longer cyclic vertex itineraries, whereas the regular cross-polytope has \(2d\) antipodal vertices, permitting eventual alternation between one pair. A farthest-*orthogonal-projection* problem also defines a different map. Searches of relevant indexed findings and literature did not identify coverage of the exact higher-dimensional cross-polytope claim; absence from searches is not a proof of publication priority.

## Limitations

No classification of dynamics for \(\lambda>1/2\) is given. The cutoff concerns one-step winning-coordinate trapping, not necessarily existence or global attraction of two-cycles outside the stated range. Tie hypersurfaces can have convention-dependent basin allocation, but have zero volume. The basin claim concerns Lebesgue volume, not arbitrary initial distributions. The literature inspection covers the full motivating preprint and scoped index/phrase searches, not every historical paper; unindexed equivalent arguments remain possible. Independent mathematical validation has not been performed.

## References

1. Abdulrahman Abdulaziz, *The Chaos Game Versus Uniform Rotation: From Sierpinski Gaskets to Periodic Orbits*, arXiv:2407.02506v1 (first public 2024-06-17), especially the planar even-polygon farthest-vertex discussion in §5. https://arxiv.org/abs/2407.02506
