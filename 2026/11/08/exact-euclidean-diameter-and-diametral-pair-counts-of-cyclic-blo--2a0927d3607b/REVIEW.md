# Independent mathematical audit

## correctness

PASS

Two positive coordinates in one block permit a signed transfer, excluding vertexhood. A singly supported vector in each positive block is a vertex exactly when its block sums are a vertex: decompositions project downward and can be lifted in the chosen coordinates. A zero block breaks the residual cycle into paths with totally unimodular bipartite edge constraints, including boundary singleton rows. With all blocks positive every edge constraint must be active; the edge equations have the unique all-half solution on an odd cycle and deficient rank on an even one. Integral vertices have squared norm at most r=floor(m/2), with equality only at maximum independent sets, and odd half-integral endpoints have squared norm m/4<r for m≥4. Nonnegativity gives the upper bound 2r on squared separation; two shifted disjoint alternating supports of size r attain it on either parity. Strict convexity in each endpoint forces vertexhood, and equality requires disjoint coordinate (not block) supports. The even cycle has two alternating supports; the odd cycle has one gap of length three and all others length two, giving m rotations. The shifts by 2j and 2j+1 intersect a fixed support in r−j and j blocks respectively, using the stated disjoint shift ranges. Hence each overlap t<r supplies m unordered distinct-support pairs. The distinct-label condition yields a(a−1) choices per shared block, and only identical block supports require a division by two at the color-count stage. This verifies both closed counts including a=1. The frozen code was inspected, not executed. Independent /workspace/branches/eca80989-28de-4482-bb5b-efd421654a49/independent_check.py and its log cover 655,187 exact unordered distances at 15 (m,a) points using doubled coordinates. This corroborates the analytic result but assumes the candidate vertex list.

## originality

PASS

Credit the equality structure and full colored diametral-pair enumeration, not the known cyclic block polytope, its half-integral vertices or the independence-number norm bound. In the inspected primary and indexed sources the close statements concern different domains, a different distance, or a vertex classification that does not supply pair multiplicities. The cited unblocked enclosing-sphere result could not be inspected and remains a risk for that special case, not evidence against the full count.

## value

PASS

This is a natural Euclidean extremal invariant of a previously defined polytope. The diameter alone uses an elementary norm bound, but the complete two-parameter equality count distinguishes coordinate from block disjointness and resolves the odd rotation overlaps, including same-block-support pairs invisible in the unblocked model. It gives reusable equality and multiplicity information, not merely an isolated small-size or normalization calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
