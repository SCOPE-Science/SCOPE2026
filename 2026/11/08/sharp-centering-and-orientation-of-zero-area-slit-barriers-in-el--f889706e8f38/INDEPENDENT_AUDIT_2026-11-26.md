# Independent mathematical audit

## correctness

PASS

The removed slit has zero area, so the affine map to the disk preserves the endpoint sampling and finite-segment event. In the line transform the endpoint-coordinate determinant is |t-q|; using the angle modulo pi retains both orders of endpoints without duplicating lines. Straddling a slit point integrates the Jacobian to L_+L_-(L_++L_-), with L_+L_-=1-s^2-h^2 and L_++L_-=2 sqrt(1-p^2). Pairing reflected angles yields strict Jensen improvement when h is moved to zero; the centered-height weight is even, and differentiating its angular integrand gives strictly negative derivative at every s in (0,1). The integral over a shifted interval of length 2a thus decreases strictly with |c|. This proves the global unique center. The half-length in disk coordinates is the Euclidean half-length times ||L^{-1}e||; equality in its singular-value bound identifies the minor axis and the circular tie, and the length restriction ensures admissibility. Integrating the centered weight gives the stated atanh formula; direct expansion gives 2-8s^2/3+O(s^4) at zero and weight ~2(1-s) at one. At a full diameter independent endpoints straddle its line with probability 1/2. An independent finite check using /tmp/opencode/frozen_1_2_3_checks.py integrated over endpoint heights with conditional horizontal coordinates uniform on chords; the two-uniform convolution gave 0.233550048 centered at a=0.3, 0.206012740 for axial displacement 0.3, and 0.189544838 for perpendicular displacement 0.4. This corroborates normalization and finite-segment crossing, not the universal optimization proof. Inspected the frozen checker without running it.

## originality

PASS

The supported distinct result is the sharp finite-segment blocking probability and global placement/orientation optimum for an interior straight slit. Classical visibility definitions and the area-endpoint chord Jacobian are not new; the closest separate Beer record concerns only local displacement of a positive-area disk hole. No directly covering theorem was found in the inspected comparisons.

## value

PASS

Zero removed area does not make visibility trivial because it is a condition on the whole connecting segment. The all-offset strict inequality and explicit length profile resolve a natural obstruction design problem and distinguish direction in the Euclidean metric from affine equivalence. The result gives both the sharp limiting half threshold and the exact finite-length design rather than only a small-slit approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
