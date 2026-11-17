# A parity-sharp farthest-facet law and a Watson limit for cycle symmetric-edge polytopes

## Finding

**Theorem.** For each integer \(n\ge3\), let \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\) with its standard Euclidean metric, and let the symmetric edge polytope of the labeled cycle be
\[
P_n=\operatorname{conv}\{\pm(e_i-e_{i+1}):i\in\mathbb Z/n\mathbb Z\}\subset H_n.
\]
For each facet \(F\) let \(u_F\in H_n\) be the unique normal for which its supporting hyperplane is \(\langle u_F,x\rangle=1\). Define its supporting-plane distance from the origin as \(d_F=1/\|u_F\|_2\).

1. **Exact farthest supporting planes.** The maximum distance among all facet supporting planes is
\[
\max_F d_F=\begin{cases}2/\sqrt n,& n\ \text{even},\\ 2\sqrt{n/(n^2-1)},&n\ \text{odd}.\end{cases}
\]
Exactly two facets attain it when \(n\) is even, and exactly \(2n\) when \(n\) is odd. Their centered integer-valued normals have precisely two adjacent potential levels (with the corresponding balanced or nearly balanced class sizes).

2. **Non-Gaussian uniform-facet limit.** For a facet \(F_n\) sampled uniformly from all facets, put \(X_n=\|u_{F_n}\|_2^2\). If \(B\) is a standard Brownian bridge on \([0,1]\), then
\[
\frac{X_n}{n^2}\ \xrightarrow{\mathrm d}\ Q:=\int_0^1\left(B(t)-\int_0^1B(s)\,ds\right)^2dt,
\quad \frac{n}{\|u_{F_n}\|_2}\xrightarrow{\mathrm d} Q^{-1/2}.
\]
The limiting law is nondegenerate, strictly positive, and has Laplace transform
\[
\mathbb E e^{-sQ}=\frac{\sqrt{s/2}}{\sinh(\sqrt{s/2})}\quad(s\ge0),
\qquad \mathbb E Q=\frac1{12},\quad\operatorname{Var}(Q)=\frac1{360}.
\]

3. **Three metric scales, combining this result with known extreme shells.** The minimum facet-plane distance satisfies
\[
4n^{-3/2}\le\min_F d_F\le\sqrt{48}\,n^{-3/2}.
\]
Thus the nearest supporting planes are of order \(n^{-3/2}\), a uniformly sampled facet-plane distance is of order \(n^{-1}\) in distribution, and the farthest supporting planes are of order \(n^{-1/2}\). The first moments of squared normals, already encompassed by the published general cactus covariance formula, are
\[
\mathbb EX_n=\begin{cases}n(n+1)/12,&n\ \text{even},\\(n^2-1)/12,&n\ \text{odd}.\end{cases}
\]
The last displayed moments are contextual prior coverage, **not** asserted as new. Likewise, earlier sharp outer radial shells of the polar cycle Lipschitz polytope determine the nearest-plane distance more precisely than the bounds in part 3; those bounds and their witness construction are presented only as a self-contained comparison, not a new closest-plane theorem.

## Assumptions and scope

The cycle is simple and unweighted, with \(n\ge3\). All geometry is intrinsic to the zero-sum hyperplane with the Euclidean metric inherited from \(\mathbb R^n\). Each facet is given equal probability, not weight proportional to facet area or spherical normal-cone measure. Supporting normals use the fixed normalization \(\langle u_F,x\rangle=1\), not unit-length normalization. A *farthest facet supporting plane* maximizes its distance from the origin; it need not be a nearest facet determining an inscribed ball. This is not a statement about arbitrary cactus graphs, weighted cycles, or Hausdorff distances.

## Proof

**1. Exact facet parametrization.** A normal \(u\in H_n\) supports \(P_n\) at height one exactly when \(|u_i-u_{i+1}|\le1\) for all cyclic edges. The corresponding contact face has dimension \(n-2\) precisely when the saturated edges span a connected graph: the saturated edge-root vectors then have rank \(n-1\). On a cycle this requires at least \(n-1\) saturated edges. Set \(d_i=u_i-u_{i+1}\); then \(\sum_i d_i=0\). For even \(n\), if there were exactly one nonsaturated edge, its difference would be an integer of odd parity by summing the other \(n-1\) unit signed gradients; it cannot have absolute value less than one. Thus every gradient is \(\pm1\), with exactly half positive. For odd \(n\), the all-tight option has an impossible odd signed sum; precisely one gradient is zero and the remaining \(n-1\) are balanced signs. Conversely each such word gives a connected tight subgraph and a unique centered potential, hence one facet. In particular their counts are \(\binom n{n/2}\) and \(n\binom{n-1}{(n-1)/2}\), respectively. This is the established cycle-facet characterization [1–3].

**2. Sharp maximum plane distance.** Choose a spanning path through all \(n\) vertices: remove the unique zero-gradient edge in the odd case and any edge in the even case. Along this path each increment is odd (\(\pm1\)), so all values of \(u\) on alternating path positions have one integer parity, and the other positions the opposite parity, after translating by a constant. Their class sizes are \(a=\lceil n/2\rceil\) and \(b=\lfloor n/2\rfloor\). For an arbitrary real proposed center \(\mu\), the sum of squared deviations of the integer potentials is at least
\[
\min_{r\in2\mathbb Z,\,s\in2\mathbb Z+1}\bigl(a(r-\mu)^2+b(s-\mu)^2\bigr).
\]
Minimizing also over \(\mu\) gives \(ab(r-s)^2/n\ge ab/n\). Equality requires constant levels within each parity class and adjacent integer levels, so \(\|u\|_2^2\ge ab/n\) with equality only for alternating two-level potentials. These satisfy the facet gradient condition. For even \(n\) there are exactly two such centered potentials. For odd \(n\) the sole zero gradient may be at any of the \(n\) edges, and there are two choices of overall sign, yielding exactly \(2n\). As \(d_F=1/\|u_F\|_2\), this proves part 1.

**3. Bridge limit.** A uniformly selected even-cycle facet has a gradient sequence that is a uniform permutation of \(n/2\) plus and \(n/2\) minus signs. Its partial sums divided by \(\sqrt n\) converge in the uniform functional topology (after piecewise-linear interpolation) to a standard Brownian bridge by the functional invariance principle for a simple random-walk bridge. In odd size the gradient word consists of a uniformly located zero inserted into an independently uniform balanced sign sequence of length \(n-1\); removing/inserting it changes the interpolated partial-sum path by at most a one-step spatial displacement and a time shift of \(1/n\), so the same limit holds. If \(S_i\) denotes the partial sum of the first \(i\) oriented gradients, then the centered facet potential is \(u_i=S_{i-1}-n^{-1}\sum_{j=0}^{n-1}S_j\) up to a global sign, irrelevant for squared norms. Therefore
\[
\frac{\|u\|_2^2}{n^2}=\frac1n\sum_{i=0}^{n-1}\left(\frac{S_i}{\sqrt n}-\frac1n\sum_{j=0}^{n-1}\frac{S_j}{\sqrt n}\right)^2
\]
converges by the continuous mapping theorem and uniform Riemann-sum approximation to \(Q\). The centered Gaussian bridge \(B(t)-\int_0^1B\) has the same distribution as a zero-mean periodic Gaussian process with independent sine/cosine Fourier coefficients of variance \(1/(4\pi^2k^2)\) for each \(k\ge1\). Consequently
\[
Q\stackrel{\mathrm d}=\sum_{k=1}^{\infty}\frac{Z_{k,1}^2+Z_{k,2}^2}{4\pi^2k^2},
\]
where the variables are independent standard normals. Euler's product for \(\sinh\) gives the claimed Laplace transform; summing the series for its first two moments yields \(1/12\) and \(1/360\). Since \(Q>0\) almost surely, taking reciprocal square roots is legitimate by the continuous mapping theorem.

**4. Nearest planes and scale separation.** Every admissible potential is 1-Lipschitz on the unweighted cycle, hence its coordinate range is at most \(\lfloor n/2\rfloor\). The elementary range-variance bound gives \(\|u\|_2^2\le n\operatorname{range}(u)^2/4\le n^3/16\), so every facet plane has distance at least \(4n^{-3/2}\). For even \(n\), the block-gradient word with \(n/2\) successive plus signs followed by \(n/2\) minus signs has squared centered norm \(n(n^2+8)/48\). For odd \(n\), the word with \((n-1)/2\) plus signs, one zero, then \((n-1)/2\) minus signs has squared centered norm \((n^2-1)(n^2+3)/(48n)\). Both are at least \(n^3/48\) in the stated range; thus at least one facet has plane distance at most \(\sqrt{48}\,n^{-3/2}\). Part 1 supplies the farthest scale and Step 3 supplies the intermediate random scale. These prove part 3.

**5. Previously covered first moments.** The uniform-facet covariance theorem [4], applied to the cycle with even-cycle conductance correction, gives the contextual expected squared-normal formulas. Independently, covariance of balanced signed increments and the identity \(\|u\|_2^2=n^{-1}\sum_{i<j}(u_i-u_j)^2\) reproduce those expressions. Their inclusion does not constitute an originality claim.

## Verification

The accompanying standard-library `verify.py` enumerates every allowed gradient word for sizes \(3\le n\le15\), constructs its unique centered normal over exact integers, and checks the facet counts, exact minimizing squared norm, exact equality multiplicities, and known first moments. For sizes \(3\le n\le9\) it independently enumerates the full alphabet of permitted increments and compares all covariance-matrix entries to the published cycle Green kernel using exact fractions. This computation is finite corroboration only; functional convergence and all-size extremal statements are analytical.

Run `python3 verify.py` from the directory containing this file and `verify.py`.

## Relationship to prior work

The cycle-facet parametrization and facet counts are established in [1–3] and are used rather than claimed anew. In particular, [2] covers even-cycle facets and [3] includes both parities. More importantly, [4] establishes the **full uniform-facet covariance for every cactus symmetric-edge polytope**; it therefore already implies the exact first moments shown above and dominates any separate second-moment claim for cycles. Previously established exact largest and second-largest radial shells of the **polar** cycle Lipschitz polytope also determine the nearest supporting-plane scale, and are not claimed as new. The new parts asserted here are the **smallest** radial shell of the polar, equivalently the sharp farthest-support-plane classification including multiplicities, and the full non-Gaussian Watson limit of randomly selected facet-plane distances. The three-scale picture contextualizes these new contributions against known closest-plane estimates. None of the inspected closely related primary statements supplies those parts. The Brownian-bridge invariance principle, Watson's quadratic functional, Euler product, and range-variance bound are standard tools, not claimed as novel.

## Limitations

The displayed proof only derives simple bounds for the *nearest* supporting-plane distance, which is already determined more precisely by previously established outer polar radial-shell formulas; no novelty is claimed for that bound. It does not determine the entire finite-size distribution of facet distances. The limiting law is for uniformly selected facets; uniform volume or Haar directions yield different measures. A semantic search and inspection of closely related primary results do not exclude all possible prior equivalent formulations; historical priority is provisional. No independent audit has been performed.

## References

[1] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first posted July 20, 2018, especially the facet-potential criterion.

[2] A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), cycle facets and their counts.

[3] B. Braun and K. Bruegge, *Facets of symmetric edge polytopes for graphs with few edges*, arXiv:2201.13303 (2022), Theorem 2.3 and its cycle specializations.

[4] *A facet-covariance Green kernel and exact determinant for cactus metric transportation balls* (2026), publicly recorded mathematical result: complete covariance of uniformly sampled canonically normalized cactus facet normals.

[5] G. S. Watson, *Goodness-of-fit tests on a circle*, Biometrika 48 (1961), 109–114, DOI:10.1093/biomet/48.1-2.109. The bridge invariance principle and Fourier expansion are used in their standard forms.
