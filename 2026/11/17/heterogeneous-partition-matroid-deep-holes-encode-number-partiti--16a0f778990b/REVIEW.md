# Scientific review

## Correctness — PASS
The projection onto each block hypersimplex is the uniquely minimizing Euclidean point by a supporting-normal inequality. The resulting rational \(\phi_i\) is strictly convex on the entire occupancy interval; transferring one unit between two partially occupied blocks strictly improves one of the two transfer directions. Hence a maximum has at most one partial block. The half-rank endpoint equality is equivalent to equal-sum partition, and the strict residual averaging proof excludes nonvertex farthest points at that threshold. Exact rational exhaustive enumeration over 122 heterogeneous instances and 1,360 independent partition instances agrees with the formulas. This computational evidence is not substituted for the proof.

## Originality — PASS, historical priority provisional
The prior equal-block deep-hole result applies only when all blocks have identical sizes and ranks; it does not give arbitrary heterogeneous occupancy compression or the succinct PARTITION threshold. Lasoń–Michałek (arXiv:2005.08359, §2.2) proves the Cartesian-product description of direct-sum matroid base polytopes, not Euclidean distance extrema. Aprile et al. (arXiv:2106.12829, §§1,4.3) study product slack matrices, and Pineda-Villavicencio–Schröter (arXiv:2010.10227, introduction and hypersimplex facial discussion) study reconstruction. Other database entries linking PARTITION with Euclidean polytopes concern inballs or zonotopes, not this rank-constrained product-to-hypersimplex Hausdorff problem. The search and partial source inspection cannot exclude an undiscovered equivalent older result.

## Mathematical value — PASS
A product of hypersimplices is a standard matroid-base polytope, and its distance from the universal same-rank hypersimplex measures the geometric cost of enforcing blockwise rank constraints. The theorem classifies the geometry of all maximizing occupancy profiles for arbitrary heterogeneous capacities and identifies weak NP-completeness of a sharp, natural exact metric threshold. This arithmetic barrier contrasts meaningfully with the closed equal-block case.

## Limits
The theorem does not establish strong NP-hardness, hardness under an expanded coordinate representation, or a full general nonvertex-extremizer classification. Finite tests are not proofs; independent verification and comprehensive historical-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
