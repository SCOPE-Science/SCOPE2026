# Independent mathematical audit

## correctness

PASS

For every n>=2, slice membership at height t is given by nonnegativity and sum_i(x_i-(1-t))_+<=t. Maximizing subset sums gives the complete halfspaces. At interior heights the coordinate faces have dimension n-1 and each size-k subset face is the product of the translated t-scaled coordinate (k-1)-simplex with the (1-t)-scaled (n-k)-cube; varying height gives facets, and both end layers are n-dimensional. Eliminating one x_i in a subset facet gives the induced Gram matrix I+uu^T with squared norm of u equal to (k-1)+(k-1)^2, hence metric factor sqrt(k^2-k+1). In the remaining n coordinates the volume integrates t^(k-1)(1-t)^(n-k)/(k-1)!, giving the exact area. Partition by excess coordinates and integrate the beta factors to verify V_n and the coordinate-facet areas. Summation verifies the increment and the first omitted increment dominates the residual factorial tail. The rank tail, fixed-K area concentration and binomial count-rank comparison then follow as stated. The independent Gram and numerical-series checks use record4() in /workspace/branches/frozen_metric_replay.py; they do not replace the analytic proof. The frozen hull diagnostic was read, not run.

## originality

FAIL

Direct corollary coverage, not an allegation about priority between same-date records. The earlier block Cayley theorem already supplies this exact one-block halfspace geometry and its fixed-height faces, by a coordinate face. The same-date augmented-cube result supplies the full Euclidean slice-area kernel explicitly. Applying the elementary hyperplane coarea factor and beta integral to this existing geometry gives the recorded metric rank spectrum, from which the boundary-law assertions are immediate. The known scalar volume is correctly credited but is not the only coverage.

## value

PASS

As geometric information, the area-weighted versus count-weighted ranks and the polynomial-size boundary approximation are meaningful quantitative descriptors of this natural exponential-facet family. They make the result useful to readers even though the quantitative claim is covered by a direct implication and is not accepted as original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
