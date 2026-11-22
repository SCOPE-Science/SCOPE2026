# Scientific review

## Correctness — PASS

The proof starts from the regular-simplex tight frame and reconstructs every feasible unit normal from its zero-sum projection vector with fixed squared norm \(N/d\). For each nontrivial sign bipartition, strict convexity reduces the minimum necessary projection energy to two lower-bounded equal-sum problems. The unique solution retains the heavier group's lower bounds and water-fills the lighter group; the minimum common sum is exactly the heavier weight total. The partition minimum gives the sharp critical scale, and equality in both energy bounds classifies every critical hyperplane. The open-ball strict endpoint and disjoint unequal-ball neighborhood follow from verified Euclidean center distances and a uniform triangle inequality. The packaged checker passed 119 exact-weight profiles and 4,760 seeded directional comparisons; these finite checks do not substitute for the argument.

## Originality — PASS, provisional priority

Osipchuk's 2026 paper defines nonconvexity-point sets and proves their topological behavior but does not give this weighted exact threshold. Casado et al. solve *point covering of the simplex body* with vertex-centered balls, not hyperplane incidence. Har-Peled and Robson (and classical Gritzmann–Klee/Alexander) already identify the balanced directions that also occur in the equal-radius corollary, so these are credited and not claimed as new. The distinct statement is the arbitrary-positive-weight threshold with the one-dimensional water-filled active-set and complete equality profile. The closest published mathematical records on weighted simplex-generator zonotope radii optimize signed-corner Euclidean norms, not lower-bounded equal-sum signed projections. Bezdek–Lángi address spherical zones and optimal great-sphere arrangements, not this fixed weighted configuration. Searches for the exact object, weighted aliases and dominance found no direct implication-equivalent theorem, although historical priority is not certified and older broader convex-programming treatments might cover it.

## Mathematical value — PASS

The result determines a complete natural inverse problem for disjoint ball obstacles: precisely which common scale forces every hyperplane through their centroid to intersect the union, for *arbitrary* unequal radii. The finite water-filling classification reveals active constraints invisible in equal-weight simplex widths; for weights \((1,1,1,2)\), the exact level is \(\sqrt{8/57}\) with three distinct projection magnitudes. It also produces an open family of disconnected sets whose hyperplane-nonconvexity-point set has nonempty interior. This is a structural classification, not a single table lookup or an arbitrary parameter slice.

## Risks and limits

Independent review has not occurred; an unlocated prior formulation of weighted signed-frame avoidance might dominate the theorem. The theorem neither solves free placement of obstacles nor gives the globally exact nonconvexity-point set. The computational spot checks are finite and not certificates for the universal quantifiers.

Self-review: passed. Independent audit: not yet performed.
