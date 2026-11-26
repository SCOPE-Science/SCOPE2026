# Independent mathematical audit

## correctness

PASS

On a strict support/sign cell the Hessian of the active objective is I+alpha vv^T and the derivative is its inverse, with zero rows and columns off support. Choosing positive active outputs and zero inactive inputs realizes every support with strict inequalities. Thus the finite piecewise-affine maximum equals the largest absolute row sum; a small row-sign perturbation attains it. For fixed row i the optimum excess is the unique zero t of -w_i^2-t(alpha^{-1}+w_i^2)+sum_{j≠i}(w_i w_j-t w_j^2)_+, obtained by maximizing numerator minus t times denominator. This is strictly decreasing; for t>0 the included weights are precisely those below w_i/t, with ties optional, and for t≤0 all can be included. Hence one sort plus all row-prefix scans suffice. For the envelope write the active Jacobian as (1-lambda)I+lambda P with P an orthogonal projector and lambda=alpha||w_S||²/(1+alpha||w_S||²). Row i of P has l2 norm squared P_ii=p, so its l1 norm is at most p+sqrt((|S|-1)p(1-p)), maximized at p=(1+1/sqrt(|S|))/2 for |S|≥2. Equality for the global envelope forces full support and equal off-diagonal magnitudes, and substituting p=1-w_i² yields the stated distinguished-to-common ratio sqrt(n)-1. The one-coordinate cell cannot reach the envelope. Uniform rows maximize at full support and match the envelope only at n=4. A smallest weight on full support proves strict expansion except in dimension two with equal weights, and concentration on one weight gives infimum 1 by the finite row formulas. A separate inverse-Hessian enumeration and scalar-prox solve reproduced several attaining pairs, including tied weights (`python3 -B /workspace/review_replay.py`, check 3). No uploaded checker was executed.

## originality

PASS

Pass for the exact fixed-weight sliced norm optimization and normalized anisotropy classification, not for the proximal map, Jacobian, epigraph representation, or generic projection-norm bound. Closest same-day epigraph comparison is substantively related, but its stated full-coordinate norm differs even on the simplest equal-weight example, and does not already evaluate the claimed slice or optimize its weights.

## value

PASS

The coordinate-error modulus is a natural robustness invariant for a widely used Euclidean proximal step, for which the Hilbert norm guarantee is insufficient. The exact prefix law turns support enumeration into a quadratic scan, while the normalized weight design distinguishes bounded uniform sensitivity from worst-case square-root dimension growth and gives the unique dimension where they coincide. These are usable exact decisions rather than a merely reformulated projection bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
