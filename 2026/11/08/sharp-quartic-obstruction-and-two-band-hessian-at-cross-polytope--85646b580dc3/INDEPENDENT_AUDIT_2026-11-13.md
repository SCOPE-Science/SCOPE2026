# Independent mathematical audit

## correctness

PASS

For the unnormalized real two-moment loss on 2d labeled points x_{i,+},x_{i,-} at the cross-polytope ±e_i (d>=3), tangent coordinates p_i=(u_{i,+}+u_{i,-})/sqrt2, q_i=(u_{i,+}-u_{i,-})/sqrt2 separate centroid and covariance linearizations. The product-sphere Hessian bands are exactly zero with multiplicity d(3d-5)/2, 4a(d-1) with multiplicity d, and 16b with multiplicity d(d-1)/2. Independent Jacobian matrix eigenvalue checks for d=3,4,6 reproduce those bands and zero multiplicities. Positive-spectrum condition one occurs only at a/b=4/(d-1), without claiming to eliminate nonrotational zero directions. For zero-Hessian symmetric-pair velocities p_i perpendicular to e_i and sum p_i=0, unit-sphere radial second derivatives force a second-order covariance diagonal D_j=sum_{i != j}p_{i,j}^2 -sum_{k != j}p_{j,k}^2. Second-order freely chosen tangent corrections can cancel every off-diagonal covariance term but no diagonal one, establishing universal liminf E/t^4 >= b||D||^2. The analytic normalized curve written in RESULT attains that coefficient. Therefore D=0 precisely permits a curve of loss O(t^6), NOT necessarily an exact design. For p1=e3,p2=-e3 the exact curve gives E(t)=6 b t^4/(1+t^2/2)^2; K skew and K1=0 supplies nonrotational exact two-design curves. These last statements are compatible, rather than contradictory.

## originality

PASS

The earlier regular-simplex two-band Hessian result uses d+1 spherical nodes and has no nonrotational kernel, whereas here the 2d-node cross-polytope has extra flat directions, a different spectral weight balance and a sharp fourth-order diagonal-flow obstruction. Needham–Shonkwiler's original complex-frame moment-map work already gives qualitative quadratic cones at singular orthodecomposable tight frames: that general phenomenon is not claimed as novel. The inspected published formulation does not state this exact real, centered, labeled 2d-point functional, two Hessian bands and b||D||^2 sharp coefficient. Xiao–Zhuang give general spherical-design gradient/Hessian methods but the specific coefficient was not found in accessible material. Prior real-moment-map normal forms remain a priority risk.

## value

PASS

Cross-polytopes are canonical antipodal spherical designs, and optimizing their moment-discrepancy loss encounters flat directions beyond rotations. An exact quartic barrier distinguishes obstructed versus second-order feasible deformations and quantifies the minimal residual on every symmetric-pair zero-Hessian direction. This is a useful local geometric obstruction and optimizer diagnosis rather than a generic Hessian formula or a claim about all exact design curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
