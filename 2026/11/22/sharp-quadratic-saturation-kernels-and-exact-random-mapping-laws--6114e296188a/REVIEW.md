# Independent mathematical audit

## correctness

PASS

In an orbit observed through f^d(x), the first repeat, if any, has index t+c and repeats the entry at t; subsequent equalities are determined by that transient length and period. Summing d-c+1 over c=1,...,d gives the repetition-type count. For each such c, the deepest required type (d-c,c) needs a c-cycle with a chain of length d-c in its component, and these d forced blocks are disjoint and each uses d vertices. Exactly those blocks cannot realize the window with no repeat. With just one extra vertex, no new cycle longer than d fits outside them, and the only way to make a longer orbit in a forced component is to append the extra vertex at the tip of its chain (or mark a vertex on the bare d-cycle). The d choices of cycle length are exactly the isomorphism classes. All components are rigid except the untouched bare d-cycle when that chain was extended elsewhere, yielding the factor 1+(d-1)/d by orbit-stabilizer, also valid at d=1. In the labeled SET of directed cycles of rooted trees, qualifying c-components have EGF (T^c-H_{d-c-1}^c)/c. Requiring at least one from each disjoint class multiplies the total mapping EGF by the stated occupancy factors. Absence of the no-repeat type means c<=d in every component and all heights at most d-c; applying the same occupancy rule with these truncated tree classes gives precisely B_d. Its subtraction therefore has no overcount. At rho=1/e the analytic tree branch has a dominant square-root with 1-T~sqrt(2(1-z/rho)); the product is analytic in z and T there and its limiting factors are positive. Singularity transfer divides the leading coefficient by that for (1-T)^(-1), while B_d is entire and negligible by Cauchy's bound on a circle beyond rho. The recurrence H_j(rho)=h_{j+1} gives the stated product; independent evaluations match all four displayed probabilities.

## originality

PASS

General one-variable unary-function counting, bounded forward profiles and the cycle-of-trees/singularity framework are prior. The supported distinct result is the minimal all-profile carrier and its exact classification, together with the specialized all-profile coefficient formula and fixed-depth saturation probability. No earlier equivalent joint result was found in the statements inspected.

## value

PASS

Realizing all bounded equality patterns is a natural small-carrier problem for unary term tests, and the exact quadratic size and classification give both minimum witnesses and the obstruction at the preceding size. The same orbit condition gives a concrete fixed-depth event in random mappings, for which the formula and strictly positive limit determine prevalence rather than just saying that a count exists. The exact symmetry factor and the no-repeat exclusion are structurally informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
