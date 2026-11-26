# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md line 27 omitted the common weight in the equal-weight corollary: for alpha=beta=2 the optimum is twice the asserted number, since the squared norm is homogeneous of degree one in the weights. The corrected RESULT.md gives gamma times the unit-weight value, and SLOGAN.txt now specifies uniqueness up to reflection. Re-audit: the mean-zero, piecewise-quadratic kernel has derivative t-1_{t>s}; integration gives f(s)-mean(f), also for endpoint evaluations. The squared norm is the top eigenvalue of the weighted Gram. In the ordered triangle x<=y, zero correlation is x^2+(1-y)^2=1/3. On the stated opposite-center branch, b(a) strictly decreases and the diagonal ratio R(a) strictly decreases from 5-2sqrt(3) to 1, giving exactly the proposed scalar Gram. In the dual certificate on lines 54–72, v/u=L and v/(1-u)=U force both displayed derivatives to vanish; v^2/(u(1-u))=ab/[(1/2-a)(1/2-b)]<1 since a+b<1/2. The certificate is a positive definite trace-one test matrix giving a sharp strictly convex quadratic lower bound throughout the triangle, hence equality only at its critical point and the reflection. At and after the threshold the heavier diagonal forces x=1/2 and equality in the PSD spectral bound forces zero off-diagonal, yielding exactly the two reflected y roots with lighter diagonal beta(5-2sqrt(3))/12. At equal weights x=1/sqrt(6), and (x-1/2)^2+1/12=(1-sqrt(2/3))/2, now correctly multiplied by gamma. The supplied checker only tests normalized beta=1 and misses this scaling defect. Independent replay `python3 -I /workspace/review-work/replay.py 2`: 89,304 grid PSD-budget checks with floating-point tolerance, plus explicit nonunit common-weight scaling and saturation checks. These are finite corroboration; the certificate proves the continuum result.

## originality

PASS

The corrected claim retains the distinct optimization of the exact largest eigenvalue for two weighted sites, across the full weight ratio range, including rigidity at the finite onset of saturation. Common-weight scaling itself is elementary and not a novelty claim. No verified covering primary or distinct indexed result was found in the available statement evidence.

## value

PASS

This is the exact full design curve for a natural small sensor problem: under enough weight imbalance the heavier sensor attains its standalone minimum and the lighter sensor is forced to a fixed covariance root. Below threshold, optimality instead requires a simultaneous balancing of two orthogonal weighted evaluations. The positive gap to every other ordered placement except the reflected one, and an exact threshold rather than a numerical optimum, answer an actual worst-case trace design question. The normalization/reporting repair does not change those conclusions or promise a result for reconstruction or larger designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
