# Independent mathematical audit

## correctness

PASS

The frozen interpolation warning incorrectly said that separately interpolating both grid trajectories introduces a defect; piecewise linear interpolation commutes with subtraction. The corrected RESULT distinguishes subtracting the continuous exact flow (whose grid interpolation error can be O(h^2)) from subtracting its grid interpolant, explicitly allows a degenerate limit and supplies the maximal-error estimate. For the same tableau c=(x,1-x), the two third-order elementary terms have coefficients x(1-x) and 1/4-x(1-x)/2, leaving h^3 delta(x) H after subtracting the exact flow. Uniform integration gives E delta=0 and Var delta=1/180. Bounded Df gives sequential contractions and the linear growth bound with small h gives a common compact set. The sum of the centered adapted local defects has maximal second moment O(h^5); summing the error equation and applying discrete Gronwall gives the same bound for the nodal errors. The sum of the absolute remainders after linearization is o_P(h^(5/2)). After scaling, the driving martingale has bounded O(sqrt(h)) increments and covariation converging uniformly to the deterministic integral of HH^T/180. The martingale FCLT gives a continuous limit; the Euler drift sum converges to the integral of JZ (the linear integral equation is continuous in the driving path in the uniform norm), yielding the claimed covariance and shared Brownian driver. Independently the scalar multiplier is 1+z+z^2/2+x(1-x)z^3+O(z^4). For independent steps the first two moments are powers of the one-step moments; the squared bias is O(h^6) and the variance is u0^2 exp(2 lambda T) N [(lambda h)^6/180]+O(h^6). This proves the positive scalar limit for nonzero lambda and u0. In the nonvanishing scalar case, H=f^4(1/f)''/2, so the reciprocal-affine classification holds on intervals; on a compact trajectory region inside such an interval, summing the O(h^4) defects yields pathwise order 3.

## originality

PASS

The exact method, expected order-three cancellation and RMS upper order 5/2 are established prior results and are not claimed by the corrected text. The audited contribution is the functional fluctuation law and covariance, an exact positive coefficient establishing sharp scalar RMS order, and the local cancellation classification. The closest sources do not derive these assertions for this method.

## value

PASS

For an existing randomized implicit integrator, the process law gives the temporal error covariance and distinguishes vanishing leading random forcing from generic error. The positive exact asymptotic on a dissipative scalar equation resolves whether the known 5/2 upper order can be improved uniformly over smooth autonomous problems; it is not merely another upper bound or a finite numerical slope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
