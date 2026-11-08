# Farthest-vertex simplex contractions have factorially many attracting cycles

## Finding

Let \(d\ge3\), let \(N=d+1\), and let \(0<\lambda<1\). On a regular Euclidean \(d\)-simplex, define the **farthest-vertex contraction** by moving a fraction \(1-\lambda\) of the way from the current point toward its farthest vertex. Break equal-distance ties by the smallest vertex label. Then, for every contraction parameter \(\lambda\):

1. There are **exactly \(d!\) periodic orbits**, each having least period \(d+1\), with no other periodic orbits. All are locally hyperbolically attracting; the return derivative on the \(d\)-dimensional affine span is \(\lambda^{d+1}I\).
2. At every periodic point, the sorted barycentric coordinates are precisely
\[
 s_i=\frac{(1-\lambda)\lambda^{N-i}}{1-\lambda^N},\qquad i=1,\ldots,N.
\]
Each orbit cycles through the \(N\) vertices in a fixed cyclic order, and the \(d!\) orbits are indexed by cyclic orders of all vertex labels.
3. **Every** starting point, including one on a tie hyperplane, eventually has distinct coordinates and then visits each farthest vertex once per \(N\) iterations, in a fixed cyclic order. Each trajectory converges geometrically to a unique periodic orbit; from that time forward its distance from the matching periodic phase is multiplied by \(\lambda\) at every step.
4. Every periodic orbit has a physical basin of **exactly \(1/d!\)** of the normalized \(d\)-dimensional Lebesgue measure of the simplex.

An explicit, nonoptimal uniform bound on the onset of the cyclic itinerary is
\[
 \delta=\frac{(1-\lambda)^2\lambda^{N-2}}{1-\lambda^N},\qquad
 T=1+\left\lfloor\frac{\log(4/\delta)}{\log(1/\lambda)}\right\rfloor.
\]
Every orbit has the stated fixed cyclic itinerary from time \(T\) onward.

## Assumptions and scope

The simplex has vertices \(v_1,\ldots,v_N\) in Euclidean space, all pairwise at the same distance. The affine barycentric representation is \(x=\sum_{i=1}^N x_i v_i\), with \(x_i\ge0\) and \(\sum_i x_i=1\). Fix a smallest-label convention at ties and write \(m(x)\) for the corresponding farthest-vertex index. The map in barycentric coordinates is
\[
 F_\lambda(x)_i=\lambda x_i+(1-\lambda)\mathbf{1}_{\{i=m(x)\}}.
\]
The identity
\[
\|x-v_i\|_2^2=\|x\|_2^2+\|v_i\|_2^2-2\langle x,v_i\rangle
\]
shows that farthest Euclidean vertex means smallest barycentric coordinate: the common-norm regular-simplex vertices have \(\langle x,v_i\rangle\) affine and strictly increasing with \(x_i\). Equivalently, use the regular standard simplex with vertices \(e_i\) in \(\mathbb R^N\), where \(\|x-e_i\|_2^2=\|x\|_2^2+1-2x_i\). Results transport by Euclidean similarity.

The claimed periodic points are genuine periodic points of the discontinuous, tie-resolved deterministic map; no periodic orbit uses a tie. The exceptional tie trajectories are included in eventual convergence and omitted only in Lebesgue-almost-everywhere symmetry arguments.

## Proof

**1. Sorted contraction.** Let \(z=(z_1\le\cdots\le z_N)\) be the nondecreasing rearrangement of \(x\). The sorted image obeys the exact autonomous recurrence
\[
 \Phi(z)=\operatorname{sort}\bigl(\lambda z_1+1-\lambda,\lambda z_2,\ldots,\lambda z_N\bigr).
\]
It is independent of how a tied minimum was chosen. Sorting real vectors is nonexpansive in the \(\ell^\infty\) norm: if two input vectors are coordinatewise within \(\varepsilon\), their same-rank order statistics are within \(\varepsilon\). Thus \(\Phi\) is a \(\lambda\)-contraction on the compact set of sorted probability vectors. Its unique fixed point is the strictly increasing vector \(s\) given in the Finding. Indeed \(s_i=\lambda s_{i+1}\) for \(i<N\) and \(\lambda s_1+1-\lambda=s_N\). Therefore, for every \(t\ge0\),
\[
 \|\operatorname{sort}(F_\lambda^t(x))-s\|_\infty
 \le\lambda^t\|\operatorname{sort}(x)-s\|_\infty\le\lambda^t.
\]
This is a global bound despite discontinuities in the labelled dynamics.

**2. A finite uniform lock-in time.** Consecutive entries of \(s\) satisfy
\[
 s_{i+1}-s_i=\frac{(1-\lambda)^2\lambda^{N-i-1}}{1-\lambda^N}\ge\delta>0.
\]
The given integer \(T\) satisfies \(\lambda^T<\delta/4\); hence at each \(t\ge T\), every pair of consecutive sorted coordinates is separated by more than \(\delta/2\). Write \(\varepsilon=\lambda^t\). The newly updated minimal coordinate is at least \(\lambda(s_1-\varepsilon)+1-\lambda=s_N-\lambda\varepsilon\). Every other updated coordinate is at most \(\lambda(s_N+\varepsilon)\). The gap is at least
\[
 (1-\lambda)s_N-2\lambda\varepsilon
 =\frac{(1-\lambda)^2}{1-\lambda^N}-2\lambda\varepsilon
 \ge\delta-2\lambda\varepsilon>\delta/2>0.
\]
Thus at every step after \(T\), the uniquely minimal coordinate becomes uniquely maximal, while all other relative coordinate orders remain unchanged. The ascending label ranking rotates by one position at every iteration; its length is exactly \(N\), and every vertex is selected once per block of \(N\) steps.

**3. Exhaustive periodic point census.** A periodic sorted vector must be a periodic point of the strict contraction \(\Phi\). But for every \(p\ge1\), \(\Phi^p\) has the same unique fixed point \(s\); hence any periodic labelled point is a permutation of \(s\). Conversely, for each permutation of \(s\), the update removes the smallest entry, multiplies the other \(N-1\) entries by \(\lambda\), and inserts the updated smallest as the new largest. The result is another permutation of \(s\); after \(N\) steps the original labelled permutation returns. Since all entries of \(s\) are distinct, no positive smaller iterate fixes it. There are \(N!\) such periodic points, organized into \(N!/N=(N-1)!=d!\) cycles. At a periodic point every chosen branch has a strict margin, so the return derivative on the simplex affine span is \(\lambda^N I\), with eigenvalues strictly below one in modulus.

**4. Attraction of every starting point.** Let \(x_T\) be an arbitrary iterate, and choose the unique permutation \(y_T\) of \(s\) with exactly the same labelled rank ordering as \(x_T\). By step 2, both points thereafter follow identical periodic vertex-choice sequences. Therefore
\[
 F_\lambda^{T+k}(x)-F_\lambda^k(y_T)
 =\lambda^k(x_T-y_T),\qquad k\ge0.
\]
This proves convergence to that periodic orbit for every initial point, not only almost every one, and with exact geometric error decay on the matched phase.

**5. Equal basin volumes.** For fixed \(t\), any equality between two coordinates of \(F_\lambda^t(x)\) holds, on each finite itinerary cell, on an affine hyperplane of codimension one. Indeed, inside that cell, coordinate differences are \(\lambda^t(x_i-x_j)\) plus a constant, and \(\lambda>0\). The set of initial conditions ever encountering a tie is therefore contained in a countable union of null hyperplanes. Off this null set, the system commutes with every permutation of the vertex labels. Such permutations act transitively on the \(d!\) periodic orbits, carry each attracting basin onto another, and preserve normalized Lebesgue measure. The basins cover the simplex by step 4 and each is measurable as a countable union of eventually fixed-itinerary sets; therefore each has measure exactly \(1/d!\).

For a concrete tetrahedral example, \(d=3\) and \(\lambda=1/2\) give sorted periodic coordinates \((1,2,4,8)/15\), exactly six four-cycles, and basin measures \(1/6\).

## Verification

The standalone `check_simplex_greedy.py` uses Python rational arithmetic for \(N=3,\ldots,7\) and \(\lambda\in\{1/4,1/2,2/3,4/5\}\). It reconstructs the fixed sorted vector, tests exact periodic points and minimal periods, iterates diverse rational initial points including ties, and checks the stated uniform transient bound and post-transient symbol rotation. Running it produced **15,580 successful exact-rational assertions**. Such checks are finite corroboration only; the all-dimensional, all-parameter theorem is proved analytically above.

## Relationship to prior work

Abdulaziz (arXiv:2407.02506v1, 17 June 2024) introduced and studied the farthest-vertex contraction game on regular planar polygons. Its Section 2 includes an equilateral triangle and Section 5 describes the parity-dependent attractors for planar regular polygons. Those planar polygon conclusions include the triangular case but do not classify a regular simplex in arbitrary dimension \(d\ge3\). In particular a regular polygon with \(N\ge4\) vertices is a planar polygon, *not* a regular \((N-1)\)-simplex: it has different vertex-distance geometry and different attractor counts. The present all-parameter simplex theorem adds a sorted-coordinate conjugate contraction, a factorial orbit census, a uniform finite lock-in bound, and equal physical basin volumes for higher dimensions.

Gaivão and Pires (arXiv:2405.08444v1, 14 May 2024) give general almost-every-parameter asymptotic periodicity criteria for multi-dimensional piecewise contractions. Such generic conditions do not determine the number, coordinates, or physical basin volumes of the present cycles for **every** value of \(\lambda\). A distinct farthest-**facet** orthogonal-projection problem on regular simplices has arithmetic barycentric orbit coordinates and no branchwise strict contraction; it does not imply this farthest-**vertex** homothety theorem, whose periodic coordinates are geometric.

## Limitations

The conclusion is restricted to regular simplices, a **common** contraction factor in all branches, and a deterministic tie convention; nonregular simplex geometry or different vertex-dependent contraction factors need not admit the sorted contraction. The upper bound on transience is uniform but not asserted sharp. Basin measures concern normalized Lebesgue volume, not the shape or connectedness of each basin. Mathematical publication priority is not established by failed database searches; an equivalent formulation in unindexed literature remains possible.

## References

- A. Abdulaziz, *The Chaos Game Versus Uniform Rotation: From Sierpinski Gaskets to Periodic Orbits*, arXiv:2407.02506v1 (first public 17 June 2024), Sections 2, 3, 5. https://arxiv.org/pdf/2407.02506
- J. P. Gaivão and B. Pires, *Multi-dimensional piecewise contractions are asymptotically periodic*, arXiv:2405.08444v1 (first public 14 May 2024), Introduction, Sections 2 and 3. https://arxiv.org/html/2405.08444v1
