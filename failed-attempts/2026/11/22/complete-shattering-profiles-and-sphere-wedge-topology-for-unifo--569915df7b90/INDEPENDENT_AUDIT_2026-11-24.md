# Independent mathematical audit

## correctness

PASS

The minimax proof is valid. Removing the support and at most two neighbors for each prescribed positive leaves a bipartite graph; its larger side plus the positives yields the stated ceiling lower bound. The upper-bound trace is built recursively by excluding the first vertex if it is in the support, allowing at most one selection in the first two positions if both are outside the support, or prescribing the second vertex positive and excluding its two neighbors; the short bases and the ceiling update check out. All-positive forces independence and size at most k. Capacity at least k for every trace is sufficient by trimming outside its positive vertices. Spacing compression gives the binomial counts. For d≥1, 3d≤n+1, and every maximal independent set dominates the path and hence has at least ceil(n/3) vertices. For an independent check of shellability without relying on the unavailable Björner–Wachs copy: in any path forest with all maximal independent sets of size at least d, choose the neighbor v of a leaf u when there is an edge. In the deletion of v every maximal independent set contains the now isolated u and is maximal in the original, so has size at least d. In the deletion of the closed neighborhood of v a maximal independent set has size at least d−1, by adjoining v to make a maximal set of the original. These two smaller forests give the deletion and link of the rank-d truncation at v, of ranks d and d−1, with no common facet. Induction gives pure vertex decomposability, starting at rank zero and at edgeless graphs (ordinary simplex skeletons, with the same deletion/link induction). Pure shellability gives the wedge, whose multiplicity is (−1)^(d−1) times reduced Euler characteristic as stated. For d=0 the complex consists of the empty face and no sphere-wedge conclusion is needed. Frozen verification_output.txt lines 1–4 records finite trace, minimax and two-field homology checks; verify.py was inspected and not executed. Neither recorded field homology nor finite trace checks establish all-parameter topology.

## originality

FAIL

The earlier fixed-weight cycle/path result was recovered in full at the decisive locations. It does not print the minimax identity or the path shattering polynomial, but its padded-path mismatch analysis and its general alternating-segment completion rule together give the minimax identity and exact support criterion directly. The polynomial and wedge rank are then standard face counts, purity and shellability consequences. The original proof is correct and uses a different trace construction, but the claimed complete classification is not distinct on the evidence below. This is an implication finding, not an assertion that the earlier record prints the same formulas or that every formulation is historically accounted for.

## value

FAIL

The exact shattering complex of a uniform path class is a natural object, and the alternative minimax proof is clear. But the earlier exact segment rules already determine the complete support complex and worst trace capacities by direct substitution. The enumerator and sphere count then use the standard path spacing count, domination bound, shellability and Euler characteristic. As submitted, no separate substantive exact result beyond these routine consequences has been established; finite verification does not supply that missing gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
