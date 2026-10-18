# Independent mathematical audit

## correctness

PASS

Correctly reconstructs Edmonds' inequality model in affine hull H_k, whose projected nonempty proper subset normal is 1_S−(|S|/n)1_E and has norm c(S)=sqrt(|S|(n−|S|)/n). Boyd–Vandenberghe's general polyhedral Chebyshev-center program specializes to maximize t with x(S)+t c(S)≤rk(S). Free center variables and x(E)=k force dual subset variables μ_S≥0 to cover every element equally with common q>0; normalization λ_S=μ_S/q gives fractional partition, and fixing ∑μ_S c(S)=1 yields the stated ratio by strong LP duality. Connectedness gives full n−1 dimension, positive radius and strong duality; x(S)≤rk(S)−ρc(S) characterizes all optimal centers. Independently solved the primal and normalized dual via scipy linprog for U_{k,n}, n=3,…,7 and 1≤k<n, recovering min(k,n−k)/sqrt(n(n−1)). This finite test is not the arbitrary-matroid proof.

## originality

FAIL

The full generality is already an immediate specialization of TWO standard pre-existing results: Edmonds' exact rank-inequality description of any matroid base polytope and the general Chebyshev-center LP for ANY polyhedron (Boyd–Vandenberghe, Convex Optimization 2004, §4.3.1). Project the known normals to x(E)=k, read their squared lengths, and take the standard textbook LP dual; free x-coordinates force precisely the asserted equal element-cover constraints. Dividing by their common q is a routine dual normalization, not a new structural matroid theorem. Formula for all Chebyshev centers is exactly the general polyhedral optimal-ball feasible set, and hypersimplex barycenter computation is standard. No separate theorem beyond this mechanical combination is demonstrated. This is statement-level prior implication despite absence of the printed word 'fractional partition' in the textbook.

## value

FAIL

The record supplies no new closed form for any nonuniform rank class, no structural optimizer classification beyond the universal LP feasible set, and no new matroid-specific property beyond normal lengths elementary from cardinalities. In light of the exact general polyhedral Chebyshev LP and Edmonds constraints, the fractional-partition ratio and center set are textbook duality and a relabeling of universally available optimization data; correct reproducibility does not add independent scientific value. A motivated new effective bound, reduction, or nontrivial new matroid invariant property could have survived, but none is asserted here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
