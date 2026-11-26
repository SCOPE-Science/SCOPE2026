# Independent mathematical audit

## correctness

PASS

The two positive phase equations give (a_i−1)(b_i−1)=1 and then a_i=a_{i+1}; conversely r>1 and s=r/(r−1) give all such states, including the fixed state at r=2. Fourier reduction of the product of the two step derivatives gives trace q+q²d and determinant q²d. The Schur–Cohn margin is 2d(1−cos θ)[1−2d−(1+2cos θ)d²], with the bracket at least 5/16. The only neutral root is the simple tangent root at q=1. In coordinates along and across the fixed curve, choose an adapted norm for the transverse derivative at the selected point and shrink the neighborhood to get uniform contraction there. The summed tangential increments are bounded by a geometric series, so sufficiently close points stay in the neighborhood and converge exponentially to a member; no global basin is implied. Implicit differentiation gives λ′(1)=1/(1−d) and λ″(1)=2d(1−2d)/(1−d)³. The even analytic modulus has quadratic decrement d(1−3d)/(2(1−d)³)>0 and fourth-order remainder. Compactness away from q=1 and strict local monotonicity select q=exp(±2πi/k) for large k. At fixed k the root through q is q+(q²−q)d+O(d²) and the other root tends to zero; the stated small-d maximum follows. Independent replay: `python /workspace/branches/independent_math.py spectrum` verifies the Schur and expansion algebra exactly and compares finite-difference return Jacobians with the factors for four finite rings; the numerical checks are diagnostic only.

## originality

PASS

The supported distinct contribution is the exact all-ring transverse spectrum and sharp spatial-size gap for the positive two-cycle family. The existence of period two for the motivating three-variable system and classical Fourier and disk tests are not claimed as new. Separate possible overlap on k=3 does not establish the all-k theorem or either claimed gap law.

## value

PASS

For a nonisolated family, a unit multiplier cannot decide whether perturbations select a nearby cycle or destabilize it. The transverse classification determines this for every finite ring, and the positive explicit gap coefficient quantifies the increasing relaxation time with system size. These are natural dynamical invariants tied to the originating recurrence, not finite numerical observations or a uniform-in-size claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
