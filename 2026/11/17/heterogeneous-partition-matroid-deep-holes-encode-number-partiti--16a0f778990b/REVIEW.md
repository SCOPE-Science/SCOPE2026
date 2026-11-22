# Independent mathematical audit

## correctness

PASS

P=product Delta(c_i,q_i) and H=Delta(R,N). For a H-vertex selecting j_i coordinates in block i, Euclidean projection retains chosen ones and redistributes missing rank equally if j<=c, or scales selected ones if j>=c. Supporting-normal optimality gives squared gap phi_i(j). Each piecewise phi is C1 and strictly convex over [0,q_i], so a two-coordinate +/-1 occupancy transfer strictly improves at least one way whenever two blocks are partially occupied. Thus all vertex maximizers have at most one partial block, yielding the candidate max. On balanced (q,c)=(2a,a), all block phi<=a/2 strictly below inside: equality R/2 exactly when equal-sum PARTITION subset exists. The projection-residual strict Jensen inequality forces all continuous equality points to be the distinct full/empty binary H vertices. Binary-encoded block parameters provide polynomial reduction and NP witness, giving weak rather than strong NP-completeness. Independent check: Wrote a separate Fraction-based exhaustive occupancy enumerator for four heterogeneous profiles ((2,4,6),(1,2,3)), ((2,6,8),(1,3,4)), ((2,3,5),(1,2,2)), ((3,5,8),(1,3,2)). Exact maxima were 3,4,109/30,24/5; every maximizer has at most one partial block. Verified supporting-normal projection condition analytically and the equal-sum PARTITION equivalence, without treating cases as an infinite proof.

## originality

PASS

Best-of-knowledge: examined primary source evidence, actual same-object implications, and published mathematical findings. Earlier constructions, generic formulas and independent source results are credited; the surviving quantitatively specified theorem is not implied by the directly inspected antecedents. No certification of absolute historical priority is asserted.

## value

PASS

The Euclidean farthest-point distance to a partition-matroid base polytope is a natural geometric discrepancy between base-choice constraints and unconstrained rank choices. Exact occupancy compression for arbitrary heterogeneous capacities and a sharp arithmetic equality threshold provide useful structure and an unexpectedly exact link to classical weak NP-completeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
