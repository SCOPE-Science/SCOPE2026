# Independent mathematical audit

## correctness

PASS

For an interval between successive delivered times, partition its Lévy increment into equal exchangeable pieces conditional on their total. Summing these conditional means and taking an L² limit gives the interpolating bridge mean. The other observed increments are independent of this segment. The centered integral has variance vd³/3 and covariance vd²/2 with the total of variance vd, giving bridge residual variance vd³/12; on the free terminal gap the independent residual has variance vd³/3. Zero gaps add nothing, and conditioning on the revealed independent delivery subset gives the stated exact mixture. For every p>0 the all-delivered term is strictly convex in the injective gap vector, proving global uniqueness. At p=1 its stationarity equations give standard gaps twice the final gap. At small p the singleton Hessian uniformly supplies curvature of order p, while the gradient at co-location is O(p²); the convexity inequality thus localizes the minimizer to O(p) despite co-location being on the ordered boundary. Expanding uniformly there gives the quadratic with linear coefficient −(2i−n−1)/9 in coordinate i: completing the square proves both the spacing and the n(n²−1)/486 gain. The ordered offsets are admissible, n=1 is exactly the singleton problem, and p=0 is excluded. A separate algebra replay gives p³/81+O(p⁴) improvement at 2/3±p/9 for n=2. Inspected RESULT.md lines 25–76, VERIFICATION.md, check.py and check_output.txt; 102 assertions are the recorded finite check, not a rerun or a proof. The expansion holds for fixed n only.

## originality

PASS

The pinned Brownian-bridge erasure problem is the strongest verified structural overlap, including the very same singleton-curvature/pair-spread mechanism, but it does not cover the free terminal gap or the specified Lévy theorem. Pass is for the free-terminal all-Lévy formulation and its sharp rare-delivery design and gain, not for introducing bridge quadrature, erasure design, or the general staircase proof mechanism.

## value

PASS

The free terminal gap is essential when the endpoint is not observed. The result quantitatively distinguishes redundant co-location from diversification for a natural loss: the first-order node offsets and the nonzero third-order risk gain for n≥2 are sharp, and one design works across the square-integrable Lévy class. This is useful even though the optimal-design method is close to the pinned analogue and the result is not a claim about adaptive channels or growing budgets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
