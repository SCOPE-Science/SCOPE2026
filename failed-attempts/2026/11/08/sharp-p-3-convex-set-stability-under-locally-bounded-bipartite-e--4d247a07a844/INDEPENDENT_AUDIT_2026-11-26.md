# Independent mathematical audit

## correctness

PASS

A proper closed set leaves at least one vertex outside on each shore: a full shore would force all vertices of the other shore. With a,b selected on the two shores, each outside vertex on the second shore misses at least a-1 into the first selected shore, and the first selected shore has total missing-edge capacity da. This gives (n-b)(a-1)<=da and the symmetric inequality. The outside vertices also imply a,b<=d+1. If a>=2 and b<=1, then n<=1+2d. If 2<=a<=b<=d+1, then m<=a+db/(b-1)<=a+da/(a-1)<=2d+2, the last difference factoring as (a-2)(a-1-d)/(a-1). Neither case is possible. Choosing at most one vertex of each shore is sufficient, giving the polynomial and hull claims. At 2d+2 vertices per shore the given four-vertex construction respects the budget, and every outside vertex has exactly one neighbor in the set. The sharpness claim is for the common two-shore cutoff, not a separate optimal threshold for every unbalanced pair.

## originality

FAIL

A distinct Resultary record by title, sharp bipartite defect threshold for geodesic convexity rigidity, contains the same key exclusion under exactly the same parameter bound. Its proof Step (2) uses only length-two geodesics with same-shore endpoints, hence is already a proof for P3-closed sets; Step (6) gives the identical sharpness witness. The different treatment of cross-shore nonedges accounts for the different classification polynomial but is an immediate consequence of the definition. This is demonstrated coverage in the inspected material, not a priority inference from dates.

## value

FAIL

A sharp local-deletion threshold for universal two-neighbor closure is a meaningful structural fact. But that fact and its sharp witness are covered, and the remaining difference from the geodesic formulation consists only of counting all cross-shore pairs instead of the adjacent ones. This follows directly from the path-length convention and does not leave an independently valuable new result in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
