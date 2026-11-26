# Independent mathematical audit

## correctness

PASS

Over any prime power, the quotient by the derived central line is a 2r-dimensional symplectic space. Over each proper quotient subspace there is one center-containing lift, and over each nonzero isotropic k-space there are q^k additional functional-graph lifts. An ordered isotropic basis has q^(2r−j)−q^j choices after j steps, so dividing by the number of ordered bases gives I_{r,k}. Two lifts generate iff their projections sum to the quotient: a subalgebra surjecting to the quotient contains a nonzero central bracket by nondegeneracy. Choosing the intersection with a fixed k-space and then a quotient graph gives C_{2r,k}; when both lifts omit the center, spanning requires complementary Lagrangians. After choosing a Lagrangian complement as reference, the other complements are symmetric graphs, q^(r(r+1)/2) also in characteristic two. These facts yield the three edge terms with the correct divisions. Coloring by a containing hyperplane is proper and the hyperplane lifts form a matching-size clique. In a maximum clique the nonempty sets of containing hyperplanes are pairwise disjoint and exhaust exactly one hyperplane per projection, so the projections are those hyperplanes. For r≥2 each has one lift, and for r=1 each has q+1, proving both maximum-clique counts. The leading population exponents are k(2r−k) and f_r(k)=2rk−3k²/2+3k/2. Ranks 1 and 2 are dominated by center-free Lagrangians; r≥4 by center-containing r-spaces since (4r+3)²/24<r². At r=3 there are three size-q^9 strata, one of dimension 2 and two of dimension 3. Only the four ordered pairs of 3-space strata can span; for each of them the ordinary or symplectic complement count divided by the corresponding population of projections tends to 1. Thus the limit is 4/9 there and 1 otherwise. Conditioning on distinct sampled vertices vanishes in the limit. Separate RREF enumeration using the projection criterion (not iterative bracket closure) gives (N,E)=(10,27), (156,3805), (691,100905) at (r,q)=(1,2),(2,2),(2,3); replay is projection_repro.py with recorded outputs in branches/d639dd7e-d580-4267-8c0f-9b52507d1a4b. Only those small prime-field instances were enumerated in that check; larger ranks were formula-only, and the proof, not the finite checks, extends to arbitrary prime powers. The frozen checker was inspected, not executed.

## originality

FAIL

Distinct indexed Resultary record cea008ee3276 gives the identical all-rank vertex and edge formulas for r≥2, including the weights, complement term and clique/chromatic number; the previously classified H_3 supplies r=1. The advertised 4/9 and its uniqueness follow by directly taking the leading terms of those exact formulas. The maximum-clique lift counts follow by the containing-hyperplane pigeonhole argument from the published quotient graph and the very same indexed fibers. This is demonstrated mathematical coverage; no precedence inference is drawn from the catalogue dates. The superficially similar 5/9 result for permuting pairs is not the basis of this decision.

## value

FAIL

The rank-three effect is an informative interpretation of the natural edge-density invariant, but as an incremental finding here it is exactly a leading-term calculation from the already indexed exact weighted census. The maximum-clique counts are the direct product from hyperplane fibers, and the exact counts themselves are covered. No independently valuable uncovered remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
