# Independent mathematical audit

## correctness

PASS

Projection to the zero-sum space preserves Gaussian coordinate orders. The graphical arrangement classifies vertices by the signs on edges, so the clique order and independent-label gap assignment determine the orientation. Each such choice has exactly the product of the gap factorials as its number of compatible orders. The factorial convolution controls noncorners: the normalized interior sum is bounded inductively by a constant times the sum of reciprocal binomial coefficients to power t−1, which is O(1/s); the two endpoint terms are bounded by 2/s. This proves the fixed-r,t condensation and constant, rather than extrapolating from tests. For r=2 exactly the orientations with empty middle gap merge in pairs upon deletion of the clique edge, giving the displayed increment and the split-to-bipartite ratio 3/5. Independent exact enumeration (python3 /workspace/branches/03680095-73ed-4252-8d9e-71dec447a52a/independent_split_check.py) covered all ten split pairs with r,s≥2 and r+s≤7, moments t=2,3,4, and the deletion formula for 2≤s≤5. For (2,2) it gave C_2=1/16 and bipartite C_2=7/72. The frozen checker was inspected as evidence, not run.

## originality

FAIL

The complete bipartite angles alone as an unlabeled spectrum would not give the split angles. The actual earlier Resultary proof gives the stronger labeled alternating-block classification, including each block’s factorial of compatible orders, and proves concentration on the very same independent-side one-block class. In a bipartite chamber, making the first side a clique just orders each of its first-side blocks independently: a block of size a gives a! equal pieces, with no other cuts because relative order across first-side blocks already follows from their positions around second-side labels. Thus the split moment weight is obtained directly by replacing each first-side factorial factor (a!)^(t−1) by 1 in the prior block sum. This generates precisely the frozen angle and moment laws. For t≥2 the new noncorner collision mass is at most the old noncorner mass (splitting reduces a power sum), already o(s^(−rt)); the subdivided one-block class has exactly (r+1)r! pieces with angle s!/(r+s)!, giving the sharp coefficient directly. Therefore this is coverage by a specific prior construction and bound, not an inference merely from related titles or an unavailable paper.

## value

FAIL

The collision moments and the edge sensitivity are natural geometric questions, but the frozen contribution reduces to an equal subdivision of already classified cones with an already controlled noncorner tail. The sampling comparison and the ratio are direct consequences of that refinement and the known gap encoding; no independently valuable new exact invariant or nontrivial extension survives in the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
