# Scientific review of isolated-cluster variance ordering

## Correctness
The exact conditional law for the two hubs yields an explicit probability generating polynomial and first and second moments. Algebra gives the closed variance formula. A separate exact identity for moving one leaf from the smaller hub to the larger hub is strictly positive beyond \((b-a+1)/8\), by a complete two-case inequality using \(A\le1/8\). Iteration gives global uniqueness within the stated diameter-at-most-three class and proves the quadratic asymptotics. A standalone Python checker passed 5263 exact rational assertions, including exhaustive retention samples for all trees in the class through 12 vertices; the general result rests on the displayed analytic argument.

## Originality
Relevant site-percolation literature studies component transitions on large regular pseudorandom graphs, not this finite-tree variance arrangement; the accessible full-text introduction, main theorems and component sections were compared. Similar graph-invariant extrema and earlier bond-percolation isolated-count laws concern other observables or independent edge retention, which cannot imply the vertex-retention formula without additional calculation. Searches for inverse imbalance, bistar, singleton-component variance and related terms found no established equivalent. This is qualified originality, not proof of historical uniqueness: general graph moment or extremal formulas may imply the special result implicitly.

## Value
A diameter-at-most-three tree is exactly a two-hub double star (stars included), the first natural nontrivial class in which tree structure varies with fixed order. Fluctuations in the count of surviving singleton clusters are a basic percolation observable. The strict balance-to-star variance ordering supplies all-order minimizers, maximizers, a quantitative structural gap, and an asymptotic factor-two contrast; it is not merely a single computed example. Restrictions to this family and to retention probability \(1/2\) are essential limits.

Self-review: passed. Independent audit: not yet performed.
