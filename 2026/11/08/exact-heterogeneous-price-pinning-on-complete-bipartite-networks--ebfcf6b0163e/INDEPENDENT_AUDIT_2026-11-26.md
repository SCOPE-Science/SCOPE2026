# Independent mathematical audit

## correctness

PASS

For the two diagonal blocks, PSD requires every shifted diagonal entry x_i,y_j>0 by a cross-shore 2×2 minor. On that domain the rank-one Schur complement is exactly (Σ1/x_i)(Σ1/y_j)≤1. The displayed iff in Proof 1 should be read with this positivity condition from its preceding sentence; the product alone on arbitrary signed diagonals is not sufficient. For the stated positive max formulas, A is nonincreasing and d=cA nondecreasing. Before any first-part activation, d is strictly increasing, so the second reciprocal sum strictly decreases once a second-part threshold is passed; after first-part activation A strictly decreases. Thus no level-one plateau is possible; the limit near c=0 exceeds one (is infinite if t≥min(p,q)), and the large-c limit is zero. At the root, the positive vector with components c/X_i and d/Y_j has shore sums d and c, so is a null vector of the shifted pinned matrix, which is PSD by the criterion. Its squared components are bounded by prices and equal them at positive gains. For any other feasible allocation, testing its shifted matrix on this vector bounds the cost difference below by a nonnegative quadratic form. Equal cost forces that vector into the new null space too; every component is positive, so the allocation is identical. Uniform extra gain h gives F(t+h)≤F(t)+h times the sum of prices, and a slight cost reduction from an allocation strictly above a lower target proves strict monotonicity. The constant-vector test gives divergence. As t tends to zero the c root tends to q times the square root of the minimum price (the end of the t=0 plateau), giving sole activation for a unique cheapest vertex. Full activation gives c=T_β and d=T_α and the exact affine law, valid also at a zero-gain boundary. For two shorewise prices α<β and second shore free, the quotient gives (q+a−t)(p−t)=pq and d=p√α; the second shore activates exactly at p−t=p√(α/β). This verifies the transition, both rates, and boundary agreement. The supplied verify_bipartite_pinning.py was inspected, not executed; its finite numerical or exact-rational cases are not the proof.

## originality

PASS

The supported distinction is the exact arbitrary independent-price solution on a non-star biclique, including the coupled target equations, exact terminal threshold, and two-shore price transition. Weighted spectral pinning, price sorting, scalar optimization ideas and affine tails are not new on their own. The closest actual complete-graph and star statements use the same objective but neither covers two shores of size at least two; earlier bipartite edge pricing uses a different decision variable and eigenvalue. No inspected source mechanically gives this full claim. The cited Jafarizadeh comparison remains bounded by access.

## value

PASS

On a natural connected graph with heterogeneous costs, the result replaces repeated matrix optimization with two monotone scalar solves and gives the unique optimal actuator allocation. It identifies exactly when the affine regime begins and yields the nontrivial two-shore transition and closed optimal rate in the two-price model. A user deciding which vertices to pin at a given budget can use these as exact predictions, rather than just a numerical feasibility test or an example in the equal-price setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
