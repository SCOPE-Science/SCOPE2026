# Exact Gaussian normal-cone angles and pair-sensitive collisions of sparse-paving matroid base polytopes

## Finding
Let \(n\ge6\), \(3\le r\le n-3\), \(s=n-r\), \(N=\binom nr\) and \(k=rs\). Let \(\mathcal H\) be a nonempty family of \(r\)-subsets of \([n]\) such that different members meet in at most \(r-2\) elements. Its complement \(\mathcal B=\binom{[n]}r\setminus\mathcal H\) is the basis family of a sparse-paving matroid. Set
\[
P=\operatorname{conv}\{\mathbf1_B:B\in\mathcal B\}\subset\mathbb R^n,
\qquad d(B)=\#\{H\in\mathcal H:|H\cap B|=r-1\}.
\]
For a permitted basis \(B\), let \(\omega(B)\) be the normalized spherical solid angle of its outward vertex normal cone, computed in the intrinsic linear span of \(P\). Then **the complete pointwise angle law** is
\[
\boxed{\omega(B)=\frac1N\left(1+\frac{d(B)}{k}\right).}
\]
Write \(\lambda=|\mathcal H|\) and let \(\mu\) count unordered pairs of different members of \(\mathcal H\) meeting in exactly \(r-2\) elements. Two independent isotropic Gaussian linear objectives expose the same vertex with probability
\[
\boxed{\mathcal C(P)=\sum_{B\in\mathcal B}\omega(B)^2
=\frac{N+\lambda(1+1/k)+8\mu/k^2}{N^2}.}
\]
In particular this Euclidean angular collision statistic recovers the circuit-hyperplane pair count \(\mu\) from \(n,r,\lambda\). Every angle satisfies the sharp uniform bounds
\[
\frac1N\le\omega(B)\le\frac1N\left(1+\frac1{\max(r,s)}\right).
\]
For fixed \(n,r,\lambda\), the collision lower bound obtained by setting \(\mu=0\) holds with equality exactly for families whose distinct forbidden bases are at Johnson distance at least three (whenever such a family exists).

## Assumptions and scope
The Euclidean geometry is the inherited standard coordinate metric, not a lattice-normalized metric. The affine hull lies in \(\{x:\sum_i x_i=r\}\). The intrinsic spherical angle is the probability that the orthogonal projection of an ambient standard Gaussian to the polytope's linear span belongs to the corresponding normal cone; this agrees with the ambient Gaussian objective's probability of exposing that vertex. Exclude ranks two and coranks two, which admit separate earlier angular results. All Gaussian objectives are independent, centered, and isotropic in the relevant span. Boundary ties have probability zero.

The stated intersection restriction makes \(\mathcal H\) an independent set of the Johnson graph \(J(n,r)\). The complement is a matroid basis family: given permitted bases \(B,C\) and \(i\in B\setminus C\), when \(|C\setminus B|=1\) the only exchange leads to \(C\); otherwise two distinct exchanges with the same removed \(i\) are adjacent in the Johnson graph and cannot both be forbidden, so at least one is permitted.

## Proof
**Step 1: Select the unrestricted optimum.** Let \(G_1,\ldots,G_n\) be independent standard Gaussians. Their descending coordinate order is uniformly distributed over all \(n!\) permutations. The unique maximum of \(\sum_{i\in B}G_i\) over all \(r\)-subsets is the top-\(r\) subset \(T\), uniform among \(N\) subsets.

**Step 2: Describe the allowed optimum if the top basis is forbidden.** If \(T\notin\mathcal H\), it wins among allowed bases. If \(T\in\mathcal H\), every alternative \(r\)-subset discards at least one of the \(r\) coordinates of \(T\) and adds at least one outside coordinate. The smallest possible loss of objective value is obtained uniquely by discarding the smallest Gaussian in \(T\) and inserting the largest Gaussian outside \(T\). Call this adjacent subset \(T'\). Because two forbidden subsets are never adjacent, \(T'\notin\mathcal H\); therefore it wins among allowed bases. Conditional on \(T\), its least-weight coordinate is uniform over \(r\) possibilities, and the maximum outside coordinate is independent and uniform over \(s\) possibilities. Hence any fixed Johnson neighbor of \(T\) is selected with conditional probability \(1/(rs)=1/k\).

**Step 3: Convert selection to intrinsic angles.** The event that a permitted \(B\) wins consists of its own top-\(r\) event (probability \(1/N\)), plus disjoint top-\(r\) events for the \(d(B)\) forbidden neighbors (each contributes \(1/(Nk)\)). Since projecting an ambient isotropic Gaussian onto the affine-direction span of \(P\) preserves the comparison of vertex objective values and yields an intrinsic isotropic Gaussian, these winning probabilities are exactly the intrinsic normal-cone solid angles. This proves the first boxed formula without a dimension-dependent approximation.

**Step 4: Count angular collisions.** Each forbidden \(H\) has \(k=rs\) adjacent permitted bases. Thus \(\sum_{B\in\mathcal B}d(B)=\lambda k\). Moreover, two forbidden sets at Johnson distance two have precisely four common Johnson neighbors, obtained by the four choices of which removed/added element to swap. Sets at distance at least three have no common neighbor by the triangle inequality. Consequently
\[
\sum_{B\in\mathcal B}d(B)^2=\lambda k+8\mu.
\]
Expanding the squared pointwise formula gives
\[
\begin{aligned}
N^2\mathcal C(P)
&=\sum_{B\in\mathcal B}\left(1+\frac{d(B)}k\right)^2\\
&=(N-\lambda)+\frac{2\lambda k}k
+\frac{\lambda k+8\mu}{k^2}\\
&=N+\lambda\left(1+\frac1k\right)+\frac{8\mu}{k^2}.
\end{aligned}
\]
As the coefficient of \(\mu\) is strictly positive, the claimed equality characterization follows.

**Step 5: Sharp angle bounds.** The \(k\) Johnson neighbors of \(B\) correspond to cells of an \(r\times s\) grid: remove one element of \(B\) and add one from its complement. Two neighbors sharing a row or column are adjacent, so forbidden neighbors occupy the cells of a partial matching. Thus \(0\le d(B)\le\min(r,s)\), yielding the bounds. The lower value occurs for a forbidden \(r\)-subset differing from \(B\) in two positions; the upper occurs by taking a family of \(\min(r,s)\) forbidden neighbors along a complete grid matching. Both constructions respect the required pairwise-intersection restriction in every admissible \(n,r\).

**Explicit separation.** At \(n=6,r=3\), take two forbidden triples. If they are \(\{1,2,3\}\) and \(\{4,5,6\}\), then \(\lambda=2,\mu=0\), all 18 surviving vertices have angle \(1/18\), and \(\mathcal C(P)=1/18\). If they are \(\{1,2,3\}\) and \(\{1,4,5\}\), then \(\lambda=2,\mu=1\); four vertices have angle \(1/20\), ten have \(1/18\), four have \(11/180\), and \(\mathcal C(P)=113/2025\). This gives two polytopes of equal dimension, rank and number of vertices but different Euclidean angle distributions.

## Verification
The accompanying standalone `check_angles.py` enumerates all possible strict coordinate orders for seven explicitly specified admissible families with \(n=6,7,8\) and admissible ranks. For every order, it brute-forces the maximum permitted objective among all allowed bases using distinct superincreasing binary weights; it does **not** use the second-best-swap formula for the optimization. It compares the resulting exact rational winning frequencies, angle spectra, and squared-frequency collision probability to both boxed expressions. All cases pass, including the two six-coordinate witness polytopes. These finite enumerations test the derivation; the unrestricted theorem follows from Steps 1–5 rather than from enumeration.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin (first public 2022-01-28, arXiv:2201.12442) study Ehrhart polynomials and the geometric construction of paving-matroid base polytopes from hypersimplices. Ferroni and Schröter (first public 2023-10-09, arXiv:2310.05487, Corollary 2.10) show that the face vector of a connected sparse-paving matroid polytope depends on \(\lambda\) and \(\mu\); that combinatorial statement is not claimed as new. The present claim computes the independent Euclidean Gaussian normal-cone weights and their two-direction collision statistic, not face numbers or lattice-normalized areas. General definitions of conic Gaussian solid angles are classical. Exact rank-two matroid normal-cone spectra are treated elsewhere; the theorem intentionally addresses ranks and coranks at least three.

## Limitations
This is not a classification of all spherical normal-fan incidence types: it determines each cone's normalized solid angle, its sharp range and the global two-direction collision probability. The formula requires the forbidden sets to be Johnson-independent; arbitrary collections of deleted hypersimplex vertices can have overlapping forbidden neighbors and invalidate the second-best argument. Publication-priority conclusions are provisional because relevant equivalent unpublished or unindexed treatments cannot be ruled out by searches alone. No computational test replaces the all-dimensional proof.

## References
- D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28, https://arxiv.org/abs/2201.12442.
- L. Ferroni and B. Schröter, *Face Enumeration for Split Matroid Polytopes*, arXiv:2310.05487, first posted 2023-10-09, https://arxiv.org/abs/2310.05487; see Section 2.5, Corollary 2.10.
- D. Amelunxen and M. Lotz, *Intrinsic Volumes of Polyhedral Cones: A Combinatorial Perspective*, Discrete & Computational Geometry (2017), https://doi.org/10.1007/s00454-017-9904-9, for Gaussian cone-angle terminology.
