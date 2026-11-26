# Independent mathematical audit

## correctness

PASS

Orient each cycle coherently. The simple-cycle relations are a basis of the incidence kernel and are supported within individual blocks. Thus a sum of block-span vectors can vanish only when each block vector vanishes, giving a linear isomorphism from the product of block spaces onto 1-perp. Normalized uniform volume pulls back to a product measure by its constant Jacobian, without any orthogonality assumption. A bridge gives a^2/12. On a cycle the fibers in the uncentered coefficient box differ by translations along the all-ones direction; subtracting the minimum picks a unique allowable coefficient vector with a zero, and ties are null sets. The omitted-column parallelepipeds have equal unweighted Jacobians (the only relation has coefficients all one), hence the probability of omitting edge i is 1/(a_i H_C). Conditional on that tile, the centered mean is −a_i b_i/2 and the other coefficient fluctuations give their ordinary segment variances. The unconditional mean vanishes since p_i a_i is constant, and the variance plus squared-mean terms give a_i²/12+p_i a_i²/6, exactly (1). Strict positivity and graph simplicity give exact support recovery. Given positive edge coefficients, the per-cycle candidate a_e(t)=12c_e/(sqrt(t²+12c_e)+t) is positive and strictly decreasing; t times the sum of its reciprocals increases from zero to infinity, so there is exactly one root and hence exactly one positive length vector. The argument also covers a single bridge, trees and cycles glued at a vertex. An independent rational hull-triangulation check of three cycle weight profiles (including fractional ones) matched the full covariance in a cycle basis and checked the rationalized inverse (/workspace/branches/independent_replay.py, zonotope()). The frozen artifacts/verify.py was inspected, not executed. Finite checks are supplementary.

## originality

PASS

The distinct scope is uniform-volume covariance for arbitrary independent positive weights on cacti together with exact reconstruction of the whole labeled weighted graph. Unit-incidence covariance, a one-special-edge cycle profile, standard zonotope geometry and an analogous recovery theorem for another body are credited antecedents. In the checked statements none gives this all-weight forward and inverse result.

## value

PASS

The result answers an identifiable information-loss question: labeled second moments alone encode both adjacency and arbitrary lengths, even with unequal weights on multiple interacting-at-vertices blocks. The harmonic correction describes how uniform volume differs from independent generator sampling, and the recovery is constructive with one scalar equation per cycle. It does not purport to establish finite-sample stability, noncactus identifiability or complexity guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
