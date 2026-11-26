# Independent mathematical audit

## correctness

PASS

Write d_i for the coefficient of e_i in R(e_i). On (e_i,e_i) the left side is Σ_j a_j r_{ji}²e_{σ(j)} and the right side is 2a_i d_i R(e_{σ(i)}). The basis vectors on the left are independent and every a_j is nonzero, so d_i=0 forces the entire input column to vanish. The e_{σ(i)} coefficient gives d_i²=2d_i d_{σ(i)}. In characteristic two there is no active column. Otherwise an active d_i propagates by d_{σ(i)}=d_i/2, giving exactly the 2^{|C|}=1 condition, impossible in characteristic zero. A scalar on each resonant cycle extends by this recurrence; the diagonal map then verifies the identity on equal basis pairs and trivially on unequal ones. This proves exactly 2^r supports and an r-dimensional diagonal locus over the stated field, with resonance equivalent to order divisibility in odd prime characteristic. Natural-basis changes are monomial because the independent squares force distinct natural-basis columns to have disjoint coordinate support. In the unweighted single resonant cycle, v=Σ e_i has v²=v and v e_j=e_{σ(j)}; for λ_{σ(i)}=λ_i/2 the map e_i↦λ_i v verifies the identity on all basis pairs, yielding rank one while the same diagonal coefficients yield rank n. An independent direct enumeration tested all 81 maps for the unweighted two-cycle over F_3, obtaining ranks 0,1,1,2,2, with both inputs active for every nonzero solution.

## originality

PASS

The supported distinction is the all-operator active-input support theorem for every weighted permutation evolution algebra over every field. Derivations already give the resonance parameter and the invertible diagonal profiles after reciprocal correspondence; the earlier characteristic-three unweighted two-cycle record also gives the exact two branches for that instance. Neither entails the all-operator necessity, including singular nondiagonal maps on arbitrary weighted cycles. The E^2=E graph-classification question does not supply that conclusion. The novelty judgment is limited to this support classification and its general attainability, not to the recurrence as a numerical cycle condition or the isolated two-cycle example.

## value

PASS

Active inputs are a natural exact invariant of a graph-based operator problem. The theorem turns the nonlinear equations into a necessary support rule applying even to singular and nondiagonal solutions, realizes every permitted support, and gives an exact count and field dependence independent of all nonzero structure weights. This is useful structural information without claiming the full operator variety; the rank-one construction shows why the distinction matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
